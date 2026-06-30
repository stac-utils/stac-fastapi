"""Sort extension."""

from enum import StrEnum
from typing import Any, Optional, Protocol

import attr
from fastapi import APIRouter, FastAPI
from pydantic import BaseModel, Field

from stac_fastapi.api.models import (
    CollectionUri,
    EmptyRequest,
    JSONSchemaResponse,
)
from stac_fastapi.api.routes import create_async_endpoint
from stac_fastapi.types.extension import ApiExtension
from stac_fastapi.types.search import APIRequest

from .request import SortExtensionGetRequest, SortExtensionPostRequest


class SortablesClient(Protocol):
    """Protocol for sortables client methods."""

    def get_sortables(self, **kwargs: Any) -> dict[str, Any]:
        """Get sortables for item search."""
        ...

    def get_collection_sortables(
        self, collection_id: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Get sortables for a specific collection."""
        ...

    def get_collections_sortables(self, **kwargs: Any) -> dict[str, Any]:
        """Get sortables for collection search."""
        ...


class SortablesSchema(BaseModel):
    """Pydantic model for the Sortables JSON Schema response."""

    schema_url: str = Field(
        default="https://json-schema.org/draft/2020-12/schema", alias="$schema"
    )
    id_url: str = Field(alias="$id")
    type: str = "object"
    title: Optional[str] = "Sortables"
    properties: dict[str, Any] = Field(default_factory=dict)
    additionalProperties: bool = True

    model_config = {
        "populate_by_name": True,
        "json_schema_extra": {
            "example": {
                "$schema": "https://json-schema.org/draft/2020-12/schema",
                "$id": "https://example.com/sortables",
                "title": "Sortables",
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "datetime": {"type": "string", "format": "date-time"},
                },
                "additionalProperties": True,
            }
        },
    }


class SortConformanceClasses(StrEnum):
    """Conformance classes for the Sort v1.1.0 extension.

    See https://github.com/stac-api-extensions/sort
    """

    ITEM_SEARCH_SORT = "https://api.stacspec.org/v1.1.0/item-search#sort"
    ITEM_SEARCH_SORTABLES = "https://api.stacspec.org/v1.1.0/item-search#sortables"

    FEATURES_SORT = "https://api.stacspec.org/v1.1.0/ogcapi-features#sort"
    FEATURES_SORTABLES = (
        "http://www.opengis.net/spec/ogcapi-features-5/1.0/conf/sortables"
    )

    COLLECTION_SEARCH_SORT = "https://api.stacspec.org/v1.1.0/collection-search#sort"
    COLLECTION_SEARCH_SORTABLES = (
        "https://api.stacspec.org/v1.1.0/collection-search#sortables"
    )


@attr.s
class SortExtension(ApiExtension):
    """Sort Extension.

    The Sort extension adds the `sortby` parameter to search endpoints and provides
    sortables endpoints for discovering available sort fields.
    https://github.com/stac-api-extensions/sort
    """

    GET: type[APIRequest] = SortExtensionGetRequest
    POST: type[BaseModel] = SortExtensionPostRequest
    client: SortablesClient | None = attr.ib(default=None)
    router: APIRouter = attr.ib(
        factory=lambda: APIRouter(default_response_class=JSONSchemaResponse)
    )

    conformance_classes: list[str] = attr.ib(
        factory=lambda: [
            SortConformanceClasses.ITEM_SEARCH_SORT,
            SortConformanceClasses.ITEM_SEARCH_SORTABLES,
            SortConformanceClasses.FEATURES_SORT,
            SortConformanceClasses.FEATURES_SORTABLES,
            SortConformanceClasses.COLLECTION_SEARCH_SORT,
            SortConformanceClasses.COLLECTION_SEARCH_SORTABLES,
        ]
    )

    def __attrs_post_init__(self):
        """Dynamically remove sortables conformance URIs if no client is provided.

        Only removes sortables classes if the conformance_classes are the default
        factory values. If the user explicitly provided conformance_classes,
        we respect their choice.
        """
        if self.client is None:
            # Check if any sortables conformance classes are present
            # If so, remove them since we can't serve sortables without a client
            # This applies to both the base class and subclasses
            self.conformance_classes = [
                c for c in self.conformance_classes if "sortables" not in c
            ]

    def register(self, app: FastAPI) -> None:
        """Register the extension with a FastAPI application.

        Args:
            app: target FastAPI application.

        Returns:
            None
        """
        if self.client is None:
            return

        self.router.prefix = app.state.router_prefix

        self.router.add_api_route(
            name="Sortables",
            path="/sortables",
            methods=["GET"],
            response_model=SortablesSchema,
            response_model_exclude_none=True,
            endpoint=create_async_endpoint(self.client.get_sortables, EmptyRequest),
        )

        self.router.add_api_route(
            name="Collection Sortables",
            path="/collections/{collection_id}/sortables",
            methods=["GET"],
            response_model=SortablesSchema,
            response_model_exclude_none=True,
            endpoint=create_async_endpoint(
                self.client.get_collection_sortables, CollectionUri
            ),
        )

        self.router.add_api_route(
            name="Collections Catalog Sortables",
            path="/collections-sortables",
            methods=["GET"],
            response_model=SortablesSchema,
            response_model_exclude_none=True,
            endpoint=create_async_endpoint(
                self.client.get_collections_sortables, EmptyRequest
            ),
        )

        app.include_router(self.router, tags=["Sort Extension"])


@attr.s
class SearchSortExtension(SortExtension):
    """Item Search Sort Extension.

    Provides sort capabilities for the `/search` endpoint.
    """

    conformance_classes: list[str] = attr.ib(
        factory=lambda: [
            SortConformanceClasses.ITEM_SEARCH_SORT,
            SortConformanceClasses.ITEM_SEARCH_SORTABLES,
        ]
    )

    def register(self, app: FastAPI) -> None:
        """Register the extension with a FastAPI application.

        Args:
            app: target FastAPI application.

        Returns:
            None
        """
        if self.client is None:
            return

        self.router.prefix = app.state.router_prefix

        self.router.add_api_route(
            name="Sortables",
            path="/sortables",
            methods=["GET"],
            response_model=SortablesSchema,
            response_model_exclude_none=True,
            endpoint=create_async_endpoint(self.client.get_sortables, EmptyRequest),
        )

        app.include_router(self.router, tags=["Sort Extension"])


@attr.s
class ItemCollectionSortExtension(SortExtension):
    """Item Collection Sort Extension.

    Provides sort capabilities for the `/collections/{id}/items` endpoint.
    """

    conformance_classes: list[str] = attr.ib(
        factory=lambda: [
            SortConformanceClasses.FEATURES_SORT,
            SortConformanceClasses.FEATURES_SORTABLES,
        ]
    )

    def register(self, app: FastAPI) -> None:
        """Register the extension with a FastAPI application.

        Args:
            app: target FastAPI application.

        Returns:
            None
        """
        if self.client is None:
            return

        self.router.prefix = app.state.router_prefix

        self.router.add_api_route(
            name="Collection Sortables",
            path="/collections/{collection_id}/sortables",
            methods=["GET"],
            response_model=SortablesSchema,
            response_model_exclude_none=True,
            endpoint=create_async_endpoint(
                self.client.get_collection_sortables, CollectionUri
            ),
        )

        app.include_router(self.router, tags=["Sort Extension"])


@attr.s
class CollectionSearchSortExtension(SortExtension):
    """Collection Search Sort Extension.

    Provides sort capabilities for the `/collections` endpoint.
    """

    conformance_classes: list[str] = attr.ib(
        factory=lambda: [
            SortConformanceClasses.COLLECTION_SEARCH_SORT,
            SortConformanceClasses.COLLECTION_SEARCH_SORTABLES,
        ]
    )

    def register(self, app: FastAPI) -> None:
        """Register the extension with a FastAPI application.

        Args:
            app: target FastAPI application.

        Returns:
            None
        """
        if self.client is None:
            return

        self.router.prefix = app.state.router_prefix

        self.router.add_api_route(
            name="Collections Catalog Sortables",
            path="/collections-sortables",
            methods=["GET"],
            response_model=SortablesSchema,
            response_model_exclude_none=True,
            endpoint=create_async_endpoint(
                self.client.get_collections_sortables, EmptyRequest
            ),
        )

        app.include_router(self.router, tags=["Sort Extension"])
