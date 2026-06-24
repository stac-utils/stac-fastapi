"""Aggregation Extension types."""

from typing import Any, Literal, NotRequired

from typing_extensions import TypedDict

from stac_fastapi.types.rfc3339 import DateTimeType

Bucket = TypedDict(
    "Bucket",
    {
        "key": str,
        "data_type": str,
        "frequency": NotRequired[dict],
        # we can't use the `class Bucket` notation because `from` is a reserved key
        "from": NotRequired[int | float],
        "to": NotRequired[int | float | None],
    },
)


class Aggregation(TypedDict):
    """A STAC aggregation."""

    name: str
    data_type: str
    buckets: NotRequired[list[Bucket]]
    overflow: NotRequired[int]
    value: NotRequired[str | int | DateTimeType]


class AggregationCollection(TypedDict):
    """STAC Item Aggregation Collection."""

    type: Literal["AggregationCollection"]
    aggregations: list[Aggregation]
    links: list[dict[str, Any]]
