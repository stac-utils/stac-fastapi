"""stac_fastapi.types.search module."""

from copy import deepcopy
from typing import Any, Dict, Optional, Set

from pydantic import validator
from starlette.requests import Request

from stac_fastapi.types.search import BaseSearchPostRequest
from stac_fastapi.types.stac import Item


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


class PgStacSearchContent:
    """Perform post-search processing when settings prevent pgstac from doing so in the database."""

    def __init__(self, client, request: Request):
        """Set result state for a single search."""
        self.base_items = {}
        self.client = client
        self.request = request

    async def get_base_item(self, collection_id: str):
        """Return the base item for the collection."""
        if collection_id not in self.base_items:
            self.base_items[collection_id] = await self.client.get_base_item(
                collection_id,
                request=self.request,
            )
        return self.base_items[collection_id]

    async def hydrate(
        self,
        item: Dict[str, Any],
        include: Optional[Set] = None,
        exclude: Optional[Set] = None,
    ) -> Item:
        """Hydrate item in-place with base_item properties, while honoring include/exclude sets."""

        def merge(b: Dict[str, Any], i: Dict[str, Any]):
            for key in b:
                if key in i:
                    if isinstance(b[key], dict) and isinstance(i.get(key), dict):
                        # Recurse on dicts to merge values
                        merge(b[key], i[key])
                    elif b[key] == i.get(key):
                        # Matching key/value is a no-op
                        pass
                    elif isinstance(b[key], list) and isinstance(i.get(key), list):
                        # Merge unequal lists
                        i[key].extend(b[key])
                else:
                    # Keys in base item that are not in item are simply copied over
                    i[key] = deepcopy(b[key])

        base_item = await self.get_base_item(item["collection"])
        merge(base_item, item)
        return item
