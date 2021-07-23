"""Model serialization."""
import json
from typing import Any, Dict, List, Union
from urllib.parse import urljoin

import geoalchemy2 as ga
from pydantic import BaseModel
from pydantic.utils import GetterDict
from stac_pydantic.shared import DATETIME_RFC339

from stac_fastapi.types.config import Settings
from stac_fastapi.types.errors import DatabaseError
from stac_fastapi.types.links import CollectionLinks, ItemLinks, filter_links


def resolve_links(links: list, base_url: str) -> List[Dict]:
    """Convert relative links to absolute links."""
    if isinstance(links[0], BaseModel):
        links = [link.dict() for link in links]
    filtered_links = filter_links(links)
    for link in filtered_links:
        link.update({"href": urljoin(base_url, link["href"])})
    return filtered_links


class ItemGetter(GetterDict):
    """Custom GetterDict.

    Custom GetterDict used internally by pydantic ORM mode when decomposing database model to pydantic model.  This
    object resolves structural differences between the two models, for example:
      - relative links stored in the database must be resolved absolute links and inferred links must be added
      - ``datetime`` is defined as its own field in the database but as ``item.properties.datetime`` in the stac spec
      - ``geometry`` can be one of several formats when exported from the database but the STAC item expects geojson
    """

    @staticmethod
    def decode_geom(geom: Union[ga.elements.WKBElement, str, Dict]) -> Dict:
        """Decode geoalchemy type to geojson."""
        if isinstance(geom, ga.elements.WKBElement):
            return json.loads(json.dumps(ga.shape.to_shape(geom).__geo_interface__))
        elif isinstance(geom, str):
            return json.loads(geom)
        elif isinstance(geom, dict):
            return geom
        raise DatabaseError("Received unexpected geometry format from database")

    def __init__(self, obj: Any):
        """Decompose orm model to pydantic model."""
        properties = obj.properties.copy()
        for field in Settings.get().indexed_fields:
            # Use getattr to accommodate extension namespaces
            field_value = getattr(obj, field.split(":")[-1])
            if field == "datetime":
                field_value = field_value.strftime(DATETIME_RFC339)
            properties[field] = field_value
        # Create inferred links
        item_links = ItemLinks(
            collection_id=obj.collection_id,
            base_url=obj.base_url,
            item_id=obj.id,
        ).create_links()
        # Resolve existing links
        if obj.links:
            item_links += resolve_links(obj.links, obj.base_url)
        db_model = obj.__class__(
            id=obj.id,
            stac_version=obj.stac_version,
            geometry=self.decode_geom(obj.geometry),
            bbox=obj.bbox,
            properties=properties,
            assets=obj.assets,
            collection_id=obj.collection_id,
            datetime=obj.datetime,
            links=item_links,
            stac_extensions=obj.stac_extensions,
        )
        db_model.type = "Feature"
        db_model.collection = db_model.collection_id
        super().__init__(db_model)


class CollectionGetter(GetterDict):
    """Custom GetterDict.

    Used internally by pydantic ORM mode when collection ORM model to pydantic model
    """

    def __init__(self, obj: Any):
        """Decompose orm model to pydantic model."""
        # Create inferred links
        collection_links = CollectionLinks(
            collection_id=obj.id, base_url=obj.base_url
        ).create_links()
        # Resolve existing links
        if obj.links:
            collection_links += resolve_links(obj.links, obj.base_url)
        # TODO: Fix bug in stac-pydantic (collection root validator) that requires coercing to empty list
        stac_extensions = obj.stac_extensions or []
        db_model = obj.__class__(
            id=obj.id,
            stac_extensions=stac_extensions,
            stac_version=obj.stac_version,
            title=obj.title,
            description=obj.description,
            keywords=obj.keywords,
            license=obj.license,
            providers=obj.providers,
            summaries=obj.summaries,
            extent=obj.extent,
            links=collection_links,
            type="collection",
        )
        super().__init__(db_model)
