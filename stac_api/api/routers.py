"""router factory"""
from typing import List

import pkg_resources
from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from stac_api.api.models import (
    CollectionUri,
    EmptyRequest,
    ItemCollectionUri,
    ItemUri,
    SearchGetRequest,
    _create_request_model,
)
from stac_api.api.routes import create_endpoint_from_model, create_endpoint_with_depends
from stac_api.clients.base import BaseCoreClient, BaseTransactionsClient
from stac_api.config import ApiExtensions, ApiSettings
from stac_api.models import schemas
from stac_pydantic import ItemCollection
from stac_pydantic.api import ConformanceClasses, LandingPage


def create_tiles_router() -> APIRouter:
    """Create API router with OGC tiles endpoints"""
    from titiler.endpoints.stac import STACTiler

    template_dir = pkg_resources.resource_filename("titiler", "templates")
    templates = Jinja2Templates(directory=template_dir)

    titiler_router = STACTiler().router

    @titiler_router.get("/viewer", response_class=HTMLResponse)
    def stac_demo(request: Request):
        """STAC Viewer."""
        return templates.TemplateResponse(
            name="stac_index.html",
            context={
                "request": request,
                "tilejson": request.url_for("tilejson"),
                "metadata": request.url_for("info"),
            },
            media_type="text/html",
        )

    # TODO: add titiler exception handlers
    return titiler_router


def create_core_router(client: BaseCoreClient, settings: ApiSettings) -> APIRouter:
    """Create API router with item endpoints"""
    search_request_model = _create_request_model(schemas.STACSearch, settings)
    router = APIRouter()
    router.add_api_route(
        name="Landing Page",
        path="/",
        response_model=LandingPage,
        response_model_exclude_unset=True,
        response_model_exclude_none=True,
        methods=["GET"],
        endpoint=create_endpoint_with_depends(client.landing_page, EmptyRequest),
    )
    router.add_api_route(
        name="Conformance Classes",
        path="/conformance",
        response_model=ConformanceClasses,
        response_model_exclude_unset=True,
        response_model_exclude_none=True,
        methods=["GET"],
        endpoint=create_endpoint_with_depends(client.conformance, EmptyRequest),
    )
    router.add_api_route(
        name="Get Item",
        path="/collections/{collectionId}/items/{itemId}",
        response_model=schemas.Item,
        response_model_exclude_unset=True,
        response_model_exclude_none=True,
        methods=["GET"],
        endpoint=create_endpoint_with_depends(client.get_item, ItemUri),
    )
    router.add_api_route(
        name="Search",
        path="/search",
        response_model=None
        if settings.api_extension_is_enabled(ApiExtensions.fields)
        else ItemCollection,
        response_model_exclude_unset=True,
        response_model_exclude_none=True,
        methods=["POST"],
        endpoint=create_endpoint_from_model(client.post_search, search_request_model),
    ),
    router.add_api_route(
        name="Search",
        path="/search",
        response_model=None
        if settings.api_extension_is_enabled(ApiExtensions.fields)
        else ItemCollection,
        response_model_exclude_unset=True,
        response_model_exclude_none=True,
        methods=["GET"],
        endpoint=create_endpoint_with_depends(client.get_search, SearchGetRequest),
    )
    router.add_api_route(
        name="Get Collections",
        path="/collections",
        response_model=List[schemas.Collection],
        response_model_exclude_unset=True,
        response_model_exclude_none=True,
        methods=["GET"],
        endpoint=create_endpoint_with_depends(client.all_collections, EmptyRequest),
    )
    router.add_api_route(
        name="Get Collection",
        path="/collections/{collectionId}",
        response_model=schemas.Collection,
        response_model_exclude_unset=True,
        response_model_exclude_none=True,
        methods=["GET"],
        endpoint=create_endpoint_with_depends(client.get_collection, CollectionUri),
    )
    router.add_api_route(
        name="Get ItemCollection",
        path="/collections/{collectionId}/items",
        response_model=ItemCollection,
        response_model_exclude_unset=True,
        response_model_exclude_none=True,
        methods=["GET"],
        endpoint=create_endpoint_with_depends(
            client.item_collection, ItemCollectionUri
        ),
    )
    return router


def create_transactions_router(
    client: BaseTransactionsClient, settings: ApiSettings
) -> APIRouter:
    """Create API router for transactions extension"""
    item_request_model = _create_request_model(schemas.Item, settings)
    collection_request_model = _create_request_model(schemas.Collection, settings)
    router = APIRouter()
    router.add_api_route(
        name="Create Item",
        path="/collections/{collectionId}/items",
        response_model=schemas.Item,
        response_model_exclude_unset=True,
        response_model_exclude_none=True,
        methods=["POST"],
        endpoint=create_endpoint_from_model(client.create_item, item_request_model),
    )
    router.add_api_route(
        name="Update Item",
        path="/collections/{collectionId}/items",
        response_model=schemas.Item,
        response_model_exclude_unset=True,
        response_model_exclude_none=True,
        methods=["PUT"],
        endpoint=create_endpoint_from_model(client.update_item, item_request_model),
    )
    router.add_api_route(
        name="Delete Item",
        path="/collections/{collectionId}/items/{itemId}",
        response_model=schemas.Item,
        response_model_exclude_unset=True,
        response_model_exclude_none=True,
        methods=["DELETE"],
        endpoint=create_endpoint_with_depends(client.delete_item, ItemUri),
    )
    router.add_api_route(
        name="Create Collection",
        path="/collections",
        response_model=schemas.Collection,
        response_model_exclude_unset=True,
        response_model_exclude_none=True,
        methods=["POST"],
        endpoint=create_endpoint_from_model(
            client.create_collection, collection_request_model
        ),
    )
    router.add_api_route(
        name="Update Collection",
        path="/collections",
        response_model=schemas.Collection,
        response_model_exclude_unset=True,
        response_model_exclude_none=True,
        methods=["PUT"],
        endpoint=create_endpoint_from_model(
            client.update_collection, collection_request_model
        ),
    )
    router.add_api_route(
        name="Delete Collection",
        path="/collections/{collectionId}",
        response_model=schemas.Collection,
        response_model_exclude_unset=True,
        response_model_exclude_none=True,
        methods=["DELETE"],
        endpoint=create_endpoint_with_depends(client.delete_collection, CollectionUri),
    )
    return router
