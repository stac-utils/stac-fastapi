"""Catalogs extension module."""

from .catalogs import CATALOGS_CONFORMANCE_CLASSES, CatalogsExtension
from .client import AsyncBaseCatalogsClient
from .types import Catalogs, Children, ObjectUri

__all__ = [
    "CatalogsExtension",
    "AsyncBaseCatalogsClient",
    "Catalogs",
    "Children",
    "ObjectUri",
    "CATALOGS_CONFORMANCE_CLASSES",
]
