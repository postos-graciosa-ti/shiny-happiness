from fastapi import APIRouter

from src.controllers.ethnicities import handle_get_ethnicities

ethnicities_routes = APIRouter()


@ethnicities_routes.get("/ethnicities")
async def get_ethnicities():
    return await handle_get_ethnicities()
