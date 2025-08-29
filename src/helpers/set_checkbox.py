def set_checkbox(ws, true_cell: str, false_cell: str, condition: bool | None):
    if condition is None:
        return

    if condition:
        ws[true_cell] = "X"

    else:
        ws[false_cell] = "X"
