from fastapi import APIRouter, Depends

from src.controllers.departments import handle_get_departments
from src.security.verify_jwt_token import verify_jwt_token

departments_routes = APIRouter(dependencies=[Depends(verify_jwt_token)])


@departments_routes.get("/departments")
async def get_departments():
    return await handle_get_departments()
