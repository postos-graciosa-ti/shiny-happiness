from sqlmodel import Field, SQLModel


class Neighborhoods(SQLModel, table=True):
    __tablename__ = "neighborhoods"
    id: int | None = Field(default=None, primary_key=True)
    name: str
