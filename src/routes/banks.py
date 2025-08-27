from fastapi import APIRouter

from src.controllers.banks import handle_get_banks

banks_routes = APIRouter()


@banks_routes.get("/banks")
async def get_banks():
    return await handle_get_banks()
