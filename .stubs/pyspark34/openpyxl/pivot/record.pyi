from .fields import Boolean as Boolean, DateTimeField as DateTimeField, Error as Error, Index as Index, Missing as Missing, Number as Number, Text as Text, TupleList as TupleList
from _typeshed import Incomplete
from openpyxl.descriptors import Integer as Integer, Sequence as Sequence, Typed as Typed
from openpyxl.descriptors.excel import ExtensionList as ExtensionList
from openpyxl.descriptors.nested import NestedBool as NestedBool, NestedInteger as NestedInteger
from openpyxl.descriptors.sequence import MultiSequence as MultiSequence, MultiSequencePart as MultiSequencePart
from openpyxl.descriptors.serialisable import Serialisable as Serialisable
from openpyxl.xml.constants import SHEET_MAIN_NS as SHEET_MAIN_NS
from openpyxl.xml.functions import tostring as tostring

class Record(Serialisable):
    tagname: str
    m: Incomplete
    n: Incomplete
    b: Incomplete
    e: Incomplete
    s: Incomplete
    d: Incomplete
    x: Incomplete
    def __init__(self, _fields=(), m: Incomplete | None = None, n: Incomplete | None = None, b: Incomplete | None = None, e: Incomplete | None = None, s: Incomplete | None = None, d: Incomplete | None = None, x: Incomplete | None = None) -> None: ...

class RecordList(Serialisable):
    mime_type: str
    rel_type: str
    tagname: str
    r: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    __attrs__: Incomplete
    def __init__(self, count: Incomplete | None = None, r=(), extLst: Incomplete | None = None) -> None: ...
    @property
    def count(self): ...
    def to_tree(self): ...
    @property
    def path(self): ...
