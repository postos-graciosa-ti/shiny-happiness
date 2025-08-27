from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config.database import engine
from src.models.experiences_times import ExperiencesTimes

experiences_times_seed = [
    {"name": "1° período: 30 dias, 2° período: 60 dias"},
    {"name": "Sem tempo de experiência"},
]


async def seed_experiences_times():
    async with AsyncSession(engine) as session:
        for data in experiences_times_seed:
            query = select(ExperiencesTimes).where(
                ExperiencesTimes.name == data["name"]
            )

            result = await session.execute(query)

            exists = result.scalar_one_or_none()

            if not exists:
                experience_time = ExperiencesTimes(**data)

                session.add(experience_time)

        try:
            await session.commit()

        except Exception as e:
            await session.rollback()

            raise e
