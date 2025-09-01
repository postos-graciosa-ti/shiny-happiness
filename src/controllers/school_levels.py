from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config.database import engine
from src.models.school_levels import SchoolLevels


async def handle_get_school_levels():
    async with AsyncSession(engine) as session:
        result = await session.exec(select(SchoolLevels))

        turns = result.all()

        return turns
