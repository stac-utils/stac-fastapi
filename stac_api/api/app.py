"""fastapi app creation"""
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Type

from fastapi import APIRouter, FastAPI
from fastapi.openapi.utils import get_openapi
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from starlette.requests import Request

from stac_api.api.extensions import FieldsExtension
from stac_api.api.extensions.extension import ApiExtension
from stac_api.api.models import (
    CollectionUri,
    EmptyRequest,
    ItemCollectionUri,
    ItemUri,
    SearchGetRequest,
    _create_request_model,
)
from stac_api.api.routes import create_endpoint_from_model, create_endpoint_with_depends
from stac_api.clients.base import BaseCoreClient
from stac_api.config import ApiSettings, inject_settings
from stac_api.errors import DEFAULT_STATUS_CODES, add_exception_handlers
from stac_api.models import schemas
from stac_api.utils.dependencies import READER, WRITER
from stac_pydantic import ItemCollection
from stac_pydantic.api import ConformanceClasses, LandingPage


@dataclass
class StacApi:
    """StacApi"""

    settings: ApiSettings
    client: BaseCoreClient
    extensions: Optional[List[ApiExtension]] = field(  # type:ignore
        default_factory=list
    )
    exceptions: Dict[Type[Exception], int] = field(
        default_factory=lambda: DEFAULT_STATUS_CODES
    )
    app: FastAPI = FastAPI()

    def get_extension(self, extension: Type[ApiExtension]) -> Optional[ApiExtension]:
        """check if an api extension is enabled"""
        for ext in self.extensions:
            if isinstance(ext, extension):
                return ext
        return None

    def register_core(self):
        """register stac core endpoints"""
        search_request_model = _create_request_model(schemas.STACSearch)
        fields_ext = self.get_extension(FieldsExtension)
        router = APIRouter()
        router.add_api_route(
            name="Landing Page",
            path="/",
            response_model=LandingPage,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["GET"],
            endpoint=create_endpoint_with_depends(
                self.client.landing_page, EmptyRequest
            ),
        )
        router.add_api_route(
            name="Conformance Classes",
            path="/conformance",
            response_model=ConformanceClasses,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["GET"],
            endpoint=create_endpoint_with_depends(
                self.client.conformance, EmptyRequest
            ),
        )
        router.add_api_route(
            name="Get Item",
            path="/collections/{collectionId}/items/{itemId}",
            response_model=schemas.Item,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["GET"],
            endpoint=create_endpoint_with_depends(self.client.get_item, ItemUri),
        )
        router.add_api_route(
            name="Search",
            path="/search",
            response_model=ItemCollection if not fields_ext else None,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["POST"],
            endpoint=create_endpoint_from_model(
                self.client.post_search, search_request_model
            ),
        ),
        router.add_api_route(
            name="Search",
            path="/search",
            response_model=ItemCollection if not fields_ext else None,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["GET"],
            endpoint=create_endpoint_with_depends(
                self.client.get_search, SearchGetRequest
            ),
        )
        router.add_api_route(
            name="Get Collections",
            path="/collections",
            response_model=List[schemas.Collection],
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["GET"],
            endpoint=create_endpoint_with_depends(
                self.client.all_collections, EmptyRequest
            ),
        )
        router.add_api_route(
            name="Get Collection",
            path="/collections/{collectionId}",
            response_model=schemas.Collection,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["GET"],
            endpoint=create_endpoint_with_depends(
                self.client.get_collection, CollectionUri
            ),
        )
        router.add_api_route(
            name="Get ItemCollection",
            path="/collections/{collectionId}/items",
            response_model=ItemCollection,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["GET"],
            endpoint=create_endpoint_with_depends(
                self.client.item_collection, ItemCollectionUri
            ),
        )
        self.app.include_router(router)

    def customize_openapi(self):
        """customize openapi schema"""
        if self.app.openapi_schema:
            return self.app.openapi_schema

        # TODO: parametrize
        openapi_schema = get_openapi(
            title="Arturo STAC API", version="0.1", routes=self.app.routes
        )

        self.app.openapi_schema = openapi_schema
        return self.app.openapi_schema

    def add_health_check(self):
        """add a health check"""
        mgmt_router = APIRouter()

        @mgmt_router.get("/_mgmt/ping")
        async def ping():
            """Liveliness/readiness probe"""
            return {"message": "PONG"}

        self.app.include_router(mgmt_router, tags=["Liveliness/Readiness"])

    def setup_db_connection(self):
        """setup database connection"""

        @self.app.on_event("startup")
        async def on_startup():
            """Create database engines and sessions on startup"""
            self.app.state.ENGINE_READER = create_engine(
                self.settings.reader_connection_string, echo=self.settings.debug
            )
            self.app.state.ENGINE_WRITER = create_engine(
                self.settings.writer_connection_string, echo=self.settings.debug
            )
            self.app.state.DB_READER = sessionmaker(
                autocommit=False, autoflush=False, bind=self.app.state.ENGINE_READER
            )
            self.app.state.DB_WRITER = sessionmaker(
                autocommit=False, autoflush=False, bind=self.app.state.ENGINE_WRITER
            )

        @self.app.on_event("shutdown")
        async def on_shutdown():
            """Dispose of database engines and sessions on app shutdown"""
            self.app.state.ENGINE_READER.dispose()
            self.app.state.ENGINE_WRITER.dispose()

        @self.app.middleware("http")
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

    def __post_init__(self):
        """post-init hook"""
        # inject settings
        self.app.debug = self.settings.debug
        self.client.extensions = self.extensions

        fields_ext = self.get_extension(FieldsExtension)
        if fields_ext:
            self.settings.default_includes = fields_ext.default_includes

        inject_settings(self.settings)

        self.register_core()
        # register extensions
        for ext in self.extensions:
            ext.register(self.app)

        # add health check
        self.add_health_check()

        # register exception handlers
        add_exception_handlers(self.app, status_codes=self.exceptions)

        self.setup_db_connection()

        # customize openapi
        self.app.openapi = self.customize_openapi
