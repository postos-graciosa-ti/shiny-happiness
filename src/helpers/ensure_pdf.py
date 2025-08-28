from io import BytesIO

from PIL import Image


def ensure_pdf(file_bytes: bytes, filename: str) -> bytes:
    """
    Garante que o arquivo seja PDF.
    - Se já for PDF (.pdf), retorna bytes direto.
    - Se for imagem, converte para PDF usando Pillow.
    """
    if filename.lower().endswith(".pdf"):
        return file_bytes

    try:
        image = Image.open(BytesIO(file_bytes))

    except Exception:
        raise ValueError("Arquivo não é PDF nem imagem válida")

    pdf_buffer = BytesIO()

    if image.mode != "RGB":
        image = image.convert("RGB")

    image.save(pdf_buffer, format="PDF")

    pdf_buffer.seek(0)

    return pdf_buffer.getvalue()
