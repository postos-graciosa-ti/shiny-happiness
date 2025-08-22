from sqlmodel import Field, SQLModel


class Departments(SQLModel, table=True):
    __tablename__ = "departments"
    id: int | None = Field(default=None, primary_key=True)
    name: str
