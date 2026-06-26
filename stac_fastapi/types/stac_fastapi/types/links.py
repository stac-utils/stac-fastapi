"""Link helpers."""

from typing import Any
from urllib.parse import urljoin, urlsplit

import attr
from stac_pydantic.links import Relations
from stac_pydantic.shared import MimeTypes

# These can be inferred from the item/collection so they aren't included in the database
# Instead they are dynamically generated when querying the database using the
# classes defined below
INFERRED_LINK_RELS = ["self", "item", "parent", "collection", "root", "items"]


def filter_links(links: list[dict]) -> list[dict]:
    """Remove inferred links."""
    return [link for link in links if link["rel"] not in INFERRED_LINK_RELS]


def resolve_links(links: list, base_url: str) -> list[dict]:
    """Convert relative links to absolute links while preserving existing absolute URLs.

    This function processes links and applies the base_url and proxy path to relative URLs
    However, it explicitly preserves absolute URLs (starting with http:// or https://) to
    prevent mangling of external links stored in STAC items (e.g., license URLs, external
    documentation links).
    """
    filtered_links = filter_links(links)
    path = urlsplit(base_url).path.rstrip("/")
    for link in filtered_links:
        href = str(link.get("href", ""))

        # Do not mangle URLs that are already absolute
        if href.startswith(("http://", "https://")):
            continue

        # Remove leading slash to prevent urljoin from replacing the entire path
        href = href.lstrip("/")
        # Construct the full path with proxy path preserved
        full_path = f"{path}/{href}" if path else href
        link.update({"href": urljoin(base_url, full_path)})
    return filtered_links


@attr.s
class BaseLinks:
    """Create inferred links common to collections and items."""

    collection_id: str = attr.ib()
    base_url: str = attr.ib()

    def root(self) -> dict[str, Any]:
        """Return the catalog root."""
        return dict(rel=Relations.root, type=MimeTypes.json, href=self.base_url)


@attr.s
class CollectionLinks(BaseLinks):
    """Create inferred links specific to collections."""

    def self(self) -> dict[str, Any]:
        """Create the `self` link."""
        path = urlsplit(self.base_url).path.rstrip("/")
        return dict(
            rel=Relations.self,
            type=MimeTypes.json,
            href=urljoin(self.base_url, f"{path}/collections/{self.collection_id}"),
        )

    def parent(self) -> dict[str, Any]:
        """Create the `parent` link."""
        return dict(rel=Relations.parent, type=MimeTypes.json, href=self.base_url)

    def items(self) -> dict[str, Any]:
        """Create the `items` link."""
        path = urlsplit(self.base_url).path.rstrip("/")
        return dict(
            rel="items",
            type=MimeTypes.geojson,
            href=urljoin(self.base_url, f"{path}/collections/{self.collection_id}/items"),
        )

    def create_links(self) -> list[dict[str, Any]]:
        """Return all inferred links."""
        return [self.self(), self.parent(), self.items(), self.root()]


@attr.s
class ItemLinks(BaseLinks):
    """Create inferred links specific to items."""

    item_id: str = attr.ib()

    def self(self) -> dict[str, Any]:
        """Create the `self` link."""
        path = urlsplit(self.base_url).path.rstrip("/")
        return dict(
            rel=Relations.self,
            type=MimeTypes.geojson,
            href=urljoin(
                self.base_url,
                f"{path}/collections/{self.collection_id}/items/{self.item_id}",
            ),
        )

    def parent(self) -> dict[str, Any]:
        """Create the `parent` link."""
        path = urlsplit(self.base_url).path.rstrip("/")
        return dict(
            rel=Relations.parent,
            type=MimeTypes.json,
            href=urljoin(self.base_url, f"{path}/collections/{self.collection_id}"),
        )

    def collection(self) -> dict[str, Any]:
        """Create the `collection` link."""
        path = urlsplit(self.base_url).path.rstrip("/")
        return dict(
            rel=Relations.collection,
            type=MimeTypes.json,
            href=urljoin(self.base_url, f"{path}/collections/{self.collection_id}"),
        )

    def create_links(self) -> list[dict[str, Any]]:
        """Return all inferred links."""
        links = [
            self.self(),
            self.parent(),
            self.collection(),
            self.root(),
        ]
        return links
