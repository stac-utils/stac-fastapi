"""stac_fastapi.types.search module.

"""
from datetime import datetime as dt
from typing import Dict, List, Optional, Union

import attr
from fastapi import Query
from pydantic import Field, PositiveInt
from pydantic.functional_validators import AfterValidator
from stac_pydantic.api import Search
from stac_pydantic.shared import BBox
from typing_extensions import Annotated

from stac_fastapi.types.rfc3339 import DateTimeType, str_to_interval


def crop(v: PositiveInt) -> PositiveInt:
    """Crop value to 10,000."""
    limit = 10_000
    if v > limit:
        v = limit
    return v


def str2list(x: str) -> Optional[List[str]]:
    """Convert string to list base on , delimiter."""
    if x:
        return x.split(",")

    return None


def str2bbox(x: str) -> Optional[BBox]:
    """Convert string to BBox based on , delimiter."""
    if x:
        t = tuple(float(v) for v in str2list(x))
        assert len(t) == 4
        return t

    return None


def _collection_converter(
    val: Annotated[
        Optional[str],
        Query(
            description="Array of collection Ids to search for items.",
            json_schema_extra={
                "example": "collection1,collection2",
            },
        ),
    ] = None,
) -> Optional[List[str]]:
    return str2list(val)


def _ids_converter(
    val: Annotated[
        Optional[str],
        Query(
            description="Array of Item ids to return.",
            json_schema_extra={
                "example": "item1,item2",
            },
        ),
    ] = None,
) -> Optional[List[str]]:
    return str2list(val)


def _bbox_converter(
    val: Annotated[
        Optional[str],
        Query(
            description="Only return items intersecting this bounding box. Mutually exclusive with **intersects**.",  # noqa: E501
            json_schema_extra={
                "example": "-175.05,-85.05,175.05,85.05",
            },
        ),
    ] = None,
) -> Optional[BBox]:
    return str2bbox(val)


def _validate_datetime(instance, attribute, value):
    """Validate Datetime."""
    _ = str_to_interval(value)


# Be careful: https://github.com/samuelcolvin/pydantic/issues/1423#issuecomment-642797287
NumType = Union[float, int]
Limit = Annotated[PositiveInt, AfterValidator(crop)]


DateTimeQueryType = Annotated[
    Optional[str],
    Query(
        description="""Only return items that have a temporal property that intersects this value.\n
Either a date-time or an interval, open or closed. Date and time expressions adhere to RFC 3339. Open intervals are expressed using double-dots.""",  # noqa: E501
        openapi_examples={
            "datetime": {"value": "2018-02-12T23:20:50Z"},
            "closed-interval": {"value": "2018-02-12T00:00:00Z/2018-03-18T12:31:12Z"},
            "open-interval-from": {"value": "2018-02-12T00:00:00Z/.."},
            "open-interval-to": {"value": "../2018-03-18T12:31:12Z"},
        },
    ),
]


@attr.s
class APIRequest:
    """Generic API Request base class."""

    def kwargs(self) -> Dict:
        """Transform api request params into format which matches the signature of the
        endpoint."""
        return self.__dict__


@attr.s
class DatetimeMixin:
    """Datetime Mixin."""

    datetime: DateTimeQueryType = attr.ib(default=None, validator=_validate_datetime)

    def parse_datetime(self) -> Optional[DateTimeType]:
        """Return Datetime objects."""
        return str_to_interval(self.datetime)

    @property
    def start_date(self) -> Optional[dt]:
        """Start Date."""
        parsed = self.parse_datetime()
        if parsed is None:
            return None

        return parsed[0] if isinstance(parsed, tuple) else parsed

    @property
    def end_date(self) -> Optional[dt]:
        """End Date."""
        parsed = self.parse_datetime()
        if parsed is None:
            return None

        return parsed[1] if isinstance(parsed, tuple) else None


@attr.s
class BaseSearchGetRequest(APIRequest, DatetimeMixin):
    """Base arguments for GET Request."""

    collections: Optional[List[str]] = attr.ib(
        default=None, converter=_collection_converter
    )
    ids: Optional[List[str]] = attr.ib(default=None, converter=_ids_converter)
    bbox: Optional[BBox] = attr.ib(default=None, converter=_bbox_converter)
    intersects: Annotated[
        Optional[str],
        Query(
            description="""Only return items intersecting this GeoJSON Geometry. Mutually exclusive with **bbox**. \n
*Remember to URL encode the GeoJSON geometry when using GET request*.""",  # noqa: E501
            openapi_examples={
                "madrid": {
                    "value": {
                        "type": "Feature",
                        "properties": {},
                        "geometry": {
                            "coordinates": [
                                [
                                    [-3.8549260500072933, 40.54923557897152],
                                    [-3.8549260500072933, 40.29428000041938],
                                    [-3.516597069715033, 40.29428000041938],
                                    [-3.516597069715033, 40.54923557897152],
                                    [-3.8549260500072933, 40.54923557897152],
                                ]
                            ],
                            "type": "Polygon",
                        },
                    },
                },
                "new-york": {
                    "value": {
                        "type": "Feature",
                        "properties": {},
                        "geometry": {
                            "coordinates": [
                                [
                                    [-74.50117532354284, 41.128266394414055],
                                    [-74.50117532354284, 40.35633909727355],
                                    [-73.46713183168603, 40.35633909727355],
                                    [-73.46713183168603, 41.128266394414055],
                                    [-74.50117532354284, 41.128266394414055],
                                ]
                            ],
                            "type": "Polygon",
                        },
                    },
                },
            },
        ),
    ] = attr.ib(default=None)
    datetime: DateTimeQueryType = attr.ib(default=None, validator=_validate_datetime)
    limit: Annotated[
        Optional[Limit],
        Query(
            description="Limits the number of results that are included in each page of the response (capped to 10_000)."  # noqa: E501
        ),
    ] = attr.ib(default=10)


class BaseSearchPostRequest(Search):
    """Base arguments for POST Request."""

    limit: Optional[Limit] = Field(
        10,
        description="Limits the number of results that are included in each page of the response (capped to 10_000).",  # noqa: E501
    )
