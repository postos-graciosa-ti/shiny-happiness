# from datetime import date

# from sqlmodel import Field, SQLModel


# class Employees(SQLModel, table=True):
#     __tablename__ = "employees"
#     id: int | None = Field(default=None, primary_key=True)
#     name: str
#     tshirt_len: str
#     legs_len: str
#     feet_len: str
#     subsidiarie_id: int = Field(default=None, foreign_key="subsidiaries.id")
#     function_id: int = Field(default=None, foreign_key="functions.id")
#     turn_id: int = Field(default=None, foreign_key="turns.id")
#     admission_date: date
#     employee_status_id: int = Field(default=None, foreign_key="employee_status.id")
#     department_id: int = Field(default=None, foreign_key="departments.id")
#     sector_id: int = Field(default=None, foreign_key="sectors.id")
#     hierarchy_structure_id: int = Field(
#         default=None, foreign_key="hierarchy_structure.id"
#     )
#     gender_id: int = Field(default=None, foreign_key="genders.id")
#     has_previous_experience: bool
#     civil_status_id: int = Field(default=None, foreign_key="civil_status.id")
#     emergency_number: str
#     esocial: str
#     access_code: str
#     time_clock_code: str
#     street: str
#     street_number: str
#     cep: str
#     residence_city_id: int = Field(default=None, foreign_key="cities.id")
#     neighborhood_id: int = Field(default=None, foreign_key="neighborhoods.id")
#     phone: str
#     mobile: str
#     email: str
#     ethnicitie_id: int = Field(default=None, foreign_key="ethnicities.id")
#     datebirth: date
#     birthstate_id: int = Field(default=None, foreign_key="states.id")
#     birthcity_id: int = Field(default=None, foreign_key="cities.id")
#     mothername: str
#     fathername: str
#     cpf: str
#     rg: str
#     rg_issuing_agency: str
#     rg_state_id: int = Field(default=None, foreign_key="states.id")
#     rg_expedition_date: date
#     military_certificate: str
#     pis: str
#     pis_register_date: date
#     votant_title: str
#     votant_zone: str
#     votant_session: str
#     ctps: str
#     ctps_serie: str
#     ctps_state: int = Field(default=None, foreign_key="states.id")
#     ctps_emission_date: date
#     cnh: str
#     cnh_category_id: int = Field(default=None, foreign_key="cnh_categories.id")
#     cnh_emission_date: date
#     cnh_validity_date: date
#     is_first_job: bool
#     already_has_been_employee: bool
#     trade_union_contribution_this_year: bool
#     receiving_unemployment_insurance: bool
#     monthly_wage: str
#     hourly_wage: str
#     pro_rated_hours: str
#     has_transport_voucher: bool
#     daily_transport_units: str
#     weekly_transport_units: str
#     monthly_transport_units: str
#     experience_time_id: int = Field(default=None, foreign_key="experiences_times.id")
#     has_hazard_pay: bool
#     has_unhealthy_pay: bool
#     payment_method_id: int = Field(default=None, foreign_key="payment_methods.id")
#     bank_id: int = Field(default=None, foreign_key="banks.id")
#     bank_agency: str
#     bank_account: str
#     wage: str
#     wage_advance: str
#     has_harmful_agents: bool
#     health_insurance: str
#     life_insurance: str
#     ag: str
#     cc: str
#     has_harmfull_exposition: bool


from datetime import date
from typing import Any, Optional

from sqlalchemy import JSON, Column, LargeBinary
from sqlmodel import Field, SQLModel


