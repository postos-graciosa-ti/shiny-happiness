from fastapi import APIRouter

from src.controllers.nationalities import (
    handle_get_nationalities,
    handle_post_nationalities,
)
from src.models.nationalities import Nationalities

nationalities_routes = APIRouter()


@nationalities_routes.get("/nationalities")
async def get_nationalities():
    return await handle_get_nationalities()


@nationalities_routes.post("/nationalities")
async def post_nationalities(nationalitie: Nationalities):
    return await handle_post_nationalities(nationalitie)
