"""Transaction extension types."""

from typing import Any, Literal, Union

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
class PutPatchItem(ItemUri):
    """Update Item."""

    item: Annotated[Item, Body()] = attr.ib(default=None)


@attr.s
class PatchOperation(BaseModel):
    """Update Operation."""

    path: str = attr.ib()


@attr.s
class PatchAddReplaceTest(PatchOperation):
    """Add, Replace or Test Operation."""

    op: Literal["add", "replace", "test"] = attr.ib()
    value: Any = attr.ib()


@attr.s
class PatchRemove(PatchOperation):
    """Remove Operation."""

    op: Literal["remove"] = attr.ib()


@attr.s
class PatchMoveCopy(PatchOperation):
    """Move or Copy Operation."""

    op: Literal["move", "copy"] = attr.ib()

    def __init__(self, *args, **kwargs):
        """Init function to add 'from' field."""
        super().__init__(*args, **kwargs)
        self.__setattr__("from", kwargs["from"])


@attr.s
class PutPatchCollection(CollectionUri):
    """Update Collection."""

    collection: Annotated[Collection, Body()] = attr.ib(default=None)
