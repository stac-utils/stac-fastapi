"""link helpers."""

from typing import Dict, List
from urllib.parse import urljoin

import attr
from stac_pydantic.shared import Link, MimeTypes, Relations

from stac_api.models.ogc import OGCTileLink

# These can be inferred from the item/collection so they aren't included in the database
# Instead they are dynamically generated when querying the database using the classes defined below
INFERRED_LINK_RELS = ["self", "item", "parent", "collection", "root"]


def filter_links(links: List[Dict]) -> List[Dict]:
    """Remove inferred links"""
    return [link for link in links if link["rel"] not in INFERRED_LINK_RELS]


@attr.s
class BaseLinks:
    """Create inferred links common to collections and items"""

    collection_id: str = attr.ib()
    base_url: str = attr.ib()

    def root(self) -> Link:
        """Return the catalog root"""
        return Link(
            rel=Relations.root, type=MimeTypes.json, href=urljoin(self.base_url, "/")
        )


@attr.s
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


@attr.s
class ItemLinks(BaseLinks):
    """Create inferred links specific to items"""

    item_id: str = attr.ib()

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

    def tiles(self) -> Link:
        """Create the `tiles` link"""
        return Link(
            rel=Relations.alternate,
            type=MimeTypes.json,
            title="tiles",
            href=urljoin(
                self.base_url,
                f"/collections/{self.collection_id}/items/{self.item_id}/tiles",
            ),
        )

    def create_links(self) -> List[Link]:
        """Convenience method to return all inferred links"""
        links = [
            self.self(),
            self.parent(),
            self.collection(),
            self.root(),
        ]
        # if config.settings.add_on_is_enabled(config.AddOns.tiles):
        # TODO: Don't always append tiles link
        links.append(self.tiles())
        return links


@attr.s
class TileLinks:
    """Create inferred links specific to OGC Tiles API"""

    base_url: str = attr.ib()
    collection_id: str = attr.ib()
    item_id: str = attr.ib()

    def __post_init__(self):
        """post init"""
        self.item_uri = urljoin(
            self.base_url, f"/collections/{self.collection_id}/items/{self.item_id}"
        )

    def tiles(self) -> OGCTileLink:
        """Create tiles link"""
        return OGCTileLink(
            href=urljoin(
                self.base_url,
                f"/titiler/tiles/{{z}}/{{x}}/{{y}}.png?url={self.item_uri}",
            ),
            rel=Relations.item,
            title="tiles",
            type=MimeTypes.png,
            templated=True,
        )

    def viewer(self) -> OGCTileLink:
        """Create viewer link"""
        return OGCTileLink(
            href=urljoin(self.base_url, f"/titiler/viewer?url={self.item_uri}"),
            rel=Relations.alternate,
            type=MimeTypes.html,
            title="viewer",
        )

    def tilejson(self) -> OGCTileLink:
        """Create tilejson link"""
        return OGCTileLink(
            href=urljoin(self.base_url, f"/titiler/tilejson.json?url={self.item_uri}"),
            rel=Relations.alternate,
            type=MimeTypes.json,
            title="tilejson",
        )

    def wmts(self) -> OGCTileLink:
        """Create wmts capabilities link"""
        return OGCTileLink(
            href=urljoin(
                self.base_url, f"/titiler/WMTSCapabilities.xml?url={self.item_uri}"
            ),
            rel=Relations.alternate,
            type=MimeTypes.xml,
            title="WMTS Capabilities",
        )

    def create_links(self) -> List[OGCTileLink]:
        """Convenience method to return all inferred links"""
        return [self.tiles(), self.tilejson(), self.wmts(), self.viewer()]
