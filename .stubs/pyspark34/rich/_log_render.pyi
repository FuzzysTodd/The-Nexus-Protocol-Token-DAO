from .console import Console as Console, ConsoleRenderable as ConsoleRenderable, RenderableType as RenderableType
from .table import Table as Table
from .text import Text as Text, TextType as TextType
from _typeshed import Incomplete
from datetime import datetime
from typing import Callable, Iterable

FormatTimeCallable = Callable[[datetime], Text]

class LogRender:
    show_time: Incomplete
    show_level: Incomplete
    show_path: Incomplete
    time_format: Incomplete
    omit_repeated_times: Incomplete
    level_width: Incomplete
    def __init__(self, show_time: bool = True, show_level: bool = False, show_path: bool = True, time_format: str | FormatTimeCallable = '[%x %X]', omit_repeated_times: bool = True, level_width: int | None = 8) -> None: ...
    def __call__(self, console: Console, renderables: Iterable['ConsoleRenderable'], log_time: datetime | None = None, time_format: str | FormatTimeCallable | None = None, level: TextType = '', path: str | None = None, line_no: int | None = None, link_path: str | None = None) -> Table: ...
