from fastapi import APIRouter

from src.controllers.cities import handle_get_cities, handle_post_cities
from src.models.cities import Cities

cities_routes = APIRouter()


@cities_routes.get("/cities")
async def get_cities():
    return await handle_get_cities()


@cities_routes.post("/cities")
async def post_cities(city: Cities):
    return await handle_post_cities(city)
