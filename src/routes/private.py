from src.routes.cities import cities_routes
from src.routes.civil_status import civil_status_routes
from src.routes.departments import departments_routes
from src.routes.employee_status import employee_status_routes
from src.routes.employees import employees_routes
from src.routes.ethnicities import ethnicities_routes
from src.routes.functions import functions_routes
from src.routes.genders import genders_routes
from src.routes.hierarchy_structure import hierarchy_structure_routes
from src.routes.neighborhoods import neighborhoods_routes
from src.routes.sectors import sectors_routes
from src.routes.states import states_routes
from src.routes.turns import turns_routes

private = [
    employees_routes,
    functions_routes,
    turns_routes,
    employee_status_routes,
    departments_routes,
    sectors_routes,
    hierarchy_structure_routes,
    genders_routes,
    civil_status_routes,
    cities_routes,
    neighborhoods_routes,
    ethnicities_routes,
    states_routes,
]
