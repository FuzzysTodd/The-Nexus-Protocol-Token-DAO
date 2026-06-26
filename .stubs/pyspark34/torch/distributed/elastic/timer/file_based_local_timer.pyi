from _typeshed import Incomplete
from torch.distributed.elastic.timer.api import TimerClient, TimerRequest
from typing import Callable, Dict, List, Set

__all__ = ['FileTimerClient', 'FileTimerRequest', 'FileTimerServer']

class FileTimerRequest(TimerRequest):
    '''
    Data object representing a countdown timer acquisition and release
    that is used between the ``FileTimerClient`` and ``FileTimerServer``.
    A negative ``expiration_time`` should be interpreted as a "release"
    request.
    ``signal`` is the signal to reap the worker process from the server
    process.
    '''
    version: int
    worker_pid: Incomplete
    scope_id: Incomplete
    expiration_time: Incomplete
    signal: Incomplete
    def __init__(self, worker_pid: int, scope_id: str, expiration_time: float, signal: int = 0) -> None: ...
    def __eq__(self, other) -> bool: ...
    def to_json(self) -> str: ...

class FileTimerClient(TimerClient):
    """
    Client side of ``FileTimerServer``. This client is meant to be used
    on the same host that the ``FileTimerServer`` is running on and uses
    pid to uniquely identify a worker.
    This client uses a named_pipe to send timer requests to the
    ``FileTimerServer``. This client is a producer while the
    ``FileTimerServer`` is a consumer. Multiple clients can work with
    the same ``FileTimerServer``.

    Args:

        file_path: str, the path of a FIFO special file. ``FileTimerServer``
                        must have created it by calling os.mkfifo().

        signal: signal, the signal to use to kill the process. Using a
                        negative or zero signal will not kill the process.
    """
    signal: Incomplete
    def __init__(self, file_path: str, signal=...) -> None: ...
    def acquire(self, scope_id: str, expiration_time: float) -> None: ...
    def release(self, scope_id: str) -> None: ...

class FileTimerServer:
    """
    Server that works with ``FileTimerClient``. Clients are expected to be
    running on the same host as the process that is running this server.
    Each host in the job is expected to start its own timer server locally
    and each server instance manages timers for local workers (running on
    processes on the same host).

    Args:

        file_path: str, the path of a FIFO special file to be created.

        max_interval: float, max interval in seconds for each watchdog loop.

        daemon: bool, running the watchdog thread in daemon mode or not.
                      A daemon thread will not block a process to stop.
        log_event: Callable[[Dict[str, str]], None], an optional callback for
                logging the events in JSON format.
    """
    def __init__(self, file_path: str, max_interval: float = 10, daemon: bool = True, log_event: Callable[[str, FileTimerRequest | None], None] = None) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def run_once(self) -> None: ...
    def register_timers(self, timer_requests: List[FileTimerRequest]) -> None: ...
    def clear_timers(self, worker_pids: Set[int]) -> None: ...
    def get_expired_timers(self, deadline: float) -> Dict[int, List[FileTimerRequest]]: ...
