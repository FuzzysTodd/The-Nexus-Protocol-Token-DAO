from .colors import Color as Color
from _typeshed import Incomplete
from openpyxl.descriptors import Bool as Bool, Float as Float, Integer as Integer, NoneSet as NoneSet, Sequence as Sequence, Set as Set, String as String, Typed as Typed
from openpyxl.descriptors.serialisable import Serialisable as Serialisable

class TableStyleElement(Serialisable):
    tagname: str
    type: Incomplete
    size: Incomplete
    dxfId: Incomplete
    def __init__(self, type: Incomplete | None = None, size: Incomplete | None = None, dxfId: Incomplete | None = None) -> None: ...

class TableStyle(Serialisable):
    tagname: str
    name: Incomplete
    pivot: Incomplete
    table: Incomplete
    count: Incomplete
    tableStyleElement: Incomplete
    __elements__: Incomplete
    def __init__(self, name: Incomplete | None = None, pivot: Incomplete | None = None, table: Incomplete | None = None, count: Incomplete | None = None, tableStyleElement=()) -> None: ...

class TableStyleList(Serialisable):
    tagname: str
    defaultTableStyle: Incomplete
    defaultPivotStyle: Incomplete
    tableStyle: Incomplete
    __elements__: Incomplete
    __attrs__: Incomplete
    def __init__(self, count: Incomplete | None = None, defaultTableStyle: str = 'TableStyleMedium9', defaultPivotStyle: str = 'PivotStyleLight16', tableStyle=()) -> None: ...
    @property
    def count(self): ...
