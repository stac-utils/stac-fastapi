"""base_item_cache classes for pgstac fastapi."""
import abc
from typing import Any, Callable, Coroutine, Dict

from starlette.requests import Request


class BaseItemCache(abc.ABC):
    """
    A cache that returns a base item for a collection.

    If no base item is found in the cache, use the fetch_base_item function
    to fetch the base item from pgstac.
    """

    def __init__(
        self,
        fetch_base_item: Callable[[str], Coroutine[Any, Any, Dict[str, Any]]],
        request: Request,
    ):
        """
        Initialize the base item cache.

        Args:
            fetch_base_item: A function that fetches the base item for a collection.
            request: The request object containing app state that may be used by caches.
        """
        self._fetch_base_item = fetch_base_item
        self._request = request

    @abc.abstractmethod
    async def get(self, collection_id: str) -> Dict[str, Any]:
        """Return the base item for the collection and cache by collection id."""
        pass


class DefaultBaseItemCache(BaseItemCache):
    """Implementation of the BaseItemCache that holds base items in a dict."""

    def __init__(
        self,
        fetch_base_item: Callable[[str], Coroutine[Any, Any, Dict[str, Any]]],
        request: Request,
    ):
        """Initialize the base item cache."""
        self._base_items = {}
        super().__init__(fetch_base_item, request)

    async def get(self, collection_id: str):
        """Return the base item for the collection and cache by collection id."""
        if collection_id not in self._base_items:
            self._base_items[collection_id] = await self._fetch_base_item(
                collection_id,
            )
        return self._base_items[collection_id]
