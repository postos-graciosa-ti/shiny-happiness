from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config.database import engine
from src.models.functions import Functions


async def handle_get_functions_by_subsidiarie():
    async with AsyncSession(engine) as session:
        query = select(Functions)

        result = await session.exec(query)

        return result.all()


async def handle_get_functions_by_id(id: int):
    async with AsyncSession(engine) as session:
        query = select(Functions).where(Functions.id == id)

        result = await session.exec(query)

        return result.first()


async def handle_post_functions(function: Functions):
    async with AsyncSession(engine) as session:
        session.add(function)

        await session.commit()

        await session.refresh(function)

        return function
