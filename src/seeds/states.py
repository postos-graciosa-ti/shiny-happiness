from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config.database import engine
from src.models.states import States

states_seed = [
    {"name": "Santa Catarina"},
]


async def seed_states():
    async with AsyncSession(engine) as session:
        for state_data in states_seed:
            result = await session.exec(
                select(States).where(States.name == state_data["name"])
            )

            existing = result.first()

            if not existing:
                session.add(States(**state_data))

        await session.commit()
