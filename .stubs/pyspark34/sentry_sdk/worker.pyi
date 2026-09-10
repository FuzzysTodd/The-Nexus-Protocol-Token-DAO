from sentry_sdk._compat import check_thread_support as check_thread_support
from sentry_sdk._queue import FullError as FullError, Queue as Queue
from sentry_sdk._types import TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.consts import DEFAULT_QUEUE_SIZE as DEFAULT_QUEUE_SIZE
from sentry_sdk.utils import logger as logger
from typing import Any, Callable

class BackgroundWorker:
    def __init__(self, queue_size: int = ...) -> None: ...
    @property
    def is_alive(self) -> bool: ...
    def start(self) -> None: ...
    def kill(self) -> None:
        """
        Kill worker thread. Returns immediately. Not useful for
        waiting on shutdown for events, use `flush` for that.
        """
    def flush(self, timeout: float, callback: Any | None = None) -> None: ...
    def full(self) -> bool: ...
    def submit(self, callback: Callable[[], None]) -> bool: ...
