from datetime import date

from sqlmodel import Field, SQLModel


class Employees(SQLModel, table=True):
    __tablename__ = "employees"
    id: int | None = Field(default=None, primary_key=True)
    name: str
    tshirt_len: str
    legs_len: str
    feet_len: str
    subsidiarie_id: int = Field(default=None, foreign_key="subsidiaries.id")
    function_id: int = Field(default=None, foreign_key="functions.id")
    turn_id: int = Field(default=None, foreign_key="turns.id")
    admission_date: date
    employee_status_id: int = Field(default=None, foreign_key="employee_status.id")
    department_id: int = Field(default=None, foreign_key="departments.id")
    sector_id: int = Field(default=None, foreign_key="sectors.id")
    hierarchy_structure_id: int = Field(
        default=None, foreign_key="hierarchy_structure.id"
    )
    gender_id: int = Field(default=None, foreign_key="genders.id")
    has_previous_experience: bool
    civil_status_id: int = Field(default=None, foreign_key="civil_status.id")
    emergency_number: str
    esocial: str
    access_code: str
    time_clock_code: str
    street: str
    street_number: str
    cep: str
    residence_city_id: int = Field(default=None, foreign_key="cities.id")
    neighborhood_id: int = Field(default=None, foreign_key="neighborhoods.id")
    phone: str
    mobile: str
    email: str
    ethnicitie_id: int = Field(default=None, foreign_key="ethnicities.id")
    datebirth: date
    birthstate_id: int = Field(default=None, foreign_key="states.id")
    birthcity_id: int = Field(default=None, foreign_key="cities.id")
    mothername: str
    fathername: str
    cpf: str
    rg: str
    rg_issuing_agency: str
    rg_state_id: int = Field(default=None, foreign_key="states.id")
    rg_expedition_date: date
    military_certificate: str
    pis: str
    pis_register_date: date
    votant_title: str
    votant_zone: str
    votant_session: str
    ctps: str
    ctps_serie: str
    ctps_state: int = Field(default=None, foreign_key="states.id")
    ctps_emission_date: date
    cnh: str
