from .toolbars import SearchToolbar
from _typeshed import Incomplete
from prompt_toolkit.auto_suggest import AutoSuggest
from prompt_toolkit.buffer import BufferAcceptHandler
from prompt_toolkit.completion import Completer
from prompt_toolkit.document import Document
from prompt_toolkit.filters import FilterOrBool
from prompt_toolkit.formatted_text import AnyFormattedText
from prompt_toolkit.history import History
from prompt_toolkit.key_binding.key_bindings import KeyBindings
from prompt_toolkit.key_binding.key_processor import KeyPressEvent
from prompt_toolkit.layout.containers import AnyContainer, Container, WindowAlign
from prompt_toolkit.layout.controls import GetLinePrefixCallable
from prompt_toolkit.layout.dimension import AnyDimension
from prompt_toolkit.layout.processors import Processor
from prompt_toolkit.lexers import Lexer
from prompt_toolkit.validation import Validator
from typing import Callable, Generic, Sequence

__all__ = ['TextArea', 'Label', 'Button', 'Frame', 'Shadow', 'Box', 'VerticalLine', 'HorizontalLine', 'RadioList', 'CheckboxList', 'Checkbox', 'ProgressBar']

E = KeyPressEvent

class Border:
    """Box drawing characters. (Thin)"""
    HORIZONTAL: str
    VERTICAL: str
    TOP_LEFT: str
    TOP_RIGHT: str
    BOTTOM_LEFT: str
    BOTTOM_RIGHT: str

class TextArea:
    '''
    A simple input field.

    This is a higher level abstraction on top of several other classes with
    sane defaults.

    This widget does have the most common options, but it does not intend to
    cover every single use case. For more configurations options, you can
    always build a text area manually, using a
    :class:`~prompt_toolkit.buffer.Buffer`,
    :class:`~prompt_toolkit.layout.BufferControl` and
    :class:`~prompt_toolkit.layout.Window`.

    Buffer attributes:

    :param text: The initial text.
    :param multiline: If True, allow multiline input.
    :param completer: :class:`~prompt_toolkit.completion.Completer` instance
        for auto completion.
    :param complete_while_typing: Boolean.
    :param accept_handler: Called when `Enter` is pressed (This should be a
        callable that takes a buffer as input).
    :param history: :class:`~prompt_toolkit.history.History` instance.
    :param auto_suggest: :class:`~prompt_toolkit.auto_suggest.AutoSuggest`
        instance for input suggestions.

    BufferControl attributes:

    :param password: When `True`, display using asterisks.
    :param focusable: When `True`, allow this widget to receive the focus.
    :param focus_on_click: When `True`, focus after mouse click.
    :param input_processors: `None` or a list of
        :class:`~prompt_toolkit.layout.Processor` objects.
    :param validator: `None` or a :class:`~prompt_toolkit.validation.Validator`
        object.

    Window attributes:

    :param lexer: :class:`~prompt_toolkit.lexers.Lexer` instance for syntax
        highlighting.
    :param wrap_lines: When `True`, don\'t scroll horizontally, but wrap lines.
    :param width: Window width. (:class:`~prompt_toolkit.layout.Dimension` object.)
    :param height: Window height. (:class:`~prompt_toolkit.layout.Dimension` object.)
    :param scrollbar: When `True`, display a scroll bar.
    :param style: A style string.
    :param dont_extend_width: When `True`, don\'t take up more width then the
                              preferred width reported by the control.
    :param dont_extend_height: When `True`, don\'t take up more width then the
                               preferred height reported by the control.
    :param get_line_prefix: None or a callable that returns formatted text to
        be inserted before a line. It takes a line number (int) and a
        wrap_count and returns formatted text. This can be used for
        implementation of line continuations, things like Vim "breakindent" and
        so on.

    Other attributes:

    :param search_field: An optional `SearchToolbar` object.
    '''
    completer: Incomplete
    complete_while_typing: Incomplete
    lexer: Incomplete
    auto_suggest: Incomplete
    read_only: Incomplete
    wrap_lines: Incomplete
    validator: Incomplete
    buffer: Incomplete
    control: Incomplete
    window: Incomplete
    def __init__(self, text: str = '', multiline: FilterOrBool = True, password: FilterOrBool = False, lexer: Lexer | None = None, auto_suggest: AutoSuggest | None = None, completer: Completer | None = None, complete_while_typing: FilterOrBool = True, validator: Validator | None = None, accept_handler: BufferAcceptHandler | None = None, history: History | None = None, focusable: FilterOrBool = True, focus_on_click: FilterOrBool = False, wrap_lines: FilterOrBool = True, read_only: FilterOrBool = False, width: AnyDimension = None, height: AnyDimension = None, dont_extend_height: FilterOrBool = False, dont_extend_width: FilterOrBool = False, line_numbers: bool = False, get_line_prefix: GetLinePrefixCallable | None = None, scrollbar: bool = False, style: str = '', search_field: SearchToolbar | None = None, preview_search: FilterOrBool = True, prompt: AnyFormattedText = '', input_processors: list[Processor] | None = None, name: str = '') -> None: ...
    @property
    def text(self) -> str:
        """
        The `Buffer` text.
        """
    @text.setter
    def text(self, value: str) -> None: ...
    @property
    def document(self) -> Document:
        """
        The `Buffer` document (text + cursor position).
        """
    @document.setter
    def document(self, value: Document) -> None: ...
    @property
    def accept_handler(self) -> BufferAcceptHandler | None:
        """
        The accept handler. Called when the user accepts the input.
        """
    @accept_handler.setter
    def accept_handler(self, value: BufferAcceptHandler) -> None: ...
    def __pt_container__(self) -> Container: ...

