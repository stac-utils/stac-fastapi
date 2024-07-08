"""Filter extension request models."""

from typing import Any, Dict, Literal, Optional

import attr
from fastapi import Query
from pydantic import BaseModel, Field
from typing_extensions import Annotated

from stac_fastapi.types.search import APIRequest

FilterLang = Literal["cql-json", "cql2-json", "cql2-text"]


@attr.s
class FilterExtensionGetRequest(APIRequest):
    """Filter extension GET request model."""

    filter: Annotated[Optional[str], Query()] = attr.ib(default=None)
    filter_crs: Annotated[Optional[str], Query(alias="filter-crs")] = attr.ib(
        default=None
    )
    filter_lang: Annotated[Optional[FilterLang], Query(alias="filter-lang")] = attr.ib(
        default="cql2-text"
    )


class FilterExtensionPostRequest(BaseModel):
    """Filter extension POST request model."""

    filter: Optional[Dict[str, Any]] = None
    filter_crs: Optional[str] = Field(alias="filter-crs", default=None)
    filter_lang: Optional[FilterLang] = Field(alias="filter-lang", default="cql2-json")
