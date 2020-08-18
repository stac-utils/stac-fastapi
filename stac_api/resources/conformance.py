"""Conformance endpoints"""
from urllib.parse import urljoin

from fastapi import APIRouter, Depends

from stac_pydantic.api import ConformanceClasses, LandingPage
from stac_pydantic.shared import Link, MimeTypes, Relations

from ..clients import collection_crud_client_factory
from ..clients.collection_crud import CollectionCrudClient
from ..models.links import CollectionLinks
from ..utils.dependencies import discover_base_url

router = APIRouter()


@router.get("/", response_model=LandingPage, response_model_exclude_unset=True)
def landing_page(
    base_url: str = Depends(discover_base_url),
    crud_client: CollectionCrudClient = Depends(collection_crud_client_factory),
):
    """Get landing page"""
    resp = LandingPage(
        title="Arturo STAC API",
        description="Arturo raster datastore",
        links=[
            Link(rel=Relations.self, type=MimeTypes.json, href=base_url),
            Link(
                rel=Relations.docs,
                type=MimeTypes.html,
                title="OpenAPI docs",
                href=urljoin(base_url, "/docs"),
            ),
            Link(
                rel=Relations.conformance,
                type=MimeTypes.json,
                title="STAC/WFS3 conformance classes implemented by this server",
                href=urljoin(base_url, "/conformance"),
            ),
            Link(
                rel=Relations.search,
                type=MimeTypes.geojson,
                title="STAC search",
                href=urljoin(base_url, "/search"),
            ),
        ],
    )
    collections = crud_client.get_all_collections()
    for coll in collections:
        coll_link = CollectionLinks(collection_id=coll.id, base_url=base_url).self()
        coll_link.rel = Relations.child
        coll_link.title = coll.title
        resp.links.append(coll_link)
    return resp


@router.get(
    "/conformance", response_model=ConformanceClasses, response_model_exclude_unset=True
)
def coformance_classes():
    """Get conformance classes"""
    return ConformanceClasses(
        conformsTo=[
            "https://stacspec.org/STAC-api.html",
            "http://docs.opengeospatial.org/is/17-069r3/17-069r3.html#ats_geojson",
        ]
    )
