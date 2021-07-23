"""api request/response models."""

import abc
from typing import Dict, Optional, Type, Union

import attr
from fastapi import Body, Path
from pydantic import BaseModel, create_model
from pydantic.fields import UndefinedType


def _create_request_model(model: Type[BaseModel]) -> Type[BaseModel]:
    """Create a pydantic model for validating request bodies."""
    fields = {}
    for (k, v) in model.__fields__.items():
        # TODO: Filter out fields based on which extensions are present
        field_info = v.field_info
        body = Body(
            None
            if isinstance(field_info.default, UndefinedType)
            else field_info.default,
            default_factory=field_info.default_factory,
            alias=field_info.alias,
            alias_priority=field_info.alias_priority,
            title=field_info.title,
            description=field_info.description,
            const=field_info.const,
            gt=field_info.gt,
            ge=field_info.ge,
            lt=field_info.lt,
            le=field_info.le,
            multiple_of=field_info.multiple_of,
            min_items=field_info.min_items,
            max_items=field_info.max_items,
            min_length=field_info.min_length,
            max_length=field_info.max_length,
            regex=field_info.regex,
            extra=field_info.extra,
        )
        fields[k] = (v.outer_type_, body)
    return create_model(model.__name__, **fields, __base__=model)


@attr.s  # type:ignore
class APIRequest(abc.ABC):
    """Generic API Request base class."""

    @abc.abstractmethod
    def kwargs(self) -> Dict:
        """Transform api request params into format which matches the signature of the endpoint."""
        ...


@attr.s  # type:ignore
class CollectionUri(APIRequest):
    """Delete collection."""

    collectionId: str = attr.ib(default=Path(..., description="Collection ID"))

    def kwargs(self) -> Dict:
        """kwargs."""
        return {"id": self.collectionId}


@attr.s
class ItemUri(CollectionUri):
    """Delete item."""

    itemId: str = attr.ib(default=Path(..., description="Item ID"))

    def kwargs(self) -> Dict:
        """kwargs."""
        return {"collection_id": self.collectionId, "item_id": self.itemId}


@attr.s
class EmptyRequest(APIRequest):
    """Empty request."""

    def kwargs(self) -> Dict:
        """kwargs."""
        return {}


@attr.s
class ItemCollectionUri(CollectionUri):
    """Get item collection."""

    limit: int = attr.ib(default=10)
    token: str = attr.ib(default=None)

    def kwargs(self) -> Dict:
        """kwargs."""
        return {
            "id": self.collectionId,
            "limit": self.limit,
            "token": self.token,
        }


@attr.s
class SearchGetRequest(APIRequest):
    """GET search request."""

    collections: Optional[str] = attr.ib(default=None)
    ids: Optional[str] = attr.ib(default=None)
    bbox: Optional[str] = attr.ib(default=None)
    datetime: Optional[Union[str]] = attr.ib(default=None)
    limit: Optional[int] = attr.ib(default=10)
    query: Optional[str] = attr.ib(default=None)
    token: Optional[str] = attr.ib(default=None)
    fields: Optional[str] = attr.ib(default=None)
    sortby: Optional[str] = attr.ib(default=None)

    def kwargs(self) -> Dict:
        """kwargs."""
        return {
            "collections": self.collections.split(",")
            if self.collections
            else self.collections,
            "ids": self.ids.split(",") if self.ids else self.ids,
            "bbox": self.bbox.split(",") if self.bbox else self.bbox,
            "datetime": self.datetime,
            "limit": self.limit,
            "query": self.query,
            "token": self.token,
            "fields": self.fields.split(",") if self.fields else self.fields,
            "sortby": self.sortby.split(",") if self.sortby else self.sortby,
        }
