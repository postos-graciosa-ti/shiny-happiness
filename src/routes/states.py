from fastapi import APIRouter

from src.controllers.states import handle_get_states

states_routes = APIRouter()


@states_routes.get("/states")
async def get_states():
    return await handle_get_states()
