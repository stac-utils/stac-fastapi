"""Transaction extension."""

from enum import Enum
from typing import List, Optional, Type, Union

import attr
from fastapi import APIRouter, Body, FastAPI
from pydantic import TypeAdapter
from stac_pydantic import Collection, Item, ItemCollection
from stac_pydantic.shared import MimeTypes
from starlette.responses import Response
from typing_extensions import Annotated

from stac_fastapi.api.models import CollectionUri, ItemUri, JSONResponse
from stac_fastapi.api.routes import create_async_endpoint
from stac_fastapi.types.config import ApiSettings
from stac_fastapi.types.extension import ApiExtension

from .client import AsyncBaseTransactionsClient, BaseTransactionsClient
from .request import PartialCollection, PartialItem, PatchOperation


class TransactionConformanceClasses(str, Enum):
    """Conformance classes for the Transaction extension.

    See https://github.com/stac-api-extensions/transaction

    """

    ITEMS = "https://api.stacspec.org/v1.0.0/ogcapi-features/extensions/transaction"
    COLLECTIONS = "https://api.stacspec.org/v1.0.0/collections/extensions/transaction"


@attr.s
class PostItem(CollectionUri):
    """Create Item."""

    item: Annotated[Union[Item, ItemCollection], Body()] = attr.ib(default=None)


@attr.s
class PutItem(ItemUri):
    """Update Item."""

    item: Annotated[Item, Body()] = attr.ib(default=None)


@attr.s
class PatchItem(ItemUri):
    """Patch Item."""

    patch: Annotated[
        Union[PartialItem, List[PatchOperation]],
        Body(),
    ] = attr.ib(default=None)


@attr.s
class PutCollection(CollectionUri):
    """Update Collection."""

    collection: Annotated[Collection, Body()] = attr.ib(default=None)


@attr.s
class PatchCollection(CollectionUri):
    """Patch Collection."""

    patch: Annotated[
        Union[PartialCollection, List[PatchOperation]],
        Body(),
    ] = attr.ib(default=None)


_patch_item_schema = TypeAdapter(List[PatchOperation]).json_schema() | {
    "examples": [
        [
            {
                "op": "add",
                "path": "/properties/foo",
                "value": "bar",
            },
            {
                "op": "replace",
                "path": "/properties/foo",
                "value": "bar",
            },
            {
                "op": "test",
                "path": "/properties/foo",
                "value": "bar",
            },
            {
                "op": "copy",
                "path": "/properties/foo",
                "from": "/properties/bar",
            },
            {
                "op": "move",
                "path": "/properties/foo",
                "from": "/properties/bar",
            },
            {
                "op": "remove",
                "path": "/properties/foo",
            },
        ]
    ]
}
# ref: https://github.com/pydantic/pydantic/issues/889
_patch_item_schema["items"]["anyOf"] = list(_patch_item_schema["$defs"].values())

_patch_collection_schema = TypeAdapter(List[PatchOperation]).json_schema() | {
    "examples": [
        [
            {
                "op": "add",
                "path": "/summeries/foo",
                "value": "bar",
            },
            {
                "op": "replace",
                "path": "/summeries/foo",
                "value": "bar",
            },
            {
                "op": "test",
                "path": "/summeries/foo",
                "value": "bar",
            },
            {
                "op": "copy",
                "path": "/summeries/foo",
                "from": "/summeries/bar",
            },
            {
                "op": "move",
                "path": "/summeries/foo",
                "from": "/summeries/bar",
            },
            {
                "op": "remove",
                "path": "/summeries/foo",
            },
        ]
    ]
}
# ref: https://github.com/pydantic/pydantic/issues/889
_patch_collection_schema["items"]["anyOf"] = list(
    _patch_collection_schema["$defs"].values()
)


