from _typeshed import Incomplete
from enum import Enum
from prompt_toolkit.auto_suggest import AutoSuggest
from prompt_toolkit.clipboard import Clipboard
from prompt_toolkit.completion import Completer
from prompt_toolkit.cursor_shapes import AnyCursorShapeConfig, CursorShapeConfig
from prompt_toolkit.document import Document
from prompt_toolkit.enums import EditingMode
from prompt_toolkit.filters import FilterOrBool
from prompt_toolkit.formatted_text import AnyFormattedText
from prompt_toolkit.history import History
from prompt_toolkit.input.base import Input
from prompt_toolkit.key_binding.key_bindings import KeyBindingsBase
from prompt_toolkit.key_binding.key_processor import KeyPressEvent
from prompt_toolkit.layout import Window
from prompt_toolkit.layout.processors import Processor
from prompt_toolkit.lexers import Lexer
from prompt_toolkit.output import ColorDepth, Output
from prompt_toolkit.styles import BaseStyle, StyleTransformation
from prompt_toolkit.validation import Validator
from typing import Callable, Generic

__all__ = ['PromptSession', 'prompt', 'confirm', 'create_confirm_session', 'CompleteStyle']

E = KeyPressEvent

class _RPrompt(Window):
    """
    The prompt that is displayed on the right side of the Window.
    """
    def __init__(self, text: AnyFormattedText) -> None: ...

class CompleteStyle(str, Enum):
    """
    How to display autocompletions for the prompt.
    """
    value: str
    COLUMN: str
    MULTI_COLUMN: str
    READLINE_LIKE: str

