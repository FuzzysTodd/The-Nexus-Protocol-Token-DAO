from . import errors as errors
from .color import Color as Color, ColorParseError as ColorParseError, ColorSystem as ColorSystem, blend_rgb as blend_rgb
from .repr import Result as Result, rich_repr as rich_repr
from .terminal_theme import DEFAULT_TERMINAL_THEME as DEFAULT_TERMINAL_THEME, TerminalTheme as TerminalTheme
from _typeshed import Incomplete
from typing import Any, Dict, Iterable, Type

StyleType: Incomplete

class _Bit:
    """A descriptor to get/set a style attribute bit."""
    bit: Incomplete
    def __init__(self, bit_no: int) -> None: ...
    def __get__(self, obj: Style, objtype: Type['Style']) -> bool | None: ...

class Style:
    """A terminal style.

    A terminal style consists of a color (`color`), a background color (`bgcolor`), and a number of attributes, such
    as bold, italic etc. The attributes have 3 states: they can either be on
    (``True``), off (``False``), or not set (``None``).

    Args:
        color (Union[Color, str], optional): Color of terminal text. Defaults to None.
        bgcolor (Union[Color, str], optional): Color of terminal background. Defaults to None.
        bold (bool, optional): Enable bold text. Defaults to None.
        dim (bool, optional): Enable dim text. Defaults to None.
        italic (bool, optional): Enable italic text. Defaults to None.
        underline (bool, optional): Enable underlined text. Defaults to None.
        blink (bool, optional): Enabled blinking text. Defaults to None.
        blink2 (bool, optional): Enable fast blinking text. Defaults to None.
        reverse (bool, optional): Enabled reverse text. Defaults to None.
        conceal (bool, optional): Enable concealed text. Defaults to None.
        strike (bool, optional): Enable strikethrough text. Defaults to None.
        underline2 (bool, optional): Enable doubly underlined text. Defaults to None.
        frame (bool, optional): Enable framed text. Defaults to None.
        encircle (bool, optional): Enable encircled text. Defaults to None.
        overline (bool, optional): Enable overlined text. Defaults to None.
        link (str, link): Link URL. Defaults to None.

    """
    STYLE_ATTRIBUTES: Incomplete
    def __init__(self, *, color: Color | str | None = None, bgcolor: Color | str | None = None, bold: bool | None = None, dim: bool | None = None, italic: bool | None = None, underline: bool | None = None, blink: bool | None = None, blink2: bool | None = None, reverse: bool | None = None, conceal: bool | None = None, strike: bool | None = None, underline2: bool | None = None, frame: bool | None = None, encircle: bool | None = None, overline: bool | None = None, link: str | None = None, meta: Dict[str, Any] | None = None) -> None: ...
    @classmethod
    def null(cls) -> Style:
        """Create an 'null' style, equivalent to Style(), but more performant."""
    @classmethod
    def from_color(cls, color: Color | None = None, bgcolor: Color | None = None) -> Style:
        """Create a new style with colors and no attributes.

        Returns:
            color (Optional[Color]): A (foreground) color, or None for no color. Defaults to None.
            bgcolor (Optional[Color]): A (background) color, or None for no color. Defaults to None.
        """
    @classmethod
    def from_meta(cls, meta: Dict[str, Any] | None) -> Style:
        """Create a new style with meta data.

        Returns:
            meta (Optional[Dict[str, Any]]): A dictionary of meta data. Defaults to None.
        """
    @classmethod
    def on(cls, meta: Dict[str, Any] | None = None, **handlers: Any) -> Style:
        """Create a blank style with meta information.

        Example:
            style = Style.on(click=self.on_click)

        Args:
            meta (Optional[Dict[str, Any]], optional): An optional dict of meta information.
            **handlers (Any): Keyword arguments are translated in to handlers.

        Returns:
            Style: A Style with meta information attached.
        """
    bold: Incomplete
    dim: Incomplete
    italic: Incomplete
    underline: Incomplete
    blink: Incomplete
    blink2: Incomplete
    reverse: Incomplete
    conceal: Incomplete
    strike: Incomplete
    underline2: Incomplete
    frame: Incomplete
    encircle: Incomplete
    overline: Incomplete
    @property
    def link_id(self) -> str:
        """Get a link id, used in ansi code for links."""
    def __bool__(self) -> bool:
        """A Style is false if it has no attributes, colors, or links."""
    @classmethod
    def normalize(cls, style: str) -> str:
        """Normalize a style definition so that styles with the same effect have the same string
        representation.

        Args:
            style (str): A style definition.

        Returns:
            str: Normal form of style definition.
        """
    @classmethod
    def pick_first(cls, *values: StyleType | None) -> StyleType:
        """Pick first non-None style."""
    def __rich_repr__(self) -> Result: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    @property
    def color(self) -> Color | None:
        """The foreground color or None if it is not set."""
    @property
    def bgcolor(self) -> Color | None:
        """The background color or None if it is not set."""
    @property
    def link(self) -> str | None:
        """Link text, if set."""
    @property
    def transparent_background(self) -> bool:
        """Check if the style specified a transparent background."""
    @property
    def background_style(self) -> Style:
        """A Style with background only."""
    @property
    def meta(self) -> Dict[str, Any]:
        """Get meta information (can not be changed after construction)."""
    @property
    def without_color(self) -> Style:
        """Get a copy of the style with color removed."""
    @classmethod
    def parse(cls, style_definition: str) -> Style:
        """Parse a style definition.

        Args:
            style_definition (str): A string containing a style.

        Raises:
            errors.StyleSyntaxError: If the style definition syntax is invalid.

        Returns:
            `Style`: A Style instance.
        """
    def get_html_style(self, theme: TerminalTheme | None = None) -> str:
        """Get a CSS style rule."""
    @classmethod
    def combine(cls, styles: Iterable['Style']) -> Style:
        """Combine styles and get result.

        Args:
            styles (Iterable[Style]): Styles to combine.

        Returns:
            Style: A new style instance.
        """
    @classmethod
    def chain(cls, *styles: Style) -> Style:
        """Combine styles from positional argument in to a single style.

        Args:
            *styles (Iterable[Style]): Styles to combine.

        Returns:
            Style: A new style instance.
        """
    def copy(self) -> Style:
        """Get a copy of this style.

        Returns:
            Style: A new Style instance with identical attributes.
        """
    def clear_meta_and_links(self) -> Style:
        """Get a copy of this style with link and meta information removed.

        Returns:
            Style: New style object.
        """
    def update_link(self, link: str | None = None) -> Style:
        """Get a copy with a different value for link.

        Args:
            link (str, optional): New value for link. Defaults to None.

        Returns:
            Style: A new Style instance.
        """
    def render(self, text: str = '', *, color_system: ColorSystem | None = ..., legacy_windows: bool = False) -> str:
        '''Render the ANSI codes for the style.

        Args:
            text (str, optional): A string to style. Defaults to "".
            color_system (Optional[ColorSystem], optional): Color system to render to. Defaults to ColorSystem.TRUECOLOR.

        Returns:
            str: A string containing ANSI style codes.
        '''
    def test(self, text: str | None = None) -> None:
        """Write text with style directly to terminal.

        This method is for testing purposes only.

        Args:
            text (Optional[str], optional): Text to style or None for style name.

        """
    def __add__(self, style: Style | None) -> Style: ...

NULL_STYLE: Incomplete

class StyleStack:
    """A stack of styles."""
    def __init__(self, default_style: Style) -> None: ...
    @property
    def current(self) -> Style:
        """Get the Style at the top of the stack."""
    def push(self, style: Style) -> None:
        """Push a new style on to the stack.

        Args:
            style (Style): New style to combine with current style.
        """
    def pop(self) -> Style:
        """Pop last style and discard.

        Returns:
            Style: New current style (also available as stack.current)
        """
