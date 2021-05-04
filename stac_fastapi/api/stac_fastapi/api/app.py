"""fastapi app creation."""
from typing import Any, Dict, List, Optional, Type

import attr
from fastapi import APIRouter, FastAPI
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.openapi.utils import get_openapi
from stac_pydantic import Collection, Item, ItemCollection
from stac_pydantic.api import ConformanceClasses, LandingPage

from stac_fastapi.api.errors import DEFAULT_STATUS_CODES, add_exception_handlers
from stac_fastapi.api.models import (
    CollectionUri,
    EmptyRequest,
    ItemCollectionUri,
    ItemUri,
    SearchGetRequest,
    _create_request_model,
)
from stac_fastapi.api.routes import create_endpoint

# TODO: make this module not depend on `stac_fastapi.extensions`
from stac_fastapi.extensions.core import FieldsExtension
from stac_fastapi.types.config import ApiSettings, Settings
from stac_fastapi.types.core import BaseCoreClient
from stac_fastapi.types.extension import ApiExtension
from stac_fastapi.types.search import STACSearch


@attr.s
class StacApi:
    """StacApi factory.

    Factory for creating a STAC-compliant FastAPI application.  After instantation, the application is accessible from
    the `StacApi.app` attribute.

    Attributes:
        settings:
            API settings and configuration, potentially using environment variables.
            See https://pydantic-docs.helpmanual.io/usage/settings/.
        client:
            A subclass of `stac_api.clients.BaseCoreClient`.  Defines the application logic which is injected
            into the API.
        extensions:
            API extensions to include with the application.  This may include official STAC extensions as well as
            third-party add ons.
        exceptions:
            Defines a global mapping between exceptions and status codes, allowing configuration of response behavior on
            certain exceptions (https://fastapi.tiangolo.com/tutorial/handling-errors/#install-custom-exception-handlers).
        app:
            The FastAPI application, defaults to a fresh application.
    """

    settings: ApiSettings = attr.ib()
    client: BaseCoreClient = attr.ib()
    extensions: List[ApiExtension] = attr.ib(default=attr.Factory(list))
    exceptions: Dict[Type[Exception], int] = attr.ib(
        default=attr.Factory(lambda: DEFAULT_STATUS_CODES)
    )
    app: FastAPI = attr.ib(default=attr.Factory(FastAPI))

    def get_extension(self, extension: Type[ApiExtension]) -> Optional[ApiExtension]:
        """Get an extension.

        Args:
            extension: extension to check for.

        Returns:
            The extension instance, if it exists.
        """
        for ext in self.extensions:
            if isinstance(ext, extension):
                return ext
        return None

    def register_core(self):
        """Register core STAC endpoints.

            GET /
            GET /conformance
            GET /collections
            GET /collections/{collectionId}
            GET /collections/{collectionId}/items
            GET /collection/{collectionId}/items/{itemId}
            GET /search
            POST /search

        Injects application logic (StacApi.client) into the API layer.

        Returns:
            None
        """
        search_request_model = _create_request_model(STACSearch)
        fields_ext = self.get_extension(FieldsExtension)
        router = APIRouter()
        router.add_api_route(
            name="Landing Page",
            path="/",
            response_model=LandingPage,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["GET"],
            endpoint=create_endpoint(self.client.landing_page, EmptyRequest),
        )
        router.add_api_route(
            name="Conformance Classes",
            path="/conformance",
            response_model=ConformanceClasses,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["GET"],
            endpoint=create_endpoint(self.client.conformance, EmptyRequest),
        )
        router.add_api_route(
            name="Get Item",
            path="/collections/{collectionId}/items/{itemId}",
            response_model=Item,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["GET"],
            endpoint=create_endpoint(self.client.get_item, ItemUri),
        )
        router.add_api_route(
            name="Search",
            path="/search",
            response_model=ItemCollection if not fields_ext else None,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["POST"],
            endpoint=create_endpoint(self.client.post_search, search_request_model),
        ),
        router.add_api_route(
            name="Search",
            path="/search",
            response_model=ItemCollection if not fields_ext else None,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["GET"],
            endpoint=create_endpoint(self.client.get_search, SearchGetRequest),
        )
        router.add_api_route(
            name="Get Collections",
            path="/collections",
            response_model=List[Collection],
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["GET"],
            endpoint=create_endpoint(self.client.all_collections, EmptyRequest),
        )
        router.add_api_route(
            name="Get Collection",
            path="/collections/{collectionId}",
            response_model=Collection,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["GET"],
            endpoint=create_endpoint(self.client.get_collection, CollectionUri),
        )
        router.add_api_route(
            name="Get ItemCollection",
            path="/collections/{collectionId}/items",
            response_model=ItemCollection,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["GET"],
            endpoint=create_endpoint(self.client.item_collection, ItemCollectionUri),
        )
        self.app.include_router(router)

    def customize_openapi(self) -> Optional[Dict[str, Any]]:
        """Customize openapi schema."""
        if self.app.openapi_schema:
            return self.app.openapi_schema

        # TODO: parametrize
        openapi_schema = get_openapi(
            title="STAC FastAPI", version="0.1", routes=self.app.routes
        )

        self.app.openapi_schema = openapi_schema
        return self.app.openapi_schema

    def add_health_check(self):
        """Add a health check."""
        mgmt_router = APIRouter()

        @mgmt_router.get("/_mgmt/ping")
        async def ping():
            """Liveliness/readiness probe."""
            return {"message": "PONG"}

        self.app.include_router(mgmt_router, tags=["Liveliness/Readiness"])

    def __attrs_post_init__(self):
        """Post-init hook.

        Responsible for setting up the application upon instantiation of the class.

        Returns:
            None
        """
        # inject settings
        self.client.extensions = self.extensions

        fields_ext = self.get_extension(FieldsExtension)
        if fields_ext:
            self.settings.default_includes = fields_ext.default_includes

        Settings.set(self.settings)

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

        # add gzip middleware
        self.app.add_middleware(GZipMiddleware)
