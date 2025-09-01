from fastapi import APIRouter

from src.controllers.school_levels import handle_get_school_levels

school_levels_routes = APIRouter()


@school_levels_routes.get("/school-levels")
async def get_school_levels():
    return await handle_get_school_levels()
