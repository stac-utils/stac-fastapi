"""STAC SQLAlchemy specific query search model.

# TODO: replace with stac-pydantic
"""

import logging
import operator
from dataclasses import dataclass
from enum import auto
from types import DynamicClassAttribute
from typing import Any, Callable, Dict, Optional, Union

from pydantic import BaseModel, root_validator
from stac_pydantic.utils import AutoValueEnum

from stac_fastapi.extensions.core.query import QueryExtension as QueryExtensionBase

logger = logging.getLogger("uvicorn")
logger.setLevel(logging.INFO)
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


class Queryables(str, AutoValueEnum):
    """Queryable fields."""

    ...


@dataclass
class QueryableTypes:
    """Defines a set of queryable fields."""

    ...


class QueryExtensionPostRequest(BaseModel):
    """Queryable validation.

    Add queryables validation to the POST request
    to raise errors for unsupported querys.
    """

    query: Optional[Dict[Queryables, Dict[Operator, Any]]]

    @root_validator(pre=True)
    def validate_query_fields(cls, values: Dict) -> Dict:
        """Validate query fields."""
        ...


class QueryExtension(QueryExtensionBase):
    """Query Extenson.

    Override the POST request model to add validation against
    supported fields
    """

    ...