class Employees(SQLModel, table=True):
    __tablename__ = "employees"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: Optional[str] = Field(default=None, nullable=True)
    tshirt_len: Optional[str] = Field(default=None, nullable=True)
    legs_len: Optional[str] = Field(default=None, nullable=True)
    feet_len: Optional[str] = Field(default=None, nullable=True)
    subsidiarie_id: Optional[int] = Field(
        default=None, foreign_key="subsidiaries.id", nullable=True
    )
    function_id: Optional[int] = Field(
        default=None, foreign_key="functions.id", nullable=True
    )
    turn_id: Optional[int] = Field(default=None, foreign_key="turns.id", nullable=True)
    admission_date: Optional[date] = Field(default=None, nullable=True)
    employee_status_id: Optional[int] = Field(
        default=None, foreign_key="employee_status.id", nullable=True
    )
    department_id: Optional[int] = Field(
        default=None, foreign_key="departments.id", nullable=True
    )
    sector_id: Optional[int] = Field(
        default=None, foreign_key="sectors.id", nullable=True
    )
    hierarchy_structure_id: Optional[int] = Field(
        default=None, foreign_key="hierarchy_structure.id", nullable=True
    )
    gender_id: Optional[int] = Field(
        default=None, foreign_key="genders.id", nullable=True
    )
    has_previous_experience: Optional[bool] = Field(default=None, nullable=True)
    civil_status_id: Optional[int] = Field(
        default=None, foreign_key="civil_status.id", nullable=True
    )
    emergency_number: Optional[str] = Field(default=None, nullable=True)
    esocial: Optional[str] = Field(default=None, nullable=True)
    access_code: Optional[str] = Field(default=None, nullable=True)
    time_clock_code: Optional[str] = Field(default=None, nullable=True)
    street: Optional[str] = Field(default=None, nullable=True)
    street_number: Optional[str] = Field(default=None, nullable=True)
    cep: Optional[str] = Field(default=None, nullable=True)
    residence_city_id: Optional[int] = Field(
        default=None, foreign_key="cities.id", nullable=True
    )
    neighborhood_id: Optional[int] = Field(
        default=None, foreign_key="neighborhoods.id", nullable=True
    )
    phone: Optional[str] = Field(default=None, nullable=True)
    mobile: Optional[str] = Field(default=None, nullable=True)
    email: Optional[str] = Field(default=None, nullable=True)
    ethnicitie_id: Optional[int] = Field(
        default=None, foreign_key="ethnicities.id", nullable=True
    )
    datebirth: Optional[date] = Field(default=None, nullable=True)
    birthstate_id: Optional[int] = Field(
        default=None, foreign_key="states.id", nullable=True
    )
    birthcity_id: Optional[int] = Field(
        default=None, foreign_key="cities.id", nullable=True
    )
    mothername: Optional[str] = Field(default=None, nullable=True)
    fathername: Optional[str] = Field(default=None, nullable=True)
    cpf: Optional[str] = Field(default=None, nullable=True)
    rg: Optional[str] = Field(default=None, nullable=True)
    rg_issuing_agency: Optional[str] = Field(default=None, nullable=True)
    rg_state_id: Optional[int] = Field(
        default=None, foreign_key="states.id", nullable=True
    )
    rg_expedition_date: Optional[date] = Field(default=None, nullable=True)
    military_certificate: Optional[str] = Field(default=None, nullable=True)
    pis: Optional[str] = Field(default=None, nullable=True)
    pis_register_date: Optional[date] = Field(default=None, nullable=True)
    votant_title: Optional[str] = Field(default=None, nullable=True)
    votant_zone: Optional[str] = Field(default=None, nullable=True)
    votant_session: Optional[str] = Field(default=None, nullable=True)
    ctps: Optional[str] = Field(default=None, nullable=True)
    ctps_serie: Optional[str] = Field(default=None, nullable=True)
    ctps_state: Optional[int] = Field(
        default=None, foreign_key="states.id", nullable=True
    )
    ctps_emission_date: Optional[date] = Field(default=None, nullable=True)
    cnh: Optional[str] = Field(default=None, nullable=True)
    cnh_category_id: Optional[int] = Field(
        default=None, foreign_key="cnh_categories.id", nullable=True
    )
    cnh_emission_date: Optional[date] = Field(default=None, nullable=True)
    cnh_validity_date: Optional[date] = Field(default=None, nullable=True)
    is_first_job: Optional[bool] = Field(default=None, nullable=True)
    already_has_been_employee: Optional[bool] = Field(default=None, nullable=True)
    trade_union_contribution_this_year: Optional[bool] = Field(
        default=None, nullable=True
    )
    receiving_unemployment_insurance: Optional[bool] = Field(
        default=None, nullable=True
    )
    monthly_wage: Optional[str] = Field(default=None, nullable=True)
    hourly_wage: Optional[str] = Field(default=None, nullable=True)
    pro_rated_hours: Optional[str] = Field(default=None, nullable=True)
    has_transport_voucher: Optional[bool] = Field(default=None, nullable=True)
    # daily_transport_units: Optional[str] = Field(default=None, nullable=True)
    # weekly_transport_units: Optional[str] = Field(default=None, nullable=True)
    # monthly_transport_units: Optional[str] = Field(default=None, nullable=True)
    experience_time_id: Optional[int] = Field(
        default=None, foreign_key="experiences_times.id", nullable=True
    )
    has_hazard_pay: Optional[bool] = Field(
        default=None, nullable=True
    )  # periculosidade
    has_unhealthy_pay: Optional[bool] = Field(
        default=None, nullable=True
    )  # insalubridade
    payment_method_id: Optional[int] = Field(
        default=None, foreign_key="payment_methods.id", nullable=True
    )
    bank_id: Optional[int] = Field(default=None, foreign_key="banks.id", nullable=True)
    bank_agency: Optional[str] = Field(default=None, nullable=True)
    bank_account: Optional[str] = Field(default=None, nullable=True)
    wage: Optional[str] = Field(default=None, nullable=True)
    wage_advance: Optional[str] = Field(default=None, nullable=True)
    health_insurance: Optional[str] = Field(default=None, nullable=True)
    life_insurance: Optional[str] = Field(default=None, nullable=True)
    ag: Optional[str] = Field(default=None, nullable=True)
    cc: Optional[str] = Field(default=None, nullable=True)
    has_harmfull_exposition: Optional[bool] = Field(default=None, nullable=True)
    nationalitie_id: Optional[int] = Field(
        default=None, foreign_key="nationalities.id", nullable=True
    )
    # drive_files_url: Optional[str] = Field(default=None, nullable=True)
    street_complement: Optional[str] = Field(default=None, nullable=True)
    residence_state_id: Optional[int] = Field(
        default=None, foreign_key="states.id", nullable=True
    )
    workdays_id: Optional[int] = Field(
        default=None, foreign_key="workdays.id", nullable=True
    )
    school_level_id: Optional[int] = Field(
        default=None, foreign_key="school_levels.id", nullable=True
    )
    parents: Optional[dict[str, Any]] = Field(
        sa_column=Column(JSON, nullable=True), default=None
    )
    ctps_file: Optional[bytes] = Field(
        sa_column=Column(LargeBinary, nullable=True), default=None
    )
    admission_health_exam_file: Optional[bytes] = Field(
        sa_column=Column(LargeBinary, nullable=True), default=None
    )
    identity_file: Optional[bytes] = Field(
        sa_column=Column(LargeBinary, nullable=True), default=None
    )
    cpf_file: Optional[bytes] = Field(
        sa_column=Column(LargeBinary, nullable=True), default=None
    )
    votant_title_file: Optional[bytes] = Field(
        sa_column=Column(LargeBinary, nullable=True), default=None
    )
    residence_proof: Optional[bytes] = Field(
        sa_column=Column(LargeBinary, nullable=True), default=None
    )
    cnh_file: Optional[bytes] = Field(
        sa_column=Column(LargeBinary, nullable=True), default=None
    )
    marriage_certificate_file: Optional[bytes] = Field(
        sa_column=Column(LargeBinary, nullable=True), default=None
    )
    military_certificate_file: Optional[bytes] = Field(
        sa_column=Column(LargeBinary, nullable=True), default=None
    )
