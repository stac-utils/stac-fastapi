"""STAC types."""

from typing import Any, Dict, List, Literal, Union

from stac_pydantic.shared import BBox
from typing_extensions import NotRequired, TypedDict

NumType = Union[float, int]


class Catalog(TypedDict):
    """STAC Catalog."""

    type: str
    stac_version: str
    stac_extensions: NotRequired[List[str]]
    id: str
    title: NotRequired[str]
    description: str
    links: List[Dict[str, Any]]


class LandingPage(Catalog):
    """STAC Landing Page."""

    conformsTo: List[str]


class Conformance(TypedDict):
    """STAC Conformance Classes."""

    conformsTo: List[str]


class Collection(Catalog):
    """STAC Collection."""

    keywords: List[str]
    license: str
    providers: List[Dict[str, Any]]
    extent: Dict[str, Any]
    summaries: Dict[str, Any]
    assets: Dict[str, Any]


class Item(TypedDict):
    """STAC Item."""

    type: Literal["Feature"]
    stac_version: str
    stac_extensions: NotRequired[List[str]]
    id: str
    geometry: Dict[str, Any]
    bbox: BBox
    properties: Dict[str, Any]
    links: List[Dict[str, Any]]
    assets: Dict[str, Any]
    collection: str


class ItemCollection(TypedDict):
    """STAC Item Collection."""

    type: Literal["FeatureCollection"]
    features: List[Item]
    links: List[Dict[str, Any]]
    numberMatched: NotRequired[int]
    numberReturned: NotRequired[int]


class Collections(TypedDict):
    """All collections endpoint.
    https://github.com/radiantearth/stac-api-spec/tree/master/collections
    """

    collections: List[Collection]
    links: List[Dict[str, Any]]
    numberMatched: NotRequired[int]
    numberReturned: NotRequired[int]
