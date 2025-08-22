from sqlmodel import Field, SQLModel


class Sectors(SQLModel, table=True):
    __tablename__ = "sectors"
    id: int | None = Field(default=None, primary_key=True)
    name: str
