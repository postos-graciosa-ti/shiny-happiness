from fastapi import APIRouter, Depends

from src.controllers.turns import handle_get_turns, handle_get_turns_by_id
from src.security.verify_jwt_token import verify_jwt_token

turns_routes = APIRouter(dependencies=[Depends(verify_jwt_token)])


@turns_routes.get("/turns")
async def get_turns():
    return await handle_get_turns()


@turns_routes.get("/turns/{id}")
async def get_turns_by_id(id: int):
    return await handle_get_turns_by_id(id)
