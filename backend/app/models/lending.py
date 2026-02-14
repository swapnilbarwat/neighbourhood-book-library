import uuid
from datetime import datetime, timezone

from sqlalchemy import DateTime
from sqlmodel import Field, SQLModel, ForeignKey

def get_datetime_utc() -> datetime:
    return datetime.now(timezone.utc)

class Rent(SQLModel, table=True):
    __tablename__ = "rent"
    Rent_id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    Transaction_id: uuid.UUID = Field(default_factory=uuid.uuid4, unique=True)
    copy_id: uuid.UUID = ForeignKey("book_copies.Copy_id")
    Member_id: uuid.UUID = ForeignKey("members.Member_id")
    Employee_id: uuid.UUID = ForeignKey("employees.Employee_id")
    Date_of_issue: datetime = Field(default_factory=get_datetime_utc, sa_type=DateTime(timezone=True)) 
    Renewal_Count: int = Field(default=0)
    Due_date: datetime = Field(default_factory=get_datetime_utc, sa_type=DateTime(timezone=True)) 
    returned_date: datetime | None = Field(default=None, sa_type=DateTime(timezone=True))  # type: ignore
    Created_date: datetime | None = Field(
        default_factory=get_datetime_utc,
        sa_type=DateTime(timezone=True),  # type: ignore
    )
    Updated_date: datetime = Field(default_factory=get_datetime_utc, sa_type=DateTime(timezone=True)) 
    Fine_amount: float = Field(default=0.0)
    Status: str = Field(default="InActive")

class Return(Rent):
    Barcode: str = Field(max_length=255)
    Condition_On_return: str = Field(max_length=255)
    returned_date: datetime = Field(default_factory=get_datetime_utc, sa_type=DateTime(timezone=True))

class Renew(Rent):
    Due_date: datetime = Field(default_factory=get_datetime_utc, sa_type=DateTime(timezone=True)) 
    Renewal_Count: int = Field(default=0)

class GetRentInfo(Rent):
    Barcode: str = ForeignKey("book_copies.Barcode")
    email: str = ForeignKey("members.Email")