# encoding: utf-8
"""Filter Extension."""

from typing import List

import attr
from fastapi import APIRouter, FastAPI

from stac_fastapi.api.models import CollectionUri, EmptyRequest
from stac_fastapi.api.routes import create_endpoint
from stac_fastapi.types.core import BaseFiltersClient
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

    client: BaseFiltersClient = attr.ib()
    conformance_classes: List[str] = attr.ib(
        default=[
            "https://api.stacspec.org/v1.0.0-beta.2/item-search#filter",
            "https://api.stacspec.org/v1.0.0-beta.2/item-search#filter:simple-cql",
            "https://api.stacspec.org/v1.0.0-beta.2/item-search#filter:item-search-filter",
        ]
    )

    def register(self, app: FastAPI) -> None:
        """Register the extension with a FastAPI application.

        Args:
            app: target FastAPI application.

        Returns:
            None
        """
        router = APIRouter()
        router.add_api_route(
            name="Queryables",
            path="/queryables",
            methods=["GET"],
            endpoint=create_endpoint(self.client.get_queryables, EmptyRequest),
        )
        router.add_api_route(
            name="Collection Queryables",
            path="/collections/{collectionId}/queryables",
            methods=["GET"],
            endpoint=create_endpoint(self.client.get_queryables, CollectionUri),
        )
        app.include_router(router, tags=["Filter Extension"])