class Label:
    """
    Widget that displays the given text. It is not editable or focusable.

    :param text: Text to display. Can be multiline. All value types accepted by
        :class:`prompt_toolkit.layout.FormattedTextControl` are allowed,
        including a callable.
    :param style: A style string.
    :param width: When given, use this width, rather than calculating it from
        the text size.
    :param dont_extend_width: When `True`, don't take up more width than
                              preferred, i.e. the length of the longest line of
                              the text, or value of `width` parameter, if
                              given. `True` by default
    :param dont_extend_height: When `True`, don't take up more width than the
                               preferred height, i.e. the number of lines of
                               the text. `False` by default.
    """
    text: Incomplete
    formatted_text_control: Incomplete
    window: Incomplete
    def __init__(self, text: AnyFormattedText, style: str = '', width: AnyDimension = None, dont_extend_height: bool = True, dont_extend_width: bool = False, align: WindowAlign | Callable[[], WindowAlign] = ..., wrap_lines: FilterOrBool = True) -> None: ...
    def __pt_container__(self) -> Container: ...

class Button:
    """
    Clickable button.

    :param text: The caption for the button.
    :param handler: `None` or callable. Called when the button is clicked. No
        parameters are passed to this callable. Use for instance Python's
        `functools.partial` to pass parameters to this callable if needed.
    :param width: Width of the button.
    """
    text: Incomplete
    left_symbol: Incomplete
    right_symbol: Incomplete
    handler: Incomplete
    width: Incomplete
    control: Incomplete
    window: Incomplete
    def __init__(self, text: str, handler: Callable[[], None] | None = None, width: int = 12, left_symbol: str = '<', right_symbol: str = '>') -> None: ...
    def __pt_container__(self) -> Container: ...

class Frame:
    """
    Draw a border around any container, optionally with a title text.

    Changing the title and body of the frame is possible at runtime by
    assigning to the `body` and `title` attributes of this class.

    :param body: Another container object.
    :param title: Text to be displayed in the top of the frame (can be formatted text).
    :param style: Style string to be applied to this widget.
    """
    title: Incomplete
    body: Incomplete
    container: Incomplete
    def __init__(self, body: AnyContainer, title: AnyFormattedText = '', style: str = '', width: AnyDimension = None, height: AnyDimension = None, key_bindings: KeyBindings | None = None, modal: bool = False) -> None: ...
    def __pt_container__(self) -> Container: ...

