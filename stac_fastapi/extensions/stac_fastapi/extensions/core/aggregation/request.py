"""Request model for the Aggregation extension."""

from typing import Optional

import attr
from pydantic import BaseModel

from stac_fastapi.types.search import APIRequest


@attr.s
class AggregationExtensionGetRequest(APIRequest):
    """Query Extension GET request model."""

    aggregations: Optional[str] = attr.ib(default=None)
    bbox: Optional[str] = attr.ib(default=None)
    intersects: Optional[str] = attr.ib(default=None)
    ids: Optional[str] = attr.ib(default=None)
    datetime: Optional[str] = attr.ib(default=None)
    collections: Optional[str] = attr.ib(default=None)


class AggregationExtensionPostRequest(BaseModel):
    """Query Extension POST request model."""

    aggregations: Optional[str] = attr.ib(default=None)
    bbox: Optional[str] = attr.ib(default=None)
    intersects: Optional[str] = attr.ib(default=None)
    ids: Optional[str] = attr.ib(default=None)
    datetime: Optional[str] = attr.ib(default=None)
    collections: Optional[str] = attr.ib(default=None)
