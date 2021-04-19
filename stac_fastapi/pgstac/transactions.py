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
from stac_fastapi.pgstac.models.links import CollectionLinks, ItemLinks, PagingLinks

logger = logging.getLogger("uvicorn")
logger.setLevel(logging.INFO)

@attr.s
class TransactionsClient(BaseTransactionsClient):
    """Transactions extension specific CRUD operations."""

    async def create_item(self, item: schemas.Item = None, **kwargs) -> Item:
        """Create item."""
        request = kwargs["request"]
        pool = request.app.state.readpool
        async with pool.acquire() as conn:
            q, p = render(
                """
                SELECT * FROM create_item(:item::text::jsonb);
                """,
                item=item.json(),
            )
            outitem = await conn.fetch(q, *p)
            logger.info(outitem)
            feature = Item.construct(**outitem)
            feature.links = await ItemLinks(
                collection_id=feature.collection,
                item_id=feature.id,
                request=request,
            ).get_links(extra_links=feature.links)
            logger.info(feature)
        return feature

    async def create_collection(
        self, collection: schemas.Collection, **kwargs
    ) -> schemas.Collection:
        """Create collection."""
        request = kwargs["request"]
        pool = request.app.state.readpool
        async with pool.acquire() as conn:
            q, p = render(
                """
                SELECT * FROM create_collections(:collection::text::jsonb);
                """,
                collection=collection.json(),
            )
            out = await conn.fetch(q, *p)
            logger.info(out)
            newcollection = out[0]
        return newcollection

    async def update_item(self, model: schemas.Item, **kwargs) -> schemas.Item:
        """Update item."""
        return await self.create_item(model, **kwargs)

    async def update_collection(
        self, model: schemas.Collection, **kwargs
    ) -> schemas.Collection:
        """Update collection."""
        return await self.create_collection(model, **kwargs)

    async def delete_item(self, id: str, **kwargs) -> schemas.Item:
        """Delete item."""
        request = kwargs["request"]
        pool = request.app.state.readpool
        async with pool.acquire() as conn:
            q, p = render(
                """
                DELETE FROM items WHERE id = :id
                RETURNING *
                """,
                id=id,
            )
            feature = await conn.fetchval(q, *p)
            logger.info(feature)
            feature = Item.construct(**feature)
            feature.links = await ItemLinks(
                collection_id=feature.collection,
                item_id=feature.id,
                request=request,
            ).get_links()
        return feature

    async def delete_collection(self, id: str, **kwargs) -> schemas.Collection:
        """Delete collection."""
        request = kwargs["request"]
        pool = request.app.state.readpool
        async with pool.acquire() as conn:
            q, p = render(
                """
                DELETE FROM collections WHERE id = :id
                RETURNING *
                """,
                id=id,
            )
            collection = await conn.fetchval(q, *p)

        return feature



@attr.s
class BulkTransactionsClient(BaseBulkTransactionsClient):
    """Postgres bulk transactions."""

    def bulk_item_insert(
        self, items: schemas.Items, chunk_size: Optional[int] = None, **kwargs
    ) -> str:
        """
        """
        # Use items.items because schemas.Items is a model with an items key
        return None
