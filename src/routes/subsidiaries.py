from fastapi import APIRouter

subsidiaries_routes = APIRouter()


@subsidiaries_routes.get("/subsidiaries/{id}")
async def get_subsidiaries_by_id(id: int):
    return
