from . import context as context, handler as handler, internal_util as internal_util, sender as sender, writer as writer
from ..interface.interface_queue import InterfaceQueue as InterfaceQueue
from ..lib import tracelog as tracelog
from .internal_util import RecordLoopThread as RecordLoopThread
from .settings_static import SettingsStatic as SettingsStatic
from _typeshed import Incomplete
from queue import Queue
from threading import Event
from wandb.proto.wandb_internal_pb2 import Record as Record, Result as Result

logger: Incomplete

def wandb_internal(settings: SettingsStatic, record_q: Queue[Record], result_q: Queue[Result], port: int | None = None, user_pid: int | None = None) -> None:
    """Internal process function entrypoint.

    Read from record queue and dispatch work to various threads.

    Arguments:
        settings: settings object
        record_q: records to be handled
        result_q: for sending results back

    """
def configure_logging(log_fname: str, log_level: int, run_id: str | None = None) -> None: ...

class HandlerThread(internal_util.RecordLoopThread):
    """Read records from queue and dispatch to handler routines."""
    name: str
    def __init__(self, settings: SettingsStatic, record_q: Queue[Record], result_q: Queue[Result], stopped: Event, writer_q: Queue[Record], interface: InterfaceQueue, context_keeper: context.ContextKeeper, debounce_interval_ms: float = 1000) -> None: ...

class SenderThread(internal_util.RecordLoopThread):
    """Read records from queue and dispatch to sender routines."""
    name: str
    def __init__(self, settings: SettingsStatic, record_q: Queue[Record], result_q: Queue[Result], stopped: Event, interface: InterfaceQueue, context_keeper: context.ContextKeeper, debounce_interval_ms: float = 5000) -> None: ...

class WriterThread(internal_util.RecordLoopThread):
    """Read records from queue and dispatch to writer routines."""
    name: str
    def __init__(self, settings: SettingsStatic, record_q: Queue[Record], result_q: Queue[Result], stopped: Event, interface: InterfaceQueue, sender_q: Queue[Record], context_keeper: context.ContextKeeper, debounce_interval_ms: float = 1000) -> None: ...

class ProcessCheck:
    """Class to help watch a process id to detect when it is dead."""
    check_process_last: float | None
    settings: Incomplete
    pid: Incomplete
    check_process_interval: Incomplete
    def __init__(self, settings: SettingsStatic, user_pid: int | None) -> None: ...
    def is_dead(self) -> bool: ...
