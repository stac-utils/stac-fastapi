"""Request model for the Aggregation extension."""

from dataclasses import dataclass
from typing import List, Optional, Union

from fastapi import Query
from pydantic import BaseModel, Field
from typing_extensions import Annotated

from stac_fastapi.types.search import APIRequest


@dataclass
class AggregationExtensionGetRequest(APIRequest):
    """Aggregation Extension GET request model."""

    aggregations: Annotated[Optional[str], Query()] = None


class AggregationExtensionPostRequest(BaseModel):
    """Aggregation Extension POST request model."""

    aggregations: Optional[Union[str, List[str]]] = Field(default=None)
