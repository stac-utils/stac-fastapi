"""Discovery Search extension request models."""

from typing import Optional

import attr
from pydantic import BaseModel, Field

from stac_fastapi.types.search import APIRequest, Limit


@attr.s
class DiscoverySearchExtensionGetRequest(APIRequest):
    """Discovery Search extension GET request model."""

    q: Optional[str] = attr.ib(default=None)
    limit: Optional[int] = attr.ib(default=10)


class DiscoverySearchExtensionPostRequest(BaseModel):
    """Discovery Search extension POST request model."""

    q: Optional[str]
    limit: Optional[Limit] = Field(default=10)
