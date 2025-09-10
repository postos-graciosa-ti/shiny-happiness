import httpx
from decouple import config
from pydantic import BaseModel

WEB_POSTOS_BASE_URL = config("WEB_POSTOS_BASE_URL")

WEB_POSTOS_API_KEY = config("WEB_POSTOS_API_KEY")


class GetDailySalesReportRequest(BaseModel):
    dataInicial: str
    dataFinal: str
    empresaCodigo: int


async def handle_get_daily_sales_report(payload: GetDailySalesReportRequest):
    url = (
        f"{WEB_POSTOS_BASE_URL}?CHAVE={WEB_POSTOS_API_KEY}"
        f"&dataInicial={payload.dataInicial}"
        f"&dataFinal={payload.dataFinal}"
        f"&empresaCodigo={payload.empresaCodigo}"
    )

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

        response.raise_for_status()

        vendas = response.json()

    total_por_funcionario_produto = {}

    for venda in vendas:
        func_key = venda["funcionarioCodigo"]

        if func_key not in total_por_funcionario_produto:
            total_por_funcionario_produto[func_key] = {
                "funcionarioNome": venda["funcionarioNome"],
                "produtos": {},
            }

        if (
            venda["produtoCodigo"]
            not in total_por_funcionario_produto[func_key]["produtos"]
        ):
            total_por_funcionario_produto[func_key]["produtos"][
                venda["produtoCodigo"]
            ] = {"produtoNome": venda["produtoNome"], "totalVendas": 0}

        total_por_funcionario_produto[func_key]["produtos"][venda["produtoCodigo"]][
            "totalVendas"
        ] += venda["valorVenda"]

    resultado = [
        {
            "funcionarioNome": func["funcionarioNome"],
            "produtos": list(func["produtos"].values()),
        }
        for func in total_por_funcionario_produto.values()
    ]

    chart_result = [
        {
            "funcionario": func["funcionarioNome"],
            "totalVendas": sum(p["totalVendas"] for p in func["produtos"].values()),
        }
        for func in total_por_funcionario_produto.values()
    ]

    return {"resultado": resultado, "chartResult": chart_result, "rawData": vendas}
