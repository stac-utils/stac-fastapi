"""Item crud client."""
import json
import logging
from datetime import datetime
from typing import Any, Dict, List, Optional, Set, Type, Union
from urllib.parse import urlencode

import attr
import geoalchemy2 as ga
import sqlalchemy as sa
from shapely.geometry import Polygon as ShapelyPolygon
from shapely.geometry import shape
from sqlakeyset import get_page
from sqlalchemy import func
from sqlalchemy.orm import Session as SqlSession
from stac_pydantic import ItemCollection
from stac_pydantic.api import ConformanceClasses
from stac_pydantic.links import PaginationLink, Relations

from stac_fastapi.extensions.core import ContextExtension, FieldsExtension
from stac_fastapi.sqlalchemy.models import database, schemas
from stac_fastapi.sqlalchemy.session import Session
from stac_fastapi.sqlalchemy.tokens import PaginationTokenClient
from stac_fastapi.sqlalchemy.types.search import SQLAlchemySTACSearch
from stac_fastapi.types.config import Settings
from stac_fastapi.types.core import BaseCoreClient
from stac_fastapi.types.errors import NotFoundError

logger = logging.getLogger(__name__)

NumType = Union[float, int]


@attr.s
class CoreCrudClient(PaginationTokenClient, BaseCoreClient):
    """Client for core endpoints defined by stac."""

    session: Session = attr.ib(default=attr.Factory(Session.create_from_env))
    item_table: Type[database.Item] = attr.ib(default=database.Item)
    collection_table: Type[database.Collection] = attr.ib(default=database.Collection)

    @staticmethod
    def _lookup_id(
        id: str, table: Type[database.BaseModel], session: SqlSession
    ) -> Type[database.BaseModel]:
        """Lookup row by id."""
        row = session.query(table).filter(table.id == id).first()
        if not row:
            raise NotFoundError(f"{table.__name__} {id} not found")
        return row

    def conformance(self, **kwargs) -> ConformanceClasses:
        """Conformance classes."""
        return ConformanceClasses(
            conformsTo=[
                "https://stacspec.org/STAC-api.html",
                "http://docs.opengeospatial.org/is/17-069r3/17-069r3.html#ats_geojson",
            ]
        )

    def all_collections(self, **kwargs) -> List[schemas.Collection]:
        """Read all collections from the database."""
        with self.session.reader.context_session() as session:
            collections = session.query(self.collection_table).all()
            response = []
            for collection in collections:
                collection.base_url = str(kwargs["request"].base_url)
                response.append(schemas.Collection.from_orm(collection))
            return response

    def get_collection(self, id: str, **kwargs) -> schemas.Collection:
        """Get collection by id."""
        with self.session.reader.context_session() as session:
            collection = self._lookup_id(id, self.collection_table, session)
            # TODO: Don't do this
            collection.base_url = str(kwargs["request"].base_url)
            return schemas.Collection.from_orm(collection)

    def item_collection(
        self, id: str, limit: int = 10, token: str = None, **kwargs
    ) -> ItemCollection:
        """Read an item collection from the database."""
        with self.session.reader.context_session() as session:
            collection_children = (
                session.query(self.item_table)
                .join(self.collection_table)
                .filter(self.collection_table.id == id)
                .order_by(self.item_table.datetime.desc(), self.item_table.id)
            )
            count = None
            if self.extension_is_enabled(ContextExtension):
                count_query = collection_children.statement.with_only_columns(
                    [func.count()]
                ).order_by(None)
                count = collection_children.session.execute(count_query).scalar()
            token = self.get_token(token) if token else token
            page = get_page(collection_children, per_page=limit, page=(token or False))
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
                    PaginationLink(
                        rel=Relations.next,
                        type="application/geo+json",
                        href=f"{kwargs['request'].base_url}collections/{id}/items?token={page.next}&limit={limit}",
                        method="GET",
                    )
                )
            if page.previous:
                links.append(
                    PaginationLink(
                        rel=Relations.previous,
                        type="application/geo+json",
                        href=f"{kwargs['request'].base_url}collections/{id}/items?token={page.previous}&limit={limit}",
                        method="GET",
                    )
                )

            response_features = []
            for item in page:
                item.base_url = str(kwargs["request"].base_url)
                response_features.append(schemas.Item.from_orm(item))

            context_obj = None
            if self.extension_is_enabled(ContextExtension):
                context_obj = {
                    "returned": len(page),
                    "limit": limit,
                    "matched": count,
                }

            return ItemCollection(
                type="FeatureCollection",
                context=context_obj,
                features=response_features,
                links=links,
            )

    def get_item(self, item_id: str, collection_id: str, **kwargs) -> schemas.Item:
        """Get item by id."""
        with self.session.reader.context_session() as session:
            item = self._lookup_id(item_id, self.item_table, session)
            item.base_url = str(kwargs["request"].base_url)
            return schemas.Item.from_orm(item)

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
    ) -> Dict[str, Any]:
        """GET search catalog."""
        # Parse request parameters
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
        search_request = SQLAlchemySTACSearch(**base_args)
        resp = self.post_search(search_request, request=kwargs["request"])

        # Pagination
        page_links = []
        for link in resp["links"]:
            if link.rel == Relations.next or link.rel == Relations.previous:
                query_params = dict(kwargs["request"].query_params)
                if link.body and link.merge:
                    query_params.update(link.body)
                link.method = "GET"
                link.href = f"{link.href}?{urlencode(query_params)}"
                link.body = None
                link.merge = False
                page_links.append(link)
            else:
                page_links.append(link)
        resp["links"] = page_links
        return resp

    def post_search(
        self, search_request: SQLAlchemySTACSearch, **kwargs
    ) -> Dict[str, Any]:
        """POST search catalog."""
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
                if self.extension_is_enabled(ContextExtension):
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
                poly = None
                if search_request.intersects is not None:
                    poly = shape(search_request.intersects)
                elif search_request.bbox:
                    poly = ShapelyPolygon.from_bounds(*search_request.bbox)

                if poly:
                    filter_geom = ga.shape.from_shape(poly, srid=4326)
                    query = query.filter(
                        ga.func.ST_Intersects(self.item_table.geometry, filter_geom)
                    )

                # Temporal query
                if search_request.datetime:
                    # Two tailed query (between)
                    dts = search_request.datetime.split("/")
                    if ".." not in search_request.datetime:
                        query = query.filter(self.item_table.datetime.between(*dts))
                    # All items after the start date
                    if dts[0] != "..":
                        query = query.filter(self.item_table.datetime >= dts[0])
                    # All items before the end date
                    if dts[1] != "..":
                        query = query.filter(self.item_table.datetime <= dts[1])

                # Query fields
                if search_request.query:
                    for (field_name, expr) in search_request.query.items():
                        field = self.item_table.get_field(field_name)
                        for (op, value) in expr.items():
                            query = query.filter(op.operator(field, value))

                if self.extension_is_enabled(ContextExtension):
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
                    PaginationLink(
                        rel=Relations.next,
                        type="application/geo+json",
                        href=f"{kwargs['request'].base_url}search",
                        method="POST",
                        body={"token": page.next},
                        merge=True,
                    )
                )
            if page.previous:
                links.append(
                    PaginationLink(
                        rel=Relations.previous,
                        type="application/geo+json",
                        href=f"{kwargs['request'].base_url}search",
                        method="POST",
                        body={"token": page.previous},
                        merge=True,
                    )
                )

            response_features = []
            filter_kwargs = {}
            if self.extension_is_enabled(FieldsExtension):
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

            xvals = []
            yvals = []
            for item in page:
                item.base_url = str(kwargs["request"].base_url)
                item_model = schemas.Item.from_orm(item)
                xvals += [item_model.bbox[0], item_model.bbox[2]]
                yvals += [item_model.bbox[1], item_model.bbox[3]]
                response_features.append(item_model.to_dict(**filter_kwargs))

        try:
            bbox = (min(xvals), min(yvals), max(xvals), max(yvals))
        except ValueError:
            bbox = None

        context_obj = None
        if self.extension_is_enabled(ContextExtension):
            context_obj = {
                "returned": len(page),
                "limit": search_request.limit,
                "matched": count,
            }

        return {
            "type": "FeatureCollection",
            "context": context_obj,
            "features": response_features,
            "links": links,
            "bbox": bbox,
        }
