from typing import Any

from pydantic import BaseModel


class RowsListParams(BaseModel):
    coord: str
    value: Any
