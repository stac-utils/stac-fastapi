"""link helpers."""

from typing import Any, Dict, List, Optional
from urllib.parse import ParseResult, parse_qs, unquote, urlencode, urljoin, urlparse

import attr
from stac_pydantic.links import Relations
from stac_pydantic.shared import MimeTypes
from starlette.requests import Request

# These can be inferred from the item/collection so they aren't included in the database
# Instead they are dynamically generated when querying the database using the classes defined below
INFERRED_LINK_RELS = ["self", "item", "parent", "collection", "root"]


def filter_links(links: List[Dict]) -> List[Dict]:
    """Remove inferred links."""
    return [link for link in links if link["rel"] not in INFERRED_LINK_RELS]


def merge_params(url: str, newparams: Dict) -> str:
    """Merge url parameters."""
    u = urlparse(url)
    params = parse_qs(u.query)
    params.update(newparams)
    param_string = unquote(urlencode(params, True))

    href = ParseResult(
        scheme=u.scheme,
        netloc=u.netloc,
        path=u.path,
        params=u.params,
        query=param_string,
        fragment=u.fragment,
    ).geturl()
    return href


@attr.s
class BaseLinks:
    """Create inferred links common to collections and items."""

    request: Request = attr.ib()

    @property
    def base_url(self):
        """Get the base url."""
        return str(self.request.base_url)

    @property
    def url(self):
        """Get the current request url."""
        return str(self.request.url)

    def resolve(self, url):
        """Resolve url to the current request url."""
        return urljoin(str(self.base_url), str(url))

    def link_self(self) -> Dict:
        """Return the self link."""
        return dict(rel=Relations.self.value, type=MimeTypes.json.value, href=self.url)

    def link_root(self) -> Dict:
        """Return the catalog root."""
        return dict(
            rel=Relations.root.value, type=MimeTypes.json.value, href=self.base_url
        )

    def create_links(self) -> List[Dict]:
        """Return all inferred links."""
        links = []
        for name in dir(self):
            if name.startswith("link_") and callable(getattr(self, name)):
                link = getattr(self, name)()
                if link is not None:
                    links.append(link)
        return links

    async def get_links(
        self, extra_links: List[Dict[str, Any]] = []
    ) -> List[Dict[str, Any]]:
        """
        Generate all the links.

        Get the links object for a stac resource by iterating through
        available methods on this class that start with link_.
        """
        # TODO: Pass request.json() into function so this doesn't need to be coroutine
        if self.request.method == "POST":
            self.request.postbody = await self.request.json()
        # join passed in links with generated links
        # and update relative paths
        links = self.create_links()
        if extra_links is not None and len(extra_links) >= 1:
            for link in extra_links:
                if link["rel"] not in INFERRED_LINK_RELS:
                    link["href"] = self.resolve(link["href"])
                    links.append(link)
        return links


@attr.s
class PagingLinks(BaseLinks):
    """Create links for paging."""

    next: Optional[str] = attr.ib(kw_only=True, default=None)
    prev: Optional[str] = attr.ib(kw_only=True, default=None)

    def link_next(self) -> Optional[Dict[str, Any]]:
        """Create link for next page."""
        if self.next is not None:
            method = self.request.method
            if method == "GET":
                href = merge_params(self.url, {"token": f"next:{self.next}"})
                link = dict(
                    rel=Relations.next.value,
                    type=MimeTypes.json.value,
                    method=method,
                    href=href,
                )
                return link
            if method == "POST":
                return {
                    "rel": Relations.next,
                    "type": MimeTypes.json,
                    "method": method,
                    "href": f"{self.request.url}",
                    "body": {**self.request.postbody, "token": f"next:{self.next}"},
                }

        return None

    def link_prev(self) -> Optional[Dict[str, Any]]:
        """Create link for previous page."""
        if self.prev is not None:
            method = self.request.method
            if method == "GET":
                href = merge_params(self.url, {"token": f"prev:{self.prev}"})
                return dict(
                    rel=Relations.previous.value,
                    type=MimeTypes.json.value,
                    method=method,
                    href=href,
                )
            if method == "POST":
                return {
                    "rel": Relations.previous,
                    "type": MimeTypes.json,
                    "method": method,
                    "href": f"{self.request.url}",
                    "body": {**self.request.postbody, "token": f"prev:{self.prev}"},
                }
        return None


