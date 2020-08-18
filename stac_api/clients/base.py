"""Base clients."""
import abc
from dataclasses import dataclass
from typing import Any, List, Tuple

from stac_api.models import schemas


@dataclass  # type:ignore
class BaseClient(abc.ABC):
    """Base datastore client"""

    @abc.abstractmethod
    def read(self, id: str) -> Any:
        """Read a record by id"""
        ...


@dataclass  # type:ignore
class BaseTransactionsClient(abc.ABC):
    """Base transactions client"""

    @abc.abstractmethod
    def create_item(self, model: schemas.Item) -> Any:
        """Create item"""
        ...

    @abc.abstractmethod
    def update_item(self, model: schemas.Item) -> Any:
        """Update item"""
        ...

    @abc.abstractmethod
    def delete_item(self, id: str) -> Any:
        """Delete item"""
        ...

    @abc.abstractmethod
    def create_collection(self, model: schemas.Collection) -> Any:
        """Create collection"""
        ...

    @abc.abstractmethod
    def update_collection(self, model: schemas.Collection) -> Any:
        """Update collection"""
        ...

    @abc.abstractmethod
    def delete_collection(self, id: str) -> Any:
        """Delete collection"""
        ...


@dataclass  # type:ignore
class BaseItemClient(BaseClient):
    """Base item client"""

    @abc.abstractmethod
    def search(self, search_request: schemas.STACSearch) -> Tuple[Any, int]:
        """search for items"""
        ...


@dataclass  # type:ignore
class BaseCollectionClient(BaseClient):
    """Base collections client"""

    @abc.abstractmethod
    def all_collections(self) -> List[Any]:
        """Get all collections"""
        ...

    @abc.abstractmethod
    def item_collection(
        self, collection_id: str, limit: int = 10, token: str = None
    ) -> Tuple[Any, int]:
        """Get item collection"""
        ...
