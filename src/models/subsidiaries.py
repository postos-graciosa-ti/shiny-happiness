from sqlmodel import Field, SQLModel


class Subsidiaries(SQLModel, table=True):
    __tablename__ = "subsidiaries"
    id: int | None = Field(default=None, primary_key=True)
    name: str
    address: str
    cnpj: str
    ie: str
    phone: str
    web_postos_subsidiarie_code: str
