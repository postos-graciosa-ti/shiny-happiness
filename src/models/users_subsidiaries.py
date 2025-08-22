from sqlmodel import Field, SQLModel


class UsersSubsidiaries(SQLModel, table=True):
    __tablename__ = "users_subsidiaries"
    user_id: int = Field(default=None, foreign_key="users.id", primary_key=True)
    subsidiarie_id: int = Field(
        default=None, foreign_key="subsidiaries.id", primary_key=True
    )
