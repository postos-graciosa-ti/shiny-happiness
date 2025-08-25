from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config.database import engine
from src.models.ethnicities import Ethnicities


async def handle_get_ethnicities():
    async with AsyncSession(engine) as session:
        result = await session.exec(select(Ethnicities))

        return result.all()
