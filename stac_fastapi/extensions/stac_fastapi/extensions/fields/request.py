"""Request models for the fields extension."""

from typing import Annotated

import attr
from fastapi import Query
from pydantic import BaseModel, Field

from stac_fastapi.types.search import APIRequest, str2list


class PostFieldsExtension(BaseModel):
    """FieldsExtension.

    Attributes:
        include: set of fields to include.
        exclude: set of fields to exclude.
    """

    include: set[str] | None = set()
    exclude: set[str] | None = set()

    @staticmethod
    def _get_field_dict(fields: set[str] | None) -> dict:
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


def _fields_converter(
    val: Annotated[
        str | None,
        Query(
            description="Include or exclude fields from items body.",
            openapi_examples={
                "user-provided": {"value": None},
                "datetime": {"value": "properties.datetime"},
            },
        ),
    ] = None,
) -> list[str] | None:
    return str2list(val)


@attr.s
class FieldsExtensionGetRequest(APIRequest):
    """Additional fields for the GET request."""

    fields: list[str] | None = attr.ib(default=None, converter=_fields_converter)


class FieldsExtensionPostRequest(BaseModel):
    """Additional fields and schema for the POST request."""

    fields: PostFieldsExtension | None = Field(
        PostFieldsExtension(),
        description="Include or exclude fields from items body.",
    )
