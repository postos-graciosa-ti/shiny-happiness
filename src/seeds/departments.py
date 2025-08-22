from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config.database import engine
from src.models.departments import Departments

departments_seed = [
    {"name": "Administrativo"},
    {"name": "Serviços gerais"},
    {"name": "Vendas"},
]


async def seed_departments():
    async with AsyncSession(engine) as session:
        for department_data in departments_seed:
            result = await session.exec(
                select(Departments).where(Departments.name == department_data["name"])
            )

            department = result.first()

            if not department:
                new_department = Departments(**department_data)

                session.add(new_department)

        await session.commit()
