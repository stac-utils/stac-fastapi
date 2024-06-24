"""Request model for the Aggregation extension."""

from typing import List, Optional

import attr

from stac_fastapi.types.search import (
    BaseSearchGetRequest,
    BaseSearchPostRequest,
    str2list,
)


@attr.s
class AggregationExtensionGetRequest(BaseSearchGetRequest):
    """Aggregation Extension GET request model."""

    aggregations: Optional[str] = attr.ib(default=None, converter=str2list)


class AggregationExtensionPostRequest(BaseSearchPostRequest):
    """Aggregation Extension POST request model."""

    aggregations: Optional[List[str]] = attr.ib(default=None)
