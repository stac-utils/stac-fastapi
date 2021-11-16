# encoding: utf-8
"""Filter Extension."""
from enum import Enum
from typing import Callable, List, Type, Union

import attr
from fastapi import APIRouter, FastAPI
from starlette.responses import JSONResponse, Response

from stac_fastapi.api.models import APIRequest, CollectionUri, EmptyRequest
from stac_fastapi.api.routes import create_async_endpoint, create_sync_endpoint
from stac_fastapi.types.core import AsyncBaseFiltersClient, BaseFiltersClient
from stac_fastapi.types.extension import ApiExtension

from .request import FilterExtensionGetRequest, FilterExtensionPostRequest


class FilterConformanceClasses(str, Enum):
    """Conformance classes for the Filter extension.

    See https://github.com/radiantearth/stac-api-spec/tree/v1.0.0-beta.4/fragments/filter
    """

    FILTER = "https://api.stacspec.org/v1.0.0-beta.4/item-search#filter:filter"
    ITEM_SEARCH_FILTER = (
        "https://api.stacspec.org/v1.0.0-beta.4/item-search#filter:item-search-filter"
    )
    CQL_TEXT = "https://api.stacspec.org/v1.0.0-beta.4/item-search#filter:cql-text"
    CQL_JSON = "https://api.stacspec.org/v1.0.0-beta.4/item-search#filter:cql-json"
    BASIC_CQL = "https://api.stacspec.org/v1.0.0-beta.4/item-search#filter:basic-cql"
    BASIC_SPATIAL_OPERATORS = "https://api.stacspec.org/v1.0.0-beta.4/item-search#filter:basic-spatial-operators"
    BASIC_TEMPORAL_OPERATORS = "https://api.stacspec.org/v1.0.0-beta.4/item-search#filter:basic-temporal-operators"
    ENHANCED_COMPARISON_OPERATORS = "https://api.stacspec.org/v1.0.0-beta.4/item-search#filter:enhanced-comparison-operators"
    ENHANCED_SPATIAL_OPERATORS = "https://api.stacspec.org/v1.0.0-beta.4/item-search#filter:enhanced-spatial-operators"
    ENHANCED_TEMPORAL_OPERATORS = "https://api.stacspec.org/v1.0.0-beta.4/item-search#filter:enhanced-temporal-operators"
    FUNCTIONS = "https://api.stacspec.org/v1.0.0-beta.4/item-search#filter:functions"
    ARITHMETIC = "https://api.stacspec.org/v1.0.0-beta.4/item-search#filter:arithmetic"
    ARRAYS = "https://api.stacspec.org/v1.0.0-beta.4/item-search#filter:arrays"
    QUERYABLE_SECOND_OPERAND = "https://api.stacspec.org/v1.0.0-beta.4/item-search#filter:queryable-second-operand"


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
            FilterConformanceClasses.ITEM_SEARCH_FILTER,
            FilterConformanceClasses.BASIC_CQL,
            FilterConformanceClasses.CQL_TEXT,
        ]
    )
    router: APIRouter = attr.ib(factory=APIRouter)
    response_class: Type[Response] = attr.ib(default=JSONResponse)

    def _create_endpoint(
        self,
        func: Callable,
        request_type: Union[
            Type[APIRequest],
        ],
    ) -> Callable:
        """Create a FastAPI endpoint."""
        if isinstance(self.client, AsyncBaseFiltersClient):
            return create_async_endpoint(
                func, request_type, response_class=self.response_class
            )
        if isinstance(self.client, BaseFiltersClient):
            return create_sync_endpoint(
                func, request_type, response_class=self.response_class
            )
        raise NotImplementedError

    def register(self, app: FastAPI) -> None:
        """Register the extension with a FastAPI application.

        Args:
            app: target FastAPI application.

        Returns:
            None
        """
        self.router.add_api_route(
            name="Queryables",
            path="/queryables",
            methods=["GET"],
            endpoint=self._create_endpoint(self.client.get_queryables, EmptyRequest),
        )
        self.router.add_api_route(
            name="Collection Queryables",
            path="/collections/{collection_id}/queryables",
            methods=["GET"],
            endpoint=self._create_endpoint(self.client.get_queryables, CollectionUri),
        )
        app.include_router(self.router, tags=["Filter Extension"])
