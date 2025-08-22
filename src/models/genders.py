from sqlmodel import Field, SQLModel


class Genders(SQLModel, table=True):
    __tablename__ = "genders"
    id: int | None = Field(default=None, primary_key=True)
    name: str
