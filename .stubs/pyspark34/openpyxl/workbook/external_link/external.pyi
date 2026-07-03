from _typeshed import Incomplete
from openpyxl.descriptors import Bool as Bool, Integer as Integer, NoneSet as NoneSet, Sequence as Sequence, String as String, Typed as Typed
from openpyxl.descriptors.excel import ExtensionList as ExtensionList, Relation as Relation
from openpyxl.descriptors.nested import NestedText as NestedText
from openpyxl.descriptors.sequence import NestedSequence as NestedSequence, ValueSequence as ValueSequence
from openpyxl.descriptors.serialisable import Serialisable as Serialisable
from openpyxl.packaging.relationship import Relationship as Relationship, get_dependents as get_dependents, get_rels_path as get_rels_path
from openpyxl.xml.constants import SHEET_MAIN_NS as SHEET_MAIN_NS
from openpyxl.xml.functions import fromstring as fromstring

class ExternalCell(Serialisable):
    r: Incomplete
    t: Incomplete
    vm: Incomplete
    v: Incomplete
    def __init__(self, r: Incomplete | None = None, t: Incomplete | None = None, vm: Incomplete | None = None, v: Incomplete | None = None) -> None: ...

class ExternalRow(Serialisable):
    r: Incomplete
    cell: Incomplete
    __elements__: Incomplete
    def __init__(self, r=(), cell: Incomplete | None = None) -> None: ...

class ExternalSheetData(Serialisable):
    sheetId: Incomplete
    refreshError: Incomplete
    row: Incomplete
    __elements__: Incomplete
    def __init__(self, sheetId: Incomplete | None = None, refreshError: Incomplete | None = None, row=()) -> None: ...

class ExternalSheetDataSet(Serialisable):
    sheetData: Incomplete
    __elements__: Incomplete
    def __init__(self, sheetData: Incomplete | None = None) -> None: ...

class ExternalSheetNames(Serialisable):
    sheetName: Incomplete
    __elements__: Incomplete
    def __init__(self, sheetName=()) -> None: ...

class ExternalDefinedName(Serialisable):
    tagname: str
    name: Incomplete
    refersTo: Incomplete
    sheetId: Incomplete
    def __init__(self, name: Incomplete | None = None, refersTo: Incomplete | None = None, sheetId: Incomplete | None = None) -> None: ...

class ExternalBook(Serialisable):
    tagname: str
    sheetNames: Incomplete
    definedNames: Incomplete
    sheetDataSet: Incomplete
    id: Incomplete
    __elements__: Incomplete
    def __init__(self, sheetNames: Incomplete | None = None, definedNames=(), sheetDataSet: Incomplete | None = None, id: Incomplete | None = None) -> None: ...

class ExternalLink(Serialisable):
    tagname: str
    mime_type: str
    externalBook: Incomplete
    file_link: Incomplete
    __elements__: Incomplete
    def __init__(self, externalBook: Incomplete | None = None, ddeLink: Incomplete | None = None, oleLink: Incomplete | None = None, extLst: Incomplete | None = None) -> None: ...
    def to_tree(self): ...
    @property
    def path(self): ...

def read_external_link(archive, book_path): ...
