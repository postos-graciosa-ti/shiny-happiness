from sqlmodel import Field, SQLModel


class States(SQLModel, table=True):
    __tablename__ = "states"
    id: int | None = Field(default=None, primary_key=True)
    name: str
