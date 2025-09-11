from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config.database import engine
from src.models.turns import Turns


async def handle_get_turns():
    async with AsyncSession(engine) as session:
        result = await session.exec(select(Turns))

        turns = result.all()

        return turns


async def handle_get_turns_by_id(id: int):
    async with AsyncSession(engine) as session:
        query = select(Turns).where(Turns.id == id)

        result = await session.exec(query)

        return result.first()
