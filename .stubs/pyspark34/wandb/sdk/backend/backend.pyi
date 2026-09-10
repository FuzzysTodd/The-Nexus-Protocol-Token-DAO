import multiprocessing
import threading
from ..service.service_sock import ServiceSockInterface as ServiceSockInterface
from ..wandb_run import Run as Run
from _typeshed import Incomplete
from typing import Any, Callable, Dict
from wandb.proto.wandb_internal_pb2 import Record as Record, Result as Result
from wandb.sdk.interface.interface import InterfaceBase as InterfaceBase
from wandb.sdk.interface.interface_queue import InterfaceQueue as InterfaceQueue
from wandb.sdk.internal.internal import wandb_internal as wandb_internal
from wandb.sdk.internal.settings_static import SettingsStatic as SettingsStatic
from wandb.sdk.lib.mailbox import Mailbox as Mailbox
from wandb.sdk.wandb_manager import _Manager
from wandb.sdk.wandb_settings import Settings as Settings

RecordQueue: Incomplete
ResultQueue: Incomplete
logger: Incomplete

class BackendThread(threading.Thread):
    """Class to running internal process as a thread."""
    name: str
    daemon: bool
    pid: int
    def __init__(self, target: Callable, kwargs: Dict[str, Any]) -> None: ...
    def run(self) -> None: ...

class Backend:
    interface: InterfaceBase | None
    wandb_process: multiprocessing.process.BaseProcess | None
    record_q: RecordQueue | None
    result_q: ResultQueue | None
    def __init__(self, mailbox: Mailbox, settings: Settings | None = None, log_level: int | None = None, manager: _Manager | None = None) -> None: ...
    def ensure_launched(self) -> None:
        """Launch backend worker if not running."""
    def server_status(self) -> None:
        """Report server status."""
    def cleanup(self) -> None: ...
