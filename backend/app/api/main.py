from fastapi import APIRouter

from app.api.routes import inventory, members, lending
from app.core.config import settings

api_router = APIRouter()
api_router.include_router(inventory.router)
api_router.include_router(members.router)
api_router.include_router(lending.router)



# if settings.ENVIRONMENT == "local":
    # do something for local environment.