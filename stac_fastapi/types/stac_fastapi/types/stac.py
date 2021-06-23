"""STAC types."""
from typing import Any, Dict, List, Optional, TypedDict, Union

NumType = Union[float, int]


class LandingPage(TypedDict):
    """STAC Landing Page."""

    stac_version: str
    stac_extensions: Optional[List[str]]
    id: str
    title: str
    description: str
    # TODO: Implement conformance classes in landing page (https://github.com/stac-utils/stac-fastapi/issues/159)
    # conformsTo: List[str]
    links: List[Dict[str, Any]]


class Conformance(TypedDict):
    """STAC Conformance Classes."""

    conformsTo: List[str]


class Catalog(TypedDict):
    """STAC Catalog."""

    type: str
    stac_version: str
    stac_extensions: Optional[List[str]]
    id: str
    title: Optional[str]
    description: str
    links: List[Dict[str, Any]]


class Collection(Catalog):
    """STAC Collection."""

    keywords: List[str]
    license: str
    providers: List[Dict[str, Any]]
    extent: Dict[str, Any]
    summaries: Dict[str, Any]
    # TODO: Support collection-level assets
    # assets: Dict[str, Any]


class Item(TypedDict):
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


class ItemCollection(TypedDict):
    """STAC Item Collection."""

    stac_version: str
    stac_extensions: Optional[List[str]]
    type: str
    features: List[Item]
    links: List[Dict[str, Any]]
