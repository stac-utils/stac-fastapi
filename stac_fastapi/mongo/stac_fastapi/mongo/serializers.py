"""Serializers."""
import abc
import json
from datetime import datetime
from typing import TypedDict

import attr
import geoalchemy2 as ga
from stac_pydantic.shared import DATETIME_RFC339

from stac_fastapi.sqlalchemy.models import database
from stac_fastapi.types import stac as stac_types
from stac_fastapi.types.config import Settings
from stac_fastapi.types.links import CollectionLinks, ItemLinks, resolve_links


@attr.s  # type:ignore
class Serializer(abc.ABC):
    """Defines serialization methods between the API and the data model."""

    @classmethod
    @abc.abstractmethod
    def db_to_stac(cls, db_model: database.BaseModel, base_url: str) -> TypedDict:
        """Transform database model to stac."""
        ...

    @classmethod
    @abc.abstractmethod
    def stac_to_db(
        cls, stac_data: TypedDict, exclude_geometry: bool = False
    ) -> database.BaseModel:
        """Transform stac to database model."""
        ...

    @classmethod
    def row_to_dict(cls, db_model: database.BaseModel):
        """Transform a database model to it's dictionary representation."""
        d = {}
        for column in db_model.__table__.columns:
            value = getattr(db_model, column.name)
            if value:
                d[column.name] = value
        return d


class ItemSerializer(Serializer):
    """Serialization methods for STAC items."""

    @classmethod
    def db_to_stac(cls, item, base_url: str) -> stac_types.Item:
        """Transform database model to stac item."""
        
        item_id = item["id"]
        collection_id = item["collection"]
        item_links = ItemLinks(
            collection_id=collection_id, item_id=item_id, base_url=base_url
        ).create_links()

        original_links = item["links"]
        if original_links:
            item_links += resolve_links(original_links, base_url)

        return stac_types.Item(
            type="Feature",
            stac_version=item["stac_version"],
            stac_extensions=item["stac_extensions"] or [],
            id=item["id"],
            collection=item["collection"],
            geometry=item["geometry"],
            bbox=item["bbox"],
            properties=item["properties"],
            links=item_links,
            assets=item["assets"],
        )

    @classmethod
    def stac_to_db(
        cls, stac_data: TypedDict, exclude_geometry: bool = False
    ) -> database.Item:
        """Transform stac item to database model."""
        indexed_fields = {}
        for field in Settings.get().indexed_fields:
            # Use getattr to accommodate extension namespaces
            field_value = stac_data["properties"][field]
            if field == "datetime":
                field_value = datetime.strptime(field_value, DATETIME_RFC339)
            indexed_fields[field.split(":")[-1]] = field_value

            # TODO: Exclude indexed fields from the properties jsonb field to prevent duplication

            now = datetime.utcnow().strftime(DATETIME_RFC339)
            if "created" not in stac_data["properties"]:
                stac_data["properties"]["created"] = now
            stac_data["properties"]["updated"] = now

        return database.Item(
            id=stac_data["id"],
            collection_id=stac_data["collection"],
            stac_version=stac_data["stac_version"],
            stac_extensions=stac_data.get("stac_extensions"),
            geometry=json.dumps(stac_data["geometry"]),
            bbox=stac_data["bbox"],
            properties=stac_data["properties"],
            assets=stac_data["assets"],
            **indexed_fields,
        )


class CollectionSerializer(Serializer):
    """Serialization methods for STAC collections."""

    @classmethod
    def db_to_stac(cls, collection, base_url: str) -> TypedDict:
        """Transform database model to stac collection."""
        collection_links = CollectionLinks(
            collection_id=collection["id"], base_url=base_url
        ).create_links()

        original_links = collection["links"]
        if original_links:
            collection_links += resolve_links(original_links, base_url)

        return stac_types.Collection(
            type="Collection",
            id=collection["id"],
            stac_extensions=collection["stac_extensions"] or [],
            stac_version=collection["stac_version"],
            title=collection["title"],
            description=collection["description"],
            keywords=collection["keywords"],
            license=collection["license"],
            providers=collection["providers"],
            summaries=collection["summaries"],
            extent=collection["extent"],
            links=collection_links,
        )

    @classmethod
    def stac_to_db(
        cls, stac_data: TypedDict, exclude_geometry: bool = False
    ) -> database.Collection:
        """Transform stac collection to database model."""
        return database.Collection(**dict(stac_data))
