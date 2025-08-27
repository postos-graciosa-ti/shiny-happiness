from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config.database import engine
from src.models.nationalities import Nationalities


async def handle_get_nationalities():
    async with AsyncSession(engine) as session:
        result = await session.execute(select(Nationalities))

        nationalities = result.scalars().all()

        return nationalities


async def handle_post_nationalities(nationality: Nationalities):
    async with AsyncSession(engine) as session:
        session.add(nationality)

        try:
            await session.commit()

            await session.refresh(nationality)

            return nationality

        except Exception as e:
            await session.rollback()

            raise e
