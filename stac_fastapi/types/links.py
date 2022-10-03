"""link helpers."""
from typing import Dict, List
from urllib.parse import urljoin, urlparse

from stac_pydantic.links import Relations
from stac_pydantic.shared import MimeTypes
from starlette.requests import Request


def get_base_url(request: Request) -> str:
    """Get base URL with respect of APIRouter prefix."""
    app = request.app
    if not app.state.router_prefix:
        return str(request.base_url)
    else:
        return "{}{}/".format(
            str(request.base_url), app.state.router_prefix.lstrip("/")
        )


def resolve_relative_links(links: List[Dict], base_url: str) -> List[Dict]:
    """Resolve relative links while skipping absolute links."""
    resolved_links = []
    for link in links:
        # Skip absolute links
        if urlparse(link["href"]).scheme:
            resolved_links.append(link)
        else:
            resolved_links.append({**link, "href": urljoin(base_url, link["href"])})
    return resolved_links


def create_root_link(request: Request):
    """Create link to API root."""
    return dict(rel=Relations.root, type=MimeTypes.json, href="/")


def hydrate_collection_links(request: Request, stac_object: Dict) -> Dict:
    """Hydrate collection with inferred links."""
    # Create inferred links
    links = [
        create_root_link(request),
        dict(rel=Relations.parent, type=MimeTypes.json, href="/"),
        dict(
            rel=Relations.self,
            type=MimeTypes.json,
            href=f"collections/{stac_object['id']}",
        ),
        dict(
            rel="items",
            type=MimeTypes.geojson,
            href=f"collections/{stac_object['id']}/items",
        ),
    ]
    inferred_link_rels = set([link["rel"] for link in links])

    # Combine with links from the stac object
    for link in stac_object["links"]:
        if link["rel"] not in inferred_link_rels:
            links.append(link)

    base_url = get_base_url(request)
    stac_object["links"] = resolve_relative_links(links, base_url)
    return stac_object


def hydrate_catalog_links(request: Request, stac_object: Dict) -> Dict:
    """Hydrate catalog with inferred links."""
    links = [
        create_root_link(request),
        {
            "rel": "service-desc",
            "type": "application/vnd.oai.openapi+json;version=3.0",
            "title": "OpenAPI service description",
            "href": request.app.openapi_url.lstrip("/"),
        },
        {
            "rel": "service-doc",
            "type": "text/html",
            "title": "OpenAPI service documentation",
            "href": request.app.docs_url.lstrip("/"),
        },
    ]

    inferred_link_rels = set([link["rel"] for link in links])

    # Combine with links from the stac object
    for link in stac_object["links"]:
        if link["rel"] not in inferred_link_rels:
            links.append(link)

    base_url = get_base_url(request)
    stac_object["links"] = resolve_relative_links(links, base_url)

    return stac_object


def hydrate_collections_links(request: Request, stac_object: Dict) -> Dict:
    """Hydrate collections with inferred links."""
    stac_object["collections"] = [
        hydrate_collection_links(request, collection)
        for collection in stac_object["collections"]
    ]

    links = [
        create_root_link(request),
        {
            "rel": Relations.parent.value,
            "type": MimeTypes.json,
            "href": "/",
        },
        {
            "rel": Relations.self.value,
            "type": MimeTypes.json,
            "href": "/collections",
        },
    ]
    inferred_link_rels = set([link["rel"] for link in links])

    # Combine with links from the stac object
    for link in stac_object["links"]:
        if link["rel"] not in inferred_link_rels:
            links.append(link)

    base_url = get_base_url(request)
    stac_object["links"] = resolve_relative_links(links, base_url)

    return stac_object


def hydrate_item_links(request: Request, stac_object: Dict) -> Dict:
    """Hydrate item with inferred links."""
    links = [
        create_root_link(request),
        {
            "rel": Relations.self,
            "type": MimeTypes.geojson,
            "href": f"/collections/{stac_object['collection']}/items/{stac_object['id']}",
        },
        {
            "rel": Relations.parent,
            "type": MimeTypes.json,
            "href": f"/collections/{stac_object['collection']}",
        },
        {
            "rel": Relations.collection,
            "type": MimeTypes.json,
            "href": f"/collections/{stac_object['collection']}",
        },
    ]

    inferred_link_rels = set([link["rel"] for link in links])

    # Combine with links from the stac object
    for link in stac_object["links"]:
        if link["rel"] not in inferred_link_rels:
            links.append(link)

    base_url = get_base_url(request)
    stac_object["links"] = resolve_relative_links(links, base_url)

    return stac_object


def hydrate_item_collection_links(request: Request, stac_object: Dict) -> Dict:
    """Hydrate item collection with inferred links."""
    stac_object["features"] = [
        hydrate_item_links(request, item) for item in stac_object["features"]
    ]

    # Item collections are returned by both `/items` and `/search` endpoints.
    if request.url.path.endswith("/items"):
        _, _, collection_name, _ = request.url.path.split("/")
        links = [
            create_root_link(request),
            {
                "rel": Relations.self,
                "type": MimeTypes.geojson,
                "href": f"/collections/{collection_name}/items",
            },
            {
                "rel": Relations.parent,
                "type": MimeTypes.json,
                "href": f"/collections/{collection_name}",
            },
        ]
    elif request.url.path.endswith("/search"):
        links = [
            create_root_link(request),
            {
                "rel": Relations.self,
                "type": MimeTypes.geojson,
                "href": "/search",
            },
        ]

    inferred_link_rels = set([link["rel"] for link in links])

    # Combine with links from the stac object
    for link in stac_object["links"]:
        if link["rel"] not in inferred_link_rels:
            links.append(link)

    base_url = get_base_url(request)
    stac_object["links"] = resolve_relative_links(links, base_url)

    return stac_object


def hydrate_inferred_links(request: Request, stac_object: Dict) -> Dict:
    """Infer the stac object type and hydrate with inferred links.

    If the stac object type is not recognized it will be returned as-is.
    """
    if stac_object.get("type") == "Catalog":
        return hydrate_catalog_links(request, stac_object)
    elif stac_object.get("type") == "Collection":
        return hydrate_collection_links(request, stac_object)
    elif stac_object.get("type") == "Feature":
        return hydrate_item_links(request, stac_object)
    elif stac_object.get("type") == "FeatureCollection":
        return hydrate_item_collection_links(request, stac_object)
    elif "collections" in stac_object:
        return hydrate_collections_links(request, stac_object)

    # Return the stac object as-is if the object type is not recognized by this function.
    return stac_object
