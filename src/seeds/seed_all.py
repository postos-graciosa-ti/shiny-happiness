from src.seeds.cities import seed_cities
from src.seeds.civil_status import seed_civil_status
from src.seeds.departments import seed_departments
from src.seeds.employee_status import seed_employee_status
from src.seeds.ethnicities import seed_ethnicities
from src.seeds.functions import seed_functions
from src.seeds.genders import seed_genders
from src.seeds.hierarchy_structure import seed_hierarchy_structure
from src.seeds.neighborhoods import seed_neighborhoods
from src.seeds.sectors import seed_sectors
from src.seeds.states import seed_states
from src.seeds.subsidiaries import seed_subsidiaries
from src.seeds.turns import seed_turns
from src.seeds.users import seed_users
from src.seeds.users_subsidiaries import seed_users_subsidiaries


async def seed_all():
    await seed_users()

    await seed_subsidiaries()

    await seed_users_subsidiaries()

    await seed_sectors()

    await seed_departments()

    await seed_hierarchy_structure()

    await seed_functions()

    await seed_turns()

    await seed_employee_status()

    await seed_genders()

    await seed_civil_status()

    await seed_cities()

    await seed_neighborhoods()

    await seed_ethnicities()

    await seed_states()
