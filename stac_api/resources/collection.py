from typing import List

from fastapi import APIRouter, Depends
from starlette import status
from starlette.exceptions import HTTPException

from .. import errors
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
    try:
        row_data = crud_client.create(collection)
    except errors.ConflictError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=e.message)
    except errors.DatabaseError as e:
        raise HTTPException(
            status_code=status.HTTP_424_FAILED_DEPENDENCY, detail=e.message
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )
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
    try:
        row_data = crud_client.update(collection)
    except errors.DatabaseError as e:
        raise HTTPException(
            status_code=status.HTTP_424_FAILED_DEPENDENCY, detail=e.message
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )
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
    try:
        row_data = crud_client.get_all_collections()
    except errors.DatabaseError as e:
        raise HTTPException(
            status_code=status.HTTP_424_FAILED_DEPENDENCY, detail=e.message
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )
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
    try:
        row_data = crud_client.read(collectionId)
    except errors.NotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.message)
    except errors.DatabaseError as e:
        raise HTTPException(
            status_code=status.HTTP_424_FAILED_DEPENDENCY, detail=e.message
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )
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
    try:
        row_data = crud_client.delete(collectionId)
    except errors.NotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.message)
    except errors.DatabaseError as e:
        raise HTTPException(
            status_code=status.HTTP_424_FAILED_DEPENDENCY, detail=e.message
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )
    row_data.base_url = base_url
    return row_data
