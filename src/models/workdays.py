from sqlmodel import Field, SQLModel

class Workdays(SQLModel, table=True):
    __tablename__ = "workdays"
    id: int | None = Field(default=None, primary_key=True)
    name: str