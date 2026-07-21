"""Sort extension."""

import warnings
from enum import EnumMeta, StrEnum
from typing import Any

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

from .client import AsyncBaseSortablesClient, BaseSortablesClient
from .request import SortExtensionGetRequest, SortExtensionPostRequest


class SortablesSchema(BaseModel):
    """Pydantic model for the Sortables JSON Schema response."""

    schema_url: str = Field(
        default="https://json-schema.org/draft/2020-12/schema", alias="$schema"
    )
    id_url: str = Field(alias="$id")
    type: str = "object"
    title: str | None = "Sortables"
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


class _DeprecatedMemberMeta(EnumMeta):
    """TODO: Remove this metaclass in 7.0.0."""

    def __getattr__(cls, name: str):
        match name:
            case "COLLECTIONS":
                warnings.warn(
                    "'COLLECTIONS' will be removed in a future version, "
                    "use 'COLLECTION_SEARCH_SORT' instead.",
                    DeprecationWarning,
                    stacklevel=2,
                )
                return cls.COLLECTION_SEARCH_SORT
            case "ITEMS":
                warnings.warn(
                    "'ITEMS' will be removed in a future version, "
                    "use 'FEATURES_SORT' instead.",
                    DeprecationWarning,
                    stacklevel=2,
                )
                return cls.FEATURES_SORT
            case "SEARCH":
                warnings.warn(
                    "'SEARCH' will be removed in a future version, "
                    "use 'ITEM_SEARCH_SORT' instead.",
                    DeprecationWarning,
                    stacklevel=2,
                )
                return cls.ITEM_SEARCH_SORT

        raise AttributeError(f"'{cls.__name__}' has no attribute '{name}'")

    def __getitem__(cls, name: str):
        match name:
            case "COLLECTIONS":
                warnings.warn(
                    "'COLLECTIONS' will be removed in a future version, "
                    "use 'COLLECTION_SEARCH_SORT' instead.",
                    DeprecationWarning,
                    stacklevel=2,
                )
                return cls.COLLECTION_SEARCH_SORT
            case "ITEMS":
                warnings.warn(
                    "'ITEMS' will be removed in a future version, "
                    "use 'FEATURES_SORT' instead.",
                    DeprecationWarning,
                    stacklevel=2,
                )
                return cls.FEATURES_SORT
            case "SEARCH":
                warnings.warn(
                    "'SEARCH' will be removed in a future version, "
                    "use 'ITEM_SEARCH_SORT' instead.",
                    DeprecationWarning,
                    stacklevel=2,
                )
                return cls.ITEM_SEARCH_SORT

        return super().__getitem__(name)


class SortConformanceClasses(StrEnum, metaclass=_DeprecatedMemberMeta):
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


SORTABLES_CONFORMANCE_URIS: frozenset[str] = frozenset(
    {
        SortConformanceClasses.ITEM_SEARCH_SORTABLES.value,
        SortConformanceClasses.FEATURES_SORTABLES.value,
        SortConformanceClasses.COLLECTION_SEARCH_SORTABLES.value,
    }
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
    client: AsyncBaseSortablesClient | BaseSortablesClient | None = attr.ib(default=None)
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
        """Remove sortables conformance classes when no client is provided.

        Without a client the sortables endpoints cannot be served, so the
        associated conformance URIs are removed from the advertised list.
        """
        if self.client is None:
            self.conformance_classes = [
                c for c in self.conformance_classes if c not in SORTABLES_CONFORMANCE_URIS
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
