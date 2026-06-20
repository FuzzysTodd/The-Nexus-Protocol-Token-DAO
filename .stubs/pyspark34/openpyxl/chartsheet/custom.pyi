from _typeshed import Incomplete
from openpyxl.descriptors import Bool as Bool, Integer as Integer, Sequence as Sequence, Set as Set, Typed as Typed
from openpyxl.descriptors.excel import Guid as Guid
from openpyxl.descriptors.serialisable import Serialisable as Serialisable
from openpyxl.worksheet.header_footer import HeaderFooter as HeaderFooter
from openpyxl.worksheet.page import PageMargins as PageMargins, PrintPageSetup as PrintPageSetup

class CustomChartsheetView(Serialisable):
    tagname: str
    guid: Incomplete
    scale: Incomplete
    state: Incomplete
    zoomToFit: Incomplete
    pageMargins: Incomplete
    pageSetup: Incomplete
    headerFooter: Incomplete
    __elements__: Incomplete
    def __init__(self, guid: Incomplete | None = None, scale: Incomplete | None = None, state: str = 'visible', zoomToFit: Incomplete | None = None, pageMargins: Incomplete | None = None, pageSetup: Incomplete | None = None, headerFooter: Incomplete | None = None) -> None: ...

class CustomChartsheetViews(Serialisable):
    tagname: str
    customSheetView: Incomplete
    __elements__: Incomplete
    def __init__(self, customSheetView: Incomplete | None = None) -> None: ...
