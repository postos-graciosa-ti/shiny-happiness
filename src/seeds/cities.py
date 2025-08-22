from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config.database import engine
from src.models.cities import Cities

cities_seed = [
    {"name": "Joinville"},
    {"name": "Florianópolis"},
]


async def seed_cities():
    async with AsyncSession(engine) as session:
        for city_data in cities_seed:
            result = await session.exec(
                select(Cities).where(Cities.name == city_data["name"])
            )

            city = result.first()

            if not city:
                new_city = Cities(**city_data)

                session.add(new_city)

        await session.commit()
