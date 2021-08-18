# encoding: utf-8
"""Filter Extension."""

from typing import Callable, List, Type, Union

import attr
from fastapi import APIRouter, FastAPI
from starlette.responses import JSONResponse, Response

from stac_fastapi.api.models import APIRequest, CollectionUri, EmptyRequest
from stac_fastapi.api.routes import create_sync_endpoint
from stac_fastapi.types.core import AsyncBaseFiltersClient, BaseFiltersClient
from stac_fastapi.types.extension import ApiExtension


@attr.s
class FilterExtension(ApiExtension):
    """Filter Extension.

    The filter extension adds several endpoints which allow the retrieval of queryables and
    provides an expressive mechanism for searching based on Item Attributes:
        GET /queryables
        GET /collections/{collectionId}/queryables

    https://github.com/radiantearth/stac-api-spec/blob/master/fragments/filter/README.md

    Attributes:
        client: Queryables endpoint logic
        conformance_classes: Conformance classes provided by the extension

    """

    client: Union[AsyncBaseFiltersClient, BaseFiltersClient] = attr.ib(
        factory=BaseFiltersClient
    )
    conformance_classes: List[str] = attr.ib(
        default=[
            "https://api.stacspec.org/v1.0.0-beta.2/item-search#filter",
            "https://api.stacspec.org/v1.0.0-beta.2/item-search#filter:simple-cql",
            "https://api.stacspec.org/v1.0.0-beta.2/item-search#filter:item-search-filter",
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
        # TODO
        # if isinstance(self.client, AsyncBaseFiltersClient):
        #     return create_async_endpoint(
        #         func, request_type, response_class=self.response_class
        #     )
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
            path="/collections/{collectionId}/queryables",
            methods=["GET"],
            endpoint=self._create_endpoint(self.client.get_queryables, CollectionUri),
        )
        app.include_router(self.router, tags=["Filter Extension"])
