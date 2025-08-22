from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config.database import engine
from src.models.employee_status import EmployeeStatus


async def handle_get_employee_status():
    async with AsyncSession(engine) as session:
        result = await session.exec(select(EmployeeStatus))

        employee_status = result.all()

        return employee_status
