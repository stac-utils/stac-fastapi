"""Base clients."""
import abc
from datetime import datetime
from typing import Any, Dict, List, Optional, Type, Union

import attr
from stac_pydantic import ItemCollection
from stac_pydantic.api import ConformanceClasses, LandingPage

from stac_api.api.extensions.extension import ApiExtension
from stac_api.models import schemas

NumType = Union[float, int]


@attr.s  # type:ignore
class BaseTransactionsClient(abc.ABC):
    """Base transactions client"""

    @abc.abstractmethod
    def create_item(self, model: schemas.Item, **kwargs) -> schemas.Item:
        """Create item"""
        ...

    @abc.abstractmethod
    def update_item(self, model: schemas.Item, **kwargs) -> schemas.Item:
        """Update item"""
        ...

    @abc.abstractmethod
    def delete_item(self, id: str, **kwargs) -> schemas.Item:
        """Delete item"""
        ...

    @abc.abstractmethod
    def create_collection(
        self, model: schemas.Collection, **kwargs
    ) -> schemas.Collection:
        """Create collection"""
        ...

    @abc.abstractmethod
    def update_collection(
        self, model: schemas.Collection, **kwargs
    ) -> schemas.Collection:
        """Update collection"""
        ...

    @abc.abstractmethod
    def delete_collection(self, id: str, **kwargs) -> schemas.Collection:
        """Delete collection"""
        ...


@attr.s  # type: ignore
class BulkTransactionsClient(abc.ABC):
    """bulk transactions client"""

    @staticmethod
    def _chunks(lst, n):
        """Yield successive n-sized chunks from lst."""
        for i in range(0, len(lst), n):
            yield lst[i : i + n]

    @abc.abstractmethod
    def bulk_item_insert(self, items: List[Dict], chunks: Optional[int] = None) -> None:
        """bulk item insertion, not implemented by default, and not exposed through the api"""
        raise NotImplementedError


@attr.s  # type:ignore
class BaseCoreClient(abc.ABC):
    """Base client for core endpoints defined by stac"""

    extensions: List[ApiExtension] = attr.ib(default=attr.Factory(list))

    def extension_is_enabled(self, extension: Type[ApiExtension]) -> bool:
        """check if an api extension is enabled"""
        return any([isinstance(ext, extension) for ext in self.extensions])

    @abc.abstractmethod
    def landing_page(self, **kwargs) -> LandingPage:
        """landing page"""
        ...

    @abc.abstractmethod
    def conformance(self, **kwargs) -> ConformanceClasses:
        """conformance classes"""
        ...

    @abc.abstractmethod
    def post_search(
        self, search_request: schemas.STACSearch, **kwargs
    ) -> Dict[str, Any]:
        """search for items"""
        ...

    @abc.abstractmethod
    def get_search(
        self,
        collections: Optional[List[str]] = None,
        ids: Optional[List[str]] = None,
        bbox: Optional[List[NumType]] = None,
        datetime: Optional[Union[str, datetime]] = None,
        limit: Optional[int] = 10,
        query: Optional[str] = None,
        token: Optional[str] = None,
        fields: Optional[List[str]] = None,
        sortby: Optional[str] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """GET search catalog"""
        ...

    @abc.abstractmethod
    def get_item(self, id: str, **kwargs) -> schemas.Item:
        """get item by id"""
        ...

    @abc.abstractmethod
    def all_collections(self) -> List[schemas.Collection]:
        """get all collections"""
        ...

    @abc.abstractmethod
    def get_collection(self, id: str, **kwargs) -> schemas.Collection:
        """get collection by id"""
        ...

    @abc.abstractmethod
    def item_collection(
        self, id: str, limit: int = 10, token: str = None, **kwargs
    ) -> ItemCollection:
        """Get item collection"""
        ...
