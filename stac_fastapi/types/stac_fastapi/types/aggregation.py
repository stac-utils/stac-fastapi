"""Aggregation Extension types."""

import sys
from typing import Any, Dict, List, Literal, Optional, Union

from pydantic import Field

from stac_fastapi.types.rfc3339 import DateTimeType

# Avoids a Pydantic error:
# TypeError: You should use `typing_extensions.TypedDict` instead of
# `typing.TypedDict` with Python < 3.12.0.  Without it, there is no way to
# differentiate required and optional fields when subclassed.
if sys.version_info < (3, 12, 0):
    from typing_extensions import TypedDict
else:
    from typing import TypedDict


class Bucket(TypedDict, total=False):
    """A STAC aggregation bucket."""

    key: str
    data_type: str
    frequency: Optional[Dict] = None
    _from: Optional[Union[int, float]] = Field(alias="filter-crs", default=None)
    to: Optional[Optional[Union[int, float]]] = None


class Aggregation(TypedDict, total=False):
    """A STAC aggregation."""

    name: str
    data_type: str
    buckets: Optional[List[Bucket]] = None
    overflow: Optional[int] = None
    value: Optional[Union[str, int, DateTimeType]] = None


class AggregationCollection(TypedDict, total=False):
    """STAC Item Aggregation Collection."""

    type: Literal["FeatureCollection"]
    aggregations: List[Aggregation]
    links: List[Dict[str, Any]]
