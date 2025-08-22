from decouple import config
from passlib.hash import sha256_crypt
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config.database import engine
from src.models.users import Users

users_seed = [
    {
        "login": "administrador@postos-graciosa-sgi.com",
        "password": sha256_crypt.hash(config("DEFAULT_PWD")),
        "name": "Administrador",
        "email": "postosgraciosati@gmail.com",
    }
]


async def seed_users():
    async with AsyncSession(engine) as session:
        for user_data in users_seed:
            result = await session.exec(
                select(Users).where(Users.login == user_data["login"])
            )

            user = result.first()

            if user:
                updated = False

                for key, value in user_data.items():
                    if not getattr(user, key, None):
                        setattr(user, key, value)

                        updated = True

                if updated:
                    session.add(user)

            else:
                new_user = Users(**user_data)

                session.add(new_user)

        await session.commit()
