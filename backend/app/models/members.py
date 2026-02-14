import uuid
from datetime import datetime, timezone

from sqlalchemy import DateTime
from sqlmodel import Field, SQLModel, ForeignKey

def get_datetime_utc() -> datetime:
    return datetime.now(timezone.utc)

class Members(SQLModel, table=True):
    __tablename__ = "members"
    Member_id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    Name: str = Field(max_length=255)
    Email: str = Field(max_length=255, unique=True)
    Phone_number: str = Field(max_length=20)
    Address: str = Field(max_length=255)
    Membership_start_date: datetime = Field(default_factory=get_datetime_utc, sa_type=DateTime(timezone=True))  # type: ignore
    Membership_end_date: datetime | None = Field(default=None, sa_type=DateTime(timezone=True))  # type: ignore
    Created_date: datetime | None = Field(
        default_factory=get_datetime_utc,
        sa_type=DateTime(timezone=True),  # type: ignore
    )
    Updated_date: datetime = True

class CreateMember(Members):
    __tablename__ = "memberships"
    membership_id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    Member_id: uuid.UUID = ForeignKey("members.Member_id")
    Registration_date: datetime = Field(default_factory=get_datetime_utc, sa_type=DateTime(timezone=True))
    Expiry_date: datetime | None = Field(default=None, sa_type=DateTime(timezone=True))
    Is_active: bool = Field(default=True)
    Type: str = Field(max_length=100)
    Created_date: datetime | None = Field(
        default_factory=get_datetime_utc,
        sa_type=DateTime(timezone=True),
    )
    updated_date: datetime = True

class DeleteMembers(Members):
    Member_id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

class UpdateMembers(Members):
    Member_id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    Name: str = Field(max_length=255)
    Email: str = Field(max_length=255, unique=True)
    Phone_number: str = Field(max_length=20)
    Address: str = Field(max_length=255)

class RenewMembership(Members):
    Member_id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    Membership_end_date: datetime | None = Field(default=None, sa_type=DateTime(timezone=True))