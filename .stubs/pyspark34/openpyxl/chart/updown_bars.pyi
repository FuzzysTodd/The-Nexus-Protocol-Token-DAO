from .axis import ChartLines as ChartLines
from .descriptors import NestedGapAmount as NestedGapAmount
from .shapes import GraphicalProperties as GraphicalProperties
from _typeshed import Incomplete
from openpyxl.descriptors import Typed as Typed
from openpyxl.descriptors.excel import ExtensionList as ExtensionList
from openpyxl.descriptors.serialisable import Serialisable as Serialisable

class UpDownBars(Serialisable):
    tagname: str
    gapWidth: Incomplete
    upBars: Incomplete
    downBars: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(self, gapWidth: int = 150, upBars: Incomplete | None = None, downBars: Incomplete | None = None, extLst: Incomplete | None = None) -> None: ...
