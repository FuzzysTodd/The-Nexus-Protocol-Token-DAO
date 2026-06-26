from _typeshed import Incomplete
from torch._ops import OpOverload, OpOverloadPacket
from typing import Callable, Dict, Sequence

__all__ = ['decomposition_table', 'pre_autograd_decomposition_table', 'meta_table', 'register_decomposition', 'get_decompositions', 'core_aten_decompositions']

decomposition_table: Incomplete
pre_autograd_decomposition_table: Incomplete
meta_table: Incomplete

def register_decomposition(aten_op, registry: Incomplete | None = None, *, type: str = 'post_autograd'):
    """
    A decorator to register a function as a decomposition to the Python
    decomposition table.  Use it like this::

        @register_decomposition(torch.ops.aten.clamp_min)
        def clamp_min(x):
            return torch.clamp(self, min=min)

    If you are writing a new decomposition, consider contributing it
    directly to PyTorch in torch._decomp.decompositions.

    This API is experimental; we are almost certainly going to extend
    the API when we make decompositions eligible for use in transforms (e.g.,
    autograd) and not just backend tracing, where we then need to know if a
    decomposition can be used to simulate a transform.

    By default, we also will register it to the Meta key of dispatcher,
    and replace the c++ Meta implementation if there is already one.
    """
def get_decompositions(aten_ops: Sequence[OpOverload | OpOverloadPacket], type: str = 'post_autograd') -> Dict[OpOverload, Callable]:
    """
    Retrieve a dictionary of decompositions corresponding to the list of
    operator overloads and overload packets passed as input.  Overload
    packets will include all decomposed overloads in the packet.  If there is
    no decomposition for a requested operator, it is silently ignored.

    This API is experimental; we are almost certainly going to give an alternate,
    more recommended formulation, where a user provides the set of operators
    they know how to implement, and we provide decompositions for everything
    not in this set.
    """
def core_aten_decompositions() -> Dict[OpOverload, Callable]: ...
