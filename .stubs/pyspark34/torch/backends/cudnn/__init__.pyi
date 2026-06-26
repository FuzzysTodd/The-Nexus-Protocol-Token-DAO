from _typeshed import Incomplete
from collections.abc import Generator
from torch.backends import ContextProp as ContextProp, PropModule as PropModule

def version():
    """Returns the version of cuDNN"""

CUDNN_TENSOR_DTYPES: Incomplete

def is_available():
    """Returns a bool indicating if CUDNN is currently available."""
def is_acceptable(tensor): ...
def set_flags(_enabled: Incomplete | None = None, _benchmark: Incomplete | None = None, _benchmark_limit: Incomplete | None = None, _deterministic: Incomplete | None = None, _allow_tf32: Incomplete | None = None): ...
def flags(enabled: bool = False, benchmark: bool = False, benchmark_limit: int = 10, deterministic: bool = False, allow_tf32: bool = True) -> Generator[None, None, None]: ...

class CudnnModule(PropModule):
    def __init__(self, m, name) -> None: ...
    enabled: Incomplete
    deterministic: Incomplete
    benchmark: Incomplete
    benchmark_limit: Incomplete
    allow_tf32: Incomplete

enabled: bool
deterministic: bool
benchmark: bool
allow_tf32: bool
benchmark_limit: int
