from ._loop import loop_last as loop_last
from ._pick import pick_bool as pick_bool
from ._wrap import divide_line as divide_line
from .align import AlignMethod as AlignMethod
from .cells import cell_len as cell_len, set_cell_size as set_cell_size
from .console import Console as Console, ConsoleOptions as ConsoleOptions, JustifyMethod as JustifyMethod, OverflowMethod as OverflowMethod
from .containers import Lines as Lines
from .control import strip_control_codes as strip_control_codes
from .emoji import EmojiVariant as EmojiVariant
from .jupyter import JupyterMixin as JupyterMixin
from .measure import Measurement as Measurement
from .segment import Segment as Segment
from .style import Style as Style, StyleType as StyleType
from _typeshed import Incomplete
from typing import Any, Callable, Dict, Iterable, List, NamedTuple, Tuple

DEFAULT_JUSTIFY: JustifyMethod
DEFAULT_OVERFLOW: OverflowMethod
TextType: Incomplete
GetStyleCallable = Callable[[str], StyleType | None]

class Span(NamedTuple):
    """A marked up region in some text."""
    start: int
    end: int
    style: str | Style
    def __bool__(self) -> bool: ...
    def split(self, offset: int) -> Tuple['Span', Span | None]:
        """Split a span in to 2 from a given offset."""
    def move(self, offset: int) -> Span:
        """Move start and end by a given offset.

        Args:
            offset (int): Number of characters to add to start and end.

        Returns:
            TextSpan: A new TextSpan with adjusted position.
        """
    def right_crop(self, offset: int) -> Span:
        """Crop the span at the given offset.

        Args:
            offset (int): A value between start and end.

        Returns:
            Span: A new (possibly smaller) span.
        """
    def extend(self, cells: int) -> Span:
        """Extend the span by the given number of cells.

        Args:
            cells (int): Additional space to add to end of span.

        Returns:
            Span: A span.
        """

