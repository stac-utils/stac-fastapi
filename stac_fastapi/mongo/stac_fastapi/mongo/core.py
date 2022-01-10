"""Item crud client."""
import json
import logging
from datetime import datetime
from typing import List, Optional, Type, Union
from urllib.parse import urljoin
import pymongo

import attr
from stac_pydantic.links import Relations
from stac_pydantic.shared import MimeTypes
from fastapi import HTTPException
from pydantic import ValidationError

from stac_fastapi.mongo import serializers
from stac_fastapi.mongo.session import Session
from stac_fastapi.mongo.types.search import SQLAlchemySTACSearch
from stac_fastapi.types.core import BaseCoreClient
from stac_fastapi.types.errors import NotFoundError
from stac_fastapi.types.stac import Collection, Collections, Item, ItemCollection
from stac_fastapi.mongo.mongo_config import MongoSettings

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
    db = MongoSettings()

    @staticmethod
    def _lookup_id(id: str, table, session):
        """Lookup row by id."""
        pass

    def all_collections(self, **kwargs) -> Collections:
        """Read all collections from the database."""
        base_url = str(kwargs["request"].base_url)
        collections = self.db.stac_collection.find()
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

    def get_collection(self, id: str, **kwargs) -> Collection:
        """Get collection by id."""
        collection = self.db.stac_collection.find_one({"id": id})
        base_url = str(kwargs["request"].base_url)

        if not collection:
            raise NotFoundError(f"{id} not found in database")

        return self.collection_serializer.db_to_stac(collection, base_url)

    def item_collection(
        self, id: str, limit: int = 10, token: str = None, **kwargs
    ) -> ItemCollection:
        """Read an item collection from the database."""
        links = []
        response_features = []
        base_url = str(kwargs["request"].base_url)
        collection_children = ( 
            self.db.stac_item
            .find({"collection": id})
            .sort([("properties.datetime", pymongo.ASCENDING), ("id", pymongo.ASCENDING)])
        )
        count = None
        if self.extension_is_enabled("ContextExtension"):
            if type(collection_children) == list:
                count = len(collection_children)

        context_obj = None
        if self.extension_is_enabled("ContextExtension"):
            context_obj = {
                "returned": count,
                "limit": limit,
                "matched": count,
            }
        for item in collection_children:
            response_features.append(
                self.item_serializer.db_to_stac(item, base_url=base_url)
            )

        return ItemCollection(
            type="FeatureCollection",
            features=response_features,
            links=links,
            context=context_obj,
        )

    def get_item(self, item_id: str, collection_id: str, **kwargs) -> Item:
        """Get item by item id, collection id."""
        item = self.db.stac_item.find_one({"id": item_id, "collection": collection_id})
        base_url = str(kwargs["request"].base_url)

        if not item:
            raise NotFoundError(f"{item_id} not found in collection {collection_id}")

        return self.item_serializer.db_to_stac(item, base_url)

    def _bbox2poly(self, bbox):
        poly = [[
            [float(bbox[0]),float(bbox[1])],
            [float(bbox[2]),float(bbox[1])],
            [float(bbox[2]),float(bbox[3])],
            [float(bbox[0]),float(bbox[3])],
            [float(bbox[0]),float(bbox[1])]
        ]]
        return poly

    def _return_date(self, datetime):
        x = datetime.split("/")
        start_date = x[0]
        end_date = x[1]
        if(start_date=='..'):
            start_date = '1900-10-01T00:00:00Z'
        if(end_date=='..'):
            end_date = '2200-12-01T12:31:12Z'
        return { "properties.datetime": { "$lt":end_date, "$gte":start_date} }

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
            search_request = SQLAlchemySTACSearch(**base_args)
        except ValidationError:
            raise HTTPException(status_code=400, detail="Invalid parameters provided")
        resp = self.post_search(search_request, request=kwargs["request"])

        return resp

    def _parse_fields(self, fields: dict):
        field_list = []
        for field in fields["exclude"]:
            field_string = "-" + field
            field_list.append(field_string)
        return field_list

    def post_search(
        self, search_request: SQLAlchemySTACSearch, **kwargs
    ) -> ItemCollection:
        """POST search catalog."""
        base_url = str(kwargs["request"].base_url)
        queries = {}

        if search_request.collections:
            for collection in search_request.collections:
                collection_filter = {"collection": collection}
                queries.update(**collection_filter)

        if search_request.ids:
            # for id in search_request.ids:
            id_filter = {"id": {"$in": search_request.ids}}
            queries.update(**id_filter)

        # Australia bbox = 101.125653,-46.522368,162.473309,-4.862972
        if search_request.bbox:
            # check for 3d bbox
            if len(search_request.bbox) == 6:
                search_request.bbox = [search_request.bbox[0], search_request.bbox[1], search_request.bbox[3], search_request.bbox[4]]
            poly = self._bbox2poly(search_request.bbox)
            bbox_filter = {
                "geometry": {"$geoIntersects": { "$geometry": { "type": 'Polygon' , "coordinates": poly }}}
            }
            queries.update(**bbox_filter)

            # bbox_filter = {
            #     "bbox": {"$geoWithin": { "$box": [[float(bbox[0]), float(bbox[1])], [float(bbox[2]), float(bbox[3])]]}},
            # }
            # queries.update(**bbox_filter)

        if search_request.intersects:
            intersect_filter = {
                "geometry": {"$geoIntersects": { "$geometry": { "type": search_request.intersects.type , "coordinates": search_request.intersects.coordinates }}}
            }
            queries.update(**intersect_filter)

        if search_request.datetime:
            date_filter = self._return_date(str(search_request.datetime))
            queries.update(**date_filter)
     
        # {"gsd": {"eq":16}}
        if search_request.query:
            if type(search_request.query) == str:
                search_request.query = json.loads(search_request.query)
            for (field_name, expr) in search_request.query.items():
                field = "properties." + field_name
                for (op, value) in expr.items():
                    key_filter = {
                        field: { f"${op}":value }
                    }
                    queries.update(**key_filter)

        exclude_list = []

        # if search_request.field:
        #     search_request.fields = self._parse_fields(search_request.field)

        if search_request.field:
            for afield in search_request.field:
                if afield[0] == "-":
                    exclude_list.append(afield[1:])

        sort_list = []
        if search_request.sortby:
            for sort in search_request.sortby:
                pass

        items = []
        items = (
            self.db.stac_item
            .find(queries)
            .limit(search_request.limit)
            .sort([("properties.datetime", pymongo.DESCENDING), ("id", pymongo.DESCENDING)])
        )

        results = []
        links = []

        for item in items:
            item = self.item_serializer.db_to_stac(item, base_url=base_url)
            if search_request.field:
                for key in exclude_list:
                    item.pop(key)
            results.append(item)
            
        count = None
        if self.extension_is_enabled("ContextExtension"):
            count = len(results)

        context_obj = None
        if self.extension_is_enabled("ContextExtension"):
            context_obj = {
                "returned": count,
                "limit": search_request.limit,
                "matched": count,
            }

        return ItemCollection(
            type="FeatureCollection",
            features=results,
            links=links,
            context=context_obj,
        )