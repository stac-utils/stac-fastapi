"""Request model for the Aggregation extension."""

from typing import List, Optional

import attr
from fastapi import Query
from pydantic import Field
from typing_extensions import Annotated

from stac_fastapi.types.search import (
    BaseSearchGetRequest,
    BaseSearchPostRequest,
    str2list,
)


@attr.s
class AggregationExtensionGetRequest(BaseSearchGetRequest):
    """Aggregation Extension GET request model."""

    aggregations: Annotated[Optional[str], Query()] = attr.ib(
        default=None, converter=str2list
    )


class AggregationExtensionPostRequest(BaseSearchPostRequest):
    """Aggregation Extension POST request model."""

    aggregations: Optional[List[str]] = Field(default=None)
