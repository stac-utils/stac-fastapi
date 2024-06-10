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
from fastapi import Path
from geojson_pydantic.geometries import (
    GeometryCollection,
    LineString,
    MultiLineString,
    MultiPoint,
    MultiPolygon,
    Point,
    Polygon,
    _GeometryBase,
)
from pydantic import BaseModel, ConstrainedInt, Field, validator
from pydantic.errors import NumberNotGtError
from pydantic.validators import int_validator
from stac_pydantic.api import Search
from stac_pydantic.shared import BBox
from stac_pydantic.utils import AutoValueEnum

from stac_fastapi.types.rfc3339 import DateTimeType, str_to_interval

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


def str2bbox(x: str) -> Optional[BBox]:
    """Convert string to BBox based on , delimiter."""
    if x:
        t = tuple(float(v) for v in str2list(x))
        assert len(t) == 4
        return t


@attr.s  # type:ignore
class APIRequest(abc.ABC):
    """Generic API Request base class."""

    def kwargs(self) -> Dict:
        """Transform api request params into format which matches the signature of the
        endpoint."""
        return self.__dict__


@attr.s
class BaseSearchGetRequest(APIRequest):
    """Base arguments for GET Request."""

    catalogs: Optional[str] = attr.ib(default=None, converter=str2list)
    collections: Optional[str] = attr.ib(default=None, converter=str2list)
    ids: Optional[str] = attr.ib(default=None, converter=str2list)
    bbox: Optional[BBox] = attr.ib(default=None, converter=str2bbox)
    intersects: Optional[str] = attr.ib(default=None, converter=str2list)
    datetime: Optional[DateTimeType] = attr.ib(default=None, converter=str_to_interval)
    limit: Optional[int] = attr.ib(default=10)


@attr.s
class BaseCatalogSearchGetRequest(APIRequest):
    """Base arguments for GET Request for searching items in a specific catalog."""

    catalog_id: str = attr.ib(default=Path(..., description="Catalog ID"))
    collections: Optional[str] = attr.ib(default=None, converter=str2list)
    ids: Optional[str] = attr.ib(default=None, converter=str2list)
    bbox: Optional[BBox] = attr.ib(default=None, converter=str2bbox)
    intersects: Optional[str] = attr.ib(default=None, converter=str2list)
    datetime: Optional[DateTimeType] = attr.ib(default=None, converter=str_to_interval)
    limit: Optional[int] = attr.ib(default=10)


