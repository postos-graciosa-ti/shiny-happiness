from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config.database import engine
from src.models.states import States


async def handle_get_states():
    async with AsyncSession(engine) as session:
        result = await session.exec(select(States))

        states = result.all()

        return states
