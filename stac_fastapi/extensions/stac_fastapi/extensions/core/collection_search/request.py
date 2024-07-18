"""Request models for the Collection-Search extension."""

from typing import Optional

import attr
from fastapi import Query
from typing_extensions import Annotated

from stac_pydantic.shared import BBox
from stac_fastapi.types.rfc3339 import DateTimeType
from stac_fastapi.types.search import APIRequest, _datetime_converter, _bbox_converter


@attr.s
class CollectionSearchExtensionGetRequest(APIRequest):
    """Basics additional Collection-Search parameters for the GET request."""

    bbox: Optional[BBox] = attr.ib(default=None, converter=_bbox_converter)
    datetime: Optional[DateTimeType] = attr.ib(
        default=None, converter=_datetime_converter
    )
    limit: Annotated[
        Optional[int],
        Query(
            description="Limits the number of results that are included in each page of the response."  # noqa: E501
        ),
    ] = attr.ib(default=None)


@attr.s
class FreeTextGetRequest(APIRequest):
    """FreeText additional Collection-Search parameters for the GET request."""

    q: Annotated[
        Optional[str],
        Query(description="A basic free-text search parameter."),
    ] = attr.ib(default=None)

