from sqlmodel import Field, SQLModel


class Functions(SQLModel, table=True):
    __tablename__ = "functions"
    id: int | None = Field(default=None, primary_key=True)
    name: str
    cbo: str
