from datetime import time
from typing import Optional

from sqlmodel import Field, SQLModel


class Turns(SQLModel, table=True):
    __tablename__ = "turns"
    id: int | None = Field(default=None, primary_key=True)
    name: str
    start_time: time
    start_interval_time: time
    end_interval_time: time
    end_time: time
    exception: Optional[str]
