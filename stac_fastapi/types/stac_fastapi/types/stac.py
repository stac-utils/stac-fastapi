"""STAC types."""

from typing import Any, Literal, NotRequired, TypedDict

from stac_pydantic.shared import BBox

NumType = float | int


class Catalog(TypedDict):
    """STAC Catalog."""

    type: str
    stac_version: str
    stac_extensions: NotRequired[list[str]]
    id: str
    title: NotRequired[str]
    description: str
    links: list[dict[str, Any]]


class LandingPage(Catalog):
    """STAC Landing Page."""

    conformsTo: list[str]


class Conformance(TypedDict):
    """STAC Conformance Classes."""

    conformsTo: list[str]


class Collection(Catalog):
    """STAC Collection."""

    keywords: list[str]
    license: str
    providers: list[dict[str, Any]]
    extent: dict[str, Any]
    summaries: dict[str, Any]
    assets: dict[str, Any]


class Item(TypedDict):
    """STAC Item."""

    type: Literal["Feature"]
    stac_version: str
    stac_extensions: NotRequired[list[str]]
    id: str
    geometry: dict[str, Any]
    bbox: BBox
    properties: dict[str, Any]
    links: list[dict[str, Any]]
    assets: dict[str, Any]
    collection: str


class ItemCollection(TypedDict):
    """STAC Item Collection."""

    type: Literal["FeatureCollection"]
    features: list[Item]
    links: list[dict[str, Any]]
    numberMatched: NotRequired[int]
    numberReturned: NotRequired[int]


class Collections(TypedDict):
    """All collections endpoint.
    https://github.com/radiantearth/stac-api-spec/tree/master/collections
    """

    collections: list[Collection]
    links: list[dict[str, Any]]
    numberMatched: NotRequired[int]
    numberReturned: NotRequired[int]
