"""stac_fastapi.types.search module.

"""

import abc
from typing import Dict, List, Optional, Union

import attr
from pydantic import PositiveInt
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


# Be careful: https://github.com/samuelcolvin/pydantic/issues/1423#issuecomment-642797287
NumType = Union[float, int]
Limit = Annotated[PositiveInt, AfterValidator(crop)]


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

    collections: Optional[str] = attr.ib(default=None, converter=str2list)
    ids: Optional[str] = attr.ib(default=None, converter=str2list)
    bbox: Optional[BBox] = attr.ib(default=None, converter=str2bbox)
    intersects: Optional[str] = attr.ib(default=None)
    datetime: Optional[DateTimeType] = attr.ib(default=None, converter=str_to_interval)
    limit: Optional[int] = attr.ib(default=10)


class BaseSearchPostRequest(Search):
    """Base arguments for POST Request."""

    limit: Optional[Limit] = 10
