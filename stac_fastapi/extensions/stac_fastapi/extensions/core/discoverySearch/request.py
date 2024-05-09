"""Discovery Search extension request models."""

from enum import Enum
from typing import Any, Dict, Optional, List

import attr
from pydantic import BaseModel, Field
from stac_pydantic.shared import BBox

from stac_fastapi.types.search import APIRequest, Limit, str2bbox

from stac_fastapi.types.rfc3339 import DateTimeType, str_to_interval

from ..filter.request import FilterLang

@attr.s
class DiscoverySearchExtensionGetRequest(APIRequest):
    """Discovery Search extension GET request model."""

    q: Optional[str] = attr.ib(default=None)
    limit: Optional[int] = attr.ib(default=10)

class DiscoverySearchExtensionPostRequest(BaseModel):
    """Discovery Search extension POST request model."""

    q: Optional[str]
    limit: Optional[Limit] = Field(default=10)
