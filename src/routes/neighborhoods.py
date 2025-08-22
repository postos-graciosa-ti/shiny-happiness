from fastapi import APIRouter

from src.controllers.neighborhoods import handle_get_neighborhoods

neighborhoods_routes = APIRouter()


@neighborhoods_routes.get("/neighborhoods")
async def get_neighborhoods():
    return await handle_get_neighborhoods()
