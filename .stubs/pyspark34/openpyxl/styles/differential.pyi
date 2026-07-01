from .numbers import NumberFormat as NumberFormat
from _typeshed import Incomplete
from openpyxl.descriptors import Alias as Alias, Sequence as Sequence, Typed as Typed
from openpyxl.descriptors.serialisable import Serialisable as Serialisable
from openpyxl.styles import Alignment as Alignment, Border as Border, Fill as Fill, Font as Font, Protection as Protection

class DifferentialStyle(Serialisable):
    tagname: str
    __elements__: Incomplete
    font: Incomplete
    numFmt: Incomplete
    fill: Incomplete
    alignment: Incomplete
    border: Incomplete
    protection: Incomplete
    extLst: Incomplete
    def __init__(self, font: Incomplete | None = None, numFmt: Incomplete | None = None, fill: Incomplete | None = None, alignment: Incomplete | None = None, border: Incomplete | None = None, protection: Incomplete | None = None, extLst: Incomplete | None = None) -> None: ...

class DifferentialStyleList(Serialisable):
    """
    Dedupable container for differential styles.
    """
    tagname: str
    dxf: Incomplete
    styles: Incomplete
    __attrs__: Incomplete
    def __init__(self, dxf=(), count: Incomplete | None = None) -> None: ...
    def append(self, dxf) -> None:
        """
        Check to see whether style already exists and append it if does not.
        """
    def add(self, dxf):
        """
        Add a differential style and return its index
        """
    def __bool__(self) -> bool: ...
    def __getitem__(self, idx): ...
    @property
    def count(self): ...