class PromptSession(Generic[_T]):
    '''
    PromptSession for a prompt application, which can be used as a GNU Readline
    replacement.

    This is a wrapper around a lot of ``prompt_toolkit`` functionality and can
    be a replacement for `raw_input`.

    All parameters that expect "formatted text" can take either just plain text
    (a unicode object), a list of ``(style_str, text)`` tuples or an HTML object.

    Example usage::

        s = PromptSession(message=\'>\')
        text = s.prompt()

    :param message: Plain text or formatted text to be shown before the prompt.
        This can also be a callable that returns formatted text.
    :param multiline: `bool` or :class:`~prompt_toolkit.filters.Filter`.
        When True, prefer a layout that is more adapted for multiline input.
        Text after newlines is automatically indented, and search/arg input is
        shown below the input, instead of replacing the prompt.
    :param wrap_lines: `bool` or :class:`~prompt_toolkit.filters.Filter`.
        When True (the default), automatically wrap long lines instead of
        scrolling horizontally.
    :param is_password: Show asterisks instead of the actual typed characters.
    :param editing_mode: ``EditingMode.VI`` or ``EditingMode.EMACS``.
    :param vi_mode: `bool`, if True, Identical to ``editing_mode=EditingMode.VI``.
    :param complete_while_typing: `bool` or
        :class:`~prompt_toolkit.filters.Filter`. Enable autocompletion while
        typing.
    :param validate_while_typing: `bool` or
        :class:`~prompt_toolkit.filters.Filter`. Enable input validation while
        typing.
    :param enable_history_search: `bool` or
        :class:`~prompt_toolkit.filters.Filter`. Enable up-arrow parting
        string matching.
    :param search_ignore_case:
        :class:`~prompt_toolkit.filters.Filter`. Search case insensitive.
    :param lexer: :class:`~prompt_toolkit.lexers.Lexer` to be used for the
        syntax highlighting.
    :param validator: :class:`~prompt_toolkit.validation.Validator` instance
        for input validation.
    :param completer: :class:`~prompt_toolkit.completion.Completer` instance
        for input completion.
    :param complete_in_thread: `bool` or
        :class:`~prompt_toolkit.filters.Filter`. Run the completer code in a
        background thread in order to avoid blocking the user interface.
        For ``CompleteStyle.READLINE_LIKE``, this setting has no effect. There
        we always run the completions in the main thread.
    :param reserve_space_for_menu: Space to be reserved for displaying the menu.
        (0 means that no space needs to be reserved.)
    :param auto_suggest: :class:`~prompt_toolkit.auto_suggest.AutoSuggest`
        instance for input suggestions.
    :param style: :class:`.Style` instance for the color scheme.
    :param include_default_pygments_style: `bool` or
        :class:`~prompt_toolkit.filters.Filter`. Tell whether the default
        styling for Pygments lexers has to be included. By default, this is
        true, but it is recommended to be disabled if another Pygments style is
        passed as the `style` argument, otherwise, two Pygments styles will be
        merged.
    :param style_transformation:
        :class:`~prompt_toolkit.style.StyleTransformation` instance.
    :param swap_light_and_dark_colors: `bool` or
        :class:`~prompt_toolkit.filters.Filter`. When enabled, apply
        :class:`~prompt_toolkit.style.SwapLightAndDarkStyleTransformation`.
        This is useful for switching between dark and light terminal
        backgrounds.
    :param enable_system_prompt: `bool` or
        :class:`~prompt_toolkit.filters.Filter`. Pressing Meta+\'!\' will show
        a system prompt.
    :param enable_suspend: `bool` or :class:`~prompt_toolkit.filters.Filter`.
        Enable Control-Z style suspension.
    :param enable_open_in_editor: `bool` or
        :class:`~prompt_toolkit.filters.Filter`. Pressing \'v\' in Vi mode or
        C-X C-E in emacs mode will open an external editor.
    :param history: :class:`~prompt_toolkit.history.History` instance.
    :param clipboard: :class:`~prompt_toolkit.clipboard.Clipboard` instance.
        (e.g. :class:`~prompt_toolkit.clipboard.InMemoryClipboard`)
    :param rprompt: Text or formatted text to be displayed on the right side.
        This can also be a callable that returns (formatted) text.
    :param bottom_toolbar: Formatted text or callable which is supposed to
        return formatted text.
    :param prompt_continuation: Text that needs to be displayed for a multiline
        prompt continuation. This can either be formatted text or a callable
        that takes a `prompt_width`, `line_number` and `wrap_count` as input
        and returns formatted text. When this is `None` (the default), then
        `prompt_width` spaces will be used.
    :param complete_style: ``CompleteStyle.COLUMN``,
        ``CompleteStyle.MULTI_COLUMN`` or ``CompleteStyle.READLINE_LIKE``.
    :param mouse_support: `bool` or :class:`~prompt_toolkit.filters.Filter`
        to enable mouse support.
    :param placeholder: Text to be displayed when no input has been given
        yet. Unlike the `default` parameter, this won\'t be returned as part of
        the output ever. This can be formatted text or a callable that returns
        formatted text.
    :param refresh_interval: (number; in seconds) When given, refresh the UI
        every so many seconds.
    :param input: `Input` object. (Note that the preferred way to change the
        input/output is by creating an `AppSession`.)
    :param output: `Output` object.
    '''
    message: Incomplete
    lexer: Incomplete
    completer: Incomplete
    complete_in_thread: Incomplete
    is_password: Incomplete
    key_bindings: Incomplete
    bottom_toolbar: Incomplete
    style: Incomplete
    style_transformation: Incomplete
    swap_light_and_dark_colors: Incomplete
    color_depth: Incomplete
    cursor: Incomplete
    include_default_pygments_style: Incomplete
    rprompt: Incomplete
    multiline: Incomplete
    prompt_continuation: Incomplete
    wrap_lines: Incomplete
    enable_history_search: Incomplete
    search_ignore_case: Incomplete
    complete_while_typing: Incomplete
    validate_while_typing: Incomplete
    complete_style: Incomplete
    mouse_support: Incomplete
    auto_suggest: Incomplete
    clipboard: Incomplete
    validator: Incomplete
    refresh_interval: Incomplete
    input_processors: Incomplete
    placeholder: Incomplete
    enable_system_prompt: Incomplete
    enable_suspend: Incomplete
    enable_open_in_editor: Incomplete
    reserve_space_for_menu: Incomplete
    tempfile_suffix: Incomplete
    tempfile: Incomplete
    history: Incomplete
    default_buffer: Incomplete
    search_buffer: Incomplete
    layout: Incomplete
    app: Incomplete
    def __init__(self, message: AnyFormattedText = '', *, multiline: FilterOrBool = False, wrap_lines: FilterOrBool = True, is_password: FilterOrBool = False, vi_mode: bool = False, editing_mode: EditingMode = ..., complete_while_typing: FilterOrBool = True, validate_while_typing: FilterOrBool = True, enable_history_search: FilterOrBool = False, search_ignore_case: FilterOrBool = False, lexer: Lexer | None = None, enable_system_prompt: FilterOrBool = False, enable_suspend: FilterOrBool = False, enable_open_in_editor: FilterOrBool = False, validator: Validator | None = None, completer: Completer | None = None, complete_in_thread: bool = False, reserve_space_for_menu: int = 8, complete_style: CompleteStyle = ..., auto_suggest: AutoSuggest | None = None, style: BaseStyle | None = None, style_transformation: StyleTransformation | None = None, swap_light_and_dark_colors: FilterOrBool = False, color_depth: ColorDepth | None = None, cursor: AnyCursorShapeConfig = None, include_default_pygments_style: FilterOrBool = True, history: History | None = None, clipboard: Clipboard | None = None, prompt_continuation: PromptContinuationText | None = None, rprompt: AnyFormattedText = None, bottom_toolbar: AnyFormattedText = None, mouse_support: FilterOrBool = False, input_processors: list[Processor] | None = None, placeholder: AnyFormattedText | None = None, key_bindings: KeyBindingsBase | None = None, erase_when_done: bool = False, tempfile_suffix: str | Callable[[], str] | None = '.txt', tempfile: str | Callable[[], str] | None = None, refresh_interval: float = 0, input: Input | None = None, output: Output | None = None) -> None: ...
    def prompt(self, message: AnyFormattedText | None = None, *, editing_mode: EditingMode | None = None, refresh_interval: float | None = None, vi_mode: bool | None = None, lexer: Lexer | None = None, completer: Completer | None = None, complete_in_thread: bool | None = None, is_password: bool | None = None, key_bindings: KeyBindingsBase | None = None, bottom_toolbar: AnyFormattedText | None = None, style: BaseStyle | None = None, color_depth: ColorDepth | None = None, cursor: AnyCursorShapeConfig | None = None, include_default_pygments_style: FilterOrBool | None = None, style_transformation: StyleTransformation | None = None, swap_light_and_dark_colors: FilterOrBool | None = None, rprompt: AnyFormattedText | None = None, multiline: FilterOrBool | None = None, prompt_continuation: PromptContinuationText | None = None, wrap_lines: FilterOrBool | None = None, enable_history_search: FilterOrBool | None = None, search_ignore_case: FilterOrBool | None = None, complete_while_typing: FilterOrBool | None = None, validate_while_typing: FilterOrBool | None = None, complete_style: CompleteStyle | None = None, auto_suggest: AutoSuggest | None = None, validator: Validator | None = None, clipboard: Clipboard | None = None, mouse_support: FilterOrBool | None = None, input_processors: list[Processor] | None = None, placeholder: AnyFormattedText | None = None, reserve_space_for_menu: int | None = None, enable_system_prompt: FilterOrBool | None = None, enable_suspend: FilterOrBool | None = None, enable_open_in_editor: FilterOrBool | None = None, tempfile_suffix: str | Callable[[], str] | None = None, tempfile: str | Callable[[], str] | None = None, default: str | Document = '', accept_default: bool = False, pre_run: Callable[[], None] | None = None, set_exception_handler: bool = True, handle_sigint: bool = True, in_thread: bool = False) -> _T:
        """
        Display the prompt.

        The first set of arguments is a subset of the :class:`~.PromptSession`
        class itself. For these, passing in ``None`` will keep the current
        values that are active in the session. Passing in a value will set the
        attribute for the session, which means that it applies to the current,
        but also to the next prompts.

        Note that in order to erase a ``Completer``, ``Validator`` or
        ``AutoSuggest``, you can't use ``None``. Instead pass in a
        ``DummyCompleter``, ``DummyValidator`` or ``DummyAutoSuggest`` instance
        respectively. For a ``Lexer`` you can pass in an empty ``SimpleLexer``.

        Additional arguments, specific for this prompt:

        :param default: The default input text to be shown. (This can be edited
            by the user).
        :param accept_default: When `True`, automatically accept the default
            value without allowing the user to edit the input.
        :param pre_run: Callable, called at the start of `Application.run`.
        :param in_thread: Run the prompt in a background thread; block the
            current thread. This avoids interference with an event loop in the
            current thread. Like `Application.run(in_thread=True)`.

        This method will raise ``KeyboardInterrupt`` when control-c has been
        pressed (for abort) and ``EOFError`` when control-d has been pressed
        (for exit).
        """
    async def prompt_async(self, message: AnyFormattedText | None = None, *, editing_mode: EditingMode | None = None, refresh_interval: float | None = None, vi_mode: bool | None = None, lexer: Lexer | None = None, completer: Completer | None = None, complete_in_thread: bool | None = None, is_password: bool | None = None, key_bindings: KeyBindingsBase | None = None, bottom_toolbar: AnyFormattedText | None = None, style: BaseStyle | None = None, color_depth: ColorDepth | None = None, cursor: CursorShapeConfig | None = None, include_default_pygments_style: FilterOrBool | None = None, style_transformation: StyleTransformation | None = None, swap_light_and_dark_colors: FilterOrBool | None = None, rprompt: AnyFormattedText | None = None, multiline: FilterOrBool | None = None, prompt_continuation: PromptContinuationText | None = None, wrap_lines: FilterOrBool | None = None, enable_history_search: FilterOrBool | None = None, search_ignore_case: FilterOrBool | None = None, complete_while_typing: FilterOrBool | None = None, validate_while_typing: FilterOrBool | None = None, complete_style: CompleteStyle | None = None, auto_suggest: AutoSuggest | None = None, validator: Validator | None = None, clipboard: Clipboard | None = None, mouse_support: FilterOrBool | None = None, input_processors: list[Processor] | None = None, placeholder: AnyFormattedText | None = None, reserve_space_for_menu: int | None = None, enable_system_prompt: FilterOrBool | None = None, enable_suspend: FilterOrBool | None = None, enable_open_in_editor: FilterOrBool | None = None, tempfile_suffix: str | Callable[[], str] | None = None, tempfile: str | Callable[[], str] | None = None, default: str | Document = '', accept_default: bool = False, pre_run: Callable[[], None] | None = None, set_exception_handler: bool = True, handle_sigint: bool = True) -> _T: ...
    @property
    def editing_mode(self) -> EditingMode: ...
    @editing_mode.setter
    def editing_mode(self, value: EditingMode) -> None: ...
    @property
    def input(self) -> Input: ...
    @property
    def output(self) -> Output: ...