@attr.s
class CollectionLinksBase(BaseLinks):
    """Create inferred links specific to collections."""

    collection_id: str = attr.ib()

    def collection_link(self, rel: str = Relations.collection.value) -> Dict:
        """Create a link to a collection."""
        return dict(
            rel=rel,
            type=MimeTypes.json.value,
            href=self.resolve(f"/collections/{self.collection_id}"),
        )


@attr.s
class CollectionLinks(CollectionLinksBase):
    """Create inferred links specific to collections."""

    def link_self(self) -> Dict:
        """Return the self link."""
        return self.collection_link(rel=Relations.self.value)

    def link_parent(self) -> Dict:
        """Create the `parent` link."""
        return dict(
            rel=Relations.parent.value,
            type=MimeTypes.json.value,
            href=self.base_url,
        )

    def link_items(self) -> Dict:
        """Create the `item` link."""
        return dict(
            rel="items",
            type=MimeTypes.geojson.value,
            href=self.resolve(f"/collections/{self.collection_id}/items"),
        )


@attr.s
class ItemLinks(CollectionLinksBase):
    """Create inferred links specific to items."""

    item_id: str = attr.ib()

    def link_self(self) -> Dict:
        """Create the self link."""
        return dict(
            rel=Relations.self.value,
            type=MimeTypes.geojson.value,
            href=self.resolve(
                f"/collections/{self.collection_id}/items/{self.item_id}"
            ),
        )

    def link_parent(self) -> Dict:
        """Create the `parent` link."""
        return self.collection_link(rel=Relations.parent.value)

    def link_collection(self) -> Dict:
        """Create the `collection` link."""
        return self.collection_link()

    def link_tiles(self) -> Dict:
        """Create the `tiles` link."""
        return dict(
            rel=Relations.alternate.value,
            type=MimeTypes.json.value,
            title="tiles",
            href=self.resolve(
                f"/collections/{self.collection_id}/items/{self.item_id}/tiles",
            ),
        )


@attr.s
class TileLinks:
    """Create inferred links specific to OGC Tiles API."""

    base_url: str = attr.ib()
    collection_id: str = attr.ib()
    item_id: str = attr.ib()

    def __post_init__(self):
        """Post init handler."""
        self.item_uri = urljoin(
            self.base_url,
            f"/collections/{self.collection_id}/items/{self.item_id}",
        )

    def link_tiles(self) -> Dict:
        """Create tiles link."""
        return dict(
            href=urljoin(
                self.base_url,
                f"/titiler/tiles/{{z}}/{{x}}/{{y}}.png?url={self.item_uri}",
            ),
            rel=Relations.item.value,
            title="tiles",
            type=MimeTypes.png.value,
            templated=True,
        )

    def link_viewer(self) -> Dict:
        """Create viewer link."""
        return dict(
            href=urljoin(self.base_url, f"/titiler/viewer?url={self.item_uri}"),
            rel=Relations.alternate.value,
            type=MimeTypes.html.value,
            title="viewer",
        )

    def link_tilejson(self) -> Dict:
        """Create tilejson link."""
        return dict(
            href=urljoin(self.base_url, f"/titiler/tilejson.json?url={self.item_uri}"),
            rel=Relations.alternate.value,
            type=MimeTypes.json.value,
            title="tilejson",
        )

    def link_wmts(self) -> Dict:
        """Create wmts capabilities link."""
        return dict(
            href=urljoin(
                self.base_url,
                f"/titiler/WMTSCapabilities.xml?url={self.item_uri}",
            ),
            rel=Relations.alternate.value,
            type=MimeTypes.xml.value,
            title="WMTS Capabilities",
        )
