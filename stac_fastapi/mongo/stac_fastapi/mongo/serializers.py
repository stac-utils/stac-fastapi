"""Serializers."""
import abc
from typing import TypedDict

import attr

from stac_fastapi.types import stac as stac_types
from stac_fastapi.types.links import CollectionLinks, ItemLinks, resolve_links


@attr.s  # type:ignore
class Serializer(abc.ABC):
    """Defines serialization methods between the API and the data model."""

    @classmethod
    @abc.abstractmethod
    def db_to_stac(cls, item: dict, base_url: str) -> TypedDict:
        """Transform database model to stac."""
        ...


class ItemSerializer(Serializer):
    """Serialization methods for STAC items."""

    @classmethod
    def db_to_stac(cls, item: dict, base_url: str) -> stac_types.Item:
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


class CollectionSerializer(Serializer):
    """Serialization methods for STAC collections."""

    @classmethod
    def db_to_stac(cls, collection: dict, base_url: str) -> stac_types.Collection:
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
