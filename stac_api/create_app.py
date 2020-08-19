"""fastapi app creation"""
from typing import Callable, Type

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from stac_api.clients.base import BaseTransactionsClient
from stac_api.models import schemas
from stac_api.models.api import APIRequest, APIResponse, DeleteCollection, DeleteItem
from stac_api.utils.dependencies import discover_base_url


# TODO: Only use one endpoint factory
def create_endpoint_from_model(
    func: Callable, request_model: Type[BaseModel], response_model: Type[APIResponse]
) -> Callable:
    """
    Create a FastAPI endpoint where request model is a pydantic model.  This works best for validating request bodies
    (POST/PUT etc.)
    """

    def _endpoint(
        request_data: request_model,  # type:ignore
        base_url: str = Depends(discover_base_url),  # type:ignore
    ):
        """endpoint"""
        resp = func(request_data)
        return response_model.create_api_response(resp, base_url)

    return _endpoint


def create_endpoint_with_depends(
    func: Callable, request_model: Type[APIRequest], response_model: Type[APIResponse]
) -> Callable:
    """
    Create a fastapi endpoint where request model is a dataclass.  This works best for validating query/patm params.
    """

    def _endpoint(
        request_data: request_model = Depends(),  # type:ignore
        base_url: str = Depends(discover_base_url),
    ):
        """endpoint"""
        resp = func(**request_data.kwargs())  # type:ignore
        return response_model.create_api_response(resp, base_url)

    return _endpoint


def create_transactions_router(client: BaseTransactionsClient) -> APIRouter:
    """Create API router for transactions extension"""
    router = APIRouter()
    router.add_api_route(
        name="Create Item",
        path="/collections/{collectionId}/items",
        response_model=schemas.Item,
        response_model_exclude_unset=True,
        response_model_exclude_none=True,
        methods=["POST"],
        endpoint=create_endpoint_from_model(
            client.create_item, schemas.Item, schemas.Item
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
            client.update_item, schemas.Item, schemas.Item
        ),
    )
    router.add_api_route(
        name="Delete Item",
        path="/collections/{collectionId}/items/{itemId}",
        response_model=schemas.Item,
        response_model_exclude_unset=True,
        response_model_exclude_none=True,
        methods=["DELETE"],
        endpoint=create_endpoint_with_depends(
            client.delete_item, DeleteItem, schemas.Item
        ),
    )
    router.add_api_route(
        name="Create Collection",
        path="/collections",
        response_model=schemas.Collection,
        response_model_exclude_unset=True,
        response_model_exclude_none=True,
        methods=["POST"],
        endpoint=create_endpoint_from_model(
            client.create_collection, schemas.Collection, schemas.Collection
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
            client.update_collection, schemas.Collection, schemas.Collection
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
            client.delete_collection, DeleteCollection, schemas.Collection
        ),
    )
    return router
