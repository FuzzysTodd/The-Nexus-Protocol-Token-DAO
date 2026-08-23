from _typeshed import Incomplete
from collections.abc import Generator
from openpyxl.compat import safe_string as safe_string
from openpyxl.descriptors import Alias as Alias, Bool as Bool, Descriptor as Descriptor, Integer as Integer, Sequence as Sequence, String as String
from openpyxl.descriptors.serialisable import Serialisable as Serialisable
from openpyxl.formula import Tokenizer as Tokenizer
from openpyxl.utils.cell import SHEETRANGE_RE as SHEETRANGE_RE

RESERVED: Incomplete
RESERVED_REGEX: Incomplete

class DefinedName(Serialisable):
    tagname: str
    name: Incomplete
    comment: Incomplete
    customMenu: Incomplete
    description: Incomplete
    help: Incomplete
    statusBar: Incomplete
    localSheetId: Incomplete
    hidden: Incomplete
    function: Incomplete
    vbProcedure: Incomplete
    xlm: Incomplete
    functionGroupId: Incomplete
    shortcutKey: Incomplete
    publishToServer: Incomplete
    workbookParameter: Incomplete
    attr_text: Incomplete
    value: Incomplete
    def __init__(self, name: Incomplete | None = None, comment: Incomplete | None = None, customMenu: Incomplete | None = None, description: Incomplete | None = None, help: Incomplete | None = None, statusBar: Incomplete | None = None, localSheetId: Incomplete | None = None, hidden: Incomplete | None = None, function: Incomplete | None = None, vbProcedure: Incomplete | None = None, xlm: Incomplete | None = None, functionGroupId: Incomplete | None = None, shortcutKey: Incomplete | None = None, publishToServer: Incomplete | None = None, workbookParameter: Incomplete | None = None, attr_text: Incomplete | None = None) -> None: ...
    @property
    def type(self): ...
    @property
    def destinations(self) -> Generator[Incomplete, None, None]: ...
    @property
    def is_reserved(self): ...
    @property
    def is_external(self): ...
    def __iter__(self): ...

class DefinedNameDict(dict):
    """
    Utility class for storing defined names.
    Allows access by name and separation of global and scoped names
    """
    def __setitem__(self, key, value) -> None: ...
    def add(self, value) -> None:
        """
        Add names without worrying about key and name matching.
        """

class DefinedNameList(Serialisable):
    tagname: str
    definedName: Incomplete
    def __init__(self, definedName=()) -> None: ...
    def by_sheet(self):
        """
        Break names down into sheet locals and globals
        """
    def __len__(self) -> int: ...
