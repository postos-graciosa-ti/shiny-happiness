from typing import Any

from pydantic import BaseModel


class RowsListParams(BaseModel):
    coord: str
    value: Any


class EmployeesBirthdayListProps(BaseModel):
    subsidiarie_id: int
    month: str
