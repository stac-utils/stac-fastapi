"""Request model for the Aggregation extension."""

from typing import Annotated

import attr
from fastapi import Query
from pydantic import Field

from stac_fastapi.types.search import (
    BaseSearchGetRequest,
    BaseSearchPostRequest,
    str2list,
)


def _agg_converter(
    val: Annotated[
        str | None,
        Query(description="A list of aggregations to compute and return."),
    ] = None,
) -> list[str] | None:
    return str2list(val)


@attr.s
class AggregationExtensionGetRequest(BaseSearchGetRequest):
    """Aggregation Extension GET request model."""

    aggregations: list[str] | None = attr.ib(default=None, converter=_agg_converter)


class AggregationExtensionPostRequest(BaseSearchPostRequest):
    """Aggregation Extension POST request model."""

    aggregations: list[str] | None = Field(
        default=None,
        description="A list of aggregations to compute and return.",
    )
