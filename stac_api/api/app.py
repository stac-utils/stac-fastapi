"""fastapi app creation"""
from typing import Dict, List, Optional, Type

import attr
from fastapi import APIRouter, FastAPI
from fastapi.openapi.utils import get_openapi
from stac_pydantic import ItemCollection
from stac_pydantic.api import ConformanceClasses, LandingPage

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


@attr.s
class StacApi:
    """StacApi"""

    settings: ApiSettings = attr.ib()
    client: BaseCoreClient = attr.ib()
    extensions: List[ApiExtension] = attr.ib(default=attr.Factory(list))
    exceptions: Dict[Type[Exception], int] = attr.ib(
        default=attr.Factory(lambda: DEFAULT_STATUS_CODES)
    )
    app: FastAPI = attr.ib(default=attr.Factory(FastAPI))

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

    def __attrs_post_init__(self):
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

        # customize openapi
        self.app.openapi = self.customize_openapi
