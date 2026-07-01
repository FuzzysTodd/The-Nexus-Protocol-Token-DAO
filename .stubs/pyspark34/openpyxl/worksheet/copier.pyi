from .worksheet import Worksheet as Worksheet
from _typeshed import Incomplete

class WorksheetCopy:
    """
    Copy the values, styles, dimensions, merged cells, margins, and
    print/page setup from one worksheet to another within the same
    workbook.
    """
    source: Incomplete
    target: Incomplete
    def __init__(self, source_worksheet, target_worksheet) -> None: ...
    def copy_worksheet(self) -> None: ...
