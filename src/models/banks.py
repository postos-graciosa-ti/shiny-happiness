from sqlmodel import Field, SQLModel


class Banks(SQLModel, table=True):
    __tablename__ = "banks"
    id: int | None = Field(default=None, primary_key=True)
    name: str
