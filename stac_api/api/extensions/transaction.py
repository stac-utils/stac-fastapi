"""transaction extension."""
import attr
from fastapi import APIRouter, FastAPI

from stac_api.api.extensions.extension import ApiExtension
from stac_api.api.models import CollectionUri, ItemUri, _create_request_model
from stac_api.api.routes import create_endpoint_from_model, create_endpoint_with_depends
from stac_api.clients.base import BaseBulkTransactionsClient, BaseTransactionsClient
from stac_api.models import schemas


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
        item_request_model = _create_request_model(schemas.Item)
        collection_request_model = _create_request_model(schemas.Collection)

        router = APIRouter()
        router.add_api_route(
            name="Create Item",
            path="/collections/{collectionId}/items",
            response_model=schemas.Item,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["POST"],
            endpoint=create_endpoint_from_model(
                self.client.create_item, item_request_model
            ),
        )
        router.add_api_route(
            name="Update Item",
            path="/collections/{collectionId}/items",
            response_model=schemas.Item,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["PUT"],
            endpoint=create_endpoint_from_model(
                self.client.update_item, item_request_model
            ),
        )
        router.add_api_route(
            name="Delete Item",
            path="/collections/{collectionId}/items/{itemId}",
            response_model=schemas.Item,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["DELETE"],
            endpoint=create_endpoint_with_depends(self.client.delete_item, ItemUri),
        )
        router.add_api_route(
            name="Create Collection",
            path="/collections",
            response_model=schemas.Collection,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["POST"],
            endpoint=create_endpoint_from_model(
                self.client.create_collection, collection_request_model
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
                self.client.update_collection, collection_request_model
            ),
        )
        router.add_api_route(
            name="Delete Collection",
            path="/collections/{collectionId}",
            response_model=schemas.Collection,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["DELETE"],
            endpoint=create_endpoint_with_depends(
                self.client.delete_collection, CollectionUri
            ),
        )
        app.include_router(router, tags=["Transaction Extension"])


@attr.s
class BulkTransactionExtension(ApiExtension):
    """Bulk Transaction Extension.

    Bulk Transaction extension adds the `POST /collections/{collectionId}/bulk_items` endpoint to the application
    for efficient bulk insertion of items.
    """

    client: BaseBulkTransactionsClient = attr.ib()

    def register(self, app: FastAPI) -> None:
        """Register the extension with a FastAPI application.

        Args:
            app: target FastAPI application.

        Returns:
            None
        """
        items_request_model = _create_request_model(schemas.Items)

        router = APIRouter()
        router.add_api_route(
            name="Bulk Create Item",
            path="/collections/{collectionId}/bulk_items",
            response_model=str,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["POST"],
            endpoint=create_endpoint_from_model(
                self.client.bulk_item_insert, items_request_model
            ),
        )
        app.include_router(router, tags=["Bulk Transaction Extension"])
