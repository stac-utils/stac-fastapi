"""stac_fastapi.types.search module."""

import operator
from enum import auto
from types import DynamicClassAttribute
from typing import Any, Callable, Dict, List, Optional, Set, Union

from pydantic import Field, root_validator, validator
from stac_pydantic.api import Search
from stac_pydantic.api.extensions.fields import FieldsExtension as FieldsBase
from stac_pydantic.utils import AutoValueEnum

from stac_fastapi.types.config import Settings

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


class PgstacSearch(Search):
    """Search model."""

    # Make collections optional, default to searching all collections if none are provided
    collections: Optional[List[str]] = None
    ids: Optional[List[str]] = None
    # Override default field extension to include default fields and pydantic includes/excludes factory
    fields: FieldsExtension = Field(FieldsExtension())
    # Override query extension with supported operators
    query: Optional[Dict[str, Dict[Operator, Any]]]
    token: Optional[str] = None
    datetime: Optional[str] = None
    sortby: Any

    @root_validator(pre=True)
    def validate_query_fields(cls, values: Dict) -> Dict:
        """Pgstac does not require the base validator for query fields."""
        return values

    @validator("datetime")
    def validate_datetime(cls, v):
        """Pgstac does not require the base validator for datetime."""
        return v
