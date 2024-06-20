"""Discovery Search extension request models."""

from typing import List, Optional

import attr
from pydantic import BaseModel, Field

from stac_fastapi.types.search import APIRequest, Limit, str2list


@attr.s
class DiscoverySearchExtensionGetRequest(APIRequest):
    """Discovery Search extension GET request model."""

    q: Optional[List[str]] = attr.ib(default=None, converter=str2list)
    limit: Optional[int] = attr.ib(default=10)


class DiscoverySearchExtensionPostRequest(BaseModel):
    """Discovery Search extension POST request model."""

    q: Optional[List[str]]
    limit: Optional[Limit] = Field(default=10)