@attr.s
class TransactionExtension(ApiExtension):
    """Transaction Extension.

    The transaction extension adds several endpoints which allow the creation,
    deletion, and updating of items and collections:
        POST /collections
        PUT /collections/{collection_id}
        DELETE /collections/{collection_id}
        POST /collections/{collection_id}/items
        PUT /collections/{collection_id}/items
        DELETE /collections/{collection_id}/items

    https://github.com/stac-api-extensions/transaction
    https://github.com/stac-api-extensions/collection-transaction

    Attributes:
        client: CRUD application logic

    """

    client: Union[AsyncBaseTransactionsClient, BaseTransactionsClient] = attr.ib()
    settings: ApiSettings = attr.ib()
    conformance_classes: List[str] = attr.ib(
        factory=lambda: [
            TransactionConformanceClasses.ITEMS,
            TransactionConformanceClasses.COLLECTIONS,
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
            status_code=201,
            response_model=Item if self.settings.enable_response_models else None,
            responses={
                201: {
                    "content": {
                        MimeTypes.geojson.value: {},
                    },
                    "model": Item,
                }
            },
            response_class=self.response_class,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["POST"],
            endpoint=create_async_endpoint(self.client.create_item, PostItem),
        )

    def register_update_item(self):
        """Register update item endpoint (PUT
        /collections/{collection_id}/items/{item_id})."""
        self.router.add_api_route(
            name="Update Item",
            path="/collections/{collection_id}/items/{item_id}",
            response_model=Item if self.settings.enable_response_models else None,
            responses={
                200: {
                    "content": {
                        MimeTypes.geojson.value: {},
                    },
                    "model": Item,
                }
            },
            response_class=self.response_class,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["PUT"],
            endpoint=create_async_endpoint(self.client.update_item, PutItem),
        )

    def register_patch_item(self):
        """Register patch item endpoint (PATCH
        /collections/{collection_id}/items/{item_id})."""
        self.router.add_api_route(
            name="Patch Item",
            path="/collections/{collection_id}/items/{item_id}",
            response_model=Item if self.settings.enable_response_models else None,
            responses={
                200: {
                    "content": {
                        MimeTypes.geojson.value: {},
                    },
                    "model": Item,
                }
            },
            openapi_extra={
                "requestBody": {
                    "content": {
                        "application/json-patch+json": {
                            "schema": _patch_item_schema,
                        },
                        "application/merge-patch+json": {
                            "schema": PartialItem.model_json_schema(),
                        },
                        "application/json": {
                            "schema": PartialItem.model_json_schema(),
                        },
                    },
                    "required": True,
                },
            },
            response_class=self.response_class,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["PATCH"],
            endpoint=create_async_endpoint(
                self.client.patch_item,
                PatchItem,
            ),
        )

    def register_delete_item(self):
        """Register delete item endpoint (DELETE
        /collections/{collection_id}/items/{item_id})."""
        self.router.add_api_route(
            name="Delete Item",
            path="/collections/{collection_id}/items/{item_id}",
            response_model=Item if self.settings.enable_response_models else None,
            responses={
                200: {
                    "content": {
                        MimeTypes.geojson.value: {},
                    },
                    "model": Item,
                }
            },
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
            status_code=201,
            response_model=Collection if self.settings.enable_response_models else None,
            responses={
                201: {
                    "content": {
                        MimeTypes.json.value: {},
                    },
                    "model": Collection,
                }
            },
            response_class=self.response_class,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["POST"],
            endpoint=create_async_endpoint(self.client.create_collection, Collection),
        )

    def register_update_collection(self):
        """Register update collection endpoint (PUT /collections/{collection_id})."""
        self.router.add_api_route(
            name="Update Collection",
            path="/collections/{collection_id}",
            response_model=Collection if self.settings.enable_response_models else None,
            responses={
                200: {
                    "content": {
                        MimeTypes.json.value: {},
                    },
                    "model": Collection,
                }
            },
            response_class=self.response_class,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["PUT"],
            endpoint=create_async_endpoint(self.client.update_collection, PutCollection),
        )

    def register_patch_collection(self):
        """Register patch collection endpoint (PATCH /collections/{collection_id})."""
        self.router.add_api_route(
            name="Patch Collection",
            path="/collections/{collection_id}",
            response_model=Collection if self.settings.enable_response_models else None,
            responses={
                200: {
                    "content": {
                        MimeTypes.geojson.value: {},
                    },
                    "model": Collection,
                }
            },
            openapi_extra={
                "requestBody": {
                    "content": {
                        "application/json-patch+json": {
                            "schema": _patch_collection_schema,
                        },
                        "application/merge-patch+json": {
                            "schema": PartialCollection.model_json_schema(),
                        },
                        "application/json": {
                            "schema": PartialCollection.model_json_schema(),
                        },
                    },
                    "required": True,
                },
            },
            response_class=self.response_class,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["PATCH"],
            endpoint=create_async_endpoint(
                self.client.patch_collection,
                PatchCollection,
            ),
        )

    def register_delete_collection(self):
        """Register delete collection endpoint (DELETE /collections/{collection_id})."""
        self.router.add_api_route(
            name="Delete Collection",
            path="/collections/{collection_id}",
            response_model=Collection if self.settings.enable_response_models else None,
            responses={
                200: {
                    "content": {
                        MimeTypes.json.value: {},
                    },
                    "model": Collection,
                }
            },
            response_class=self.response_class,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["DELETE"],
            endpoint=create_async_endpoint(self.client.delete_collection, CollectionUri),
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
        self.register_patch_item()
        self.register_delete_item()
        self.register_create_collection()
        self.register_update_collection()
        self.register_patch_collection()
        self.register_delete_collection()
        app.include_router(self.router, tags=["Transaction Extension"])
