from .colors import Color as Color, ColorDescriptor as ColorDescriptor
from _typeshed import Incomplete
from openpyxl.compat import safe_string as safe_string
from openpyxl.descriptors import Alias as Alias, Float as Float, Integer as Integer, MinMax as MinMax, NoneSet as NoneSet, Sequence as Sequence, Set as Set
from openpyxl.descriptors.serialisable import Serialisable as Serialisable
from openpyxl.xml.constants import SHEET_MAIN_NS as SHEET_MAIN_NS
from openpyxl.xml.functions import Element as Element, localname as localname

FILL_NONE: str
FILL_SOLID: str
FILL_PATTERN_DARKDOWN: str
FILL_PATTERN_DARKGRAY: str
FILL_PATTERN_DARKGRID: str
FILL_PATTERN_DARKHORIZONTAL: str
FILL_PATTERN_DARKTRELLIS: str
FILL_PATTERN_DARKUP: str
FILL_PATTERN_DARKVERTICAL: str
FILL_PATTERN_GRAY0625: str
FILL_PATTERN_GRAY125: str
FILL_PATTERN_LIGHTDOWN: str
FILL_PATTERN_LIGHTGRAY: str
FILL_PATTERN_LIGHTGRID: str
FILL_PATTERN_LIGHTHORIZONTAL: str
FILL_PATTERN_LIGHTTRELLIS: str
FILL_PATTERN_LIGHTUP: str
FILL_PATTERN_LIGHTVERTICAL: str
FILL_PATTERN_MEDIUMGRAY: str
fills: Incomplete

class Fill(Serialisable):
    """Base class"""
    tagname: str
    @classmethod
    def from_tree(cls, el): ...

class PatternFill(Fill):
    """Area fill patterns for use in styles.
    Caution: if you do not specify a fill_type, other attributes will have
    no effect !"""
    tagname: str
    __elements__: Incomplete
    patternType: Incomplete
    fill_type: Incomplete
    fgColor: Incomplete
    start_color: Incomplete
    bgColor: Incomplete
    end_color: Incomplete
    def __init__(self, patternType: Incomplete | None = None, fgColor=..., bgColor=..., fill_type: Incomplete | None = None, start_color: Incomplete | None = None, end_color: Incomplete | None = None) -> None: ...
    def to_tree(self, tagname: Incomplete | None = None, idx: Incomplete | None = None): ...

DEFAULT_EMPTY_FILL: Incomplete
DEFAULT_GRAY_FILL: Incomplete

class Stop(Serialisable):
    tagname: str
    position: Incomplete
    color: Incomplete
    def __init__(self, color, position) -> None: ...

class StopList(Sequence):
    expected_type = Stop
    def __set__(self, obj, values) -> None: ...

class GradientFill(Fill):
    '''Fill areas with gradient

    Two types of gradient fill are supported:

        - A type=\'linear\' gradient interpolates colours between
          a set of specified Stops, across the length of an area.
          The gradient is left-to-right by default, but this
          orientation can be modified with the degree
          attribute.  A list of Colors can be provided instead
          and they will be positioned with equal distance between them.

        - A type=\'path\' gradient applies a linear gradient from each
          edge of the area. Attributes top, right, bottom, left specify
          the extent of fill from the respective borders. Thus top="0.2"
          will fill the top 20% of the cell.

    '''
    tagname: str
    type: Incomplete
    fill_type: Incomplete
    degree: Incomplete
    left: Incomplete
    right: Incomplete
    top: Incomplete
    bottom: Incomplete
    stop: Incomplete
    def __init__(self, type: str = 'linear', degree: int = 0, left: int = 0, right: int = 0, top: int = 0, bottom: int = 0, stop=()) -> None: ...
    def __iter__(self): ...
    def to_tree(self, tagname: Incomplete | None = None, namespace: Incomplete | None = None, idx: Incomplete | None = None): ...
