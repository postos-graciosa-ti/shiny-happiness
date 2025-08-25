from sqlmodel import Field, SQLModel


class Ethnicities(SQLModel, table=True):
    __tablename__ = "ethnicities"
    id: int | None = Field(default=None, primary_key=True)
    name: str
