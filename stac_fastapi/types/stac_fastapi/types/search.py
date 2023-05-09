"""stac_fastapi.types.search module.

# TODO: replace with stac-pydantic
"""

import abc
import operator
from datetime import datetime
from enum import auto
from types import DynamicClassAttribute
from typing import Any, Callable, Dict, Generator, List, Optional, Union

import attr
from geojson_pydantic.geometries import (
    LineString,
    MultiLineString,
    MultiPoint,
    MultiPolygon,
    Point,
    Polygon,
    _GeometryBase,
)
from pydantic import BaseModel, ConstrainedInt, validator
from pydantic.errors import NumberNotGtError
from pydantic.validators import int_validator
from stac_pydantic.shared import BBox
from stac_pydantic.utils import AutoValueEnum

from stac_fastapi.types.rfc3339 import rfc3339_str_to_datetime, str_to_interval

# Be careful: https://github.com/samuelcolvin/pydantic/issues/1423#issuecomment-642797287
NumType = Union[float, int]


class Limit(ConstrainedInt):
    """An positive integer that maxes out at 10,000."""

    ge: int = 1
    le: int = 10_000

    @classmethod
    def __get_validators__(cls) -> Generator[Callable[..., Any], None, None]:
        """Yield the relevant validators."""
        yield int_validator
        yield cls.validate

    @classmethod
    def validate(cls, value: int) -> int:
        """Validate the integer value."""
        if value < cls.ge:
            raise NumberNotGtError(limit_value=cls.ge)
        if value > cls.le:
            return cls.le
        return value


class Operator(str, AutoValueEnum):
    """Defines the set of operators supported by the API."""

    eq = auto()
    ne = auto()
    lt = auto()
    lte = auto()
    gt = auto()
    gte = auto()

    # TODO: These are defined in the spec but aren't currently implemented by the api
    # startsWith = auto()
    # endsWith = auto()
    # contains = auto()
    # in = auto()

    @DynamicClassAttribute
    def operator(self) -> Callable[[Any, Any], bool]:
        """Return python operator."""
        return getattr(operator, self._value_)


def str2list(x: str) -> Optional[List]:
    """Convert string to list base on , delimiter."""
    if x:
        return x.split(",")


@attr.s  # type:ignore
class APIRequest(abc.ABC):
    """Generic API Request base class."""

    def kwargs(self) -> Dict:
        """Transform api request params into format which matches the signature of the endpoint."""
        return self.__dict__


@attr.s
class BaseSearchGetRequest(APIRequest):
    """Base arguments for GET Request."""

    collections: Optional[str] = attr.ib(default=None, converter=str2list)
    ids: Optional[str] = attr.ib(default=None, converter=str2list)
    bbox: Optional[str] = attr.ib(default=None, converter=str2list)
    intersects: Optional[str] = attr.ib(default=None)
    datetime: Optional[str] = attr.ib(default=None)
    limit: Optional[int] = attr.ib(default=10)


class BaseSearchPostRequest(BaseModel):
    """Search model.

    Replace base model in STAC-pydantic as it includes additional fields,
    not in the core model.
    https://github.com/radiantearth/stac-api-spec/tree/master/item-search#query-parameter-table

    PR to fix this:
    https://github.com/stac-utils/stac-pydantic/pull/100
    """

    collections: Optional[List[str]]
    ids: Optional[List[str]]
    bbox: Optional[BBox]
    intersects: Optional[
        Union[Point, MultiPoint, LineString, MultiLineString, Polygon, MultiPolygon]
    ]
    datetime: Optional[str]
    limit: Optional[Limit] = 10

    @property
    def start_date(self) -> Optional[datetime]:
        """Extract the start date from the datetime string."""
        interval = str_to_interval(self.datetime)
        return interval[0] if interval else None

    @property
    def end_date(self) -> Optional[datetime]:
        """Extract the end date from the datetime string."""
        interval = str_to_interval(self.datetime)
        return interval[1] if interval else None

    @validator("intersects")
    def validate_spatial(cls, v, values):
        """Check bbox and intersects are not both supplied."""
        if v and values["bbox"]:
            raise ValueError("intersects and bbox parameters are mutually exclusive")
        return v

    @validator("bbox")
    def validate_bbox(cls, v: BBox):
        """Check order of supplied bbox coordinates."""
        if v:
            # Validate order
            if len(v) == 4:
                xmin, ymin, xmax, ymax = v
            else:
                xmin, ymin, min_elev, xmax, ymax, max_elev = v
                if max_elev < min_elev:
                    raise ValueError(
                        "Maximum elevation must greater than minimum elevation"
                    )

            if xmax < xmin:
                raise ValueError(
                    "Maximum longitude must be greater than minimum longitude"
                )

            if ymax < ymin:
                raise ValueError(
                    "Maximum longitude must be greater than minimum longitude"
                )

            # Validate against WGS84
            if xmin < -180 or ymin < -90 or xmax > 180 or ymax > 90:
                raise ValueError("Bounding box must be within (-180, -90, 180, 90)")

        return v

    @validator("datetime")
    def validate_datetime(cls, v):
        """Validate datetime."""
        if "/" in v:
            values = v.split("/")
        else:
            # Single date is interpreted as end date
            values = ["..", v]

        dates = []
        for value in values:
            if value == ".." or value == "":
                dates.append("..")
                continue

            # throws ValueError if invalid RFC 3339 string
            dates.append(rfc3339_str_to_datetime(value))

        if dates[0] == ".." and dates[1] == "..":
            raise ValueError(
                "Invalid datetime range, both ends of range may not be open"
            )

        if ".." not in dates and dates[0] > dates[1]:
            raise ValueError(
                "Invalid datetime range, must match format (begin_date, end_date)"
            )

        return v

    @property
    def spatial_filter(self) -> Optional[_GeometryBase]:
        """Return a geojson-pydantic object representing the spatial filter for the search request.

        Check for both because the ``bbox`` and ``intersects`` parameters are mutually exclusive.
        """
        if self.bbox:
            return Polygon(
                coordinates=[
                    [
                        [self.bbox[0], self.bbox[3]],
                        [self.bbox[2], self.bbox[3]],
                        [self.bbox[2], self.bbox[1]],
                        [self.bbox[0], self.bbox[1]],
                        [self.bbox[0], self.bbox[3]],
                    ]
                ]
            )
        if self.intersects:
            return self.intersects
        return
