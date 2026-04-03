"""Aggregation extensions clients."""

import abc
from typing import List, Optional, Union

import attr
from geojson_pydantic.geometries import Geometry
from stac_pydantic.shared import BBox

from stac_fastapi.types.rfc3339 import DateTimeType

from .types import Aggregation, AggregationCollection


@attr.s
class BaseAggregationClient(abc.ABC):
    """Defines a pattern for implementing the STAC aggregation extension."""

    # BUCKET = Bucket
    # AGGREGAION = Aggregation
    # AGGREGATION_COLLECTION = AggregationCollection

    def get_aggregations(
        self, collection_id: Optional[str] = None, **kwargs
    ) -> AggregationCollection:
        """Get the aggregations available for the given collection_id.

        If collection_id is None, returns the available aggregations over all
        collections.
        """
        return AggregationCollection(
            type="AggregationCollection",
            aggregations=[Aggregation(name="total_count", data_type="integer")],
            links=[
                {
                    "rel": "root",
                    "type": "application/json",
                    "href": "https://example.org/",
                },
                {
                    "rel": "self",
                    "type": "application/json",
                    "href": "https://example.org/aggregations",
                },
            ],
        )

    def aggregate(
        self, collection_id: Optional[str] = None, **kwargs
    ) -> AggregationCollection:
        """Return the aggregation buckets for a given search result"""
        return AggregationCollection(
            type="AggregationCollection",
            aggregations=[],
            links=[
                {
                    "rel": "root",
                    "type": "application/json",
                    "href": "https://example.org/",
                },
                {
                    "rel": "self",
                    "type": "application/json",
                    "href": "https://example.org/aggregations",
                },
            ],
        )


@attr.s
class AsyncBaseAggregationClient(abc.ABC):
    """Defines an async pattern for implementing the STAC aggregation extension."""

    # BUCKET = Bucket
    # AGGREGAION = Aggregation
    # AGGREGATION_COLLECTION = AggregationCollection

    async def get_aggregations(
        self, collection_id: Optional[str] = None, **kwargs
    ) -> AggregationCollection:
        """Get the aggregations available for the given collection_id.

        If collection_id is None, returns the available aggregations over all
        collections.
        """
        return AggregationCollection(
            type="AggregationCollection",
            aggregations=[Aggregation(name="total_count", data_type="integer")],
            links=[
                {
                    "rel": "root",
                    "type": "application/json",
                    "href": "https://example.org/",
                },
                {
                    "rel": "self",
                    "type": "application/json",
                    "href": "https://example.org/aggregations",
                },
            ],
        )

    async def aggregate(
        self,
        collection_id: Optional[str] = None,
        aggregations: Optional[Union[str, List[str]]] = None,
        collections: Optional[List[str]] = None,
        ids: Optional[List[str]] = None,
        bbox: Optional[BBox] = None,
        intersects: Optional[Geometry] = None,
        datetime: Optional[DateTimeType] = None,
        limit: Optional[int] = 10,
        **kwargs,
    ) -> AggregationCollection:
        """Return the aggregation buckets for a given search result"""
        return AggregationCollection(
            type="AggregationCollection",
            aggregations=[],
            links=[
                {
                    "rel": "root",
                    "type": "application/json",
                    "href": "https://example.org/",
                },
                {
                    "rel": "self",
                    "type": "application/json",
                    "href": "https://example.org/aggregations",
                },
            ],
        )
