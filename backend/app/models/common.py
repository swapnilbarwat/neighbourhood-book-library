
from typing import Optional
from sqlmodel import SQLModel

class CustomResponse(SQLModel):
    status: str
    message: Optional[str] = None
    data: Optional[SQLModel] = None 

def get_custom_response(message: str, data: SQLModel) -> CustomResponse:
    return CustomResponse (
        status="Successful",
        message=message,
        data=data
    )