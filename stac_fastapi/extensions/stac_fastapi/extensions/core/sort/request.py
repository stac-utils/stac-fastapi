"""Request model for the Sort Extension."""

from typing import List, Optional

import attr
from fastapi import Query
from pydantic import BaseModel, Field
from stac_pydantic.api.extensions.sort import SortExtension as PostSortModel
from typing_extensions import Annotated

from stac_fastapi.types.search import APIRequest, str2list


def _sort_converter(
    val: Annotated[
        Optional[str],
        Query(
            description="An array of property names, prefixed by either '+' for ascending or '-' for descending. If no prefix is provided, '+' is assumed.",  # noqa: E501
            openapi_examples={
                "user-provided": {"value": None},
                "resolution": {"value": "-gsd"},
                "resolution-and-dates": {"value": "-gsd,-datetime"},
            },
        ),
    ],
) -> Optional[List[str]]:
    return str2list(val)


@attr.s
class SortExtensionGetRequest(APIRequest):
    """Sortby Parameter for GET requests."""

    sortby: Optional[List[str]] = attr.ib(default=None, converter=_sort_converter)


class SortExtensionPostRequest(BaseModel):
    """Sortby parameter for POST requests."""

    sortby: Optional[List[PostSortModel]] = Field(
        None,
        description="An array of property (field) names, and direction in form of '{'field': '<property_name>', 'direction':'<direction>'}'",  # noqa: E501
        openapi_examples={
            "user-provided": {"value": None},
            "creation-time": {
                "value": [
                    {
                        "field": "properties.created",
                        "direction": "asc",
                    }
                ],
            },
        },
    )
