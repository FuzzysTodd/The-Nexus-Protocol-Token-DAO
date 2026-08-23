from .memory import *
from .random import *
import torch
import torch._C
from . import amp as amp, jiterator as jiterator, nvtx as nvtx, profiler as profiler, sparse as sparse
from .graphs import CUDAGraph as CUDAGraph, graph as graph, graph_pool_handle as graph_pool_handle, is_current_stream_capturing as is_current_stream_capturing, make_graphed_callables as make_graphed_callables
from .streams import Event as Event, ExternalStream as ExternalStream, Stream as Stream
from _typeshed import Incomplete
from torch.storage import _LegacyStorage
from torch.types import Device
from typing import Any, List, Tuple

__all__ = ['BFloat16Storage', 'BFloat16Tensor', 'BoolStorage', 'BoolTensor', 'ByteStorage', 'ByteTensor', 'CharStorage', 'CharTensor', 'ComplexDoubleStorage', 'ComplexFloatStorage', 'DoubleStorage', 'DoubleTensor', 'FloatStorage', 'FloatTensor', 'HalfStorage', 'HalfTensor', 'IntStorage', 'IntTensor', 'LongStorage', 'LongTensor', 'ShortStorage', 'ShortTensor', 'CUDAGraph', 'CudaError', 'DeferredCudaCallError', 'Event', 'ExternalStream', 'OutOfMemoryError', 'Stream', 'StreamContext', 'amp', 'caching_allocator_alloc', 'caching_allocator_delete', 'can_device_access_peer', 'check_error', 'cudaStatus', 'cudart', 'current_blas_handle', 'current_device', 'current_stream', 'default_generators', 'default_stream', 'device', 'device_count', 'device_of', 'empty_cache', 'get_allocator_backend', 'CUDAPluggableAllocator', 'change_current_allocator', 'get_arch_list', 'get_device_capability', 'get_device_name', 'get_device_properties', 'get_gencode_flags', 'get_rng_state', 'get_rng_state_all', 'get_sync_debug_mode', 'graph', 'graph_pool_handle', 'graphs', 'has_half', 'has_magma', 'init', 'initial_seed', 'ipc_collect', 'is_available', 'is_bf16_supported', 'is_current_stream_capturing', 'is_initialized', 'jiterator', 'list_gpu_processes', 'make_graphed_callables', 'manual_seed', 'manual_seed_all', 'max_memory_allocated', 'max_memory_cached', 'max_memory_reserved', 'mem_get_info', 'memory', 'memory_allocated', 'memory_cached', 'memory_reserved', 'memory_snapshot', 'memory_stats', 'memory_stats_as_nested_dict', 'memory_summary', 'memory_usage', 'nccl', 'nvtx', 'profiler', 'random', 'reset_accumulated_memory_stats', 'reset_max_memory_allocated', 'reset_max_memory_cached', 'reset_peak_memory_stats', 'seed', 'seed_all', 'set_device', 'set_per_process_memory_fraction', 'set_rng_state', 'set_rng_state_all', 'set_stream', 'set_sync_debug_mode', 'sparse', 'stream', 'streams', 'synchronize', 'utilization']

class _LazySeedTracker:
    manual_seed_all_cb: Incomplete
    manual_seed_cb: Incomplete
    call_order: Incomplete
    def __init__(self) -> None: ...
    def queue_seed_all(self, cb, traceback) -> None: ...
    def queue_seed(self, cb, traceback) -> None: ...
    def get_calls(self) -> List: ...

has_magma: bool
has_half: bool
default_generators: Tuple[torch._C.Generator]

def is_available() -> bool:
    """Returns a bool indicating if CUDA is currently available."""
def is_bf16_supported():
    """Returns a bool indicating if the current CUDA/ROCm device supports dtype bfloat16"""
def is_initialized():
    """Returns whether PyTorch's CUDA state has been initialized."""

class DeferredCudaCallError(Exception): ...

OutOfMemoryError: Incomplete

def init() -> None:
    """Initialize PyTorch's CUDA state.  You may need to call
    this explicitly if you are interacting with PyTorch via
    its C API, as Python bindings for CUDA functionality will not
    be available until this initialization takes place.  Ordinary users
    should not need this, as all of PyTorch's CUDA methods
    automatically initialize CUDA state on-demand.

    Does nothing if the CUDA state is already initialized.
    """
def cudart(): ...

class cudaStatus:
    SUCCESS: int
    ERROR_NOT_READY: int

class CudaError(RuntimeError):
    def __init__(self, code: int) -> None: ...

def check_error(res: int) -> None: ...