class Text(JupyterMixin):
    '''Text with color / style.

    Args:
        text (str, optional): Default unstyled text. Defaults to "".
        style (Union[str, Style], optional): Base style for text. Defaults to "".
        justify (str, optional): Justify method: "left", "center", "full", "right". Defaults to None.
        overflow (str, optional): Overflow method: "crop", "fold", "ellipsis". Defaults to None.
        no_wrap (bool, optional): Disable text wrapping, or None for default. Defaults to None.
        end (str, optional): Character to end text with. Defaults to "\\\\n".
        tab_size (int): Number of spaces per tab, or ``None`` to use ``console.tab_size``. Defaults to None.
        spans (List[Span], optional). A list of predefined style spans. Defaults to None.
    '''
    style: Incomplete
    justify: Incomplete
    overflow: Incomplete
    no_wrap: Incomplete
    end: Incomplete
    tab_size: Incomplete
    def __init__(self, text: str = '', style: str | Style = '', *, justify: JustifyMethod | None = None, overflow: OverflowMethod | None = None, no_wrap: bool | None = None, end: str = '\n', tab_size: int | None = None, spans: List[Span] | None = None) -> None: ...
    def __len__(self) -> int: ...
    def __bool__(self) -> bool: ...
    def __add__(self, other: Any) -> Text: ...
    def __eq__(self, other: object) -> bool: ...
    def __contains__(self, other: object) -> bool: ...
    def __getitem__(self, slice: int | slice) -> Text: ...
    @property
    def cell_len(self) -> int:
        """Get the number of cells required to render this text."""
    @property
    def markup(self) -> str:
        """Get console markup to render this Text.

        Returns:
            str: A string potentially creating markup tags.
        """
    @classmethod
    def from_markup(cls, text: str, *, style: str | Style = '', emoji: bool = True, emoji_variant: EmojiVariant | None = None, justify: JustifyMethod | None = None, overflow: OverflowMethod | None = None, end: str = '\n') -> Text:
        '''Create Text instance from markup.

        Args:
            text (str): A string containing console markup.
            emoji (bool, optional): Also render emoji code. Defaults to True.
            justify (str, optional): Justify method: "left", "center", "full", "right". Defaults to None.
            overflow (str, optional): Overflow method: "crop", "fold", "ellipsis". Defaults to None.
            end (str, optional): Character to end text with. Defaults to "\\\\n".

        Returns:
            Text: A Text instance with markup rendered.
        '''
    @classmethod
    def from_ansi(cls, text: str, *, style: str | Style = '', justify: JustifyMethod | None = None, overflow: OverflowMethod | None = None, no_wrap: bool | None = None, end: str = '\n', tab_size: int | None = 8) -> Text:
        '''Create a Text object from a string containing ANSI escape codes.

        Args:
            text (str): A string containing escape codes.
            style (Union[str, Style], optional): Base style for text. Defaults to "".
            justify (str, optional): Justify method: "left", "center", "full", "right". Defaults to None.
            overflow (str, optional): Overflow method: "crop", "fold", "ellipsis". Defaults to None.
            no_wrap (bool, optional): Disable text wrapping, or None for default. Defaults to None.
            end (str, optional): Character to end text with. Defaults to "\\\\n".
            tab_size (int): Number of spaces per tab, or ``None`` to use ``console.tab_size``. Defaults to None.
        '''
    @classmethod
    def styled(cls, text: str, style: StyleType = '', *, justify: JustifyMethod | None = None, overflow: OverflowMethod | None = None) -> Text:
        '''Construct a Text instance with a pre-applied styled. A style applied in this way won\'t be used
        to pad the text when it is justified.

        Args:
            text (str): A string containing console markup.
            style (Union[str, Style]): Style to apply to the text. Defaults to "".
            justify (str, optional): Justify method: "left", "center", "full", "right". Defaults to None.
            overflow (str, optional): Overflow method: "crop", "fold", "ellipsis". Defaults to None.

        Returns:
            Text: A text instance with a style applied to the entire string.
        '''
    @classmethod
    def assemble(cls, *parts: str | Text | Tuple[str, StyleType], style: str | Style = '', justify: JustifyMethod | None = None, overflow: OverflowMethod | None = None, no_wrap: bool | None = None, end: str = '\n', tab_size: int = 8, meta: Dict[str, Any] | None = None) -> Text:
        '''Construct a text instance by combining a sequence of strings with optional styles.
        The positional arguments should be either strings, or a tuple of string + style.

        Args:
            style (Union[str, Style], optional): Base style for text. Defaults to "".
            justify (str, optional): Justify method: "left", "center", "full", "right". Defaults to None.
            overflow (str, optional): Overflow method: "crop", "fold", "ellipsis". Defaults to None.
            end (str, optional): Character to end text with. Defaults to "\\\\n".
            tab_size (int): Number of spaces per tab, or ``None`` to use ``console.tab_size``. Defaults to None.
            meta (Dict[str, Any], optional). Meta data to apply to text, or None for no meta data. Default to None

        Returns:
            Text: A new text instance.
        '''
    @property
    def plain(self) -> str:
        """Get the text as a single string."""
    @plain.setter
    def plain(self, new_text: str) -> None:
        """Set the text to a new value."""
    @property
    def spans(self) -> List[Span]:
        """Get a reference to the internal list of spans."""
    @spans.setter
    def spans(self, spans: List[Span]) -> None:
        """Set spans."""
    def blank_copy(self, plain: str = '') -> Text:
        """Return a new Text instance with copied meta data (but not the string or spans)."""
    def copy(self) -> Text:
        """Return a copy of this instance."""
    def stylize(self, style: str | Style, start: int = 0, end: int | None = None) -> None:
        """Apply a style to the text, or a portion of the text.

        Args:
            style (Union[str, Style]): Style instance or style definition to apply.
            start (int): Start offset (negative indexing is supported). Defaults to 0.
            end (Optional[int], optional): End offset (negative indexing is supported), or None for end of text. Defaults to None.
        """
    def stylize_before(self, style: str | Style, start: int = 0, end: int | None = None) -> None:
        """Apply a style to the text, or a portion of the text. Styles will be applied before other styles already present.

        Args:
            style (Union[str, Style]): Style instance or style definition to apply.
            start (int): Start offset (negative indexing is supported). Defaults to 0.
            end (Optional[int], optional): End offset (negative indexing is supported), or None for end of text. Defaults to None.
        """
    def apply_meta(self, meta: Dict[str, Any], start: int = 0, end: int | None = None) -> None:
        """Apply meta data to the text, or a portion of the text.

        Args:
            meta (Dict[str, Any]): A dict of meta information.
            start (int): Start offset (negative indexing is supported). Defaults to 0.
            end (Optional[int], optional): End offset (negative indexing is supported), or None for end of text. Defaults to None.

        """
    def on(self, meta: Dict[str, Any] | None = None, **handlers: Any) -> Text:
        '''Apply event handlers (used by Textual project).

        Example:
            >>> from rich.text import Text
            >>> text = Text("hello world")
            >>> text.on(click="view.toggle(\'world\')")

        Args:
            meta (Dict[str, Any]): Mapping of meta information.
            **handlers: Keyword args are prefixed with "@" to defined handlers.

        Returns:
            Text: Self is returned to method may be chained.
        '''
    def remove_suffix(self, suffix: str) -> None:
        """Remove a suffix if it exists.

        Args:
            suffix (str): Suffix to remove.
        """
    def get_style_at_offset(self, console: Console, offset: int) -> Style:
        """Get the style of a character at give offset.

        Args:
            console (~Console): Console where text will be rendered.
            offset (int): Offset in to text (negative indexing supported)

        Returns:
            Style: A Style instance.
        """
    def extend_style(self, spaces: int) -> None:
        """Extend the Text given number of spaces where the spaces have the same style as the last character.

        Args:
            spaces (int): Number of spaces to add to the Text.
        """
    def highlight_regex(self, re_highlight: str, style: GetStyleCallable | StyleType | None = None, *, style_prefix: str = '') -> int:
        """Highlight text with a regular expression, where group names are
        translated to styles.

        Args:
            re_highlight (str): A regular expression.
            style (Union[GetStyleCallable, StyleType]): Optional style to apply to whole match, or a callable
                which accepts the matched text and returns a style. Defaults to None.
            style_prefix (str, optional): Optional prefix to add to style group names.

        Returns:
            int: Number of regex matches
        """
    def highlight_words(self, words: Iterable[str], style: str | Style, *, case_sensitive: bool = True) -> int:
        """Highlight words with a style.

        Args:
            words (Iterable[str]): Worlds to highlight.
            style (Union[str, Style]): Style to apply.
            case_sensitive (bool, optional): Enable case sensitive matchings. Defaults to True.

        Returns:
            int: Number of words highlighted.
        """
    def rstrip(self) -> None:
        """Strip whitespace from end of text."""
    def rstrip_end(self, size: int) -> None:
        """Remove whitespace beyond a certain width at the end of the text.

        Args:
            size (int): The desired size of the text.
        """
    def set_length(self, new_length: int) -> None:
        """Set new length of the text, clipping or padding is required."""
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> Iterable[Segment]: ...
    def __rich_measure__(self, console: Console, options: ConsoleOptions) -> Measurement: ...
    def render(self, console: Console, end: str = '') -> Iterable['Segment']:
        """Render the text as Segments.

        Args:
            console (Console): Console instance.
            end (Optional[str], optional): Optional end character.

        Returns:
            Iterable[Segment]: Result of render that may be written to the console.
        """
    def join(self, lines: Iterable['Text']) -> Text:
        """Join text together with this instance as the separator.

        Args:
            lines (Iterable[Text]): An iterable of Text instances to join.

        Returns:
            Text: A new text instance containing join text.
        """
    def expand_tabs(self, tab_size: int | None = None) -> None:
        """Converts tabs to spaces.

        Args:
            tab_size (int, optional): Size of tabs. Defaults to 8.

        """
    def truncate(self, max_width: int, *, overflow: OverflowMethod | None = None, pad: bool = False) -> None:
        '''Truncate text if it is longer that a given width.

        Args:
            max_width (int): Maximum number of characters in text.
            overflow (str, optional): Overflow method: "crop", "fold", or "ellipsis". Defaults to None, to use self.overflow.
            pad (bool, optional): Pad with spaces if the length is less than max_width. Defaults to False.
        '''
    def pad(self, count: int, character: str = ' ') -> None:
        """Pad left and right with a given number of characters.

        Args:
            count (int): Width of padding.
        """
    def pad_left(self, count: int, character: str = ' ') -> None:
        '''Pad the left with a given character.

        Args:
            count (int): Number of characters to pad.
            character (str, optional): Character to pad with. Defaults to " ".
        '''
    def pad_right(self, count: int, character: str = ' ') -> None:
        '''Pad the right with a given character.

        Args:
            count (int): Number of characters to pad.
            character (str, optional): Character to pad with. Defaults to " ".
        '''
    def align(self, align: AlignMethod, width: int, character: str = ' ') -> None:
        '''Align text to a given width.

        Args:
            align (AlignMethod): One of "left", "center", or "right".
            width (int): Desired width.
            character (str, optional): Character to pad with. Defaults to " ".
        '''
    def append(self, text: Text | str, style: str | Style | None = None) -> Text:
        """Add text with an optional style.

        Args:
            text (Union[Text, str]): A str or Text to append.
            style (str, optional): A style name. Defaults to None.

        Returns:
            Text: Returns self for chaining.
        """
    def append_text(self, text: Text) -> Text:
        """Append another Text instance. This method is more performant that Text.append, but
        only works for Text.

        Returns:
            Text: Returns self for chaining.
        """
    def append_tokens(self, tokens: Iterable[Tuple[str, StyleType | None]]) -> Text:
        """Append iterable of str and style. Style may be a Style instance or a str style definition.

        Args:
            pairs (Iterable[Tuple[str, Optional[StyleType]]]): An iterable of tuples containing str content and style.

        Returns:
            Text: Returns self for chaining.
        """
    def copy_styles(self, text: Text) -> None:
        """Copy styles from another Text instance.

        Args:
            text (Text): A Text instance to copy styles from, must be the same length.
        """
    def split(self, separator: str = '\n', *, include_separator: bool = False, allow_blank: bool = False) -> Lines:
        '''Split rich text in to lines, preserving styles.

        Args:
            separator (str, optional): String to split on. Defaults to "\\\\n".
            include_separator (bool, optional): Include the separator in the lines. Defaults to False.
            allow_blank (bool, optional): Return a blank line if the text ends with a separator. Defaults to False.

        Returns:
            List[RichText]: A list of rich text, one per line of the original.
        '''
    def divide(self, offsets: Iterable[int]) -> Lines:
        """Divide text in to a number of lines at given offsets.

        Args:
            offsets (Iterable[int]): Offsets used to divide text.

        Returns:
            Lines: New RichText instances between offsets.
        """
    def right_crop(self, amount: int = 1) -> None:
        """Remove a number of characters from the end of the text."""
    def wrap(self, console: Console, width: int, *, justify: JustifyMethod | None = None, overflow: OverflowMethod | None = None, tab_size: int = 8, no_wrap: bool | None = None) -> Lines:
        '''Word wrap the text.

        Args:
            console (Console): Console instance.
            width (int): Number of characters per line.
            emoji (bool, optional): Also render emoji code. Defaults to True.
            justify (str, optional): Justify method: "default", "left", "center", "full", "right". Defaults to "default".
            overflow (str, optional): Overflow method: "crop", "fold", or "ellipsis". Defaults to None.
            tab_size (int, optional): Default tab size. Defaults to 8.
            no_wrap (bool, optional): Disable wrapping, Defaults to False.

        Returns:
            Lines: Number of lines.
        '''
    def fit(self, width: int) -> Lines:
        """Fit the text in to given width by chopping in to lines.

        Args:
            width (int): Maximum characters in a line.

        Returns:
            Lines: Lines container.
        """
    def detect_indentation(self) -> int:
        """Auto-detect indentation of code.

        Returns:
            int: Number of spaces used to indent code.
        """
    def with_indent_guides(self, indent_size: int | None = None, *, character: str = '│', style: StyleType = 'dim green') -> Text:
        '''Adds indent guide lines to text.

        Args:
            indent_size (Optional[int]): Size of indentation, or None to auto detect. Defaults to None.
            character (str, optional): Character to use for indentation. Defaults to "│".
            style (Union[Style, str], optional): Style of indent guides.

        Returns:
            Text: New text with indentation guides.
        '''
