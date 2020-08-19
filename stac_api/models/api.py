"""api request/response models, #TODO: Move this somewhere more sensible"""

import abc
from dataclasses import dataclass
from typing import Any, Dict

from fastapi import Path


@dataclass  # type:ignore
class APIRequest(abc.ABC):
    """Generic API Request base class"""

    @abc.abstractmethod
    def kwargs(self) -> Dict:
        """Transform api request params into format which matches the signature of the endpoint"""
        ...


@dataclass  # type:ignore
class DeleteCollection(APIRequest):
    """Delete collection"""

    collectionId: str = Path(..., description="Collection ID")

    def kwargs(self) -> Dict:
        """kwargs"""
        return {"id": self.collectionId}


@dataclass
class DeleteItem(DeleteCollection):
    """Delete item"""

    itemId: str = Path(..., description="Item ID")

    def kwargs(self) -> Dict:
        """kwargs"""
        return {"id": self.itemId}


@dataclass  # type:ignore
class APIResponse(abc.ABC):
    """Generic API Response base class"""

    @classmethod
    @abc.abstractmethod
    def create_api_response(self, obj: Any, base_url: str) -> Any:
        """Transform endpoint response into something compatible with fastapi"""
        ...
