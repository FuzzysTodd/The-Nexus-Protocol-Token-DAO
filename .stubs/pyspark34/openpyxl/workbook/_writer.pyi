from _typeshed import Incomplete
from openpyxl.packaging.relationship import Relationship as Relationship, RelationshipList as RelationshipList
from openpyxl.packaging.workbook import ChildSheet as ChildSheet, PivotCache as PivotCache, WorkbookPackage as WorkbookPackage
from openpyxl.utils import quote_sheetname as quote_sheetname
from openpyxl.utils.datetime import CALENDAR_MAC_1904 as CALENDAR_MAC_1904
from openpyxl.workbook.defined_name import DefinedName as DefinedName, DefinedNameList as DefinedNameList
from openpyxl.workbook.external_reference import ExternalReference as ExternalReference
from openpyxl.workbook.properties import WorkbookProperties as WorkbookProperties
from openpyxl.xml.constants import ARC_APP as ARC_APP, ARC_CORE as ARC_CORE, ARC_CUSTOM as ARC_CUSTOM, ARC_ROOT_RELS as ARC_ROOT_RELS, ARC_WORKBOOK as ARC_WORKBOOK, CUSTOMUI_NS as CUSTOMUI_NS, PKG_REL_NS as PKG_REL_NS
from openpyxl.xml.functions import fromstring as fromstring, tostring as tostring

def get_active_sheet(wb):
    """
    Return the index of the active sheet.
    If the sheet set to active is hidden return the next visible sheet or None
    """

class WorkbookWriter:
    wb: Incomplete
    rels: Incomplete
    package: Incomplete
    def __init__(self, wb) -> None: ...
    def write_properties(self) -> None: ...
    def write_worksheets(self) -> None: ...
    def write_refs(self) -> None: ...
    def write_names(self) -> None: ...
    def write_pivots(self) -> None: ...
    def write_views(self) -> None: ...
    def write(self):
        """Write the core workbook xml."""
    def write_rels(self):
        """Write the workbook relationships xml."""
    def write_root_rels(self):
        """Write the package relationships"""
