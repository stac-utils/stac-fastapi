"""base api extension."""
import abc
from typing import List, Optional

import attr
from fastapi import FastAPI


@attr.s
class ApiExtension(abc.ABC):
    """Abstract base class for defining API extensions."""

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
