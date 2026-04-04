"""Catalogs extension module."""

from .catalogs import (
    CATALOGS_CORE_CONFORMANCE,
    CATALOGS_TRANSACTION_CONFORMANCE,
    CatalogsExtension,
    CatalogsTransactionExtension,
)
from .client import AsyncBaseCatalogsClient, BaseCatalogsClient
from .types import (
    CatalogChildrenRequest,
    CatalogCollectionItemsRequest,
    CatalogCollectionItemUri,
    CatalogCollectionsRequest,
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
    "CatalogsTransactionExtension",
    "AsyncBaseCatalogsClient",
    "BaseCatalogsClient",
    "Catalogs",
    "Children",
    "ObjectUri",
    "CATALOGS_CORE_CONFORMANCE",
    "CATALOGS_TRANSACTION_CONFORMANCE",
    "CatalogsUri",
    "CatalogsGetRequest",
    "CatalogCollectionUri",
    "CatalogCollectionItemUri",
    "CatalogCollectionItemsRequest",
    "CatalogCollectionsRequest",
    "SubCatalogsRequest",
    "CatalogChildrenRequest",
    "CreateCatalogRequest",
    "UpdateCatalogRequest",
    "CreateCatalogCollectionRequest",
    "CreateSubCatalogRequest",
    "UnlinkSubCatalogRequest",
]
