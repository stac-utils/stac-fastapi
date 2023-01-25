"""Asynchronous backend for pgstac."""

from typing import Any, Dict, List, Optional, Tuple

import buildpg
from asyncpg.exceptions import InvalidDatetimeFormatError
from starlette.datastructures import State

from stac_fastapi.types.backend import AsyncBackend
from stac_fastapi.types.errors import InvalidQueryParameter
from stac_fastapi.types.links import PaginationLinks
from stac_fastapi.types.search import BaseSearchPostRequest
from stac_fastapi.types.stac import Collection, ItemCollection


class PgstacBackend(AsyncBackend):
    """An asynchronous backend for pgstac."""

    async def all_collections(state: State) -> List[Collection]:
        """Get all collections."""
        pool = state.readpool
        async with pool.acquire() as conn:
            collections = await conn.fetchval(
                """
                SELECT * FROM all_collections();
                """
            )
        if collections is None:
            return list()
        else:
            return [Collection(**collection) for collection in collections]

    async def get_collection(state: State, collection_id: str) -> Optional[Collection]:
        """Get a single collection."""
        pool = state.readpool
        async with pool.acquire() as conn:
            q, p = buildpg.render(
                """
                SELECT * FROM get_collection(:id::text);
                """,
                id=collection_id,
            )
            collection = await conn.fetchval(q, *p)
        if collection is None:
            return None
        else:
            return Collection(**collection)

    async def search_post(
        state: State, search_request: BaseSearchPostRequest
    ) -> Tuple[ItemCollection, PaginationLinks]:
        """Search the database."""
        items: Dict[str, Any]
        req = search_request.json(exclude_none=True, by_alias=True)
        pool = state.readpool
        try:
            async with pool.acquire() as conn:
                q, p = buildpg.render(
                    """
                    SELECT * FROM search(:req::text::jsonb);
                    """,
                    req=req,
                )
                items = await conn.fetchval(q, *p)
        except InvalidDatetimeFormatError:
            raise InvalidQueryParameter(
                f"Datetime parameter {search_request.datetime} is invalid."
            )

        def make_query_dict(name: str) -> Optional[Dict[str, str]]:
            value = items.pop(name, None)
            if value is None:
                return None
            else:
                return {"token": f"{name}:{value}"}

        next = make_query_dict("next")
        prev = make_query_dict("prev")
        pagination_links = PaginationLinks.from_dicts(next=next, prev=prev)

        return (ItemCollection(**items), pagination_links)

    async def get_base_item(
        state: State, collection_id: str
    ) -> Optional[Dict[str, Any]]:
        """Get the base item from the database."""
        pool = state.readpool
        async with pool.acquire() as conn:
            q, p = buildpg.render(
                """
                SELECT * FROM collection_base_item(:collection_id::text);
                """,
                collection_id=collection_id,
            )
            return await conn.fetchval(q, *p)
