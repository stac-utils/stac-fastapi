"""Base clients."""
import abc
from datetime import datetime
from typing import Any, Dict, List, Optional, Type, Union

import attr
from stac_pydantic import ItemCollection
from stac_pydantic.api import ConformanceClasses, LandingPage

from stac_api.api.extensions.extension import ApiExtension
from stac_api.models import schemas

NumType = Union[float, int]


@attr.s  # type:ignore
class BaseTransactionsClient(abc.ABC):
    """Defines a pattern for implementing the STAC transaction extension."""

    @abc.abstractmethod
    def create_item(self, model: schemas.Item, **kwargs) -> schemas.Item:
        """Create a new item.

        Called with `POST /collections/{collectionId}/items`.

        Args:
            model: the item

        Returns:
            The item that was created.

        """
        ...

    @abc.abstractmethod
    def update_item(self, model: schemas.Item, **kwargs) -> schemas.Item:
        """Perform a complete update on an existing item.

        Called with `PUT /collections/{collectionId}/items`. It is expected that this item already exists.  The update
        should do a diff against the saved item and perform any necessary updates.  Partial updates are not supported
        by the transactions extension.

        Args:
            model: the item (must be complete)

        Returns:
            The updated item.
        """
        ...

    @abc.abstractmethod
    def delete_item(self, id: str, **kwargs) -> schemas.Item:
        """Delete an item from a collection.

        Called with `DELETE /collections/{collectionId}/items/{itemId}`

        Args:
            id: id of the item.

        Returns:
            The deleted item.
        """
        ...

    @abc.abstractmethod
    def create_collection(
        self, model: schemas.Collection, **kwargs
    ) -> schemas.Collection:
        """Create a new collection.

        Called with `POST /collections`.

        Args:
            model: the collection

        Returns:
            The collection that was created.
        """
        ...

    @abc.abstractmethod
    def update_collection(
        self, model: schemas.Collection, **kwargs
    ) -> schemas.Collection:
        """Perform a complete update on an existing collection.

        Called with `PUT /collections`. It is expected that this item already exists.  The update should do a diff
        against the saved collection and perform any necessary updates.  Partial updates are not supported by the
        transactions extension.

        Args:
            model: the collection (must be complete)

        Returns:

        """
        ...

    @abc.abstractmethod
    def delete_collection(self, id: str, **kwargs) -> schemas.Collection:
        """Delete a collection.

        Called with `DELETE /collections/{collectionId}`

        Args:
            id: id of the collection.

        Returns:
            The deleted collection.
        """
        ...


@attr.s  # type: ignore
class BaseBulkTransactionsClient(abc.ABC):
    """BulkTransactionsClient"""

    @staticmethod
    def _chunks(lst, n):
        """Yield successive n-sized chunks from list.

        https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks
        """
        # """Yield successive n-sized chunks from lst."""
        for i in range(0, len(lst), n):
            yield lst[i : i + n]

    @abc.abstractmethod
    def bulk_item_insert(
        self, items: schemas.Items, chunk_size: Optional[int] = None, **kwargs
    ) -> str:
        """Bulk creation of items.

        Args:
            items: list of items.
            chunk_size: number of items processed at a time.

        Returns:
            Message indicating the status of the insert.

        """
        raise NotImplementedError


@attr.s  # type:ignore
class BaseCoreClient(abc.ABC):
    """Defines a pattern for implementing STAC api core endpoints.

    Attributes:
        extensions: list of registered api extensions.
    """

    extensions: List[ApiExtension] = attr.ib(default=attr.Factory(list))

    def extension_is_enabled(self, extension: Type[ApiExtension]) -> bool:
        """check if an api extension is enabled."""
        return any([isinstance(ext, extension) for ext in self.extensions])

    @abc.abstractmethod
    def landing_page(self, **kwargs) -> LandingPage:
        """Landing page.

        Called with `GET /`.

        Returns:
            API landing page, serving as an entry point to the API.
        """
        ...

    @abc.abstractmethod
    def conformance(self, **kwargs) -> ConformanceClasses:
        """Conformance classes.

        Called with `GET /conformance`.

        Returns:
            Conformance classes which the server conforms to.
        """
        ...

    @abc.abstractmethod
    def post_search(
        self, search_request: schemas.STACSearch, **kwargs
    ) -> Dict[str, Any]:
        """Cross catalog search (POST)

        Called with `POST /search`.

        Args:
            search_request: search request parameters.

        Returns:
            ItemCollection containing items which match the search criteria.
        """
        ...

    @abc.abstractmethod
    def get_search(
        self,
        collections: Optional[List[str]] = None,
        ids: Optional[List[str]] = None,
        bbox: Optional[List[NumType]] = None,
        datetime: Optional[Union[str, datetime]] = None,
        limit: Optional[int] = 10,
        query: Optional[str] = None,
        token: Optional[str] = None,
        fields: Optional[List[str]] = None,
        sortby: Optional[str] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """Cross catalog search (GET)

        Called with `GET /search`.

        Returns:
            ItemCollection containing items which match the search criteria.
        """
        ...

    @abc.abstractmethod
    def get_item(self, id: str, **kwargs) -> schemas.Item:
        """Get item by id.

        Called with `GET /collections/{collectionId}/items/{itemId}`.

        Args:
            id: Id of the item.

        Returns:
            Item.
        """
        ...

    @abc.abstractmethod
    def all_collections(self) -> List[schemas.Collection]:
        """Get all available collections.

        Called with `GET /collections`.

        Returns:
            A list of collections.
        """
        ...

    @abc.abstractmethod
    def get_collection(self, id: str, **kwargs) -> schemas.Collection:
        """Get collection by id.

        Called with `GET /collections/{collectionId}`.

        Args:
            id: Id of the collection.

        Returns:
            Collection.
        """
        ...

    @abc.abstractmethod
    def item_collection(
        self, id: str, limit: int = 10, token: str = None, **kwargs
    ) -> ItemCollection:
        """Get all items from a specific collection.

        Called with `GET /collections/{collectionId}/items`

        Args:
            id: id of the collection.
            limit: number of items to return.
            token: pagination token.

        Returns:
            An ItemCollection.
        """
        ...
