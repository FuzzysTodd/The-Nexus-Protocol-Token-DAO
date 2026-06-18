from ..interface.interface_queue import InterfaceQueue as InterfaceQueue
from .settings_static import SettingsStatic as SettingsStatic
from _typeshed import Incomplete
from queue import PriorityQueue
from tensorboard.compat.proto.event_pb2 import ProtoEvent as ProtoEvent
from typing import Any, Dict
from wandb import util as util
from wandb.proto.wandb_internal_pb2 import RunRecord as RunRecord
from wandb.sdk.interface.interface import FilesDict as FilesDict, GlobStr as GlobStr
from wandb.sdk.lib import filesystem as filesystem
from wandb.viz import CustomChart as CustomChart

HistoryDict = Dict[str, Any]
SHUTDOWN_DELAY: int
ERROR_DELAY: int
REMOTE_FILE_TOKEN: str
logger: Incomplete

def is_tfevents_file_created_by(path: str, hostname: str | None, start_time: float | None) -> bool:
    """Check if a path is a tfevents file.

    Optionally checks that it was created by [hostname] after [start_time].

    tensorboard tfevents filename format:
        https://github.com/tensorflow/tensorboard/blob/f3f26b46981da5bd46a5bb93fcf02d9eb7608bc1/tensorboard/summary/writer/event_file_writer.py#L81
    tensorflow tfevents filename format:
        https://github.com/tensorflow/tensorflow/blob/8f597046dc30c14b5413813d02c0e0aed399c177/tensorflow/core/util/events_writer.cc#L68
    """

class TBWatcher:
    def __init__(self, settings: SettingsStatic, run_proto: RunRecord, interface: InterfaceQueue, force: bool = False) -> None: ...
    def add(self, logdir: str, save: bool, root_dir: str) -> None: ...
    def finish(self) -> None: ...

class TBDirWatcher:
    directory_watcher: Incomplete
    tf_compat: Incomplete
    def __init__(self, tbwatcher: TBWatcher, logdir: str, save: bool, namespace: str | None, queue: PriorityQueue, force: bool = False) -> None: ...
    def start(self) -> None: ...
    def process_event(self, event: ProtoEvent) -> None: ...
    def shutdown(self) -> None: ...
    def finish(self) -> None: ...

class Event:
    """An event wrapper to enable priority queueing."""
    event: Incomplete
    namespace: Incomplete
    created_at: Incomplete
    def __init__(self, event: ProtoEvent, namespace: str | None) -> None: ...
    def __lt__(self, other: Event) -> bool: ...

class TBEventConsumer:
    """Consume tfevents from a priority queue.

    There should always only be one of these per run_manager.  We wait for 10 seconds of
    queued events to reduce the chance of multiple tfevent files triggering out of order
    steps.
    """
    tb_history: Incomplete
    def __init__(self, tbwatcher: TBWatcher, queue: PriorityQueue, run_proto: RunRecord, settings: SettingsStatic, delay: int = 10) -> None: ...
    def start(self) -> None: ...
    def finish(self) -> None: ...

class TBHistory:
    def __init__(self) -> None: ...
    def add(self, d: HistoryDict) -> None: ...
