"""STAC types."""

from typing import Any, Dict, List, Literal, Optional, Union

import attr
from stac_pydantic.shared import BBox
from typing_extensions import TypedDict

NumType = Union[float, int]


class Catalog(TypedDict, total=False):
    """STAC Catalog."""

    type: str
    stac_version: str
    stac_extensions: Optional[List[str]]
    id: str
    title: Optional[str]
    description: str
    links: List[Dict[str, Any]]


class LandingPage(Catalog, total=False):
    """STAC Landing Page."""

    conformsTo: List[str]


class Conformance(TypedDict):
    """STAC Conformance Classes."""

    conformsTo: List[str]


class Collection(Catalog, total=False):
    """STAC Collection."""

    keywords: List[str]
    license: str
    providers: List[Dict[str, Any]]
    extent: Dict[str, Any]
    summaries: Dict[str, Any]
    assets: Dict[str, Any]


class Item(TypedDict, total=False):
    """STAC Item."""

    type: Literal["Feature"]
    stac_version: str
    stac_extensions: Optional[List[str]]
    id: str
    geometry: Dict[str, Any]
    bbox: BBox
    properties: Dict[str, Any]
    links: List[Dict[str, Any]]
    assets: Dict[str, Any]
    collection: str


class ItemCollection(TypedDict, total=False):
    """STAC Item Collection."""

    type: Literal["FeatureCollection"]
    features: List[Item]
    links: List[Dict[str, Any]]
    context: Optional[Dict[str, int]]


class Collections(TypedDict, total=False):
    """All collections endpoint.
    https://github.com/radiantearth/stac-api-spec/tree/master/collections
    """

    collections: List[Collection]
    links: List[Dict[str, Any]]


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
class PatchAddReplaceTest:
    """Add, Replace or Test Operation."""

    path: str = attr.ib()
    op: Literal["add", "replace", "test"] = attr.ib()
    value: Any = attr.ib()


@attr.s
class PatchRemove:
    """Remove Operation."""

    path: str = attr.ib()
    op: Literal["remove"] = attr.ib()


@attr.s
class PatchMoveCopy:
    """Move or Copy Operation."""

    path: str = attr.ib()
    op: Literal["move", "copy"] = attr.ib()

    def __attrs_init__(self, *args, **kwargs):
        """Init function to add 'from' field."""
        super().__init__(*args, **kwargs)
        self.__setattr__("from", kwargs["from"])


PatchOperation = Union[PatchAddReplaceTest, PatchMoveCopy, PatchRemove]
