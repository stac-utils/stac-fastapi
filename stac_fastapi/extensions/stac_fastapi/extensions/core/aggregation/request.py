"""Request model for the Aggregation extension."""

from typing import List, Optional, Union

import attr

from stac_fastapi.extensions.core.filter.request import (
    FilterExtensionGetRequest,
    FilterExtensionPostRequest,
)
from stac_fastapi.types.search import BaseSearchGetRequest, BaseSearchPostRequest, str2list


@attr.s
class AggregationExtensionGetRequest(BaseSearchGetRequest, FilterExtensionGetRequest):
    """Aggregation Extension GET request model."""

    aggregations: Optional[str] = attr.ib(default=None, converter=str2list)


class AggregationExtensionPostRequest(BaseSearchPostRequest, FilterExtensionPostRequest):
    """Aggregation Extension POST request model."""

    aggregations: Optional[List[str]] = attr.ib(default=None)
