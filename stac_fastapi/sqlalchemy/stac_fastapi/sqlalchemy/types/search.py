"""stac_fastapi.types.search module.

# TODO: replace with stac-pydantic
"""

import logging
import operator
from dataclasses import dataclass
from enum import auto
from types import DynamicClassAttribute
from typing import Any, Callable, Dict, List, Optional, Set, Union

import sqlalchemy as sa
from pydantic import Field, ValidationError, conint, root_validator
from pydantic.error_wrappers import ErrorWrapper
from stac_pydantic.api import Search
from stac_pydantic.api.extensions.fields import FieldsExtension as FieldsBase
from stac_pydantic.utils import AutoValueEnum

from stac_fastapi.types.config import Settings

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


class FieldsExtension(FieldsBase):
    """FieldsExtension.

    Attributes:
        include: set of fields to include.
        exclude: set of fields to exclude.
    """

    include: Optional[Set[str]] = set()
    exclude: Optional[Set[str]] = set()

    @staticmethod
    def _get_field_dict(fields: Optional[Set[str]]) -> Dict:
        """Pydantic include/excludes notation.

        Internal method to create a dictionary for advanced include or exclude of pydantic fields on model export
        Ref: https://pydantic-docs.helpmanual.io/usage/exporting_models/#advanced-include-and-exclude
        """
        field_dict = {}
        for field in fields or []:
            if "." in field:
                parent, key = field.split(".")
                if parent not in field_dict:
                    field_dict[parent] = {key}
                else:
                    field_dict[parent].add(key)
            else:
                field_dict[field] = ...  # type:ignore
        return field_dict

    @property
    def filter_fields(self) -> Dict:
        """Create pydantic include/exclude expression.

        Create dictionary of fields to include/exclude on model export based on the included and excluded fields passed
        to the API
        Ref: https://pydantic-docs.helpmanual.io/usage/exporting_models/#advanced-include-and-exclude
        """
        # Always include default_includes, even if they
        # exist in the exclude list.
        include = (self.include or set()) - (self.exclude or set())
        include |= Settings.get().default_includes or set()

        return {
            "include": self._get_field_dict(include),
            "exclude": self._get_field_dict(self.exclude),
        }


class SQLAlchemySTACSearch(Search):
    """Search model."""

    # Make collections optional, default to searching all collections if none are provided
    collections: Optional[List[str]] = None
    # Override default field extension to include default fields and pydantic includes/excludes factory
    field: FieldsExtension = Field(FieldsExtension(), alias="fields")
    # Override query extension with supported operators
    query: Optional[Dict[Queryables, Dict[Operator, Any]]]
    token: Optional[str] = None
    limit: Optional[conint(gt=0, le=10000)] = 10

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
                        SQLAlchemySTACSearch,
                    )
        return values
