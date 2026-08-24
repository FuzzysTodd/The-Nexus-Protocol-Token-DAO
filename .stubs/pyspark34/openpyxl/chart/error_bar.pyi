from .data_source import NumDataSource as NumDataSource
from .shapes import GraphicalProperties as GraphicalProperties
from _typeshed import Incomplete
from openpyxl.descriptors import Alias as Alias, Float as Float, Set as Set, Typed as Typed
from openpyxl.descriptors.excel import ExtensionList as ExtensionList
from openpyxl.descriptors.nested import NestedBool as NestedBool, NestedFloat as NestedFloat, NestedNoneSet as NestedNoneSet, NestedSet as NestedSet
from openpyxl.descriptors.serialisable import Serialisable as Serialisable

class ErrorBars(Serialisable):
    tagname: str
    errDir: Incomplete
    direction: Incomplete
    errBarType: Incomplete
    style: Incomplete
    errValType: Incomplete
    size: Incomplete
    noEndCap: Incomplete
    plus: Incomplete
    minus: Incomplete
    val: Incomplete
    spPr: Incomplete
    graphicalProperties: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(self, errDir: Incomplete | None = None, errBarType: str = 'both', errValType: str = 'fixedVal', noEndCap: Incomplete | None = None, plus: Incomplete | None = None, minus: Incomplete | None = None, val: Incomplete | None = None, spPr: Incomplete | None = None, extLst: Incomplete | None = None) -> None: ...
