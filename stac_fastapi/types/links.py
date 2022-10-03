"""link helpers."""
from typing import Dict
from urllib.parse import urljoin

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


def create_root_link(request: Request):
    """Create link to API root."""
    return dict(rel=Relations.root, type=MimeTypes.json, href=get_base_url(request))


def hydrate_collection_links(request: Request, stac_object: Dict) -> Dict:
    """Hydrate collection with inferred links."""
    base_url = get_base_url(request)
    links = [
        create_root_link(request),
        dict(rel=Relations.parent, type=MimeTypes.json, href=base_url),
        dict(
            rel=Relations.self,
            type=MimeTypes.json,
            href=urljoin(base_url, f"collections/{stac_object['id']}"),
        ),
        dict(
            rel="items",
            type=MimeTypes.geojson,
            href=urljoin(base_url, f"collections/{stac_object['id']}/items"),
        ),
    ]
    stac_object["links"].extend(links)
    return stac_object


def hydrate_catalog_links(request: Request, stac_object: Dict) -> Dict:
    """Hydrate catalog with inferred links."""
    base_url = get_base_url(request)
    resolved_links = [
        create_root_link(request),
        {
            "rel": "service-desc",
            "type": "application/vnd.oai.openapi+json;version=3.0",
            "title": "OpenAPI service description",
            "href": urljoin(base_url, request.app.openapi_url.lstrip("/")),
        },
        {
            "rel": "service-doc",
            "type": "text/html",
            "title": "OpenAPI service documentation",
            "href": urljoin(base_url, request.app.docs_url.lstrip("/")),
        },
    ]
    # The landing page returns partially resolved links because it requires fetching collections
    # through the backend client.  These need to be resolved by prepending the base url.
    for link in stac_object["links"]:
        link["href"] = urljoin(base_url, link["href"])
        resolved_links.append(link)

    stac_object["links"] = resolved_links
    return stac_object


def hydrate_collections_links(request: Request, stac_object: Dict) -> Dict:
    """Hydrate collections with inferred links."""
    base_url = get_base_url(request)
    stac_object["collections"] = [
        hydrate_collection_links(request, collection)
        for collection in stac_object["collections"]
    ]

    links = [
        create_root_link(request),
        {
            "rel": Relations.parent.value,
            "type": MimeTypes.json,
            "href": base_url,
        },
        {
            "rel": Relations.self.value,
            "type": MimeTypes.json,
            "href": urljoin(base_url, "collections"),
        },
    ]
    stac_object["links"].extend(links)
    return stac_object


def hydrate_item_links(request: Request, stac_object: Dict) -> Dict:
    """Hydrate item with inferred links."""
    base_url = get_base_url(request)

    links = [
        create_root_link(request),
        {
            "rel": Relations.self,
            "type": MimeTypes.geojson,
            "href": urljoin(
                base_url,
                f"collections/{stac_object['collection']}/items/{stac_object['id']}",
            ),
        },
        {
            "rel": Relations.parent,
            "type": MimeTypes.json,
            "href": urljoin(base_url, f"collections/{stac_object['collection']}"),
        },
        {
            "rel": Relations.collection,
            "type": MimeTypes.json,
            "href": urljoin(base_url, f"collections/{stac_object['collection']}"),
        },
    ]

    stac_object["links"].extend(links)
    return stac_object


def hydrate_item_collection_links(request: Request, stac_object: Dict) -> Dict:
    """Hydrate item collection with inferred links."""
    base_url = get_base_url(request)
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
                "href": urljoin(
                    base_url,
                    f"collections/{collection_name}/items",
                ),
            },
            {
                "rel": Relations.parent,
                "type": MimeTypes.json,
                "href": urljoin(base_url, f"collections/{collection_name}"),
            },
        ]
    elif request.url.path.endswith("/search"):
        links = [
            create_root_link(request),
            {
                "rel": Relations.self,
                "type": MimeTypes.geojson,
                "href": urljoin(base_url, "search"),
            },
        ]
    stac_object["links"].extend(links)
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
