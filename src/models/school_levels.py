from sqlmodel import Field, SQLModel


class SchoolLevels(SQLModel, table=True):
    __tablename__ = "school_levels"
    id: int | None = Field(default=None, primary_key=True)
    name: str
