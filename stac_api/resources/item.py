"""Item endpoints"""

import json
from datetime import datetime
from typing import List, Optional, Union
from urllib.parse import urlencode

from fastapi import APIRouter, Depends, Query
from starlette.requests import Request

from stac_pydantic.api.extensions.paging import PaginationLink
from stac_pydantic.item import ItemCollection
from stac_pydantic.shared import Link, Relations

from ..clients.postgres.collection import (
    CollectionCrudClient,
    collection_crud_client_factory,
)
from ..clients.postgres.item import ItemCrudClient, item_crud_client_factory
from ..models import schemas
from ..utils.dependencies import discover_base_url, parse_list_factory

router = APIRouter()

NumType = Union[float, int]


@router.get(
    "/collections/{collectionId}/items",
    response_model=ItemCollection,
    response_model_exclude_unset=True,
    response_model_exclude_none=True,
)
def get_item_collection(
    collectionId: str,
    limit: int = 10,
    token: Optional[str] = None,
    crud_client: CollectionCrudClient = Depends(collection_crud_client_factory),
    base_url: str = Depends(discover_base_url),
):
    """Get collection items"""
    page, count = crud_client.item_collection(collectionId, limit, token=token)

    links = []
    if page.next:
        links.append(
            PaginationLink(
                rel=Relations.next,
                type="application/geo+json",
                href=f"{base_url}/collections/{collectionId}/items?token={page.next}&limit={limit}",
                method="GET",
            )
        )
    if page.previous:
        links.append(
            PaginationLink(
                rel=Relations.previous,
                type="application/geo+json",
                href=f"{base_url}/collections/{collectionId}/items?token={page.previous}&limit={limit}",
                method="GET",
            )
        )

    response_features = []
    for item in page:
        item.base_url = base_url
        response_features.append(schemas.Item.from_orm(item))

    return ItemCollection(
        type="FeatureCollection",
        context={"returned": len(page), "limit": limit, "matched": count},
        features=response_features,
        links=links,
    )


@router.get(
    "/collections/{collectionId}/items/{itemId}",
    response_model=schemas.Item,
    response_model_exclude_unset=True,
    response_model_exclude_none=True,
)
def get_item_by_id(
    itemId: str,
    crud_client: ItemCrudClient = Depends(item_crud_client_factory),
    base_url: str = Depends(discover_base_url),
):
    """Get item"""
    row_data = crud_client.read(itemId)
    row_data.base_url = base_url
    return row_data


@router.post(
    "/search",
    response_model=ItemCollection,
    response_model_exclude_unset=True,
    response_model_exclude_none=True,
)
def search_items_post(
    search_request: schemas.STACSearch,
    crud_client: ItemCrudClient = Depends(item_crud_client_factory),
    base_url: str = Depends(discover_base_url),
):
    """POST search catalog"""
    page, count = crud_client.search(search_request)

    links = []
    if page.next:
        links.append(
            PaginationLink(
                rel=Relations.next,
                type="application/geo+json",
                href=f"{base_url}/search",
                method="POST",
                body={"token": page.next},
                merge=True,
            )
        )
    if page.previous:
        links.append(
            PaginationLink(
                rel=Relations.previous,
                type="application/geo+json",
                href=f"{base_url}/search",
                method="POST",
                body={"token": page.previous},
                merge=True,
            )
        )

    response_features = []
    filter_kwargs = search_request.field.filter_fields
    for item in page:
        item.base_url = base_url
        response_features.append(schemas.Item.from_orm(item).to_dict(**filter_kwargs))

    # Geoalchemy doesn't have a good way of calculating extent of many features, so we'll calculate it outside the db
    bbox = None
    if count > 0:
        xvals = [
            item
            for sublist in [
                [float(item["bbox"][0]), float(item["bbox"][2])]
                for item in response_features
            ]
            for item in sublist
        ]
        yvals = [
            item
            for sublist in [
                [float(item["bbox"][1]), float(item["bbox"][3])]
                for item in response_features
            ]
            for item in sublist
        ]
        bbox = (min(xvals), min(yvals), max(xvals), max(yvals))

    return ItemCollection(
        type="FeatureCollection",
        context={
            "returned": len(page),
            "limit": search_request.limit,
            "matched": count,
        },
        features=response_features,
        links=links,
        bbox=bbox,
    )


