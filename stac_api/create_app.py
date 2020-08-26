"""fastapi app creation"""
from typing import Callable, List, Type

import pkg_resources
from fastapi import APIRouter, Body, Depends, FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from pydantic import BaseModel, create_model
from pydantic.fields import UndefinedType
from stac_api.clients.base import BaseCoreClient, BaseTransactionsClient
from stac_api.clients.postgres.core import CoreCrudClient
from stac_api.clients.postgres.tokens import PaginationTokenClient
from stac_api.clients.postgres.transactions import TransactionsClient
from stac_api.clients.tiles.ogc import TilesClient
from stac_api.config import AddOns, ApiExtensions, ApiSettings, inject_settings
from stac_api.errors import DEFAULT_STATUS_CODES, add_exception_handlers
from stac_api.models import ogc, schemas
from stac_api.models.api import (
    APIRequest,
    CollectionUri,
    EmptyRequest,
    ItemCollectionUri,
    ItemUri,
    SearchGetRequest,
)
from stac_api.openapi import config_openapi
from stac_api.resources import conformance, mgmt
from stac_api.utils.dependencies import READER, WRITER
from stac_pydantic import ItemCollection


def _create_request_model(
    model: Type[BaseModel], settings: ApiSettings
) -> Type[BaseModel]:
    """Create a pydantic model for validating a request body"""

    fields = {}
    for (k, v) in model.__fields__.items():
        if k == "query":
            if not settings.api_extension_is_enabled(ApiExtensions.query):
                continue

        if k == "sortby":
            if not settings.api_extension_is_enabled(ApiExtensions.sort):
                continue

        if k == "field":
            if not settings.api_extension_is_enabled(ApiExtensions.fields):
                continue

        field_info = v.field_info
        body = Body(
            None
            if isinstance(field_info.default, UndefinedType)
            else field_info.default,
            default_factory=field_info.default_factory,
            alias=field_info.alias,
            alias_priority=field_info.alias_priority,
            title=field_info.title,
            description=field_info.description,
            const=field_info.const,
            gt=field_info.gt,
            ge=field_info.ge,
            lt=field_info.lt,
            le=field_info.le,
            multiple_of=field_info.multiple_of,
            min_items=field_info.min_items,
            max_items=field_info.max_items,
            min_length=field_info.min_length,
            max_length=field_info.max_length,
            regex=field_info.regex,
            extra=field_info.extra,
        )
        fields[k] = (v.outer_type_, body)
    return create_model(model.__name__, **fields, __base__=model)


# TODO: Only use one endpoint factory
def create_endpoint_from_model(
    func: Callable, request_model: Type[BaseModel]
) -> Callable:
    """
    Create a FastAPI endpoint where request model is a pydantic model.  This works best for validating request bodies
    (POST/PUT etc.)
    """

    def _endpoint(
        request: Request, request_data: request_model,  # type:ignore
    ):
        """endpoint"""
        resp = func(request_data, request=request)
        return resp

    return _endpoint


def create_endpoint_with_depends(
    func: Callable, request_model: Type[APIRequest],
) -> Callable:
    """
    Create a fastapi endpoint where request model is a dataclass.  This works best for validating query/patm params.
    """

    def _endpoint(
        request: Request, request_data: request_model = Depends(),  # type:ignore
    ):
        """endpoint"""
        resp = func(
            request=request, **request_data.kwargs()  # type:ignore
        )
        return resp

    return _endpoint


def create_tiles_router(client: TilesClient) -> APIRouter:
    """Create API router with OGC tiles endpoints"""
    # from titiler.endpoints import demo
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


def create_app(settings: ApiSettings) -> FastAPI:
    """Create a FastAPI app"""
    paging_client = PaginationTokenClient()
    core_client = CoreCrudClient(pagination_client=paging_client)

    app = FastAPI()
    inject_settings(settings)

    app.debug = settings.debug
    app.include_router(mgmt.router, tags=["Liveliness/Readiness"])
    app.include_router(conformance.router, tags=["Conformance Classes"])
    app.include_router(
        create_core_router(core_client, settings), tags=["Core Endpoints"]
    )
    add_exception_handlers(app, DEFAULT_STATUS_CODES)

    if settings.api_extension_is_enabled(ApiExtensions.transaction):
        transaction_client = TransactionsClient()
        app.include_router(
            create_transactions_router(transaction_client, settings),
            tags=["Transaction Extension"],
        )

    if settings.add_on_is_enabled(AddOns.tiles):
        tiles_client = TilesClient()
        app.include_router(create_tiles_router(tiles_client))

    config_openapi(app)

    @app.on_event("startup")
    async def on_startup():
        """Create database engines and sessions on startup"""
        app.state.ENGINE_READER = create_engine(settings.reader_connection_string)
        app.state.ENGINE_WRITER = create_engine(settings.writer_connection_string)
        app.state.DB_READER = sessionmaker(
            autocommit=False, autoflush=False, bind=app.state.ENGINE_READER
        )
        app.state.DB_WRITER = sessionmaker(
            autocommit=False, autoflush=False, bind=app.state.ENGINE_WRITER
        )

    @app.on_event("shutdown")
    async def on_shutdown():
        """Dispose of database engines and sessions on app shutdown"""
        app.state.ENGINE_READER.dispose()
        app.state.ENGINE_WRITER.dispose()

    @app.middleware("http")
    async def create_db_connection(request: Request, call_next):
        """Create a new database connection for each request"""
        reader = request.app.state.DB_READER()
        writer = request.app.state.DB_WRITER()
        READER.set(reader)
        WRITER.set(writer)
        resp = await call_next(request)
        reader.close()
        writer.close()
        return resp

    return app
