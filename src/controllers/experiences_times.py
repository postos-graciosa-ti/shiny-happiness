from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config.database import engine
from src.models.experiences_times import ExperiencesTimes


async def handle_get_experiences_times():
    async with AsyncSession(engine) as session:
        result = await session.execute(select(ExperiencesTimes))

        experiences_times = result.scalars().all()

        return experiences_times
