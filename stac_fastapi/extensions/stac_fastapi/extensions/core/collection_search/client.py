"""collection-search extensions clients."""

import abc

import attr

from stac_fastapi.types import stac

from .request import BaseCollectionSearchPostRequest


@attr.s
class AsyncBaseCollectionSearchClient(abc.ABC):
    """Defines a pattern for implementing the STAC collection-search POST extension."""

    @abc.abstractmethod
    async def post_all_collections(
        self,
        search_request: BaseCollectionSearchPostRequest,
        **kwargs,
    ) -> stac.ItemCollection:
        """Get all available collections.

        Called with `POST /collections`.

        Returns:
            A list of collections.

        """
        ...


@attr.s
class BaseCollectionSearchClient(abc.ABC):
    """Defines a pattern for implementing the STAC collection-search POST extension."""

    @abc.abstractmethod
    def post_all_collections(
        self, search_request: BaseCollectionSearchPostRequest, **kwargs
    ) -> stac.ItemCollection:
        """Get all available collections.

        Called with `POST /collections`.

        Returns:
            A list of collections.

        """
        ...
