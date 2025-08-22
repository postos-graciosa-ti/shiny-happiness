from sqlmodel import Field, SQLModel


class HierarchyStructure(SQLModel, table=True):
    __tablename__ = "hierarchy_structure"
    id: int | None = Field(default=None, primary_key=True)
    name: str
