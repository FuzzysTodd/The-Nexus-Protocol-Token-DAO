from _typeshed import Incomplete
from openpyxl.compat import safe_string as safe_string
from openpyxl.descriptors import Bool as Bool, Integer as Integer, MinMax as MinMax, String as String, Typed as Typed
from openpyxl.descriptors.sequence import NestedSequence as NestedSequence
from openpyxl.descriptors.serialisable import Serialisable as Serialisable

COLOR_INDEX: Incomplete
BLACK: Incomplete
WHITE: Incomplete
BLUE: Incomplete
aRGB_REGEX: Incomplete

class RGB(Typed):
    """
    Descriptor for aRGB values
    If not supplied alpha is 00
    """
    expected_type = str
    def __set__(self, instance, value) -> None: ...

class Color(Serialisable):
    """Named colors for use in styles."""
    tagname: str
    rgb: Incomplete
    indexed: Incomplete
    auto: Incomplete
    theme: Incomplete
    tint: Incomplete
    type: Incomplete
    def __init__(self, rgb=..., indexed: Incomplete | None = None, auto: Incomplete | None = None, theme: Incomplete | None = None, tint: float = 0.0, index: Incomplete | None = None, type: str = 'rgb') -> None: ...
    @property
    def value(self): ...
    @value.setter
    def value(self, value) -> None: ...
    def __iter__(self): ...
    @property
    def index(self): ...
    def __add__(self, other):
        """
        Adding colours is undefined behaviour best do nothing
        """

class ColorDescriptor(Typed):
    expected_type = Color
    def __set__(self, instance, value) -> None: ...

class RgbColor(Serialisable):
    tagname: str
    rgb: Incomplete
    def __init__(self, rgb: Incomplete | None = None) -> None: ...

class ColorList(Serialisable):
    tagname: str
    indexedColors: Incomplete
    mruColors: Incomplete
    __elements__: Incomplete
    def __init__(self, indexedColors=(), mruColors=()) -> None: ...
    def __bool__(self) -> bool: ...
    @property
    def index(self): ...
