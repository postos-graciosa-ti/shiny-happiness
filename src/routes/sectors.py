from fastapi import APIRouter, Depends

from src.controllers.sectors import handle_get_sectors
from src.security.verify_jwt_token import verify_jwt_token

sectors_routes = APIRouter(dependencies=[Depends(verify_jwt_token)])


@sectors_routes.get("/sectors")
async def get_sectors():
    return await handle_get_sectors()