@router.get(
    "/search",
    response_model=ItemCollection,
    response_model_exclude_unset=True,
    response_model_exclude_none=True,
)
def search_items_get(
    request: Request,
    collections: Optional[List[str]] = Depends(parse_list_factory("collections")),
    ids: Optional[List[str]] = Depends(parse_list_factory("ids")),
    bbox: Optional[List[NumType]] = Depends(parse_list_factory("bbox")),
    datetime: Optional[Union[str, datetime]] = Query(None),
    limit: Optional[int] = Query(10),
    query: Optional[str] = Query(None),
    token: Optional[str] = None,
    fields: Optional[List[str]] = Depends(parse_list_factory("fields")),
    sortby: Optional[str] = Depends(parse_list_factory("sortby")),
    crud_client: ItemCrudClient = Depends(item_crud_client_factory),
    base_url: str = Depends(discover_base_url),
):
    """GET search catalog"""
    # Parse request parameters
    base_args = {
        "collections": collections,
        "ids": ids,
        "bbox": bbox,
        "limit": limit,
        "token": token,
        "query": json.loads(query) if query else query,
    }
    if datetime:
        base_args["datetime"] = datetime
    if sortby:
        # https://github.com/radiantearth/stac-spec/tree/master/api-spec/extensions/sort#http-get-or-post-form
        sort_param = []
        for sort in sortby:
            sort_param.append(
                {"field": sort[1:], "direction": "asc" if sort[0] == "+" else "desc"}
            )
        base_args["sortby"] = sort_param

    if fields:
        includes = set()
        excludes = set()
        for field in fields:
            if field[0] == "-":
                excludes.add(field[1:])
            elif field[0] == "+":
                includes.add(field[1:])
            else:
                includes.add(field)
        base_args["fields"] = {"include": includes, "exclude": excludes}

    # Do the request
    search_request = schemas.STACSearch(**base_args)
    filter_kwargs = search_request.field.filter_fields
    page, count = crud_client.search(search_request)

    # Pagination
    links = []
    query_params = dict(request.query_params)
    if page.next:
        query_params["token"] = page.next
        links.append(
            PaginationLink(
                rel=Relations.next,
                type="application/geo+json",
                href=f"{base_url}/search?{urlencode(query_params)}",
                method="GET",
            )
        )
    if page.previous:
        query_params["token"] = page.previous
        links.append(
            PaginationLink(
                rel=Relations.previous,
                type="application/geo+json",
                href=f"{base_url}/search?{urlencode(query_params)}",
                method="GET",
            )
        )

    # Add OGC Tile links
    if not collections:
        collections = {item.collection_id for item in page}  # type:ignore

    for coll in collections:
        links.append(
            Link(
                rel=Relations.tiles,
                type="application/json",
                href=f"{base_url}/collections/{coll}/tiles?{urlencode(query_params)}",
            )
        )

    # Decompose to pydantic models
    response_features = []
    for item in page:
        item.base_url = base_url
        response_features.append(schemas.Item.from_orm(item).to_dict(**filter_kwargs))

    # Add bbox
    if count > 0:
        xvals = [
            item
            for sublist in [
                [float(item["bbox"][0]), float(item["bbox"][2])]
                for item in response_features
            ]
            for item in sublist
        ]
        yvals = [
            item
            for sublist in [
                [float(item["bbox"][1]), float(item["bbox"][3])]
                for item in response_features
            ]
            for item in sublist
        ]
        bbox = (min(xvals), min(yvals), max(xvals), max(yvals))  # type:ignore

    return ItemCollection(
        type="FeatureCollection",
        context={
            "returned": len(page),
            "limit": search_request.limit,
            "matched": count,
        },
        features=response_features,
        links=links,
        bbox=bbox,
    )
