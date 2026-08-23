from .alignment import Alignment as Alignment
from .protection import Protection as Protection
from _typeshed import Incomplete
from array import array
from openpyxl.descriptors import Bool as Bool, Float as Float, Integer as Integer, Sequence as Sequence, Typed as Typed
from openpyxl.descriptors.excel import ExtensionList as ExtensionList
from openpyxl.descriptors.serialisable import Serialisable as Serialisable
from openpyxl.utils.indexed_list import IndexedList as IndexedList

class ArrayDescriptor:
    key: Incomplete
    def __init__(self, key) -> None: ...
    def __get__(self, instance, cls): ...
    def __set__(self, instance, value) -> None: ...

class StyleArray(array):
    """
    Simplified named tuple with an array
    """
    tagname: str
    fontId: Incomplete
    fillId: Incomplete
    borderId: Incomplete
    numFmtId: Incomplete
    protectionId: Incomplete
    alignmentId: Incomplete
    pivotButton: Incomplete
    quotePrefix: Incomplete
    xfId: Incomplete
    def __new__(cls, args=...): ...
    def __hash__(self): ...
    def __copy__(self): ...
    def __deepcopy__(self, memo): ...

class CellStyle(Serialisable):
    tagname: str
    numFmtId: Incomplete
    fontId: Incomplete
    fillId: Incomplete
    borderId: Incomplete
    xfId: Incomplete
    quotePrefix: Incomplete
    pivotButton: Incomplete
    applyNumberFormat: Incomplete
    applyFont: Incomplete
    applyFill: Incomplete
    applyBorder: Incomplete
    applyAlignment: Incomplete
    applyProtection: Incomplete
    alignment: Incomplete
    protection: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    __attrs__: Incomplete
    def __init__(self, numFmtId: int = 0, fontId: int = 0, fillId: int = 0, borderId: int = 0, xfId: Incomplete | None = None, quotePrefix: Incomplete | None = None, pivotButton: Incomplete | None = None, applyNumberFormat: Incomplete | None = None, applyFont: Incomplete | None = None, applyFill: Incomplete | None = None, applyBorder: Incomplete | None = None, applyAlignment: Incomplete | None = None, applyProtection: Incomplete | None = None, alignment: Incomplete | None = None, protection: Incomplete | None = None, extLst: Incomplete | None = None) -> None: ...
    def to_array(self):
        """
        Convert to StyleArray
        """
    @classmethod
    def from_array(cls, style):
        """
        Convert from StyleArray
        """
    @property
    def applyProtection(self): ...
    @property
    def applyAlignment(self): ...

class CellStyleList(Serialisable):
    tagname: str
    __attrs__: Incomplete
    count: Incomplete
    xf: Incomplete
    alignment: Incomplete
    protection: Incomplete
    __elements__: Incomplete
    def __init__(self, count: Incomplete | None = None, xf=()) -> None: ...
    @property
    def count(self): ...
    def __getitem__(self, idx): ...
