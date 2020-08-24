"""link helpers."""

from dataclasses import dataclass
from typing import Dict, List
from urllib.parse import urljoin

from stac_api.models.ogc import OGCTileLink
from stac_pydantic.shared import Link, MimeTypes, Relations

# These can be inferred from the item/collection so they aren't included in the database
# Instead they are dynamically generated when querying the database using the classes defined below
INFERRED_LINK_RELS = ["self", "item", "parent", "collection", "root"]


def filter_links(links: List[Dict]) -> List[Dict]:
    """Remove inferred links"""
    return [link for link in links if link["rel"] not in INFERRED_LINK_RELS]


@dataclass
class BaseLinks:
    """Create inferred links common to collections and items"""

    collection_id: str
    base_url: str

    def root(self) -> Link:
        """Return the catalog root"""
        return Link(
            rel=Relations.root, type=MimeTypes.json, href=urljoin(self.base_url, "/")
        )


@dataclass
class CollectionLinks(BaseLinks):
    """Create inferred links specific to collections"""

    def self(self) -> Link:
        """Create the `self` link."""
        return Link(
            rel=Relations.self,
            type=MimeTypes.json,
            href=urljoin(self.base_url, f"/collections/{self.collection_id}"),
        )

    def parent(self) -> Link:
        """Create the `parent` link."""
        return Link(
            rel=Relations.parent, type=MimeTypes.json, href=urljoin(self.base_url, "/")
        )

    def item(self) -> Link:
        """Create the `item` link."""
        return Link(
            rel=Relations.item,
            type=MimeTypes.geojson,
            href=urljoin(self.base_url, f"/collections/{self.collection_id}/items"),
        )

    def create_links(self) -> List[Link]:
        """Convenience method to return all inferred links"""
        return [self.self(), self.parent(), self.item(), self.root()]


@dataclass
class ItemLinks(BaseLinks):
    """Create inferred links specific to items"""

    item_id: str

    def self(self) -> Link:
        """Create the `self` link."""
        return Link(
            rel=Relations.self,
            type=MimeTypes.geojson,
            href=urljoin(
                self.base_url, f"/collections/{self.collection_id}/items/{self.item_id}"
            ),
        )

    def parent(self) -> Link:
        """Create the `parent` link."""
        return Link(
            rel=Relations.parent,
            type=MimeTypes.json,
            href=urljoin(self.base_url, f"/collections/{self.collection_id}"),
        )

    def collection(self) -> Link:
        """Create the `collection` link."""
        return Link(
            rel=Relations.collection,
            type=MimeTypes.json,
            href=urljoin(self.base_url, f"/collections/{self.collection_id}"),
        )

    def create_links(self) -> List[Link]:
        """Convenience method to return all inferred links"""
        return [
            self.self(),
            self.parent(),
            self.collection(),
            self.root(),
        ]


@dataclass
class TileLinks:
    """Create inferred links specific to OGC Tiles API"""

    base_url: str
    collection_id: str
    item_id: str

    def __post_init__(self):
        """post init"""
        self.item_uri = urljoin(self.base_url, f"{self.collection_id}/{self.item_id}")

    def tiles(self) -> OGCTileLink:
        """Create tiles link"""
        return OGCTileLink(
            href=urljoin(
                self.base_url, f"/tiles/{{z}}/{{x}}/{{y}}.png?url={self.item_uri}",
            ),
            rel=Relations.item,
            title="Tile layer",
            type=MimeTypes.png,
            templated=True,
        )

    def viewer(self) -> OGCTileLink:
        """Create viewer link"""
        return OGCTileLink(
            href=urljoin(self.base_url, f"/stac/viewer?url={self.item_uri}"),
            rel=Relations.alternate,
            type=MimeTypes.html,
        )

    def tilejson(self) -> OGCTileLink:
        """Create tilejson link"""
        return OGCTileLink(
            href=urljoin(self.base_url, f"/tilejson.json?url={self.item_uri}"),
            rel=Relations.alternate,
            type=MimeTypes.json,
        )

    def create_links(self) -> List[OGCTileLink]:
        """Convenience method to return all inferred links"""
        return [self.tiles(), self.tilejson(), self.viewer()]
