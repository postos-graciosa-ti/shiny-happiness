from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config.database import engine
from src.models.banks import Banks

banks_seed = [
    {"name": "Banco do Brasil"},
]


async def seed_banks():
    async with AsyncSession(engine) as session:
        for bank_data in banks_seed:
            result = await session.exec(
                select(Banks).where(Banks.name == bank_data["name"])
            )

            existing = result.first()

            if not existing:
                session.add(Banks(**bank_data))

        await session.commit()
