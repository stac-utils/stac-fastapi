"""Link helpers."""

from typing import Any, Dict, List
from urllib.parse import urljoin

import attr
from stac_pydantic.links import Relations
from stac_pydantic.shared import MimeTypes

# These can be inferred from the item/collection so they aren't included in the database
# Instead they are dynamically generated when querying the database using the
# classes defined below
INFERRED_LINK_RELS = ["self", "item", "parent", "collection", "root", "items"]


def filter_links(links: List[Dict]) -> List[Dict]:
    """Remove inferred links."""
    return [link for link in links if link["rel"] not in INFERRED_LINK_RELS]


def resolve_links(links: list, base_url: str) -> List[Dict]:
    """Convert relative links to absolute links."""
    filtered_links = filter_links(links)
    for link in filtered_links:
        link.update({"href": urljoin(base_url, link["href"])})
    return filtered_links


@attr.s
class BaseLinks:
    """Create inferred links common to collections and items."""

    collection_id: str = attr.ib()
    base_url: str = attr.ib()

    def root(self) -> Dict[str, Any]:
        """Return the catalog root."""
        return dict(rel=Relations.root, type=MimeTypes.json, href=self.base_url)


@attr.s
class CollectionLinks(BaseLinks):
    """Create inferred links specific to collections."""

    def self(self) -> Dict[str, Any]:
        """Create the `self` link."""
        return dict(
            rel=Relations.self,
            type=MimeTypes.json,
            href=urljoin(self.base_url, f"collections/{self.collection_id}"),
        )

    def parent(self) -> Dict[str, Any]:
        """Create the `parent` link."""
        return dict(rel=Relations.parent, type=MimeTypes.json, href=self.base_url)

    def items(self) -> Dict[str, Any]:
        """Create the `items` link."""
        return dict(
            rel="items",
            type=MimeTypes.geojson,
            href=urljoin(self.base_url, f"collections/{self.collection_id}/items"),
        )

    def create_links(self) -> List[Dict[str, Any]]:
        """Return all inferred links."""
        return [self.self(), self.parent(), self.items(), self.root()]


@attr.s
class ItemLinks(BaseLinks):
    """Create inferred links specific to items."""

    item_id: str = attr.ib()

    def self(self) -> Dict[str, Any]:
        """Create the `self` link."""
        return dict(
            rel=Relations.self,
            type=MimeTypes.geojson,
            href=urljoin(
                self.base_url,
                f"collections/{self.collection_id}/items/{self.item_id}",
            ),
        )

    def parent(self) -> Dict[str, Any]:
        """Create the `parent` link."""
        return dict(
            rel=Relations.parent,
            type=MimeTypes.json,
            href=urljoin(self.base_url, f"collections/{self.collection_id}"),
        )

    def collection(self) -> Dict[str, Any]:
        """Create the `collection` link."""
        return dict(
            rel=Relations.collection,
            type=MimeTypes.json,
            href=urljoin(self.base_url, f"collections/{self.collection_id}"),
        )

    def create_links(self) -> List[Dict[str, Any]]:
        """Return all inferred links."""
        links = [
            self.self(),
            self.parent(),
            self.collection(),
            self.root(),
        ]
        return links
