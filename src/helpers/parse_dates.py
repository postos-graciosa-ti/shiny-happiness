from datetime import date, datetime
from typing import Union, get_args, get_origin

from sqlmodel import SQLModel


def parse_dates(obj: SQLModel):
    for field_name, field_type in obj.__annotations__.items():
        value = getattr(obj, field_name, None)
        if value is None:
            continue

        # Detecta date e Optional[date]
        origin = get_origin(field_type)
        args = get_args(field_type)
        is_date_field = field_type in [date, datetime] or (
            origin is Union and date in args
        )

        if not is_date_field:
            continue

        # Converte strings e datetime para date
        if isinstance(value, str):
            try:
                setattr(
                    obj, field_name, datetime.strptime(value[:10], "%Y-%m-%d").date()
                )
            except ValueError:
                setattr(obj, field_name, None)
        elif isinstance(value, datetime):
            setattr(obj, field_name, value.date())
