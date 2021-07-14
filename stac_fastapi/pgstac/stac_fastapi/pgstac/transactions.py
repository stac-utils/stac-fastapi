"""transactions extension client."""

import logging

import attr
import stac_pydantic
from fastapi.responses import ORJSONResponse

from stac_fastapi.pgstac.db import dbfunc
from stac_fastapi.types import stac as stac_types
from stac_fastapi.types.core import BaseTransactionsClient

logger = logging.getLogger("uvicorn")
logger.setLevel(logging.INFO)

# TODO: The functions in this class need to use the `self` argument


@attr.s
class TransactionsClient(BaseTransactionsClient):
    """Transactions extension specific CRUD operations."""

    async def create_item(item: stac_pydantic.Item = None, **kwargs) -> stac_types.Item:
        """Create item."""
        request = kwargs["request"]
        pool = request.app.state.writepool
        await dbfunc(pool, "create_item", item)
        return ORJSONResponse(item.dict())

    async def update_item(item: stac_pydantic.Item = None, **kwargs) -> stac_types.Item:
        """Update item."""
        request = kwargs["request"]
        pool = request.app.state.writepool
        await dbfunc(pool, "update_item", item)
        return ORJSONResponse(item.dict())

    async def create_collection(
        collection: stac_pydantic.Collection, **kwargs
    ) -> stac_types.Collection:
        """Create collection."""
        request = kwargs["request"]
        pool = request.app.state.writepool
        await dbfunc(pool, "create_collection", collection)
        return ORJSONResponse(collection.dict())

    async def update_collection(
        collection: stac_pydantic.Collection, **kwargs
    ) -> stac_types.Collection:
        """Update collection."""
        request = kwargs["request"]
        pool = request.app.state.writepool
        await dbfunc(pool, "update_collection", collection)
        return ORJSONResponse(collection.dict())

    async def delete_item(
        item_id: str, collection_id: str, **kwargs
    ) -> stac_types.Collection:
        """Delete collection."""
        request = kwargs["request"]
        pool = request.app.state.writepool
        await dbfunc(pool, "delete_item", item_id)
        return ORJSONResponse({"deleted item": item_id})

    async def delete_collection(id: str, **kwargs) -> stac_types.Collection:
        """Delete collection."""
        request = kwargs["request"]
        pool = request.app.state.writepool
        await dbfunc(pool, "delete_collection", id)
        return ORJSONResponse({"deleted collection": id})
