"""api module"""
from .routes import create_endpoint_from_model, create_endpoint_with_depends

__all__ = ("create_endpoint_from_model", "create_endpoint_with_depends")
