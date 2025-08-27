from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config.database import engine
from src.models.payment_methods import PaymentMethods


async def handle_get_payment_methods():
    async with AsyncSession(engine) as session:
        result = await session.execute(select(PaymentMethods))

        payment_methods = result.scalars().all()

        return payment_methods
