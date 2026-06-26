from _typeshed import Incomplete
from openpyxl.descriptors import Bool as Bool, Integer as Integer, Sequence as Sequence, Typed as Typed
from openpyxl.descriptors.excel import ExtensionList as ExtensionList
from openpyxl.descriptors.serialisable import Serialisable as Serialisable

class ChartsheetView(Serialisable):
    tagname: str
    tabSelected: Incomplete
    zoomScale: Incomplete
    workbookViewId: Incomplete
    zoomToFit: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(self, tabSelected: Incomplete | None = None, zoomScale: Incomplete | None = None, workbookViewId: int = 0, zoomToFit: bool = True, extLst: Incomplete | None = None) -> None: ...

class ChartsheetViewList(Serialisable):
    tagname: str
    sheetView: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(self, sheetView: Incomplete | None = None, extLst: Incomplete | None = None) -> None: ...
