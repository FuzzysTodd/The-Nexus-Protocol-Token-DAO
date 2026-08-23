from _typeshed import Incomplete
from enum import Enum
from prompt_toolkit.application import Application
from prompt_toolkit.filters import FilterOrBool
from prompt_toolkit.formatted_text import AnyFormattedText
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.layout.screen import Screen
from prompt_toolkit.output import ColorDepth, Output
from prompt_toolkit.styles import Attrs, BaseStyle, StyleTransformation
from typing import Any, Callable, Dict

__all__ = ['Renderer', 'print_formatted_text']

class HeightIsUnknownError(Exception):
    """Information unavailable. Did not yet receive the CPR response."""

class _StyleStringToAttrsCache(Dict[str, Attrs]):
    """
    A cache structure that maps style strings to :class:`.Attr`.
    (This is an important speed up.)
    """
    get_attrs_for_style_str: Incomplete
    style_transformation: Incomplete
    def __init__(self, get_attrs_for_style_str: Callable[[str], Attrs], style_transformation: StyleTransformation) -> None: ...
    def __missing__(self, style_str: str) -> Attrs: ...

class _StyleStringHasStyleCache(Dict[str, bool]):
    """
    Cache for remember which style strings don't render the default output
    style (default fg/bg, no underline and no reverse and no blink). That way
    we know that we should render these cells, even when they're empty (when
    they contain a space).

    Note: we don't consider bold/italic/hidden because they don't change the
    output if there's no text in the cell.
    """
    style_string_to_attrs: Incomplete
    def __init__(self, style_string_to_attrs: dict[str, Attrs]) -> None: ...
    def __missing__(self, style_str: str) -> bool: ...

class CPR_Support(Enum):
    """Enum: whether or not CPR is supported."""
    SUPPORTED: str
    NOT_SUPPORTED: str
    UNKNOWN: str

class Renderer:
    """
    Typical usage:

    ::

        output = Vt100_Output.from_pty(sys.stdout)
        r = Renderer(style, output)
        r.render(app, layout=...)
    """
    CPR_TIMEOUT: int
    style: Incomplete
    output: Incomplete
    full_screen: Incomplete
    mouse_support: Incomplete
    cpr_not_supported_callback: Incomplete
    cpr_support: Incomplete
    def __init__(self, style: BaseStyle, output: Output, full_screen: bool = False, mouse_support: FilterOrBool = False, cpr_not_supported_callback: Callable[[], None] | None = None) -> None: ...
    mouse_handlers: Incomplete
    def reset(self, _scroll: bool = False, leave_alternate_screen: bool = True) -> None: ...
    @property
    def last_rendered_screen(self) -> Screen | None:
        """
        The `Screen` class that was generated during the last rendering.
        This can be `None`.
        """
    @property
    def height_is_known(self) -> bool:
        """
        True when the height from the cursor until the bottom of the terminal
        is known. (It's often nicer to draw bottom toolbars only if the height
        is known, in order to avoid flickering when the CPR response arrives.)
        """
    @property
    def rows_above_layout(self) -> int:
        """
        Return the number of rows visible in the terminal above the layout.
        """
    def request_absolute_cursor_position(self) -> None:
        """
        Get current cursor position.

        We do this to calculate the minimum available height that we can
        consume for rendering the prompt. This is the available space below te
        cursor.

        For vt100: Do CPR request. (answer will arrive later.)
        For win32: Do API call. (Answer comes immediately.)
        """
    def report_absolute_cursor_row(self, row: int) -> None:
        '''
        To be called when we know the absolute cursor position.
        (As an answer of a "Cursor Position Request" response.)
        '''
    @property
    def waiting_for_cpr(self) -> bool:
        """
        Waiting for CPR flag. True when we send the request, but didn't got a
        response.
        """
    async def wait_for_cpr_responses(self, timeout: int = 1) -> None:
        """
        Wait for a CPR response.
        """
    def render(self, app: Application[Any], layout: Layout, is_done: bool = False) -> None:
        """
        Render the current interface to the output.

        :param is_done: When True, put the cursor at the end of the interface. We
                won't print any changes to this part.
        """
    def erase(self, leave_alternate_screen: bool = True) -> None:
        """
        Hide all output and put the cursor back at the first line. This is for
        instance used for running a system command (while hiding the CLI) and
        later resuming the same CLI.)

        :param leave_alternate_screen: When True, and when inside an alternate
            screen buffer, quit the alternate screen.
        """
    def clear(self) -> None:
        """
        Clear screen and go to 0,0
        """

def print_formatted_text(output: Output, formatted_text: AnyFormattedText, style: BaseStyle, style_transformation: StyleTransformation | None = None, color_depth: ColorDepth | None = None) -> None:
    """
    Print a list of (style_str, text) tuples in the given style to the output.
    """
