from .controls import BufferControl
from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod
from prompt_toolkit.document import Document
from prompt_toolkit.filters import FilterOrBool
from prompt_toolkit.formatted_text import AnyFormattedText, StyleAndTextTuples
from typing import Callable

__all__ = ['Processor', 'TransformationInput', 'Transformation', 'DummyProcessor', 'HighlightSearchProcessor', 'HighlightIncrementalSearchProcessor', 'HighlightSelectionProcessor', 'PasswordProcessor', 'HighlightMatchingBracketProcessor', 'DisplayMultipleCursors', 'BeforeInput', 'ShowArg', 'AfterInput', 'AppendAutoSuggestion', 'ConditionalProcessor', 'ShowLeadingWhiteSpaceProcessor', 'ShowTrailingWhiteSpaceProcessor', 'TabsProcessor', 'ReverseSearchProcessor', 'DynamicProcessor', 'merge_processors']

class Processor(metaclass=ABCMeta):
    """
    Manipulate the fragments for a given line in a
    :class:`~prompt_toolkit.layout.controls.BufferControl`.
    """
    @abstractmethod
    def apply_transformation(self, transformation_input: TransformationInput) -> Transformation:
        """
        Apply transformation. Returns a :class:`.Transformation` instance.

        :param transformation_input: :class:`.TransformationInput` object.
        """
SourceToDisplay = Callable[[int], int]
DisplayToSource = Callable[[int], int]

class TransformationInput:
    """
    :param buffer_control: :class:`.BufferControl` instance.
    :param lineno: The number of the line to which we apply the processor.
    :param source_to_display: A function that returns the position in the
        `fragments` for any position in the source string. (This takes
        previous processors into account.)
    :param fragments: List of fragments that we can transform. (Received from the
        previous processor.)
    """
    buffer_control: Incomplete
    document: Incomplete
    lineno: Incomplete
    source_to_display: Incomplete
    fragments: Incomplete
    width: Incomplete
    height: Incomplete
    def __init__(self, buffer_control: BufferControl, document: Document, lineno: int, source_to_display: SourceToDisplay, fragments: StyleAndTextTuples, width: int, height: int) -> None: ...
    def unpack(self) -> tuple[BufferControl, Document, int, SourceToDisplay, StyleAndTextTuples, int, int]: ...

class Transformation:
    """
    Transformation result, as returned by :meth:`.Processor.apply_transformation`.

    Important: Always make sure that the length of `document.text` is equal to
               the length of all the text in `fragments`!

    :param fragments: The transformed fragments. To be displayed, or to pass to
        the next processor.
    :param source_to_display: Cursor position transformation from original
        string to transformed string.
    :param display_to_source: Cursor position transformed from source string to
        original string.
    """
    fragments: Incomplete
    source_to_display: Incomplete
    display_to_source: Incomplete
    def __init__(self, fragments: StyleAndTextTuples, source_to_display: SourceToDisplay | None = None, display_to_source: DisplayToSource | None = None) -> None: ...

class DummyProcessor(Processor):
    """
    A `Processor` that doesn't do anything.
    """
    def apply_transformation(self, transformation_input: TransformationInput) -> Transformation: ...

class HighlightSearchProcessor(Processor):
    """
    Processor that highlights search matches in the document.
    Note that this doesn't support multiline search matches yet.

    The style classes 'search' and 'search.current' will be applied to the
    content.
    """
    def apply_transformation(self, transformation_input: TransformationInput) -> Transformation: ...

class HighlightIncrementalSearchProcessor(HighlightSearchProcessor):
    """
    Highlight the search terms that are used for highlighting the incremental
    search. The style class 'incsearch' will be applied to the content.

    Important: this requires the `preview_search=True` flag to be set for the
    `BufferControl`. Otherwise, the cursor position won't be set to the search
    match while searching, and nothing happens.
    """

class HighlightSelectionProcessor(Processor):
    """
    Processor that highlights the selection in the document.
    """
    def apply_transformation(self, transformation_input: TransformationInput) -> Transformation: ...

class PasswordProcessor(Processor):
    '''
    Processor that masks the input. (For passwords.)

    :param char: (string) Character to be used. "*" by default.
    '''
    char: Incomplete
    def __init__(self, char: str = '*') -> None: ...
    def apply_transformation(self, ti: TransformationInput) -> Transformation: ...

class HighlightMatchingBracketProcessor(Processor):
    """
    When the cursor is on or right after a bracket, it highlights the matching
    bracket.

    :param max_cursor_distance: Only highlight matching brackets when the
        cursor is within this distance. (From inside a `Processor`, we can't
        know which lines will be visible on the screen. But we also don't want
        to scan the whole document for matching brackets on each key press, so
        we limit to this value.)
    """
    chars: Incomplete
    max_cursor_distance: Incomplete
    def __init__(self, chars: str = '[](){}<>', max_cursor_distance: int = 1000) -> None: ...
    def apply_transformation(self, transformation_input: TransformationInput) -> Transformation: ...

