from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter()


class Message(BaseModel):
    message: str


@router.get("/_mgmt/ping", response_model=Message)
async def ping():
    """Liveliness probe"""
    return Message(message="PONG")
