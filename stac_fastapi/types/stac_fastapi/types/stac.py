"""STAC types."""
from typing import Any, Dict, List, Optional, TypedDict, Union

NumType = Union[float, int]


class LandingPage(TypedDict, total=False):
    """STAC Landing Page."""

    type: str
    stac_version: str
    stac_extensions: Optional[List[str]]
    id: str
    title: str
    description: str
    conformsTo: List[str]
    links: List[Dict[str, Any]]


class Conformance(TypedDict):
    """STAC Conformance Classes."""

    conformsTo: List[str]


class Catalog(TypedDict, total=False):
    """STAC Catalog."""

    type: str
    stac_version: str
    stac_extensions: Optional[List[str]]
    id: str
    title: Optional[str]
    description: str
    links: List[Dict[str, Any]]


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

    type: str
    stac_version: str
    stac_extensions: Optional[List[str]]
    id: str
    geometry: Dict[str, Any]
    bbox: List[NumType]
    properties: Dict[str, Any]
    links: List[Dict[str, Any]]
    assets: Dict[str, Any]
    collection: str


class ItemCollection(TypedDict, total=False):
    """STAC Item Collection."""

    type: str
    features: List[Item]
    links: List[Dict[str, Any]]
    context: Optional[Dict[str, int]]


class Collections(TypedDict, total=False):
    """All collections endpoint.

    https://github.com/radiantearth/stac-api-spec/tree/master/collections
    """

    collections: List[Collection]
    links: List[Dict[str, Any]]
