# encoding: utf-8
"""Filter Extension."""
from enum import Enum
from typing import List, Type, Union

import attr
from fastapi import APIRouter, FastAPI
from starlette.responses import Response

from stac_fastapi.api.models import CollectionUri, EmptyRequest, JSONSchemaResponse
from stac_fastapi.api.routes import create_async_endpoint
from stac_fastapi.types.core import AsyncBaseFiltersClient, BaseFiltersClient
from stac_fastapi.types.extension import ApiExtension

from .request import FilterExtensionGetRequest, FilterExtensionPostRequest


class FilterConformanceClasses(str, Enum):
    """Conformance classes for the Filter extension.

    See https://github.com/radiantearth/stac-api-spec/tree/v1.0.0-rc.1/fragments/filter
    """

    FILTER = "http://www.opengis.net/spec/ogcapi-features-3/1.0/conf/filter"
    FEATURES_FILTER = (
        "http://www.opengis.net/spec/ogcapi-features-3/1.0/conf/features-filter"
    )
    ITEM_SEARCH_FILTER = "https://api.stacspec.org/v1.0.0-rc.1/item-search#filter"
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

    The filter extension adds several endpoints which allow the retrieval of queryables and
    provides an expressive mechanism for searching based on Item Attributes:
        GET /queryables
        GET /collections/{collection_id}/queryables

    https://github.com/radiantearth/stac-api-spec/blob/master/fragments/filter/README.md

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
            FilterConformanceClasses.FEATURES_FILTER,
            FilterConformanceClasses.ITEM_SEARCH_FILTER,
            FilterConformanceClasses.BASIC_CQL2,
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
            endpoint=create_async_endpoint(
                self.client.get_queryables, EmptyRequest, self.response_class
            ),
        )
        self.router.add_api_route(
            name="Collection Queryables",
            path="/collections/{collection_id}/queryables",
            methods=["GET"],
            endpoint=create_async_endpoint(
                self.client.get_queryables, CollectionUri, self.response_class
            ),
        )
        app.include_router(self.router, tags=["Filter Extension"])
