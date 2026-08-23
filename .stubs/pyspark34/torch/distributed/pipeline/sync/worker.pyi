import torch
from .microbatch import Batch
from .stream import AbstractStream
from _typeshed import Incomplete
from types import TracebackType
from typing import Callable, Generator, List, Tuple, Type

__all__ = ['Task', 'worker', 'create_workers', 'spawn_workers']

ExcInfo = Tuple[Type[BaseException], BaseException, TracebackType]

class Task:
    """A task represents how to compute a micro-batch on a partition.

    It consists of two parts: :meth:`compute` and :meth:`finalize`.
    :meth:`compute` should be executed in worker threads concurrently.
    :meth:`finalize` should be executed after when worker threads complete to
    execute :meth:`compute`.

    :meth:`compute` might be boosted by worker threads. Because it produces
    several CUDA API calls by user code. In PyTorch, parallel CUDA API calls
    are not serialized through GIL. So more than one CUDA API call can be
    produced at the same time.

    """
    stream: Incomplete
    def __init__(self, stream: AbstractStream, *, compute: Callable[[], Batch], finalize: Callable[[Batch], None] | None) -> None: ...
    def compute(self) -> Batch: ...
    def finalize(self, batch: Batch) -> None: ...

def worker(in_queue: InQueue, out_queue: OutQueue, device: torch.device) -> None:
    """The main loop of a worker thread."""
def create_workers(devices: List[torch.device]) -> Tuple[List[InQueue], List[OutQueue]]:
    """Spawns worker threads. A worker thread is bound to a device."""
def spawn_workers(devices: List[torch.device]) -> Generator[Tuple[List[InQueue], List[OutQueue]], None, None]: ...
