# encoding: utf-8
"""Collection Search Extension."""
from enum import Enum
from typing import List, Type, Union

import attr
from fastapi import APIRouter, FastAPI
from starlette.responses import JSONResponse, Response
from stac_pydantic.api.collections import Collections

from stac_fastapi.api.models import JSONSchemaResponse
from stac_fastapi.api.routes import create_async_endpoint
from stac_fastapi.types.core import AsyncCollectionSearchClient, CollectionSearchClient
from stac_fastapi.types.extension import ApiExtension
from stac_fastapi.types.search import BaseCollectionSearchGetRequest, BaseCollectionSearchPostRequest

from .request import CollectionSearchExtensionGetRequest, CollectionSearchExtensionPostRequest

class CollectionSearchConformanceClasses(str, Enum):
    """Conformance classes for the Collection Search extension.

    See
    https://github.com/stac-api-extensions/collection-search
    """

    CORE = "https://api.stacspec.org/v1.0.0-rc.1/core"
    COLLECTION_SEARCH = "https://api.stacspec.org/v1.0.0-rc.1/collection-search"
    SIMPLE_QUERY = "http://www.opengis.net/spec/ogcapi-common-2/1.0/conf/simple-query"

@attr.s
class CollectionSearchExtension(ApiExtension):
    """CollectionSearch Extension.

    The collection search extension adds two endpoints which allow searching of 
    collections via GET and POST:
        GET /collection-search
        POST /collection-search

    https://github.com/stac-api-extensions/collection-search

    Attributes:
        search_get_request_model: Get request model for collection search
        search_post_request_model: Post request model for collection search
        client: Collection Search endpoint logic
        conformance_classes: Conformance classes provided by the extension
    """
    
    GET = CollectionSearchExtensionGetRequest
    POST = CollectionSearchExtensionPostRequest

    collection_search_get_request_model: Type[BaseCollectionSearchGetRequest] = attr.ib(
        default=BaseCollectionSearchGetRequest
    )
    collection_search_post_request_model: Type[BaseCollectionSearchPostRequest] = attr.ib(
        default=BaseCollectionSearchPostRequest
    )
    
    client: Union[AsyncCollectionSearchClient, CollectionSearchClient] = attr.ib(
        factory=CollectionSearchClient
    )
    
    conformance_classes: List[str] = attr.ib(
        default=[
            CollectionSearchConformanceClasses.CORE,
            CollectionSearchConformanceClasses.COLLECTION_SEARCH,
            CollectionSearchConformanceClasses.SIMPLE_QUERY,
        ]
    )
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
            name="Collection Search",
            path="/collection-search",
            response_model=None,
            response_class=self.response_class,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["GET"],
            endpoint=create_async_endpoint(
                self.client.get_collection_search, self.collection_search_get_request_model
            ),
        )

        self.router.add_api_route(
            name="Collection Search",
            path="/collection-search",
            response_model=None,
            response_class=self.response_class,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["POST"],
            endpoint=create_async_endpoint(
                self.client.post_collection_search, self.collection_search_post_request_model
            ),
        )

        app.include_router(self.router, tags=["Collection Search Extension"])
