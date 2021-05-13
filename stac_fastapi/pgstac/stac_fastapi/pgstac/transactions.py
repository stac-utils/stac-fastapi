"""transactions extension client."""

import logging

import attr
from fastapi.responses import ORJSONResponse
from stac_pydantic import Item

from stac_fastapi.pgstac.db import dbfunc
from stac_fastapi.pgstac.models import schemas
from stac_fastapi.types.core import BaseTransactionsClient

logger = logging.getLogger("uvicorn")
logger.setLevel(logging.INFO)


@attr.s
class TransactionsClient(BaseTransactionsClient):
    """Transactions extension specific CRUD operations."""

    async def create_item(item: schemas.Item = None, **kwargs) -> Item:
        """Create item."""
        request = kwargs["request"]
        pool = request.app.state.writepool
        await dbfunc(pool, "create_item", item)
        return ORJSONResponse(item.dict())

    async def update_item(item: schemas.Item = None, **kwargs) -> Item:
        """Update item."""
        request = kwargs["request"]
        pool = request.app.state.writepool
        await dbfunc(pool, "update_item", item)
        return ORJSONResponse(item.dict())

    async def create_collection(
        collection: schemas.Collection, **kwargs
    ) -> schemas.Collection:
        """Create collection."""
        request = kwargs["request"]
        pool = request.app.state.writepool
        await dbfunc(pool, "create_collection", collection)
        return ORJSONResponse(collection.dict())

    async def update_collection(
        collection: schemas.Collection, **kwargs
    ) -> schemas.Collection:
        """Update collection."""
        request = kwargs["request"]
        pool = request.app.state.writepool
        await dbfunc(pool, "update_collection", collection)
        return ORJSONResponse(collection.dict())

    async def delete_item(id: str, **kwargs) -> schemas.Collection:
        """Delete collection."""
        request = kwargs["request"]
        pool = request.app.state.writepool
        await dbfunc(pool, "delete_item", id)
        return ORJSONResponse({"deleted item": id})

    async def delete_collection(id: str, **kwargs) -> schemas.Collection:
        """Delete collection."""
        request = kwargs["request"]
        pool = request.app.state.writepool
        await dbfunc(pool, "delete_collection", id)
        return ORJSONResponse({"deleted collection": id})
