"""Catalogs extension module."""

from stac_pydantic.api.collections import Collections

from .catalogs import CATALOGS_CONFORMANCE_CLASSES, CatalogsExtension
from .client import AsyncBaseCatalogsClient, BaseCatalogsClient
from .types import Catalogs, Children

__all__ = [
    "CatalogsExtension",
    "AsyncBaseCatalogsClient",
    "BaseCatalogsClient",
    "Catalogs",
    "Collections",
    "Children",
    "CATALOGS_CONFORMANCE_CLASSES",
]
