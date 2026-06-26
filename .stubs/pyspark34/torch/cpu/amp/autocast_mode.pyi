import torch
from _typeshed import Incomplete
from typing import Any

__all__ = ['autocast']

class autocast(torch.amp.autocast_mode.autocast):
    '''
    See :class:`torch.autocast`.
    ``torch.cpu.amp.autocast(args...)`` is equivalent to ``torch.autocast("cpu", args...)``
    '''
    device: str
    fast_dtype: Incomplete
    def __init__(self, enabled: bool = True, dtype: torch.dtype = ..., cache_enabled: bool = True) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any): ...
    def __call__(self, func): ...
