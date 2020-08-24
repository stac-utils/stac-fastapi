"""Item crud client."""
import logging
from dataclasses import dataclass
from typing import List, Optional, Type, Union

import sqlalchemy as sa
from fastapi import Depends

import geoalchemy2 as ga
from sqlakeyset import get_page
from stac_api import config, errors
from stac_api.clients.base import BaseCoreClient
from stac_api.clients.postgres.base import PostgresClient
from stac_api.clients.postgres.tokens import (
    PaginationTokenClient,
    pagination_token_client_factory,
)
from stac_api.config import ApiExtensions
from stac_api.errors import DatabaseError
from stac_api.models import database, schemas
from stac_pydantic import ItemCollection
from stac_pydantic.api.extensions.paging import PaginationLink
from stac_pydantic.shared import Relations

logger = logging.getLogger(__name__)

NumType = Union[float, int]


@dataclass
class CoreCrudClient(PostgresClient, BaseCoreClient):
    """Item specific CRUD operations"""

    pagination_client: Optional[PaginationTokenClient] = None
    table: Type[database.Item] = database.Item
    collection_table: Type[database.Collection] = database.Collection

    def all_collections(self, **kwargs) -> List[schemas.Collection]:
        """Read all collections from the database"""
        try:
            collections = self.reader_session.query(self.collection_table).all()
        except Exception as e:
            logger.error(e, exc_info=True)
            raise errors.DatabaseError(
                "Unhandled database error when getting item collection"
            )

        response = []
        for collection in collections:
            collection.base_url = str(kwargs["request"].base_url)
            response.append(schemas.Collection.from_orm(collection))
        return response

    def get_collection(self, id: str, **kwargs) -> schemas.Collection:
        """Get collection by id"""
        collection = self.lookup_id(id, table=self.collection_table).first()
        collection.base_url = str(kwargs["request"].base_url)
        return schemas.Collection.from_orm(collection)

    def item_collection(
        self, id: str, limit: int = 10, token: str = None, **kwargs
    ) -> ItemCollection:
        """Read an item collection from the database"""
        try:
            collection_children = (
                self.lookup_id(id, table=self.collection_table)
                .first()
                .children.order_by(database.Item.datetime.desc(), database.Item.id)
            )
            count = None
            if config.settings.api_extension_is_enabled(config.ApiExtensions.context):
                count = collection_children.count()
            token = self.pagination_client.get(token) if token else token
            page = get_page(collection_children, per_page=limit, page=(token or False))
            # Create dynamic attributes for each page
            page.next = (
                self.pagination_client.insert(keyset=page.paging.bookmark_next)
                if page.paging.has_next
                else None
            )
            page.previous = (
                self.pagination_client.insert(keyset=page.paging.bookmark_previous)
                if page.paging.has_previous
                else None
            )
        except errors.NotFoundError:
            raise
        except Exception as e:
            logger.error(e, exc_info=True)
            raise errors.DatabaseError(
                "Unhandled database error when getting collection children"
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
        if config.settings.api_extension_is_enabled(ApiExtensions.context):
            context_obj = {"returned": len(page), "limit": limit, "matched": count}

        return ItemCollection(
            type="FeatureCollection",
            context=context_obj,
            features=response_features,
            links=links,
        )

    def get_item(self, id: str, **kwargs) -> schemas.Item:
        """Get item by id"""
        obj = self.lookup_id(id).first()
        obj.base_url = str(kwargs["request"].base_url)
        return schemas.Item.from_orm(obj)

    def search(self, search_request: schemas.STACSearch, **kwargs) -> ItemCollection:
        """STAC search operation"""
        token = (
            self.pagination_client.get(search_request.token)
            if search_request.token
            else False
        )
        query = self.reader_session.query(self.table)
        count = None

        # Filter by collection
        if search_request.collections:
            collection_filter = sa.or_(
                *[
                    self.table.collection_id == col_id
                    for col_id in search_request.collections
                ]
            )
            query = query.filter(collection_filter)

        # Sort
        if search_request.sortby:
            sort_fields = [
                getattr(self.table.get_field(sort.field), sort.direction.value)()
                for sort in search_request.sortby
            ]
            # Add id to end of sort to ensure unique keyset
            sort_fields.append(self.table.id)
            query = query.order_by(*sort_fields)
        else:
            # Default sort is date and id
            query = query.order_by(self.table.datetime.desc(), self.table.id)

        # Ignore other parameters if ID is present
        if search_request.ids:
            id_filter = sa.or_(*[self.table.id == i for i in search_request.ids])
            try:
                items = query.filter(id_filter).order_by(self.table.id)
                page = get_page(items, per_page=search_request.limit, page=token)
                if config.settings.api_extension_is_enabled(ApiExtensions.context):
                    count = len(search_request.ids)
                page.next = (
                    self.pagination_client.insert(keyset=page.paging.bookmark_next)
                    if page.paging.has_next
                    else None
                )
                page.previous = (
                    self.pagination_client.insert(keyset=page.paging.bookmark_previous)
                    if page.paging.has_previous
                    else None
                )
            except Exception as e:
                logger.error(e, exc_info=True)
                raise DatabaseError(
                    "Unhandled database error when searching for items by id"
                )
        else:
            # Spatial query
            poly = search_request.polygon()
            if poly:
                filter_geom = ga.shape.from_shape(poly, srid=4326)
                query = query.filter(
                    ga.func.ST_Intersects(self.table.geometry, filter_geom)
                )

            # Temporal query
            if search_request.datetime:
                # Two tailed query (between)
                if ".." not in search_request.datetime:
                    query = query.filter(
                        self.table.datetime.between(*search_request.datetime)
                    )
                # All items after the start date
                if search_request.datetime[0] != "..":
                    query = query.filter(
                        self.table.datetime >= search_request.datetime[0]
                    )
                # All items before the end date
                if search_request.datetime[1] != "..":
                    query = query.filter(
                        self.table.datetime <= search_request.datetime[1]
                    )

            # Query fields
            if search_request.query:
                for (field_name, expr) in search_request.query.items():
                    field = self.table.get_field(field_name)
                    for (op, value) in expr.items():
                        query = query.filter(op.operator(field, value))

            try:
                if config.settings.api_extension_is_enabled(ApiExtensions.context):
                    count = query.count()
                page = get_page(query, per_page=search_request.limit, page=token)
                # Create dynamic attributes for each page
                page.next = (
                    self.pagination_client.insert(keyset=page.paging.bookmark_next)
                    if page.paging.has_next
                    else None
                )
                page.previous = (
                    self.pagination_client.insert(keyset=page.paging.bookmark_previous)
                    if page.paging.has_previous
                    else None
                )
            except Exception as e:
                logger.error(e, exc_info=True)
                raise DatabaseError(
                    "Unhandled database error during spatial/temporal query"
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
        if config.settings.api_extension_is_enabled(ApiExtensions.fields):
            filter_kwargs = search_request.field.filter_fields

        for item in page:
            item.base_url = str(kwargs["request"].base_url)
            response_features.append(
                schemas.Item.from_orm(item).to_dict(**filter_kwargs)
            )

        # Geoalchemy doesn't have a good way of calculating extent of many features, so we'll calculate it outside the db
        bbox = None
        if count > 0:
            xvals = [
                item
                for sublist in [
                    [float(item["bbox"][0]), float(item["bbox"][2])]
                    for item in response_features
                ]
                for item in sublist
            ]
            yvals = [
                item
                for sublist in [
                    [float(item["bbox"][1]), float(item["bbox"][3])]
                    for item in response_features
                ]
                for item in sublist
            ]
            bbox = (min(xvals), min(yvals), max(xvals), max(yvals))

        context_obj = None
        if config.settings.api_extension_is_enabled(ApiExtensions.context):
            context_obj = {
                "returned": len(page),
                "limit": search_request.limit,
                "matched": count,
            }

        return ItemCollection(
            type="FeatureCollection",
            context=context_obj,
            features=response_features,
            links=links,
            bbox=bbox,
        )


def core_crud_client_factory(
    pagination_client: PaginationTokenClient = Depends(pagination_token_client_factory),
) -> CoreCrudClient:
    """FastAPI dependency."""
    return CoreCrudClient(table=database.Item, pagination_client=pagination_client,)
