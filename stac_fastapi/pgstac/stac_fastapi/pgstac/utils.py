"""stac-fastapi utility methods."""
from typing import Any, Dict, Optional, Set, Union

from stac_fastapi.types.stac import Item


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
