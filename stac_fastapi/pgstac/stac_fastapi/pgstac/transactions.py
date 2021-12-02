"""transactions extension client."""

import logging
from typing import Dict

import attr

from stac_fastapi.pgstac.db import dbfunc
from stac_fastapi.types import stac as stac_types
from stac_fastapi.types.core import AsyncBaseTransactionsClient

logger = logging.getLogger("uvicorn")
logger.setLevel(logging.INFO)


@attr.s
class TransactionsClient(AsyncBaseTransactionsClient):
    """Transactions extension specific CRUD operations."""

    async def create_item(self, item: stac_types.Item, **kwargs) -> stac_types.Item:
        """Create item."""
        request = kwargs["request"]
        pool = request.app.state.writepool
        await dbfunc(pool, "create_item", item)
        return item

    async def update_item(self, item: stac_types.Item, **kwargs) -> stac_types.Item:
        """Update item."""
        request = kwargs["request"]
        pool = request.app.state.writepool
        await dbfunc(pool, "update_item", item)
        return item

    async def create_collection(
        self, collection: stac_types.Collection, **kwargs
    ) -> stac_types.Collection:
        """Create collection."""
        request = kwargs["request"]
        pool = request.app.state.writepool
        await dbfunc(pool, "create_collection", collection)
        return collection

    async def update_collection(
        self, collection: stac_types.Collection, **kwargs
    ) -> stac_types.Collection:
        """Update collection."""
        request = kwargs["request"]
        pool = request.app.state.writepool
        await dbfunc(pool, "update_collection", collection)
        return collection

    async def delete_item(self, item_id: str, collection_id: str, **kwargs) -> Dict:
        """Delete collection."""
        request = kwargs["request"]
        pool = request.app.state.writepool
        await dbfunc(pool, "delete_item", item_id)
        return {"deleted item": item_id}

    async def delete_collection(self, collection_id: str, **kwargs) -> Dict:
        """Delete collection."""
        request = kwargs["request"]
        pool = request.app.state.writepool
        await dbfunc(pool, "delete_collection", collection_id)
        return {"deleted collection": collection_id}
