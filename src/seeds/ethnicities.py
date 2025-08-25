from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config.database import engine
from src.models.ethnicities import Ethnicities

ethnicities_seed = [
    {"name": "Branca"},
    {"name": "Preta"},
    {"name": "Parda"},
    {"name": "Amarela"},
    {"name": "Indígena"},
]


async def seed_ethnicities():
    async with AsyncSession(engine) as session:
        for ethnicity_data in ethnicities_seed:
            result = await session.exec(
                select(Ethnicities).where(Ethnicities.name == ethnicity_data["name"])
            )

            existing = result.first()

            if not existing:
                session.add(Ethnicities(**ethnicity_data))

        await session.commit()
