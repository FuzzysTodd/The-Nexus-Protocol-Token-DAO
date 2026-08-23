from _typeshed import Incomplete
from ansi2html.style import SCHEME as SCHEME, add_truecolor_style_rule as add_truecolor_style_rule, get_styles as get_styles, pop_truecolor_styles as pop_truecolor_styles
from typing import List, Set, Tuple, TypedDict

ANSI_FULL_RESET: int
ANSI_INTENSITY_INCREASED: int
ANSI_INTENSITY_REDUCED: int
ANSI_INTENSITY_NORMAL: int
ANSI_STYLE_ITALIC: int
ANSI_STYLE_NORMAL: int
ANSI_BLINK_SLOW: int
ANSI_BLINK_FAST: int
ANSI_BLINK_OFF: int
ANSI_UNDERLINE_ON: int
ANSI_UNDERLINE_OFF: int
ANSI_CROSSED_OUT_ON: int
ANSI_CROSSED_OUT_OFF: int
ANSI_VISIBILITY_ON: int
ANSI_VISIBILITY_OFF: int
ANSI_FOREGROUND_CUSTOM_MIN: int
ANSI_FOREGROUND_CUSTOM_MAX: int
ANSI_FOREGROUND: int
ANSI_FOREGROUND_DEFAULT: int
ANSI_BACKGROUND_CUSTOM_MIN: int
ANSI_BACKGROUND_CUSTOM_MAX: int
ANSI_BACKGROUND: int
ANSI_BACKGROUND_DEFAULT: int
ANSI_NEGATIVE_ON: int
ANSI_NEGATIVE_OFF: int
ANSI_FOREGROUND_HIGH_INTENSITY_MIN: int
ANSI_FOREGROUND_HIGH_INTENSITY_MAX: int
ANSI_BACKGROUND_HIGH_INTENSITY_MIN: int
ANSI_BACKGROUND_HIGH_INTENSITY_MAX: int
ANSI_256_COLOR_ID: int
ANSI_TRUECOLOR_ID: int
VT100_BOX_CODES: Incomplete

class _State:
    inside_span: bool
    def __init__(self) -> None: ...
    intensity: Incomplete
    style: Incomplete
    blink: Incomplete
    underline: Incomplete
    crossedout: Incomplete
    visibility: Incomplete
    foreground: Incomplete
    background: Incomplete
    negative: Incomplete
    def reset(self) -> None: ...
    def adjust(self, ansi_code: int, parameter: str | None = None) -> None: ...
    def adjust_truecolor(self, ansi_code: int, r: int, g: int, b: int) -> None: ...
    def to_css_classes(self) -> List[str]: ...

class OSC_Link:
    url: Incomplete
    text: Incomplete
    def __init__(self, url: str, text: str) -> None: ...

def map_vt100_box_code(char: str) -> str: ...

class CursorMoveUp: ...

class Attributes(TypedDict):
    dark_bg: bool
    line_wrap: bool
    font_size: str
    body: str
    styles: Set[str]

class Ansi2HTMLConverter:
    '''Convert Ansi color codes to CSS+HTML

    Example:

    >>> conv = Ansi2HTMLConverter()
    >>> ansi = " ".join(sys.stdin.readlines())
    >>> html = conv.convert(ansi)
    '''
    latex: Incomplete
    inline: Incomplete
    dark_bg: Incomplete
    line_wrap: Incomplete
    font_size: Incomplete
    linkify: Incomplete
    escaped: Incomplete
    markup_lines: Incomplete
    output_encoding: Incomplete
    scheme: Incomplete
    title: Incomplete
    hyperref: bool
    styles: Incomplete
    vt100_box_codes_prog: Incomplete
    ansi_codes_prog: Incomplete
    url_matcher: Incomplete
    osc_link_re: Incomplete
    def __init__(self, latex: bool = False, inline: bool = False, dark_bg: bool = True, line_wrap: bool = True, font_size: str = 'normal', linkify: bool = False, escaped: bool = True, markup_lines: bool = False, output_encoding: str = 'utf-8', scheme: str = 'ansi2html', title: str = '') -> None: ...
    def do_linkify(self, line: str) -> str: ...
    def handle_osc_links(self, part: OSC_Link) -> str: ...
    def apply_regex(self, ansi: str) -> Tuple[str, Set[str]]: ...
    def prepare(self, ansi: str = '', ensure_trailing_newline: bool = False) -> Attributes:
        """Load the contents of 'ansi' into this object"""
    def convert(self, ansi: str, full: bool = True, ensure_trailing_newline: bool = False) -> str:
        """
        :param ansi: ANSI sequence to convert.
        :param full: Whether to include the full HTML document or only the body.
        :param ensure_trailing_newline: Ensures that ``\\n`` character is present at the end of the output.
        """
    def produce_headers(self) -> str: ...

def main() -> None:
    """
    $ ls --color=always | ansi2html > directories.html
    $ sudo tail /var/log/messages | ccze -A | ansi2html > logs.html
    $ task burndown | ansi2html > burndown.html
    """
