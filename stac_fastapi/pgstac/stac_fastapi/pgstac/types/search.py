"""stac_fastapi.types.search module."""

from typing import Dict, Optional

from pydantic import validator

from stac_fastapi.types.search import BaseSearchPostRequest


class PgstacSearch(BaseSearchPostRequest):
    """Search model.

    Overrides the validation for datetime from the base request model.
    """

    conf: Optional[Dict] = None

    @validator("filter_lang", pre=False, check_fields=False, always=True)
    def validate_query_uses_cql(cls, v, values):
        """Use of Query Extension is not allowed with cql2."""
        if values.get("query", None) is not None and v != "cql-json":
            raise ValueError(
                "Query extension is not available when using pgstac with cql2"
            )

        return v
