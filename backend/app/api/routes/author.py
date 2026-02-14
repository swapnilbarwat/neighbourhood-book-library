import uuid
from typing import Any

from app.models.crud import authors
from fastapi import APIRouter, HTTPException
from sqlmodel import col, delete, func, select

from app.models.books import (
   CreateAuthor,
   Author
)
from app.models.common import CustomResponse
from app.api.deps import SessionDep


router = APIRouter(prefix="/membership", tags=["Authors"])


@router.post(
    "/addauthor",
    response_model=CustomResponse,
)
def add_author(session: SessionDep, author_in: Author) -> Any:
    """
    create new author.
    """
    response = authors.create_author(session=session, author_create=author_in)
    return response