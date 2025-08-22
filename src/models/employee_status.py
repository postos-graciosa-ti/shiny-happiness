from sqlmodel import Field, SQLModel


class EmployeeStatus(SQLModel, table=True):
    __tablename__ = "employee_status"
    id: int | None = Field(default=None, primary_key=True)
    name: str
