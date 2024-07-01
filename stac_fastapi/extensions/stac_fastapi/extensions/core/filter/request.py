"""Filter extension request models."""

from dataclasses import dataclass
from typing import Any, Dict, Literal, Optional

from fastapi import Query
from pydantic import BaseModel, Field
from typing_extensions import Annotated

from stac_fastapi.types.search import APIRequest

FilterLang = Literal["cql-json", "cql2-json", "cql2-text"]


@dataclass
class FilterExtensionGetRequest(APIRequest):
    """Filter extension GET request model."""

    filter: Annotated[Optional[str], Query()] = None
    filter_crs: Annotated[Optional[str], Query(alias="filter-crs")] = None
    filter_lang: Annotated[Optional[FilterLang], Query(alias="filter-lang")] = "cql2-text"


class FilterExtensionPostRequest(BaseModel):
    """Filter extension POST request model."""

    filter: Optional[Dict[str, Any]] = None
    filter_crs: Optional[str] = Field(alias="filter-crs", default=None)
    filter_lang: Optional[FilterLang] = Field(alias="filter-lang", default="cql2-json")