class DisplayMultipleCursors(Processor):
    """
    When we're in Vi block insert mode, display all the cursors.
    """
    def apply_transformation(self, transformation_input: TransformationInput) -> Transformation: ...

class BeforeInput(Processor):
    """
    Insert text before the input.

    :param text: This can be either plain text or formatted text
        (or a callable that returns any of those).
    :param style: style to be applied to this prompt/prefix.
    """
    text: Incomplete
    style: Incomplete
    def __init__(self, text: AnyFormattedText, style: str = '') -> None: ...
    def apply_transformation(self, ti: TransformationInput) -> Transformation: ...

class ShowArg(BeforeInput):
    """
    Display the 'arg' in front of the input.

    This was used by the `PromptSession`, but now it uses the
    `Window.get_line_prefix` function instead.
    """
    def __init__(self) -> None: ...

class AfterInput(Processor):
    """
    Insert text after the input.

    :param text: This can be either plain text or formatted text
        (or a callable that returns any of those).
    :param style: style to be applied to this prompt/prefix.
    """
    text: Incomplete
    style: Incomplete
    def __init__(self, text: AnyFormattedText, style: str = '') -> None: ...
    def apply_transformation(self, ti: TransformationInput) -> Transformation: ...

class AppendAutoSuggestion(Processor):
    """
    Append the auto suggestion to the input.
    (The user can then press the right arrow the insert the suggestion.)
    """
    style: Incomplete
    def __init__(self, style: str = 'class:auto-suggestion') -> None: ...
    def apply_transformation(self, ti: TransformationInput) -> Transformation: ...

class ShowLeadingWhiteSpaceProcessor(Processor):
    """
    Make leading whitespace visible.

    :param get_char: Callable that returns one character.
    """
    style: Incomplete
    get_char: Incomplete
    def __init__(self, get_char: Callable[[], str] | None = None, style: str = 'class:leading-whitespace') -> None: ...
    def apply_transformation(self, ti: TransformationInput) -> Transformation: ...

class ShowTrailingWhiteSpaceProcessor(Processor):
    """
    Make trailing whitespace visible.

    :param get_char: Callable that returns one character.
    """
    style: Incomplete
    get_char: Incomplete
    def __init__(self, get_char: Callable[[], str] | None = None, style: str = 'class:training-whitespace') -> None: ...
    def apply_transformation(self, ti: TransformationInput) -> Transformation: ...

class TabsProcessor(Processor):
    """
    Render tabs as spaces (instead of ^I) or make them visible (for instance,
    by replacing them with dots.)

    :param tabstop: Horizontal space taken by a tab. (`int` or callable that
        returns an `int`).
    :param char1: Character or callable that returns a character (text of
        length one). This one is used for the first space taken by the tab.
    :param char2: Like `char1`, but for the rest of the space.
    """
    char1: Incomplete
    char2: Incomplete
    tabstop: Incomplete
    style: Incomplete
    def __init__(self, tabstop: int | Callable[[], int] = 4, char1: str | Callable[[], str] = '|', char2: str | Callable[[], str] = '┈', style: str = 'class:tab') -> None: ...
    def apply_transformation(self, ti: TransformationInput) -> Transformation: ...

class ReverseSearchProcessor(Processor):
    '''
    Process to display the "(reverse-i-search)`...`:..." stuff around
    the search buffer.

    Note: This processor is meant to be applied to the BufferControl that
    contains the search buffer, it\'s not meant for the original input.
    '''
    def apply_transformation(self, ti: TransformationInput) -> Transformation: ...

class ConditionalProcessor(Processor):
    """
    Processor that applies another processor, according to a certain condition.
    Example::

        # Create a function that returns whether or not the processor should
        # currently be applied.
        def highlight_enabled():
            return true_or_false

        # Wrapped it in a `ConditionalProcessor` for usage in a `BufferControl`.
        BufferControl(input_processors=[
            ConditionalProcessor(HighlightSearchProcessor(),
                                 Condition(highlight_enabled))])

    :param processor: :class:`.Processor` instance.
    :param filter: :class:`~prompt_toolkit.filters.Filter` instance.
    """
    processor: Incomplete
    filter: Incomplete
    def __init__(self, processor: Processor, filter: FilterOrBool) -> None: ...
    def apply_transformation(self, transformation_input: TransformationInput) -> Transformation: ...

class DynamicProcessor(Processor):
    """
    Processor class that dynamically returns any Processor.

    :param get_processor: Callable that returns a :class:`.Processor` instance.
    """
    get_processor: Incomplete
    def __init__(self, get_processor: Callable[[], Processor | None]) -> None: ...
    def apply_transformation(self, ti: TransformationInput) -> Transformation: ...

def merge_processors(processors: list[Processor]) -> Processor:
    """
    Merge multiple `Processor` objects into one.
    """

class _MergedProcessor(Processor):
    """
    Processor that groups multiple other `Processor` objects, but exposes an
    API as if it is one `Processor`.
    """
    processors: Incomplete
    def __init__(self, processors: list[Processor]) -> None: ...
    def apply_transformation(self, ti: TransformationInput) -> Transformation: ...
