from _typeshed import Incomplete
from openpyxl.descriptors import Bool as Bool, Integer as Integer, Sequence as Sequence
from openpyxl.descriptors.serialisable import Serialisable as Serialisable

class Break(Serialisable):
    tagname: str
    id: Incomplete
    min: Incomplete
    max: Incomplete
    man: Incomplete
    pt: Incomplete
    def __init__(self, id: int = 0, min: int = 0, max: int = 16383, man: bool = True, pt: Incomplete | None = None) -> None: ...

class RowBreak(Serialisable):
    tagname: str
    count: Incomplete
    manualBreakCount: Incomplete
    brk: Incomplete
    __elements__: Incomplete
    __attrs__: Incomplete
    def __init__(self, count: Incomplete | None = None, manualBreakCount: Incomplete | None = None, brk=()) -> None: ...
    def __bool__(self) -> bool: ...
    def __len__(self) -> int: ...
    @property
    def count(self): ...
    @property
    def manualBreakCount(self): ...
    def append(self, brk: Incomplete | None = None) -> None:
        """
        Add a page break
        """
PageBreak = RowBreak

class ColBreak(RowBreak):
    tagname: str
    count: Incomplete
    manualBreakCount: Incomplete
    brk: Incomplete
    __attrs__: Incomplete
