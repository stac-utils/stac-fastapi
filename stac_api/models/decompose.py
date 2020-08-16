import json
from typing import Any, Dict, List, Union
from urllib.parse import urljoin

import geoalchemy2 as ga
from pydantic.utils import GetterDict
from stac_pydantic.item import ItemProperties
from stac_pydantic.shared import DATETIME_RFC339

from .links import CollectionLinks, ItemLinks, filter_links
from ..errors import DatabaseError
from ..settings import settings


def resolve_links(links: list, base_url: str) -> List[Dict]:
    """
    Convert relative links to absolute links using the specified base url.  It would be more appropriate to use a view,
    but SQLAlchemy ORM doesn't support this as far as I know.
    """
    filtered_links = filter_links(links)
    for link in filtered_links:
        link.update({"href": urljoin(base_url, link["href"])})
    return filtered_links


class ItemGetter(GetterDict):
    """
    Custom GetterDict used internally by pydantic ORM mode when decomposing database model to pydantic model.  This
    object resolves structural differences between the two models, for example:
      - relative links stored in the database must be resolved absolute links and inferred links must be added
      - ``datetime`` is defined as its own field in the database but as ``item.properties.datetime`` in the stac spec
      - ``geometry`` can be one of several formats when exported from the database but the STAC item expects geojson
    """

    @staticmethod
    def decode_geom(geom: Union[ga.elements.WKBElement, str, Dict]) -> Dict:
        if isinstance(geom, ga.elements.WKBElement):
            return json.loads(json.dumps(ga.shape.to_shape(geom).__geo_interface__))
        elif isinstance(geom, str):
            return json.loads(geom)
        elif isinstance(geom, dict):
            return geom
        raise DatabaseError("Received unexpected geometry format from database")

    def __init__(self, obj: Any):
        properties = {}
        for field in settings.indexed_fields:
            # Use getattr to accommodate extension namespaces
            field_value = getattr(obj, field.split(":")[-1])
            if field == "datetime":
                field_value = field_value.strftime(DATETIME_RFC339)
            properties[field] = field_value
        obj.properties.update(ItemProperties(**properties))
        # Create inferred links
        item_links = ItemLinks(
            collection_id=obj.collection_id, base_url=obj.base_url, item_id=obj.id
        ).create_links()
        # Resolve existing links
        if obj.links:
            item_links += resolve_links(obj.links, obj.base_url)
        obj.type = "Feature"
        obj.links = item_links
        obj.geometry = self.decode_geom(obj.geometry)
        obj.collection = obj.collection_id
        super().__init__(obj)


class CollectionGetter(GetterDict):
    """
    Custom GetterDict used internally by pydantic ORM mode when collection ORM model to pydantic model
    """

    def __init__(self, obj: Any):
        # Create inferred links
        collection_links = CollectionLinks(
            collection_id=obj.id, base_url=obj.base_url
        ).create_links()
        # Resolve existing links
        if obj.links:
            collection_links += resolve_links(obj.links, obj.base_url)
        obj.links = collection_links
        super().__init__(obj)
