"""Request model for the Query extension."""

from dataclasses import dataclass
from typing import Any, Dict, Optional

from fastapi import Query
from pydantic import BaseModel
from typing_extensions import Annotated

from stac_fastapi.types.search import APIRequest


@dataclass
class QueryExtensionGetRequest(APIRequest):
    """Query Extension GET request model."""

    query: Annotated[Optional[str], Query()] = None


class QueryExtensionPostRequest(BaseModel):
    """Query Extension POST request model."""

    query: Optional[Dict[str, Dict[str, Any]]] = None
