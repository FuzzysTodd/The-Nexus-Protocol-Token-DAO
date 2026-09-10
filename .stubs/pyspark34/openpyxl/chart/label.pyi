from .shapes import GraphicalProperties as GraphicalProperties
from .text import RichText as RichText
from _typeshed import Incomplete
from openpyxl.descriptors import Alias as Alias, Sequence as Sequence, Typed as Typed
from openpyxl.descriptors.excel import ExtensionList as ExtensionList
from openpyxl.descriptors.nested import NestedBool as NestedBool, NestedInteger as NestedInteger, NestedNoneSet as NestedNoneSet, NestedString as NestedString
from openpyxl.descriptors.serialisable import Serialisable as Serialisable

class _DataLabelBase(Serialisable):
    numFmt: Incomplete
    spPr: Incomplete
    graphicalProperties: Incomplete
    txPr: Incomplete
    textProperties: Incomplete
    dLblPos: Incomplete
    position: Incomplete
    showLegendKey: Incomplete
    showVal: Incomplete
    showCatName: Incomplete
    showSerName: Incomplete
    showPercent: Incomplete
    showBubbleSize: Incomplete
    showLeaderLines: Incomplete
    separator: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(self, numFmt: Incomplete | None = None, spPr: Incomplete | None = None, txPr: Incomplete | None = None, dLblPos: Incomplete | None = None, showLegendKey: Incomplete | None = None, showVal: Incomplete | None = None, showCatName: Incomplete | None = None, showSerName: Incomplete | None = None, showPercent: Incomplete | None = None, showBubbleSize: Incomplete | None = None, showLeaderLines: Incomplete | None = None, separator: Incomplete | None = None, extLst: Incomplete | None = None) -> None: ...

class DataLabel(_DataLabelBase):
    tagname: str
    idx: Incomplete
    numFmt: Incomplete
    spPr: Incomplete
    txPr: Incomplete
    dLblPos: Incomplete
    showLegendKey: Incomplete
    showVal: Incomplete
    showCatName: Incomplete
    showSerName: Incomplete
    showPercent: Incomplete
    showBubbleSize: Incomplete
    showLeaderLines: Incomplete
    separator: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(self, idx: int = 0, **kw) -> None: ...

class DataLabelList(_DataLabelBase):
    tagname: str
    dLbl: Incomplete
    delete: Incomplete
    numFmt: Incomplete
    spPr: Incomplete
    txPr: Incomplete
    dLblPos: Incomplete
    showLegendKey: Incomplete
    showVal: Incomplete
    showCatName: Incomplete
    showSerName: Incomplete
    showPercent: Incomplete
    showBubbleSize: Incomplete
    showLeaderLines: Incomplete
    separator: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(self, dLbl=(), delete: Incomplete | None = None, **kw) -> None: ...
