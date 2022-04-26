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


class PgstacSearchContent:
    """
    Perform post-search processing of items if pgstac is set to `nohydrate`.

    This includes:
        - Hydrating the items with the collection's base_item properties
        - Filtering the fields according to the fields extension's include/exclude sets
        - Removing invalid assets

    Note that these actions are destructive to the item instances passed in.
    """

    def __init__(self, client, request: Request):
        """Set result state for a single search."""
        self.base_items = {}
        self.client = client
        self.request = request

    async def hydrate(
        self,
        item: Dict[str, Any],
        include: Set = None,
        exclude: Set = None,
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
                        i[key].extend(deepcopy(b[key]))
                else:
                    # Keys in base item that are not in item are simply copied over
                    i[key] = deepcopy(b[key])

        base_item = await self._get_base_item(item["collection"])
        merge(base_item, item)
        cleaned_item = self._filter_fields(item, include, exclude)
        cleaned_item = self._remove_invalid_assets(cleaned_item)

        return Item(**cleaned_item)

    async def _get_base_item(self, collection_id: str):
        """Return the base item for the collection and cache by collection id."""
        if collection_id not in self.base_items:
            self.base_items[collection_id] = await self.client.get_base_item(
                collection_id,
                request=self.request,
            )
        return self.base_items[collection_id]

    def _filter_fields(
        self,
        item: Item,
        include: Set = None,
        exclude: Set = None,
    ):
        """Preserve and remove fields as indicated by the fields extension include/exclude sets."""
        if not include and not exclude:
            return item

        clean_item = {}
        for key_path in include or []:
            keys = key_path.split(".")
            root = keys[0]
            if root in item:
                if isinstance(item[root], dict) and len(keys) > 1:
                    # Recurse on "includes" key paths notation for sub-keys
                    clean_item[root] = self._filter_fields(
                        item[root], include=[".".join(keys[1:])]
                    )
                else:
                    clean_item[root] = item[root]

        for key_path in exclude or []:
            keys = key_path.split(".")
            root = keys[0]
            if root in item:
                if isinstance(item[root], dict) and len(keys) > 1:
                    # Recurse on "excludes" key paths notation for sub-keys
                    clean_item[root] = self._filter_fields(
                        item[root], exclude=[".".join(keys[1:])]
                    )
                else:
                    # Item is marked for exclusion
                    clean_item = item
                    clean_item.pop(root, None)
            else:
                # Key is not in item, so preserve the item without modification
                clean_item = item

        return clean_item

    def _remove_invalid_assets(self, item: Item):
        """
        Remove invalid assets from the item.

        Pgstac may return assets without an href if assets aren't uniformly
        distributed across all items. In this case, the asset without an href
        is removed from the item.
        """
        if "assets" in item:
            item["assets"] = {k: v for k, v in item["assets"].items() if "href" in v}

        return item
