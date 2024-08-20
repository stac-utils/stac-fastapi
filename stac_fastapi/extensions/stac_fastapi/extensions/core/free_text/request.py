"""Request model for the Free-text extension."""

from typing import List, Optional

import attr
from fastapi import Query
from pydantic import BaseModel, Field
from typing_extensions import Annotated

from stac_fastapi.types.search import APIRequest, str2list


def _ft_converter(
    val: Annotated[
        Optional[str],
        Query(
            description="Parameter to perform free-text queries against STAC metadata",
            json_schema_extra={
                "example": "ocean,coast",
            },
        ),
    ] = None,
) -> Optional[List[str]]:
    return str2list(val)


@attr.s
class FreeTextExtensionGetRequest(APIRequest):
    """Free-text Extension GET request model."""

    q: Optional[List[str]] = attr.ib(default=None, converter=_ft_converter)


class FreeTextExtensionPostRequest(BaseModel):
    """Free-text Extension POST request model."""

    q: Optional[List[str]] = Field(
        None,
        description="Parameter to perform free-text queries against STAC metadata",
    )


@attr.s
class FreeTextAdvancedExtensionGetRequest(APIRequest):
    """Free-text Extension GET request model."""

    q: Annotated[
        Optional[str],
        Query(
            description="Parameter to perform free-text queries against STAC metadata",
            json_schema_extra={
                "example": "ocean,coast",
            },
        ),
    ] = attr.ib(default=None)


class FreeTextAdvancedExtensionPostRequest(BaseModel):
    """Free-text Extension POST request model."""

    q: Optional[str] = Field(
        None,
        description="Parameter to perform free-text queries against STAC metadata",
    )
