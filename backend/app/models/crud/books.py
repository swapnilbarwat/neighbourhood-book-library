import uuid
from typing import Any

from app.models.common import CustomResponse, get_custom_response
from sqlmodel import Session, select

from app.models.books import Books, BookCreate, UpdateBooks, BooksDelete, BookCopies

def create_book(*, session: Session, book_create: Books) -> Books | CustomResponse:
    # Check if book with same title already exists
    existing_book = get_book_from_isbn(session=session, isbn=book_create.Isbn)
    if existing_book:
        # Book exists: increment inventory count
        book_copy = get_book_copies_from_isbn(session=session, isbn=existing_book.Isbn)
        print(book_copy)
        if book_copy:
            book_copy.Count = book_copy.Count + 1
            session.add(book_copy)
            session.commit()
            session.refresh(book_copy)
            return get_custom_response(message="Book already exist. Increased inventory by 1.", data=book_copy)
    else:
        # New book: create Books entry and BookCopies entry
        db_obj = book_create.model_validate(book_create)
        session.add(db_obj)
        session.commit()
        session.refresh(db_obj)
        return get_custom_response(message="Book added successfully", data=db_obj)

def update_book(*, session: Session, db_book: Books, book_in: UpdateBooks) -> Any:
    book_data = book_in.model_validate(exclude_unset=True)
    db_book.sqlmodel_update(book_data)
    session.add(db_book)
    session.commit()
    session.refresh(db_book)
    return get_custom_response(message="Book updated successfully", data=db_book)

def delete_book(*, session: Session, db_book: BooksDelete) -> None:
    session.delete(db_book)
    session.commit()

def get_book_from_isbn(*, session: Session, isbn: str) -> Books | None:
    statement = select(Books).where(Books.Isbn == isbn)
    session_book = session.exec(statement).first()
    return session_book

def get_book_copies_from_isbn(*, session: Session, isbn: str) -> BookCopies | None:
    print(isbn)
    statement = select(BookCopies).where(BookCopies.Isbn == isbn)
    session_book = session.exec(statement).first()
    return session_book
