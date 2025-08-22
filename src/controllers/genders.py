from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config.database import engine
from src.models.genders import Genders


async def handle_get_genders():
    async with AsyncSession(engine) as session:
        query = select(Genders)

        result = await session.exec(query)

        genders = result.all()

        return genders
