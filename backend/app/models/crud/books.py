import uuid
from typing import Any

from sqlmodel import Session, select

from app.core.security import get_password_hash, verify_password
from app.models.books import Books, BookCreate, UpdateBooks, BooksDelete

def create_book(*, session: Session, book_create: BookCreate) -> Books:
    db_obj = book_create.model_validate(exclude_unset=True)
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj

def update_book(*, session: Session, db_book: UpdateBooks, book_in: UpdateBooks) -> Any:
    book_data = book_in.model_validate(exclude_unset=True)
    db_book.sqlmodel_update(book_data)
    session.add(db_book)
    session.commit()
    session.refresh(db_book)
    return db_book

def delete_book(*, session: Session, db_book: BooksDelete) -> None:
    session.delete(db_book)
    session.commit()

def get_book_by_title(*, session: Session, title: str) -> Books | None:
    statement = select(Books).where(Books.Title == title)
    session_book = session.exec(statement).first()
    return session_book