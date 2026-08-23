import abc
import threading
from . import errors as errors, themes as themes
from ._export_format import CONSOLE_HTML_FORMAT as CONSOLE_HTML_FORMAT, CONSOLE_SVG_FORMAT as CONSOLE_SVG_FORMAT
from ._fileno import get_fileno as get_fileno
from ._log_render import FormatTimeCallable as FormatTimeCallable, LogRender as LogRender
from ._windows import WindowsConsoleFeatures as WindowsConsoleFeatures
from .align import Align as Align, AlignMethod as AlignMethod
from .color import ColorSystem as ColorSystem, blend_rgb as blend_rgb
from .control import Control as Control
from .emoji import EmojiVariant as EmojiVariant
from .highlighter import NullHighlighter as NullHighlighter, ReprHighlighter as ReprHighlighter
from .live import Live as Live
from .measure import Measurement as Measurement, measure_renderables as measure_renderables
from .pager import Pager as Pager, SystemPager as SystemPager
from .pretty import Pretty as Pretty, is_expandable as is_expandable
from .protocol import rich_cast as rich_cast
from .region import Region as Region
from .scope import render_scope as render_scope
from .screen import Screen as Screen
from .segment import Segment as Segment
from .status import Status as Status
from .style import Style as Style, StyleType as StyleType
from .styled import Styled as Styled
from .terminal_theme import DEFAULT_TERMINAL_THEME as DEFAULT_TERMINAL_THEME, SVG_EXPORT_THEME as SVG_EXPORT_THEME, TerminalTheme as TerminalTheme
from .text import Text as Text, TextType as TextType
from .theme import Theme as Theme, ThemeStack as ThemeStack
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from rich._null_file import NULL_FILE as NULL_FILE
from types import ModuleType, TracebackType
from typing import Any, Callable, IO, Iterable, List, Literal, Mapping, NamedTuple, Protocol, TextIO, Tuple, Type

JUPYTER_DEFAULT_COLUMNS: int
JUPYTER_DEFAULT_LINES: int
WINDOWS: Incomplete
HighlighterType: Incomplete
JustifyMethod: Incomplete
OverflowMethod: Incomplete

class NoChange: ...

NO_CHANGE: Incomplete

class ConsoleDimensions(NamedTuple):
    """Size of the terminal."""
    width: int
    height: int

@dataclass
class ConsoleOptions:
    """Options for __rich_console__ method."""
    size: ConsoleDimensions
    legacy_windows: bool
    min_width: int
    max_width: int
    is_terminal: bool
    encoding: str
    max_height: int
    justify: JustifyMethod | None = ...
    overflow: OverflowMethod | None = ...
    no_wrap: bool | None = ...
    highlight: bool | None = ...
    markup: bool | None = ...
    height: int | None = ...
    @property
    def ascii_only(self) -> bool:
        """Check if renderables should use ascii only."""
    def copy(self) -> ConsoleOptions:
        """Return a copy of the options.

        Returns:
            ConsoleOptions: a copy of self.
        """
    def update(self, *, width: int | NoChange = ..., min_width: int | NoChange = ..., max_width: int | NoChange = ..., justify: JustifyMethod | None | NoChange = ..., overflow: OverflowMethod | None | NoChange = ..., no_wrap: bool | None | NoChange = ..., highlight: bool | None | NoChange = ..., markup: bool | None | NoChange = ..., height: int | None | NoChange = ...) -> ConsoleOptions:
        """Update values, return a copy."""
    def update_width(self, width: int) -> ConsoleOptions:
        """Update just the width, return a copy.

        Args:
            width (int): New width (sets both min_width and max_width)

        Returns:
            ~ConsoleOptions: New console options instance.
        """
    def update_height(self, height: int) -> ConsoleOptions:
        """Update the height, and return a copy.

        Args:
            height (int): New height

        Returns:
            ~ConsoleOptions: New Console options instance.
        """
    def reset_height(self) -> ConsoleOptions:
        """Return a copy of the options with height set to ``None``.

        Returns:
            ~ConsoleOptions: New console options instance.
        """
    def update_dimensions(self, width: int, height: int) -> ConsoleOptions:
        """Update the width and height, and return a copy.

        Args:
            width (int): New width (sets both min_width and max_width).
            height (int): New height.

        Returns:
            ~ConsoleOptions: New console options instance.
        """
    def __init__(self, size, legacy_windows, min_width, max_width, is_terminal, encoding, max_height, justify, overflow, no_wrap, highlight, markup, height) -> None: ...

class RichCast(Protocol):
    """An object that may be 'cast' to a console renderable."""
    def __rich__(self) -> ConsoleRenderable | RichCast | str: ...

