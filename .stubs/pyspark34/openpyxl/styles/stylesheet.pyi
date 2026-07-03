from .borders import Border as Border
from .builtins import styles as styles
from .cell_style import CellStyle as CellStyle, CellStyleList as CellStyleList
from .colors import COLOR_INDEX as COLOR_INDEX, ColorList as ColorList
from .differential import DifferentialStyle as DifferentialStyle
from .fills import Fill as Fill
from .fonts import Font as Font
from .numbers import BUILTIN_FORMATS as BUILTIN_FORMATS, BUILTIN_FORMATS_MAX_SIZE as BUILTIN_FORMATS_MAX_SIZE, BUILTIN_FORMATS_REVERSE as BUILTIN_FORMATS_REVERSE, NumberFormatList as NumberFormatList, builtin_format_code as builtin_format_code, is_date_format as is_date_format, is_timedelta_format as is_timedelta_format
from .table import TableStyleList as TableStyleList
from _typeshed import Incomplete
from openpyxl.descriptors import Typed as Typed
from openpyxl.descriptors.excel import ExtensionList as ExtensionList
from openpyxl.descriptors.sequence import NestedSequence as NestedSequence
from openpyxl.descriptors.serialisable import Serialisable as Serialisable
from openpyxl.utils.indexed_list import IndexedList as IndexedList
from openpyxl.xml.constants import ARC_STYLE as ARC_STYLE, SHEET_MAIN_NS as SHEET_MAIN_NS
from openpyxl.xml.functions import fromstring as fromstring

class Stylesheet(Serialisable):
    tagname: str
    numFmts: Incomplete
    fonts: Incomplete
    fills: Incomplete
    borders: Incomplete
    cellStyleXfs: Incomplete
    cellXfs: Incomplete
    cellStyles: Incomplete
    dxfs: Incomplete
    tableStyles: Incomplete
    colors: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    number_formats: Incomplete
    cell_styles: Incomplete
    alignments: Incomplete
    protections: Incomplete
    named_styles: Incomplete
    def __init__(self, numFmts: Incomplete | None = None, fonts=(), fills=(), borders=(), cellStyleXfs: Incomplete | None = None, cellXfs: Incomplete | None = None, cellStyles: Incomplete | None = None, dxfs=(), tableStyles: Incomplete | None = None, colors: Incomplete | None = None, extLst: Incomplete | None = None) -> None: ...
    @classmethod
    def from_tree(cls, node): ...
    @property
    def custom_formats(self): ...
    def to_tree(self, tagname: Incomplete | None = None, idx: Incomplete | None = None, namespace: Incomplete | None = None): ...

def apply_stylesheet(archive, wb):
    """
    Add styles to workbook if present
    """
def write_stylesheet(wb): ...
