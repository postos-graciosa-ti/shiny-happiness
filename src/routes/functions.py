from fastapi import APIRouter, Depends

from src.controllers.functions import (
    handle_get_functions_by_id,
    handle_get_functions_by_subsidiarie,
    handle_post_functions,
)
from src.models.functions import Functions
from src.security.verify_jwt_token import verify_jwt_token

functions_routes = APIRouter(dependencies=[Depends(verify_jwt_token)])


@functions_routes.get("/functions")
async def get_functions_by_subsidiarie():
    return await handle_get_functions_by_subsidiarie()


@functions_routes.get("/functions/{id}")
async def get_functions_by_id(id: int):
    return await handle_get_functions_by_id(id)


@functions_routes.post("/functions")
async def post_functions(function: Functions):
    return await handle_post_functions(function)
