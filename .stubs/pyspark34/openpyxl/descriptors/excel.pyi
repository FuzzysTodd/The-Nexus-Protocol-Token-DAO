from . import Integer as Integer, MatchPattern as MatchPattern, MinMax as MinMax, Sequence as Sequence, String as String
from .serialisable import Serialisable as Serialisable
from _typeshed import Incomplete
from openpyxl.compat import safe_string as safe_string
from openpyxl.xml.constants import REL_NS as REL_NS
from openpyxl.xml.functions import Element as Element

class HexBinary(MatchPattern):
    pattern: str

class UniversalMeasure(MatchPattern):
    pattern: str

class TextPoint(MinMax):
    """
    Size in hundredths of points.
    In theory other units of measurement can be used but these are unbounded
    """
    expected_type = int
    min: int
    max: int
Coordinate = Integer

class Percentage(MinMax):
    pattern: str
    min: int
    max: int
    def __set__(self, instance, value) -> None: ...

class Extension(Serialisable):
    uri: Incomplete
    def __init__(self, uri: Incomplete | None = None) -> None: ...

class ExtensionList(Serialisable):
    ext: Incomplete
    def __init__(self, ext=()) -> None: ...

class Relation(String):
    namespace = REL_NS
    allow_none: bool

class Base64Binary(MatchPattern):
    pattern: str

class Guid(MatchPattern):
    pattern: str

class CellRange(MatchPattern):
    pattern: str
    allow_none: bool
    def __set__(self, instance, value) -> None: ...
