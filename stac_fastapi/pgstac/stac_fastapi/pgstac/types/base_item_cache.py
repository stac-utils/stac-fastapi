import abc
from typing import Any, Callable, Coroutine, Dict


class BaseItemCache(abc.ABC):
    """
    A cache that returns a base item for a collection.

    If no base item is found in the cache, use the fetch_base_item function
    to fetch the base item from pgstac.
    """

    def __init__(
        self, fetch_base_item: Callable[[str], Coroutine[Any, Any, Dict[str, Any]]]
    ):
        self._fetch_base_item = fetch_base_item

    @abc.abstractmethod
    async def get(self, collection_id: str) -> Dict[str, Any]:
        """Return the base item for the collection and cache by collection id."""
        pass


class DefaultBaseItemCache(BaseItemCache):
    """
    Implementation of the BaseItemCache that holds base items in a dict.
    """

    def __init__(
        self, fetch_base_item: Callable[[str], Coroutine[Any, Any, Dict[str, Any]]]
    ):
        self._base_items = {}
        super().__init__(fetch_base_item)

    async def get(self, collection_id: str):
        if collection_id not in self._base_items:
            self._base_items[collection_id] = await self._fetch_base_item(
                collection_id,
            )
        return self._base_items[collection_id]
