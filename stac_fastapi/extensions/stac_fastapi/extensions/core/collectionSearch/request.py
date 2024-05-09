"""Collection Search extension request models."""

from enum import Enum
from typing import Any, Dict, Optional, List

import attr
from pydantic import BaseModel, Field
from stac_pydantic.shared import BBox

from stac_fastapi.types.search import APIRequest, Limit, str2bbox

from stac_fastapi.types.rfc3339 import DateTimeType, str_to_interval

@attr.s
class CollectionSearchExtensionGetRequest(APIRequest):
    """Collection Search extension GET request model."""

    bbox: Optional[BBox] = attr.ib(default=None, converter=str2bbox)
    datetime: Optional[DateTimeType] = attr.ib(default=None, converter=str_to_interval)
    limit: Optional[int] = attr.ib(default=10)
    q: Optional[str] = attr.ib(default=None)

class CollectionSearchExtensionPostRequest(BaseModel):
    """Collection Search extension POST request model."""

    bbox: Optional[BBox]
    datetime: Optional[DateTimeType]
    limit: Optional[Limit] = Field(default=10)
    q: Optional[str]
