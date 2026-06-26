from .errors import ColorError as ColorError
from .typing import CallableGenerator as CallableGenerator, ReprArgs as ReprArgs
from .utils import Representation as Representation, almost_equal_floats as almost_equal_floats
from _typeshed import Incomplete
from typing import Any, Dict, Tuple

ColorTuple = Tuple[int, int, int] | Tuple[int, int, int, float]
ColorType = ColorTuple | str
HslColorTuple = Tuple[float, float, float] | Tuple[float, float, float, float]

class RGBA:
    """
    Internal use only as a representation of a color.
    """
    r: Incomplete
    g: Incomplete
    b: Incomplete
    alpha: Incomplete
    def __init__(self, r: float, g: float, b: float, alpha: float | None) -> None: ...
    def __getitem__(self, item: Any) -> Any: ...

r_hex_short: str
r_hex_long: str
r_rgb: Incomplete
r_rgba: Incomplete
r_hsl: Incomplete
r_hsla: Incomplete
repeat_colors: Incomplete
rads: Incomplete

class Color(Representation):
    def __init__(self, value: ColorType) -> None: ...
    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None: ...
    def original(self) -> ColorType:
        """
        Original value passed to Color
        """
    def as_named(self, *, fallback: bool = False) -> str: ...
    def as_hex(self) -> str:
        '''
        Hex string representing the color can be 3, 4, 6 or 8 characters depending on whether the string
        a "short" representation of the color is possible and whether there\'s an alpha channel.
        '''
    def as_rgb(self) -> str:
        """
        Color as an rgb(<r>, <g>, <b>) or rgba(<r>, <g>, <b>, <a>) string.
        """
    def as_rgb_tuple(self, *, alpha: bool | None = None) -> ColorTuple:
        """
        Color as an RGB or RGBA tuple; red, green and blue are in the range 0 to 255, alpha if included is
        in the range 0 to 1.

        :param alpha: whether to include the alpha channel, options are
          None - (default) include alpha only if it's set (e.g. not None)
          True - always include alpha,
          False - always omit alpha,
        """
    def as_hsl(self) -> str:
        """
        Color as an hsl(<h>, <s>, <l>) or hsl(<h>, <s>, <l>, <a>) string.
        """
    def as_hsl_tuple(self, *, alpha: bool | None = None) -> HslColorTuple:
        """
        Color as an HSL or HSLA tuple, e.g. hue, saturation, lightness and optionally alpha; all elements are in
        the range 0 to 1.

        NOTE: this is HSL as used in HTML and most other places, not HLS as used in python's colorsys.

        :param alpha: whether to include the alpha channel, options are
          None - (default) include alpha only if it's set (e.g. not None)
          True - always include alpha,
          False - always omit alpha,
        """
    @classmethod
    def __get_validators__(cls) -> CallableGenerator: ...
    def __repr_args__(self) -> ReprArgs: ...
    def __eq__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...

def parse_tuple(value: Tuple[Any, ...]) -> RGBA:
    """
    Parse a tuple or list as a color.
    """
def parse_str(value: str) -> RGBA:
    """
    Parse a string to an RGBA tuple, trying the following formats (in this order):
    * named color, see COLORS_BY_NAME below
    * hex short eg. `<prefix>fff` (prefix can be `#`, `0x` or nothing)
    * hex long eg. `<prefix>ffffff` (prefix can be `#`, `0x` or nothing)
    * `rgb(<r>, <g>, <b>) `
    * `rgba(<r>, <g>, <b>, <a>)`
    """
def ints_to_rgba(r: int | str, g: int | str, b: int | str, alpha: float | None) -> RGBA: ...
def parse_color_value(value: int | str, max_val: int = 255) -> float:
    """
    Parse a value checking it's a valid int in the range 0 to max_val and divide by max_val to give a number
    in the range 0 to 1
    """
def parse_float_alpha(value: None | str | float | int) -> float | None:
    """
    Parse a value checking it's a valid float in the range 0 to 1
    """
def parse_hsl(h: str, h_units: str, sat: str, light: str, alpha: float | None = None) -> RGBA:
    """
    Parse raw hue, saturation, lightness and alpha values and convert to RGBA.
    """
def float_to_255(c: float) -> int: ...

COLORS_BY_NAME: Incomplete
COLORS_BY_VALUE: Incomplete
