from fastapi import APIRouter, Depends

from src.controllers.genders import handle_get_genders
from src.security.verify_jwt_token import verify_jwt_token

genders_routes = APIRouter(dependencies=[Depends(verify_jwt_token)])


@genders_routes.get("/genders")
async def get_genders():
    return await handle_get_genders()
