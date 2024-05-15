"""Base api extension."""

import abc
from typing import List, Optional

import attr
from fastapi import FastAPI
from pydantic import BaseModel


@attr.s
class ApiExtension(abc.ABC):
    """Abstract base class for defining API extensions."""

    GET = None
    POST = None

    def get_request_model(self, verb: Optional[str] = "GET") -> Optional[BaseModel]:
        """Return the request model for the extension.method.

        The model can differ based on HTTP verb
        """
        return getattr(self, verb)

    conformance_classes: List[str] = attr.ib(factory=list)
    schema_href: Optional[str] = attr.ib(default=None)

    @abc.abstractmethod
    def register(self, app: FastAPI) -> None:
        """Register the extension with a FastAPI application.

        Args:
            app: target FastAPI application.

        Returns:
            None
        """
        pass
