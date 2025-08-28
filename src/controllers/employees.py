import io
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import aiosmtplib
from decouple import config
from openpyxl import load_workbook
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config.database import engine
from src.helpers.parse_dates import parse_dates
from src.models.cities import Cities
from src.models.civil_status import CivilStatus
from src.models.cnh_categories import CnhCategories
from src.models.employees import Employees
from src.models.ethnicities import Ethnicities
from src.models.genders import Genders
from src.models.nationalities import Nationalities
from src.models.neighborhoods import Neighborhoods
from src.models.states import States
from src.models.subsidiaries import Subsidiaries


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


async def handle_post_send_employees_admission_to_contability(id: int):
    async with AsyncSession(engine) as session:
        employee_data = await session.get(Employees, id)

        employee_subsidiarie = await session.get(
            Subsidiaries, employee_data.subsidiarie_id
        )

        employee_gender = await session.get(Genders, employee_data.gender_id)

        employee_civil_status = await session.get(
            CivilStatus, employee_data.civil_status_id
        )

        employee_neighborhood = await session.get(
            Neighborhoods, employee_data.neighborhood_id
        )

        employee_residence_city = await session.get(
            Cities, employee_data.residence_city_id
        )

        employee_ethnicities = await session.get(
            Ethnicities, employee_data.ethnicitie_id
        )

        employee_birthcity = await session.get(Cities, employee_data.birthcity_id)

        employee_birthstate = await session.get(States, employee_data.birthstate_id)

        employee_nationalitie = await session.get(
            Nationalities, employee_data.nationalitie_id
        )

        employee_rg_state = await session.get(States, employee_data.rg_state_id)

        employee_ctps_state = await session.get(States, employee_data.ctps_state)

        employee_cnh_category = await session.get(
            CnhCategories, employee_data.cnh_category_id
        )

        SMTP_HOST = config("SMTP_HOST")

        SMTP_PORT = config("SMTP_PORT")

        SMTP_USER = config("SMTP_USER")

        SMTP_PASS = config("SMTP_PASS")

        EMAIL_TO = config("EMAIL_TO")

        template_path = "src/assets/ficha_da_contabilidade.xlsx"

        wb = load_workbook(template_path)

        ws = wb.active

        ws["H1"] = employee_subsidiarie.name

        ws["H4"] = employee_data.name

        ws["AA4"] = employee_gender.name

        ws["AI4"] = employee_civil_status.name

        ws["J6"] = employee_data.street

        ws["Y6"] = employee_data.street_number

        # ws["AJ6"] = employee_data complemento

        ws["H7"] = employee_neighborhood.name

        ws["X7"] = employee_data.cep

        ws["AD7"] = employee_residence_city.name

        # ws["AM"] = estado de residência

        ws["H9"] = employee_data.phone

        ws["O9"] = employee_data.mobile

        ws["Y9"] = employee_data.email

        ws["AL9"] = employee_ethnicities.name

        ws["H10"] = employee_birthcity.name

        ws["AB10"] = employee_birthstate.name

        ws["AJ10"] = employee_nationalitie.name

        ws["H11"] = employee_data.mothername

        ws["AF11"] = employee_data.fathername

        ws["H17"] = employee_data.cpf

        ws["H18"] = employee_data.rg

        ws["R18"] = employee_data.rg_issuing_agency

        ws["X18"] = employee_rg_state.name

        ws["AA18"] = employee_data.rg_expedition_date

        ws["H19"] = employee_data.military_certificate

        ws["H20"] = employee_data.pis

        ws["W20"] = employee_data.pis_register_date

        ws["H21"] = employee_data.votant_title

        ws["R21"] = employee_data.votant_zone

        ws["Y21"] = employee_data.votant_session

        ws["H22"] = employee_data.ctps

        ws["M22"] = employee_data.ctps_serie

        ws["R22"] = employee_ctps_state.name

        ws["Y22"] = employee_data.ctps_emission_date

        ws["H23"] = employee_data.cnh

        ws["T23"] = employee_cnh_category.name

        ws["Z23"] = employee_data.cnh_emission_date

        ws["AI23"] = employee_data.cnh_validity_date

        if (
            employee_data.is_first_job is not None
            and employee_data.is_first_job == False  # noqa: E712
        ):
            ws["H26"] = "X"
        else:
            ws["H25"] = "X"

        if (
            employee_data.already_has_been_employee is not None
            and employee_data.already_has_been_employee == False  # noqa: E712
        ):
            ws["O26"] = "X"
        else:
            ws["O25"] = "X"

        if (
            employee_data.trade_union_contribution_this_year is not None
            and employee_data.trade_union_contribution_this_year == False  # noqa: E712
        ):
            ws["W26"] = "X"
        else:
            ws["25"] = "X"

        if (
            employee_data.receiving_unemployment_insurance is not None
            and employee_data.receiving_unemployment_insurance == False  # noqa: E712
        ):
            ws["AA26"] = "X"
        else:
            ws["AA25"]

        if (
            employee_data.has_previous_experience is not None
            and employee_data.has_previous_experience == False  # noqa: E712
        ):
            ws["AK26"] = "X"
        else:
            ws["AK25"] = "X"

        file_stream = io.BytesIO()

        wb.save(file_stream)

        file_stream.seek(0)

        message = MIMEMultipart()

        message["From"] = SMTP_USER

        message["To"] = EMAIL_TO

        message["Subject"] = (
            f"Encaminhamento de documentos do colaborador {employee_data.name} para admissão"
        )

        message.attach(
            MIMEText(
                f"Segue em anexo os documentos do colaborador {employee_data.name} para admissão com data para {employee_data.admission_date}",
                "plain",
            )
        )

        file_name = f"ficha_da_contabilidade_{employee_data.name}.xlsx"

        part = MIMEApplication(file_stream.read(), Name=file_name)

        part["Content-Disposition"] = f'attachment; filename="{file_name}"'

        message.attach(part)

        await aiosmtplib.send(
            message,
            hostname=SMTP_HOST,
            port=SMTP_PORT,
            username=SMTP_USER,
            password=SMTP_PASS,
            start_tls=True,
        )

        return {"status": "Email enviado com sucesso"}


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
