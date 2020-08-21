"""api request/response models, #TODO: Move this somewhere more sensible"""

import abc
from dataclasses import dataclass
from typing import Dict

from fastapi import Path


@dataclass  # type:ignore
class APIRequest(abc.ABC):
    """Generic API Request base class"""

    @abc.abstractmethod
    def kwargs(self) -> Dict:
        """Transform api request params into format which matches the signature of the endpoint"""
        ...


@dataclass  # type:ignore
class CollectionUri(APIRequest):
    """Delete collection"""

    collectionId: str = Path(..., description="Collection ID")

    def kwargs(self) -> Dict:
        """kwargs"""
        return {"id": self.collectionId}


@dataclass
class ItemUri(CollectionUri):
    """Delete item"""

    itemId: str = Path(..., description="Item ID")

    def kwargs(self) -> Dict:
        """kwargs"""
        return {"id": self.itemId}


@dataclass
class EmptyRequest(APIRequest):
    """Empty request"""

    def kwargs(self) -> Dict:
        """kwargs"""
        return {}


@dataclass
class ItemCollectionUri(CollectionUri):
    """Get item collection"""

    limit: int = 10
    token: str = None

    def kwargs(self) -> Dict:
        """kwargs"""
        return {"id": self.collectionId, "limit": self.limit, "token": self.token}
