from sqlmodel import Field, SQLModel


class Nationalities(SQLModel, table=True):
    __tablename__ = "nationalities"
    id: int | None = Field(default=None, primary_key=True)
    name: str
