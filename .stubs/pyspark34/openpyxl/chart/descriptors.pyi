from .data_source import NumFmt as NumFmt
from openpyxl.descriptors import Typed as Typed
from openpyxl.descriptors.nested import NestedMinMax as NestedMinMax

class NestedGapAmount(NestedMinMax):
    allow_none: bool
    min: int
    max: int

class NestedOverlap(NestedMinMax):
    allow_none: bool
    min: int
    max: int

class NumberFormatDescriptor(Typed):
    """
    Allow direct assignment of format code
    """
    expected_type = NumFmt
    allow_none: bool
    def __set__(self, instance, value) -> None: ...
