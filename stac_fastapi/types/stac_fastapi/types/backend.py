"""Storage backends for stac-fastapi.

Backends are used to fetch data for a client. They intentionally have
restrictive method signatures in order to enforce separation of responsibilities
between backends and clients.
"""

from abc import ABC, abstractclassmethod
from typing import List, Optional

from starlette.datastructures import State

from stac_fastapi.types.search import BaseSearchPostRequest
from stac_fastapi.types.stac import Collection, ItemCollection


class AsyncBackend(ABC):
    """An asynchronous backend."""

    @abstractclassmethod
    async def all_collections(state: State) -> List[Collection]:
        """Get all collections."""
        ...

    @abstractclassmethod
    async def get_collection(state: State, collection_id: str) -> Optional[Collection]:
        """Get a single collection by id."""
        ...

    @abstractclassmethod
    async def search_post(
        state: State, search: BaseSearchPostRequest
    ) -> ItemCollection:
        """Search the backend for items using a search POST request model."""
        ...
