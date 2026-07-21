"""Sort extension clients."""

import abc
from typing import Any

import attr
from starlette.requests import Request


@attr.s
class AsyncBaseSortablesClient(abc.ABC):
    """Defines a pattern for implementing the STAC sort extension sortables endpoints."""

    async def get_sortables(
        self, request: Request | None = None, **kwargs: Any
    ) -> dict[str, Any]:
        """Get the sortables available for item search.

        This base implementation returns a blank sortables schema.
        """
        return {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "$id": "https://example.org/sortables",
            "type": "object",
            "title": "Sortables",
            "properties": {},
        }

    async def get_collection_sortables(
        self, collection_id: str, request: Request | None = None, **kwargs: Any
    ) -> dict[str, Any]:
        """Get the sortables available for a specific collection.

        This base implementation returns a blank sortables schema.
        """
        return {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "$id": f"https://example.org/collections/{collection_id}/sortables",
            "type": "object",
            "title": "Sortables",
            "properties": {},
        }

    async def get_collections_sortables(
        self, request: Request | None = None, **kwargs: Any
    ) -> dict[str, Any]:
        """Get the sortables available for collection search.

        This base implementation returns a blank sortables schema.
        """
        return {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "$id": "https://example.org/collections-sortables",
            "type": "object",
            "title": "Sortables",
            "properties": {},
        }


@attr.s
class BaseSortablesClient(abc.ABC):
    """Defines a pattern for implementing the STAC sort extension sortables endpoints."""

    def get_sortables(
        self, request: Request | None = None, **kwargs: Any
    ) -> dict[str, Any]:
        """Get the sortables available for item search.

        This base implementation returns a blank sortables schema.
        """
        return {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "$id": "https://example.org/sortables",
            "type": "object",
            "title": "Sortables",
            "properties": {},
        }

    def get_collection_sortables(
        self, collection_id: str, request: Request | None = None, **kwargs: Any
    ) -> dict[str, Any]:
        """Get the sortables available for a specific collection.

        This base implementation returns a blank sortables schema.
        """
        return {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "$id": f"https://example.org/collections/{collection_id}/sortables",
            "type": "object",
            "title": "Sortables",
            "properties": {},
        }

    def get_collections_sortables(
        self, request: Request | None = None, **kwargs: Any
    ) -> dict[str, Any]:
        """Get the sortables available for collection search.

        This base implementation returns a blank sortables schema.
        """
        return {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "$id": "https://example.org/collections-sortables",
            "type": "object",
            "title": "Sortables",
            "properties": {},
        }
