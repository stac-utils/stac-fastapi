"""transaction extension."""
import attr
from fastapi import APIRouter, FastAPI
from stac_pydantic import Collection, Item

from stac_fastapi.api.models import CollectionUri, ItemUri, _create_request_model
from stac_fastapi.api.routes import create_endpoint
from stac_fastapi.types.core import BaseTransactionsClient
from stac_fastapi.types.extension import ApiExtension


@attr.s
class TransactionExtension(ApiExtension):
    """Transaction Extension.

    The transaction extension adds several endpoints which allow the creation, deletion, and updating of items and
    collections:
        POST /collections
        PUT /collections/{collectionId}
        DELETE /collections/{collectionId}
        POST /collections/{collectionId}/items
        PUT /collections/{collectionId}/items
        DELETE /collections/{collectionId}/items

    https://github.com/radiantearth/stac-api-spec/blob/master/ogcapi-features/extensions/transaction/README.md

    Attributes:
        client: CRUD application logic
    """

    client: BaseTransactionsClient = attr.ib()

    def register(self, app: FastAPI) -> None:
        """Register the extension with a FastAPI application.

        Args:
            app: target FastAPI application.

        Returns:
            None
        """
        item_request_model = _create_request_model(Item)
        collection_request_model = _create_request_model(Collection)

        router = APIRouter()
        router.add_api_route(
            name="Create Item",
            path="/collections/{collectionId}/items",
            response_model=Item,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["POST"],
            endpoint=create_endpoint(self.client.create_item, item_request_model),
        )
        router.add_api_route(
            name="Update Item",
            path="/collections/{collectionId}/items",
            response_model=Item,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["PUT"],
            endpoint=create_endpoint(self.client.update_item, item_request_model),
        )
        router.add_api_route(
            name="Delete Item",
            path="/collections/{collectionId}/items/{itemId}",
            response_model=Item,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["DELETE"],
            endpoint=create_endpoint(self.client.delete_item, ItemUri),
        )
        router.add_api_route(
            name="Create Collection",
            path="/collections",
            response_model=Collection,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["POST"],
            endpoint=create_endpoint(
                self.client.create_collection, collection_request_model
            ),
        )
        router.add_api_route(
            name="Update Collection",
            path="/collections",
            response_model=Collection,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["PUT"],
            endpoint=create_endpoint(
                self.client.update_collection, collection_request_model
            ),
        )
        router.add_api_route(
            name="Delete Collection",
            path="/collections/{collectionId}",
            response_model=Collection,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["DELETE"],
            endpoint=create_endpoint(self.client.delete_collection, CollectionUri),
        )
        app.include_router(router, tags=["Transaction Extension"])
