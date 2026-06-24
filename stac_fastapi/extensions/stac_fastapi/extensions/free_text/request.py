"""Request model for the Free-text extension."""

from typing import Annotated

import attr
from fastapi import Query
from pydantic import BaseModel, Field

from stac_fastapi.types.search import APIRequest


def _ft_converter(
    val: Annotated[
        str | None,
        Query(
            description="Parameter to perform free-text queries against STAC metadata",
            openapi_examples={
                "user-provided": {"value": None},
                "Coastal": {"value": "ocean,coast"},
            },
        ),
    ] = None,
) -> list[str] | None:
    if val:
        return val.split(",")
    return None


@attr.s
class FreeTextExtensionGetRequest(APIRequest):
    """Free-text Extension GET request model."""

    q: list[str] | None = attr.ib(default=None, converter=_ft_converter)


class FreeTextExtensionPostRequest(BaseModel):
    """Free-text Extension POST request model."""

    q: list[str] | None = Field(
        None,
        description="Parameter to perform free-text queries against STAC metadata",
    )


@attr.s
class FreeTextAdvancedExtensionGetRequest(APIRequest):
    """Free-text Extension GET request model."""

    q: Annotated[
        str | None,
        Query(
            description="Parameter to perform free-text queries against STAC metadata",
            openapi_examples={
                "user-provided": {"value": None},
                "Coastal": {"value": "ocean,coast"},
            },
        ),
    ] = attr.ib(default=None)


class FreeTextAdvancedExtensionPostRequest(BaseModel):
    """Free-text Extension POST request model."""

    q: str | None = Field(
        None,
        description="Parameter to perform free-text queries against STAC metadata",
    )
