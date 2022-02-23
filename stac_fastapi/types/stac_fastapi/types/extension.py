"""base api extension."""
import abc
from typing import List, Optional

import attr
from fastapi import FastAPI
from pydantic import BaseModel


@attr.s
class ApiExtension(abc.ABC):
    """Interface for defining API extensions.

    Extensions contain functionality that extent the capabilities of the API
    beyond what is provided by the main STAC API conformance classes.  While
    there are many extensions defined in the STAC API spec iteslf, this interface
    may be used to implement 3rd-party extensions which act as hooks for customizing
    API behavior.  This allows users to extensively customize the API to meet their
    use cases.

    The `GET` and `POST` attributes allow extensions to define their own or modify
    existing request bodies.  For example the Filter Extension requires adding a
    `filter` member to the request body of `POST /search` requests.
    """

    GET = None
    POST = None

    def get_request_model(self, verb: Optional[str] = "GET") -> Optional[BaseModel]:
        """Return the request model for the extension verb.

        The model may differ based on HTTP verb

        Args:
            verb: HTTP verb (POST/GET).

        Returns:
            Type[BaseModel]: The request model.
        """
        return getattr(self, verb)

    conformance_classes: List[str] = attr.ib(factory=list)
    schema_href: Optional[str] = attr.ib(default=None)

    @abc.abstractmethod
    def register(self, app: FastAPI) -> None:
        """Register the extension with a FastAPI application.

        This method is called when an extension is attached to the FastAPI
        application, allowing for extensions to be injected at runtime (on app
        startup).  This method should perform any actions required for the
        extension to function properly, such as configuring new API routes, routers,
        or middlewares.

        Args:
            app: target FastAPI application.
        """
        pass
