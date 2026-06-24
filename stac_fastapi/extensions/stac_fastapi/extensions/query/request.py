"""Request model for the Query extension."""

from typing import Annotated, Any

import attr
from fastapi import Query
from pydantic import BaseModel, Field

from stac_fastapi.types.search import APIRequest


@attr.s
class QueryExtensionGetRequest(APIRequest):
    """Query Extension GET request model."""

    query: Annotated[
        str | None,
        Query(
            description="Allows additional filtering based on the properties of Item objects",  # noqa: E501
            openapi_examples={
                "user-provided": {"value": None},
                "cloudy": {"value": '{"eo:cloud_cover": {"gte": 95}}'},
            },
        ),
    ] = attr.ib(default=None)


class QueryExtensionPostRequest(BaseModel):
    """Query Extension POST request model."""

    query: dict[str, dict[str, Any]] | None = Field(
        None,
        description="Allows additional filtering based on the properties of Item objects",  # noqa: E501
        json_schema_extra={
            "examples": [
                # user-provided
                None,
                # cloudy
                '{"eo:cloud_cover": {"gte": 95}}',
            ],
        },
    )
