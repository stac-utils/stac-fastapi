from typing import Any, Dict, List, Optional, TypedDict, Union

NumType = Union[float, int]


class LandingPage(TypedDict):
    stac_version: str
    id: str
    title: str
    description: str
    conformsTo: List[str]
    links: List[Dict[str, Any]]


class Conformance(TypedDict):
    conformsTo: List[str]


class Catalog(TypedDict):
    type: str
    stac_version: str
    stac_extensions: Optional[List[str]]
    id: str
    title: Optional[str]
    description: str
    links: List[Dict[str, Any]]


class Collection(Catalog):
    keywords: List[str]
    license: str
    providers: List[Dict[str, Any]]
    extent: Dict[str, Any]
    summaries: Dict[str, Any]
    assets: Dict[str, Any]


class Item(TypedDict):
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
    stac_version: str
    stac_extensions: Optional[List[str]]
    type: str
    features: List[Item]
    links: List[Dict[str, Any]]
