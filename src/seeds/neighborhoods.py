from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config.database import engine
from src.models.neighborhoods import Neighborhoods

neighborhoods_seed = [
    {"name": "Centro"},
    {"name": "Atiradores"},
    {"name": "Trindade"},
    {"name": "Coqueiros"},
]


async def seed_neighborhoods():
    async with AsyncSession(engine) as session:
        for neighborhood_data in neighborhoods_seed:
            result = await session.exec(
                select(Neighborhoods).where(
                    Neighborhoods.name == neighborhood_data["name"]
                )
            )

            neighborhood = result.first()

            if not neighborhood:
                new_neighborhood = Neighborhoods(**neighborhood_data)

                session.add(new_neighborhood)

        await session.commit()
