"""Item crud client."""
import json
import logging
from datetime import datetime
from typing import List, Optional, Set, Type, Union
from urllib.parse import urljoin

import attr
import pymongo
import stac_pydantic
from fastapi import HTTPException
from geojson_pydantic.geometries import Polygon
from pydantic import ValidationError
from stac_pydantic.links import Relations
from stac_pydantic.shared import MimeTypes

from stac_fastapi.mongo import serializers
from stac_fastapi.mongo.config import MongoSettings
from stac_fastapi.mongo.session import Session
from stac_fastapi.mongo.types.error_checks import ErrorChecks
from stac_fastapi.types.config import Settings
from stac_fastapi.types.core import BaseCoreClient
from stac_fastapi.types.search import BaseSearchPostRequest
from stac_fastapi.types.stac import Collection, Collections, Item, ItemCollection

logger = logging.getLogger(__name__)

NumType = Union[float, int]


@attr.s
class CoreCrudClient(BaseCoreClient):
    """Client for core endpoints defined by stac."""

    session: Session = attr.ib(default=attr.Factory(Session.create_from_env))
    item_serializer: Type[serializers.Serializer] = attr.ib(
        default=serializers.ItemSerializer
    )
    collection_serializer: Type[serializers.Serializer] = attr.ib(
        default=serializers.CollectionSerializer
    )
    settings = MongoSettings()
    client = settings.create_client
    item_table = client.stac.stac_item
    collection_table = client.stac.stac_collection

    @staticmethod
    def _lookup_id(id: str, table, session):
        """Lookup row by id."""
        pass

    def all_collections(self, **kwargs) -> Collections:
        """Read all collections from the database."""
        base_url = str(kwargs["request"].base_url)

        with self.client.start_session(causal_consistency=True) as session:
            collections = self.collection_table.find({}, session=session)

            serialized_collections = [
                self.collection_serializer.db_to_stac(collection, base_url=base_url)
                for collection in collections
            ]
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
        collection_list = Collections(
            collections=serialized_collections or [], links=links
        )
        return collection_list

    def get_collection(self, collection_id: str, **kwargs) -> Collection:
        """Get collection by id."""
        base_url = str(kwargs["request"].base_url)

        with self.client.start_session(causal_consistency=True) as session:
            error_check = ErrorChecks(session=session, client=self.client)
            error_check._check_collection_not_found(collection_id)
            collection = self.collection_table.find_one(
                {"id": collection_id}, session=session
            )
        return self.collection_serializer.db_to_stac(collection, base_url)

    def item_collection(
        self, collection_id: str, limit: int = 10, token: str = None, **kwargs
    ) -> ItemCollection:
        """Read an item collection from the database."""
        links = []
        response_features = []
        base_url = str(kwargs["request"].base_url)

        with self.client.start_session() as session:
            collection_children = self.item_table.find(
                {"collection": collection_id}, session=session
            ).sort(
                [("properties.datetime", pymongo.ASCENDING), ("id", pymongo.ASCENDING)]
            )

            for item in collection_children:
                response_features.append(
                    self.item_serializer.db_to_stac(item, base_url=base_url)
                )

        context_obj = None
        if self.extension_is_enabled("ContextExtension"):
            count = len(response_features)
            context_obj = {
                "returned": count if count <= 10 else limit,
                "limit": limit,
                "matched": len(response_features) or None,
            }

        return ItemCollection(
            type="FeatureCollection",
            features=response_features,
            links=links,
            context=context_obj,
        )

    def get_item(self, item_id: str, collection_id: str, **kwargs) -> Item:
        """Get item by item id, collection id."""
        base_url = str(kwargs["request"].base_url)
        with self.client.start_session() as session:
            error_check = ErrorChecks(session=session, client=self.client)
            error_check._check_item_not_found(item_id, collection_id)
            item = self.item_table.find_one(
                {"id": item_id, "collection": collection_id}, session=session
            )
        return self.item_serializer.db_to_stac(item, base_url)

    def _return_date(self, datetime):
        datetime = datetime.split("/")
        if len(datetime) == 1:
            datetime = datetime[0][0:19] + "Z"
            return {"properties.datetime": {"$eq": datetime}}
        else:
            start_date = datetime[0]
            end_date = datetime[1]
            if start_date != ".." and end_date != "..":
                start_date = start_date[0:19] + "Z"
                end_date = end_date[0:19] + "Z"
            elif start_date != "..":
                start_date = start_date[0:19] + "Z"
                end_date = "2200-12-01T12:31:12Z"
            elif end_date != "..":
                start_date = "1900-10-01T00:00:00Z"
                end_date = end_date[0:19] + "Z"
            else:
                start_date = "1900-10-01T00:00:00Z"
                end_date = "2200-12-01T12:31:12Z"

            return {"properties.datetime": {"$lt": end_date, "$gte": start_date}}

    def get_search(
        self,
        collections: Optional[List[str]] = None,
        ids: Optional[List[str]] = None,
        bbox: Optional[List[NumType]] = None,
        datetime: Optional[Union[str, datetime]] = None,
        limit: Optional[int] = 10,
        query: Optional[str] = None,
        token: Optional[str] = None,
        fields: Optional[List[str]] = None,
        sortby: Optional[str] = None,
        **kwargs,
    ) -> ItemCollection:
        """GET search catalog."""
        base_args = {
            "collections": collections,
            "ids": ids,
            "bbox": bbox,
            "limit": limit,
            "token": token,
            "query": json.loads(query) if query else query,
        }
        if datetime:
            base_args["datetime"] = datetime
        if sortby:
            # https://github.com/radiantearth/stac-spec/tree/master/api-spec/extensions/sort#http-get-or-post-form
            sort_param = []
            for sort in sortby:
                sort_param.append(
                    {
                        "field": sort[1:],
                        "direction": "asc" if sort[0] == "+" else "desc",
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
        resp = self.post_search(search_request, request=kwargs["request"])

        return resp

    def post_search(
        self, search_request: BaseSearchPostRequest, **kwargs
    ) -> ItemCollection:
        """POST search catalog."""
        base_url = str(kwargs["request"].base_url)
        queries = {}

        if search_request.collections:
            for collection in search_request.collections:
                collection_filter = {"collection": collection}
                queries.update(**collection_filter)

        if search_request.ids:
            id_filter = {"id": {"$in": search_request.ids}}
            queries.update(**id_filter)

        if search_request.bbox:
            # check for 3d bbox
            if len(search_request.bbox) == 6:
                search_request.bbox = [
                    search_request.bbox[0],
                    search_request.bbox[1],
                    search_request.bbox[3],
                    search_request.bbox[4],
                ]
            geom = Polygon.from_bounds(*search_request.bbox).dict(exclude_none=True)
            bbox_filter = {"geometry": {"$geoIntersects": {"$geometry": geom}}}
            queries.update(**bbox_filter)

        if search_request.intersects:
            intersect_filter = {
                "geometry": {
                    "$geoIntersects": {
                        "$geometry": {
                            "type": search_request.intersects.type,
                            "coordinates": search_request.intersects.coordinates,
                        }
                    }
                }
            }
            queries.update(**intersect_filter)

        if search_request.datetime:
            date_filter = self._return_date(str(search_request.datetime))
            queries.update(**date_filter)

        if search_request.query:
            if type(search_request.query) == str:
                search_request.query = json.loads(search_request.query)
            for (field_name, expr) in search_request.query.items():
                field = "properties." + field_name
                for (op, value) in expr.items():
                    key_filter = {field: {f"${op}": value}}
                    queries.update(**key_filter)

        sort_list = []
        if search_request.sortby:
            for sort in search_request.sortby:
                if sort.field == "datetime":
                    sort.field = "properties.datetime"
                if sort.direction == "asc":
                    sort.direction = pymongo.ASCENDING
                else:
                    sort.direction = pymongo.DESCENDING
                sort_list.append((sort.field, sort.direction))
        else:
            sort_list = [("properties.datetime", pymongo.ASCENDING)]

        with self.client.start_session() as session:
            items = (
                self.item_table.find(queries, session=session)
                .limit(search_request.limit)
                .sort(sort_list)
            )

            results = []
            links = []

            for item in items:
                item = self.item_serializer.db_to_stac(item, base_url=base_url)
                results.append(item)

        if self.extension_is_enabled("FieldsExtension"):
            if search_request.query is not None:
                query_include: Set[str] = set(
                    [
                        k if k in Settings.get().indexed_fields else f"properties.{k}"
                        for k in search_request.query.keys()
                    ]
                )
                if not search_request.fields.include:
                    search_request.fields.include = query_include
                else:
                    search_request.fields.include.union(query_include)

            filter_kwargs = search_request.fields.filter_fields

            results = [
                json.loads(stac_pydantic.Item(**feat).json(**filter_kwargs))
                for feat in results
            ]

        context_obj = None
        if self.extension_is_enabled("ContextExtension"):
            count = len(results)
            context_obj = {
                "returned": count if count <= 10 else search_request.limit,
                "limit": search_request.limit,
                "matched": len(results) or None,
            }

        return ItemCollection(
            type="FeatureCollection",
            features=results,
            links=links,
            context=context_obj,
        )
