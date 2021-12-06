"""Filter extension request models."""

from typing import Any, Dict, Optional

import attr
from pydantic import BaseModel

from stac_fastapi.types.search import APIRequest


@attr.s
class FilterExtensionGetRequest(APIRequest):
    """Filter extension GET request model."""

    filter: Optional[str] = attr.ib(default=None)


class FilterExtensionPostRequest(BaseModel):
    """Filter extension POST request model."""

    filter: Optional[Dict[str, Any]] = None
