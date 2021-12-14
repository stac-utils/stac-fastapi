"""Filter extension request models."""

from enum import Enum
from typing import Any, Dict, Optional

import attr
from pydantic import BaseModel, Field

from stac_fastapi.types.search import APIRequest


class FilterLang(str, Enum):
    """Choices for filter-lang value in a POST request.

    Based on https://github.com/radiantearth/stac-api-spec/tree/master/fragments/filter#queryables

    Note the addition of cql2-json, which is used by the pgstac backend,
    but is not included in the spec above.
    """

    cql_json = "cql-json"
    cql2_json = "cql2-json"
    cql_text = "cql-text"


@attr.s
class FilterExtensionGetRequest(APIRequest):
    """Filter extension GET request model."""

    filter: Optional[str] = attr.ib(default=None)


class FilterExtensionPostRequest(BaseModel):
    """Filter extension POST request model."""

    filter: Optional[Dict[str, Any]] = None
    filter_crs: Optional[str] = Field(alias="filter-crs", default=None)
    filter_lang: Optional[FilterLang] = Field(alias="filter-lang", default=None)
