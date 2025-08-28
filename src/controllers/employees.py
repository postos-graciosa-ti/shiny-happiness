import base64

from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config.database import engine
from src.helpers.decode_pdf_fields import decode_pdf_fields
from src.helpers.encode_pdf_fields import encode_pdf_fields
from src.helpers.ensure_pdf import ensure_pdf
from src.helpers.get_binary_fields import get_binary_fields
from src.helpers.parse_dates import parse_dates
from src.models.employees import Employees


async def handle_get_employees_by_subsidiarie(id: int):
    async with AsyncSession(engine) as session:
        result = await session.exec(
            select(Employees).where(Employees.subsidiarie_id == id)
        )

        employees = result.all()

        return [encode_pdf_fields(emp) for emp in employees]


async def handle_post_employees(employee: Employees):
    parse_dates(employee)

    decode_pdf_fields(employee)

    for field in get_binary_fields():
        file_bytes = getattr(employee, field, None)

        if isinstance(file_bytes, bytes):
            setattr(employee, field, ensure_pdf(file_bytes, f"{field}.pdf"))

    async with AsyncSession(engine) as session:
        session.add(employee)

        try:
            await session.commit()

            await session.refresh(employee)

            return encode_pdf_fields(employee)

        except Exception as e:
            await session.rollback()

            raise e


# NOTE: possível melhoria: só alterar o registro se for diferente do que está no banco real
# NOTE: testar primeiro, se falhar, implantar melhoria
async def handle_patch_employees(id: int, employee: Employees):
    parse_dates(employee)

    async with AsyncSession(engine) as session:
        query = select(Employees).where(Employees.id == id)

        result = await session.exec(query)

        db_employee = result.first()

        if not db_employee:
            return None

        for key, value in employee.dict(exclude_unset=True).items():
            if key in get_binary_fields():
                if isinstance(value, str):
                    try:
                        value = base64.b64decode(value)

                    except Exception as e:
                        raise ValueError(
                            f"Erro ao decodificar arquivo do campo {key}"
                        ) from e

                value = ensure_pdf(value, f"{key}.pdf")

            setattr(db_employee, key, value)

        session.add(db_employee)

        await session.commit()

        await session.refresh(db_employee)

        return encode_pdf_fields(db_employee)


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
