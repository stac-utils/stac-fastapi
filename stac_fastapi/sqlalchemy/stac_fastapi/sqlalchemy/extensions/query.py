"""STAC SQLAlchemy specific query search model.

# TODO: replace with stac-pydantic
"""

import logging
import operator
from dataclasses import dataclass
from enum import auto
from types import DynamicClassAttribute
from typing import Any, Callable, Dict, Optional, Union

import sqlalchemy as sa
from pydantic import BaseModel, ValidationError, root_validator
from pydantic.error_wrappers import ErrorWrapper
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
    """Queryable fields.

    Define an enum of queryable fields and their data type.  Queryable fields are explicitly defined for two reasons:
        1. So the caller knows which fields they can query by
        2. Because JSONB queries with sqlalchemy ORM require casting the type of the field at runtime
            (see ``QueryableTypes``)

    # TODO: Let the user define these in a config file
    """

    orientation = auto()
    gsd = auto()
    epsg = "proj:epsg"
    height = auto()
    width = auto()
    minzoom = "cog:minzoom"
    maxzoom = "cog:maxzoom"
    dtype = "cog:dtype"
    foo = "foo"

    def __str__(self) -> str:
        """Return the Queryable's value as its __str__.

        Python 3.11 changed the default __str__ behavior for Enums, and since we
        can't use StrEnum (it was introduced in 3.11), we need to define our
        expected behavior explicitly.
        """
        return self.value


@dataclass
class QueryableTypes:
    """Defines a set of queryable fields.

    # TODO: Let the user define these in a config file
    # TODO: There is a much better way of defining this field <> type mapping than two enums with same keys
    """

    orientation = sa.String
    gsd = sa.Float
    epsg = sa.Integer
    height = sa.Integer
    width = sa.Integer
    minzoom = sa.Integer
    maxzoom = sa.Integer
    dtype = sa.String


class QueryExtensionPostRequest(BaseModel):
    """Queryable validation.

    Add queryables validation to the POST request
    to raise errors for unsupported querys.
    """

    query: Optional[Dict[Queryables, Dict[Operator, Any]]]

    @root_validator(pre=True)
    def validate_query_fields(cls, values: Dict) -> Dict:
        """Validate query fields."""
        logger.debug(f"Validating SQLAlchemySTACSearch {cls} {values}")
        if "query" in values and values["query"]:
            queryable_fields = Queryables.__members__.values()
            for field_name in values["query"]:
                if field_name not in queryable_fields:
                    raise ValidationError(
                        [
                            ErrorWrapper(
                                ValueError(f"Cannot search on field: {field_name}"),
                                "STACSearch",
                            )
                        ],
                        QueryExtensionPostRequest,
                    )
        return values


class QueryExtension(QueryExtensionBase):
    """Query Extenson.

    Override the POST request model to add validation against
    supported fields
    """

    POST = QueryExtensionPostRequest
