from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config.database import engine
from src.models.civil_status import CivilStatus


async def handle_get_civil_status():
    async with AsyncSession(engine) as session:
        result = await session.exec(select(CivilStatus))

        civil_status = result.all()

        return civil_status
