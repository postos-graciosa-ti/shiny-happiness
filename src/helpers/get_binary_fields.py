from sqlalchemy import LargeBinary

from src.models.employees import Employees


def get_binary_fields():
    """
    Retorna dinamicamente todos os campos LargeBinary do modelo Employees.
    Qualquer campo binário novo será tratado automaticamente.
    """
    return [
        col.name
        for col in Employees.__table__.columns
        if isinstance(col.type, LargeBinary)
    ]
