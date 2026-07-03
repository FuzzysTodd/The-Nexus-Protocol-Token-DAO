import dataclasses
import enum
import jax
from _typeshed import Incomplete
from jax._src import api_util as api_util, effects as effects, state as state, tree_util as tree_util, util as util
from jax._src.interpreters import mlir as mlir
from jax._src.pallas import indexing as indexing
from typing import Any, Callable

map: Incomplete
unsafe_map: Incomplete
zip: Incomplete
unsafe_zip: Incomplete
repeat_p: Incomplete

def repeat(x, repeats, axis): ...

trace_start_p: Incomplete
trace_stop_p: Incomplete

def trace(message: str, level: int = 10): ...

run_scoped_p: Incomplete

def run_scoped(f: Callable[..., None], *types, **kw_types) -> None: ...

class DeviceIdType(enum.Enum):
    MESH: str
    LOGICAL: str

semaphore_signal_p: Incomplete

def semaphore_signal(sem, inc: int | jax.Array = 1, *, device_id: int | jax.Array | None = None, device_id_type: DeviceIdType = ...): ...

semaphore_wait_p: Incomplete

def semaphore_wait(sem, dec: int | jax.Array = 1): ...

@dataclasses.dataclass
class DMAFuture:
    flat_args: Any
    tree: Any
    device_id_type: DeviceIdType | None
    def wait(self) -> None: ...
    def __init__(self, flat_args, tree, device_id_type) -> None: ...

dma_start_p: Incomplete

def dma_start(src_ref, src_indices, dst_ref, dst_indices, sem) -> DMAFuture: ...
def remote_dma_start(src_ref, src_indices, dst_ref, dst_indices, src_sem, dst_sem, device_id, device_id_type: DeviceIdType) -> tuple[DMAFuture, DMAFuture]: ...

dma_wait_p: Incomplete

def async_copy(src_ref, dst_ref, sem):
    """Issues a DMA copying from src_ref to dst_ref."""
def async_remote_copy(src_ref, dst_ref, send_sem, recv_sem, device_id, device_id_type: DeviceIdType = ...): ...

device_id_p: Incomplete
device_id: Incomplete
