"""Collection endpoints"""
from typing import List

from fastapi import APIRouter, Depends

from ..clients import collection_crud_client_factory
from ..clients.collection_crud import CollectionCrudClient
from ..models import schemas
from ..utils.dependencies import discover_base_url

router = APIRouter()


@router.post(
    "/collections",
    summary="Create a new collection",
    response_model=schemas.Collection,
    response_model_exclude_unset=True,
    response_model_exclude_none=True,
)
def create_collection(
    collection: schemas.Collection,
    crud_client: CollectionCrudClient = Depends(collection_crud_client_factory),
    base_url: str = Depends(discover_base_url),
):
    """Create a new collection (transactions extension)"""
    row_data = crud_client.create(collection)
    row_data.base_url = base_url
    return row_data


@router.put(
    "/collections",
    summary="Update a collection if it exists, otherwise create a new collection",
    response_model=schemas.Collection,
    response_model_exclude_unset=True,
    response_model_exclude_none=True,
)
def update_collection_by_id(
    collection: schemas.Collection,
    crud_client: CollectionCrudClient = Depends(collection_crud_client_factory),
    base_url: str = Depends(discover_base_url),
):
    """Update collection (transactions extension)"""
    row_data = crud_client.update(collection)
    row_data.base_url = base_url
    return row_data


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
    row_data = crud_client.get_all_collections()
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


@router.delete(
    "/collections/{collectionId}",
    summary="Delete a collection by id",
    response_model=schemas.Collection,
    response_model_exclude_unset=True,
    response_model_exclude_none=True,
)
def delete_collection_by_id(
    collectionId: str,
    crud_client: CollectionCrudClient = Depends(collection_crud_client_factory),
    base_url: str = Depends(discover_base_url),
):
    """Delete a collection (transactions extension)"""
    row_data = crud_client.delete(collectionId)
    row_data.base_url = base_url
    return row_data
