from sqlmodel import Field, SQLModel


class Cities(SQLModel, table=True):
    __tablename__ = "cities"
    id: int | None = Field(default=None, primary_key=True)
    name: str
