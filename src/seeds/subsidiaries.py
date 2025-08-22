from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config.database import engine
from src.models.subsidiaries import Subsidiaries


async def seed_subsidiaries():
    subsidiaries_to_seed = [
        {
            "name": "Posto Graciosa",
            "cnpj": "76.608.660/0001-11",
            "address": "R. Florianópolis, 510 – Itaum, Joinville – SC, 89207-000",
            "phone": "(47) 3436-0030",
            "ie": "251.006.042",
        },
        {
            "name": "Auto Posto Fátima",
            "cnpj": "79.270.211/0001-02",
            "address": "R. Fátima, 1730 – Fátima, Joinville – SC, 89229-102",
            "phone": "(47) 3466-0248",
            "ie": "251.297.373",
        },
        {
            "name": "Posto Bemer",
            "cnpj": "81.512.683/0001-68",
            "address": "R. Boehmerwald, 675 – Boehmerwald, Joinville – SC, 89232-485",
            "phone": "(47) 3465-0328",
            "ie": "252.073.924",
        },
        {
            "name": "Posto Jariva",
            "cnpj": "04.123.127/0001-59",
            "address": "R. Monsenhor Gercino, 5085 – Jarivatuba, Joinville – SC, 89230-290",
            "phone": "(47) 3466-4665",
            "ie": "254.220.738",
        },
        {
            "name": "Posto Graciosa V",
            "cnpj": "84.708.437/0006-89",
            "address": "R. Santa Catarina, 1870 – Floresta, Joinville – SC, 89212-000",
            "phone": "(47) 3436-1763",
            "ie": "250.205.572",
        },
        {
            "name": "Auto Posto Pirai",
            "cnpj": "11.168.652/0001-56",
            "address": "R. Quinze de Novembro, 5031 – Vila Nova, Joinville – SC, 89237-000",
            "phone": "(47) 3422-9676",
            "ie": "255.947.267",
        },
    ]

    async with AsyncSession(engine) as session:
        for data in subsidiaries_to_seed:
            result = await session.execute(
                select(Subsidiaries).where(Subsidiaries.cnpj == data["cnpj"])
            )

            db_subsidiary = result.scalar_one_or_none()

            if not db_subsidiary:
                subsidiary = Subsidiaries(**data)

                session.add(subsidiary)

            else:
                updated = False

                for field, value in data.items():
                    current_value = getattr(db_subsidiary, field, None)

                    if current_value in [None, ""] and value not in [None, ""]:
                        setattr(db_subsidiary, field, value)

                        updated = True

                if updated:
                    session.add(db_subsidiary)

        await session.commit()
