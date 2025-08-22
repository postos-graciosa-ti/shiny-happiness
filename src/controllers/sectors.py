from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config.database import engine
from src.models.sectors import Sectors


async def handle_get_sectors():
    async with AsyncSession(engine) as session:
        query = select(Sectors)

        result = await session.exec(query)

        sectors = result.all()

        return sectors
