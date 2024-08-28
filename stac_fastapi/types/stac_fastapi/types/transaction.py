"""Transaction extension types."""

import sys
from typing import Any, Dict, List, Literal, Optional, Union

import attr
from fastapi import Body
from pydantic import BaseModel
from stac_pydantic import Collection, Item, ItemCollection
from stac_pydantic.shared import BBox
from typing_extensions import Annotated

from stac_fastapi.api.models import CollectionUri, ItemUri

if sys.version_info < (3, 12, 0):
    from typing_extensions import TypedDict
else:
    from typing import TypedDict


class PartialCollection(TypedDict, total=False):
    """Partial STAC Collection."""

    type: Optional[str]
    stac_version: Optional[str]
    stac_extensions: Optional[List[str]]
    id: Optional[str]
    title: Optional[str]
    description: Optional[str]
    links: List[Dict[str, Any]]
    keywords: Optional[List[str]]
    license: Optional[str]
    providers: Optional[List[Dict[str, Any]]]
    extent: Optional[Dict[str, Any]]
    summaries: Optional[Dict[str, Any]]
    assets: Optional[Dict[str, Any]]


class PartialItem(TypedDict, total=False):
    """Partial STAC Item."""

    type: Optional[Literal["Feature"]]
    stac_version: Optional[str]
    stac_extensions: Optional[List[str]]
    id: Optional[str]
    geometry: Optional[Dict[str, Any]]
    bbox: Optional[BBox]
    properties: Optional[Dict[str, Any]]
    links: Optional[List[Dict[str, Any]]]
    assets: Optional[Dict[str, Any]]
    collection: Optional[str]


@attr.s
class PostItem(CollectionUri):
    """Create Item."""

    item: Annotated[Union[Item, ItemCollection], Body()] = attr.ib(default=None)


@attr.s
class PatchAddReplaceTest(BaseModel):
    """Add, Replace or Test Operation."""

    path: str = attr.ib()
    op: Literal["add", "replace", "test"] = attr.ib()
    value: Any = attr.ib()


@attr.s
class PatchRemove(BaseModel):
    """Remove Operation."""

    path: str = attr.ib()
    op: Literal["remove"] = attr.ib()


@attr.s
class PatchMoveCopy(BaseModel):
    """Move or Copy Operation."""

    path: str = attr.ib()
    op: Literal["move", "copy"] = attr.ib()

    def __attrs_init__(self, *args, **kwargs):
        """Init function to add 'from' field."""
        super().__init__(*args, **kwargs)
        self.__setattr__("from", kwargs["from"])


PatchOperation = Union[PatchAddReplaceTest, PatchMoveCopy, PatchRemove]


@attr.s
class PutItem(ItemUri):
    """Update Item."""

    item: Annotated[Item, Body()] = attr.ib(default=None)


@attr.s
class PatchItem(ItemUri):
    """Patch Item."""

    patch: Annotated[
        Union[PartialItem, List[PatchOperation]],
        Body(),
    ] = attr.ib(default=None)


@attr.s
class PutCollection(CollectionUri):
    """Update Collection."""

    collection: Annotated[Collection, Body()] = attr.ib(default=None)


@attr.s
class PatchCollection(CollectionUri):
    """Patch Collection."""

    patch: Annotated[
        Union[PartialCollection, List[PatchOperation]],
        Body(),
    ] = attr.ib(default=None)
