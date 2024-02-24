"""Conformance Classes."""

from enum import Enum


class STACConformanceClasses(str, Enum):
    """Conformance classes for the STAC API spec."""

    CORE = "https://api.stacspec.org/v1.0.0/core"
    OGC_API_FEAT = "https://api.stacspec.org/v1.0.0/ogcapi-features"
    COLLECTIONS = "https://api.stacspec.org/v1.0.0/collections"
    ITEM_SEARCH = "https://api.stacspec.org/v1.0.0/item-search"


class OAFConformanceClasses(str, Enum):
    """Conformance classes for OGC API - Features."""

    CORE = "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/core"
    OPEN_API = "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/oas30"
    GEOJSON = "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/geojson"


BASE_CONFORMANCE_CLASSES = [
    STACConformanceClasses.CORE,
    STACConformanceClasses.OGC_API_FEAT,
    STACConformanceClasses.COLLECTIONS,
    STACConformanceClasses.ITEM_SEARCH,
    OAFConformanceClasses.CORE,
    OAFConformanceClasses.OPEN_API,
    OAFConformanceClasses.GEOJSON,
]
