from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config.database import engine
from src.models.functions import Functions

functions_seed = [
    {"name": "Analista administrativo júnior", "cbo": "2521-05"},
    {"name": "Analista administrativo pleno", "cbo": "2521-05"},
    {"name": "Analista administrativo sênior", "cbo": "2521-05"},
    {"name": "Analista de recursos humanos júnior", "cbo": "2524-05"},
    {"name": "Analista de recursos humanos pleno", "cbo": "2524-05"},
    {"name": "Analista de recursos humanos sênior", "cbo": "2524-05"},
    {"name": "Analista de tecnologia da informação júnior", "cbo": "2124"},
    {"name": "Analista de tecnologia da informação pleno", "cbo": "2124"},
    {"name": "Analista de tecnologia da informação sênior", "cbo": "2124"},
    {"name": "Assistente de compras júnior", "cbo": "4110-10"},
    {"name": "Assistente de compras pleno", "cbo": "4110-10"},
    {"name": "Assistente de compras sênior", "cbo": "4110-10"},
    {"name": "Auxiliar administrativo júnior", "cbo": "4110-05"},
    {"name": "Auxiliar administrativo pleno", "cbo": "4110-05"},
    {"name": "Auxiliar administrativo sênior", "cbo": "4110-05"},
    {"name": "Auxiliar de recursos humanos júnior", "cbo": "4110-10"},
    {"name": "Auxiliar de recursos humanos pleno", "cbo": "4110-10"},
    {"name": "Auxiliar de recursos humanos sênior", "cbo": "4110-10"},
    {"name": "Auxiliar de serviços gerais I", "cbo": "5143-20"},
    {"name": "Auxiliar de serviços gerais II", "cbo": "5143-20"},
    {"name": "Auxiliar de serviços gerais III", "cbo": "5143-20"},
    {"name": "Coordenador de vendas/caixa júnior", "cbo": "520110"},
    {"name": "Coordenador de vendas/caixa pleno", "cbo": "520110"},
    {"name": "Coordenador de vendas/caixa sênior", "cbo": "520110"},
    {"name": "Coordenador de vendas júnior", "cbo": "1423-20"},
    {"name": "Coordenador de vendas pleno", "cbo": "1423-20"},
    {"name": "Coordenador de vendas sênior", "cbo": "1423-20"},
    {"name": "Frentista I", "cbo": "5211-35"},
    {"name": "Frentista II", "cbo": "5211-35"},
    {"name": "Frentista III", "cbo": "5211-35"},
    {"name": "Frentista/caixa I", "cbo": "5211-35"},
    {"name": "Frentista/caixa II", "cbo": "5211-35"},
    {"name": "Frentista/caixa III", "cbo": "5211-35"},
    {"name": "Gerente administrativo", "cbo": "1421-05"},
    {"name": "Gerente comercial", "cbo": "1423-05"},
    {"name": "Gerente de compras", "cbo": "1424-05"},
    {"name": "Gerente financeiro", "cbo": "1421-15"},
    {"name": "Operador de caixa I", "cbo": "4211-25"},
    {"name": "Operador de caixa II", "cbo": "4211-25"},
    {"name": "Operador de caixa III", "cbo": "4211-25"},
    {"name": "Assistente de loja I", "cbo": "5211-40"},
    {"name": "Assistente de loja II", "cbo": "5211-40"},
    {"name": "Assistente de loja III", "cbo": "5211-40"},
    {"name": "Trocador de óleo/frentista I", "cbo": "9191-10"},
    {"name": "Trocador de óleo/frentista II", "cbo": "9191-10"},
    {"name": "Trocador de óleo/frentista III", "cbo": "9191-10"},
]


async def seed_functions():
    async with AsyncSession(engine) as session:
        for function_data in functions_seed:
            result = await session.exec(
                select(Functions).where(Functions.name == function_data["name"])
            )

            function = result.first()

            if not function:
                new_function = Functions(**function_data)

                session.add(new_function)

        await session.commit()
