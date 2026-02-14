from typing import Optional
import uuid
from datetime import datetime, timezone

from sqlalchemy import DateTime
from sqlmodel import Field, SQLModel, ForeignKey


def get_datetime_utc() -> datetime:
    return datetime.now(timezone.utc)

class Books(SQLModel, table=True):
    __tablename__ = "books"
    Book_id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    Title: str = Field(max_length=255)
    Author_id: uuid.UUID = Field(foreign_key="authors.Author_id")
    publication_date: datetime = Field(default="")
    Publisher_id: uuid.UUID = Field(default="", foreign_key="publishers.Publisher_id")
    Isbn: str = Field(max_length=13)
    Genre: str = Field(max_length=100)
    Price: float = Field(default=0)
    cover_image_url: str
    Created_date: datetime | None = Field(
        default_factory=get_datetime_utc,
        sa_type=DateTime(timezone=True),
    )
    Updated_date: datetime | None = Field(
        default_factory=get_datetime_utc,
        sa_type=DateTime(timezone=True),
    )
    is_deleted: bool = Field(default=False)

class BookCopies(SQLModel, table=True):
    __tablename__ = "book_copies"
    Copy_id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    Book_id: str = ForeignKey("books.Book_id")
    Barcode: str = Field(unique=True)
    Isbn: str = Field(max_length=13)
    Status: str = Field(max_length=50)
    Shelf_location: str = Field(max_length=100)
    cutter_code: str = Field(max_length=100)
    Condition_On_Issue: str = Field(max_length=255)
    Condition_On_return: str = Field(max_length=255)
    Count: int = Field(default=0)
    created_date: datetime | None = Field(
        default_factory=get_datetime_utc,
        sa_type=DateTime(timezone=True),  # type: ignore
    )
    updated_date: datetime = True

# Properties to receive via API on creation
class BookCreate(Books):
    Title: str = True
    Author_id: uuid.UUID = Field(foreign_key="authors.Author_id")
    publication_date: datetime = Field(default=None)
    Publisher_id: uuid.UUID = Field(foreign_key="publishers.Publisher_id")
    Isbn: str = Field(max_length=13)
    Genre: str = Field(max_length=100)
    Price: float = Field(gt=0)
    Count: int = Field(default=0)
    Barcode: str = True
    cover_image_url: str

class BooksDelete(Books):
    Book_id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

class GetBooks(Books):
    Book_id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    Title: str = Field(max_length=255)
    Author_id: uuid.UUID = Field(foreign_key="authors.Author_id")
    publication_date: datetime = True

class UpdateBooks(Books):
    Book_id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    Title: str = Field(max_length=255)
    Author_id: uuid.UUID = Field(foreign_key="authors.Author_id")
    publication_date: datetime = Field(default=None)
    Publisher_id: uuid.UUID = Field(foreign_key="publishers.Publisher_id")
    Isbn: str = Field(max_length=13)
    Genre: str = True
    Price: float = True
    Count: int = True
    cover_image_url: str

class Publisher(SQLModel, table=True):
    __tablename__ = "publishers"
    Publisher_id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    Publisher_name: str = Field(max_length=255)
    created_date: datetime | None = Field(
        default_factory=get_datetime_utc,
        sa_type=DateTime(timezone=True),
    )
    updated_date: datetime | None = Field(
        default_factory=get_datetime_utc,
        sa_type=DateTime(timezone=True),
    )
    Address1: str = Field(max_length=255)
    state: str = Field(max_length=100)
    Zipcode: str = Field(max_length=20)
    country: str = Field(max_length=100)
    is_deleted: bool = Field(default=False)

class CreatePublisher(Publisher):
    Publisher_name: str = Field(max_length=255)
    Address1: str = Field(max_length=255)
    state: str = Field(max_length=100)
    Zipcode: str = Field(max_length=20)
    country: str = Field(max_length=100)

class DeletePublisher(Publisher):
    Publisher_id: uuid.UUID = Field(default_factory=uuid.uuid4)

class UpdatePublisher(Publisher):
    Publisher_id: uuid.UUID = Field(default_factory=uuid.uuid4)
    Publisher_name: str = Field(max_length=255)
    Address1: str = Field(max_length=255)
    state: str = Field(max_length=100)
    Zipcode: str = Field(max_length=20)
    country: str = Field(max_length=100)

class GetPublisher(Publisher):
    Publisher_id: uuid.UUID = Field(default_factory=uuid.uuid4)
    Publisher_name: str = Field(max_length=255)

class Author(SQLModel, table=True):
    __tablename__ = "authors"
    Author_id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    First_name: str = Field(max_length=255)
    Last_name: str = Field(max_length=255)
    Address1: str = Field(max_length=255)
    State: str = Field(max_length=100)
    Zip: str = Field(max_length=20)
    country: str = Field(max_length=100)
    created_date: datetime | None = Field(
        default_factory=get_datetime_utc,
        sa_type=DateTime(timezone=True),   
    )  
    isAssociatedWithCommunity: bool = Field(default=False)
    updated_date: datetime | None = Field(default=None)
    is_deleted: bool = Field(default=False)

class CreateAuthor(Author):
    First_name: str = Field(max_length=255)
    Last_name: str = Field(max_length=255)
    Address1: str = Field(max_length=255)
    State: str = Field(max_length=100)
    Zip: str = Field(max_length=20)
    country: str = Field(max_length=100)

class DeleteAuthor(Author):
    Author_id: uuid.UUID = Field(default_factory=uuid.uuid4)

class UpdateAuthor(Author):
    Author_id: uuid.UUID = Field(default_factory=uuid.uuid4)
    First_name: Optional[str] = Field(max_length=255)
    last_name: Optional[str] = Field(max_length=255)
    Address1: str = Field(max_length=255)
    State: str = Field(max_length=100)
    Zip: str = Field(max_length=20)
    country: str = Field(max_length=100)

class GetAuthor(Author):
    Author_id: uuid.UUID = Field(default_factory=uuid.uuid4)
    First_name: Optional[str] = Field(max_length=255)
    last_name: Optional[str] = Field(max_length=255)