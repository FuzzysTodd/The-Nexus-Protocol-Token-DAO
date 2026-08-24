from .base import ProgressBar, ProgressBarCounter
from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod
from prompt_toolkit.formatted_text import AnyFormattedText
from prompt_toolkit.layout.dimension import AnyDimension

__all__ = ['Formatter', 'Text', 'Label', 'Percentage', 'Bar', 'Progress', 'TimeElapsed', 'TimeLeft', 'IterationsPerSecond', 'SpinningWheel', 'Rainbow', 'create_default_formatters']

class Formatter(metaclass=ABCMeta):
    """
    Base class for any formatter.
    """
    @abstractmethod
    def format(self, progress_bar: ProgressBar, progress: ProgressBarCounter[object], width: int) -> AnyFormattedText: ...
    def get_width(self, progress_bar: ProgressBar) -> AnyDimension: ...

class Text(Formatter):
    """
    Display plain text.
    """
    text: Incomplete
    def __init__(self, text: AnyFormattedText, style: str = '') -> None: ...
    def format(self, progress_bar: ProgressBar, progress: ProgressBarCounter[object], width: int) -> AnyFormattedText: ...
    def get_width(self, progress_bar: ProgressBar) -> AnyDimension: ...

class Label(Formatter):
    """
    Display the name of the current task.

    :param width: If a `width` is given, use this width. Scroll the text if it
        doesn't fit in this width.
    :param suffix: String suffix to be added after the task name, e.g. ': '.
        If no task name was given, no suffix will be added.
    """
    width: Incomplete
    suffix: Incomplete
    def __init__(self, width: AnyDimension = None, suffix: str = '') -> None: ...
    def format(self, progress_bar: ProgressBar, progress: ProgressBarCounter[object], width: int) -> AnyFormattedText: ...
    def get_width(self, progress_bar: ProgressBar) -> AnyDimension: ...

class Percentage(Formatter):
    """
    Display the progress as a percentage.
    """
    template: str
    def format(self, progress_bar: ProgressBar, progress: ProgressBarCounter[object], width: int) -> AnyFormattedText: ...
    def get_width(self, progress_bar: ProgressBar) -> AnyDimension: ...

class Bar(Formatter):
    """
    Display the progress bar itself.
    """
    template: str
    start: Incomplete
    end: Incomplete
    sym_a: Incomplete
    sym_b: Incomplete
    sym_c: Incomplete
    unknown: Incomplete
    def __init__(self, start: str = '[', end: str = ']', sym_a: str = '=', sym_b: str = '>', sym_c: str = ' ', unknown: str = '#') -> None: ...
    def format(self, progress_bar: ProgressBar, progress: ProgressBarCounter[object], width: int) -> AnyFormattedText: ...
    def get_width(self, progress_bar: ProgressBar) -> AnyDimension: ...

class Progress(Formatter):
    '''
    Display the progress as text.  E.g. "8/20"
    '''
    template: str
    def format(self, progress_bar: ProgressBar, progress: ProgressBarCounter[object], width: int) -> AnyFormattedText: ...
    def get_width(self, progress_bar: ProgressBar) -> AnyDimension: ...

class TimeElapsed(Formatter):
    """
    Display the elapsed time.
    """
    def format(self, progress_bar: ProgressBar, progress: ProgressBarCounter[object], width: int) -> AnyFormattedText: ...
    def get_width(self, progress_bar: ProgressBar) -> AnyDimension: ...

class TimeLeft(Formatter):
    """
    Display the time left.
    """
    template: str
    unknown: str
    def format(self, progress_bar: ProgressBar, progress: ProgressBarCounter[object], width: int) -> AnyFormattedText: ...
    def get_width(self, progress_bar: ProgressBar) -> AnyDimension: ...

class IterationsPerSecond(Formatter):
    """
    Display the iterations per second.
    """
    template: str
    def format(self, progress_bar: ProgressBar, progress: ProgressBarCounter[object], width: int) -> AnyFormattedText: ...
    def get_width(self, progress_bar: ProgressBar) -> AnyDimension: ...

class SpinningWheel(Formatter):
    """
    Display a spinning wheel.
    """
    characters: str
    def format(self, progress_bar: ProgressBar, progress: ProgressBarCounter[object], width: int) -> AnyFormattedText: ...
    def get_width(self, progress_bar: ProgressBar) -> AnyDimension: ...

class Rainbow(Formatter):
    """
    For the fun. Add rainbow colors to any of the other formatters.
    """
    colors: Incomplete
    formatter: Incomplete
    def __init__(self, formatter: Formatter) -> None: ...
    def format(self, progress_bar: ProgressBar, progress: ProgressBarCounter[object], width: int) -> AnyFormattedText: ...
    def get_width(self, progress_bar: ProgressBar) -> AnyDimension: ...

def create_default_formatters() -> list[Formatter]:
    """
    Return the list of default formatters.
    """
