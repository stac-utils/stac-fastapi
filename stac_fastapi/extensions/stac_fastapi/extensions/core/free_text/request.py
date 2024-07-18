"""Request model for the Free-text extension."""

from typing import Optional

import attr
from fastapi import Query
from pydantic import BaseModel, Field
from typing_extensions import Annotated

from stac_fastapi.types.search import APIRequest


@attr.s
class FreeTextExtensionGetRequest(APIRequest):
    """Free-text Extension GET request model."""

    q: Annotated[
        Optional[str],
        Query(
            description="Parameter to perform free-text queries against STAC metadata",
            json_schema_extra={
                "example": "item1,item2",
            },
        ),
    ] = attr.ib(default=None)


class FreeTextExtensionPostRequest(BaseModel):
    """Free-text Extension POST request model."""

    q: Optional[str] = Field(
        None,
        description="Parameter to perform free-text queries against STAC metadata",
    )
