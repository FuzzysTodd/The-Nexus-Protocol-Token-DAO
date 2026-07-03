import torch
from _typeshed import Incomplete
from enum import IntEnum

__all__ = ['is_built', 'cuFFTPlanCacheAttrContextProp', 'cuFFTPlanCache', 'cuFFTPlanCacheManager', 'cuBLASModule', 'preferred_linalg_library', 'cufft_plan_cache', 'matmul', 'SDPBackend', 'enable_flash_sdp', 'flash_sdp_enabled', 'enable_mem_efficient_sdp', 'mem_efficient_sdp_enabled', 'math_sdp_enabled', 'enable_math_sdp', 'sdp_kernel']

def is_built():
    """Returns whether PyTorch is built with CUDA support.  Note that this
    doesn't necessarily mean CUDA is available; just that if this PyTorch
    binary were run a machine with working CUDA drivers and devices, we
    would be able to use it."""

class cuFFTPlanCacheAttrContextProp:
    getter: Incomplete
    setter: Incomplete
    def __init__(self, getter, setter) -> None: ...
    def __get__(self, obj, objtype): ...
    def __set__(self, obj, val) -> None: ...

class cuFFTPlanCache:
    """
    Represents a specific plan cache for a specific `device_index`. The
    attributes `size` and `max_size`, and method `clear`, can fetch and/ or
    change properties of the C++ cuFFT plan cache.
    """
    device_index: Incomplete
    def __init__(self, device_index) -> None: ...
    size: Incomplete
    max_size: Incomplete
    def clear(self): ...

class cuFFTPlanCacheManager:
    """
    Represents all cuFFT plan caches. When indexed with a device object/index,
    this object returns the `cuFFTPlanCache` corresponding to that device.

    Finally, this object, when used directly as a `cuFFTPlanCache` object (e.g.,
    setting the `.max_size`) attribute, the current device's cuFFT plan cache is
    used.
    """
    caches: Incomplete
    def __init__(self) -> None: ...
    def __getitem__(self, device): ...
    def __getattr__(self, name): ...
    def __setattr__(self, name, value): ...

class cuBLASModule:
    def __getattr__(self, name): ...
    def __setattr__(self, name, value): ...

def preferred_linalg_library(backend: None | str | torch._C._LinalgBackend = None) -> torch._C._LinalgBackend:
    '''
    .. warning:: This flag is experimental and subject to change.

    When PyTorch runs a CUDA linear algebra operation it often uses the cuSOLVER or MAGMA libraries,
    and if both are available it decides which to use with a heuristic.
    This flag (a :class:`str`) allows overriding those heuristics.

    * If `"cusolver"` is set then cuSOLVER will be used wherever possible.
    * If `"magma"` is set then MAGMA will be used wherever possible.
    * If `"default"` (the default) is set then heuristics will be used to pick between
      cuSOLVER and MAGMA if both are available.
    * When no input is given, this function returns the currently preferred library.

    Note: When a library is preferred other libraries may still be used if the preferred library
    doesn\'t implement the operation(s) called.
    This flag may achieve better performance if PyTorch\'s heuristic library selection is incorrect
    for your application\'s inputs.

    Currently supported linalg operators:

    * :func:`torch.linalg.inv`
    * :func:`torch.linalg.inv_ex`
    * :func:`torch.linalg.cholesky`
    * :func:`torch.linalg.cholesky_ex`
    * :func:`torch.cholesky_solve`
    * :func:`torch.cholesky_inverse`
    * :func:`torch.linalg.lu_factor`
    * :func:`torch.linalg.lu`
    * :func:`torch.linalg.lu_solve`
    * :func:`torch.linalg.qr`
    * :func:`torch.linalg.eigh`
    * :func:`torch.linalg.eighvals`
    * :func:`torch.linalg.svd`
    * :func:`torch.linalg.svdvals`
    '''

class SDPBackend(IntEnum):
    """Enum class for the scaled dot product attention backends.

    .. warning:: This class is in beta and subject to change.

    This class needs to stay aligned with the enum defined in:
    pytorch/aten/src/ATen/native/transformers/sdp_utils_cpp.h
    """
    ERROR: int
    MATH: int
    FLASH_ATTENTION: int
    EFFICIENT_ATTENTION: int

def flash_sdp_enabled():
    """
    .. warning:: This flag is beta and subject to change.

    Returns whether flash scaled dot product attention is enabled or not.
    """
def enable_flash_sdp(enabled: bool):
    """
    .. warning:: This flag is beta and subject to change.

    Enables or disables flash scaled dot product attention.
    """
def mem_efficient_sdp_enabled():
    """
    .. warning:: This flag is beta and subject to change.

    Returns whether memory efficient scaled dot product attention is enabled or not.
    """
def enable_mem_efficient_sdp(enabled: bool):
    """
    .. warning:: This flag is beta and subject to change.

    Enables or disables memory efficient scaled dot product attention.
    """
def math_sdp_enabled():
    """
    .. warning:: This flag is beta and subject to change.

    Returns whether math scaled dot product attention is enabled or not.
    """
def enable_math_sdp(enabled: bool):
    """
    .. warning:: This flag is beta and subject to change.

    Enables or disables math scaled dot product attention.
    """
def sdp_kernel(enable_flash: bool = True, enable_math: bool = True, enable_mem_efficient: bool = True):
    """
    .. warning:: This flag is beta and subject to change.

    This context manager can be used to temporarily enable or disable any of the three backends for scaled dot product attention.
    Upon exiting the context manager, the previous state of the flags will be restored.
    """

cufft_plan_cache: Incomplete
matmul: Incomplete
