"""collection-search extensions clients."""

import abc

import attrs

from stac_fastapi.types.stac import ItemCollection

from .request import BaseCollectionSearchPostRequest


@attrs.define
class AsyncBaseCollectionSearchClient(abc.ABC):
    """Defines a pattern for implementing the STAC collection-search POST extension."""

    @abc.abstractmethod
    async def post_all_collections(
        self,
        search_request: BaseCollectionSearchPostRequest,
        **kwargs,
    ) -> ItemCollection:
        """Get all available collections.

        Called with `POST /collections`.

        Returns:
            A list of collections.

        """
        ...


@attrs.define
class BaseCollectionSearchClient(abc.ABC):
    """Defines a pattern for implementing the STAC collection-search POST extension."""

    @abc.abstractmethod
    def post_all_collections(
        self, search_request: BaseCollectionSearchPostRequest, **kwargs
    ) -> ItemCollection:
        """Get all available collections.

        Called with `POST /collections`.

        Returns:
            A list of collections.

        """
        ...
