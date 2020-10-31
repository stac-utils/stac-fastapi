"""cloudfront extension"""
from dataclasses import dataclass

from fastapi import FastAPI
from starlette.requests import Request

from stac_api.api.extensions.extension import ApiExtension
from stac_api.clients.cloudfront import Signer


@dataclass
class CloudfrontExtension(ApiExtension):
    client: Signer


    def middleware(self, request: Request, call_next):
        breakpoint()


    def register(self, app: FastAPI) -> None:
        """register extension with the application"""
        ...

