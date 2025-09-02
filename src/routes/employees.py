from fastapi import APIRouter, Depends

from src.controllers.employees import (
    handle_delete_employees,
    handle_get_employees_by_subsidiarie,
    handle_patch_employees,
    handle_post_employees,
    handle_post_request_admissional_exam,
    handle_post_send_employees_admission_to_contability,
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


@employees_routes.post("/employees/{id}/request-admissional-exam")
async def post_request_admissional_exam(id: int):
    return await handle_post_request_admissional_exam(id)


@employees_routes.post("/employees/{id}/send-admission-to-contability")
async def post_send_employees_admission_to_contability(id: int):
    return await handle_post_send_employees_admission_to_contability(id)


@employees_routes.patch("/employees/{id}")
async def patch_employees(id: int, employee: Employees):
    return await handle_patch_employees(id, employee)


@employees_routes.delete("/employees/{id}")
async def delete_employees(id: int):
    return await handle_delete_employees(id)
