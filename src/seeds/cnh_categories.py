from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config.database import engine
from src.models.cnh_categories import CnhCategories

cnh_categories_seed = [
    {"name": "A"},
    {"name": "B"},
    {"name": "AB"},
    {"name": "C"},
    {"name": "D"},
    {"name": "E"},
    {"name": "ACC"},
]


async def seed_cnh_categories():
    async with AsyncSession(engine) as session:
        for category in cnh_categories_seed:
            exists = await session.exec(
                select(CnhCategories).where(CnhCategories.name == category["name"])
            )

            if not exists.first():
                session.add(CnhCategories(**category))

        await session.commit()
