from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config.database import engine
from src.models.banks import Banks


async def handle_get_banks():
    async with AsyncSession(engine) as session:
        result = await session.execute(select(Banks))

        banks = result.scalars().all()

        return banks
