from sqlmodel import Field, SQLModel


class Users(SQLModel, table=True):
    __tablename__ = "users"
    id: int | None = Field(default=None, primary_key=True)
    login: str
    password: str
    name: str
    email: str
