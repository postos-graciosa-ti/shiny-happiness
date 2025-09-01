from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config.database import engine
from src.models.school_levels import SchoolLevels

school_levels_seed = [
    {"name": "Analfabeto"},
    {"name": "1° grau incompleto"},
    {"name": "2° grau incompleto"},
    {"name": "1° grau completo"},
    {"name": "2° grau completo"},
    {"name": "Superior"},
    {"name": "Superior cursando"},
]


async def seed_school_levels():
    async with AsyncSession(engine) as session:
        for level_data in school_levels_seed:
            result = await session.exec(
                select(SchoolLevels).where(SchoolLevels.name == level_data["name"])
            )

            level = result.first()

            if not level:
                new_level = SchoolLevels(**level_data)

                session.add(new_level)

        await session.commit()