class Shadow:
    """
    Draw a shadow underneath/behind this container.
    (This applies `class:shadow` the the cells under the shadow. The Style
    should define the colors for the shadow.)

    :param body: Another container object.
    """
    container: Incomplete
    def __init__(self, body: AnyContainer) -> None: ...
    def __pt_container__(self) -> Container: ...

class Box:
    """
    Add padding around a container.

    This also makes sure that the parent can provide more space than required by
    the child. This is very useful when wrapping a small element with a fixed
    size into a ``VSplit`` or ``HSplit`` object. The ``HSplit`` and ``VSplit``
    try to make sure to adapt respectively the width and height, possibly
    shrinking other elements. Wrapping something in a ``Box`` makes it flexible.

    :param body: Another container object.
    :param padding: The margin to be used around the body. This can be
        overridden by `padding_left`, padding_right`, `padding_top` and
        `padding_bottom`.
    :param style: A style string.
    :param char: Character to be used for filling the space around the body.
        (This is supposed to be a character with a terminal width of 1.)
    """
    padding_left: Incomplete
    padding_right: Incomplete
    padding_top: Incomplete
    padding_bottom: Incomplete
    body: Incomplete
    container: Incomplete
    def __init__(self, body: AnyContainer, padding: AnyDimension = None, padding_left: AnyDimension = None, padding_right: AnyDimension = None, padding_top: AnyDimension = None, padding_bottom: AnyDimension = None, width: AnyDimension = None, height: AnyDimension = None, style: str = '', char: None | str | Callable[[], str] = None, modal: bool = False, key_bindings: KeyBindings | None = None) -> None: ...
    def __pt_container__(self) -> Container: ...

class _DialogList(Generic[_T]):
    """
    Common code for `RadioList` and `CheckboxList`.
    """
    open_character: str
    close_character: str
    container_style: str
    default_style: str
    selected_style: str
    checked_style: str
    multiple_selection: bool
    show_scrollbar: bool
    values: Incomplete
    current_values: Incomplete
    current_value: Incomplete
    control: Incomplete
    window: Incomplete
    def __init__(self, values: Sequence[tuple[_T, AnyFormattedText]], default_values: Sequence[_T] | None = None) -> None: ...
    def __pt_container__(self) -> Container: ...

class RadioList(_DialogList[_T]):
    """
    List of radio buttons. Only one can be checked at the same time.

    :param values: List of (value, label) tuples.
    """
    open_character: str
    close_character: str
    container_style: str
    default_style: str
    selected_style: str
    checked_style: str
    multiple_selection: bool
    def __init__(self, values: Sequence[tuple[_T, AnyFormattedText]], default: _T | None = None) -> None: ...

class CheckboxList(_DialogList[_T]):
    """
    List of checkbox buttons. Several can be checked at the same time.

    :param values: List of (value, label) tuples.
    """
    open_character: str
    close_character: str
    container_style: str
    default_style: str
    selected_style: str
    checked_style: str
    multiple_selection: bool

class Checkbox(CheckboxList[str]):
    """Backward compatibility util: creates a 1-sized CheckboxList

    :param text: the text
    """
    show_scrollbar: bool
    def __init__(self, text: AnyFormattedText = '', checked: bool = False) -> None: ...
    @property
    def checked(self) -> bool: ...
    current_values: Incomplete
    @checked.setter
    def checked(self, value: bool) -> None: ...

class VerticalLine:
    """
    A simple vertical line with a width of 1.
    """
    window: Incomplete
    def __init__(self) -> None: ...
    def __pt_container__(self) -> Container: ...

class HorizontalLine:
    """
    A simple horizontal line with a height of 1.
    """
    window: Incomplete
    def __init__(self) -> None: ...
    def __pt_container__(self) -> Container: ...

class ProgressBar:
    label: Incomplete
    container: Incomplete
    def __init__(self) -> None: ...
    @property
    def percentage(self) -> int: ...
    @percentage.setter
    def percentage(self, value: int) -> None: ...
    def __pt_container__(self) -> Container: ...
