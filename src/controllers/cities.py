from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config.database import engine
from src.models.cities import Cities


async def handle_get_cities():
    async with AsyncSession(engine) as session:
        query = select(Cities)

        result = await session.exec(query)

        cities = result.all()

        return cities


async def handle_post_cities(city: Cities):
    async with AsyncSession(engine) as session:
        session.add(city)

        await session.commit()

        await session.refresh(city)

        return city
