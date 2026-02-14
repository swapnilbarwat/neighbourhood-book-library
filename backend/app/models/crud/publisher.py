import uuid
from typing import Any

from app.models.common import CustomResponse, get_custom_response
from sqlmodel import Session, select

from app.models.books import Publisher

def create_publisher(*, session: Session, publisher_create: Publisher) -> CustomResponse:
    db_obj = publisher_create.model_validate(publisher_create)
    publisher = get_publisher_by_name(session=session, publisher_name=publisher_create.Publisher_name)
    if publisher:
        return get_custom_response(message="Author added successfully", data=db_obj)
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return get_custom_response(message="Author added successfully", data=db_obj)

def get_publisher_by_name(*, session: Session, publisher_name: str) -> Publisher:
    statement = select(Publisher).where(Publisher.Publisher_name == publisher_name)
    session_publisher = session.exec(statement).first()
    return session_publisher