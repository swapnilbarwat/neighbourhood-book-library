import uuid
from typing import Any

from app.models.members import Members
from sqlmodel import Session, select

from app.core.security import get_password_hash, verify_password
from app.models.members import (
    DeleteMembers,
    Members,
    UpdateMembers
)

def create_member(*, session: Session, member_create: Members) -> Members:
    db_obj = member_create.model_validate(exclude_unset=True)
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj

def update_member(*, session: Session, db_member: UpdateMembers, member_in: UpdateMembers) -> Any:
    member_data = member_in.model_validate(exclude_unset=True)
    db_member.sqlmodel_update(member_data)
    session.add(db_member)
    session.commit()
    session.refresh(db_member)
    return db_member

def delete_member(*, session: Session, db_member: DeleteMembers) -> None:
    session.delete(db_member)
    session.commit()

def get_member_by_email(*, session: Session, email: str) -> Members | None:
    statement = select(Members).where(Members.Email == email)
    session_member = session.exec(statement).first()
    return session_member    