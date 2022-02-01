"""Base clients."""
import abc

import attr

from stac_fastapi.types import stac as stac_types


@attr.s  # type:ignore
class BaseTransactionsClient(abc.ABC):
    """Defines a pattern for implementing the STAC transaction extension."""

    @abc.abstractmethod
    def create_item(self, item: stac_types.Item, **kwargs) -> stac_types.Item:
        """Create a new item.

        Called with `POST /collections/{collection_id}/items`.

        Args:
            item: the item

        Returns:
            The item that was created.

        """
        ...

    @abc.abstractmethod
    def update_item(self, item: stac_types.Item, **kwargs) -> stac_types.Item:
        """Perform a complete update on an existing item.

        Called with `PUT /collections/{collection_id}/items`. It is expected that this item already exists.  The update
        should do a diff against the saved item and perform any necessary updates.  Partial updates are not supported
        by the transactions extension.

        Args:
            item: the item (must be complete)

        Returns:
            The updated item.
        """
        ...

    @abc.abstractmethod
    def delete_item(
        self, item_id: str, collection_id: str, **kwargs
    ) -> stac_types.Item:
        """Delete an item from a collection.

        Called with `DELETE /collections/{collection_id}/items/{item_id}`

        Args:
            item_id: id of the item.
            collection_id: id of the collection.

        Returns:
            The deleted item.
        """
        ...

    @abc.abstractmethod
    def create_collection(
        self, collection: stac_types.Collection, **kwargs
    ) -> stac_types.Collection:
        """Create a new collection.

        Called with `POST /collections`.

        Args:
            collection: the collection

        Returns:
            The collection that was created.
        """
        ...

    @abc.abstractmethod
    def update_collection(
        self, collection: stac_types.Collection, **kwargs
    ) -> stac_types.Collection:
        """Perform a complete update on an existing collection.

        Called with `PUT /collections`. It is expected that this item already exists.  The update should do a diff
        against the saved collection and perform any necessary updates.  Partial updates are not supported by the
        transactions extension.

        Args:
            collection: the collection (must be complete)

        Returns:
            The updated collection.
        """
        ...

    @abc.abstractmethod
    def delete_collection(self, collection_id: str, **kwargs) -> stac_types.Collection:
        """Delete a collection.

        Called with `DELETE /collections/{collection_id}`

        Args:
            collection_id: id of the collection.

        Returns:
            The deleted collection.
        """
        ...


@attr.s  # type:ignore
class AsyncBaseTransactionsClient(abc.ABC):
    """Defines a pattern for implementing the STAC transaction extension."""

    @abc.abstractmethod
    async def create_item(self, item: stac_types.Item, **kwargs) -> stac_types.Item:
        """Create a new item.

        Called with `POST /collections/{collection_id}/items`.

        Args:
            item: the item

        Returns:
            The item that was created.

        """
        ...

    @abc.abstractmethod
    async def update_item(self, item: stac_types.Item, **kwargs) -> stac_types.Item:
        """Perform a complete update on an existing item.

        Called with `PUT /collections/{collection_id}/items`. It is expected that this item already exists.  The update
        should do a diff against the saved item and perform any necessary updates.  Partial updates are not supported
        by the transactions extension.

        Args:
            item: the item (must be complete)

        Returns:
            The updated item.
        """
        ...

    @abc.abstractmethod
    async def delete_item(
        self, item_id: str, collection_id: str, **kwargs
    ) -> stac_types.Item:
        """Delete an item from a collection.

        Called with `DELETE /collections/{collection_id}/items/{item_id}`

        Args:
            item_id: id of the item.
            collection_id: id of the collection.

        Returns:
            The deleted item.
        """
        ...

    @abc.abstractmethod
    async def create_collection(
        self, collection: stac_types.Collection, **kwargs
    ) -> stac_types.Collection:
        """Create a new collection.

        Called with `POST /collections`.

        Args:
            collection: the collection

        Returns:
            The collection that was created.
        """
        ...

    @abc.abstractmethod
    async def update_collection(
        self, collection: stac_types.Collection, **kwargs
    ) -> stac_types.Collection:
        """Perform a complete update on an existing collection.

        Called with `PUT /collections`. It is expected that this item already exists.  The update should do a diff
        against the saved collection and perform any necessary updates.  Partial updates are not supported by the
        transactions extension.

        Args:
            collection: the collection (must be complete)

        Returns:
            The updated collection.
        """
        ...

    @abc.abstractmethod
    async def delete_collection(
        self, collection_id: str, **kwargs
    ) -> stac_types.Collection:
        """Delete a collection.

        Called with `DELETE /collections/{collection_id}`

        Args:
            collection_id: id of the collection.

        Returns:
            The deleted collection.
        """
        ...
