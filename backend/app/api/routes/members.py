import uuid
from typing import Any

from app.models.crud import members
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import col, delete, func, select

from app.models.members import (
    Members,
    UpdateMembers,
    DeleteMembers
)
from app.api.deps import SessionDep


router = APIRouter(prefix="/membership", tags=["Members"])


@router.post(
    "/addmember",
    response_model=Members,
)
def add_member(session: SessionDep, member_in: Members) -> Any:
    """
    create new member.
    """
    member = members.create_member(session=session, member_create=member_in)
    return member

@router.get(
        "/",
        response_model=Members,
)
def get_member(session: SessionDep, member_in: Members) -> Any:
    """
    Get member by email
    """
    member = members.get_member_by_email(session=session, email=member_in.Email)
    return member

@router.delete(
        "/deletemember",
        response_model=DeleteMembers,
)
def delete_member(session: SessionDep, member_in: DeleteMembers) -> Any:
    """
    Delete member by id
    """
    member = members.get_member_by_email(session=session, email=member_in.Email)
    if not member:
        raise HTTPException(
            status_code=400,
            detail="Member which you are trying to delete does not exist.",
        
    )
    members.delete_member(session=session, db_member=member_in)
    return member

@router.patch(
        "/updatemember",
        response_model= Members,
)
def update_member(session: SessionDep, member_in: UpdateMembers) -> Any:
    member = members.get_member_by_email(session=session, email=member_in.Email)
    if not member:
        raise HTTPException(
            status_code=400,
            detail="The member which you are trying to update does not exist.",
        
    )
    member = members.update_member(session=session, db_member=member, member_in=member_in)
    return member