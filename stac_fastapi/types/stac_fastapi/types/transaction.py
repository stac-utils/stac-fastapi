"""Transaction extension types."""

from typing import Any, List, Literal, NewType, Union

import attr
from fastapi import Body
from pydantic import BaseModel
from stac_pydantic import Collection, Item, ItemCollection
from typing_extensions import Annotated

from stac_fastapi.api.models import CollectionUri, ItemUri


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
        Union[Item, List[PatchOperation]],
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
        Union[Collection, List[PatchOperation]],
        Body(),
    ] = attr.ib(default=None)
