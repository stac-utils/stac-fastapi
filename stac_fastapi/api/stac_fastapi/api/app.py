"""fastapi app creation."""
from typing import Any, Dict, List, Optional, Tuple, Type, Union

import attr
from brotli_asgi import BrotliMiddleware
from fastapi import APIRouter, FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.params import Depends
from stac_pydantic import Collection, Item, ItemCollection
from stac_pydantic.api import ConformanceClasses, LandingPage
from stac_pydantic.api.collections import Collections
from stac_pydantic.version import STAC_VERSION
from starlette.responses import JSONResponse, Response

from stac_fastapi.api.errors import DEFAULT_STATUS_CODES, add_exception_handlers
from stac_fastapi.api.middleware import CORSMiddleware, ProxyHeaderMiddleware
from stac_fastapi.api.models import (
    CollectionUri,
    EmptyRequest,
    GeoJSONResponse,
    ItemCollectionUri,
    ItemUri,
    create_request_model,
)
from stac_fastapi.api.openapi import update_openapi
from stac_fastapi.api.routes import Scope, add_route_dependencies, create_async_endpoint

# TODO: make this module not depend on `stac_fastapi.extensions`
from stac_fastapi.extensions.core import FieldsExtension, TokenPaginationExtension
from stac_fastapi.types.config import ApiSettings, Settings
from stac_fastapi.types.core import AsyncBaseCoreClient, BaseCoreClient
from stac_fastapi.types.extension import ApiExtension
from stac_fastapi.types.search import BaseSearchGetRequest, BaseSearchPostRequest


