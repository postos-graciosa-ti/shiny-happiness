from fastapi import APIRouter

from src.controllers.experiences_times import handle_get_experiences_times

experiences_times_routes = APIRouter()


@experiences_times_routes.get("/experiences-times")
async def get_experiences_times():
    return await handle_get_experiences_times()
