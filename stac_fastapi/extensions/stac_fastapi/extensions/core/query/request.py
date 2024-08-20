"""Request model for the Query extension."""

from typing import Any, Dict, Optional

import attr
from fastapi import Query
from pydantic import BaseModel, Field
from typing_extensions import Annotated

from stac_fastapi.types.search import APIRequest


@attr.s
class QueryExtensionGetRequest(APIRequest):
    """Query Extension GET request model."""

    query: Annotated[
        Optional[str],
        Query(
            description="Allows additional filtering based on the properties of Item objects",  # noqa: E501
            json_schema_extra={
                "example": '{"eo:cloud_cover": {"gte": 95}}',
            },
        ),
    ] = attr.ib(default=None)


class QueryExtensionPostRequest(BaseModel):
    """Query Extension POST request model."""

    query: Optional[Dict[str, Dict[str, Any]]] = Field(
        None,
        description="Allows additional filtering based on the properties of Item objects",  # noqa: E501
        json_schema_extra={
            "example": {"eo:cloud_cover": {"gte": 95}},
        },
    )
