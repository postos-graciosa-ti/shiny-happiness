from datetime import date, datetime

from sqlmodel import SQLModel


def parse_dates(obj: SQLModel):
    for field_name, field_type in obj.__annotations__.items():
        value = getattr(obj, field_name, None)

        if value is None:
            continue

        if field_type in [date, datetime]:
            if isinstance(value, str):
                setattr(obj, field_name, datetime.strptime(value, "%Y-%m-%d").date())

            elif isinstance(value, datetime):
                setattr(obj, field_name, value.date())

    return obj
