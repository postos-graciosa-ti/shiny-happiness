from fastapi import APIRouter

from src.controllers.cities import handle_get_cities

cities_routes = APIRouter()


@cities_routes.get("/cities")
async def get_cities():
    return await handle_get_cities()
