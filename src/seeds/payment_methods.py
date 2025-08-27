from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config.database import engine
from src.models.payment_methods import PaymentMethods

payment_methods_seed = [
    {"name": "Dinheiro"},
    {"name": "Cheque"},
]


async def seed_payment_methods():
    async with AsyncSession(engine) as session:
        existing = await session.execute(select(PaymentMethods))

        if existing.scalars().first():
            return

        for method_data in payment_methods_seed:
            payment_method = PaymentMethods(**method_data)

            session.add(payment_method)

        await session.commit()
