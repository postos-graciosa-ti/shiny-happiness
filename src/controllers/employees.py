import io
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import aiosmtplib
from decouple import config
from openpyxl import load_workbook
from sqlalchemy.orm import aliased
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config.database import engine
from src.helpers.handle_update_xlsx_rows import handle_update_xlsx_rows
from src.helpers.parse_dates import parse_dates
from src.helpers.set_checkbox import set_checkbox
from src.models.cities import Cities
from src.models.civil_status import CivilStatus
from src.models.cnh_categories import CnhCategories
from src.models.employees import Employees
from src.models.ethnicities import Ethnicities
from src.models.functions import Functions
from src.models.genders import Genders
from src.models.nationalities import Nationalities
from src.models.neighborhoods import Neighborhoods
from src.models.states import States
from src.models.subsidiaries import Subsidiaries
from src.schemas.employees import RowsListParams


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
        SMTP_HOST = config("SMTP_HOST")

        SMTP_PORT = config("SMTP_PORT")

        SMTP_USER = config("SMTP_USER")

        SMTP_PASS = config("SMTP_PASS")

        EMAIL_TO = config("EMAIL_TO")

        template_path = "src/assets/ficha_da_contabilidade.xlsx"

        wb = load_workbook(template_path)

        ws = wb.active

        ResidenceCity = aliased(Cities)

        BirthCity = aliased(Cities)

        BirthState = aliased(States)

        RgState = aliased(States)

        CtpsState = aliased(States)

        ResidenceState = aliased(States)

        query = (
            select(
                Employees,
                Subsidiaries,
                Genders,
                CivilStatus,
                Neighborhoods,
                ResidenceCity,
                Ethnicities,
                BirthCity,
                BirthState,
                Nationalities,
                RgState,
                CtpsState,
                CnhCategories,
                Functions,
                ResidenceState,
            )
            .join(Subsidiaries, Subsidiaries.id == Employees.subsidiarie_id)
            .join(Genders, Genders.id == Employees.gender_id)
            .join(CivilStatus, CivilStatus.id == Employees.civil_status_id)
            .join(Neighborhoods, Neighborhoods.id == Employees.neighborhood_id)
            .join(ResidenceCity, ResidenceCity.id == Employees.residence_city_id)
            .join(Ethnicities, Ethnicities.id == Employees.ethnicitie_id)
            .join(BirthCity, BirthCity.id == Employees.birthcity_id)
            .join(BirthState, BirthState.id == Employees.birthstate_id)
            .join(Nationalities, Nationalities.id == Employees.nationalitie_id)
            .join(RgState, RgState.id == Employees.rg_state_id)
            .join(CtpsState, CtpsState.id == Employees.ctps_state)
            .join(CnhCategories, CnhCategories.id == Employees.cnh_category_id)
            .join(Functions, Functions.id == Employees.function_id)
            .join(ResidenceState, ResidenceState.id == Employees.residence_state_id)
            .where(Employees.id == id)
        )

        result = await session.exec(query)

        (
            employee,
            employee_subsidiarie,
            employee_gender,
            employee_civil_status,
            employee_neighborhood,
            employee_residence_city,
            employee_ethnicitie,
            employee_birthcity,
            employee_birthstate,
            employee_nationalitie,
            employee_rg_state,
            employee_ctps_state,
            employee_cnh_category,
            employee_function,
            employee_residence_state,
        ) = result.first()

        rows_to_update = [
            RowsListParams(coord="H1", value=employee_subsidiarie.name),
            RowsListParams(coord="H4", value=employee.name),
            RowsListParams(coord="AA4", value=employee_gender.name),
            RowsListParams(coord="AI4", value=employee_civil_status.name),
            RowsListParams(coord="J6", value=employee.street),
            RowsListParams(coord="Y6", value=employee.street_number),
            RowsListParams(coord="H7", value=employee_neighborhood.name),
            RowsListParams(coord="X7", value=employee.cep),
            RowsListParams(coord="AD7", value=employee_residence_city.name),
            RowsListParams(coord="H9", value=employee.phone),
            RowsListParams(coord="O9", value=employee.mobile),
            RowsListParams(coord="Y9", value=employee.email),
            RowsListParams(coord="AL9", value=employee_ethnicitie.name),
            RowsListParams(coord="R10", value=employee_birthcity.name),
            RowsListParams(coord="AB10", value=employee_birthstate.name),
            RowsListParams(coord="AJ10", value=employee_nationalitie.name),
            RowsListParams(coord="H11", value=employee.mothername),
            RowsListParams(coord="AF11", value=employee.fathername),
            RowsListParams(coord="H17", value=employee.cpf),
            RowsListParams(coord="H18", value=employee.rg),
            RowsListParams(coord="R18", value=employee.rg_issuing_agency),
            RowsListParams(coord="X18", value=employee_rg_state.name),
            RowsListParams(coord="R22", value=employee_ctps_state.name),
            RowsListParams(coord="AA18", value=employee.rg_expedition_date),
            RowsListParams(coord="H19", value=employee.military_certificate),
            RowsListParams(coord="H20", value=employee.pis),
            RowsListParams(coord="W20", value=employee.pis_register_date),
            RowsListParams(coord="H21", value=employee.votant_title),
            RowsListParams(coord="R21", value=employee.votant_zone),
            RowsListParams(coord="Y21", value=employee.votant_session),
            RowsListParams(coord="H22", value=employee.ctps),
            RowsListParams(coord="M22", value=employee.ctps_serie),
            RowsListParams(coord="T23", value=employee_cnh_category.name),
            RowsListParams(coord="H30", value=employee_function.name),
            RowsListParams(coord="Y22", value=employee.ctps_emission_date),
            RowsListParams(coord="H23", value=employee.cnh),
            RowsListParams(coord="Z23", value=employee.cnh_emission_date),
            RowsListParams(coord="AI23", value=employee.cnh_validity_date),
            RowsListParams(coord="W30", value=employee.admission_date),
            RowsListParams(coord="AD30", value=employee.monthly_wage),
            RowsListParams(coord="AJ30", value=employee.hourly_wage),
            RowsListParams(coord="AL30", value=employee.pro_rated_hours),
            RowsListParams(coord="AJ6", value=employee.street_complement),
            RowsListParams(coord="AM7", value=employee_residence_state.name),
        ]

        await handle_update_xlsx_rows(ws, rows_to_update)

        set_checkbox(ws, "H25", "H26", employee.is_first_job)

        set_checkbox(ws, "O25", "O26", employee.already_has_been_employee)

        set_checkbox(ws, "W25", "W26", employee.trade_union_contribution_this_year)

        set_checkbox(ws, "AA25", "AA26", employee.receiving_unemployment_insurance)

        set_checkbox(ws, "AK25", "AK26", employee.has_previous_experience)

        set_checkbox(ws, "P32", "M32", employee.has_harmfull_exposition)

        set_checkbox(ws, "B35", "B36", employee.has_transport_voucher)

        if employee.has_transport_voucher:
            ws["G36"] = employee.daily_transport_units

        if employee.experience_time_id:
            ws["B39"] = "X"

            ws["F39"] = "X"

            ws["H41"] = "X"

        else:
            ws["B40"] = "X"

        set_checkbox(ws, "K44", "H44", employee.has_hazard_pay)

        set_checkbox(ws, "K45", "H45", employee.has_unhealthy_pay)

        if employee_subsidiarie.id == 1:
            ws["H46"] = "X"

        else:
            ws["K46"] = employee_subsidiarie.id

        file_stream = io.BytesIO()

        wb.save(file_stream)

        file_stream.seek(0)

        message = MIMEMultipart()

        message["From"] = SMTP_USER

        message["To"] = EMAIL_TO

        message["Subject"] = (
            f"Encaminhamento de documentos do colaborador {employee.name} para admissão"
        )

        message.attach(
            MIMEText(
                f"Segue em anexo os documentos do colaborador {employee.name} para admissão em {employee.admission_date}",
                "plain",
            )
        )

        file_name = f"ficha_da_contabilidade_{employee.name}.xlsx"

        part = MIMEApplication(file_stream.read(), Name=file_name)

        part["Content-Disposition"] = f'attachment; filename="{file_name}"'

        message.attach(part)

        try:
            await aiosmtplib.send(
                message,
                hostname=SMTP_HOST,
                port=int(SMTP_PORT),
                username=SMTP_USER,
                password=SMTP_PASS,
                start_tls=True,
            )

        except Exception as e:
            return {"error": f"Falha ao enviar email: {str(e)}"}

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
