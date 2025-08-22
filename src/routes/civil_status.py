from fastapi import APIRouter, Depends

from src.controllers.civil_status import handle_get_civil_status
from src.security.verify_jwt_token import verify_jwt_token

civil_status_routes = APIRouter(dependencies=[Depends(verify_jwt_token)])


@civil_status_routes.get("/civil-status")
async def get_civil_status():
    return await handle_get_civil_status()
