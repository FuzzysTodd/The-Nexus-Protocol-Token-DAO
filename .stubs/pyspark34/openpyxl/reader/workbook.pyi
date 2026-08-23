from _typeshed import Incomplete
from collections.abc import Generator
from openpyxl.packaging.relationship import get_dependents as get_dependents, get_rel as get_rel, get_rels_path as get_rels_path
from openpyxl.packaging.workbook import WorkbookPackage as WorkbookPackage
from openpyxl.pivot.cache import CacheDefinition as CacheDefinition
from openpyxl.pivot.record import RecordList as RecordList
from openpyxl.utils.datetime import CALENDAR_MAC_1904 as CALENDAR_MAC_1904
from openpyxl.workbook import Workbook as Workbook
from openpyxl.workbook.defined_name import DefinedNameList as DefinedNameList
from openpyxl.workbook.external_link.external import read_external_link as read_external_link
from openpyxl.worksheet.print_settings import PrintArea as PrintArea, PrintTitles as PrintTitles
from openpyxl.xml.functions import fromstring as fromstring

class WorkbookParser:
    archive: Incomplete
    workbook_part_name: Incomplete
    defined_names: Incomplete
    wb: Incomplete
    keep_links: Incomplete
    sheets: Incomplete
    def __init__(self, archive, workbook_part_name, keep_links: bool = True) -> None: ...
    @property
    def rels(self): ...
    caches: Incomplete
    def parse(self) -> None: ...
    def find_sheets(self) -> Generator[Incomplete, None, None]:
        """
        Find all sheets in the workbook and return the link to the source file.

        Older XLSM files sometimes contain invalid sheet elements.
        Warn user when these are removed.
        """
    def assign_names(self) -> None:
        """
        Bind defined names and other definitions to worksheets or the workbook
        """
    @property
    def pivot_caches(self):
        """
        Get PivotCache objects
        """
