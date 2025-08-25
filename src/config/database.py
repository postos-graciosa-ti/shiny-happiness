from decouple import config
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import SQLModel

from src.migrations.watch import watch
from src.models.cities import Cities
from src.models.civil_status import CivilStatus
from src.models.departments import Departments
from src.models.employee_status import EmployeeStatus
from src.models.employees import Employees
from src.models.ethnicities import Ethnicities
from src.models.functions import Functions
from src.models.genders import Genders
from src.models.hierarchy_structure import HierarchyStructure
from src.models.neighborhoods import Neighborhoods
from src.models.sectors import Sectors
from src.models.states import States
from src.models.subsidiaries import Subsidiaries
from src.models.turns import Turns
from src.models.users import Users
from src.models.users_subsidiaries import UsersSubsidiaries

database_url = config("DATABASE_URL")

engine = create_async_engine(
    database_url,
    echo=True,
    connect_args={"check_same_thread": False},
)


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

        await watch(
            engine,
            [
                Users,
                Subsidiaries,
                UsersSubsidiaries,
                Employees,
                Sectors,
                Departments,
                HierarchyStructure,
                Functions,
                Turns,
                EmployeeStatus,
                Genders,
                CivilStatus,
                Cities,
                Neighborhoods,
                Ethnicities,
                States,
            ],
            use_identity=False,
        )
