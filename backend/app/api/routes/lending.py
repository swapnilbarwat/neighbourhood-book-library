import uuid
from typing import Any

from app.models.crud import books, lending
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import col, delete, func, select

from app.models.lending import (
    Rent,
    Return,
    Renew,
    GetRentInfo
)
from app.api.deps import SessionDep

router = APIRouter(prefix="/books", tags=["Lending"])

@router.post(
    "/rent",
    response_model=Rent,
)
def rent(session: SessionDep, book_in: Rent) -> Any:
    """
    Rent a book.
    """
    book = books.get_book_by_title(session=session, title=book_in.Title)
    if book:
        raise HTTPException(
            status_code=400,
            detail="The book with this title already exists in the system.",
        
    )
    rent = lending.rent(session=session, rent=book_in)
    return rent

@router.get(
        "/",
        response_model=GetRentInfo,
)
def get_rent_information(session: SessionDep, book_in: GetRentInfo) -> GetRentInfo:
    """
    Get rent information by barcode and email    """
    rent_info = lending.get_rent_info(session=session, db_member=book_in)
    return rent_info   

@router.get(
        "/return",
        response_model=Return,
)
def return_book(session: SessionDep, rent_info: Return) -> Any:
    """
    Return a book.
    """
    return_info = rent_info.delete_book(session=session, Book_id=rent_info.Book_id)
    return return_info

@router.patch(
        "/renew",
        response_model=Renew
)
def renew_book(session: SessionDep, book_in: Renew) -> Any:
    return 