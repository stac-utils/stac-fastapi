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
        """If using query syntax, forces cql-json."""
        retval = v
        if values.get("query", None) is not None:
            retval = "cql-json"
        if values.get("collections", None) is not None:
            retval = "cql-json"
        if values.get("ids", None) is not None:
            retval = "cql-json"
        if values.get("datetime", None) is not None:
            retval = "cql-json"
        if values.get("bbox", None) is not None:
            retval = "cql-json"
        if v == "cql2-json" and retval == "cql-json":
            raise ValueError(
                "query, collections, ids, datetime, and bbox"
                "parameters are not available in cql2-json"
            )
        return retval
