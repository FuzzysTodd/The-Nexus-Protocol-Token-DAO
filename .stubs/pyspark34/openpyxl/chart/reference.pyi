from _typeshed import Incomplete
from collections.abc import Generator
from itertools import chain as chain
from openpyxl.descriptors import MinMax as MinMax, Strict as Strict, String as String, Typed as Typed
from openpyxl.descriptors.serialisable import Serialisable as Serialisable
from openpyxl.utils import get_column_letter as get_column_letter, quote_sheetname as quote_sheetname, range_to_tuple as range_to_tuple
from openpyxl.worksheet.worksheet import Worksheet as Worksheet

class DummyWorksheet:
    title: Incomplete
    def __init__(self, title) -> None: ...

class Reference(Strict):
    """
    Normalise cell range references
    """
    min_row: Incomplete
    max_row: Incomplete
    min_col: Incomplete
    max_col: Incomplete
    range_string: Incomplete
    worksheet: Incomplete
    def __init__(self, worksheet: Incomplete | None = None, min_col: Incomplete | None = None, min_row: Incomplete | None = None, max_col: Incomplete | None = None, max_row: Incomplete | None = None, range_string: Incomplete | None = None) -> None: ...
    def __len__(self) -> int: ...
    def __eq__(self, other): ...
    @property
    def rows(self) -> Generator[Incomplete, None, None]:
        """
        Return all rows in the range
        """
    @property
    def cols(self) -> Generator[Incomplete, None, None]:
        """
        Return all columns in the range
        """
    def pop(self):
        """
        Return and remove the first cell
        """
    @property
    def sheetname(self): ...
