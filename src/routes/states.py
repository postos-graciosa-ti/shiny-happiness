from fastapi import APIRouter

from src.controllers.states import handle_get_states, handle_post_states
from src.models.states import States

states_routes = APIRouter()


@states_routes.get("/states")
async def get_states():
    return await handle_get_states()


@states_routes.post("/states")
async def post_states(state: States):
    return await handle_post_states(state)
