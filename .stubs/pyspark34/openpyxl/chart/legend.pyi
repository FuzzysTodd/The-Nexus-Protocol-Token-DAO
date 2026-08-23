from .layout import Layout as Layout
from .shapes import GraphicalProperties as GraphicalProperties
from .text import RichText as RichText
from _typeshed import Incomplete
from openpyxl.descriptors import Alias as Alias, Integer as Integer, Sequence as Sequence, Typed as Typed
from openpyxl.descriptors.excel import ExtensionList as ExtensionList
from openpyxl.descriptors.nested import NestedBool as NestedBool, NestedInteger as NestedInteger, NestedSet as NestedSet
from openpyxl.descriptors.serialisable import Serialisable as Serialisable

class LegendEntry(Serialisable):
    tagname: str
    idx: Incomplete
    delete: Incomplete
    txPr: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(self, idx: int = 0, delete: bool = False, txPr: Incomplete | None = None, extLst: Incomplete | None = None) -> None: ...

class Legend(Serialisable):
    tagname: str
    legendPos: Incomplete
    position: Incomplete
    legendEntry: Incomplete
    layout: Incomplete
    overlay: Incomplete
    spPr: Incomplete
    graphicalProperties: Incomplete
    txPr: Incomplete
    textProperties: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(self, legendPos: str = 'r', legendEntry=(), layout: Incomplete | None = None, overlay: Incomplete | None = None, spPr: Incomplete | None = None, txPr: Incomplete | None = None, extLst: Incomplete | None = None) -> None: ...
