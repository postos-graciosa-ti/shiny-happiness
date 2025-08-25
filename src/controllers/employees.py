from datetime import datetime

from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config.database import engine
from src.helpers.parse_dates import parse_dates
from src.models.employees import Employees


async def handle_get_employees_by_subsidiarie(id: int):
    async with AsyncSession(engine) as session:
        result = await session.exec(
            select(Employees).where(Employees.subsidiarie_id == id)
        )

        employees = result.all()

        return employees


async def handle_post_employees(employee: Employees):
    parse_dates(employee)

    async with AsyncSession(engine) as session:
        session.add(employee)

        try:
            await session.commit()

            await session.refresh(employee)

            return employee

        except Exception as e:
            await session.rollback()

            raise e


# NOTE: possível melhoria: só alterar o registro se for diferente do que está no banco real
# NOTE: testar primeiro, se falhar, implantar melhoria
async def handle_patch_employees(id: int, employee: Employees):
    if isinstance(employee.admission_date, str):
        employee.admission_date = datetime.strptime(
            employee.admission_date, "%Y-%m-%d"
        ).date()

    elif isinstance(employee.admission_date, datetime):
        employee.admission_date = employee.admission_date.date()

    async with AsyncSession(engine) as session:
        query = select(Employees).where(Employees.id == id)

        result = await session.exec(query)

        db_employee = result.first()

        if not db_employee:
            return None

        for key, value in employee.dict(exclude_unset=True).items():
            setattr(db_employee, key, value)

        session.add(db_employee)

        await session.commit()

        await session.refresh(db_employee)

        return db_employee


# NOTE: depois employee.id vai ser chave estrangeira em outras tabelas
# NOTE: aí precisa mudar para delete on cascade
async def handle_delete_employees(id: int):
    async with AsyncSession(engine) as session:
        query = select(Employees).where(Employees.id == id)

        result = await session.exec(query)

        db_employee = result.first()

        if not db_employee:
            return None

        await session.delete(db_employee)

        await session.commit()

        return {"success": True}
