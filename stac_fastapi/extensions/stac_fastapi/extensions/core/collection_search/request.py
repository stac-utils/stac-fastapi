"""Request models for the Collection-Search extension."""

from typing import Optional

import attr
from fastapi import Query
from stac_pydantic.shared import BBox
from typing_extensions import Annotated

from stac_fastapi.types.rfc3339 import DateTimeType
from stac_fastapi.types.search import APIRequest, _bbox_converter, _datetime_converter


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
    ] = attr.ib(default=10)
