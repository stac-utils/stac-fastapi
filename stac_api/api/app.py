"""fastapi app creation"""

from fastapi import APIRouter, FastAPI,  Depends, HTTPException, Request, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from starlette.requests import Request

from stac_api.api.models import ItemUri, Login
from stac_api.api.routers import (
    create_core_router,
    create_tiles_router,
    create_transactions_router,
)
from stac_api.api.routes import create_endpoint_with_depends
from stac_api.clients.postgres.core import CoreCrudClient
from stac_api.clients.postgres.tokens import PaginationTokenClient
from stac_api.clients.postgres.transactions import TransactionsClient
from stac_api.clients.tiles.ogc import TilesClient
from stac_api.config import AddOns, ApiExtensions, ApiSettings, inject_settings
from stac_api.errors import DEFAULT_STATUS_CODES, add_exception_handlers
from stac_api.models.ogc import TileSetResource
from stac_api.openapi import config_openapi
from stac_api.utils.cognito import get_tokens
from stac_api.utils.dependencies import READER, WRITER

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


def create_app(settings: ApiSettings) -> FastAPI:
    """Create a FastAPI app"""
    paging_client = PaginationTokenClient()
    core_client = CoreCrudClient(pagination_client=paging_client)

    app = FastAPI()
    inject_settings(settings)

    app.debug = settings.debug
    app.include_router(
        create_core_router(core_client, settings), tags=["Core Endpoints"],
        dependencies=[Depends(oauth2_scheme)]
    )
    add_exception_handlers(app, DEFAULT_STATUS_CODES)

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request,
                                           exc: RequestValidationError):
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content=jsonable_encoder(
                {
                    "detail": exc.errors(),
                    "query_params": request.query_params,
                    "path_params": request.path_params,
                }
            ),
        )

    if settings.api_extension_is_enabled(ApiExtensions.transaction):
        transaction_client = TransactionsClient()
        app.include_router(
            create_transactions_router(transaction_client, settings),
            tags=["Transaction Extension"], dependencies=[Depends(oauth2_scheme)]
        )

    if settings.add_on_is_enabled(AddOns.tiles):
        tiles_client = TilesClient()
        app.add_api_route(
            name="Get OGC Tiles Resource",
            path="/collections/{collectionId}/items/{itemId}/tiles",
            response_model=TileSetResource,
            response_model_exclude_none=True,
            response_model_exclude_unset=True,
            methods=["GET"],
            endpoint=create_endpoint_with_depends(tiles_client.get_item_tiles, ItemUri),
            tags=["OGC Tiles"],
            dependencies=[Depends(oauth2_scheme)]
        )
        app.include_router(create_tiles_router(), prefix="/titiler", tags=["Titiler"], dependencies=[Depends(oauth2_scheme)])

    config_openapi(app)

    @app.on_event("startup")
    async def on_startup():
        """Create database engines and sessions on startup"""
        app.state.ENGINE_READER = create_engine(
            settings.reader_connection_string, echo=settings.debug
        )
        app.state.ENGINE_WRITER = create_engine(
            settings.writer_connection_string, echo=settings.debug
        )
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
        if "titiler" in str(request.url):
            return await call_next(request)
        reader = request.app.state.DB_READER()
        writer = request.app.state.DB_WRITER()
        READER.set(reader)
        WRITER.set(writer)
        resp = await call_next(request)
        reader.close()
        writer.close()
        return resp

    @app.post("/login")
    async def login(body: Login):
        try:
            tokens = await get_tokens(body.username, body.password)

            return tokens
        except Exception as exception:
            raise HTTPException(status_code=400, detail=f"{exception}")

    @app.post("/token")
    async def get_token(form_data: OAuth2PasswordRequestForm = Depends()):
        try:
            username = form_data.username
            password = form_data.password
            tokens = await get_tokens(username, password)
            access_token = tokens["access_token"]

            return {"access_token": access_token, "token_type": "bearer"}
        except Exception as exception:
            raise HTTPException(status_code=400, detail=f"{exception}")

    mgmt_router = APIRouter()

    @mgmt_router.get("/_mgmt/ping")
    async def ping():
        """Liveliness/readiness probe"""
        return {"message": "PONG"}

    app.include_router(mgmt_router, tags=["Liveliness/Readiness"])

    return app
