"""Item crud client."""
import json
import logging
from datetime import datetime
from typing import List, Optional, Type, Union
from urllib.parse import urljoin
import pymongo

import attr
from sqlalchemy.orm import Session as SqlSession
from stac_pydantic.links import Relations
from stac_pydantic.shared import MimeTypes

from stac_fastapi.mongo import serializers
from stac_fastapi.sqlalchemy.models import database
from stac_fastapi.sqlalchemy.session import Session
from stac_fastapi.sqlalchemy.tokens import PaginationTokenClient
from stac_fastapi.sqlalchemy.types.search import SQLAlchemySTACSearch
from stac_fastapi.types.core import BaseCoreClient
from stac_fastapi.types.errors import NotFoundError
from stac_fastapi.types.stac import Collection, Collections, Item, ItemCollection
from stac_fastapi.mongo.mongo_config import MongoSettings

logger = logging.getLogger(__name__)

NumType = Union[float, int]

@attr.s
class CoreCrudClient(PaginationTokenClient, BaseCoreClient):
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
    def _lookup_id(
        id: str, table: Type[database.BaseModel], session: SqlSession
    ) -> Type[database.BaseModel]:
        """Lookup row by id."""
        row = session.query(table).filter(table.id == id).first()
        if not row:
            raise NotFoundError(f"{table.__name__} {id} not found")
        return row

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

    # pagination commented out - is different with mongo
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

    def bbox2poly(self, bbox):
        poly = [[
            [float(bbox[0]),float(bbox[1])],
            [float(bbox[2]),float(bbox[1])],
            [float(bbox[2]),float(bbox[3])],
            [float(bbox[0]),float(bbox[3])],
            [float(bbox[0]),float(bbox[1])]
        ]]
        return poly

    def return_date(self, datetime):
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
        intersects: Optional[dict] = None,
        token: Optional[str] = None,
        fields: Optional[List[str]] = None,
        sortby: Optional[str] = None,
        **kwargs,
    ) -> ItemCollection:
        """GET search catalog."""
        queries = {}
        base_url = str(kwargs["request"].base_url)

        if collections:
            for collection in collections:
                collection_filter = {"collection": collection}
                queries.update(**collection_filter)

        if ids:
            for id in ids:
                id_filter = {"id": id}
                queries.update(**id_filter)

        # Australia bbox = 101.125653,-46.522368,162.473309,-4.862972
        if bbox:
            poly = self.bbox2poly(bbox)
            bbox_filter = {
                "geometry": {"$geoIntersects": { "$geometry": { "type": 'Polygon' , "coordinates": poly }}}
            }
            queries.update(**bbox_filter)

            # bbox_filter = {
            #     "bbox": {"$geoWithin": { "$box": [[float(bbox[0]), float(bbox[1])], [float(bbox[2]), float(bbox[3])]]}},
            # }
            # queries.update(**bbox_filter)

        if intersects:
            intersect_filter = {
                "geometry": {"$geoIntersects": { "$geometry": { "type": intersects.type , "coordinates": intersects.coordinates }}}
            }
            queries.update(**intersect_filter)

        if datetime:
            date_filter = self.return_date(datetime)
            queries.update(**date_filter)
     
        # {"gsd": {"eq":16}}
        if query:
            query = json.loads(query)
            for (field_name, expr) in query.items():
                field = "properties." + field_name
                for (op, value) in expr.items():
                    key_filter = {
                        field: { f"${op}":value }
                    }
                    queries.update(**key_filter)

        exclude_list = []
        if fields:
            for afield in fields:
                if afield[0] == "-":
                    exclude_list.append(afield[1:])

        sort_list = []
        if sortby:
            for sort in sortby:
                pass

        items = (
            self.db.stac_item
            .find(queries)
            .limit(limit)
            .sort([("properties.datetime", pymongo.ASCENDING), ("id", pymongo.ASCENDING)])
        )

        results = []
        links = []

        try:
            for item in items:
                item = self.item_serializer.db_to_stac(item, base_url=base_url)
                if field:
                    for key in exclude_list:
                        item.pop(key)
                results.append(item)
        except:
            return results

        count = None
        if self.extension_is_enabled("ContextExtension"):
            count = len(results)

        context_obj = None
        if self.extension_is_enabled("ContextExtension"):
            context_obj = {
                "returned": count,
                "limit": limit,
                "matched": count,
            }

        return ItemCollection(
            type="FeatureCollection",
            features=results,
            links=links,
            context=context_obj,
        )

    def parse_fields(self, fields: dict):
        field_list = []
        for field in fields["exclude"]:
            field_string = "-" + field
            field_list.append(field_string)
        return field_list

    def post_search(
        self, search_request: SQLAlchemySTACSearch, **kwargs
    ) -> ItemCollection:
        """POST search catalog."""
        if search_request.fields:
            search_request.fields = self.parse_fields(search_request.fields)
        return self.get_search(
            collections=search_request.collections,
            ids=search_request.ids,
            limit=search_request.limit,
            bbox=search_request.bbox,
            intersects=search_request.intersects,
            query=search_request.query,
            datetime=search_request.datetime,
            fields=search_request.field,
            request=kwargs["request"]
        )
