"""Collection endpoints"""
from typing import List

from fastapi import APIRouter, Depends

from ..clients.postgres.collection import (
    CollectionCrudClient,
    collection_crud_client_factory,
)
from ..models import schemas
from ..utils.dependencies import discover_base_url

router = APIRouter()


@router.get(
    "/collections",
    summary="Get all collections",
    response_model=List[schemas.CollectionBase],
    response_model_exclude_unset=True,
    response_model_exclude_none=True,
)
def get_all_collections(
    crud_client: CollectionCrudClient = Depends(collection_crud_client_factory),
    base_url: str = Depends(discover_base_url),
):
    """Get all collections"""
    row_data = crud_client.all_collections()
    response_data = []
    for row in row_data:
        row.base_url = base_url
        response_data.append(schemas.Collection.from_orm(row))
    return response_data


@router.get(
    "/collections/{collectionId}",
    summary="Get a collection by id",
    response_model=schemas.Collection,
    response_model_exclude_unset=True,
    response_model_exclude_none=True,
)
def get_collection_by_id(
    collectionId: str,
    crud_client: CollectionCrudClient = Depends(collection_crud_client_factory),
    base_url: str = Depends(discover_base_url),
):
    """Get a single collection"""
    row_data = crud_client.read(collectionId)
    row_data.base_url = base_url
    return row_data