class BaseSearchPostRequest(Search):
    """Search model.

    Replace base model in STAC-pydantic as it includes additional fields, not in the core
    model.
    https://github.com/radiantearth/stac-api-spec/tree/master/item-search#query-parameter-table

    PR to fix this:
    https://github.com/stac-utils/stac-pydantic/pull/100
    """

    catalogs: Optional[List[str]]
    collections: Optional[List[str]]
    ids: Optional[List[str]]
    bbox: Optional[BBox]
    intersects: Optional[
        Union[
            Point,
            MultiPoint,
            LineString,
            MultiLineString,
            Polygon,
            MultiPolygon,
            GeometryCollection,
        ]
    ]
    datetime: Optional[DateTimeType]
    limit: Optional[Limit] = Field(default=10)

    @property
    def start_date(self) -> Optional[datetime]:
        """Extract the start date from the datetime string."""
        return self.datetime[0] if self.datetime else None

    @property
    def end_date(self) -> Optional[datetime]:
        """Extract the end date from the datetime string."""
        return self.datetime[1] if self.datetime else None

    @validator("intersects")
    def validate_spatial(cls, v, values):
        """Check bbox and intersects are not both supplied."""
        if v and values["bbox"]:
            raise ValueError("intersects and bbox parameters are mutually exclusive")
        return v

    @validator("bbox", pre=True)
    def validate_bbox(cls, v: Union[str, BBox]) -> BBox:
        """Check order of supplied bbox coordinates."""
        if v:
            if type(v) == str:
                v = str2bbox(v)
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

    @validator("datetime", pre=True)
    def validate_datetime(cls, v: Union[str, DateTimeType]) -> DateTimeType:
        """Parse datetime."""
        if type(v) == str:
            v = str_to_interval(v)
        return v

    @property
    def spatial_filter(self) -> Optional[_GeometryBase]:
        """Return a geojson-pydantic object representing the spatial filter for the search
        request.

        Check for both because the ``bbox`` and ``intersects`` parameters are
        mutually exclusive.
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


class BaseCatalogSearchPostRequest(Search):
    """Search model for searching items in a specific catalog (same as BaseSearchPostRequest excluding catalogs)."""

    collections: Optional[List[str]] = None
    ids: Optional[List[str]] = None
    bbox: Optional[BBox] = None
    intersects: Optional[
        Union[
            Point,
            MultiPoint,
            LineString,
            MultiLineString,
            Polygon,
            MultiPolygon,
            GeometryCollection,
        ]
    ] = None
    datetime: Optional[DateTimeType] = None
    limit: Optional[Limit] = 10

    @property
    def start_date(self) -> Optional[datetime]:
        """Extract the start date from the datetime string."""
        return self.datetime[0] if self.datetime else None

    @property
    def end_date(self) -> Optional[datetime]:
        """Extract the end date from the datetime string."""
        return self.datetime[1] if self.datetime else None

    @validator("intersects")
    def validate_spatial(cls, v, values):
        """Check bbox and intersects are not both supplied."""
        if v and values["bbox"]:
            raise ValueError("intersects and bbox parameters are mutually exclusive")
        return v

    @validator("bbox", pre=True)
    def validate_bbox(cls, v: Union[str, BBox]) -> BBox:
        """Check order of supplied bbox coordinates."""
        if v:
            if type(v) == str:
                v = str2bbox(v)
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

    @validator("datetime", pre=True)
    def validate_datetime(cls, v: Union[str, DateTimeType]) -> DateTimeType:
        """Parse datetime."""
        if type(v) == str:
            v = str_to_interval(v)
        return v

    @property
    def spatial_filter(self) -> Optional[_GeometryBase]:
        """Return a geojson-pydantic object representing the spatial filter for the search
        request.

        Check for both because the ``bbox`` and ``intersects`` parameters are
        mutually exclusive.
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


@attr.s
class CatalogSearchPostRequest(APIRequest):
    """Search model for searching items in a specific catalog."""

    catalog_id: str = attr.ib(default=Path(..., description="Catalog ID"))
    search_request: BaseCatalogSearchPostRequest = attr.ib(default=None)


@attr.s
class BaseCollectionSearchGetRequest(APIRequest):
    """Base arguments for Collection Search GET Request."""

    bbox: Optional[BBox] = attr.ib(default=None, converter=str2bbox)
    datetime: Optional[DateTimeType] = attr.ib(default=None, converter=str_to_interval)
    limit: Optional[int] = attr.ib(default=10)
    q: Optional[str] = attr.ib(default=None)


class BaseCollectionSearchPostRequest(BaseModel):
    """Search model.
    Replace base model in STAC-pydantic as it includes additional fields, not in the core
    model.
    """

    bbox: Optional[BBox]
    datetime: Optional[DateTimeType]
    limit: Optional[Limit] = 10
    q: Optional[str]


@attr.s
class BaseDiscoverySearchGetRequest(APIRequest):
    """Base arguments for Collection Search GET Request."""

    q: Optional[str] = attr.ib(default=None)
    limit: Optional[int] = attr.ib(default=10)


class BaseDiscoverySearchPostRequest(BaseModel):
    """Search model.

    Replace base model in STAC-pydantic as it includes additional fields, not in the core
    model.
    """

    q: Optional[str]
    limit: Optional[Limit] = Field(default=10)
