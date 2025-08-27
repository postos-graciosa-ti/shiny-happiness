from sqlmodel import Field, SQLModel


class PaymentMethods(SQLModel, table=True):
    __tablename__ = "payment_methods"
    id: int | None = Field(default=None, primary_key=True)
    name: str