def prompt(message: AnyFormattedText | None = None, *, history: History | None = None, editing_mode: EditingMode | None = None, refresh_interval: float | None = None, vi_mode: bool | None = None, lexer: Lexer | None = None, completer: Completer | None = None, complete_in_thread: bool | None = None, is_password: bool | None = None, key_bindings: KeyBindingsBase | None = None, bottom_toolbar: AnyFormattedText | None = None, style: BaseStyle | None = None, color_depth: ColorDepth | None = None, cursor: AnyCursorShapeConfig = None, include_default_pygments_style: FilterOrBool | None = None, style_transformation: StyleTransformation | None = None, swap_light_and_dark_colors: FilterOrBool | None = None, rprompt: AnyFormattedText | None = None, multiline: FilterOrBool | None = None, prompt_continuation: PromptContinuationText | None = None, wrap_lines: FilterOrBool | None = None, enable_history_search: FilterOrBool | None = None, search_ignore_case: FilterOrBool | None = None, complete_while_typing: FilterOrBool | None = None, validate_while_typing: FilterOrBool | None = None, complete_style: CompleteStyle | None = None, auto_suggest: AutoSuggest | None = None, validator: Validator | None = None, clipboard: Clipboard | None = None, mouse_support: FilterOrBool | None = None, input_processors: list[Processor] | None = None, placeholder: AnyFormattedText | None = None, reserve_space_for_menu: int | None = None, enable_system_prompt: FilterOrBool | None = None, enable_suspend: FilterOrBool | None = None, enable_open_in_editor: FilterOrBool | None = None, tempfile_suffix: str | Callable[[], str] | None = None, tempfile: str | Callable[[], str] | None = None, in_thread: bool = False, default: str = '', accept_default: bool = False, pre_run: Callable[[], None] | None = None) -> str:
    """
    The global `prompt` function. This will create a new `PromptSession`
    instance for every call.
    """
def create_confirm_session(message: str, suffix: str = ' (y/n) ') -> PromptSession[bool]:
    """
    Create a `PromptSession` object for the 'confirm' function.
    """
def confirm(message: str = 'Confirm?', suffix: str = ' (y/n) ') -> bool:
    """
    Display a confirmation prompt that returns True/False.
    """
