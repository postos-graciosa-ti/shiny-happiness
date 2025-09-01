from fastapi import APIRouter, Depends

from src.controllers.workdays import handle_get_workdays
from src.security.verify_jwt_token import verify_jwt_token

workdays_routes = APIRouter(dependencies=[Depends(verify_jwt_token)])


@workdays_routes.get("/workdays")
async def get_workdays():
    return await handle_get_workdays()
