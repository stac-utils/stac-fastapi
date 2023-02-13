"""Request models for the fields extension."""

from __future__ import annotations

import copy
from typing import Dict, Optional, Set

import attr
from pydantic import BaseModel, Field

from stac_fastapi.types.config import Settings
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
                    if field_dict[parent] is not ...:
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
        recommended = self.into_recommended()

        return {
            "include": self._get_field_dict(recommended.include),
            "exclude": self._get_field_dict(recommended.exclude),
        }

    def into_recommended(self) -> PostFieldsExtension:
        """Convert this fields extension into the recommended sets.

        Based on https://github.com/stac-api-extensions/fields#includeexclude-semantics
        """
        include = self.include or set()
        exclude = (self.exclude or set()) - include
        # We can't do a simple set intersection, because we may include subkeys
        # while excluding everything else. E.g. we may want to include an
        # attribute of a specific asset, but exclude the rest of the asset
        # dictionary.
        default_include = copy.deepcopy(Settings.get().default_includes)
        if any(incl.startswith("assets.") for incl in include):
            default_include.remove("assets")
        include = (include | default_include) - exclude
        return PostFieldsExtension(include=include, exclude=exclude)


@attr.s
class FieldsExtensionGetRequest(APIRequest):
    """Additional fields for the GET request."""

    fields: Optional[str] = attr.ib(default=None, converter=str2list)


class FieldsExtensionPostRequest(BaseModel):
    """Additional fields and schema for the POST request."""

    fields: Optional[PostFieldsExtension] = Field(None)
