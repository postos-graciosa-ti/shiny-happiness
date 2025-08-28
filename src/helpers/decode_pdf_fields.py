import base64

from src.helpers.get_binary_fields import get_binary_fields
from src.models.employees import Employees


def decode_pdf_fields(employee: Employees):
    """Decodifica base64 -> bytes para todos os campos LargeBinary"""
    for field in get_binary_fields():
        value = getattr(employee, field, None)

        if isinstance(value, str):
            try:
                setattr(employee, field, base64.b64decode(value))

            except Exception as e:
                raise ValueError(f"Erro ao decodificar arquivo do campo {field}") from e
