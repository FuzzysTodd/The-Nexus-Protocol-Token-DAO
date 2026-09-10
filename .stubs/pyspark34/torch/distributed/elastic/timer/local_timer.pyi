import multiprocessing as mp
from .api import RequestQueue, TimerClient, TimerRequest, TimerServer
from typing import Any, Dict, List, Set

__all__ = ['LocalTimerClient', 'MultiprocessingRequestQueue', 'LocalTimerServer']

class LocalTimerClient(TimerClient):
    """
    Client side of ``LocalTimerServer``. This client is meant to be used
    on the same host that the ``LocalTimerServer`` is running on and uses
    pid to uniquely identify a worker. This is particularly useful in situations
    where one spawns a subprocess (trainer) per GPU on a host with multiple
    GPU devices.
    """
    def __init__(self, mp_queue) -> None: ...
    def acquire(self, scope_id, expiration_time) -> None: ...
    def release(self, scope_id) -> None: ...

class MultiprocessingRequestQueue(RequestQueue):
    """
    A ``RequestQueue`` backed by python ``multiprocessing.Queue``
    """
    def __init__(self, mp_queue: mp.Queue) -> None: ...
    def size(self) -> int: ...
    def get(self, size, timeout: float) -> List[TimerRequest]: ...

class LocalTimerServer(TimerServer):
    """
    Server that works with ``LocalTimerClient``. Clients are expected to be
    subprocesses to the parent process that is running this server. Each host
    in the job is expected to start its own timer server locally and each
    server instance manages timers for local workers (running on processes
    on the same host).
    """
    def __init__(self, mp_queue: mp.Queue, max_interval: float = 60, daemon: bool = True) -> None: ...
    def register_timers(self, timer_requests: List[TimerRequest]) -> None: ...
    def clear_timers(self, worker_ids: Set[int]) -> None: ...
    def get_expired_timers(self, deadline: float) -> Dict[Any, List[TimerRequest]]: ...
