from .colors import ColorDescriptor as ColorDescriptor
from _typeshed import Incomplete
from openpyxl.compat import safe_string as safe_string
from openpyxl.descriptors import Alias as Alias, Bool as Bool, Integer as Integer, NoneSet as NoneSet, Sequence as Sequence, Typed as Typed
from openpyxl.descriptors.serialisable import Serialisable as Serialisable

BORDER_NONE: Incomplete
BORDER_DASHDOT: str
BORDER_DASHDOTDOT: str
BORDER_DASHED: str
BORDER_DOTTED: str
BORDER_DOUBLE: str
BORDER_HAIR: str
BORDER_MEDIUM: str
BORDER_MEDIUMDASHDOT: str
BORDER_MEDIUMDASHDOTDOT: str
BORDER_MEDIUMDASHED: str
BORDER_SLANTDASHDOT: str
BORDER_THICK: str
BORDER_THIN: str

class Side(Serialisable):
    """Border options for use in styles.
    Caution: if you do not specify a border_style, other attributes will
    have no effect !"""
    __fields__: Incomplete
    color: Incomplete
    style: Incomplete
    border_style: Incomplete
    def __init__(self, style: Incomplete | None = None, color: Incomplete | None = None, border_style: Incomplete | None = None) -> None: ...

class Border(Serialisable):
    """Border positioning for use in styles."""
    tagname: str
    __fields__: Incomplete
    __elements__: Incomplete
    start: Incomplete
    end: Incomplete
    left: Incomplete
    right: Incomplete
    top: Incomplete
    bottom: Incomplete
    diagonal: Incomplete
    vertical: Incomplete
    horizontal: Incomplete
    outline: Incomplete
    diagonalUp: Incomplete
    diagonalDown: Incomplete
    diagonal_direction: Incomplete
    def __init__(self, left: Incomplete | None = None, right: Incomplete | None = None, top: Incomplete | None = None, bottom: Incomplete | None = None, diagonal: Incomplete | None = None, diagonal_direction: Incomplete | None = None, vertical: Incomplete | None = None, horizontal: Incomplete | None = None, diagonalUp: bool = False, diagonalDown: bool = False, outline: bool = True, start: Incomplete | None = None, end: Incomplete | None = None) -> None: ...
    def __iter__(self): ...

DEFAULT_BORDER: Incomplete
