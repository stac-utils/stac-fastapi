"""Get Queryables."""
from typing import Any, Optional

from buildpg import render
from fastapi import Request
from fastapi.responses import JSONResponse

from stac_fastapi.types.core import AsyncBaseFiltersClient


class FiltersClient(AsyncBaseFiltersClient):
    """Defines a pattern for implementing the STAC filter extension."""

    async def get_queryables(
        self, request: Request, collection_id: Optional[str] = None, **kwargs: Any
    ) -> JSONResponse:
        """Get the queryables available for the given collection_id.

        If collection_id is None, returns the intersection of all
        queryables over all collections.
        This base implementation returns a blank queryable schema. This is not allowed
        under OGC CQL but it is allowed by the STAC API Filter Extension
        https://github.com/radiantearth/stac-api-spec/tree/master/fragments/filter#queryables
        """
        pool = request.app.state.readpool

        async with pool.acquire() as conn:
            q, p = render(
                """
                    SELECT * FROM get_queryables(:collection::text);
                """,
                collection=collection_id,
            )
            queryables = await conn.fetchval(q, *p)
            queryables["$id"] = str(request.url)
            headers = {"Content-Type": "application/schema+json"}
            return JSONResponse(queryables, headers=headers)
