import torch.overrides
from _typeshed import Incomplete
from torch._prims.nvfuser_executor import NvfuserPrimOperatorSupport as NvfuserPrimOperatorSupport
from torch._prims_common import torch_function_passthrough as torch_function_passthrough
from torch.fx.experimental.proxy_tensor import get_isolated_graphmodule as get_isolated_graphmodule
from typing import Any, Callable, Dict, Sequence

def torch_to_refs_map():
    """
    Mapping of torch API functions to torch._refs functions.
    E.g. torch_to_refs_map()[torch.add] == torch._refs.add
    """
def all_prims():
    """
    Set of all prim functions, e.g., torch._prims.add in all_prims()
    """

class NvfuserPrimsMode(torch.overrides.TorchFunctionMode):
    '''
    Switches the interpretation of torch.ops.prims.* functions to
    use nvFuser\'s prims in torch.ops.nvprims.*

    >>> # xdoctest: +SKIP("undefined vars")
    >>> with NvfuserPrimsMode():
    ...     torch.ops.prims.add(x, y)  # calls torch.ops.nvprims.add(x, y)

    By default, this context manager will fall back on the torch.ops.prims* if the
    nvprim does not exist.
    It\'s possible to skip certain prims by passing their names to the skip_ops
    argument. skip_ops is expected to be a sequence of strings, e.g.,
    ["prims.add.default"] In order to check the expected name of a prim, one can
    use the `torch.overrides.resolve_name`.

    >>> # xdoctest: +SKIP("undefined vars")
    >>> with NvfuserPrimsMode(skips_ops=("prims.add.default")):
    ...     torch.ops.prims.add.default(x, y)  # does not call torch.ops.nvprims.add.default(x, y)
    '''
    skip_ops: Incomplete
    def __init__(self, *, skip_ops=()) -> None: ...
    def __torch_function__(self, orig_func: Callable, types: Sequence, args: Sequence[Any] = (), kwargs: Dict = None): ...

class TorchRefsMode(torch.overrides.TorchFunctionMode):
    """
    Switches the interpretation of torch.* functions and Tensor methods to
    use PrimTorch refs in torch._refs.  (Direct calls to _refs are unaffected.)

    >>> # xdoctest: +SKIP
    >>> with TorchRefsMode():
    ...     torch.add(x, y)  # calls torch._refs.add(x, y)

    By default, this context manager will fall back on the torch.* if the
    ref does not exist; set strict=True to error if this occurs.
    If the ref exists we still would like to fall back on the torch.* sometimes,
    this behavior can be customized by passing a function to should_fallback_fn.
    """
    strict: Incomplete
    should_fallback_fn: Incomplete
    prims_mode_cls: Incomplete
    def __init__(self, strict: bool = False, should_fallback_fn=..., prims_mode_cls=...) -> None: ...
    def __torch_function__(self, orig_func: Callable, types: Sequence, args: Sequence[Any] = (), kwargs: Dict = None): ...

class TorchRefsNvfuserCapabilityMode(TorchRefsMode):
    skip_ops: Incomplete
    def __init__(self, *, skip_ops=()) -> None: ...
    def __torch_function__(self, orig_func: Callable, types: Sequence, args: Sequence[Any] = (), kwargs: Dict = None): ...
