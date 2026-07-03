from _typeshed import Incomplete
from openpyxl.descriptors import Alias as Alias, Bool as Bool, Integer as Integer, NoneSet as NoneSet, String as String, Typed as Typed
from openpyxl.descriptors.excel import ExtensionList as ExtensionList, Relation as Relation
from openpyxl.descriptors.nested import NestedString as NestedString
from openpyxl.descriptors.sequence import NestedSequence as NestedSequence
from openpyxl.descriptors.serialisable import Serialisable as Serialisable
from openpyxl.workbook.defined_name import DefinedNameList as DefinedNameList
from openpyxl.workbook.external_reference import ExternalReference as ExternalReference
from openpyxl.workbook.function_group import FunctionGroupList as FunctionGroupList
from openpyxl.workbook.properties import CalcProperties as CalcProperties, FileVersion as FileVersion, WorkbookProperties as WorkbookProperties
from openpyxl.workbook.protection import FileSharing as FileSharing, WorkbookProtection as WorkbookProtection
from openpyxl.workbook.smart_tags import SmartTagList as SmartTagList, SmartTagProperties as SmartTagProperties
from openpyxl.workbook.views import BookView as BookView, CustomWorkbookView as CustomWorkbookView
from openpyxl.workbook.web import WebPublishObjectList as WebPublishObjectList, WebPublishing as WebPublishing
from openpyxl.xml.constants import SHEET_MAIN_NS as SHEET_MAIN_NS

class FileRecoveryProperties(Serialisable):
    tagname: str
    autoRecover: Incomplete
    crashSave: Incomplete
    dataExtractLoad: Incomplete
    repairLoad: Incomplete
    def __init__(self, autoRecover: Incomplete | None = None, crashSave: Incomplete | None = None, dataExtractLoad: Incomplete | None = None, repairLoad: Incomplete | None = None) -> None: ...

class ChildSheet(Serialisable):
    """
    Represents a reference to a worksheet or chartsheet in workbook.xml

    It contains the title, order and state but only an indirect reference to
    the objects themselves.
    """
    tagname: str
    name: Incomplete
    sheetId: Incomplete
    state: Incomplete
    id: Incomplete
    def __init__(self, name: Incomplete | None = None, sheetId: Incomplete | None = None, state: str = 'visible', id: Incomplete | None = None) -> None: ...

class PivotCache(Serialisable):
    tagname: str
    cacheId: Incomplete
    id: Incomplete
    def __init__(self, cacheId: Incomplete | None = None, id: Incomplete | None = None) -> None: ...

class WorkbookPackage(Serialisable):
    """
    Represent the workbook file in the archive
    """
    tagname: str
    conformance: Incomplete
    fileVersion: Incomplete
    fileSharing: Incomplete
    workbookPr: Incomplete
    properties: Incomplete
    workbookProtection: Incomplete
    bookViews: Incomplete
    sheets: Incomplete
    functionGroups: Incomplete
    externalReferences: Incomplete
    definedNames: Incomplete
    calcPr: Incomplete
    oleSize: Incomplete
    customWorkbookViews: Incomplete
    pivotCaches: Incomplete
    smartTagPr: Incomplete
    smartTagTypes: Incomplete
    webPublishing: Incomplete
    fileRecoveryPr: Incomplete
    webPublishObjects: Incomplete
    extLst: Incomplete
    Ignorable: Incomplete
    __elements__: Incomplete
    def __init__(self, conformance: Incomplete | None = None, fileVersion: Incomplete | None = None, fileSharing: Incomplete | None = None, workbookPr: Incomplete | None = None, workbookProtection: Incomplete | None = None, bookViews=(), sheets=(), functionGroups: Incomplete | None = None, externalReferences=(), definedNames: Incomplete | None = None, calcPr: Incomplete | None = None, oleSize: Incomplete | None = None, customWorkbookViews=(), pivotCaches=(), smartTagPr: Incomplete | None = None, smartTagTypes: Incomplete | None = None, webPublishing: Incomplete | None = None, fileRecoveryPr: Incomplete | None = None, webPublishObjects: Incomplete | None = None, extLst: Incomplete | None = None, Ignorable: Incomplete | None = None) -> None: ...
    def to_tree(self): ...
    @property
    def active(self): ...
