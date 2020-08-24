"""Base clients."""
import abc
from dataclasses import dataclass
from typing import List

from stac_api.models import schemas
from stac_pydantic import ItemCollection


@dataclass  # type:ignore
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


@dataclass  # type:ignore
class BaseCoreClient(abc.ABC):
    """Base item client"""

    @abc.abstractmethod
    def search(self, search_request: schemas.STACSearch, **kwargs) -> ItemCollection:
        """search for items"""
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
