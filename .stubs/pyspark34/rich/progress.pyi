import abc
import typing
from . import filesize as filesize, get_console as get_console
from .console import Console as Console, Group as Group, JustifyMethod as JustifyMethod, RenderableType as RenderableType
from .highlighter import Highlighter as Highlighter
from .jupyter import JupyterMixin as JupyterMixin
from .live import Live as Live
from .progress_bar import ProgressBar as ProgressBar
from .spinner import Spinner as Spinner
from .style import StyleType as StyleType
from .table import Column as Column, Table as Table
from .text import Text as Text, TextType as TextType
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from dataclasses import dataclass
from io import RawIOBase
from mmap import mmap
from os import PathLike
from threading import Thread
from types import TracebackType
from typing import Any, BinaryIO, Callable, ContextManager, Dict, Generic, Iterable, List, Literal, NamedTuple, Sequence, TextIO, Tuple, Type, TypeVar

TaskID: Incomplete
ProgressType = TypeVar('ProgressType')
GetTimeCallable = Callable[[], float]

class _TrackThread(Thread):
    """A thread to periodically update progress."""
    progress: Incomplete
    task_id: Incomplete
    update_period: Incomplete
    done: Incomplete
    completed: int
    def __init__(self, progress: Progress, task_id: TaskID, update_period: float) -> None: ...
    def run(self) -> None: ...
    def __enter__(self) -> _TrackThread: ...
    def __exit__(self, exc_type: Type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> None: ...

def track(sequence: Sequence[ProgressType] | Iterable[ProgressType], description: str = 'Working...', total: float | None = None, auto_refresh: bool = True, console: Console | None = None, transient: bool = False, get_time: Callable[[], float] | None = None, refresh_per_second: float = 10, style: StyleType = 'bar.back', complete_style: StyleType = 'bar.complete', finished_style: StyleType = 'bar.finished', pulse_style: StyleType = 'bar.pulse', update_period: float = 0.1, disable: bool = False, show_speed: bool = True) -> Iterable[ProgressType]:
    '''Track progress by iterating over a sequence.

    Args:
        sequence (Iterable[ProgressType]): A sequence (must support "len") you wish to iterate over.
        description (str, optional): Description of task show next to progress bar. Defaults to "Working".
        total: (float, optional): Total number of steps. Default is len(sequence).
        auto_refresh (bool, optional): Automatic refresh, disable to force a refresh after each iteration. Default is True.
        transient: (bool, optional): Clear the progress on exit. Defaults to False.
        console (Console, optional): Console to write to. Default creates internal Console instance.
        refresh_per_second (float): Number of times per second to refresh the progress information. Defaults to 10.
        style (StyleType, optional): Style for the bar background. Defaults to "bar.back".
        complete_style (StyleType, optional): Style for the completed bar. Defaults to "bar.complete".
        finished_style (StyleType, optional): Style for a finished bar. Defaults to "bar.finished".
        pulse_style (StyleType, optional): Style for pulsing bars. Defaults to "bar.pulse".
        update_period (float, optional): Minimum time (in seconds) between calls to update(). Defaults to 0.1.
        disable (bool, optional): Disable display of progress.
        show_speed (bool, optional): Show speed if total isn\'t known. Defaults to True.
    Returns:
        Iterable[ProgressType]: An iterable of the values in the sequence.

    '''

class _Reader(RawIOBase, BinaryIO):
    """A reader that tracks progress while it's being read from."""
    handle: Incomplete
    progress: Incomplete
    task: Incomplete
    close_handle: Incomplete
    def __init__(self, handle: BinaryIO, progress: Progress, task: TaskID, close_handle: bool = True) -> None: ...
    def __enter__(self) -> _Reader: ...
    def __exit__(self, exc_type: Type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> None: ...
    def __iter__(self) -> BinaryIO: ...
    def __next__(self) -> bytes: ...
    @property
    def closed(self) -> bool: ...
    def fileno(self) -> int: ...
    def isatty(self) -> bool: ...
    @property
    def mode(self) -> str: ...
    @property
    def name(self) -> str: ...
    def readable(self) -> bool: ...
    def seekable(self) -> bool: ...
    def writable(self) -> bool: ...
    def read(self, size: int = -1) -> bytes: ...
    def readinto(self, b: bytearray | memoryview | mmap): ...
    def readline(self, size: int = -1) -> bytes: ...
    def readlines(self, hint: int = -1) -> List[bytes]: ...
    def close(self) -> None: ...
    def seek(self, offset: int, whence: int = 0) -> int: ...
    def tell(self) -> int: ...
    def write(self, s: Any) -> int: ...

class _ReadContext(ContextManager[_I], Generic[_I]):
    """A utility class to handle a context for both a reader and a progress."""
    progress: Incomplete
    reader: Incomplete
    def __init__(self, progress: Progress, reader: _I) -> None: ...
    def __enter__(self) -> _I: ...
    def __exit__(self, exc_type: Type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> None: ...

def wrap_file(file: BinaryIO, total: int, *, description: str = 'Reading...', auto_refresh: bool = True, console: Console | None = None, transient: bool = False, get_time: Callable[[], float] | None = None, refresh_per_second: float = 10, style: StyleType = 'bar.back', complete_style: StyleType = 'bar.complete', finished_style: StyleType = 'bar.finished', pulse_style: StyleType = 'bar.pulse', disable: bool = False) -> ContextManager[BinaryIO]:
    '''Read bytes from a file while tracking progress.

    Args:
        file (Union[str, PathLike[str], BinaryIO]): The path to the file to read, or a file-like object in binary mode.
        total (int): Total number of bytes to read.
        description (str, optional): Description of task show next to progress bar. Defaults to "Reading".
        auto_refresh (bool, optional): Automatic refresh, disable to force a refresh after each iteration. Default is True.
        transient: (bool, optional): Clear the progress on exit. Defaults to False.
        console (Console, optional): Console to write to. Default creates internal Console instance.
        refresh_per_second (float): Number of times per second to refresh the progress information. Defaults to 10.
        style (StyleType, optional): Style for the bar background. Defaults to "bar.back".
        complete_style (StyleType, optional): Style for the completed bar. Defaults to "bar.complete".
        finished_style (StyleType, optional): Style for a finished bar. Defaults to "bar.finished".
        pulse_style (StyleType, optional): Style for pulsing bars. Defaults to "bar.pulse".
        disable (bool, optional): Disable display of progress.
    Returns:
        ContextManager[BinaryIO]: A context manager yielding a progress reader.

    '''
@typing.overload
def open(file: str | PathLike[str] | bytes, mode: Literal['rt'] | Literal['r'], buffering: int = -1, encoding: str | None = None, errors: str | None = None, newline: str | None = None, *, total: int | None = None, description: str = 'Reading...', auto_refresh: bool = True, console: Console | None = None, transient: bool = False, get_time: Callable[[], float] | None = None, refresh_per_second: float = 10, style: StyleType = 'bar.back', complete_style: StyleType = 'bar.complete', finished_style: StyleType = 'bar.finished', pulse_style: StyleType = 'bar.pulse', disable: bool = False) -> ContextManager[TextIO]: ...
@typing.overload
def open(file: str | PathLike[str] | bytes, mode: Literal['rb'], buffering: int = -1, encoding: str | None = None, errors: str | None = None, newline: str | None = None, *, total: int | None = None, description: str = 'Reading...', auto_refresh: bool = True, console: Console | None = None, transient: bool = False, get_time: Callable[[], float] | None = None, refresh_per_second: float = 10, style: StyleType = 'bar.back', complete_style: StyleType = 'bar.complete', finished_style: StyleType = 'bar.finished', pulse_style: StyleType = 'bar.pulse', disable: bool = False) -> ContextManager[BinaryIO]: ...

class ProgressColumn(ABC, metaclass=abc.ABCMeta):
    """Base class for a widget to use in progress display."""
    max_refresh: float | None
    def __init__(self, table_column: Column | None = None) -> None: ...
    def get_table_column(self) -> Column:
        """Get a table column, used to build tasks table."""
    def __call__(self, task: Task) -> RenderableType:
        """Called by the Progress object to return a renderable for the given task.

        Args:
            task (Task): An object containing information regarding the task.

        Returns:
            RenderableType: Anything renderable (including str).
        """
    @abstractmethod
    def render(self, task: Task) -> RenderableType:
        """Should return a renderable object."""

class RenderableColumn(ProgressColumn):
    """A column to insert an arbitrary column.

    Args:
        renderable (RenderableType, optional): Any renderable. Defaults to empty string.
    """
    renderable: Incomplete
    def __init__(self, renderable: RenderableType = '', *, table_column: Column | None = None) -> None: ...
    def render(self, task: Task) -> RenderableType: ...

class SpinnerColumn(ProgressColumn):
    '''A column with a \'spinner\' animation.

    Args:
        spinner_name (str, optional): Name of spinner animation. Defaults to "dots".
        style (StyleType, optional): Style of spinner. Defaults to "progress.spinner".
        speed (float, optional): Speed factor of spinner. Defaults to 1.0.
        finished_text (TextType, optional): Text used when task is finished. Defaults to " ".
    '''
    spinner: Incomplete
    finished_text: Incomplete
    def __init__(self, spinner_name: str = 'dots', style: StyleType | None = 'progress.spinner', speed: float = 1.0, finished_text: TextType = ' ', table_column: Column | None = None) -> None: ...
    def set_spinner(self, spinner_name: str, spinner_style: StyleType | None = 'progress.spinner', speed: float = 1.0) -> None:
        '''Set a new spinner.

        Args:
            spinner_name (str): Spinner name, see python -m rich.spinner.
            spinner_style (Optional[StyleType], optional): Spinner style. Defaults to "progress.spinner".
            speed (float, optional): Speed factor of spinner. Defaults to 1.0.
        '''
    def render(self, task: Task) -> RenderableType: ...

class TextColumn(ProgressColumn):
    """A column containing text."""
    text_format: Incomplete
    justify: Incomplete
    style: Incomplete
    markup: Incomplete
    highlighter: Incomplete
    def __init__(self, text_format: str, style: StyleType = 'none', justify: JustifyMethod = 'left', markup: bool = True, highlighter: Highlighter | None = None, table_column: Column | None = None) -> None: ...
    def render(self, task: Task) -> Text: ...

class BarColumn(ProgressColumn):
    '''Renders a visual progress bar.

    Args:
        bar_width (Optional[int], optional): Width of bar or None for full width. Defaults to 40.
        style (StyleType, optional): Style for the bar background. Defaults to "bar.back".
        complete_style (StyleType, optional): Style for the completed bar. Defaults to "bar.complete".
        finished_style (StyleType, optional): Style for a finished bar. Defaults to "bar.finished".
        pulse_style (StyleType, optional): Style for pulsing bars. Defaults to "bar.pulse".
    '''
    bar_width: Incomplete
    style: Incomplete
    complete_style: Incomplete
    finished_style: Incomplete
    pulse_style: Incomplete
    def __init__(self, bar_width: int | None = 40, style: StyleType = 'bar.back', complete_style: StyleType = 'bar.complete', finished_style: StyleType = 'bar.finished', pulse_style: StyleType = 'bar.pulse', table_column: Column | None = None) -> None: ...
    def render(self, task: Task) -> ProgressBar:
        """Gets a progress bar widget for a task."""

class TimeElapsedColumn(ProgressColumn):
    """Renders time elapsed."""
    def render(self, task: Task) -> Text:
        """Show time elapsed."""

class TaskProgressColumn(TextColumn):
    '''Show task progress as a percentage.

    Args:
        text_format (str, optional): Format for percentage display. Defaults to "[progress.percentage]{task.percentage:>3.0f}%".
        text_format_no_percentage (str, optional): Format if percentage is unknown. Defaults to "".
        style (StyleType, optional): Style of output. Defaults to "none".
        justify (JustifyMethod, optional): Text justification. Defaults to "left".
        markup (bool, optional): Enable markup. Defaults to True.
        highlighter (Optional[Highlighter], optional): Highlighter to apply to output. Defaults to None.
        table_column (Optional[Column], optional): Table Column to use. Defaults to None.
        show_speed (bool, optional): Show speed if total is unknown. Defaults to False.
    '''
    text_format_no_percentage: Incomplete
    show_speed: Incomplete
    def __init__(self, text_format: str = '[progress.percentage]{task.percentage:>3.0f}%', text_format_no_percentage: str = '', style: StyleType = 'none', justify: JustifyMethod = 'left', markup: bool = True, highlighter: Highlighter | None = None, table_column: Column | None = None, show_speed: bool = False) -> None: ...
    @classmethod
    def render_speed(cls, speed: float | None) -> Text:
        """Render the speed in iterations per second.

        Args:
            task (Task): A Task object.

        Returns:
            Text: Text object containing the task speed.
        """
    def render(self, task: Task) -> Text: ...

class TimeRemainingColumn(ProgressColumn):
    """Renders estimated time remaining.

    Args:
        compact (bool, optional): Render MM:SS when time remaining is less than an hour. Defaults to False.
        elapsed_when_finished (bool, optional): Render time elapsed when the task is finished. Defaults to False.
    """
    max_refresh: float
    compact: Incomplete
    elapsed_when_finished: Incomplete
    def __init__(self, compact: bool = False, elapsed_when_finished: bool = False, table_column: Column | None = None) -> None: ...
    def render(self, task: Task) -> Text:
        """Show time remaining."""

class FileSizeColumn(ProgressColumn):
    """Renders completed filesize."""
    def render(self, task: Task) -> Text:
        """Show data completed."""

class TotalFileSizeColumn(ProgressColumn):
    """Renders total filesize."""
    def render(self, task: Task) -> Text:
        """Show data completed."""

class MofNCompleteColumn(ProgressColumn):
    '''Renders completed count/total, e.g. \'  10/1000\'.

    Best for bounded tasks with int quantities.

    Space pads the completed count so that progress length does not change as task progresses
    past powers of 10.

    Args:
        separator (str, optional): Text to separate completed and total values. Defaults to "/".
    '''
    separator: Incomplete
    def __init__(self, separator: str = '/', table_column: Column | None = None) -> None: ...
    def render(self, task: Task) -> Text:
        """Show completed/total."""

class DownloadColumn(ProgressColumn):
    """Renders file size downloaded and total, e.g. '0.5/2.3 GB'.

    Args:
        binary_units (bool, optional): Use binary units, KiB, MiB etc. Defaults to False.
    """
    binary_units: Incomplete
    def __init__(self, binary_units: bool = False, table_column: Column | None = None) -> None: ...
    def render(self, task: Task) -> Text:
        """Calculate common unit for completed and total."""

class TransferSpeedColumn(ProgressColumn):
    """Renders human readable transfer speed."""
    def render(self, task: Task) -> Text:
        """Show data transfer speed."""

class ProgressSample(NamedTuple):
    """Sample of progress for a given time."""
    timestamp: float
    completed: float

@dataclass
class Task:
    """Information regarding a progress task.

    This object should be considered read-only outside of the :class:`~Progress` class.

    """
    id: TaskID
    description: str
    total: float | None
    completed: float
    finished_time: float | None = ...
    visible: bool = ...
    fields: Dict[str, Any] = ...
    start_time: float | None = ...
    stop_time: float | None = ...
    finished_speed: float | None = ...
    def get_time(self) -> float:
        """float: Get the current time, in seconds."""
    @property
    def started(self) -> bool:
        """bool: Check if the task as started."""
    @property
    def remaining(self) -> float | None:
        """Optional[float]: Get the number of steps remaining, if a non-None total was set."""
    @property
    def elapsed(self) -> float | None:
        """Optional[float]: Time elapsed since task was started, or ``None`` if the task hasn't started."""
    @property
    def finished(self) -> bool:
        """Check if the task has finished."""
    @property
    def percentage(self) -> float:
        """float: Get progress of task as a percentage. If a None total was set, returns 0"""
    @property
    def speed(self) -> float | None:
        """Optional[float]: Get the estimated speed in steps per second."""
    @property
    def time_remaining(self) -> float | None:
        """Optional[float]: Get estimated time to completion, or ``None`` if no data."""
    def __init__(self, id, description, total, completed, _get_time, finished_time, visible, fields, finished_speed, _lock) -> None: ...

class Progress(JupyterMixin):
    """Renders an auto-updating progress bar(s).

    Args:
        console (Console, optional): Optional Console instance. Default will an internal Console instance writing to stdout.
        auto_refresh (bool, optional): Enable auto refresh. If disabled, you will need to call `refresh()`.
        refresh_per_second (Optional[float], optional): Number of times per second to refresh the progress information or None to use default (10). Defaults to None.
        speed_estimate_period: (float, optional): Period (in seconds) used to calculate the speed estimate. Defaults to 30.
        transient: (bool, optional): Clear the progress on exit. Defaults to False.
        redirect_stdout: (bool, optional): Enable redirection of stdout, so ``print`` may be used. Defaults to True.
        redirect_stderr: (bool, optional): Enable redirection of stderr. Defaults to True.
        get_time: (Callable, optional): A callable that gets the current time, or None to use Console.get_time. Defaults to None.
        disable (bool, optional): Disable progress display. Defaults to False
        expand (bool, optional): Expand tasks table to fit width. Defaults to False.
    """
    columns: Incomplete
    speed_estimate_period: Incomplete
    disable: Incomplete
    expand: Incomplete
    live: Incomplete
    get_time: Incomplete
    print: Incomplete
    log: Incomplete
    def __init__(self, *columns: str | ProgressColumn, console: Console | None = None, auto_refresh: bool = True, refresh_per_second: float = 10, speed_estimate_period: float = 30.0, transient: bool = False, redirect_stdout: bool = True, redirect_stderr: bool = True, get_time: GetTimeCallable | None = None, disable: bool = False, expand: bool = False) -> None: ...
    @classmethod
    def get_default_columns(cls) -> Tuple[ProgressColumn, ...]:
        '''Get the default columns used for a new Progress instance:
           - a text column for the description (TextColumn)
           - the bar itself (BarColumn)
           - a text column showing completion percentage (TextColumn)
           - an estimated-time-remaining column (TimeRemainingColumn)
        If the Progress instance is created without passing a columns argument,
        the default columns defined here will be used.

        You can also create a Progress instance using custom columns before
        and/or after the defaults, as in this example:

            progress = Progress(
                SpinnerColumn(),
                *Progress.default_columns(),
                "Elapsed:",
                TimeElapsedColumn(),
            )

        This code shows the creation of a Progress display, containing
        a spinner to the left, the default columns, and a labeled elapsed
        time column.
        '''
    @property
    def console(self) -> Console: ...
    @property
    def tasks(self) -> List[Task]:
        """Get a list of Task instances."""
    @property
    def task_ids(self) -> List[TaskID]:
        """A list of task IDs."""
    @property
    def finished(self) -> bool:
        """Check if all tasks have been completed."""
    def start(self) -> None:
        """Start the progress display."""
    def stop(self) -> None:
        """Stop the progress display."""
    def __enter__(self) -> Progress: ...
    def __exit__(self, exc_type: Type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> None: ...
    def track(self, sequence: Iterable[ProgressType] | Sequence[ProgressType], total: float | None = None, task_id: TaskID | None = None, description: str = 'Working...', update_period: float = 0.1) -> Iterable[ProgressType]:
        """Track progress by iterating over a sequence.

        Args:
            sequence (Sequence[ProgressType]): A sequence of values you want to iterate over and track progress.
            total: (float, optional): Total number of steps. Default is len(sequence).
            task_id: (TaskID): Task to track. Default is new task.
            description: (str, optional): Description of task, if new task is created.
            update_period (float, optional): Minimum time (in seconds) between calls to update(). Defaults to 0.1.

        Returns:
            Iterable[ProgressType]: An iterable of values taken from the provided sequence.
        """
    def wrap_file(self, file: BinaryIO, total: int | None = None, *, task_id: TaskID | None = None, description: str = 'Reading...') -> BinaryIO:
        """Track progress file reading from a binary file.

        Args:
            file (BinaryIO): A file-like object opened in binary mode.
            total (int, optional): Total number of bytes to read. This must be provided unless a task with a total is also given.
            task_id (TaskID): Task to track. Default is new task.
            description (str, optional): Description of task, if new task is created.

        Returns:
            BinaryIO: A readable file-like object in binary mode.

        Raises:
            ValueError: When no total value can be extracted from the arguments or the task.
        """
    @typing.overload
    def open(self, file: str | PathLike[str] | bytes, mode: Literal['rb'], buffering: int = -1, encoding: str | None = None, errors: str | None = None, newline: str | None = None, *, total: int | None = None, task_id: TaskID | None = None, description: str = 'Reading...') -> BinaryIO: ...
    @typing.overload
    def open(self, file: str | PathLike[str] | bytes, mode: Literal['r'] | Literal['rt'], buffering: int = -1, encoding: str | None = None, errors: str | None = None, newline: str | None = None, *, total: int | None = None, task_id: TaskID | None = None, description: str = 'Reading...') -> TextIO: ...
    def start_task(self, task_id: TaskID) -> None:
        """Start a task.

        Starts a task (used when calculating elapsed time). You may need to call this manually,
        if you called ``add_task`` with ``start=False``.

        Args:
            task_id (TaskID): ID of task.
        """
    def stop_task(self, task_id: TaskID) -> None:
        """Stop a task.

        This will freeze the elapsed time on the task.

        Args:
            task_id (TaskID): ID of task.
        """
    def update(self, task_id: TaskID, *, total: float | None = None, completed: float | None = None, advance: float | None = None, description: str | None = None, visible: bool | None = None, refresh: bool = False, **fields: Any) -> None:
        """Update information associated with a task.

        Args:
            task_id (TaskID): Task id (returned by add_task).
            total (float, optional): Updates task.total if not None.
            completed (float, optional): Updates task.completed if not None.
            advance (float, optional): Add a value to task.completed if not None.
            description (str, optional): Change task description if not None.
            visible (bool, optional): Set visible flag if not None.
            refresh (bool): Force a refresh of progress information. Default is False.
            **fields (Any): Additional data fields required for rendering.
        """
    def reset(self, task_id: TaskID, *, start: bool = True, total: float | None = None, completed: int = 0, visible: bool | None = None, description: str | None = None, **fields: Any) -> None:
        """Reset a task so completed is 0 and the clock is reset.

        Args:
            task_id (TaskID): ID of task.
            start (bool, optional): Start the task after reset. Defaults to True.
            total (float, optional): New total steps in task, or None to use current total. Defaults to None.
            completed (int, optional): Number of steps completed. Defaults to 0.
            visible (bool, optional): Enable display of the task. Defaults to True.
            description (str, optional): Change task description if not None. Defaults to None.
            **fields (str): Additional data fields required for rendering.
        """
    def advance(self, task_id: TaskID, advance: float = 1) -> None:
        """Advance task by a number of steps.

        Args:
            task_id (TaskID): ID of task.
            advance (float): Number of steps to advance. Default is 1.
        """
    def refresh(self) -> None:
        """Refresh (render) the progress information."""
    def get_renderable(self) -> RenderableType:
        """Get a renderable for the progress display."""
    def get_renderables(self) -> Iterable[RenderableType]:
        """Get a number of renderables for the progress display."""
    def make_tasks_table(self, tasks: Iterable[Task]) -> Table:
        """Get a table to render the Progress display.

        Args:
            tasks (Iterable[Task]): An iterable of Task instances, one per row of the table.

        Returns:
            Table: A table instance.
        """
    def __rich__(self) -> RenderableType:
        """Makes the Progress class itself renderable."""
    def add_task(self, description: str, start: bool = True, total: float | None = 100.0, completed: int = 0, visible: bool = True, **fields: Any) -> TaskID:
        """Add a new 'task' to the Progress display.

        Args:
            description (str): A description of the task.
            start (bool, optional): Start the task immediately (to calculate elapsed time). If set to False,
                you will need to call `start` manually. Defaults to True.
            total (float, optional): Number of total steps in the progress if known.
                Set to None to render a pulsing animation. Defaults to 100.
            completed (int, optional): Number of steps completed so far. Defaults to 0.
            visible (bool, optional): Enable display of the task. Defaults to True.
            **fields (str): Additional data fields required for rendering.

        Returns:
            TaskID: An ID you can use when calling `update`.
        """
    def remove_task(self, task_id: TaskID) -> None:
        """Delete a task if it exists.

        Args:
            task_id (TaskID): A task ID.

        """
