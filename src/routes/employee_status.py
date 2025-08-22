from fastapi import APIRouter, Depends

from src.controllers.employee_status import handle_get_employee_status
from src.security.verify_jwt_token import verify_jwt_token

employee_status_routes = APIRouter(dependencies=[Depends(verify_jwt_token)])


@employee_status_routes.get("/employee-status")
async def get_employee_status():
    return await handle_get_employee_status()
