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
from stac_api.clients.tiles.ogc import TilesClient
from stac_api.config import ApiSettings
from stac_api.models import ogc, schemas
from stac_pydantic import ItemCollection


def create_tiles_router(client: TilesClient) -> APIRouter:
    """Create API router with OGC tiles endpoints"""
    from titiler.endpoints.factory import TilerFactory
    from rio_tiler_crs import STACReader

    template_dir = pkg_resources.resource_filename("titiler", "templates")
    templates = Jinja2Templates(directory=template_dir)

    router = APIRouter()
    router.add_api_route(
        name="Get OGC Tiles Resource",
        path="/collections/{collectionId}/items/{itemId}/tiles",
        response_model=ogc.TileSetResource,
        response_model_exclude_none=True,
        response_model_exclude_unset=True,
        methods=["GET"],
        endpoint=create_endpoint_with_depends(client.get_item_tiles, ItemUri),
        tags=["OGC Tiles"],
    )

    titiler_router = TilerFactory(reader=STACReader, add_asset_deps=True).router
    for route in titiler_router.routes:
        route.tags = []

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

    router.include_router(titiler_router, tags=["Titiler"])
    # TODO: add titiler exception handlers
    return router


def create_core_router(client: BaseCoreClient, settings: ApiSettings) -> APIRouter:
    """Create API router with item endpoints"""
    search_request_model = _create_request_model(schemas.STACSearch, settings)
    router = APIRouter()
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
        response_model=ItemCollection,
        response_model_exclude_unset=True,
        response_model_exclude_none=True,
        methods=["POST"],
        endpoint=create_endpoint_from_model(client.post_search, search_request_model),
    ),
    router.add_api_route(
        name="Search",
        path="/search",
        response_model=ItemCollection,
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
