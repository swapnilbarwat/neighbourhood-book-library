import uuid
from typing import Any

from app.models.common import CustomResponse, get_custom_response
from sqlmodel import Session, select

from app.models.books import CreateAuthor, Author

def create_author(*, session: Session, author_create: Author) -> CustomResponse:
    db_obj = author_create.model_validate(author_create)
    author = get_author_by_name(session=session, f_name=author_create.First_name, l_name=author_create.Last_name)
    if author:
        return get_custom_response(message="Author already exist", data=None)
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return get_custom_response(message="Author added successfully", data=db_obj)

def get_author_by_name(*, session: Session, f_name: str, l_name: str) -> Author:
    statement = select(Author).where(Author.First_name == f_name, Author.Last_name == l_name)
    session_author = session.exec(statement).first()
    return session_author