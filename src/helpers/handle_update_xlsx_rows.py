from typing import List

from src.schemas.employees import RowsListParams


async def handle_update_xlsx_rows(ws, rows: List[RowsListParams]) -> List[str]:
    updated_cells = []

    for row in rows:
        ws[row.coord] = row.value if row.value is not None else ""

        updated_cells.append(row.coord)

    return updated_cells