@attr.s
class StacApi:
    """StacApi factory.

    Factory for creating a STAC-compliant FastAPI application.  After instantation, the application is accessible from
    the `StacApi.app` attribute.

    Attributes:
        settings:
            API settings and configuration, potentially using environment variables. See https://pydantic-docs.helpmanual.io/usage/settings/.
        client:
            A subclass of `stac_api.clients.BaseCoreClient`.  Defines the application logic which is injected into the API.
        extensions:
            API extensions to include with the application.  This may include official STAC extensions as well as third-party add ons.
        exceptions:
            Defines a global mapping between exceptions and status codes, allowing configuration of response behavior on certain exceptions (https://fastapi.tiangolo.com/tutorial/handling-errors/#install-custom-exception-handlers).
        app:
            The FastAPI application, defaults to a fresh application.
        route_dependencies (list of tuples of route scope dicts (eg `{'path': '/collections', 'method': 'POST'}`) and list of dependencies (e.g. `[Depends(oauth2_scheme)]`)):
            Applies specified dependencies to specified routes. This is useful for applying custom auth requirements to routes defined elsewhere in the application.
    """

    settings: ApiSettings = attr.ib()
    client: Union[AsyncBaseCoreClient, BaseCoreClient] = attr.ib()
    extensions: List[ApiExtension] = attr.ib(default=attr.Factory(list))
    exceptions: Dict[Type[Exception], int] = attr.ib(
        default=attr.Factory(lambda: DEFAULT_STATUS_CODES)
    )
    app: FastAPI = attr.ib(
        default=attr.Factory(
            lambda self: FastAPI(
                openapi_url=self.settings.openapi_url,
                docs_url=self.settings.docs_url,
                redoc_url=None,
            ),
            takes_self=True,
        ),
        converter=update_openapi,
    )
    router: APIRouter = attr.ib(default=attr.Factory(APIRouter))
    title: str = attr.ib(default="stac-fastapi")
    api_version: str = attr.ib(default="0.1")
    stac_version: str = attr.ib(default=STAC_VERSION)
    description: str = attr.ib(default="stac-fastapi")
    search_get_request_model: Type[BaseSearchGetRequest] = attr.ib(
        default=BaseSearchGetRequest
    )
    search_post_request_model: Type[BaseSearchPostRequest] = attr.ib(
        default=BaseSearchPostRequest
    )
    pagination_extension = attr.ib(default=TokenPaginationExtension)
    response_class: Type[Response] = attr.ib(default=JSONResponse)
    middlewares: List = attr.ib(
        default=attr.Factory(
            lambda: [BrotliMiddleware, CORSMiddleware, ProxyHeaderMiddleware]
        )
    )
    route_dependencies: List[Tuple[List[Scope], List[Depends]]] = attr.ib(default=[])

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

    def register_landing_page(self):
        """Register landing page (GET /).

        Returns:
            None
        """
        self.router.add_api_route(
            name="Landing Page",
            path="/",
            response_model=LandingPage
            if self.settings.enable_response_models
            else None,
            response_class=self.response_class,
            response_model_exclude_unset=False,
            response_model_exclude_none=True,
            methods=["GET"],
            endpoint=create_async_endpoint(
                self.client.landing_page, EmptyRequest, self.response_class
            ),
        )

    def register_conformance_classes(self):
        """Register conformance classes (GET /conformance).

        Returns:
            None
        """
        self.router.add_api_route(
            name="Conformance Classes",
            path="/conformance",
            response_model=ConformanceClasses
            if self.settings.enable_response_models
            else None,
            response_class=self.response_class,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["GET"],
            endpoint=create_async_endpoint(
                self.client.conformance, EmptyRequest, self.response_class
            ),
        )

    def register_get_item(self):
        """Register get item endpoint (GET /collections/{collection_id}/items/{item_id}).

        Returns:
            None
        """
        self.router.add_api_route(
            name="Get Item",
            path="/collections/{collection_id}/items/{item_id}",
            response_model=Item if self.settings.enable_response_models else None,
            response_class=GeoJSONResponse,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["GET"],
            endpoint=create_async_endpoint(
                self.client.get_item, ItemUri, GeoJSONResponse
            ),
        )

    def register_post_search(self):
        """Register search endpoint (POST /search).

        Returns:
            None
        """
        fields_ext = self.get_extension(FieldsExtension)
        self.router.add_api_route(
            name="Search",
            path="/search",
            response_model=(ItemCollection if not fields_ext else None)
            if self.settings.enable_response_models
            else None,
            response_class=GeoJSONResponse,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["POST"],
            endpoint=create_async_endpoint(
                self.client.post_search, self.search_post_request_model, GeoJSONResponse
            ),
        )

    def register_get_search(self):
        """Register search endpoint (GET /search).

        Returns:
            None
        """
        fields_ext = self.get_extension(FieldsExtension)
        self.router.add_api_route(
            name="Search",
            path="/search",
            response_model=(ItemCollection if not fields_ext else None)
            if self.settings.enable_response_models
            else None,
            response_class=GeoJSONResponse,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["GET"],
            endpoint=create_async_endpoint(
                self.client.get_search, self.search_get_request_model, GeoJSONResponse
            ),
        )

    def register_get_collections(self):
        """Register get collections endpoint (GET /collections).

        Returns:
            None
        """
        self.router.add_api_route(
            name="Get Collections",
            path="/collections",
            response_model=Collections
            if self.settings.enable_response_models
            else None,
            response_class=self.response_class,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["GET"],
            endpoint=create_async_endpoint(
                self.client.all_collections, EmptyRequest, self.response_class
            ),
        )

    def register_get_collection(self):
        """Register get collection endpoint (GET /collection/{collection_id}).

        Returns:
            None
        """
        self.router.add_api_route(
            name="Get Collection",
            path="/collections/{collection_id}",
            response_model=Collection if self.settings.enable_response_models else None,
            response_class=self.response_class,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["GET"],
            endpoint=create_async_endpoint(
                self.client.get_collection, CollectionUri, self.response_class
            ),
        )

    def register_get_item_collection(self):
        """Register get item collection endpoint (GET /collection/{collection_id}/items).

        Returns:
            None
        """
        pagination_extension = self.get_extension(self.pagination_extension)
        if pagination_extension is not None:
            mixins = [pagination_extension.GET]
        else:
            mixins = None
        request_model = create_request_model(
            "ItemCollectionURI",
            base_model=ItemCollectionUri,
            mixins=mixins,
        )
        self.router.add_api_route(
            name="Get ItemCollection",
            path="/collections/{collection_id}/items",
            response_model=ItemCollection
            if self.settings.enable_response_models
            else None,
            response_class=GeoJSONResponse,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["GET"],
            endpoint=create_async_endpoint(
                self.client.item_collection, request_model, GeoJSONResponse
            ),
        )

    def register_core(self):
        """Register core STAC endpoints.

            GET /
            GET /conformance
            GET /collections
            GET /collections/{collection_id}
            GET /collections/{collection_id}/items
            GET /collection/{collection_id}/items/{item_id}
            GET /search
            POST /search

        Injects application logic (StacApi.client) into the API layer.

        Returns:
            None
        """
        self.register_landing_page()
        self.register_conformance_classes()
        self.register_get_item()
        self.register_post_search()
        self.register_get_search()
        self.register_get_collections()
        self.register_get_collection()
        self.register_get_item_collection()

    def customize_openapi(self) -> Optional[Dict[str, Any]]:
        """Customize openapi schema."""
        if self.app.openapi_schema:
            return self.app.openapi_schema

        openapi_schema = get_openapi(
            title=self.title,
            version=self.api_version,
            description=self.description,
            routes=self.app.routes,
            servers=self.app.servers,
        )

        self.app.openapi_schema = openapi_schema
        return self.app.openapi_schema

    def add_health_check(self):
        """Add a health check."""
        mgmt_router = APIRouter(prefix=self.app.state.router_prefix)

        @mgmt_router.get("/_mgmt/ping")
        async def ping():
            """Liveliness/readiness probe."""
            return {"message": "PONG"}

        self.app.include_router(mgmt_router, tags=["Liveliness/Readiness"])

    def add_route_dependencies(
        self, scopes: List[Scope], dependencies=List[Depends]
    ) -> None:
        """Add custom dependencies to routes.

        Args:
            scopes: list of scopes. Each scope should be a dict with a `path` and `method` property.
            dependencies: list of [FastAPI dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/) to apply to each scope.

        Returns:
            None
        """
        return add_route_dependencies(self.app.router.routes, scopes, dependencies)

    def __attrs_post_init__(self):
        """Post-init hook.

        Responsible for setting up the application upon instantiation of the class.

        Returns:
            None
        """
        # inject settings
        self.client.extensions = self.extensions
        self.client.stac_version = self.stac_version
        self.client.title = self.title
        self.client.description = self.description

        fields_ext = self.get_extension(FieldsExtension)
        if fields_ext:
            self.settings.default_includes = fields_ext.default_includes

        Settings.set(self.settings)
        self.app.state.settings = self.settings

        # Register core STAC endpoints
        self.register_core()
        self.app.include_router(self.router)

        # keep link to the router prefix value
        router_prefix = self.router.prefix
        self.app.state.router_prefix = router_prefix if router_prefix else ""

        # register extensions
        for ext in self.extensions:
            ext.register(self.app)

        # add health check
        self.add_health_check()

        # register exception handlers
        add_exception_handlers(self.app, status_codes=self.exceptions)

        # customize openapi
        self.app.openapi = self.customize_openapi

        # add middlewares
        for middleware in self.middlewares:
            self.app.add_middleware(middleware)

        # customize route dependencies
        for scopes, dependencies in self.route_dependencies:
            self.add_route_dependencies(scopes=scopes, dependencies=dependencies)
