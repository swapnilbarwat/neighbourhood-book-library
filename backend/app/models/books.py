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
    publication_date: datetime = Field(default=None)
    Publisher_id: uuid.UUID = Field(foreign_key="publishers.Publisher_id")
    Isbn: str = Field(max_length=13)
    Genre: str = Field(max_length=100)
    Price: float = Field(gt=0)
    cover_image_url: str
    Created_date: datetime | None = Field(
        default_factory=get_datetime_utc,
        sa_type=DateTime(timezone=True),  # type: ignore
    )
    Updated_date: datetime = True

class BookCopies(SQLModel, table=True):
    __tablename__ = "book_copies"
    Copy_id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    Book_id: str = ForeignKey("books.Book_id")
    Barcode: str = True
    Status: str = True
    Shelf_location: str = True
    cutter_code: str = True
    Condition_On_Issue: str = True
    Condition_On_return: str = True
    Count: int = True
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