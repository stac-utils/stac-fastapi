"""Aggregation Extension types."""

from typing import Any, Dict, List, Literal, Optional, Union

from typing_extensions import NotRequired, TypedDict

from stac_fastapi.types.rfc3339 import DateTimeType

Bucket = TypedDict(
    "Bucket",
    {
        "key": str,
        "data_type": str,
        "frequency": NotRequired[Dict],
        # we can't use the `class Bucket` notation because `from` is a reserved key
        "from": NotRequired[Union[int, float]],
        "to": NotRequired[Optional[Union[int, float]]],
    },
)


class Aggregation(TypedDict):
    """A STAC aggregation."""

    name: str
    data_type: str
    buckets: NotRequired[List[Bucket]]
    overflow: NotRequired[int]
    value: NotRequired[Union[str, int, DateTimeType]]


class AggregationCollection(TypedDict):
    """STAC Item Aggregation Collection."""

    type: Literal["AggregationCollection"]
    aggregations: List[Aggregation]
    links: List[Dict[str, Any]]
