"""Item crud client."""
import json
import logging
import operator
from datetime import datetime
from typing import List, Optional, Set, Type, Union
from urllib.parse import unquote_plus, urlencode, urljoin

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

from stac_fastapi.sqlalchemy import serializers
from stac_fastapi.sqlalchemy.extensions.query import Operator
from stac_fastapi.sqlalchemy.models import database
from stac_fastapi.sqlalchemy.session import Session
from stac_fastapi.sqlalchemy.tokens import PaginationTokenClient
from stac_fastapi.types.config import Settings
from stac_fastapi.types.core import BaseCoreClient
from stac_fastapi.types.errors import NotFoundError
from stac_fastapi.types.search import BaseSearchPostRequest
from stac_fastapi.types.stac import Collection, Collections, Item, ItemCollection

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
        with self.session.reader.context_session() as session:
            collections = session.query(self.collection_table).all()
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
        with self.session.reader.context_session() as session:
            collection = self._lookup_id(collection_id, self.collection_table, session)
            return self.collection_serializer.db_to_stac(collection, base_url)

    def item_collection(
        self,
        collection_id: str,
        bbox: Optional[List[NumType]] = None,
        datetime: Optional[str] = None,
        limit: int = 10,
        token: str = None,
        **kwargs,
    ) -> ItemCollection:
        """Read an item collection from the database."""
        base_url = str(kwargs["request"].base_url)
        with self.session.reader.context_session() as session:
            # Look up the collection first to get a 404 if it doesn't exist
            _ = self._lookup_id(collection_id, self.collection_table, session)
            query = (
                session.query(self.item_table)
                .join(self.collection_table)
                .filter(self.collection_table.id == collection_id)
                .order_by(self.item_table.datetime.desc(), self.item_table.id)
            )
            # Spatial query
            geom = None
            if bbox:
                bbox = [float(x) for x in bbox]
                if len(bbox) == 4:
                    geom = ShapelyPolygon.from_bounds(*bbox)
                elif len(bbox) == 6:
                    """Shapely doesn't support 3d bounding boxes so use the 2d portion"""
                    bbox_2d = [bbox[0], bbox[1], bbox[3], bbox[4]]
                    geom = ShapelyPolygon.from_bounds(*bbox_2d)
            if geom:
                filter_geom = ga.shape.from_shape(geom, srid=4326)
                query = query.filter(
                    ga.func.ST_Intersects(self.item_table.geometry, filter_geom)
                )

            # Temporal query
            if datetime:
                # Two tailed query (between)
                dts = datetime.split("/")
                # Non-interval date ex. "2000-02-02T00:00:00.00Z"
                if len(dts) == 1:
                    query = query.filter(self.item_table.datetime == dts[0])
                # is there a benefit to between instead of >= and <= ?
                elif dts[0] not in ["", ".."] and dts[1] not in ["", ".."]:
                    query = query.filter(self.item_table.datetime.between(*dts))
                # All items after the start date
                elif dts[0] not in ["", ".."]:
                    query = query.filter(self.item_table.datetime >= dts[0])
                # All items before the end date
                elif dts[1] not in ["", ".."]:
                    query = query.filter(self.item_table.datetime <= dts[1])

            count = None
            if self.extension_is_enabled("ContextExtension"):
                count_query = query.statement.with_only_columns(
                    [func.count()]
                ).order_by(None)
                count = query.session.execute(count_query).scalar()
            token = self.get_token(token) if token else token
            page = get_page(query, per_page=limit, page=(token or False))
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

            links = [
                {
                    "rel": Relations.self.value,
                    "type": "application/geo+json",
                    "href": str(kwargs["request"].url),
                },
                {
                    "rel": Relations.root.value,
                    "type": "application/json",
                    "href": str(kwargs["request"].base_url),
                },
                {
                    "rel": Relations.parent.value,
                    "type": "application/json",
                    "href": str(kwargs["request"].base_url),
                },
            ]
            if page.next:
                links.append(
                    {
                        "rel": Relations.next.value,
                        "type": "application/geo+json",
                        "href": f"{kwargs['request'].base_url}collections/{collection_id}/items?token={page.next}&limit={limit}",
                        "method": "GET",
                    }
                )
            if page.previous:
                links.append(
                    {
                        "rel": Relations.previous.value,
                        "type": "application/geo+json",
                        "href": f"{kwargs['request'].base_url}collections/{collection_id}/items?token={page.previous}&limit={limit}",
                        "method": "GET",
                    }
                )

            response_features = []
            for item in page:
                response_features.append(
                    self.item_serializer.db_to_stac(item, base_url=base_url)
                )

            context_obj = None
            if self.extension_is_enabled("ContextExtension"):
                context_obj = {
                    "returned": len(page),
                    "limit": limit,
                    "matched": count,
                }

            return ItemCollection(
                type="FeatureCollection",
                features=response_features,
                links=links,
                context=context_obj,
            )

    def get_item(self, item_id: str, collection_id: str, **kwargs) -> Item:
        """Get item by id."""
        base_url = str(kwargs["request"].base_url)
        with self.session.reader.context_session() as session:
            db_query = session.query(self.item_table)
            db_query = db_query.filter(self.item_table.collection_id == collection_id)
            db_query = db_query.filter(self.item_table.id == item_id)
            item = db_query.first()
            if not item:
                raise NotFoundError(f"{self.item_table.__name__} {item_id} not found")
            return self.item_serializer.db_to_stac(item, base_url=base_url)

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
        intersects: Optional[str] = None,
        **kwargs,
    ) -> ItemCollection:
        """GET search catalog."""
        # Parse request parameters
        base_args = {
            "collections": collections,
            "ids": ids,
            "bbox": bbox,
            "limit": limit,
            "token": token,
            "query": json.loads(unquote_plus(query)) if query else query,
        }

        if datetime:
            base_args["datetime"] = datetime

        if intersects:
            base_args["intersects"] = json.loads(unquote_plus(intersects))

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

        # Pagination
        page_links = []
        for link in resp["links"]:
            if link["rel"] == Relations.next or link["rel"] == Relations.previous:
                query_params = dict(kwargs["request"].query_params)
                if link["body"] and link["merge"]:
                    query_params.update(link["body"])
                link["method"] = "GET"
                link["href"] = f"{link['body']}?{urlencode(query_params)}"
                link["body"] = None
                link["merge"] = False
                page_links.append(link)
            else:
                page_links.append(link)
        resp["links"] = page_links
        return resp

    def post_search(
        self, search_request: BaseSearchPostRequest, **kwargs
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
                    # is there a benefit to between instead of >= and <= ?
                    elif dts[0] not in ["", ".."] and dts[1] not in ["", ".."]:
                        query = query.filter(self.item_table.datetime.between(*dts))
                    # All items after the start date
                    elif dts[0] not in ["", ".."]:
                        query = query.filter(self.item_table.datetime >= dts[0])
                    # All items before the end date
                    elif dts[1] not in ["", ".."]:
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
                    if not search_request.fields.include:
                        search_request.fields.include = query_include
                    else:
                        search_request.fields.include.union(query_include)

                filter_kwargs = search_request.fields.filter_fields
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
