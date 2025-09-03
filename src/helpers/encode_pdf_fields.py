import base64

from src.helpers.get_binary_fields import get_binary_fields
from src.models.employees import Employees


def encode_pdf_fields(emp: Employees):
    """Converte todos os campos LargeBinary para base64"""
    emp_dict = emp.dict()

    for field in get_binary_fields():
        value = getattr(emp, field, None)

        if value:
            emp_dict[field] = base64.b64encode(value).decode("utf-8")

    return emp_dict
