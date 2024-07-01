"""Request model for the Aggregation extension."""

from dataclasses import dataclass
from typing import List, Optional

from fastapi import Query
from pydantic import Field
from typing_extensions import Annotated

from stac_fastapi.types.search import (
    BaseSearchGetRequest,
    BaseSearchPostRequest,
    str2list,
)


@dataclass
class AggregationExtensionGetRequest(BaseSearchGetRequest):
    """Aggregation Extension GET request model."""

    aggregations: Annotated[Optional[str], Query()] = None

    def __post_init__(self):
        """convert attributes."""
        super().__post_init__()
        if self.aggregations:
            self.aggregations = str2list(self.aggregations)  # type: ignore


class AggregationExtensionPostRequest(BaseSearchPostRequest):
    """Aggregation Extension POST request model."""

    aggregations: Optional[List[str]] = Field(default=None)
