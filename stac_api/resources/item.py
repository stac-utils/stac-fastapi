"""Item endpoints"""

import json
from datetime import datetime
from typing import List, Optional, Union

from fastapi import APIRouter, Depends, Query
from starlette.requests import Request

from stac_api.clients.postgres.item import ItemCrudClient, item_crud_client_factory
from stac_api.models import schemas
from stac_api.utils.dependencies import parse_list_factory
from stac_pydantic.item import ItemCollection

router = APIRouter()

NumType = Union[float, int]


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
    return crud_client.search(search_request, request=request)
