import datetime
from .formatters import Formatter
from _typeshed import Incomplete
from prompt_toolkit.formatted_text import AnyFormattedText
from prompt_toolkit.input import Input
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.key_binding.key_processor import KeyPressEvent
from prompt_toolkit.layout.controls import UIContent, UIControl
from prompt_toolkit.output import ColorDepth, Output
from prompt_toolkit.styles import BaseStyle
from typing import Callable, Generic, Iterable, Iterator, Sequence, TextIO

__all__ = ['ProgressBar']

E = KeyPressEvent

class ProgressBar:
    '''
    Progress bar context manager.

    Usage ::

        with ProgressBar(...) as pb:
            for item in pb(data):
                ...

    :param title: Text to be displayed above the progress bars. This can be a
        callable or formatted text as well.
    :param formatters: List of :class:`.Formatter` instances.
    :param bottom_toolbar: Text to be displayed in the bottom toolbar. This
        can be a callable or formatted text.
    :param style: :class:`prompt_toolkit.styles.BaseStyle` instance.
    :param key_bindings: :class:`.KeyBindings` instance.
    :param cancel_callback: Callback function that\'s called when control-c is
        pressed by the user. This can be used for instance to start "proper"
        cancellation if the wrapped code supports it.
    :param file: The file object used for rendering, by default `sys.stderr` is used.

    :param color_depth: `prompt_toolkit` `ColorDepth` instance.
    :param output: :class:`~prompt_toolkit.output.Output` instance.
    :param input: :class:`~prompt_toolkit.input.Input` instance.
    '''
    title: Incomplete
    formatters: Incomplete
    bottom_toolbar: Incomplete
    counters: Incomplete
    style: Incomplete
    key_bindings: Incomplete
    cancel_callback: Incomplete
    color_depth: Incomplete
    output: Incomplete
    input: Incomplete
    def __init__(self, title: AnyFormattedText = None, formatters: Sequence[Formatter] | None = None, bottom_toolbar: AnyFormattedText = None, style: BaseStyle | None = None, key_bindings: KeyBindings | None = None, cancel_callback: Callable[[], None] | None = None, file: TextIO | None = None, color_depth: ColorDepth | None = None, output: Output | None = None, input: Input | None = None) -> None: ...
    app: Incomplete
    def __enter__(self) -> ProgressBar: ...
    def __exit__(self, *a: object) -> None: ...
    def __call__(self, data: Iterable[_T] | None = None, label: AnyFormattedText = '', remove_when_done: bool = False, total: int | None = None) -> ProgressBarCounter[_T]:
        """
        Start a new counter.

        :param label: Title text or description for this progress. (This can be
            formatted text as well).
        :param remove_when_done: When `True`, hide this progress bar.
        :param total: Specify the maximum value if it can't be calculated by
            calling ``len``.
        """
    def invalidate(self) -> None: ...

class _ProgressControl(UIControl):
    """
    User control for the progress bar.
    """
    progress_bar: Incomplete
    formatter: Incomplete
    def __init__(self, progress_bar: ProgressBar, formatter: Formatter, cancel_callback: Callable[[], None] | None) -> None: ...
    def create_content(self, width: int, height: int) -> UIContent: ...
    def is_focusable(self) -> bool: ...
    def get_key_bindings(self) -> KeyBindings: ...

class ProgressBarCounter(Generic[_CounterItem]):
    """
    An individual counter (A progress bar can have multiple counters).
    """
    start_time: Incomplete
    stop_time: Incomplete
    progress_bar: Incomplete
    data: Incomplete
    items_completed: int
    label: Incomplete
    remove_when_done: Incomplete
    total: Incomplete
    def __init__(self, progress_bar: ProgressBar, data: Iterable[_CounterItem] | None = None, label: AnyFormattedText = '', remove_when_done: bool = False, total: int | None = None) -> None: ...
    def __iter__(self) -> Iterator[_CounterItem]: ...
    def item_completed(self) -> None:
        """
        Start handling the next item.

        (Can be called manually in case we don't have a collection to loop through.)
        """
    @property
    def done(self) -> bool:
        """Whether a counter has been completed.

        Done counter have been stopped (see stopped) and removed depending on
        remove_when_done value.

        Contrast this with stopped. A stopped counter may be terminated before
        100% completion. A done counter has reached its 100% completion.
        """
    @done.setter
    def done(self, value: bool) -> None: ...
    @property
    def stopped(self) -> bool:
        """Whether a counter has been stopped.

        Stopped counters no longer have increasing time_elapsed. This distinction is
        also used to prevent the Bar formatter with unknown totals from continuing to run.

        A stopped counter (but not done) can be used to signal that a given counter has
        encountered an error but allows other counters to continue
        (e.g. download X of Y failed). Given how only done counters are removed
        (see remove_when_done) this can help aggregate failures from a large number of
        successes.

        Contrast this with done. A done counter has reached its 100% completion.
        A stopped counter may be terminated before 100% completion.
        """
    @stopped.setter
    def stopped(self, value: bool) -> None: ...
    @property
    def percentage(self) -> float: ...
    @property
    def time_elapsed(self) -> datetime.timedelta:
        """
        Return how much time has been elapsed since the start.
        """
    @property
    def time_left(self) -> datetime.timedelta | None:
        """
        Timedelta representing the time left.
        """
