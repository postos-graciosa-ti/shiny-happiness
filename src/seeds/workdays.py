from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config.database import engine
from src.models.workdays import Workdays

workdays_seed = [
    {"name": "Segunda a Sexta-feira"},
    {"name": "Sábado"},
    {"name": "Segunda a Domingo"},
]


async def seed_workdays():
    async with AsyncSession(engine) as session:
        for workday_data in workdays_seed:
            result = await session.exec(
                select(Workdays).where(Workdays.name == workday_data["name"])
            )

            workday = result.first()

            if not workday:
                new_workday = Workdays(**workday_data)

                session.add(new_workday)

        await session.commit()