class _DeviceGuard:
    idx: Incomplete
    prev_idx: int
    def __init__(self, index: int) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, type: Any, value: Any, traceback: Any): ...

class device:
    """Context-manager that changes the selected device.

    Args:
        device (torch.device or int): device index to select. It's a no-op if
            this argument is a negative integer or ``None``.
    """
    idx: Incomplete
    prev_idx: int
    def __init__(self, device: Any) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, type: Any, value: Any, traceback: Any): ...

class device_of(device):
    """Context-manager that changes the current device to that of given object.

    You can use both tensors and storages as arguments. If a given object is
    not allocated on a GPU, this is a no-op.

    Args:
        obj (Tensor or Storage): object allocated on the selected device.
    """
    def __init__(self, obj) -> None: ...

def set_device(device: _device_t) -> None:
    """Sets the current device.

    Usage of this function is discouraged in favor of :any:`device`. In most
    cases it's better to use ``CUDA_VISIBLE_DEVICES`` environmental variable.

    Args:
        device (torch.device or int): selected device. This function is a no-op
            if this argument is negative.
    """
def get_device_name(device: _device_t | None = None) -> str:
    """Gets the name of a device.

    Args:
        device (torch.device or int, optional): device for which to return the
            name. This function is a no-op if this argument is a negative
            integer. It uses the current device, given by :func:`~torch.cuda.current_device`,
            if :attr:`device` is ``None`` (default).

    Returns:
        str: the name of the device
    """
def get_device_capability(device: _device_t | None = None) -> Tuple[int, int]:
    """Gets the cuda capability of a device.

    Args:
        device (torch.device or int, optional): device for which to return the
            device capability. This function is a no-op if this argument is
            a negative integer. It uses the current device, given by
            :func:`~torch.cuda.current_device`, if :attr:`device` is ``None``
            (default).

    Returns:
        tuple(int, int): the major and minor cuda capability of the device
    """
def get_device_properties(device: _device_t) -> _CudaDeviceProperties:
    """Gets the properties of a device.

    Args:
        device (torch.device or int or str): device for which to return the
            properties of the device.

    Returns:
        _CudaDeviceProperties: the properties of the device
    """
def can_device_access_peer(device: _device_t, peer_device: _device_t) -> bool:
    """Checks if peer access between two devices is possible.
    """

class StreamContext:
    """Context-manager that selects a given stream.

    All CUDA kernels queued within its context will be enqueued on a selected
    stream.

    Args:
        Stream (Stream): selected stream. This manager is a no-op if it's
            ``None``.
    .. note:: Streams are per-device.
    """
    cur_stream: torch.cuda.Stream | None
    stream: Incomplete
    idx: Incomplete
    src_prev_stream: Incomplete
    dst_prev_stream: Incomplete
    def __init__(self, stream: torch.cuda.Stream | None) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, type: Any, value: Any, traceback: Any): ...

def stream(stream: torch.cuda.Stream | None) -> StreamContext:
    """Wrapper around the Context-manager StreamContext that
    selects a given stream.

    Arguments:
        stream (Stream): selected stream. This manager is a no-op if it's
            ``None``.
    ..Note:: In eager mode stream is of type Stream class while in JIT it is
    an object of the custom class ``torch.classes.cuda.Stream``.
    """
def set_stream(stream: Stream):
    """Sets the current stream.This is a wrapper API to set the stream.
        Usage of this function is discouraged in favor of the ``stream``
        context manager.

    Args:
        stream (Stream): selected stream. This function is a no-op
            if this argument is ``None``.
    """
def device_count() -> int:
    """Returns the number of GPUs available."""
def get_arch_list() -> List[str]:
    """Returns list CUDA architectures this library was compiled for."""
def get_gencode_flags() -> str:
    """Returns NVCC gencode flags this library was compiled with."""
def current_device() -> int:
    """Returns the index of a currently selected device."""
def synchronize(device: _device_t = None) -> None:
    """Waits for all kernels in all streams on a CUDA device to complete.

    Args:
        device (torch.device or int, optional): device for which to synchronize.
            It uses the current device, given by :func:`~torch.cuda.current_device`,
            if :attr:`device` is ``None`` (default).
    """
def ipc_collect():
    """Force collects GPU memory after it has been released by CUDA IPC.

    .. note::
        Checks if any sent CUDA tensors could be cleaned from the memory. Force
        closes shared memory file used for reference counting if there is no
        active counters. Useful when the producer process stopped actively sending
        tensors and want to release unused memory.
    """
