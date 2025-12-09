"""Base api extension."""

import abc
from typing import List, Optional, Type, Union

import attr
from fastapi import FastAPI
from pydantic import BaseModel

from stac_fastapi.types.search import APIRequest


@attr.s
class ApiExtension(abc.ABC):
    """Abstract base class for defining API extensions."""

    GET: Optional[Type[APIRequest]] = None
    POST: Optional[Type[BaseModel]] = None

    def get_request_model(
        self, verb: str = "GET"
    ) -> Optional[Union[Type[BaseModel], Type[APIRequest]]]:
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
