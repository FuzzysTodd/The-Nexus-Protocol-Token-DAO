import enum
import torch
import traceback
from _typeshed import Incomplete
from dataclasses import dataclass
from torch.utils._python_dispatch import TorchDispatchMode as TorchDispatchMode
from torch.utils._pytree import tree_map as tree_map
from typing import Any, Dict, Iterator, List, Tuple, TypeVar

DEFAULT_STREAM_ID: int
TK = TypeVar('TK')
TVa = TypeVar('TVa')
TVb = TypeVar('TVb')
DataPtr = int
StreamId = int
EventId = int
SeqNum = int
logger: Incomplete

class AccessType(enum.Enum):
    READ: Incomplete
    WRITE: Incomplete

@dataclass
class Access:
    """Stores information about a single access to a tensor by a kernel.

    Args:
        type: either AccessType.READ or AccessType.Write.
        seq_num: the sequential number of the kernel performing the access.
        stream: the stream id of the stream executing the kernel.
        operator: the schema of the launched kernel, which lists the
            arguments and return type.
        aliases: the arguments in the schema this access corresponds to.
        is_output: Whether the tensor was an output of the kernel.
        stack_trace: the stack summary object captured during access.
    """
    type: AccessType
    seq_num: SeqNum
    stream: StreamId
    operator: str
    aliases: List[str]
    is_output: bool
    stack_trace: traceback.StackSummary
    def __init__(self, type, seq_num, stream, operator, aliases, is_output, stack_trace) -> None: ...

class SynchronizationError(Exception):
    """Base class for errors detected by CUDA Sanitizer."""

class UnsynchronizedAccessError(SynchronizationError):
    """Stores information about two unsynchronized accesses to one data pointer."""
    data_ptr: Incomplete
    allocation_stack_trace: Incomplete
    current_access: Incomplete
    previous_access: Incomplete
    def __init__(self, data_ptr: DataPtr, allocation_stack_trace: traceback.StackSummary | None, current_access: Access, previous_access: Access) -> None: ...

class CUDASanitizerErrors(Exception):
    """Wrapper class for errors reported by CUDA Sanitizer."""
    errors: Incomplete
    def __init__(self, errors: List[SynchronizationError]) -> None: ...

def format_log_message(message: str) -> str: ...

@dataclass
class TensorInfo:
    """Stores information about a single tensor and recent accesses to it.

    Args:
        allocation_stack_trace: the stack summary object captured during tensor
            allocation. Can be ``None`` if the allocation wasn't caught by CSAN.
        reads: list of read accesses to the tensor that were performed since
            the last write.
        write: the last write access to the tensor.
    """
    allocation_stack_trace: traceback.StackSummary | None
    reads: List[Access] = ...
    write: Access | None = ...
    def __init__(self, allocation_stack_trace, reads, write) -> None: ...

class _TensorsAccessed:
    accesses: Incomplete
    def __init__(self) -> None: ...
    def ensure_tensor_exists(self, data_ptr: DataPtr) -> None: ...
    def ensure_tensor_does_not_exist(self, data_ptr: DataPtr) -> None: ...
    def create_tensor(self, data_ptr: DataPtr, stack_trace: traceback.StackSummary | None) -> None: ...
    def delete_tensor(self, data_ptr: DataPtr) -> None: ...
    def were_there_reads_since_last_write(self, data_ptr: DataPtr) -> bool: ...
    def get_allocation_stack_trace(self, data_ptr: DataPtr) -> traceback.StackSummary | None: ...
    def get_write(self, data_ptr: DataPtr) -> Access | None: ...
    def get_reads(self, data_ptr: DataPtr) -> List[Access]: ...
    def add_read(self, data_ptr: DataPtr, access: Access) -> None: ...
    def set_write(self, data_ptr: DataPtr, access: Access) -> None: ...

class StreamSynchronizations:
    current_sync_states: Incomplete
    recorded_sync_states: Incomplete
    host_sync_state: Incomplete
    def __init__(self) -> None: ...
    def create_stream(self, stream: StreamId) -> None: ...
    def create_event(self, event: EventId) -> None: ...
    def delete_event(self, event: EventId) -> None: ...
    def update_seq_num(self, stream: StreamId, seq_num: SeqNum) -> None: ...
    def record_state(self, event: EventId, stream: StreamId) -> None: ...
    def stream_wait_for_event(self, stream: StreamId, event: EventId) -> None: ...
    def all_streams_wait_for_event(self, event: EventId) -> None: ...
    def all_streams_wait_for_stream(self, stream: StreamId) -> None: ...
    def sync_all_streams(self) -> None: ...
    def is_ordered_after(self, current_stream: StreamId, seq_num: SeqNum, other_stream: StreamId) -> bool: ...

class EventHandler:
    """Analyzes CSAN trace for synchronization errors.

    Stores information on each stream's synchronizations with other streams as well
    as tensor accesses to determine whether a given kernel launch might cause a
    data race.
    """
    tensors_accessed: Incomplete
    syncs: Incomplete
    seq_num: int
    def __init__(self) -> None: ...

def zip_by_key(a: Dict[TK, TVa], b: Dict[TK, TVb]) -> Iterator[Tuple[TK, TVa, TVb]]: ...
def zip_arguments(schema: torch.FunctionSchema, args: Tuple[Any, ...], kwargs: Dict[str, Any]) -> Iterator[Tuple[torch.Argument, Any]]: ...

class ArgumentHandler:
    dataptrs_read: Incomplete
    dataptrs_written: Incomplete
    tensor_aliases: Incomplete
    outputs: Incomplete
    def __init__(self) -> None: ...
    def parse_inputs(self, schema: torch.FunctionSchema, args: Tuple[Any, ...], kwargs: Dict[str, Any]) -> None: ...
    def parse_outputs(self, outputs: Any) -> None: ...

class CUDASanitizerDispatchMode(TorchDispatchMode):
    event_handler: Incomplete
    def __init__(self) -> None: ...
    def __torch_dispatch__(self, func, types, args=(), kwargs: Incomplete | None = None): ...

class CUDASanitizer:
    """Manages the lifetime of a CUDASanitizer dispatch mode object.

    The CUDASanitizer class wraps the entering/exiting functions of the dispatch mode
    context manager in the enable function/destructor, respectively. This is to
    explicitly set the lifetime of the dispatch mode object to that of the application.
    This approach was deemed more elegant than using the atexit module.
    """
    dispatch: Incomplete
    enabled: bool
    def __init__(self) -> None: ...
    def enable(self) -> None: ...
    def __del__(self) -> None: ...

def enable_cuda_sanitizer() -> None:
    """Enables CUDA Sanitizer.

    The sanitizer will begin to analyze low-level CUDA calls invoked by torch functions
    for synchronization errors. All data races found will be printed to the standard
    error output along with stack traces of suspected causes. For best results, the
    sanitizer should be enabled at the very beginning of the program.
    """

cuda_sanitizer: Incomplete
