from fastapi import APIRouter, Depends

from src.security.verify_jwt_token import verify_jwt_token
from src.controllers.hierarchy_structure import handle_get_hierarchy_structure

hierarchy_structure_routes = APIRouter(dependencies=[Depends(verify_jwt_token)])


@hierarchy_structure_routes.get("/hierarchy-structure")
async def get_hierarchy_structure():
    return await handle_get_hierarchy_structure()
