# encoding: utf-8
"""Collection Search Extension."""
from typing import List, Type, Union

import attr
from fastapi import APIRouter, FastAPI
from starlette.responses import JSONResponse, Response

from stac_fastapi.api.routes import create_async_endpoint
from stac_fastapi.types.core import AsyncDiscoverySearchClient, DiscoverySearchClient
from stac_fastapi.types.extension import ApiExtension
from stac_fastapi.types.search import (
    BaseDiscoverySearchGetRequest,
    BaseDiscoverySearchPostRequest,
)

from .request import (
    DiscoverySearchExtensionGetRequest,
    DiscoverySearchExtensionPostRequest,
)


@attr.s
class DiscoverySearchExtension(ApiExtension):
    """DiscoverySearch Extension.

    The collection search extension adds two endpoints which allow searching of
    collections via GET and POST:
        GET /discovery-search
        POST /discovery-search

    https://github.com/stac-api-extensions/collection-search

    Attributes:
        search_get_request_model: Get request model for collection search
        search_post_request_model: Post request model for collection search
        client: Collection Search endpoint logic
        conformance_classes: Conformance classes provided by the extension
    """

    GET = DiscoverySearchExtensionGetRequest
    POST = DiscoverySearchExtensionPostRequest

    discovery_search_get_request_model: Type[BaseDiscoverySearchGetRequest] = attr.ib(
        default=BaseDiscoverySearchGetRequest
    )
    discovery_search_post_request_model: Type[BaseDiscoverySearchPostRequest] = attr.ib(
        default=BaseDiscoverySearchPostRequest
    )

    client: Union[AsyncDiscoverySearchClient, DiscoverySearchClient] = attr.ib(
        factory=DiscoverySearchClient
    )

    conformance_classes: List[str] = attr.ib(default=[])
    router: APIRouter = attr.ib(factory=APIRouter)
    response_class: Type[Response] = attr.ib(default=JSONResponse)

    def register(self, app: FastAPI) -> None:
        """Register the extension with a FastAPI application.

        Args:
            app: target FastAPI application.

        Returns:
            None
        """
        self.router.prefix = app.state.router_prefix
        self.router.add_api_route(
            name="Discovery Search",
            path="/discovery-search",
            response_model=None,
            response_class=self.response_class,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["GET"],
            endpoint=create_async_endpoint(
                self.client.get_discovery_search,
                self.discovery_search_get_request_model,
            ),
        )

        self.router.add_api_route(
            name="Discovery Search",
            path="/discovery-search",
            response_model=None,
            response_class=self.response_class,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["POST"],
            endpoint=create_async_endpoint(
                self.client.post_discovery_search,
                self.discovery_search_post_request_model,
            ),
        )

        app.include_router(self.router, tags=["Discovery Search Extension"])
