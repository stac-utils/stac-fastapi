from dataclasses import dataclass
from typing import List, Dict
from urllib.parse import urljoin

from stac_pydantic.shared import Link, MimeTypes, Relations


# These can be inferred from the item/collection so they aren't included in the database
# Instead they are dynamically generated when querying the database using the classes defined below
INFERRED_LINK_RELS = ["self", "item", "parent", "collection", "root"]


def filter_links(links: List[Dict]) -> List[Dict]:
    """Remove inferred links"""
    return [l for l in links if l["rel"] not in INFERRED_LINK_RELS]


@dataclass
class BaseLinks:
    """Create inferred links common to collections and items"""

    collection_id: str
    base_url: str

    def root(self) -> Link:
        return Link(
            rel=Relations.root, type=MimeTypes.json, href=urljoin(self.base_url, "/")
        )


@dataclass
class CollectionLinks(BaseLinks):
    """Create inferred links specific to collections"""

    def self(self) -> Link:
        return Link(
            rel=Relations.self,
            type=MimeTypes.json,
            href=urljoin(self.base_url, f"/collections/{self.collection_id}"),
        )

    def parent(self) -> Link:
        return Link(
            rel=Relations.parent, type=MimeTypes.json, href=urljoin(self.base_url, "/")
        )

    def item(self) -> Link:
        return Link(
            rel=Relations.item,
            type=MimeTypes.geojson,
            href=urljoin(self.base_url, f"/collections/{self.collection_id}/items"),
        )

    def tiles(self) -> Link:
        return Link(
            rel=Relations.tiles,
            type=MimeTypes.json,
            href=urljoin(self.base_url, f"/collections/{self.collection_id}/tiles"),
        )

    def create_links(self) -> List[Link]:
        return [self.self(), self.parent(), self.item(), self.root(), self.tiles()]


@dataclass
class ItemLinks(BaseLinks):
    """Create inferred links specific to items"""

    item_id: str

    def self(self) -> Link:
        return Link(
            rel=Relations.self,
            type=MimeTypes.geojson,
            href=urljoin(
                self.base_url, f"/collections/{self.collection_id}/items/{self.item_id}"
            ),
        )

    def parent(self) -> Link:
        return Link(
            rel=Relations.parent,
            type=MimeTypes.json,
            href=urljoin(self.base_url, f"/collections/{self.collection_id}"),
        )

    def collection(self) -> Link:
        return Link(
            rel=Relations.collection,
            type=MimeTypes.json,
            href=urljoin(self.base_url, f"/collections/{self.collection_id}"),
        )

    def tiles(self) -> Link:
        return Link(
            rel=Relations.tiles,
            type=MimeTypes.json,
            href=urljoin(
                self.base_url,
                f"/collections/{self.collection_id}/items/{self.item_id}/tiles",
            ),
        )

    def create_links(self) -> List[Link]:
        return [
            self.self(),
            self.parent(),
            self.collection(),
            self.root(),
            self.tiles(),
        ]
