import asyncio
from _typeshed import Incomplete
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.clipboard import Clipboard
from prompt_toolkit.cursor_shapes import AnyCursorShapeConfig
from prompt_toolkit.enums import EditingMode
from prompt_toolkit.filters import FilterOrBool
from prompt_toolkit.formatted_text import AnyFormattedText
from prompt_toolkit.input.base import Input
from prompt_toolkit.key_binding.key_bindings import Binding, KeyBindingsBase, KeysTuple
from prompt_toolkit.key_binding.key_processor import KeyPressEvent
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.output import ColorDepth, Output
from prompt_toolkit.search import SearchState
from prompt_toolkit.styles import BaseStyle, StyleTransformation
from typing import Any, Callable, Coroutine, Generic, overload

__all__ = ['Application']

E = KeyPressEvent

class Application(Generic[_AppResult]):
    """
    The main Application class!
    This glues everything together.

    :param layout: A :class:`~prompt_toolkit.layout.Layout` instance.
    :param key_bindings:
        :class:`~prompt_toolkit.key_binding.KeyBindingsBase` instance for
        the key bindings.
    :param clipboard: :class:`~prompt_toolkit.clipboard.Clipboard` to use.
    :param full_screen: When True, run the application on the alternate screen buffer.
    :param color_depth: Any :class:`~.ColorDepth` value, a callable that
        returns a :class:`~.ColorDepth` or `None` for default.
    :param erase_when_done: (bool) Clear the application output when it finishes.
    :param reverse_vi_search_direction: Normally, in Vi mode, a '/' searches
        forward and a '?' searches backward. In Readline mode, this is usually
        reversed.
    :param min_redraw_interval: Number of seconds to wait between redraws. Use
        this for applications where `invalidate` is called a lot. This could cause
        a lot of terminal output, which some terminals are not able to process.

        `None` means that every `invalidate` will be scheduled right away
        (which is usually fine).

        When one `invalidate` is called, but a scheduled redraw of a previous
        `invalidate` call has not been executed yet, nothing will happen in any
        case.

    :param max_render_postpone_time: When there is high CPU (a lot of other
        scheduled calls), postpone the rendering max x seconds.  '0' means:
        don't postpone. '.5' means: try to draw at least twice a second.

    :param refresh_interval: Automatically invalidate the UI every so many
        seconds. When `None` (the default), only invalidate when `invalidate`
        has been called.

    :param terminal_size_polling_interval: Poll the terminal size every so many
        seconds. Useful if the applications runs in a thread other then then
        main thread where SIGWINCH can't be handled, or on Windows.

    Filters:

    :param mouse_support: (:class:`~prompt_toolkit.filters.Filter` or
        boolean). When True, enable mouse support.
    :param paste_mode: :class:`~prompt_toolkit.filters.Filter` or boolean.
    :param editing_mode: :class:`~prompt_toolkit.enums.EditingMode`.

    :param enable_page_navigation_bindings: When `True`, enable the page
        navigation key bindings. These include both Emacs and Vi bindings like
        page-up, page-down and so on to scroll through pages. Mostly useful for
        creating an editor or other full screen applications. Probably, you
        don't want this for the implementation of a REPL. By default, this is
        enabled if `full_screen` is set.

    Callbacks (all of these should accept an
    :class:`~prompt_toolkit.application.Application` object as input.)

    :param on_reset: Called during reset.
    :param on_invalidate: Called when the UI has been invalidated.
    :param before_render: Called right before rendering.
    :param after_render: Called right after rendering.

    I/O:
    (Note that the preferred way to change the input/output is by creating an
    `AppSession` with the required input/output objects. If you need multiple
    applications running at the same time, you have to create a separate
    `AppSession` using a `with create_app_session():` block.

    :param input: :class:`~prompt_toolkit.input.Input` instance.
    :param output: :class:`~prompt_toolkit.output.Output` instance. (Probably
                   Vt100_Output or Win32Output.)

    Usage:

        app = Application(...)
        app.run()

        # Or
        await app.run_async()
    """
    style: Incomplete
    style_transformation: Incomplete
    key_bindings: Incomplete
    layout: Incomplete
    clipboard: Incomplete
    full_screen: Incomplete
    mouse_support: Incomplete
    paste_mode: Incomplete
    editing_mode: Incomplete
    erase_when_done: Incomplete
    reverse_vi_search_direction: Incomplete
    enable_page_navigation_bindings: Incomplete
    min_redraw_interval: Incomplete
    max_render_postpone_time: Incomplete
    refresh_interval: Incomplete
    terminal_size_polling_interval: Incomplete
    cursor: Incomplete
    on_invalidate: Incomplete
    on_reset: Incomplete
    before_render: Incomplete
    after_render: Incomplete
    output: Incomplete
    input: Incomplete
    pre_run_callables: Incomplete
    future: Incomplete
    loop: Incomplete
    context: Incomplete
    quoted_insert: bool
    vi_state: Incomplete
    emacs_state: Incomplete
    ttimeoutlen: float
    timeoutlen: float
    renderer: Incomplete
    render_counter: int
    key_processor: Incomplete
    def __init__(self, layout: Layout | None = None, style: BaseStyle | None = None, include_default_pygments_style: FilterOrBool = True, style_transformation: StyleTransformation | None = None, key_bindings: KeyBindingsBase | None = None, clipboard: Clipboard | None = None, full_screen: bool = False, color_depth: ColorDepth | Callable[[], ColorDepth | None] | None = None, mouse_support: FilterOrBool = False, enable_page_navigation_bindings: None | FilterOrBool = None, paste_mode: FilterOrBool = False, editing_mode: EditingMode = ..., erase_when_done: bool = False, reverse_vi_search_direction: FilterOrBool = False, min_redraw_interval: float | int | None = None, max_render_postpone_time: float | int | None = 0.01, refresh_interval: float | None = None, terminal_size_polling_interval: float | None = 0.5, cursor: AnyCursorShapeConfig = None, on_reset: ApplicationEventHandler[_AppResult] | None = None, on_invalidate: ApplicationEventHandler[_AppResult] | None = None, before_render: ApplicationEventHandler[_AppResult] | None = None, after_render: ApplicationEventHandler[_AppResult] | None = None, input: Input | None = None, output: Output | None = None) -> None: ...
    @property
    def color_depth(self) -> ColorDepth:
        """
        The active :class:`.ColorDepth`.

        The current value is determined as follows:

        - If a color depth was given explicitly to this application, use that
          value.
        - Otherwise, fall back to the color depth that is reported by the
          :class:`.Output` implementation. If the :class:`.Output` class was
          created using `output.defaults.create_output`, then this value is
          coming from the $PROMPT_TOOLKIT_COLOR_DEPTH environment variable.
        """
    @property
    def current_buffer(self) -> Buffer:
        """
        The currently focused :class:`~.Buffer`.

        (This returns a dummy :class:`.Buffer` when none of the actual buffers
        has the focus. In this case, it's really not practical to check for
        `None` values or catch exceptions every time.)
        """
    @property
    def current_search_state(self) -> SearchState:
        """
        Return the current :class:`.SearchState`. (The one for the focused
        :class:`.BufferControl`.)
        """
    exit_style: str
    def reset(self) -> None:
        """
        Reset everything, for reading the next input.
        """
    def invalidate(self) -> None:
        """
        Thread safe way of sending a repaint trigger to the input event loop.
        """
    @property
    def invalidated(self) -> bool:
        """True when a redraw operation has been scheduled."""
    async def run_async(self, pre_run: Callable[[], None] | None = None, set_exception_handler: bool = True, handle_sigint: bool = True, slow_callback_duration: float = 0.5) -> _AppResult:
        '''
        Run the prompt_toolkit :class:`~prompt_toolkit.application.Application`
        until :meth:`~prompt_toolkit.application.Application.exit` has been
        called. Return the value that was passed to
        :meth:`~prompt_toolkit.application.Application.exit`.

        This is the main entry point for a prompt_toolkit
        :class:`~prompt_toolkit.application.Application` and usually the only
        place where the event loop is actually running.

        :param pre_run: Optional callable, which is called right after the
            "reset" of the application.
        :param set_exception_handler: When set, in case of an exception, go out
            of the alternate screen and hide the application, display the
            exception, and wait for the user to press ENTER.
        :param handle_sigint: Handle SIGINT signal if possible. This will call
            the `<sigint>` key binding when a SIGINT is received. (This only
            works in the main thread.)
        :param slow_callback_duration: Display warnings if code scheduled in
            the asyncio event loop takes more time than this. The asyncio
            default of `0.1` is sometimes not sufficient on a slow system,
            because exceptionally, the drawing of the app, which happens in the
            event loop, can take a bit longer from time to time.
        '''
    def run(self, pre_run: Callable[[], None] | None = None, set_exception_handler: bool = True, handle_sigint: bool = True, in_thread: bool = False) -> _AppResult:
        '''
        A blocking \'run\' call that waits until the UI is finished.

        This will start the current asyncio event loop. If no loop is set for
        the current thread, then it will create a new loop. If a new loop was
        created, this won\'t close the new loop (if `in_thread=False`).

        :param pre_run: Optional callable, which is called right after the
            "reset" of the application.
        :param set_exception_handler: When set, in case of an exception, go out
            of the alternate screen and hide the application, display the
            exception, and wait for the user to press ENTER.
        :param in_thread: When true, run the application in a background
            thread, and block the current thread until the application
            terminates. This is useful if we need to be sure the application
            won\'t use the current event loop (asyncio does not support nested
            event loops). A new event loop will be created in this background
            thread, and that loop will also be closed when the background
            thread terminates. When this is used, it\'s especially important to
            make sure that all asyncio background tasks are managed through
            `get_appp().create_background_task()`, so that unfinished tasks are
            properly cancelled before the event loop is closed. This is used
            for instance in ptpython.
        :param handle_sigint: Handle SIGINT signal. Call the key binding for
            `Keys.SIGINT`. (This only works in the main thread.)
        '''
    def create_background_task(self, coroutine: Coroutine[Any, Any, None]) -> asyncio.Task[None]:
        """
        Start a background task (coroutine) for the running application. When
        the `Application` terminates, unfinished background tasks will be
        cancelled.

        Given that we still support Python versions before 3.11, we can't use
        task groups (and exception groups), because of that, these background
        tasks are not allowed to raise exceptions. If they do, we'll call the
        default exception handler from the event loop.

        If at some point, we have Python 3.11 as the minimum supported Python
        version, then we can use a `TaskGroup` (with the lifetime of
        `Application.run_async()`, and run run the background tasks in there.

        This is not threadsafe.
        """
    async def cancel_and_wait_for_background_tasks(self) -> None:
        """
        Cancel all background tasks, and wait for the cancellation to complete.
        If any of the background tasks raised an exception, this will also
        propagate the exception.

        (If we had nurseries like Trio, this would be the `__aexit__` of a
        nursery.)
        """
    def cpr_not_supported_callback(self) -> None:
        """
        Called when we don't receive the cursor position response in time.
        """
    @overload
    def exit(self) -> None:
        """Exit without arguments."""
    @overload
    def exit(self, *, result: _AppResult, style: str = '') -> None:
        """Exit with `_AppResult`."""
    @overload
    def exit(self, *, exception: BaseException | type[BaseException], style: str = '') -> None:
        """Exit with exception."""
    async def run_system_command(self, command: str, wait_for_enter: bool = True, display_before_text: AnyFormattedText = '', wait_text: str = 'Press ENTER to continue...') -> None:
        """
        Run system command (While hiding the prompt. When finished, all the
        output will scroll above the prompt.)

        :param command: Shell command to be executed.
        :param wait_for_enter: FWait for the user to press enter, when the
            command is finished.
        :param display_before_text: If given, text to be displayed before the
            command executes.
        :return: A `Future` object.
        """
    def suspend_to_background(self, suspend_group: bool = True) -> None:
        """
        (Not thread safe -- to be called from inside the key bindings.)
        Suspend process.

        :param suspend_group: When true, suspend the whole process group.
            (This is the default, and probably what you want.)
        """
    def print_text(self, text: AnyFormattedText, style: BaseStyle | None = None) -> None:
        """
        Print a list of (style_str, text) tuples to the output.
        (When the UI is running, this method has to be called through
        `run_in_terminal`, otherwise it will destroy the UI.)

        :param text: List of ``(style_str, text)`` tuples.
        :param style: Style class to use. Defaults to the active style in the CLI.
        """
    @property
    def is_running(self) -> bool:
        """`True` when the application is currently active/running."""
    @property
    def is_done(self) -> bool: ...
    def get_used_style_strings(self) -> list[str]:
        """
        Return a list of used style strings. This is helpful for debugging, and
        for writing a new `Style`.
        """

class _CombinedRegistry(KeyBindingsBase):
    """
    The `KeyBindings` of key bindings for a `Application`.
    This merges the global key bindings with the one of the current user
    control.
    """
    app: Incomplete
    def __init__(self, app: Application[_AppResult]) -> None: ...
    @property
    def bindings(self) -> list[Binding]:
        """Not needed - this object is not going to be wrapped in another
        KeyBindings object."""
    def get_bindings_for_keys(self, keys: KeysTuple) -> list[Binding]: ...
    def get_bindings_starting_with_keys(self, keys: KeysTuple) -> list[Binding]: ...
