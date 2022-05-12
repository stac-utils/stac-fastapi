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

    # Build a shallow copy of included fields on an item, or a sub-tree of an item
    def include_fields(
        source: Dict[str, Any], fields: Optional[Set[str]]
    ) -> Dict[str, Any]:
        if not fields:
            return source

        clean_item: Dict[str, Any] = {}
        for key_path in fields or []:
            key_path_parts = key_path.split(".")
            key_root = key_path_parts[0]
            if key_root in source:
                if isinstance(source[key_root], dict) and len(key_path_parts) > 1:
                    # The root of this key path on the item is a dict, and the
                    # key path indicates a sub-key to be included. Walk the dict
                    # from the root key and get the full nested value to include.
                    value = include_fields(
                        source[key_root], fields=set([".".join(key_path_parts[1:])])
                    )

                    if isinstance(clean_item.get(key_root), dict):
                        # A previously specified key and sub-keys may have been included
                        # already, so do a deep merge update if the root key already exists.
                        dict_deep_update(clean_item[key_root], value)
                    else:
                        # The root key does not exist, so add it. Fields
                        # extension only allows nested referencing on dicts, so
                        # this won't overwrite anything.
                        clean_item[key_root] = value
                else:
                    # The item value to include is not a dict, or, it is a dict but the
                    # key path is for the whole value, not a sub-key. Include the entire
                    # value in the cleaned item.
                    clean_item[key_root] = source[key_root]
            else:
                # The key, or root key of a multi-part key, is not present in the item,
                # so it is ignored
                pass
        return clean_item

    # For an item built up for included fields, remove excluded fields. This
    # modifies `source` in place.
    def exclude_fields(source: Dict[str, Any], fields: Optional[Set[str]]) -> None:
        for key_path in fields or []:
            key_path_part = key_path.split(".")
            key_root = key_path_part[0]
            if key_root in source:
                if isinstance(source[key_root], dict) and len(key_path_part) > 1:
                    # Walk the nested path of this key to remove the leaf-key
                    exclude_fields(
                        source[key_root], fields=set([".".join(key_path_part[1:])])
                    )
                    # If, after removing the leaf-key, the root is now an empty
                    # dict, remove it entirely
                    if not source[key_root]:
                        del source[key_root]
                else:
                    # The key's value is not a dict, or there is no sub-key to remove. The
                    # entire key can be removed from the source.
                    source.pop(key_root, None)
            else:
                # The key to remove does not exist on the source, so it is ignored
                pass

    # Coalesce incoming type to a dict
    item = dict(item)

    clean_item = include_fields(item, include)

    # If, after including all the specified fields, there are no included properties,
    # return just id and collection.
    if not clean_item:
        return Item({"id": item.get(id), "collection": item.get("collection")})

    exclude_fields(clean_item, exclude)

    return Item(**clean_item)


def dict_deep_update(merge_to: Dict[str, Any], merge_from: Dict[str, Any]) -> None:
    """Perform a deep update of two dicts.

    merge_to is updated in-place with the values from merge_from.
    merge_from values take precedence over existing values in merge_to.
    """
    for k, v in merge_from.items():
        if (
            k in merge_to
            and isinstance(merge_to[k], dict)
            and isinstance(merge_from[k], dict)
        ):
            dict_deep_update(merge_to[k], merge_from[k])
        else:
            merge_to[k] = v
