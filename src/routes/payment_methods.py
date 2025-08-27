from fastapi import APIRouter

from src.controllers.payment_methods import handle_get_payment_methods

payment_methods_routes = APIRouter()


@payment_methods_routes.get("/payment-methods")
async def get_payment_methods():
    return await handle_get_payment_methods()
