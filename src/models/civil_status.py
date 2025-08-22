from sqlmodel import Field, SQLModel


class CivilStatus(SQLModel, table=True):
    __tablename__ = "civil_status"
    id: int | None = Field(default=None, primary_key=True)
    name: str
