"""context extension."""
from typing import List, Optional

import attr
from fastapi import FastAPI
import fastapi
from stac_fastapi.types.errors import NotFoundError

from stac_fastapi.types.extension import ApiExtension


@attr.s
class CrsExtension(ApiExtension):
    """Crs Extension.
    """

    crs: List[str] = attr.ib(
        factory=lambda: [
            "http://www.opengis.net/def/crs/OGC/1.3/CRS84",
            "http://www.opengis.net/def/crs/EPSG/0/25832",
        ]
    )
    # Service wide storage-crs ( will be overriden if defined in collection entry )
    storageCrs: str = attr.ib(default="http://www.opengis.net/def/crs/OGC/1.3/CRS84")
    conformance_classes: List[str] = attr.ib(
        default=["http://www.opengis.net/spec/ogcapi-features-2/1.0/conf/crs"]
    )

    def epsg_from_crs(self, crs) -> int:
        """Returns an EPSG code from supported crs"""
        epsg_mapping = {
            "http://www.opengis.net/def/crs/OGC/1.3/CRS84": 4326,
            "http://www.opengis.net/def/crs/EPSG/0/25832": 25832,
        }

        if crs in epsg_mapping:
            return epsg_mapping[crs]
        else:
            raise ValueError("crs not supported")

    def is_crs_supported(self, crs) -> bool:
        """Asserts whether the CRS is supported"""

        if crs in self.crs:
            return True

        return False

    def register(self, app: FastAPI) -> None:
        """Register the extension with a FastAPI application.

        Args:
            app: target FastAPI application.

        Returns:
            None
        """
        pass
