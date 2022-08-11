"""link helpers."""

from typing import Any, Dict, List, Optional
from urllib.parse import urljoin

import attr
from stac_pydantic.links import Relations
from stac_pydantic.shared import MimeTypes

# These can be inferred from the item/collection so they aren't included in the database
# Instead they are dynamically generated when querying the database using the classes defined below
INFERRED_LINK_RELS = ["self", "item", "parent", "collection", "root"]


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

    def resolve(self, url):
        """Resolve url to the current request url."""
        return urljoin(str(self.base_url), str(url))


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

    def get_links(
        self, extra_links: Optional[List[Dict[str, Any]]] = None
    ) -> List[Dict[str, Any]]:
        """
        Generate all the links.

        Get the links object for a stac resource by iterating through
        available methods on this class that start with link_.
        """
        # join passed in links with generated links
        # and update relative paths
        links = self.create_links()

        if extra_links:
            # For extra links passed in,
            # add links modified with a resolved href.
            # Drop any links that are dynamically
            # determined by the server (e.g. self, parent, etc.)
            # Resolving the href allows for relative paths
            # to be stored in pgstac and for the hrefs in the
            # links of response STAC objects to be resolved
            # to the request url.
            links += [
                {**link, "href": self.resolve(link["href"])}
                for link in extra_links
                if link["rel"] not in INFERRED_LINK_RELS
            ]

        return links


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
