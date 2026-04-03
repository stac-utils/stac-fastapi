"""Transaction clients."""

import abc
from typing import List, Optional, Union

import attr
from stac_pydantic import Collection, Item, ItemCollection
from starlette.responses import Response

from stac_fastapi.types import stac

from .request import PartialCollection, PartialItem, PatchOperation


@attr.s  # type:ignore
class BaseTransactionsClient(abc.ABC):
    """Defines a pattern for implementing the STAC API Transaction Extension."""

    @abc.abstractmethod
    def create_item(
        self,
        collection_id: str,
        item: Union[Item, ItemCollection],
        **kwargs,
    ) -> Optional[Union[stac.Item, Response, None]]:
        """Create a new item.

        Called with `POST /collections/{collection_id}/items`.

        Args:
            item: the item or item collection
            collection_id: the id of the collection from the resource path

        Returns:
            The item that was created or None if item collection.
        """
        ...

    @abc.abstractmethod
    def update_item(
        self, collection_id: str, item_id: str, item: Item, **kwargs
    ) -> Optional[Union[stac.Item, Response]]:
        """Perform a complete update on an existing item.

        Called with `PUT /collections/{collection_id}/items`. It is expected
        that this item already exists.  The update should do a diff against the
        saved item and perform any necessary updates.  Partial updates are not
        supported by the transactions extension.

        Args:
            item: the item (must be complete)
            collection_id: the id of the collection from the resource path

        Returns:
            The updated item.
        """
        ...

    @abc.abstractmethod
    def patch_item(
        self,
        collection_id: str,
        item_id: str,
        patch: Union[PartialItem, List[PatchOperation]],
        **kwargs,
    ) -> Optional[Union[stac.Item, Response]]:
        """Update an item from a collection.

        Called with `PATCH /collections/{collection_id}/items/{item_id}`

        example:
            # convert merge patch item to list of operations
            if isinstance(patch, PartialItem):
                patch = patch.operations()

            item = backend.patch_item(collection_id, item_id, patch)

            return item

        Args:
            item_id: id of the item.
            collection_id: id of the collection.
            patch: either the partial item or list of patch operations.

        Returns:
            The patched item.
        """
        ...

    @abc.abstractmethod
    def delete_item(
        self, item_id: str, collection_id: str, **kwargs
    ) -> Optional[Union[stac.Item, Response]]:
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
        self, collection: Collection, **kwargs
    ) -> Optional[Union[stac.Collection, Response]]:
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
        self, collection_id: str, collection: Collection, **kwargs
    ) -> Optional[Union[stac.Collection, Response]]:
        """Perform a complete update on an existing collection.

        Called with `PUT /collections/{collection_id}`. It is expected that this
        collection already exists.  The update should do a diff against the saved
        collection and perform any necessary updates.  Partial updates are not
        supported by the transactions extension.

        Args:
            collection_id: id of the existing collection to be updated
            collection: the updated collection (must be complete)

        Returns:
            The updated collection.
        """
        ...

    @abc.abstractmethod
    def patch_collection(
        self,
        collection_id: str,
        patch: Union[PartialCollection, List[PatchOperation]],
        **kwargs,
    ) -> Optional[Union[stac.Collection, Response]]:
        """Update a collection.

        Called with `PATCH /collections/{collection_id}`

        example:
            # convert merge patch item to list of operations
            if isinstance(patch, PartialCollection):
                patch = patch.operations()

            collection = backend.patch_collection(collection_id, patch)

            return collection

        Args:
            collection_id: id of the collection.
            patch: either the partial collection or list of patch operations.

        Returns:
            The patched collection.
        """
        ...

    @abc.abstractmethod
    def delete_collection(
        self, collection_id: str, **kwargs
    ) -> Optional[Union[stac.Collection, Response]]:
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
    async def create_item(
        self,
        collection_id: str,
        item: Union[Item, ItemCollection],
        **kwargs,
    ) -> Optional[Union[stac.Item, Response, None]]:
        """Create a new item.

        Called with `POST /collections/{collection_id}/items`.

        Args:
            item: the item or item collection
            collection_id: the id of the collection from the resource path

        Returns:
            The item that was created or None if item collection.
        """
        ...

    @abc.abstractmethod
    async def update_item(
        self, collection_id: str, item_id: str, item: Item, **kwargs
    ) -> Optional[Union[stac.Item, Response]]:
        """Perform a complete update on an existing item.

        Called with `PUT /collections/{collection_id}/items`. It is expected
        that this item already exists.  The update should do a diff against the
        saved item and perform any necessary updates.  Partial updates are not
        supported by the transactions extension.

        Args:
            item: the item (must be complete)

        Returns:
            The updated item.
        """
        ...

    @abc.abstractmethod
    async def patch_item(
        self,
        collection_id: str,
        item_id: str,
        patch: Union[PartialItem, List[PatchOperation]],
        **kwargs,
    ) -> Optional[Union[stac.Item, Response]]:
        """Update an item from a collection.

        Called with `PATCH /collections/{collection_id}/items/{item_id}`

        example:
            # convert merge patch item to list of operations
            if isinstance(patch, PartialItem):
                patch = patch.operations()

            item = backend.patch_item(collection_id, item_id, patch)

            return item

        Args:
            item_id: id of the item.
            collection_id: id of the collection.
            patch: either the partial item or list of patch operations.

        Returns:
            The patched item.
        """
        ...

    @abc.abstractmethod
    async def delete_item(
        self, item_id: str, collection_id: str, **kwargs
    ) -> Optional[Union[stac.Item, Response]]:
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
        self, collection: Collection, **kwargs
    ) -> Optional[Union[stac.Collection, Response]]:
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
        self, collection_id: str, collection: Collection, **kwargs
    ) -> Optional[Union[stac.Collection, Response]]:
        """Perform a complete update on an existing collection.

        Called with `PUT /collections/{collection_id}`. It is expected that this item
        already exists.  The update should do a diff against the saved collection and
        perform any necessary updates.  Partial updates are not supported by the
        transactions extension.

        Args:
            collection_id: id of the existing collection to be updated
            collection: the updated collection (must be complete)

        Returns:
            The updated collection.
        """
        ...

    @abc.abstractmethod
    async def patch_collection(
        self,
        collection_id: str,
        patch: Union[PartialCollection, List[PatchOperation]],
        **kwargs,
    ) -> Optional[Union[stac.Collection, Response]]:
        """Update a collection.

        Called with `PATCH /collections/{collection_id}`

        example:
            # convert merge patch item to list of operations
            if isinstance(patch, PartialCollection):
                patch = patch.operations()

            collection = backend.patch_collection(collection_id, patch)

            return collection

        Args:
            collection_id: id of the collection.
            patch: either the partial collection or list of patch operations.

        Returns:
            The patched collection.
        """
        ...

    @abc.abstractmethod
    async def delete_collection(
        self, collection_id: str, **kwargs
    ) -> Optional[Union[stac.Collection, Response]]:
        """Delete a collection.

        Called with `DELETE /collections/{collection_id}`

        Args:
            collection_id: id of the collection.

        Returns:
            The deleted collection.
        """
        ...
