from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.models.workdays import Workdays
from src.config.database import engine


async def handle_get_workdays():
    async with AsyncSession(engine) as session:
        result = await session.exec(select(Workdays))

        turns = result.all()

        return turns
