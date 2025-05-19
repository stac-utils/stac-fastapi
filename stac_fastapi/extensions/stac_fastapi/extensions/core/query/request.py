"""Request model for the Query extension."""

from typing import Any, Dict, Optional

import attrs
from fastapi import Query
from pydantic import BaseModel, Field
from typing_extensions import Annotated

from stac_fastapi.types.search import APIRequest


@attrs.define
class QueryExtensionGetRequest(APIRequest):
    """Query Extension GET request model."""

    query: Annotated[
        Optional[str],
        Query(
            description="Allows additional filtering based on the properties of Item objects",  # noqa: E501
            openapi_examples={
                "user-provided": {"value": None},
                "cloudy": {"value": '{"eo:cloud_cover": {"gte": 95}}'},
            },
        ),
    ] = attrs.field(default=None)


class QueryExtensionPostRequest(BaseModel):
    """Query Extension POST request model."""

    query: Optional[Dict[str, Dict[str, Any]]] = Field(
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
