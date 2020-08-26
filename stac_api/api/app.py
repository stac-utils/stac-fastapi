"""fastapi app creation"""

from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from starlette.requests import Request

from stac_api.api.routers import (
    create_core_router,
    create_tiles_router,
    create_transactions_router,
)
from stac_api.clients.postgres.core import CoreCrudClient
from stac_api.clients.postgres.tokens import PaginationTokenClient
from stac_api.clients.postgres.transactions import TransactionsClient
from stac_api.clients.tiles.ogc import TilesClient
from stac_api.config import AddOns, ApiExtensions, ApiSettings, inject_settings
from stac_api.errors import DEFAULT_STATUS_CODES, add_exception_handlers
from stac_api.openapi import config_openapi
from stac_api.resources import conformance, mgmt
from stac_api.utils.dependencies import READER, WRITER


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
