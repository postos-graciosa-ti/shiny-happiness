from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config.database import engine
from src.models.departments import Departments


async def handle_get_departments():
    async with AsyncSession(engine) as session:
        statement = select(Departments)

        result = await session.exec(statement)

        departments = result.all()

        return departments
