"""Management endpoints."""

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Message(BaseModel):
    """Liveliness probe response model"""

    message: str


@router.get("/_mgmt/ping", response_model=Message)
async def ping():
    """Liveliness/readiness probe"""
    return Message(message="PONG")
