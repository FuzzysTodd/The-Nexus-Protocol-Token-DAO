from .custom import CustomChartsheetViews as CustomChartsheetViews
from .properties import ChartsheetProperties as ChartsheetProperties
from .protection import ChartsheetProtection as ChartsheetProtection
from .publish import WebPublishItems as WebPublishItems
from .relation import DrawingHF as DrawingHF, SheetBackgroundPicture as SheetBackgroundPicture
from .views import ChartsheetViewList as ChartsheetViewList
from _typeshed import Incomplete
from openpyxl.descriptors import Alias as Alias, Set as Set, Typed as Typed
from openpyxl.descriptors.excel import ExtensionList as ExtensionList
from openpyxl.descriptors.serialisable import Serialisable as Serialisable
from openpyxl.drawing.spreadsheet_drawing import AbsoluteAnchor as AbsoluteAnchor, SpreadsheetDrawing as SpreadsheetDrawing
from openpyxl.workbook.child import _WorkbookChild
from openpyxl.worksheet.drawing import Drawing as Drawing
from openpyxl.worksheet.header_footer import HeaderFooter as HeaderFooter
from openpyxl.worksheet.page import PageMargins as PageMargins, PrintPageSetup as PrintPageSetup
from openpyxl.xml.constants import REL_NS as REL_NS, SHEET_MAIN_NS as SHEET_MAIN_NS

class Chartsheet(_WorkbookChild, Serialisable):
    tagname: str
    mime_type: str
    sheetPr: Incomplete
    sheetViews: Incomplete
    sheetProtection: Incomplete
    customSheetViews: Incomplete
    pageMargins: Incomplete
    pageSetup: Incomplete
    drawing: Incomplete
    drawingHF: Incomplete
    picture: Incomplete
    webPublishItems: Incomplete
    extLst: Incomplete
    sheet_state: Incomplete
    headerFooter: Incomplete
    HeaderFooter: Incomplete
    __elements__: Incomplete
    __attrs__: Incomplete
    def __init__(self, sheetPr: Incomplete | None = None, sheetViews: Incomplete | None = None, sheetProtection: Incomplete | None = None, customSheetViews: Incomplete | None = None, pageMargins: Incomplete | None = None, pageSetup: Incomplete | None = None, headerFooter: Incomplete | None = None, drawing: Incomplete | None = None, drawingHF: Incomplete | None = None, picture: Incomplete | None = None, webPublishItems: Incomplete | None = None, extLst: Incomplete | None = None, parent: Incomplete | None = None, title: str = '', sheet_state: str = 'visible') -> None: ...
    def add_chart(self, chart) -> None: ...
    def to_tree(self): ...
