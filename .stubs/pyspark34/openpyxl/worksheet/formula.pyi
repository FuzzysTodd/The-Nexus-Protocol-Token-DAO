from _typeshed import Incomplete
from openpyxl.compat import safe_string as safe_string

class DataTableFormula:
    t: str
    ref: Incomplete
    ca: Incomplete
    dt2D: Incomplete
    dtr: Incomplete
    r1: Incomplete
    r2: Incomplete
    del1: Incomplete
    del2: Incomplete
    def __init__(self, ref, ca: bool = False, dt2D: bool = False, dtr: bool = False, r1: Incomplete | None = None, r2: Incomplete | None = None, del1: bool = False, del2: bool = False, **kw) -> None: ...
    def __iter__(self): ...

class ArrayFormula:
    t: str
    ref: Incomplete
    text: Incomplete
    def __init__(self, ref, text: Incomplete | None = None) -> None: ...
    def __iter__(self): ...
