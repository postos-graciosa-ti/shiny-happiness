from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config.database import engine
from src.models.users_subsidiaries import UsersSubsidiaries


async def seed_users_subsidiaries():
    users_subsidiaries = [
        UsersSubsidiaries(user_id=1, subsidiarie_id=1),
        UsersSubsidiaries(user_id=1, subsidiarie_id=2),
        UsersSubsidiaries(user_id=1, subsidiarie_id=3),
        UsersSubsidiaries(user_id=1, subsidiarie_id=4),
        UsersSubsidiaries(user_id=1, subsidiarie_id=5),
        UsersSubsidiaries(user_id=1, subsidiarie_id=6),
    ]

    async with AsyncSession(engine) as session:
        for us in users_subsidiaries:
            query = select(UsersSubsidiaries).where(
                UsersSubsidiaries.user_id == us.user_id,
                UsersSubsidiaries.subsidiarie_id == us.subsidiarie_id,
            )

            result = await session.exec(query)

            existing = result.first()

            if not existing:
                session.add(us)

        await session.commit()

        print(
            "Seed de users_subsidiaries concluída: usuário 1 associado a todas as filiais."
        )
