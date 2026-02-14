import uuid
from typing import Any

from app.models.members import Members
from sqlmodel import Session, select

from app.models.lending import (
    Rent,
    Return,
    Renew,
    GetRentInfo
)

def rent(*, session: Session, rent: Rent) -> Rent:
    db_obj = rent.model_validate(exclude_unset=True)
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj

def renew(*, session: Session, db_member: Renew, rent_in: Renew) -> Any:
    rent_data = rent_in.model_validate(exclude_unset=True)
    db_member.sqlmodel_update(rent_data)
    session.add(db_member)
    session.commit()
    session.refresh(db_member)
    return db_member

def return_book(*, session: Session, db_member: Return) -> None:
    # add logic to change the status from rent table to returned
    return 

def get_rent_info(*, session: Session, db_member: GetRentInfo) -> Rent:
    statement = select(GetRentInfo).where(GetRentInfo.Barcode == db_member.Barcode, GetRentInfo.email == db_member.email)
    session_rent_info = session.exec(statement).first()
    return session_rent_info