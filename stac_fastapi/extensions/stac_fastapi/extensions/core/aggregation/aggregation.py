"""Aggregation Extension."""
from enum import Enum
from typing import List, Union

import attr
from fastapi import APIRouter, FastAPI

from stac_fastapi.api.models import CollectionUri, EmptyRequest
from stac_fastapi.api.routes import create_async_endpoint
from stac_fastapi.types.extension import ApiExtension

from .client import AsyncBaseAggregationClient, BaseAggregationClient
from .request import AggregationExtensionGetRequest, AggregationExtensionPostRequest


class AggregationConformanceClasses(str, Enum):
    """Conformance classes for the Aggregation extension.

    See
    https://github.com/stac-api-extensions/aggregation
    """

    AGGREGATION = "https://api.stacspec.org/v0.3.0/aggregation"


@attr.s
class AggregationExtension(ApiExtension):
    """Aggregation Extension.

    The purpose of the Aggregation Extension is to provide an endpoint similar to
    the Search endpoint (/search), but which will provide aggregated information
    on matching Items rather than the Items themselves. This is highly influenced
    by the Elasticsearch and OpenSearch aggregation endpoint, but with a more
    regular structure for responses.

    The Aggregation extension adds several endpoints which allow the retrieval of
    available aggregation fields and aggregation buckets based on a seearch query:
        GET /aggregations
        POST /aggregations
        GET /collections/{collection_id}/aggregations
        POST /collections/{collection_id}/aggregations
        GET /aggregate
        POST /aggregate
        GET /collections/{collection_id}/aggregate
        POST /collections/{collection_id}/aggregate

    https://github.com/stac-api-extensions/aggregation/blob/main/README.md

    Attributes:
        conformance_classes: Conformance classes provided by the extension
    """

    GET = AggregationExtensionGetRequest
    POST = AggregationExtensionPostRequest

    client: Union[AsyncBaseAggregationClient, BaseAggregationClient] = attr.ib(
        factory=BaseAggregationClient
    )

    conformance_classes: List[str] = attr.ib(
        default=[AggregationConformanceClasses.AGGREGATION]
    )
    router: APIRouter = attr.ib(factory=APIRouter)

    def register(self, app: FastAPI) -> None:
        """Register the extension with a FastAPI application.

        Args:
            app: target FastAPI application.

        Returns:
            None
        """
        self.router.prefix = app.state.router_prefix
        self.router.add_api_route(
            name="Aggregations",
            path="/aggregations",
            methods=["GET", "POST"],
            endpoint=create_async_endpoint(self.client.get_aggregations, EmptyRequest),
        )
        self.router.add_api_route(
            name="Collection Aggregations",
            path="/collections/{collection_id}/aggregations",
            methods=["GET", "POST"],
            endpoint=create_async_endpoint(self.client.get_aggregations, CollectionUri),
        )
        self.router.add_api_route(
            name="Aggregate",
            path="/aggregate",
            methods=["GET"],
            endpoint=create_async_endpoint(self.client.aggregate, self.GET),
        )
        self.router.add_api_route(
            name="Aggregate",
            path="/aggregate",
            methods=["POST"],
            endpoint=create_async_endpoint(self.client.aggregate, self.POST),
        )
        self.router.add_api_route(
            name="Collection Aggregate",
            path="/collections/{collection_id}/aggregate",
            methods=["GET"],
            endpoint=create_async_endpoint(self.client.aggregate, self.GET),
        )
        self.router.add_api_route(
            name="Collection Aggregate",
            path="/collections/{collection_id}/aggregate",
            methods=["POST"],
            endpoint=create_async_endpoint(self.client.aggregate, self.POST),
        )
        app.include_router(self.router, tags=["Aggregation Extension"])
