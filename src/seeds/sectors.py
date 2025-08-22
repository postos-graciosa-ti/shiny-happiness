from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config.database import engine
from src.models.sectors import Sectors

sectors_seed = [
    {"name": "Administrativo"},
    {"name": "Recursos humanos"},
    {"name": "Compras"},
    {"name": "Serviços gerais"},
    {"name": "Loja de conveniência"},
    {"name": "Pista"},
    {"name": "Comercial"},
    {"name": "Financeiro"},
]


async def seed_sectors():
    async with AsyncSession(engine) as session:
        for sector_data in sectors_seed:
            result = await session.exec(
                select(Sectors).where(Sectors.name == sector_data["name"])
            )

            sector = result.first()

            if not sector:
                new_sector = Sectors(**sector_data)

                session.add(new_sector)

        await session.commit()
