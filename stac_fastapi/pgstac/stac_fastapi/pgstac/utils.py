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
        return Item(**item)

    item = dict(item)

    clean_item: Dict[str, Any] = {}
    for key_path in include or []:
        keys = key_path.split(".")
        root = keys[0]
        if root in item:
            if isinstance(item[root], dict) and len(keys) > 1:
                # Recurse on "includes" key paths notation for sub-keys
                clean_item[root] = filter_fields(
                    item[root], include=set([".".join(keys[1:])])
                )
            else:
                clean_item[root] = item[root]

    for key_path in exclude or []:
        keys = key_path.split(".")
        root = keys[0]
        if root in item:
            if isinstance(item[root], dict) and len(keys) > 1:
                # Recurse on "excludes" key paths notation for sub-keys
                clean_item[root] = filter_fields(
                    item[root], exclude=set([".".join(keys[1:])])
                )
            else:
                # Item is marked for exclusion
                clean_item = item
                clean_item.pop(root, None)
        else:
            # Key is not in item, so preserve the item without modification
            clean_item = item

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
