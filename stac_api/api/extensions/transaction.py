"""stac-api transaction extension"""
import attr
from fastapi import APIRouter, FastAPI

from stac_api.api.extensions.extension import ApiExtension
from stac_api.api.models import CollectionUri, ItemUri, _create_request_model
from stac_api.api.routes import create_endpoint_from_model, create_endpoint_with_depends
from stac_api.clients.base import BaseTransactionsClient
from stac_api.models import schemas


@attr.s
class TransactionExtension(ApiExtension):
    """
    stac-api transaction extension
    (https://github.com/radiantearth/stac-api-spec/blob/master/extensions/transaction/README.md)
    """

    client: BaseTransactionsClient = attr.ib()

    def register(self, app: FastAPI) -> None:
        """register extension with the application"""

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
