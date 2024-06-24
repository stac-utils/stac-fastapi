"""Request models for the fields extension."""

import warnings
from dataclasses import dataclass
from typing import Dict, Optional, Set

from fastapi import Query
from pydantic import BaseModel, Field
from typing_extensions import Annotated

from stac_fastapi.types.search import APIRequest, str2list


class PostFieldsExtension(BaseModel):
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

        Internal method to create a dictionary for advanced include or exclude
        of pydantic fields on model export
        Ref: https://pydantic-docs.helpmanual.io/usage/exporting_models/#advanced-include-and-exclude
        """
        field_dict = {}
        for field in fields or []:
            if "." in field:
                parent, key = field.split(".")
                if parent not in field_dict:
                    field_dict[parent] = {key}
                else:
                    if field_dict[parent] is not ...:
                        field_dict[parent].add(key)
            else:
                field_dict[field] = ...  # type:ignore

        return field_dict

    @property
    def filter_fields(self) -> Dict:
        """Create pydantic include/exclude expression.

        Create dictionary of fields to include/exclude on model export based on
        the included and excluded fields passed to the API
        Ref: https://pydantic-docs.helpmanual.io/usage/exporting_models/#advanced-include-and-exclude
        """
        warnings.warn(
            """The `PostFieldsExtension.filter_fields`
            method is deprecated and will be removed in 3.0.""",
            DeprecationWarning,
            stacklevel=1,
        )

        # Always include default_includes, even if they
        # exist in the exclude list.
        include = (self.include or set()) - (self.exclude or set())
        include |= set()

        return {
            "include": self._get_field_dict(include),
            "exclude": self._get_field_dict(self.exclude),
        }


@dataclass
class FieldsExtensionGetRequest(APIRequest):
    """Additional fields for the GET request."""

    fields: Annotated[Optional[str], Query()] = None

    def __post_init__(self):
        """convert attributes."""
        if self.fields:
            self.fields = str2list(self.fields)  # type: ignore


class FieldsExtensionPostRequest(BaseModel):
    """Additional fields and schema for the POST request."""

    fields: Optional[PostFieldsExtension] = Field(PostFieldsExtension())
