from fastapi import APIRouter

from src.controllers.neighborhoods import (
    handle_get_neighborhoods,
    handle_get_neighborhoods_by_id,
    handle_post_neighborhoods,
)
from src.models.neighborhoods import Neighborhoods

neighborhoods_routes = APIRouter()


@neighborhoods_routes.get("/neighborhoods")
async def get_neighborhoods():
    return await handle_get_neighborhoods()


@neighborhoods_routes.get("/neighborhoods/{id}")
async def get_neighborhoods_by_id(id: int):
    return await handle_get_neighborhoods_by_id(id)


@neighborhoods_routes.post("/neighborhoods")
async def post_neighborhoods(neighborhood: Neighborhoods):
    return await handle_post_neighborhoods(neighborhood)