def current_stream(device: _device_t | None = None) -> Stream:
    """Returns the currently selected :class:`Stream` for a given device.

    Args:
        device (torch.device or int, optional): selected device. Returns
            the currently selected :class:`Stream` for the current device, given
            by :func:`~torch.cuda.current_device`, if :attr:`device` is ``None``
            (default).
    """
def default_stream(device: _device_t | None = None) -> Stream:
    """Returns the default :class:`Stream` for a given device.

    Args:
        device (torch.device or int, optional): selected device. Returns
            the default :class:`Stream` for the current device, given by
            :func:`~torch.cuda.current_device`, if :attr:`device` is ``None``
            (default).
    """
def current_blas_handle():
    """Returns cublasHandle_t pointer to current cuBLAS handle"""
def set_sync_debug_mode(debug_mode: int | str) -> None:
    '''Sets the debug mode for cuda synchronizing operations.

    Args:
        debug_mode(str or int): if "default" or 0, don\'t error or warn on synchronizing operations,
            if "warn" or 1, warn on synchronizing operations, if "error" or 2, error out synchronizing operations.

    Warning:
        This is an experimental feature, and not all synchronizing operations will trigger warning or error. In
        particular, operations in torch.distributed and torch.sparse namespaces are not covered yet.
    '''
def get_sync_debug_mode() -> int:
    """Returns current value of debug mode for cuda synchronizing operations."""
def memory_usage(device: Device | int | None = None) -> int:
    """Returns the percent of time over the past sample period during which global (device)
    memory was being read or written. as given by `nvidia-smi`.

    Args:
        device (torch.device or int, optional): selected device. Returns
            statistic for the current device, given by :func:`~torch.cuda.current_device`,
            if :attr:`device` is ``None`` (default).

    Warning: Each sample period may be between 1 second and 1/6 second,
    depending on the product being queried.
    """
def utilization(device: Device | int | None = None) -> int:
    """Returns the percent of time over the past sample period during which one or
    more kernels was executing on the GPU as given by `nvidia-smi`.

    Args:
        device (torch.device or int, optional): selected device. Returns
            statistic for the current device, given by :func:`~torch.cuda.current_device`,
            if :attr:`device` is ``None`` (default).

    Warning: Each sample period may be between 1 second and 1/6 second,
    depending on the product being queried.
    """

class _CudaBase:
    is_cuda: bool
    is_sparse: bool
    def type(self, *args, **kwargs): ...
    __new__: Incomplete

class _CudaLegacyStorage(_LegacyStorage):
    @classmethod
    def from_buffer(cls, *args, **kwargs) -> None: ...

class ByteStorage(_CudaLegacyStorage):
    def dtype(self): ...

class DoubleStorage(_CudaLegacyStorage):
    def dtype(self): ...

class FloatStorage(_CudaLegacyStorage):
    def dtype(self): ...

class HalfStorage(_CudaLegacyStorage):
    def dtype(self): ...

class LongStorage(_CudaLegacyStorage):
    def dtype(self): ...

class IntStorage(_CudaLegacyStorage):
    def dtype(self): ...

class ShortStorage(_CudaLegacyStorage):
    def dtype(self): ...

class CharStorage(_CudaLegacyStorage):
    def dtype(self): ...

class BoolStorage(_CudaLegacyStorage):
    def dtype(self): ...

class BFloat16Storage(_CudaLegacyStorage):
    def dtype(self): ...

class ComplexDoubleStorage(_CudaLegacyStorage):
    def dtype(self): ...

class ComplexFloatStorage(_CudaLegacyStorage):
    def dtype(self): ...

# Names in __all__ with no definition:
#   BFloat16Tensor
#   BoolTensor
#   ByteTensor
#   CUDAPluggableAllocator
#   CharTensor
#   DoubleTensor
#   FloatTensor
#   HalfTensor
#   IntTensor
#   LongTensor
#   ShortTensor
#   caching_allocator_alloc
#   caching_allocator_delete
#   change_current_allocator
#   empty_cache
#   get_allocator_backend
#   get_rng_state
#   get_rng_state_all
#   graphs
#   initial_seed
#   list_gpu_processes
#   manual_seed
#   manual_seed_all
#   max_memory_allocated
#   max_memory_cached
#   max_memory_reserved
#   mem_get_info
#   memory
#   memory_allocated
#   memory_cached
#   memory_reserved
#   memory_snapshot
#   memory_stats
#   memory_stats_as_nested_dict
#   memory_summary
#   nccl
#   random
#   reset_accumulated_memory_stats
#   reset_max_memory_allocated
#   reset_max_memory_cached
#   reset_peak_memory_stats
#   seed
#   seed_all
#   set_per_process_memory_fraction
#   set_rng_state
#   set_rng_state_all
#   streams
