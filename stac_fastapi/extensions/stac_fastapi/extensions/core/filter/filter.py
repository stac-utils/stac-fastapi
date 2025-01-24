# encoding: utf-8
"""Filter Extension."""
from enum import Enum
from typing import List, Type, Union

import attr
from fastapi import APIRouter, FastAPI
from starlette.responses import Response

from stac_fastapi.api.models import CollectionUri, EmptyRequest, JSONSchemaResponse
from stac_fastapi.api.routes import create_async_endpoint
from stac_fastapi.types.extension import ApiExtension

from .client import AsyncBaseFiltersClient, BaseFiltersClient
from .request import FilterExtensionGetRequest, FilterExtensionPostRequest


class FilterConformanceClasses(str, Enum):
    """Conformance classes for the Filter extension.

    See
    https://github.com/stac-api-extensions/filter
    """

    FILTER = "http://www.opengis.net/spec/ogcapi-features-3/1.0/conf/filter"

    SEARCH = "https://api.stacspec.org/v1.0.0-rc.2/item-search#filter"
    ITEMS = "http://www.opengis.net/spec/ogcapi-features-3/1.0/conf/features-filter"
    COLLECTIONS = "https://api.stacspec.org/v1.0.0-rc.1/collection-search#filter"

    CQL2_TEXT = "http://www.opengis.net/spec/cql2/1.0/conf/cql2-text"
    CQL2_JSON = "http://www.opengis.net/spec/cql2/1.0/conf/cql2-json"
    BASIC_CQL2 = "http://www.opengis.net/spec/cql2/1.0/conf/basic-cql2"
    BASIC_SPATIAL_OPERATORS = (
        "http://www.opengis.net/spec/cql2/1.0/conf/basic-spatial-operators"
    )
    TEMPORAL_OPERATORS = " http://www.opengis.net/spec/cql2/1.0/conf/temporal-operators"
    ADVANCED_COMPARISON_OPERATORS = (
        "http://www.opengis.net/spec/cql2/1.0/conf/advanced-comparison-operators"
    )
    SPATIAL_OPERATORS = "http://www.opengis.net/spec/cql2/1.0/conf/spatial-operators"
    FUNCTIONS = "http://www.opengis.net/spec/cql2/1.0/conf/functions"
    ARITHMETIC = "http://www.opengis.net/spec/cql2/1.0/conf/arithmetic"
    ARRAYS = "http://www.opengis.net/spec/cql2/1.0/conf/array-operators"
    PROPERTY_PROPERTY = "http://www.opengis.net/spec/cql2/1.0/conf/property-property"
    ACCENT_CASE_INSENSITIVE_COMPARISON = (
        "http://www.opengis.net/spec/cql2/1.0/conf/accent-case-insensitive-comparison"
    )


@attr.s
class FilterExtension(ApiExtension):
    """Filter Extension.

    The filter extension adds several endpoints which allow the retrieval of
    queryables and provides an expressive mechanism for searching based on Item
    Attributes:
        GET /queryables
        GET /collections/{collection_id}/queryables

    https://github.com/stac-api-extensions/filter/blob/main/README.md

    Attributes:
        client: Queryables endpoint logic
        conformance_classes: Conformance classes provided by the extension
    """

    GET = FilterExtensionGetRequest
    POST = FilterExtensionPostRequest

    client: Union[AsyncBaseFiltersClient, BaseFiltersClient] = attr.ib(
        factory=BaseFiltersClient
    )
    conformance_classes: List[str] = attr.ib(
        default=[
            FilterConformanceClasses.FILTER,
            FilterConformanceClasses.SEARCH,
            FilterConformanceClasses.ITEMS,
            FilterConformanceClasses.BASIC_CQL2,
            FilterConformanceClasses.CQL2_JSON,
            FilterConformanceClasses.CQL2_TEXT,
        ]
    )
    router: APIRouter = attr.ib(factory=APIRouter)
    response_class: Type[Response] = attr.ib(default=JSONSchemaResponse)

    def register(self, app: FastAPI) -> None:
        """Register the extension with a FastAPI application.

        Args:
            app: target FastAPI application.

        Returns:
            None
        """
        self.router.prefix = app.state.router_prefix
        self.router.add_api_route(
            name="Queryables",
            path="/queryables",
            methods=["GET"],
            responses={
                200: {
                    "content": {
                        "application/schema+json": {},
                    },
                    # TODO: add output model in stac-pydantic
                },
            },
            response_class=self.response_class,
            endpoint=create_async_endpoint(self.client.get_queryables, EmptyRequest),
        )
        self.router.add_api_route(
            name="Collection Queryables",
            path="/collections/{collection_id}/queryables",
            methods=["GET"],
            responses={
                200: {
                    "content": {
                        "application/schema+json": {},
                    },
                    # TODO: add output model in stac-pydantic
                },
            },
            response_class=self.response_class,
            endpoint=create_async_endpoint(self.client.get_queryables, CollectionUri),
        )
        app.include_router(self.router, tags=["Filter Extension"])


