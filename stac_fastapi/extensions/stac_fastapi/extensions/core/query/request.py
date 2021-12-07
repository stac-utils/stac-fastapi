"""Request model for the Query extension."""

from typing import Any, Dict, Optional

import attr
from pydantic import BaseModel

from stac_fastapi.types.search import APIRequest


@attr.s
class QueryExtensionGetRequest(APIRequest):
    """Query Extension GET request model."""

    query: Optional[str] = attr.ib(default=None)


class QueryExtensionPostRequest(BaseModel):
    """Query Extension POST request model."""

    query: Optional[Dict[str, Dict[str, Any]]]
