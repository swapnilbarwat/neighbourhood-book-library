from fastapi import APIRouter

from app.api.routes import inventory, members, lending, author, publisher
from app.core.config import settings

api_router = APIRouter()
api_router.include_router(inventory.router)
api_router.include_router(members.router)
api_router.include_router(lending.router)
api_router.include_router(author.router)
api_router.include_router(publisher.router)



# if settings.ENVIRONMENT == "local":
    # do something for local environment.   