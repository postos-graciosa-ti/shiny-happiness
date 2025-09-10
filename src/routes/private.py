from src.routes.banks import banks_routes
from src.routes.cities import cities_routes
from src.routes.civil_status import civil_status_routes
from src.routes.cnh_categories import cnh_categories_routes
from src.routes.departments import departments_routes
from src.routes.employee_status import employee_status_routes
from src.routes.employees import employees_routes
from src.routes.ethnicities import ethnicities_routes
from src.routes.experiences_times import experiences_times_routes
from src.routes.functions import functions_routes
from src.routes.genders import genders_routes
from src.routes.hierarchy_structure import hierarchy_structure_routes
from src.routes.nationalities import nationalities_routes
from src.routes.neighborhoods import neighborhoods_routes
from src.routes.payment_methods import payment_methods_routes
from src.routes.sales_report import sales_report_routes
from src.routes.school_levels import school_levels_routes
from src.routes.sectors import sectors_routes
from src.routes.states import states_routes
from src.routes.turns import turns_routes
from src.routes.workdays import workdays_routes

private = [
    sales_report_routes,
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
    cnh_categories_routes,
    experiences_times_routes,
    payment_methods_routes,
    banks_routes,
    nationalities_routes,
    workdays_routes,
    school_levels_routes,
]