class ConsoleRenderable(Protocol):
    """An object that supports the console protocol."""
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
RenderableType = ConsoleRenderable | RichCast | str
RenderResult = Iterable[RenderableType | Segment]

class CaptureError(Exception):
    """An error in the Capture context manager."""

class NewLine:
    """A renderable to generate new line(s)"""
    count: Incomplete
    def __init__(self, count: int = 1) -> None: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> Iterable[Segment]: ...

class ScreenUpdate:
    """Render a list of lines at a given offset."""
    x: Incomplete
    y: Incomplete
    def __init__(self, lines: List[List[Segment]], x: int, y: int) -> None: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...

class Capture:
    """Context manager to capture the result of printing to the console.
    See :meth:`~rich.console.Console.capture` for how to use.

    Args:
        console (Console): A console instance to capture output.
    """
    def __init__(self, console: Console) -> None: ...
    def __enter__(self) -> Capture: ...
    def __exit__(self, exc_type: Type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> None: ...
    def get(self) -> str:
        """Get the result of the capture."""

class ThemeContext:
    """A context manager to use a temporary theme. See :meth:`~rich.console.Console.use_theme` for usage."""
    console: Incomplete
    theme: Incomplete
    inherit: Incomplete
    def __init__(self, console: Console, theme: Theme, inherit: bool = True) -> None: ...
    def __enter__(self) -> ThemeContext: ...
    def __exit__(self, exc_type: Type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> None: ...

class PagerContext:
    """A context manager that 'pages' content. See :meth:`~rich.console.Console.pager` for usage."""
    pager: Incomplete
    styles: Incomplete
    links: Incomplete
    def __init__(self, console: Console, pager: Pager | None = None, styles: bool = False, links: bool = False) -> None: ...
    def __enter__(self) -> PagerContext: ...
    def __exit__(self, exc_type: Type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> None: ...

class ScreenContext:
    """A context manager that enables an alternative screen. See :meth:`~rich.console.Console.screen` for usage."""
    console: Incomplete
    hide_cursor: Incomplete
    screen: Incomplete
    def __init__(self, console: Console, hide_cursor: bool, style: StyleType = '') -> None: ...
    def update(self, *renderables: RenderableType, style: StyleType | None = None) -> None:
        """Update the screen.

        Args:
            renderable (RenderableType, optional): Optional renderable to replace current renderable,
                or None for no change. Defaults to None.
            style: (Style, optional): Replacement style, or None for no change. Defaults to None.
        """
    def __enter__(self) -> ScreenContext: ...
    def __exit__(self, exc_type: Type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> None: ...

class Group:
    """Takes a group of renderables and returns a renderable object that renders the group.

    Args:
        renderables (Iterable[RenderableType]): An iterable of renderable objects.
        fit (bool, optional): Fit dimension of group to contents, or fill available space. Defaults to True.
    """
    fit: Incomplete
    def __init__(self, *renderables: RenderableType, fit: bool = True) -> None: ...
    @property
    def renderables(self) -> List['RenderableType']: ...
    def __rich_measure__(self, console: Console, options: ConsoleOptions) -> Measurement: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...

def group(fit: bool = True) -> Callable[..., Callable[..., Group]]:
    """A decorator that turns an iterable of renderables in to a group.

    Args:
        fit (bool, optional): Fit dimension of group to contents, or fill available space. Defaults to True.
    """

COLOR_SYSTEMS: Incomplete

@dataclass
class ConsoleThreadLocals(threading.local):
    """Thread local values for Console context."""
    theme_stack: ThemeStack
    buffer: List[Segment] = ...
    buffer_index: int = ...
    def __init__(self, theme_stack, buffer, buffer_index) -> None: ...

class RenderHook(ABC, metaclass=abc.ABCMeta):
    """Provides hooks in to the render process."""
    @abstractmethod
    def process_renderables(self, renderables: List[ConsoleRenderable]) -> List[ConsoleRenderable]:
        """Called with a list of objects to render.

        This method can return a new list of renderables, or modify and return the same list.

        Args:
            renderables (List[ConsoleRenderable]): A number of renderable objects.

        Returns:
            List[ConsoleRenderable]: A replacement list of renderables.
        """

def get_windows_console_features() -> WindowsConsoleFeatures: ...
def detect_legacy_windows() -> bool:
    """Detect legacy Windows."""

class Console:
    '''A high level console interface.

    Args:
        color_system (str, optional): The color system supported by your terminal,
            either ``"standard"``, ``"256"`` or ``"truecolor"``. Leave as ``"auto"`` to autodetect.
        force_terminal (Optional[bool], optional): Enable/disable terminal control codes, or None to auto-detect terminal. Defaults to None.
        force_jupyter (Optional[bool], optional): Enable/disable Jupyter rendering, or None to auto-detect Jupyter. Defaults to None.
        force_interactive (Optional[bool], optional): Enable/disable interactive mode, or None to auto detect. Defaults to None.
        soft_wrap (Optional[bool], optional): Set soft wrap default on print method. Defaults to False.
        theme (Theme, optional): An optional style theme object, or ``None`` for default theme.
        stderr (bool, optional): Use stderr rather than stdout if ``file`` is not specified. Defaults to False.
        file (IO, optional): A file object where the console should write to. Defaults to stdout.
        quiet (bool, Optional): Boolean to suppress all output. Defaults to False.
        width (int, optional): The width of the terminal. Leave as default to auto-detect width.
        height (int, optional): The height of the terminal. Leave as default to auto-detect height.
        style (StyleType, optional): Style to apply to all output, or None for no style. Defaults to None.
        no_color (Optional[bool], optional): Enabled no color mode, or None to auto detect. Defaults to None.
        tab_size (int, optional): Number of spaces used to replace a tab character. Defaults to 8.
        record (bool, optional): Boolean to enable recording of terminal output,
            required to call :meth:`export_html`, :meth:`export_svg`, and :meth:`export_text`. Defaults to False.
        markup (bool, optional): Boolean to enable :ref:`console_markup`. Defaults to True.
        emoji (bool, optional): Enable emoji code. Defaults to True.
        emoji_variant (str, optional): Optional emoji variant, either "text" or "emoji". Defaults to None.
        highlight (bool, optional): Enable automatic highlighting. Defaults to True.
        log_time (bool, optional): Boolean to enable logging of time by :meth:`log` methods. Defaults to True.
        log_path (bool, optional): Boolean to enable the logging of the caller by :meth:`log`. Defaults to True.
        log_time_format (Union[str, TimeFormatterCallable], optional): If ``log_time`` is enabled, either string for strftime or callable that formats the time. Defaults to "[%X] ".
        highlighter (HighlighterType, optional): Default highlighter.
        legacy_windows (bool, optional): Enable legacy Windows mode, or ``None`` to auto detect. Defaults to ``None``.
        safe_box (bool, optional): Restrict box options that don\'t render on legacy Windows.
        get_datetime (Callable[[], datetime], optional): Callable that gets the current time as a datetime.datetime object (used by Console.log),
            or None for datetime.now.
        get_time (Callable[[], time], optional): Callable that gets the current time in seconds, default uses time.monotonic.
    '''
    is_jupyter: Incomplete
    tab_size: Incomplete
    record: Incomplete
    legacy_windows: Incomplete
    soft_wrap: Incomplete
    quiet: Incomplete
    stderr: Incomplete
    highlighter: Incomplete
    safe_box: Incomplete
    get_datetime: Incomplete
    get_time: Incomplete
    style: Incomplete
    no_color: Incomplete
    is_interactive: Incomplete
    def __init__(self, *, color_system: Literal['auto', 'standard', '256', 'truecolor', 'windows'] | None = 'auto', force_terminal: bool | None = None, force_jupyter: bool | None = None, force_interactive: bool | None = None, soft_wrap: bool = False, theme: Theme | None = None, stderr: bool = False, file: IO[str] | None = None, quiet: bool = False, width: int | None = None, height: int | None = None, style: StyleType | None = None, no_color: bool | None = None, tab_size: int = 8, record: bool = False, markup: bool = True, emoji: bool = True, emoji_variant: EmojiVariant | None = None, highlight: bool = True, log_time: bool = True, log_path: bool = True, log_time_format: str | FormatTimeCallable = '[%X]', highlighter: HighlighterType | None = ..., legacy_windows: bool | None = None, safe_box: bool = True, get_datetime: Callable[[], datetime] | None = None, get_time: Callable[[], float] | None = None, _environ: Mapping[str, str] | None = None) -> None: ...
    @property
    def file(self) -> IO[str]:
        """Get the file object to write to."""
    @file.setter
    def file(self, new_file: IO[str]) -> None:
        """Set a new file object."""
    def set_live(self, live: Live) -> None:
        """Set Live instance. Used by Live context manager.

        Args:
            live (Live): Live instance using this Console.

        Raises:
            errors.LiveError: If this Console has a Live context currently active.
        """
    def clear_live(self) -> None:
        """Clear the Live instance."""
    def push_render_hook(self, hook: RenderHook) -> None:
        """Add a new render hook to the stack.

        Args:
            hook (RenderHook): Render hook instance.
        """
    def pop_render_hook(self) -> None:
        """Pop the last renderhook from the stack."""
    def __enter__(self) -> Console:
        """Own context manager to enter buffer context."""
    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None:
        """Exit buffer context."""
    def begin_capture(self) -> None:
        """Begin capturing console output. Call :meth:`end_capture` to exit capture mode and return output."""
    def end_capture(self) -> str:
        """End capture mode and return captured string.

        Returns:
            str: Console output.
        """
    def push_theme(self, theme: Theme, *, inherit: bool = True) -> None:
        """Push a new theme on to the top of the stack, replacing the styles from the previous theme.
        Generally speaking, you should call :meth:`~rich.console.Console.use_theme` to get a context manager, rather
        than calling this method directly.

        Args:
            theme (Theme): A theme instance.
            inherit (bool, optional): Inherit existing styles. Defaults to True.
        """
    def pop_theme(self) -> None:
        """Remove theme from top of stack, restoring previous theme."""
    def use_theme(self, theme: Theme, *, inherit: bool = True) -> ThemeContext:
        """Use a different theme for the duration of the context manager.

        Args:
            theme (Theme): Theme instance to user.
            inherit (bool, optional): Inherit existing console styles. Defaults to True.

        Returns:
            ThemeContext: [description]
        """
    @property
    def color_system(self) -> str | None:
        '''Get color system string.

        Returns:
            Optional[str]: "standard", "256" or "truecolor".
        '''
    @property
    def encoding(self) -> str:
        '''Get the encoding of the console file, e.g. ``"utf-8"``.

        Returns:
            str: A standard encoding string.
        '''
    @property
    def is_terminal(self) -> bool:
        """Check if the console is writing to a terminal.

        Returns:
            bool: True if the console writing to a device capable of
            understanding terminal codes, otherwise False.
        """
    @property
    def is_dumb_terminal(self) -> bool:
        """Detect dumb terminal.

        Returns:
            bool: True if writing to a dumb terminal, otherwise False.

        """
    @property
    def options(self) -> ConsoleOptions:
        """Get default console options."""
    @property
    def size(self) -> ConsoleDimensions:
        """Get the size of the console.

        Returns:
            ConsoleDimensions: A named tuple containing the dimensions.
        """
    @size.setter
    def size(self, new_size: Tuple[int, int]) -> None:
        """Set a new size for the terminal.

        Args:
            new_size (Tuple[int, int]): New width and height.
        """
    @property
    def width(self) -> int:
        """Get the width of the console.

        Returns:
            int: The width (in characters) of the console.
        """
    @width.setter
    def width(self, width: int) -> None:
        """Set width.

        Args:
            width (int): New width.
        """
    @property
    def height(self) -> int:
        """Get the height of the console.

        Returns:
            int: The height (in lines) of the console.
        """
    @height.setter
    def height(self, height: int) -> None:
        """Set height.

        Args:
            height (int): new height.
        """
    def bell(self) -> None:
        """Play a 'bell' sound (if supported by the terminal)."""
    def capture(self) -> Capture:
        '''A context manager to *capture* the result of print() or log() in a string,
        rather than writing it to the console.

        Example:
            >>> from rich.console import Console
            >>> console = Console()
            >>> with console.capture() as capture:
            ...     console.print("[bold magenta]Hello World[/]")
            >>> print(capture.get())

        Returns:
            Capture: Context manager with disables writing to the terminal.
        '''
    def pager(self, pager: Pager | None = None, styles: bool = False, links: bool = False) -> PagerContext:
        '''A context manager to display anything printed within a "pager". The pager application
        is defined by the system and will typically support at least pressing a key to scroll.

        Args:
            pager (Pager, optional): A pager object, or None to use :class:`~rich.pager.SystemPager`. Defaults to None.
            styles (bool, optional): Show styles in pager. Defaults to False.
            links (bool, optional): Show links in pager. Defaults to False.

        Example:
            >>> from rich.console import Console
            >>> from rich.__main__ import make_test_card
            >>> console = Console()
            >>> with console.pager():
                    console.print(make_test_card())

        Returns:
            PagerContext: A context manager.
        '''
    def line(self, count: int = 1) -> None:
        """Write new line(s).

        Args:
            count (int, optional): Number of new lines. Defaults to 1.
        """
    def clear(self, home: bool = True) -> None:
        """Clear the screen.

        Args:
            home (bool, optional): Also move the cursor to 'home' position. Defaults to True.
        """
    def status(self, status: RenderableType, *, spinner: str = 'dots', spinner_style: StyleType = 'status.spinner', speed: float = 1.0, refresh_per_second: float = 12.5) -> Status:
        '''Display a status and spinner.

        Args:
            status (RenderableType): A status renderable (str or Text typically).
            spinner (str, optional): Name of spinner animation (see python -m rich.spinner). Defaults to "dots".
            spinner_style (StyleType, optional): Style of spinner. Defaults to "status.spinner".
            speed (float, optional): Speed factor for spinner animation. Defaults to 1.0.
            refresh_per_second (float, optional): Number of refreshes per second. Defaults to 12.5.

        Returns:
            Status: A Status object that may be used as a context manager.
        '''
    def show_cursor(self, show: bool = True) -> bool:
        """Show or hide the cursor.

        Args:
            show (bool, optional): Set visibility of the cursor.
        """
    def set_alt_screen(self, enable: bool = True) -> bool:
        """Enables alternative screen mode.

        Note, if you enable this mode, you should ensure that is disabled before
        the application exits. See :meth:`~rich.Console.screen` for a context manager
        that handles this for you.

        Args:
            enable (bool, optional): Enable (True) or disable (False) alternate screen. Defaults to True.

        Returns:
            bool: True if the control codes were written.

        """
    @property
    def is_alt_screen(self) -> bool:
        """Check if the alt screen was enabled.

        Returns:
            bool: True if the alt screen was enabled, otherwise False.
        """
    def set_window_title(self, title: str) -> bool:
        '''Set the title of the console terminal window.

        Warning: There is no means within Rich of "resetting" the window title to its
        previous value, meaning the title you set will persist even after your application
        exits.

        ``fish`` shell resets the window title before and after each command by default,
        negating this issue. Windows Terminal and command prompt will also reset the title for you.
        Most other shells and terminals, however, do not do this.

        Some terminals may require configuration changes before you can set the title.
        Some terminals may not support setting the title at all.

        Other software (including the terminal itself, the shell, custom prompts, plugins, etc.)
        may also set the terminal window title. This could result in whatever value you write
        using this method being overwritten.

        Args:
            title (str): The new title of the terminal window.

        Returns:
            bool: True if the control code to change the terminal title was
                written, otherwise False. Note that a return value of True
                does not guarantee that the window title has actually changed,
                since the feature may be unsupported/disabled in some terminals.
        '''
    def screen(self, hide_cursor: bool = True, style: StyleType | None = None) -> ScreenContext:
        """Context manager to enable and disable 'alternative screen' mode.

        Args:
            hide_cursor (bool, optional): Also hide the cursor. Defaults to False.
            style (Style, optional): Optional style for screen. Defaults to None.

        Returns:
            ~ScreenContext: Context which enables alternate screen on enter, and disables it on exit.
        """
    def measure(self, renderable: RenderableType, *, options: ConsoleOptions | None = None) -> Measurement:
        """Measure a renderable. Returns a :class:`~rich.measure.Measurement` object which contains
        information regarding the number of characters required to print the renderable.

        Args:
            renderable (RenderableType): Any renderable or string.
            options (Optional[ConsoleOptions], optional): Options to use when measuring, or None
                to use default options. Defaults to None.

        Returns:
            Measurement: A measurement of the renderable.
        """
    def render(self, renderable: RenderableType, options: ConsoleOptions | None = None) -> Iterable[Segment]:
        """Render an object in to an iterable of `Segment` instances.

        This method contains the logic for rendering objects with the console protocol.
        You are unlikely to need to use it directly, unless you are extending the library.

        Args:
            renderable (RenderableType): An object supporting the console protocol, or
                an object that may be converted to a string.
            options (ConsoleOptions, optional): An options object, or None to use self.options. Defaults to None.

        Returns:
            Iterable[Segment]: An iterable of segments that may be rendered.
        """
    def render_lines(self, renderable: RenderableType, options: ConsoleOptions | None = None, *, style: Style | None = None, pad: bool = True, new_lines: bool = False) -> List[List[Segment]]:
        '''Render objects in to a list of lines.

        The output of render_lines is useful when further formatting of rendered console text
        is required, such as the Panel class which draws a border around any renderable object.

        Args:
            renderable (RenderableType): Any object renderable in the console.
            options (Optional[ConsoleOptions], optional): Console options, or None to use self.options. Default to ``None``.
            style (Style, optional): Optional style to apply to renderables. Defaults to ``None``.
            pad (bool, optional): Pad lines shorter than render width. Defaults to ``True``.
            new_lines (bool, optional): Include "
" characters at end of lines.

        Returns:
            List[List[Segment]]: A list of lines, where a line is a list of Segment objects.
        '''
    def render_str(self, text: str, *, style: str | Style = '', justify: JustifyMethod | None = None, overflow: OverflowMethod | None = None, emoji: bool | None = None, markup: bool | None = None, highlight: bool | None = None, highlighter: HighlighterType | None = None) -> Text:
        '''Convert a string to a Text instance. This is called automatically if
        you print or log a string.

        Args:
            text (str): Text to render.
            style (Union[str, Style], optional): Style to apply to rendered text.
            justify (str, optional): Justify method: "default", "left", "center", "full", or "right". Defaults to ``None``.
            overflow (str, optional): Overflow method: "crop", "fold", or "ellipsis". Defaults to ``None``.
            emoji (Optional[bool], optional): Enable emoji, or ``None`` to use Console default.
            markup (Optional[bool], optional): Enable markup, or ``None`` to use Console default.
            highlight (Optional[bool], optional): Enable highlighting, or ``None`` to use Console default.
            highlighter (HighlighterType, optional): Optional highlighter to apply.
        Returns:
            ConsoleRenderable: Renderable object.

        '''
    def get_style(self, name: str | Style, *, default: Style | str | None = None) -> Style:
        """Get a Style instance by its theme name or parse a definition.

        Args:
            name (str): The name of a style or a style definition.

        Returns:
            Style: A Style object.

        Raises:
            MissingStyle: If no style could be parsed from name.

        """
    def rule(self, title: TextType = '', *, characters: str = '─', style: str | Style = 'rule.line', align: AlignMethod = 'center') -> None:
        '''Draw a line with optional centered title.

        Args:
            title (str, optional): Text to render over the rule. Defaults to "".
            characters (str, optional): Character(s) to form the line. Defaults to "─".
            style (str, optional): Style of line. Defaults to "rule.line".
            align (str, optional): How to align the title, one of "left", "center", or "right". Defaults to "center".
        '''
    def control(self, *control: Control) -> None:
        """Insert non-printing control codes.

        Args:
            control_codes (str): Control codes, such as those that may move the cursor.
        """
    def out(self, *objects: Any, sep: str = ' ', end: str = '\n', style: str | Style | None = None, highlight: bool | None = None) -> None:
        '''Output to the terminal. This is a low-level way of writing to the terminal which unlike
        :meth:`~rich.console.Console.print` won\'t pretty print, wrap text, or apply markup, but will
        optionally apply highlighting and a basic style.

        Args:
            sep (str, optional): String to write between print data. Defaults to " ".
            end (str, optional): String to write at end of print data. Defaults to "\\\\n".
            style (Union[str, Style], optional): A style to apply to output. Defaults to None.
            highlight (Optional[bool], optional): Enable automatic highlighting, or ``None`` to use
                console default. Defaults to ``None``.
        '''
    def print(self, *objects: Any, sep: str = ' ', end: str = '\n', style: str | Style | None = None, justify: JustifyMethod | None = None, overflow: OverflowMethod | None = None, no_wrap: bool | None = None, emoji: bool | None = None, markup: bool | None = None, highlight: bool | None = None, width: int | None = None, height: int | None = None, crop: bool = True, soft_wrap: bool | None = None, new_line_start: bool = False) -> None:
        '''Print to the console.

        Args:
            objects (positional args): Objects to log to the terminal.
            sep (str, optional): String to write between print data. Defaults to " ".
            end (str, optional): String to write at end of print data. Defaults to "\\\\n".
            style (Union[str, Style], optional): A style to apply to output. Defaults to None.
            justify (str, optional): Justify method: "default", "left", "right", "center", or "full". Defaults to ``None``.
            overflow (str, optional): Overflow method: "ignore", "crop", "fold", or "ellipsis". Defaults to None.
            no_wrap (Optional[bool], optional): Disable word wrapping. Defaults to None.
            emoji (Optional[bool], optional): Enable emoji code, or ``None`` to use console default. Defaults to ``None``.
            markup (Optional[bool], optional): Enable markup, or ``None`` to use console default. Defaults to ``None``.
            highlight (Optional[bool], optional): Enable automatic highlighting, or ``None`` to use console default. Defaults to ``None``.
            width (Optional[int], optional): Width of output, or ``None`` to auto-detect. Defaults to ``None``.
            crop (Optional[bool], optional): Crop output to width of terminal. Defaults to True.
            soft_wrap (bool, optional): Enable soft wrap mode which disables word wrapping and cropping of text or ``None`` for
                Console default. Defaults to ``None``.
            new_line_start (bool, False): Insert a new line at the start if the output contains more than one line. Defaults to ``False``.
        '''
    def print_json(self, json: str | None = None, *, data: Any = None, indent: None | int | str = 2, highlight: bool = True, skip_keys: bool = False, ensure_ascii: bool = False, check_circular: bool = True, allow_nan: bool = True, default: Callable[[Any], Any] | None = None, sort_keys: bool = False) -> None:
        """Pretty prints JSON. Output will be valid JSON.

        Args:
            json (Optional[str]): A string containing JSON.
            data (Any): If json is not supplied, then encode this data.
            indent (Union[None, int, str], optional): Number of spaces to indent. Defaults to 2.
            highlight (bool, optional): Enable highlighting of output: Defaults to True.
            skip_keys (bool, optional): Skip keys not of a basic type. Defaults to False.
            ensure_ascii (bool, optional): Escape all non-ascii characters. Defaults to False.
            check_circular (bool, optional): Check for circular references. Defaults to True.
            allow_nan (bool, optional): Allow NaN and Infinity values. Defaults to True.
            default (Callable, optional): A callable that converts values that can not be encoded
                in to something that can be JSON encoded. Defaults to None.
            sort_keys (bool, optional): Sort dictionary keys. Defaults to False.
        """
    def update_screen(self, renderable: RenderableType, *, region: Region | None = None, options: ConsoleOptions | None = None) -> None:
        """Update the screen at a given offset.

        Args:
            renderable (RenderableType): A Rich renderable.
            region (Region, optional): Region of screen to update, or None for entire screen. Defaults to None.
            x (int, optional): x offset. Defaults to 0.
            y (int, optional): y offset. Defaults to 0.

        Raises:
            errors.NoAltScreen: If the Console isn't in alt screen mode.

        """
    def update_screen_lines(self, lines: List[List[Segment]], x: int = 0, y: int = 0) -> None:
        """Update lines of the screen at a given offset.

        Args:
            lines (List[List[Segment]]): Rendered lines (as produced by :meth:`~rich.Console.render_lines`).
            x (int, optional): x offset (column no). Defaults to 0.
            y (int, optional): y offset (column no). Defaults to 0.

        Raises:
            errors.NoAltScreen: If the Console isn't in alt screen mode.
        """
    def print_exception(self, *, width: int | None = 100, extra_lines: int = 3, theme: str | None = None, word_wrap: bool = False, show_locals: bool = False, suppress: Iterable[str | ModuleType] = (), max_frames: int = 100) -> None:
        """Prints a rich render of the last exception and traceback.

        Args:
            width (Optional[int], optional): Number of characters used to render code. Defaults to 100.
            extra_lines (int, optional): Additional lines of code to render. Defaults to 3.
            theme (str, optional): Override pygments theme used in traceback
            word_wrap (bool, optional): Enable word wrapping of long lines. Defaults to False.
            show_locals (bool, optional): Enable display of local variables. Defaults to False.
            suppress (Iterable[Union[str, ModuleType]]): Optional sequence of modules or paths to exclude from traceback.
            max_frames (int): Maximum number of frames to show in a traceback, 0 for no maximum. Defaults to 100.
        """
    def log(self, *objects: Any, sep: str = ' ', end: str = '\n', style: str | Style | None = None, justify: JustifyMethod | None = None, emoji: bool | None = None, markup: bool | None = None, highlight: bool | None = None, log_locals: bool = False, _stack_offset: int = 1) -> None:
        '''Log rich content to the terminal.

        Args:
            objects (positional args): Objects to log to the terminal.
            sep (str, optional): String to write between print data. Defaults to " ".
            end (str, optional): String to write at end of print data. Defaults to "\\\\n".
            style (Union[str, Style], optional): A style to apply to output. Defaults to None.
            justify (str, optional): One of "left", "right", "center", or "full". Defaults to ``None``.
            emoji (Optional[bool], optional): Enable emoji code, or ``None`` to use console default. Defaults to None.
            markup (Optional[bool], optional): Enable markup, or ``None`` to use console default. Defaults to None.
            highlight (Optional[bool], optional): Enable automatic highlighting, or ``None`` to use console default. Defaults to None.
            log_locals (bool, optional): Boolean to enable logging of locals where ``log()``
                was called. Defaults to False.
            _stack_offset (int, optional): Offset of caller from end of call stack. Defaults to 1.
        '''
    def input(self, prompt: TextType = '', *, markup: bool = True, emoji: bool = True, password: bool = False, stream: TextIO | None = None) -> str:
        """Displays a prompt and waits for input from the user. The prompt may contain color / style.

        It works in the same way as Python's builtin :func:`input` function and provides elaborate line editing and history features if Python's builtin :mod:`readline` module is previously loaded.

        Args:
            prompt (Union[str, Text]): Text to render in the prompt.
            markup (bool, optional): Enable console markup (requires a str prompt). Defaults to True.
            emoji (bool, optional): Enable emoji (requires a str prompt). Defaults to True.
            password: (bool, optional): Hide typed text. Defaults to False.
            stream: (TextIO, optional): Optional file to read input from (rather than stdin). Defaults to None.

        Returns:
            str: Text read from stdin.
        """
    def export_text(self, *, clear: bool = True, styles: bool = False) -> str:
        """Generate text from console contents (requires record=True argument in constructor).

        Args:
            clear (bool, optional): Clear record buffer after exporting. Defaults to ``True``.
            styles (bool, optional): If ``True``, ansi escape codes will be included. ``False`` for plain text.
                Defaults to ``False``.

        Returns:
            str: String containing console contents.

        """
    def save_text(self, path: str, *, clear: bool = True, styles: bool = False) -> None:
        """Generate text from console and save to a given location (requires record=True argument in constructor).

        Args:
            path (str): Path to write text files.
            clear (bool, optional): Clear record buffer after exporting. Defaults to ``True``.
            styles (bool, optional): If ``True``, ansi style codes will be included. ``False`` for plain text.
                Defaults to ``False``.

        """
    def export_html(self, *, theme: TerminalTheme | None = None, clear: bool = True, code_format: str | None = None, inline_styles: bool = False) -> str:
        """Generate HTML from console contents (requires record=True argument in constructor).

        Args:
            theme (TerminalTheme, optional): TerminalTheme object containing console colors.
            clear (bool, optional): Clear record buffer after exporting. Defaults to ``True``.
            code_format (str, optional): Format string to render HTML. In addition to '{foreground}',
                '{background}', and '{code}', should contain '{stylesheet}' if inline_styles is ``False``.
            inline_styles (bool, optional): If ``True`` styles will be inlined in to spans, which makes files
                larger but easier to cut and paste markup. If ``False``, styles will be embedded in a style tag.
                Defaults to False.

        Returns:
            str: String containing console contents as HTML.
        """
    def save_html(self, path: str, *, theme: TerminalTheme | None = None, clear: bool = True, code_format: str = ..., inline_styles: bool = False) -> None:
        """Generate HTML from console contents and write to a file (requires record=True argument in constructor).

        Args:
            path (str): Path to write html file.
            theme (TerminalTheme, optional): TerminalTheme object containing console colors.
            clear (bool, optional): Clear record buffer after exporting. Defaults to ``True``.
            code_format (str, optional): Format string to render HTML. In addition to '{foreground}',
                '{background}', and '{code}', should contain '{stylesheet}' if inline_styles is ``False``.
            inline_styles (bool, optional): If ``True`` styles will be inlined in to spans, which makes files
                larger but easier to cut and paste markup. If ``False``, styles will be embedded in a style tag.
                Defaults to False.

        """
    def export_svg(self, *, title: str = 'Rich', theme: TerminalTheme | None = None, clear: bool = True, code_format: str = ..., font_aspect_ratio: float = 0.61, unique_id: str | None = None) -> str:
        """
        Generate an SVG from the console contents (requires record=True in Console constructor).

        Args:
            title (str, optional): The title of the tab in the output image
            theme (TerminalTheme, optional): The ``TerminalTheme`` object to use to style the terminal
            clear (bool, optional): Clear record buffer after exporting. Defaults to ``True``
            code_format (str, optional): Format string used to generate the SVG. Rich will inject a number of variables
                into the string in order to form the final SVG output. The default template used and the variables
                injected by Rich can be found by inspecting the ``console.CONSOLE_SVG_FORMAT`` variable.
            font_aspect_ratio (float, optional): The width to height ratio of the font used in the ``code_format``
                string. Defaults to 0.61, which is the width to height ratio of Fira Code (the default font).
                If you aren't specifying a different font inside ``code_format``, you probably don't need this.
            unique_id (str, optional): unique id that is used as the prefix for various elements (CSS styles, node
                ids). If not set, this defaults to a computed value based on the recorded content.
        """
    def save_svg(self, path: str, *, title: str = 'Rich', theme: TerminalTheme | None = None, clear: bool = True, code_format: str = ..., font_aspect_ratio: float = 0.61, unique_id: str | None = None) -> None:
        """Generate an SVG file from the console contents (requires record=True in Console constructor).

        Args:
            path (str): The path to write the SVG to.
            title (str, optional): The title of the tab in the output image
            theme (TerminalTheme, optional): The ``TerminalTheme`` object to use to style the terminal
            clear (bool, optional): Clear record buffer after exporting. Defaults to ``True``
            code_format (str, optional): Format string used to generate the SVG. Rich will inject a number of variables
                into the string in order to form the final SVG output. The default template used and the variables
                injected by Rich can be found by inspecting the ``console.CONSOLE_SVG_FORMAT`` variable.
            font_aspect_ratio (float, optional): The width to height ratio of the font used in the ``code_format``
                string. Defaults to 0.61, which is the width to height ratio of Fira Code (the default font).
                If you aren't specifying a different font inside ``code_format``, you probably don't need this.
            unique_id (str, optional): unique id that is used as the prefix for various elements (CSS styles, node
                ids). If not set, this defaults to a computed value based on the recorded content.
        """
