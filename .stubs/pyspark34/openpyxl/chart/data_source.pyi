from _typeshed import Incomplete
from openpyxl.descriptors import Alias as Alias, Bool as Bool, Integer as Integer, Sequence as Sequence, String as String, Typed as Typed
from openpyxl.descriptors.excel import ExtensionList as ExtensionList
from openpyxl.descriptors.nested import NestedInteger as NestedInteger, NestedString as NestedString, NestedText as NestedText
from openpyxl.descriptors.serialisable import Serialisable as Serialisable

class NumFmt(Serialisable):
    formatCode: Incomplete
    sourceLinked: Incomplete
    def __init__(self, formatCode: Incomplete | None = None, sourceLinked: bool = False) -> None: ...

class NumberValueDescriptor(NestedText):
    """
    Data should be numerical but isn't always :-/
    """
    allow_none: bool
    expected_type: Incomplete
    def __set__(self, instance, value) -> None: ...

class NumVal(Serialisable):
    idx: Incomplete
    formatCode: Incomplete
    v: Incomplete
    def __init__(self, idx: Incomplete | None = None, formatCode: Incomplete | None = None, v: Incomplete | None = None) -> None: ...

class NumData(Serialisable):
    formatCode: Incomplete
    ptCount: Incomplete
    pt: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(self, formatCode: Incomplete | None = None, ptCount: Incomplete | None = None, pt=(), extLst: Incomplete | None = None) -> None: ...

class NumRef(Serialisable):
    f: Incomplete
    ref: Incomplete
    numCache: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(self, f: Incomplete | None = None, numCache: Incomplete | None = None, extLst: Incomplete | None = None) -> None: ...

class StrVal(Serialisable):
    tagname: str
    idx: Incomplete
    v: Incomplete
    def __init__(self, idx: int = 0, v: Incomplete | None = None) -> None: ...

class StrData(Serialisable):
    tagname: str
    ptCount: Incomplete
    pt: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(self, ptCount: Incomplete | None = None, pt=(), extLst: Incomplete | None = None) -> None: ...

class StrRef(Serialisable):
    tagname: str
    f: Incomplete
    strCache: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(self, f: Incomplete | None = None, strCache: Incomplete | None = None, extLst: Incomplete | None = None) -> None: ...

class NumDataSource(Serialisable):
    numRef: Incomplete
    numLit: Incomplete
    def __init__(self, numRef: Incomplete | None = None, numLit: Incomplete | None = None) -> None: ...

class Level(Serialisable):
    tagname: str
    pt: Incomplete
    __elements__: Incomplete
    def __init__(self, pt=()) -> None: ...

class MultiLevelStrData(Serialisable):
    tagname: str
    ptCount: Incomplete
    lvl: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(self, ptCount: Incomplete | None = None, lvl=(), extLst: Incomplete | None = None) -> None: ...

class MultiLevelStrRef(Serialisable):
    tagname: str
    f: Incomplete
    multiLvlStrCache: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(self, f: Incomplete | None = None, multiLvlStrCache: Incomplete | None = None, extLst: Incomplete | None = None) -> None: ...

class AxDataSource(Serialisable):
    tagname: str
    numRef: Incomplete
    numLit: Incomplete
    strRef: Incomplete
    strLit: Incomplete
    multiLvlStrRef: Incomplete
    def __init__(self, numRef: Incomplete | None = None, numLit: Incomplete | None = None, strRef: Incomplete | None = None, strLit: Incomplete | None = None, multiLvlStrRef: Incomplete | None = None) -> None: ...
