"""Item crud client."""
import re
from datetime import datetime
from typing import Any, Dict, List, Optional, Union
from urllib.parse import unquote_plus, urljoin

import attr
import orjson
from fastapi import HTTPException
from pydantic import ValidationError
from pygeofilter.backends.cql2_json import to_cql2
from pygeofilter.parsers.cql2_text import parse as parse_cql2_text
from pypgstac.hydration import hydrate
from stac_pydantic.links import Relations
from stac_pydantic.shared import MimeTypes
from starlette.requests import Request

from stac_fastapi.pgstac.backend import PgstacBackend
from stac_fastapi.pgstac.config import Settings
from stac_fastapi.pgstac.models.links import (
    CollectionLinks,
    ItemCollectionLinks,
    ItemLinks,
    PagingLinks,
)
from stac_fastapi.pgstac.types.search import PgstacSearch
from stac_fastapi.pgstac.utils import filter_fields
from stac_fastapi.types.core import AsyncBaseCoreClient
from stac_fastapi.types.errors import NotFoundError
from stac_fastapi.types.requests import get_base_url
from stac_fastapi.types.stac import Collection, Collections, Item, ItemCollection

NumType = Union[float, int]


@attr.s
class CoreCrudClient(AsyncBaseCoreClient):
    """Client for core endpoints defined by stac."""

    async def all_collections(self, **kwargs) -> Collections:
        """Read all collections from the database."""
        request: Request = kwargs["request"]
        base_url = get_base_url(request)
        collections = await PgstacBackend.all_collections(request.app.state)
        linked_collections: List[Collection] = []
        if collections is not None and len(collections) > 0:
            for c in collections:
                c["links"] = await CollectionLinks(
                    collection_id=c["id"], request=request
                ).get_links(extra_links=c["links"])

                linked_collections.append(c)

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
            collection_id: ID of the collection.

        Returns:
            Collection.
        """
        request: Request = kwargs["request"]
        collection = await PgstacBackend.get_collection(
            request.app.state, collection_id
        )
        if collection is None:
            raise NotFoundError(f"Collection {collection_id} does not exist.")

        collection["links"] = await CollectionLinks(
            collection_id=collection_id, request=request
        ).get_links(extra_links=collection["links"])

        return collection

    async def _get_base_item(
        self, collection_id: str, request: Request
    ) -> Dict[str, Any]:
        """Get the base item of a collection for use in rehydrating full item collection properties.

        Args:
            collection: ID of the collection.

        Returns:
            Item.
        """
        item = await PgstacBackend.get_base_item(request.app.state, collection_id)
        if item is None:
            raise NotFoundError(f"A base item for {collection_id} does not exist.")

        return item

    async def _search_base(
        self,
        search_request: PgstacSearch,
        **kwargs: Any,
    ) -> ItemCollection:
        """Cross catalog search (POST).

        Called with `POST /search`.

        Args:
            search_request: search request parameters.

        Returns:
            ItemCollection containing items which match the search criteria.
        """
        request: Request = kwargs["request"]
        settings: Settings = request.app.state.settings

        search_request.conf = search_request.conf or {}
        search_request.conf["nohydrate"] = settings.use_api_hydrate
        collection, pagination_links = await PgstacBackend.search_post(
            request.app.state, search_request
        )

        exclude = search_request.fields.exclude
        if exclude and len(exclude) == 0:
            exclude = None
        include = search_request.fields.include
        if include and len(include) == 0:
            include = None

        async def _add_item_links(
            feature: Item,
            collection_id: Optional[str] = None,
            item_id: Optional[str] = None,
        ) -> None:
            """Add ItemLinks to the Item.

            If the fields extension is excluding links, then don't add them.
            Also skip links if the item doesn't provide collection and item ids.
            """
            collection_id = feature.get("collection") or collection_id
            item_id = feature.get("id") or item_id

            if (
                search_request.fields.exclude is None
                or "links" not in search_request.fields.exclude
                and all([collection_id, item_id])
            ):
                feature["links"] = await ItemLinks(
                    collection_id=collection_id,
                    item_id=item_id,
                    request=request,
                ).get_links(extra_links=feature.get("links"))

        cleaned_features: List[Item] = []

        if settings.use_api_hydrate:

            async def _get_base_item(collection_id: str) -> Dict[str, Any]:
                return await self._get_base_item(collection_id, request)

            base_item_cache = settings.base_item_cache(
                fetch_base_item=_get_base_item, request=request
            )

            for feature in collection.get("features") or []:
                base_item = await base_item_cache.get(feature.get("collection"))
                feature = hydrate(base_item, feature)

                # Grab ids needed for links that may be removed by the fields extension.
                collection_id = feature.get("collection")
                item_id = feature.get("id")

                feature = filter_fields(feature, include, exclude)
                await _add_item_links(feature, collection_id, item_id)

                cleaned_features.append(feature)
        else:
            for feature in collection.get("features") or []:
                await _add_item_links(feature)
                cleaned_features.append(feature)

        collection["features"] = cleaned_features
        collection["links"] = await PagingLinks(
            request=request, pagination_links=pagination_links
        ).get_links()
        return collection

    async def item_collection(
        self,
        collection_id: str,
        bbox: Optional[List[NumType]] = None,
        datetime: Optional[Union[str, datetime]] = None,
        limit: Optional[int] = None,
        token: str = None,
        **kwargs,
    ) -> ItemCollection:
        """Get all items from a specific collection.

        Called with `GET /collections/{collection_id}/items`

        Args:
            collection_id: id of the collection.
            limit: number of items to return.
            token: pagination token.

        Returns:
            An ItemCollection.
        """
        # If collection does not exist, NotFoundError wil be raised
        await self.get_collection(collection_id, **kwargs)

        base_args = {
            "collections": [collection_id],
            "bbox": bbox,
            "datetime": datetime,
            "limit": limit,
            "token": token,
        }

        clean = {}
        for k, v in base_args.items():
            if v is not None and v != []:
                clean[k] = v

        req = self.post_request_model(
            **clean,
        )
        item_collection = await self._search_base(req, **kwargs)
        links = await ItemCollectionLinks(
            collection_id=collection_id, request=kwargs["request"]
        ).get_links(extra_links=item_collection["links"])
        item_collection["links"] = links
        return item_collection

    async def get_item(self, item_id: str, collection_id: str, **kwargs) -> Item:
        """Get item by id.

        Called with `GET /collections/{collection_id}/items/{item_id}`.

        Args:
            item_id: ID of the item.
            collection_id: ID of the collection the item is in.

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
        filter: Optional[str] = None,
        filter_lang: Optional[str] = None,
        **kwargs,
    ) -> ItemCollection:
        """Cross catalog search (GET).

        Called with `GET /search`.

        Returns:
            ItemCollection containing items which match the search criteria.
        """
        request = kwargs["request"]
        query_params = str(request.query_params)

        # Kludgy fix because using factory does not allow alias for filter-lang
        if filter_lang is None:
            match = re.search(r"filter-lang=([a-z0-9-]+)", query_params, re.IGNORECASE)
            if match:
                filter_lang = match.group(1)

        # Parse request parameters
        base_args = {
            "collections": collections,
            "ids": ids,
            "bbox": bbox,
            "limit": limit,
            "token": token,
            "query": orjson.loads(unquote_plus(query)) if query else query,
        }

        if filter:
            if filter_lang == "cql2-text":
                ast = parse_cql2_text(filter)
                base_args["filter"] = orjson.loads(to_cql2(ast))
                base_args["filter-lang"] = "cql2-json"

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

        # Remove None values from dict
        clean = {}
        for k, v in base_args.items():
            if v is not None and v != []:
                clean[k] = v

        # Do the request
        try:
            search_request = self.post_request_model(**clean)
        except ValidationError as e:
            raise HTTPException(
                status_code=400, detail=f"Invalid parameters provided {e}"
            )
        return await self.post_search(search_request, request=kwargs["request"])
