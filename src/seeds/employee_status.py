from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config.database import engine
from src.models.employee_status import EmployeeStatus

employee_status_seed = [
    {"name": "Ativo"},
    {"name": "Inativo"},
    {"name": "Afastado"},
]


async def seed_employee_status():
    async with AsyncSession(engine) as session:
        for status_data in employee_status_seed:
            result = await session.exec(
                select(EmployeeStatus).where(EmployeeStatus.name == status_data["name"])
            )

            status = result.first()

            if not status:
                new_status = EmployeeStatus(**status_data)

                session.add(new_status)

        await session.commit()
