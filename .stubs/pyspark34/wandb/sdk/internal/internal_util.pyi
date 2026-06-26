import threading
from ..lib import tracelog as tracelog
from _typeshed import Incomplete
from queue import Queue
from threading import Event
from types import TracebackType
from typing import Tuple, Type
from wandb.proto.wandb_internal_pb2 import Record as Record, Result as Result

ExceptionType = Tuple[Type[BaseException], BaseException, TracebackType] | Tuple[None, None, None]
logger: Incomplete

class ExceptionThread(threading.Thread):
    """Class to catch exceptions when running a thread."""
    def __init__(self, stopped: Event) -> None: ...
    def run(self) -> None: ...
    def get_exception(self) -> ExceptionType | None: ...

class RecordLoopThread(ExceptionThread):
    """Class to manage reading from queues safely."""
    def __init__(self, input_record_q: Queue[Record], result_q: Queue[Result], stopped: Event, debounce_interval_ms: float = 1000) -> None: ...
