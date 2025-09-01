from sqlmodel import Field, SQLModel


class EmployeesParents(SQLModel, table=True):
    __tablename__ = "employees_parents"
    id: int | None = Field(default=None, primary_key=True)
    name: str
    employee_id: int = Field(default=None, foreign_key="employees.id", primary_key=True)
