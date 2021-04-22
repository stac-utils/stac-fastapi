"""transactions extension client."""

import json
import logging
from typing import Dict, Optional, Type
from buildpg import render
import attr

# TODO: This import should come from `backend` module
from stac_fastapi.extensions.third_party.bulk_transactions import (
    BaseBulkTransactionsClient,
)
from stac_fastapi.pgstac.models import schemas
from stac_fastapi.types.core import BaseTransactionsClient
from stac_fastapi.types.errors import NotFoundError
from stac_pydantic import Collection, Item, ItemCollection
from stac_fastapi.pgstac.models.links import (
    CollectionLinks,
    ItemLinks,
    PagingLinks,
)
from fastapi.responses import ORJSONResponse

logger = logging.getLogger("uvicorn")
logger.setLevel(logging.INFO)


@attr.s
class TransactionsClient(BaseTransactionsClient):
    """Transactions extension specific CRUD operations."""

    async def create_item(item: schemas.Item = None, **kwargs) -> Item:
        """Create item."""
        request = kwargs["request"]
        pool = request.app.state.writepool
        async with pool.acquire() as conn:
            q, p = render(
                """
                SELECT * FROM create_item(:item::text::jsonb);
                """,
                item=item.json(),
            )
            await conn.fetch(q, *p)

        return item

    async def create_collection(
        collection: schemas.Collection, **kwargs
    ) -> schemas.Collection:
        """Create collection."""
        logger.info(kwargs)
        request = kwargs["request"]

        pool = request.app.state.writepool
        async with pool.acquire() as conn:
            q, p = render(
                """
                SELECT * FROM create_collection(:collection::text::jsonb);
                """,
                collection=collection.json(),
            )
            await conn.fetchval(q, *p)

        return collection

    async def update_item(self, model: schemas.Item, **kwargs) -> schemas.Item:
        """Update item."""
        return await self.create_item(model, **kwargs)

    async def update_collection(
        self, request_data: schemas.Collection, **kwargs
    ) -> schemas.Collection:
        """Update collection."""
        return await self.create_collection(request_data, **kwargs)

    async def delete_item(id: str, **kwargs) -> schemas.Collection:
        """Delete collection."""
        request = kwargs["request"]
        pool = request.app.state.writepool
        async with pool.acquire() as conn:
            q, p = render(
                """
                DELETE FROM items WHERE id = :id
                """,
                id=id,
            )
            result = await conn.execute(q, *p)
            if result == "DELETE 0":
                raise NotFoundError
            logger.info(result)

        return ORJSONResponse({"pgresponse": result})

    async def delete_collection(id: str, **kwargs) -> schemas.Collection:
        """Delete collection."""
        request = kwargs["request"]
        pool = request.app.state.writepool
        async with pool.acquire() as conn:
            q, p = render(
                """
                DELETE FROM collections WHERE id = :id
                """,
                id=id,
            )
            result = await conn.execute(q, *p)
            if result == "DELETE 0":
                raise NotFoundError
            logger.info(result)

        return ORJSONResponse({"pgresponse": result})
