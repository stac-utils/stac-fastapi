"""transaction extension."""
from typing import List, Optional, Type, Union

import attr
from fastapi import APIRouter, Body, FastAPI
from stac_pydantic import Collection, Item
from starlette.responses import JSONResponse, Response

from stac_fastapi.api.models import CollectionUri, ItemUri
from stac_fastapi.api.routes import create_async_endpoint
from stac_fastapi.types import stac as stac_types
from stac_fastapi.types.config import ApiSettings
from stac_fastapi.types.core import AsyncBaseTransactionsClient, BaseTransactionsClient
from stac_fastapi.types.extension import ApiExtension


@attr.s
class PostItem(CollectionUri):
    """Create Item."""

    item: stac_types.Item = attr.ib(default=Body(None))


@attr.s
class PutItem(ItemUri):
    """Update Item."""

    item: stac_types.Item = attr.ib(default=Body(None))


@attr.s
class TransactionExtension(ApiExtension):
    """Transaction Extension.

    The transaction extension adds several endpoints which allow the creation, deletion, and updating of items and
    collections:
        POST /collections
        PUT /collections/{collection_id}
        DELETE /collections/{collection_id}
        POST /collections/{collection_id}/items
        PUT /collections/{collection_id}/items
        DELETE /collections/{collection_id}/items

    https://github.com/radiantearth/stac-api-spec/blob/master/ogcapi-features/extensions/transaction/README.md

    Attributes:
        client: CRUD application logic
    """

    client: Union[AsyncBaseTransactionsClient, BaseTransactionsClient] = attr.ib()
    settings: ApiSettings = attr.ib()
    conformance_classes: List[str] = attr.ib(
        factory=lambda: [
            "https://api.stacspec.org/v1.0.0-rc.1/ogcapi-features/extensions/transaction",
            "http://www.opengis.net/spec/ogcapi-features-4/1.0/conf/simpletx",
        ]
    )
    schema_href: Optional[str] = attr.ib(default=None)
    router: APIRouter = attr.ib(factory=APIRouter)
    response_class: Type[Response] = attr.ib(default=JSONResponse)

    def register_create_item(self):
        """Register create item endpoint (POST /collections/{collection_id}/items)."""
        self.router.add_api_route(
            name="Create Item",
            path="/collections/{collection_id}/items",
            response_model=Item if self.settings.enable_response_models else None,
            response_class=self.response_class,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["POST"],
            endpoint=create_async_endpoint(self.client.create_item, PostItem),
        )

    def register_update_item(self):
        """Register update item endpoint (PUT /collections/{collection_id}/items)."""
        self.router.add_api_route(
            name="Update Item",
            path="/collections/{collection_id}/items/{item_id}",
            response_model=Item if self.settings.enable_response_models else None,
            response_class=self.response_class,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["PUT"],
            endpoint=create_async_endpoint(self.client.update_item, PutItem),
        )

    def register_delete_item(self):
        """Register delete item endpoint (DELETE /collections/{collection_id}/items/{item_id})."""
        self.router.add_api_route(
            name="Delete Item",
            path="/collections/{collection_id}/items/{item_id}",
            response_model=Item if self.settings.enable_response_models else None,
            response_class=self.response_class,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["DELETE"],
            endpoint=create_async_endpoint(self.client.delete_item, ItemUri),
        )

    def register_create_collection(self):
        """Register create collection endpoint (POST /collections)."""
        self.router.add_api_route(
            name="Create Collection",
            path="/collections",
            response_model=Collection if self.settings.enable_response_models else None,
            response_class=self.response_class,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["POST"],
            endpoint=create_async_endpoint(
                self.client.create_collection, stac_types.Collection
            ),
        )

    def register_update_collection(self):
        """Register update collection endpoint (PUT /collections)."""
        self.router.add_api_route(
            name="Update Collection",
            path="/collections",
            response_model=Collection if self.settings.enable_response_models else None,
            response_class=self.response_class,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["PUT"],
            endpoint=create_async_endpoint(
                self.client.update_collection, stac_types.Collection
            ),
        )

    def register_delete_collection(self):
        """Register delete collection endpoint (DELETE /collections/{collection_id})."""
        self.router.add_api_route(
            name="Delete Collection",
            path="/collections/{collection_id}",
            response_model=Collection if self.settings.enable_response_models else None,
            response_class=self.response_class,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["DELETE"],
            endpoint=create_async_endpoint(
                self.client.delete_collection, CollectionUri
            ),
        )

    def register(self, app: FastAPI) -> None:
        """Register the extension with a FastAPI application.

        Args:
            app: target FastAPI application.

        Returns:
            None
        """
        self.router.prefix = app.state.router_prefix
        self.register_create_item()
        self.register_update_item()
        self.register_delete_item()
        self.register_create_collection()
        self.register_update_collection()
        self.register_delete_collection()
        app.include_router(self.router, tags=["Transaction Extension"])
