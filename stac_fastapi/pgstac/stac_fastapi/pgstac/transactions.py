"""transactions extension client."""

import logging
from typing import Optional, Union

import attr
from buildpg import render
from fastapi import HTTPException, Request
from starlette.responses import JSONResponse, Response

from stac_fastapi.extensions.third_party.bulk_transactions import (
    AsyncBaseBulkTransactionsClient,
    Items,
)
from stac_fastapi.pgstac.db import dbfunc
from stac_fastapi.pgstac.models.links import CollectionLinks, ItemLinks
from stac_fastapi.types import stac as stac_types
from stac_fastapi.types.core import AsyncBaseTransactionsClient

logger = logging.getLogger("uvicorn")
logger.setLevel(logging.INFO)


@attr.s
class TransactionsClient(AsyncBaseTransactionsClient):
    """Transactions extension specific CRUD operations."""

    async def create_item(
        self, collection_id: str, item: stac_types.Item, request: Request, **kwargs
    ) -> Optional[Union[stac_types.Item, Response]]:
        """Create item."""
        body_collection_id = item.get("collection")
        if body_collection_id is not None and collection_id != body_collection_id:
            raise HTTPException(
                status_code=400,
                detail=f"Collection ID from path parameter ({collection_id}) does not match Collection ID from Item ({body_collection_id})",
            )
        item["collection"] = collection_id
        async with request.app.state.get_connection(request, "w") as conn:
            await dbfunc(conn, "create_item", item)
        item["links"] = await ItemLinks(
            collection_id=collection_id,
            item_id=item["id"],
            request=request,
        ).get_links(extra_links=item.get("links"))
        return stac_types.Item(**item)

    async def update_item(
        self,
        request: Request,
        collection_id: str,
        item_id: str,
        item: stac_types.Item,
        **kwargs,
    ) -> Optional[Union[stac_types.Item, Response]]:
        """Update item."""
        body_collection_id = item.get("collection")
        if body_collection_id is not None and collection_id != body_collection_id:
            raise HTTPException(
                status_code=400,
                detail=f"Collection ID from path parameter ({collection_id}) does not match Collection ID from Item ({body_collection_id})",
            )
        item["collection"] = collection_id
        body_item_id = item["id"]
        if body_item_id != item_id:
            raise HTTPException(
                status_code=400,
                detail=f"Item ID from path parameter ({item_id}) does not match Item ID from Item ({body_item_id})",
            )
        async with request.app.state.get_connection(request, "w") as conn:
            await dbfunc(conn, "update_item", item)
        item["links"] = await ItemLinks(
            collection_id=collection_id,
            item_id=item["id"],
            request=request,
        ).get_links(extra_links=item.get("links"))
        return stac_types.Item(**item)

    async def create_collection(
        self, collection: stac_types.Collection, request: Request, **kwargs
    ) -> Optional[Union[stac_types.Collection, Response]]:
        """Create collection."""
        async with request.app.state.get_connection(request, "w") as conn:
            await dbfunc(conn, "create_collection", collection)
        collection["links"] = await CollectionLinks(
            collection_id=collection["id"], request=request
        ).get_links(extra_links=collection.get("links"))

        return stac_types.Collection(**collection)

    async def update_collection(
        self, collection: stac_types.Collection, request: Request, **kwargs
    ) -> Optional[Union[stac_types.Collection, Response]]:
        """Update collection."""
        async with request.app.state.get_connection(request, "w") as conn:
            await dbfunc(conn, "update_collection", collection)
        collection["links"] = await CollectionLinks(
            collection_id=collection["id"], request=request
        ).get_links(extra_links=collection.get("links"))
        return stac_types.Collection(**collection)

    async def delete_item(
        self, item_id: str, collection_id: str, request: Request, **kwargs
    ) -> Optional[Union[stac_types.Item, Response]]:
        """Delete item."""
        q, p = render(
            "SELECT * FROM delete_item(:item::text, :collection::text);",
            item=item_id,
            collection=collection_id,
        )
        async with request.app.state.get_connection(request, "w") as conn:
            await conn.fetchval(q, *p)
        return JSONResponse({"deleted item": item_id})

    async def delete_collection(
        self, collection_id: str, request: Request, **kwargs
    ) -> Optional[Union[stac_types.Collection, Response]]:
        """Delete collection."""
        async with request.app.state.get_connection(request, "w") as conn:
            await dbfunc(conn, "delete_collection", collection_id)
        return JSONResponse({"deleted collection": collection_id})


@attr.s
class BulkTransactionsClient(AsyncBaseBulkTransactionsClient):
    """Postgres bulk transactions."""

    async def bulk_item_insert(self, items: Items, request: Request, **kwargs) -> str:
        """Bulk item insertion using pgstac."""
        items = list(items.items.values())
        async with request.app.state.get_connection(request, "w") as conn:
            await dbfunc(conn, "create_items", items)

        return_msg = f"Successfully added {len(items)} items."
        return return_msg
