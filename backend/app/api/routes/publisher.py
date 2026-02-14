import uuid
from typing import Any

from app.models.crud import publisher
from fastapi import APIRouter, HTTPException
from sqlmodel import col, delete, func, select

from app.models.books import (
   Publisher
)
from app.models.common import CustomResponse
from app.api.deps import SessionDep


router = APIRouter(prefix="/membership", tags=["Publishers"])


@router.post(
    "/addpublisher",
    response_model=CustomResponse
)
def add_publisher(session: SessionDep, publisher_in: Publisher) -> Any:
    """
    create new publisher.
    """
    response = publisher.create_publisher(session=session, publisher_create=publisher_in)
    return response