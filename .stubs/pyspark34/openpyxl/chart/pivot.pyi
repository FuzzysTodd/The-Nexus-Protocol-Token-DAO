from .label import DataLabel as DataLabel
from .marker import Marker as Marker
from .shapes import GraphicalProperties as GraphicalProperties
from .text import RichText as RichText
from _typeshed import Incomplete
from openpyxl.descriptors import Alias as Alias, Typed as Typed
from openpyxl.descriptors.excel import ExtensionList as ExtensionList
from openpyxl.descriptors.nested import NestedInteger as NestedInteger, NestedText as NestedText
from openpyxl.descriptors.serialisable import Serialisable as Serialisable

class PivotSource(Serialisable):
    tagname: str
    name: Incomplete
    fmtId: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(self, name: Incomplete | None = None, fmtId: Incomplete | None = None, extLst: Incomplete | None = None) -> None: ...

class PivotFormat(Serialisable):
    tagname: str
    idx: Incomplete
    spPr: Incomplete
    graphicalProperties: Incomplete
    txPr: Incomplete
    TextBody: Incomplete
    marker: Incomplete
    dLbl: Incomplete
    DataLabel: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(self, idx: int = 0, spPr: Incomplete | None = None, txPr: Incomplete | None = None, marker: Incomplete | None = None, dLbl: Incomplete | None = None, extLst: Incomplete | None = None) -> None: ...
