from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config.database import engine
from src.models.civil_status import CivilStatus

civil_status_seed = [
    {"name": "Solteiro"},
    {"name": "Casado"},
    {"name": "Divorciado"},
    {"name": "Viúvo"},
    {"name": "Separado"},
    {"name": "União Estável"},
]


async def seed_civil_status():
    async with AsyncSession(engine) as session:
        for civil_status_data in civil_status_seed:
            result = await session.exec(
                select(CivilStatus).where(CivilStatus.name == civil_status_data["name"])
            )

            civil_status = result.first()

            if not civil_status:
                new_civil_status = CivilStatus(**civil_status_data)

                session.add(new_civil_status)

        await session.commit()
