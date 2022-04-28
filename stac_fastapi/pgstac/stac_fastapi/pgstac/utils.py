"""stac-fastapi utility methods."""
from copy import deepcopy
from typing import Any, Dict, Optional, Set, Union

from stac_fastapi.pgstac.types.base_item_cache import BaseItemCache
from stac_fastapi.types.stac import Item


async def hydrate(
    item: Union[Item, Dict[str, Any]], base_item_cache: BaseItemCache
) -> Item:
    """Hydrate item in-place with base_item properties.

    This will not perform a deep copy; values of the original item will be referenced
    in the return item.
    """
    item = dict(item)

    # Merge will mutate i, but create deep copies of values in the base item
    # This will prevent the base item values from being mutated, e.g. by
    # filtering out fields in `filter_fields`.
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

    base_item = await base_item_cache.get(item["collection"])
    merge(base_item, item)
    return Item(**item)


def filter_fields(
    item: Union[Item, Dict[str, Any]],
    include: Optional[Set[str]] = None,
    exclude: Optional[Set[str]] = None,
) -> Item:
    """Preserve and remove fields as indicated by the fields extension include/exclude sets.

    Returns a shallow copy of the Item with the fields filtered.

    This will not perform a deep copy; values of the original item will be referenced
    in the return item.
    """
    if not include and not exclude:
        return item

    # Build a shallow copy of included fields on item
    def include_fields(
        full_item: Dict[str, Any], fields: Optional[Set[str]]
    ) -> Dict[str, Any]:
        if not fields:
            return full_item

        clean_item: Dict[str, Any] = {}
        for key_path in fields or []:
            keys = key_path.split(".")
            root = keys[0]
            if root in full_item:
                if isinstance(full_item[root], dict) and len(keys) > 1:
                    # Recurse on "includes" key paths notation for sub-keys
                    clean_item[root] = include_fields(
                        full_item[root], fields=set([".".join(keys[1:])])
                    )
                else:
                    clean_item[root] = full_item[root]
        return clean_item

    # For an item built up for included fields, remove excluded fields
    def exclude_fields(
        clean_item: Dict[str, Any], fields: Optional[Set[str]]
    ) -> Dict[str, Any]:
        if not clean_item and not fields:
            return item

        for key_path in fields or []:
            keys = key_path.split(".")
            root = keys[0]
            if root in clean_item:
                if isinstance(clean_item[root], dict) and len(keys) > 1:
                    # Recurse on "excludes" key path notation for sub-keys
                    clean_item[root] = exclude_fields(
                        clean_item[root], fields=set([".".join(keys[1:])])
                    )
                    # Remove root key entirely if it is now empty
                    if not clean_item[root]:
                        del clean_item[root]
                else:
                    clean_item.pop(root, None)

        return clean_item

    # Coalesce incoming type to a dict
    item = dict(item)

    clean_item = include_fields(item, include)
    clean_item = exclude_fields(clean_item, exclude)
    return Item(**clean_item)


def remove_invalid_assets(item: Item) -> None:
    """
    Remove invalid assets from the item. This method mutates the Item.

    Pgstac may return assets without an href if assets aren't uniformly
    distributed across all items. In this case, the asset without an href
    is removed from the item.
    """
    if "assets" in item:
        item["assets"] = {k: v for k, v in item["assets"].items() if "href" in v}
