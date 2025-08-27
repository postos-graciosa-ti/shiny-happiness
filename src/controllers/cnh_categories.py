from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config.database import engine
from src.models.cnh_categories import CnhCategories


async def handle_get_cnh_categories():
    async with AsyncSession(engine) as session:
        result = await session.exec(select(CnhCategories))

        return result.all()
