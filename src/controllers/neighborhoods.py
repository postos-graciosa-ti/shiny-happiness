from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config.database import engine
from src.models.neighborhoods import Neighborhoods


async def handle_get_neighborhoods():
    async with AsyncSession(engine) as session:
        query = select(Neighborhoods)

        result = await session.exec(query)

        neighborhoods = result.all()

        return neighborhoods


async def handle_get_neighborhoods_by_id(id: int):
    async with AsyncSession(engine) as session:
        query = select(Neighborhoods).where(Neighborhoods.id == id)

        result = await session.exec(query)

        neighborhoods = result.first()

        return neighborhoods


async def handle_post_neighborhoods(neighborhood: Neighborhoods):
    async with AsyncSession(engine) as session:
        session.add(neighborhood)

        await session.commit()

        await session.refresh(neighborhood)

        return neighborhood