@attr.s
class SearchFilterExtension(FilterExtension):
    """Item Search Filter Extension."""

    conformance_classes: List[str] = attr.ib(
        default=[
            FilterConformanceClasses.FILTER,
            FilterConformanceClasses.SEARCH,
            FilterConformanceClasses.BASIC_CQL2,
            FilterConformanceClasses.CQL2_JSON,
            FilterConformanceClasses.CQL2_TEXT,
        ]
    )

    def register(self, app: FastAPI) -> None:
        """Register the extension with a FastAPI application.

        Args:
            app: target FastAPI application.

        Returns:
            None
        """
        self.router.prefix = app.state.router_prefix
        self.router.add_api_route(
            name="Queryables",
            path="/queryables",
            methods=["GET"],
            responses={
                200: {
                    "content": {
                        "application/schema+json": {},
                    },
                    # TODO: add output model in stac-pydantic
                },
            },
            response_class=self.response_class,
            endpoint=create_async_endpoint(self.client.get_queryables, EmptyRequest),
        )
        app.include_router(self.router, tags=["Filter Extension"])


@attr.s
class ItemCollectionFilterExtension(FilterExtension):
    """Item Collection Filter Extension."""

    conformance_classes: List[str] = attr.ib(
        default=[
            FilterConformanceClasses.FILTER,
            FilterConformanceClasses.ITEMS,
            FilterConformanceClasses.BASIC_CQL2,
            FilterConformanceClasses.CQL2_JSON,
            FilterConformanceClasses.CQL2_TEXT,
        ]
    )

    def register(self, app: FastAPI) -> None:
        """Register the extension with a FastAPI application.

        Args:
            app: target FastAPI application.

        Returns:
            None
        """
        self.router.add_api_route(
            name="Collection Queryables",
            path="/collections/{collection_id}/queryables",
            methods=["GET"],
            responses={
                200: {
                    "content": {
                        "application/schema+json": {},
                    },
                    # TODO: add output model in stac-pydantic
                },
            },
            response_class=self.response_class,
            endpoint=create_async_endpoint(self.client.get_queryables, CollectionUri),
        )
        app.include_router(self.router, tags=["Filter Extension"])


@attr.s
class CollectionSearchFilterExtension(FilterExtension):
    """Collection Search Filter Extension."""

    conformance_classes: List[str] = attr.ib(
        default=[
            FilterConformanceClasses.FILTER,
            FilterConformanceClasses.COLLECTIONS,
            FilterConformanceClasses.BASIC_CQL2,
            FilterConformanceClasses.CQL2_JSON,
            FilterConformanceClasses.CQL2_TEXT,
        ]
    )

    def register(self, app: FastAPI) -> None:
        """Register the extension with a FastAPI application.

        Args:
            app: target FastAPI application.

        Returns:
            None
        """
        pass
