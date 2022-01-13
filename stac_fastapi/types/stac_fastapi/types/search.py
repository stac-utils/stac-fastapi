"""stac_fastapi.types.search module.

# TODO: replace with stac-pydantic
"""

import abc
import operator
from datetime import datetime
from enum import auto
from types import DynamicClassAttribute
from typing import Any, Callable, Dict, List, Optional, Union

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
from pydantic import BaseModel, conint, validator
from pydantic.datetime_parse import parse_datetime
from stac_pydantic.shared import BBox
from stac_pydantic.utils import AutoValueEnum

# Be careful: https://github.com/samuelcolvin/pydantic/issues/1423#issuecomment-642797287
NumType = Union[float, int]


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
    intersects: Optional[str] = attr.ib(default=None, converter=str2list)
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
    limit: Optional[conint(gt=0, le=10000)] = 10

    @property
    def start_date(self) -> Optional[datetime]:
        """Extract the start date from the datetime string."""
        if not self.datetime:
            return

        values = self.datetime.split("/")
        if len(values) == 1:
            return None
        if values[0] == "..":
            return None
        return parse_datetime(values[0])

    @property
    def end_date(self) -> Optional[datetime]:
        """Extract the end date from the datetime string."""
        if not self.datetime:
            return

        values = self.datetime.split("/")
        if len(values) == 1:
            return parse_datetime(values[0])
        if values[1] == "..":
            return None
        return parse_datetime(values[1])

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
            if value == "..":
                dates.append(value)
                continue

            parse_datetime(value)
            dates.append(value)

        if ".." not in dates:
            if parse_datetime(dates[0]) > parse_datetime(dates[1]):
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
