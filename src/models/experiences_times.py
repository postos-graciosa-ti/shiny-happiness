from sqlmodel import Field, SQLModel


class ExperiencesTimes(SQLModel, table=True):
    __tablename__ = "experiences_times"
    id: int | None = Field(default=None, primary_key=True)
    name: str
