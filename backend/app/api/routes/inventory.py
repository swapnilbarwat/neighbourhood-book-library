import uuid
from typing import Any

from app.models.crud import books
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import col, delete, func, select

from app.models.books import (
    Books,
    BooksDelete,
    UpdateBooks
)
from app.api.deps import SessionDep

router = APIRouter(prefix="/books", tags=["Books"])

@router.post(
    "/addbooks",
    response_model=Books,
)
def add_book(session: SessionDep, book_in: Books) -> Any:
    """
    create new book.
    """
    book = books.get_book_by_title(session=session, title=book_in.Title)
    if book:
        raise HTTPException(
            status_code=400,
            detail="The book with this title already exists in the system.",
        
    )
    book = books.create_book(session=session, book_create=book_in)
    return book

@router.get(
        "/",
        response_model=Books,
)
def get_book(session: SessionDep, book_in: Books) -> Any:
    """
    Get book by title
    """
    book = books.get_book_by_title(session=session, title=book_in.Title)
    return book

@router.delete(
        "/deletebook",
        response_model=Books,
)
def delete_book(session: SessionDep, book_in: BooksDelete) -> Any:
    """
    Delete book by id
    """
    book = books.get_book_by_title(session=session, title=book_in.Title)
    if not book:
        raise HTTPException(
            status_code=400,
            detail="The book which you are trying to delete does not exist.",
        
    )
    book = books.delete_book(session=session, Book_id=book_in.Book_id)
    return book

@router.patch(
        "/update",
        response_model=Books
)
def update_book(session: SessionDep, book_in: UpdateBooks) -> Any:
    book = books.get_book_by_title(session=session, title=book_in.Title)
    if not book:
        raise HTTPException(
            status_code=400,
            detail="The book which you are trying to update does not exist.",
        
    )
    book = books.update_book(session=SessionDep, book_in=book_in)
    return book