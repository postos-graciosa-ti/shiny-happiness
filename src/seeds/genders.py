from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config.database import engine
from src.models.genders import Genders

genders_seed = [
    {"name": "Masculino"},
    {"name": "Feminino"},
]


async def seed_genders():
    async with AsyncSession(engine) as session:
        for gender_data in genders_seed:
            result = await session.exec(
                select(Genders).where(Genders.name == gender_data["name"])
            )

            gender = result.first()

            if not gender:
                new_gender = Genders(**gender_data)

                session.add(new_gender)

        await session.commit()
