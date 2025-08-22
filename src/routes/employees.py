from fastapi import APIRouter, Depends

from src.controllers.employees import (
    handle_delete_employees,
    handle_get_employees_by_subsidiarie,
    handle_patch_employees,
    handle_post_employees,
)
from src.models.employees import Employees
from src.security.verify_jwt_token import verify_jwt_token

employees_routes = APIRouter(dependencies=[Depends(verify_jwt_token)])


@employees_routes.get("/subsidiaries/{id}/employees")
async def get_employees(id: int):
    return await handle_get_employees_by_subsidiarie(id)


@employees_routes.post("/subsidiaries/{id}/employees")
async def post_employees(employee: Employees):
    return await handle_post_employees(employee)


@employees_routes.patch("/employees/{id}")
async def patch_employees(id: int, employee: Employees):
    return await handle_patch_employees(id, employee)


@employees_routes.delete("/employees/{id}")
async def delete_employees(id: int):
    return await handle_delete_employees(id)
