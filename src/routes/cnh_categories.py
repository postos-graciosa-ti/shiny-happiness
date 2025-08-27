from fastapi import APIRouter

from src.controllers.cnh_categories import handle_get_cnh_categories

cnh_categories_routes = APIRouter()


@cnh_categories_routes.get("/cnh-categories")
async def get_cnh_categories():
    return await handle_get_cnh_categories()
