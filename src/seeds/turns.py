from datetime import time

from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config.database import engine
from src.models.turns import Turns

turns_seed = [
    {
        "name": "06:00/14:00 (manhã padrão)",
        "start_time": time(6, 0, 0, 0),
        "start_interval_time": time(10, 0, 0, 0),
        "end_interval_time": time(11, 0, 0, 0),
        "end_time": time(14, 0, 0, 0),
    },
    {
        "name": "06:00/15:00 (serviços gerais graciosa matriz)",
        "start_time": time(6, 0, 0, 0),
        "start_interval_time": time(0, 0, 0, 0),
        "end_interval_time": time(0, 0, 0, 0),
        "end_time": time(15, 0, 0, 0),
    },
    {
        "name": "08:00/14:15 (serviços gerais outras filiais)",
        "start_time": time(8, 0, 0, 0),
        "start_interval_time": time(10, 0, 0, 0),
        "end_interval_time": time(10, 15, 0, 0),
        "end_time": time(14, 15, 0, 0),
    },
    {
        "name": "08:00/18:00 (comercial I)",
        "start_time": time(8, 0, 0, 0),
        "start_interval_time": time(12, 0, 0, 0),
        "end_interval_time": time(14, 0, 0, 0),
        "end_time": time(18, 0, 0, 0),
        "exception": "Sábado 08:00/12:00",
    },
    {
        "name": "09:00/19:00 (comercial II)",
        "start_time": time(9, 0, 0, 0),
        "start_interval_time": time(12, 0, 0, 0),
        "end_interval_time": time(14, 0, 0, 0),
        "end_time": time(19, 0, 0, 0),
        "exception": "Terça-feira 08:00/12:00",
    },
    {
        "name": "09:00/19:00 (comercial III)",
        "start_time": time(9, 0, 0, 0),
        "start_interval_time": time(12, 0, 0, 0),
        "end_interval_time": time(14, 0, 0, 0),
        "end_time": time(19, 0, 0, 0),
        "exception": "Sábado 09:00/13:00",
    },
    {
        "name": "14:00/22:00 (tarde padrão)",
        "start_time": time(14, 0, 0, 0),
        "start_interval_time": time(17, 0, 0, 0),
        "end_interval_time": time(18, 0, 0, 0),
        "end_time": time(22, 0, 0, 0),
    },
    {
        "name": "18:00/02:00 (madrugada graciosa matriz I)",
        "start_time": time(18, 0, 0, 0),
        "start_interval_time": time(22, 0, 0, 0),
        "end_interval_time": time(23, 15, 0, 0),
        "end_time": time(2, 0, 0, 0),
    },
    {
        "name": "22:00/06:00 (madrugada graciosa matriz II)",
        "start_time": time(22, 0, 0, 0),
        "start_interval_time": time(2, 0, 0, 0),
        "end_interval_time": time(3, 15, 0, 0),
        "end_time": time(6, 0, 0, 0),
    },
    {
        "name": "07:30/17:30 (administrativo I)",
        "start_time": time(7, 30, 0, 0),
        "start_interval_time": time(12, 0, 0, 0),
        "end_interval_time": time(13, 30, 0, 0),
        "end_time": time(17, 30, 0, 0),
        "exception": "Sexta-feira 07:30/17:00",
    },
    {
        "name": "07:30/18:00 (administrativo II)",
        "start_time": time(7, 30, 0, 0),
        "start_interval_time": time(12, 0, 0, 0),
        "end_interval_time": time(13, 30, 0, 0),
        "end_time": time(18, 0, 0, 0),
        "exception": "Sexta-feira 07:30/17:00",
    },
    {
        "name": "06:00/14:00 (manhã Piraí)",
        "start_time": time(6, 0, 0, 0),
        "start_interval_time": time(12, 0, 0, 0),
        "end_interval_time": time(12, 15, 0, 0),
        "end_time": time(14, 0, 0, 0),
        "exception": "Domingo 13:00/19:00",
    },
    {
        "name": "14:00/22:00 (tarde Piraí)",
        "start_time": time(14, 0, 0, 0),
        "start_interval_time": time(17, 0, 0, 0),
        "end_interval_time": time(18, 0, 0, 0),
        "end_time": time(22, 0, 0, 0),
        "exception": "Domingo 13:00/19:00",
    },
]


async def seed_turns():
    async with AsyncSession(engine) as session:
        for turn_data in turns_seed:
            result = await session.exec(
                select(Turns).where(Turns.name == turn_data["name"])
            )

            turn = result.first()

            if not turn:
                new_turn = Turns(**turn_data)

                session.add(new_turn)

        await session.commit()
