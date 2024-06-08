"""Aggregation Extension types."""

from typing import Any, Dict, List, Literal, Optional, Union

from pydantic import Field
from typing_extensions import TypedDict

from stac_fastapi.types.rfc3339 import DateTimeType


class Bucket(TypedDict, total=False):
    """A STAC aggregation bucket."""

    key: str
    data_type: str
    frequency: Optional[Dict] = None
    _from: Optional[Union[int, float]] = Field(alias="from", default=None)
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

    type: Literal["AggregationCollection"]
    aggregations: List[Aggregation]
    links: List[Dict[str, Any]]
