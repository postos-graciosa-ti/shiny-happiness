from fastapi import APIRouter
from pydantic import BaseModel

from src.controllers.sales_report import handle_get_daily_sales_report

sales_report_routes = APIRouter()


class GetDailySalesReportRequest(BaseModel):
    dataInicial: str
    dataFinal: str
    empresaCodigo: int


@sales_report_routes.post("/sales-report/daily-sales")
async def get_daily_sales_report(payload: GetDailySalesReportRequest):
    return await handle_get_daily_sales_report(payload)
