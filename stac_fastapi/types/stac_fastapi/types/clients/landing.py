"""Base clients."""
import abc
from typing import List
from urllib.parse import urljoin

import attr
from stac_pydantic.links import Relations
from stac_pydantic.shared import MimeTypes
from stac_pydantic.version import STAC_VERSION

from stac_fastapi.types import stac as stac_types


@attr.s
class LandingPageMixin(abc.ABC):
    """Create a STAC landing page (GET /)."""

    stac_version: str = attr.ib(default=STAC_VERSION)
    landing_page_id: str = attr.ib(default="stac-fastapi")
    title: str = attr.ib(default="stac-fastapi")
    description: str = attr.ib(default="stac-fastapi")

    def _landing_page(
        self,
        base_url: str,
        conformance_classes: List[str],
        extension_schemas: List[str],
    ) -> stac_types.LandingPage:
        landing_page = stac_types.LandingPage(
            type="Catalog",
            id=self.landing_page_id,
            title=self.title,
            description=self.description,
            stac_version=self.stac_version,
            conformsTo=conformance_classes,
            links=[
                {
                    "rel": Relations.self.value,
                    "type": MimeTypes.json,
                    "href": base_url,
                },
                {
                    "rel": Relations.root.value,
                    "type": MimeTypes.json,
                    "href": base_url,
                },
                {
                    "rel": "data",
                    "type": MimeTypes.json,
                    "href": urljoin(base_url, "collections"),
                },
                {
                    "rel": Relations.conformance.value,
                    "type": MimeTypes.json,
                    "title": "STAC/WFS3 conformance classes implemented by this server",
                    "href": urljoin(base_url, "conformance"),
                },
                {
                    "rel": Relations.search.value,
                    "type": MimeTypes.geojson,
                    "title": "STAC search",
                    "href": urljoin(base_url, "search"),
                    "method": "GET",
                },
                {
                    "rel": Relations.search.value,
                    "type": MimeTypes.json,
                    "title": "STAC search",
                    "href": urljoin(base_url, "search"),
                    "method": "POST",
                },
            ],
            stac_extensions=extension_schemas,
        )
        return landing_page
