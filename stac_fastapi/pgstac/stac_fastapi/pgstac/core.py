"""Item crud client."""
import re
from datetime import datetime
from typing import Any, Dict, List, Optional, Union
from urllib.parse import urljoin

import attr
import orjson
from asyncpg.exceptions import InvalidDatetimeFormatError
from buildpg import render
from fastapi import HTTPException
from pydantic import ValidationError
from stac_pydantic.links import Relations
from stac_pydantic.shared import MimeTypes
from starlette.requests import Request

from stac_fastapi.pgstac.models.links import CollectionLinks, ItemLinks, PagingLinks
from stac_fastapi.pgstac.types.search import PgstacSearch
from stac_fastapi.types.core import AsyncBaseCoreClient
from stac_fastapi.types.errors import InvalidQueryParameter, NotFoundError
from stac_fastapi.types.stac import Collection, Collections, Item, ItemCollection

NumType = Union[float, int]


@attr.s
class CoreCrudClient(AsyncBaseCoreClient):
    """Client for core endpoints defined by stac."""

    async def all_collections(self, **kwargs) -> Collections:
        """Read all collections from the database."""
        request: Request = kwargs["request"]
        base_url = str(request.base_url)
        pool = request.app.state.readpool

        async with pool.acquire() as conn:
            collections = await conn.fetchval(
                """
                SELECT * FROM all_collections();
                """
            )
        linked_collections: List[Collection] = []
        if collections is not None and len(collections) > 0:
            for c in collections:
                coll = Collection(**c)
                coll["links"] = await CollectionLinks(
                    collection_id=coll["id"], request=request
                ).get_links(extra_links=coll.get("links"))

                linked_collections.append(coll)

        links = [
            {
                "rel": Relations.root.value,
                "type": MimeTypes.json,
                "href": base_url,
            },
            {
                "rel": Relations.parent.value,
                "type": MimeTypes.json,
                "href": base_url,
            },
            {
                "rel": Relations.self.value,
                "type": MimeTypes.json,
                "href": urljoin(base_url, "collections"),
            },
        ]
        collection_list = Collections(collections=linked_collections or [], links=links)
        return collection_list

    async def get_collection(self, collection_id: str, **kwargs) -> Collection:
        """Get collection by id.

        Called with `GET /collections/{collection_id}`.

        Args:
            id: Id of the collection.

        Returns:
            Collection.
        """
        collection: Optional[Dict[str, Any]]

        request: Request = kwargs["request"]
        pool = request.app.state.readpool
        async with pool.acquire() as conn:
            q, p = render(
                """
                SELECT * FROM get_collection(:id::text);
                """,
                id=collection_id,
            )
            collection = await conn.fetchval(q, *p)
        if collection is None:
            raise NotFoundError(f"Collection {id} does not exist.")

        collection["links"] = await CollectionLinks(
            collection_id=collection_id, request=request
        ).get_links(extra_links=collection.get("links"))

        return Collection(**collection)

    async def _search_base(
        self, search_request: PgstacSearch, **kwargs: Any
    ) -> ItemCollection:
        """Cross catalog search (POST).

        Called with `POST /search`.

        Args:
            search_request: search request parameters.

        Returns:
            ItemCollection containing items which match the search criteria.
        """
        items: Dict[str, Any]

        request: Request = kwargs["request"]
        pool = request.app.state.readpool

        # pool = kwargs["request"].app.state.readpool
        req = search_request.json(exclude_none=True, by_alias=True)

        try:
            async with pool.acquire() as conn:
                q, p = render(
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

        next: Optional[str] = items.pop("next", None)
        prev: Optional[str] = items.pop("prev", None)
        collection = ItemCollection(**items)
        cleaned_features: List[Item] = []

        for feature in collection.get("features") or []:
            feature = Item(**feature)
            if (
                search_request.fields.exclude is None
                or "links" not in search_request.fields.exclude
            ):
                # TODO: feature.collection is not always included
                # This code fails if it's left outside of the fields expression
                # I've fields extension updated test cases to always include feature.collection
                feature["links"] = await ItemLinks(
                    collection_id=feature["collection"],
                    item_id=feature["id"],
                    request=request,
                ).get_links(extra_links=feature.get("links"))

                exclude = search_request.fields.exclude
                if exclude and len(exclude) == 0:
                    exclude = None
                include = search_request.fields.include
                if include and len(include) == 0:
                    include = None
            cleaned_features.append(feature)

        collection["features"] = cleaned_features
        collection["links"] = await PagingLinks(
            request=request,
            next=next,
            prev=prev,
        ).get_links()
        return collection

    async def item_collection(
        self,
        collection_id: str,
        limit: Optional[int] = None,
        token: str = None,
        **kwargs,
    ) -> ItemCollection:
        """Get all items from a specific collection.

        Called with `GET /collections/{collection_id}/items`

        Args:
            id: id of the collection.
            limit: number of items to return.
            token: pagination token.

        Returns:
            An ItemCollection.
        """
        # If collection does not exist, NotFoundError wil be raised
        await self.get_collection(collection_id, **kwargs)

        req = self.post_request_model(
            collections=[collection_id], limit=limit, token=token
        )
        item_collection = await self._search_base(req, **kwargs)
        links = await CollectionLinks(
            collection_id=collection_id, request=kwargs["request"]
        ).get_links(extra_links=item_collection["links"])
        item_collection["links"] = links
        return item_collection

    async def get_item(self, item_id: str, collection_id: str, **kwargs) -> Item:
        """Get item by id.

        Called with `GET /collections/{collection_id}/items/{item_id}`.

        Args:
            id: Id of the item.

        Returns:
            Item.
        """
        # If collection does not exist, NotFoundError wil be raised
        await self.get_collection(collection_id, **kwargs)

        req = self.post_request_model(
            ids=[item_id], collections=[collection_id], limit=1
        )
        item_collection = await self._search_base(req, **kwargs)
        if not item_collection["features"]:
            raise NotFoundError(
                f"Item {item_id} in Collection {collection_id} does not exist."
            )

        return Item(**item_collection["features"][0])

    async def post_search(
        self, search_request: PgstacSearch, **kwargs
    ) -> ItemCollection:
        """Cross catalog search (POST).

        Called with `POST /search`.

        Args:
            search_request: search request parameters.

        Returns:
            ItemCollection containing items which match the search criteria.
        """
        item_collection = await self._search_base(search_request, **kwargs)
        return ItemCollection(**item_collection)

    async def get_search(
        self,
        collections: Optional[List[str]] = None,
        ids: Optional[List[str]] = None,
        bbox: Optional[List[NumType]] = None,
        datetime: Optional[Union[str, datetime]] = None,
        limit: Optional[int] = None,
        query: Optional[str] = None,
        token: Optional[str] = None,
        fields: Optional[List[str]] = None,
        sortby: Optional[str] = None,
        **kwargs,
    ) -> ItemCollection:
        """Cross catalog search (GET).

        Called with `GET /search`.

        Returns:
            ItemCollection containing items which match the search criteria.
        """
        # Parse request parameters
        base_args = {
            "collections": collections,
            "ids": ids,
            "bbox": bbox,
            "limit": limit,
            "token": token,
            "query": orjson.loads(query) if query else query,
        }

        if datetime:
            base_args["datetime"] = datetime

        if sortby:
            # https://github.com/radiantearth/stac-spec/tree/master/api-spec/extensions/sort#http-get-or-post-form
            sort_param = []
            for sort in sortby:
                sortparts = re.match(r"^([+-]?)(.*)$", sort)
                if sortparts:
                    sort_param.append(
                        {
                            "field": sortparts.group(2).strip(),
                            "direction": "desc" if sortparts.group(1) == "-" else "asc",
                        }
                    )
            base_args["sortby"] = sort_param

        if fields:
            includes = set()
            excludes = set()
            for field in fields:
                if field[0] == "-":
                    excludes.add(field[1:])
                elif field[0] == "+":
                    includes.add(field[1:])
                else:
                    includes.add(field)
            base_args["fields"] = {"include": includes, "exclude": excludes}

        # Do the request
        try:
            search_request = self.post_request_model(**base_args)
        except ValidationError:
            raise HTTPException(status_code=400, detail="Invalid parameters provided")
        return await self.post_search(search_request, request=kwargs["request"])
