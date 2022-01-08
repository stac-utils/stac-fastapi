"""Item crud client."""
import json
import logging
import operator
from datetime import datetime
from typing import List, Optional, Set, Type, Union
from urllib.parse import urlencode, urljoin
from stac_fastapi.types import stac as stac_types
import pymongo

import attr
import geoalchemy2 as ga
import sqlalchemy as sa
import stac_pydantic
from fastapi import HTTPException
from pydantic import ValidationError
from shapely.geometry import Polygon as ShapelyPolygon
from shapely.geometry import shape
from sqlakeyset import get_page
from sqlalchemy import func
from sqlalchemy.orm import Session as SqlSession
from stac_pydantic.links import Relations
from stac_pydantic.shared import MimeTypes

from stac_fastapi.mongo import serializers
from stac_fastapi.sqlalchemy.models import database
from stac_fastapi.sqlalchemy.session import Session
from stac_fastapi.sqlalchemy.tokens import PaginationTokenClient
from stac_fastapi.sqlalchemy.types.search import Operator, SQLAlchemySTACSearch
from stac_fastapi.types.config import Settings
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
    item_table: Type[database.Item] = attr.ib(default=database.Item)
    collection_table: Type[database.Collection] = attr.ib(default=database.Collection)
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
        token: Optional[str] = None,
        fields: Optional[List[str]] = None,
        sortby: Optional[str] = None,
        **kwargs,
    ) -> ItemCollection:
        """GET search catalog."""
        queries = {}
        base_url = str(kwargs["request"].base_url)

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
            # filters.append(bbox_filter)

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

    def post_search(
        self, search_request: SQLAlchemySTACSearch, **kwargs
    ) -> ItemCollection:
        """POST search catalog."""
        base_url = str(kwargs["request"].base_url)
        with self.session.reader.context_session() as session:
            token = (
                self.get_token(search_request.token) if search_request.token else False
            )
            query = session.query(self.item_table)

            # Filter by collection
            count = None
            if search_request.collections:
                query = query.join(self.collection_table).filter(
                    sa.or_(
                        *[
                            self.collection_table.id == col_id
                            for col_id in search_request.collections
                        ]
                    )
                )

            # Sort
            if search_request.sortby:
                sort_fields = [
                    getattr(
                        self.item_table.get_field(sort.field),
                        sort.direction.value,
                    )()
                    for sort in search_request.sortby
                ]
                sort_fields.append(self.item_table.id)
                query = query.order_by(*sort_fields)
            else:
                # Default sort is date
                query = query.order_by(
                    self.item_table.datetime.desc(), self.item_table.id
                )

            # Ignore other parameters if ID is present
            if search_request.ids:
                id_filter = sa.or_(
                    *[self.item_table.id == i for i in search_request.ids]
                )
                items = query.filter(id_filter).order_by(self.item_table.id)
                page = get_page(items, per_page=search_request.limit, page=token)
                if self.extension_is_enabled("ContextExtension"):
                    count = len(search_request.ids)
                page.next = (
                    self.insert_token(keyset=page.paging.bookmark_next)
                    if page.paging.has_next
                    else None
                )
                page.previous = (
                    self.insert_token(keyset=page.paging.bookmark_previous)
                    if page.paging.has_previous
                    else None
                )

            else:
                # Spatial query
                geom = None
                if search_request.intersects is not None:
                    geom = shape(search_request.intersects)
                elif search_request.bbox:
                    if len(search_request.bbox) == 4:
                        geom = ShapelyPolygon.from_bounds(*search_request.bbox)
                    elif len(search_request.bbox) == 6:
                        """Shapely doesn't support 3d bounding boxes we'll just use the 2d portion"""
                        bbox_2d = [
                            search_request.bbox[0],
                            search_request.bbox[1],
                            search_request.bbox[3],
                            search_request.bbox[4],
                        ]
                        geom = ShapelyPolygon.from_bounds(*bbox_2d)

                if geom:
                    filter_geom = ga.shape.from_shape(geom, srid=4326)
                    query = query.filter(
                        ga.func.ST_Intersects(self.item_table.geometry, filter_geom)
                    )

                # Temporal query
                if search_request.datetime:
                    # Two tailed query (between)
                    dts = search_request.datetime.split("/")
                    # Non-interval date ex. "2000-02-02T00:00:00.00Z"
                    if len(dts) == 1:
                        query = query.filter(self.item_table.datetime == dts[0])
                    elif ".." not in search_request.datetime:
                        query = query.filter(self.item_table.datetime.between(*dts))
                    # All items after the start date
                    elif dts[0] != "..":
                        query = query.filter(self.item_table.datetime >= dts[0])
                    # All items before the end date
                    elif dts[1] != "..":
                        query = query.filter(self.item_table.datetime <= dts[1])

                # Query fields
                if search_request.query:
                    for (field_name, expr) in search_request.query.items():
                        field = self.item_table.get_field(field_name)
                        for (op, value) in expr.items():
                            if op == Operator.gte:
                                query = query.filter(operator.ge(field, value))
                            elif op == Operator.lte:
                                query = query.filter(operator.le(field, value))
                            else:
                                query = query.filter(op.operator(field, value))

                if self.extension_is_enabled("ContextExtension"):
                    count_query = query.statement.with_only_columns(
                        [func.count()]
                    ).order_by(None)
                    count = query.session.execute(count_query).scalar()
                page = get_page(query, per_page=search_request.limit, page=token)
                # Create dynamic attributes for each page
                page.next = (
                    self.insert_token(keyset=page.paging.bookmark_next)
                    if page.paging.has_next
                    else None
                )
                page.previous = (
                    self.insert_token(keyset=page.paging.bookmark_previous)
                    if page.paging.has_previous
                    else None
                )

            links = []
            if page.next:
                links.append(
                    {
                        "rel": Relations.next.value,
                        "type": "application/geo+json",
                        "href": f"{kwargs['request'].base_url}search",
                        "method": "POST",
                        "body": {"token": page.next},
                        "merge": True,
                    }
                )
            if page.previous:
                links.append(
                    {
                        "rel": Relations.previous.value,
                        "type": "application/geo+json",
                        "href": f"{kwargs['request'].base_url}search",
                        "method": "POST",
                        "body": {"token": page.previous},
                        "merge": True,
                    }
                )

            response_features = []
            filter_kwargs = {}

            for item in page:
                response_features.append(
                    self.item_serializer.db_to_stac(item, base_url=base_url)
                )

            # Use pydantic includes/excludes syntax to implement fields extension
            if self.extension_is_enabled("FieldsExtension"):
                if search_request.query is not None:
                    query_include: Set[str] = set(
                        [
                            k
                            if k in Settings.get().indexed_fields
                            else f"properties.{k}"
                            for k in search_request.query.keys()
                        ]
                    )
                    if not search_request.field.include:
                        search_request.field.include = query_include
                    else:
                        search_request.field.include.union(query_include)

                filter_kwargs = search_request.field.filter_fields
                # Need to pass through `.json()` for proper serialization
                # of datetime
                response_features = [
                    json.loads(stac_pydantic.Item(**feat).json(**filter_kwargs))
                    for feat in response_features
                ]

        context_obj = None
        if self.extension_is_enabled("ContextExtension"):
            context_obj = {
                "returned": len(page),
                "limit": search_request.limit,
                "matched": count,
            }

        return ItemCollection(
            type="FeatureCollection",
            features=response_features,
            links=links,
            context=context_obj,
        )
