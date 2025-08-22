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
