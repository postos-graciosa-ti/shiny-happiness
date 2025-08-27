from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config.database import engine
from src.models.nationalities import Nationalities

nationalities_seed = [
    {"name": "Brasileiro"},
    {"name": "Venezuelano"},
]


async def seed_nationalities():
    async with AsyncSession(engine) as session:
        for nationality in nationalities_seed:
            exists = await session.execute(
                select(Nationalities).where(Nationalities.name == nationality["name"])
            )

            if not exists.scalar_one_or_none():
                session.add(Nationalities(**nationality))

        await session.commit()
