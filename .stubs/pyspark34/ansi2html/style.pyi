from _typeshed import Incomplete
from typing import Dict, List

class Rule:
    klass: Incomplete
    kw: Incomplete
    kwl: Incomplete
    def __init__(self, klass: str, **kw: str) -> None: ...

def index(r: int, g: int, b: int) -> str:
    """
    Implements the 6x6x6 color cube location of 8bit mode described at
    https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit
    """
def color_component(x: int) -> int:
    """
    Implements the 6x6x6 color cube values of 8bit mode described at
    https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit
    """
def color(r: int, g: int, b: int) -> str: ...
def level(grey: int) -> str:
    """
    Implements 24 grey values of 8bit mode described at
    https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit
    """
def index2(grey: int) -> str:
    """
    Implements 24 grey location of 8bit mode described at
    https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit
    """

SCHEME: Incomplete
truecolor_rules: List[Rule]

def intensify(color: str, dark_bg: bool, amount: int = 64) -> str: ...
def get_styles(dark_bg: bool = True, line_wrap: bool = True, scheme: str = 'ansi2html') -> List[Rule]: ...
def add_truecolor_style_rule(is_foreground: bool, ansi_code: int, r: int, g: int, b: int, parameter: str) -> None: ...
def pop_truecolor_styles() -> Dict[str, Rule]: ...
