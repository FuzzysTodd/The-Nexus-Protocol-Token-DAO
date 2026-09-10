import torch
from _typeshed import Incomplete
from typing import Any

__all__ = ['autocast', 'custom_fwd', 'custom_bwd']

class autocast(torch.amp.autocast_mode.autocast):
    '''
    See :class:`torch.autocast`.
    ``torch.cuda.amp.autocast(args...)`` is equivalent to ``torch.autocast("cuda", args...)``
    '''
    device: str
    fast_dtype: Incomplete
    def __init__(self, enabled: bool = True, dtype: torch.dtype = ..., cache_enabled: bool = True) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any): ...
    def __call__(self, func): ...

def custom_fwd(fwd: Incomplete | None = None, *, cast_inputs: Incomplete | None = None):
    """
    Helper decorator for ``forward`` methods of custom autograd functions (subclasses of
    :class:`torch.autograd.Function`).  See the :ref:`example page<amp-custom-examples>` for more detail.

    Args:
        cast_inputs (:class:`torch.dtype` or None, optional, default=None):  If not ``None``,
            when ``forward`` runs in an autocast-enabled region, casts incoming
            floating-point CUDA Tensors to the target dtype (non-floating-point Tensors are not affected),
            then executes ``forward`` with autocast disabled.
            If ``None``, ``forward``'s internal ops execute with the current autocast state.

    .. note::
        If the decorated ``forward`` is called outside an autocast-enabled region,
        :func:`custom_fwd<custom_fwd>` is a no-op and ``cast_inputs`` has no effect.
    """
def custom_bwd(bwd):
    """
    Helper decorator for backward methods of custom autograd functions (subclasses of
    :class:`torch.autograd.Function`).
    Ensures that ``backward`` executes with the same autocast state as ``forward``.
    See the :ref:`example page<amp-custom-examples>` for more detail.
    """
