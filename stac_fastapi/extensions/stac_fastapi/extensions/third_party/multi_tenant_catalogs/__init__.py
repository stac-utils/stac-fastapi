"""Catalogs extension module."""

from .catalogs import CATALOGS_CONFORMANCE_CLASSES, CatalogsExtension
from .client import AsyncBaseCatalogsClient, BaseCatalogsClient
from .types import (
    CatalogChildrenRequest,
    CatalogCollectionItemsRequest,
    CatalogCollectionItemUri,
    CatalogCollectionUri,
    Catalogs,
    CatalogsGetRequest,
    CatalogsUri,
    Children,
    CreateCatalogCollectionRequest,
    CreateCatalogRequest,
    CreateSubCatalogRequest,
    ObjectUri,
    SubCatalogsRequest,
    UnlinkSubCatalogRequest,
    UpdateCatalogRequest,
)

__all__ = [
    "CatalogsExtension",
    "AsyncBaseCatalogsClient",
    "BaseCatalogsClient",
    "Catalogs",
    "Children",
    "ObjectUri",
    "CATALOGS_CONFORMANCE_CLASSES",
    "CatalogsUri",
    "CatalogsGetRequest",
    "CatalogCollectionUri",
    "CatalogCollectionItemUri",
    "CatalogCollectionItemsRequest",
    "SubCatalogsRequest",
    "CatalogChildrenRequest",
    "CreateCatalogRequest",
    "UpdateCatalogRequest",
    "CreateCatalogCollectionRequest",
    "CreateSubCatalogRequest",
    "UnlinkSubCatalogRequest",
]
