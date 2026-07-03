from .clipboard import ClipboardData
from .selection import PasteMode, SelectionState
from _typeshed import Incomplete
from typing import Callable, Iterable, List, Pattern

__all__ = ['Document']

class _ImmutableLineList(List[str]):
    """
    Some protection for our 'lines' list, which is assumed to be immutable in the cache.
    (Useful for detecting obvious bugs.)
    """
    __setitem__: Incomplete
    append: Incomplete
    clear: Incomplete
    extend: Incomplete
    insert: Incomplete
    pop: Incomplete
    remove: Incomplete
    reverse: Incomplete
    sort: Incomplete

class _DocumentCache:
    lines: Incomplete
    line_indexes: Incomplete
    def __init__(self) -> None: ...

class Document:
    """
    This is a immutable class around the text and cursor position, and contains
    methods for querying this data, e.g. to give the text before the cursor.

    This class is usually instantiated by a :class:`~prompt_toolkit.buffer.Buffer`
    object, and accessed as the `document` property of that class.

    :param text: string
    :param cursor_position: int
    :param selection: :class:`.SelectionState`
    """
    def __init__(self, text: str = '', cursor_position: int | None = None, selection: SelectionState | None = None) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    @property
    def text(self) -> str:
        """The document text."""
    @property
    def cursor_position(self) -> int:
        """The document cursor position."""
    @property
    def selection(self) -> SelectionState | None:
        """:class:`.SelectionState` object."""
    @property
    def current_char(self) -> str:
        """Return character under cursor or an empty string."""
    @property
    def char_before_cursor(self) -> str:
        """Return character before the cursor or an empty string."""
    @property
    def text_before_cursor(self) -> str: ...
    @property
    def text_after_cursor(self) -> str: ...
    @property
    def current_line_before_cursor(self) -> str:
        """Text from the start of the line until the cursor."""
    @property
    def current_line_after_cursor(self) -> str:
        """Text from the cursor until the end of the line."""
    @property
    def lines(self) -> list[str]:
        """
        Array of all the lines.
        """
    @property
    def lines_from_current(self) -> list[str]:
        """
        Array of the lines starting from the current line, until the last line.
        """
    @property
    def line_count(self) -> int:
        """Return the number of lines in this document. If the document ends
        with a trailing \\n, that counts as the beginning of a new line."""
    @property
    def current_line(self) -> str:
        """Return the text on the line where the cursor is. (when the input
        consists of just one line, it equals `text`."""
    @property
    def leading_whitespace_in_current_line(self) -> str:
        """The leading whitespace in the left margin of the current line."""
    @property
    def on_first_line(self) -> bool:
        """
        True when we are at the first line.
        """
    @property
    def on_last_line(self) -> bool:
        """
        True when we are at the last line.
        """
    @property
    def cursor_position_row(self) -> int:
        """
        Current row. (0-based.)
        """
    @property
    def cursor_position_col(self) -> int:
        """
        Current column. (0-based.)
        """
    def translate_index_to_position(self, index: int) -> tuple[int, int]:
        """
        Given an index for the text, return the corresponding (row, col) tuple.
        (0-based. Returns (0, 0) for index=0.)
        """
    def translate_row_col_to_index(self, row: int, col: int) -> int:
        """
        Given a (row, col) tuple, return the corresponding index.
        (Row and col params are 0-based.)

        Negative row/col values are turned into zero.
        """
    @property
    def is_cursor_at_the_end(self) -> bool:
        """True when the cursor is at the end of the text."""
    @property
    def is_cursor_at_the_end_of_line(self) -> bool:
        """True when the cursor is at the end of this line."""
    def has_match_at_current_position(self, sub: str) -> bool:
        """
        `True` when this substring is found at the cursor position.
        """
    def find(self, sub: str, in_current_line: bool = False, include_current_position: bool = False, ignore_case: bool = False, count: int = 1) -> int | None:
        """
        Find `text` after the cursor, return position relative to the cursor
        position. Return `None` if nothing was found.

        :param count: Find the n-th occurrence.
        """
    def find_all(self, sub: str, ignore_case: bool = False) -> list[int]:
        """
        Find all occurrences of the substring. Return a list of absolute
        positions in the document.
        """
    def find_backwards(self, sub: str, in_current_line: bool = False, ignore_case: bool = False, count: int = 1) -> int | None:
        """
        Find `text` before the cursor, return position relative to the cursor
        position. Return `None` if nothing was found.

        :param count: Find the n-th occurrence.
        """
    def get_word_before_cursor(self, WORD: bool = False, pattern: Pattern[str] | None = None) -> str:
        """
        Give the word before the cursor.
        If we have whitespace before the cursor this returns an empty string.

        :param pattern: (None or compiled regex). When given, use this regex
            pattern.
        """
    def find_start_of_previous_word(self, count: int = 1, WORD: bool = False, pattern: Pattern[str] | None = None) -> int | None:
        """
        Return an index relative to the cursor position pointing to the start
        of the previous word. Return `None` if nothing was found.

        :param pattern: (None or compiled regex). When given, use this regex
            pattern.
        """
    def find_boundaries_of_current_word(self, WORD: bool = False, include_leading_whitespace: bool = False, include_trailing_whitespace: bool = False) -> tuple[int, int]:
        """
        Return the relative boundaries (startpos, endpos) of the current word under the
        cursor. (This is at the current line, because line boundaries obviously
        don't belong to any word.)
        If not on a word, this returns (0,0)
        """
    def get_word_under_cursor(self, WORD: bool = False) -> str:
        """
        Return the word, currently below the cursor.
        This returns an empty string when the cursor is on a whitespace region.
        """
    def find_next_word_beginning(self, count: int = 1, WORD: bool = False) -> int | None:
        """
        Return an index relative to the cursor position pointing to the start
        of the next word. Return `None` if nothing was found.
        """
    def find_next_word_ending(self, include_current_position: bool = False, count: int = 1, WORD: bool = False) -> int | None:
        """
        Return an index relative to the cursor position pointing to the end
        of the next word. Return `None` if nothing was found.
        """
    def find_previous_word_beginning(self, count: int = 1, WORD: bool = False) -> int | None:
        """
        Return an index relative to the cursor position pointing to the start
        of the previous word. Return `None` if nothing was found.
        """
    def find_previous_word_ending(self, count: int = 1, WORD: bool = False) -> int | None:
        """
        Return an index relative to the cursor position pointing to the end
        of the previous word. Return `None` if nothing was found.
        """
    def find_next_matching_line(self, match_func: Callable[[str], bool], count: int = 1) -> int | None:
        """
        Look downwards for empty lines.
        Return the line index, relative to the current line.
        """
    def find_previous_matching_line(self, match_func: Callable[[str], bool], count: int = 1) -> int | None:
        """
        Look upwards for empty lines.
        Return the line index, relative to the current line.
        """
    def get_cursor_left_position(self, count: int = 1) -> int:
        """
        Relative position for cursor left.
        """
    def get_cursor_right_position(self, count: int = 1) -> int:
        """
        Relative position for cursor_right.
        """
    def get_cursor_up_position(self, count: int = 1, preferred_column: int | None = None) -> int:
        """
        Return the relative cursor position (character index) where we would be if the
        user pressed the arrow-up button.

        :param preferred_column: When given, go to this column instead of
                                 staying at the current column.
        """
    def get_cursor_down_position(self, count: int = 1, preferred_column: int | None = None) -> int:
        """
        Return the relative cursor position (character index) where we would be if the
        user pressed the arrow-down button.

        :param preferred_column: When given, go to this column instead of
                                 staying at the current column.
        """
    def find_enclosing_bracket_right(self, left_ch: str, right_ch: str, end_pos: int | None = None) -> int | None:
        """
        Find the right bracket enclosing current position. Return the relative
        position to the cursor position.

        When `end_pos` is given, don't look past the position.
        """
    def find_enclosing_bracket_left(self, left_ch: str, right_ch: str, start_pos: int | None = None) -> int | None:
        """
        Find the left bracket enclosing current position. Return the relative
        position to the cursor position.

        When `start_pos` is given, don't look past the position.
        """
    def find_matching_bracket_position(self, start_pos: int | None = None, end_pos: int | None = None) -> int:
        """
        Return relative cursor position of matching [, (, { or < bracket.

        When `start_pos` or `end_pos` are given. Don't look past the positions.
        """
    def get_start_of_document_position(self) -> int:
        """Relative position for the start of the document."""
    def get_end_of_document_position(self) -> int:
        """Relative position for the end of the document."""
    def get_start_of_line_position(self, after_whitespace: bool = False) -> int:
        """Relative position for the start of this line."""
    def get_end_of_line_position(self) -> int:
        """Relative position for the end of this line."""
    def last_non_blank_of_current_line_position(self) -> int:
        """
        Relative position for the last non blank character of this line.
        """
    def get_column_cursor_position(self, column: int) -> int:
        """
        Return the relative cursor position for this column at the current
        line. (It will stay between the boundaries of the line in case of a
        larger number.)
        """
    def selection_range(self) -> tuple[int, int]:
        """
        Return (from, to) tuple of the selection.
        start and end position are included.

        This doesn't take the selection type into account. Use
        `selection_ranges` instead.
        """
    def selection_ranges(self) -> Iterable[tuple[int, int]]:
        """
        Return a list of `(from, to)` tuples for the selection or none if
        nothing was selected. The upper boundary is not included.

        This will yield several (from, to) tuples in case of a BLOCK selection.
        This will return zero ranges, like (8,8) for empty lines in a block
        selection.
        """
    def selection_range_at_line(self, row: int) -> tuple[int, int] | None:
        """
        If the selection spans a portion of the given line, return a (from, to) tuple.

        The returned upper boundary is not included in the selection, so
        `(0, 0)` is an empty selection.  `(0, 1)`, is a one character selection.

        Returns None if the selection doesn't cover this line at all.
        """
    def cut_selection(self) -> tuple[Document, ClipboardData]:
        """
        Return a (:class:`.Document`, :class:`.ClipboardData`) tuple, where the
        document represents the new document when the selection is cut, and the
        clipboard data, represents whatever has to be put on the clipboard.
        """
    def paste_clipboard_data(self, data: ClipboardData, paste_mode: PasteMode = ..., count: int = 1) -> Document:
        """
        Return a new :class:`.Document` instance which contains the result if
        we would paste this data at the current cursor position.

        :param paste_mode: Where to paste. (Before/after/emacs.)
        :param count: When >1, Paste multiple times.
        """
    def empty_line_count_at_the_end(self) -> int:
        """
        Return number of empty lines at the end of the document.
        """
    def start_of_paragraph(self, count: int = 1, before: bool = False) -> int:
        """
        Return the start of the current paragraph. (Relative cursor position.)
        """
    def end_of_paragraph(self, count: int = 1, after: bool = False) -> int:
        """
        Return the end of the current paragraph. (Relative cursor position.)
        """
    def insert_after(self, text: str) -> Document:
        """
        Create a new document, with this text inserted after the buffer.
        It keeps selection ranges and cursor position in sync.
        """
    def insert_before(self, text: str) -> Document:
        """
        Create a new document, with this text inserted before the buffer.
        It keeps selection ranges and cursor position in sync.
        """
