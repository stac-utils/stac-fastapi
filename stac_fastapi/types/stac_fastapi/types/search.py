"""stac_fastapi.types.search module.

"""

import abc
from typing import Dict, List, Optional

import attr
from pydantic import PositiveInt
from pydantic.functional_validators import AfterValidator
from stac_pydantic.api import Search
from typing_extensions import Annotated


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
    bbox: Optional[str] = attr.ib(default=None, converter=str2list)
    intersects: Optional[str] = attr.ib(default=None)
    datetime: Optional[str] = attr.ib(default=None)
    limit: Optional[int] = attr.ib(default=10)


class BaseSearchPostRequest(Search):
    """Base arguments for POST Request."""

    limit: Optional[Limit] = 10
