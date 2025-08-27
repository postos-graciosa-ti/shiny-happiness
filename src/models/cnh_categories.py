from sqlmodel import Field, SQLModel


class CnhCategories(SQLModel, table=True):
    __tablename__ = "cnh_categories"
    id: int | None = Field(default=None, primary_key=True)
    name: str
