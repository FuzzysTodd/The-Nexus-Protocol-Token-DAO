import torch
from _typeshed import Incomplete
from dataclasses import dataclass
from torch.fx.experimental.proxy_tensor import fetch_tensor_proxy as fetch_tensor_proxy, get_innermost_proxy_mode as get_innermost_proxy_mode, get_proxy_slot as get_proxy_slot, set_proxy_slot as set_proxy_slot, track_tensor_tree as track_tensor_tree
from torch.utils._mode_utils import no_dispatch as no_dispatch
from torch.utils._pytree import tree_flatten as tree_flatten, tree_map as tree_map, tree_map_only as tree_map_only

@dataclass
class _CommResult:
    def __init__(self, _tensor, _work) -> None: ...

class CommTensor(torch.Tensor):
    """
    A Tensor subclass to wrap input tensors for collective communications. This
    Tensor subclass works for both eager and tracing mode.

    In eager mode, it will record whether the inplace collective communication
    has been launched using this Tensor and remember the corresponding work
    handle. If yes, it will expliclty call wait() in the ``__torch_dispatch__``
    function before subsequent operations consuming the value of the Tensor.

    In tracing mode, ``CommTensor`` inserts two node into the graph using the
    ``__torch_dispatch__`` function.
    1. The first node is inserted right after the
    communication, wrapping both the inplace output tensor and the returned
    work handle into a custom ``_CommResult`` type. We have to do this because
    ``ProxyTorchDispatchMode`` only handles ``torch.Tensor``, ``_ProxyTensor``,
    and ``torch.nn.Parameter`` objects and will treat the work handle
    as a constant and embed that into the graph. As a result, during execution,
    it will use the work handle created during tracing and will lead to wrong
    result. The solution in this test is to manually create a proxy on the
    return value of ``allreduce_`` which is ``([tensor], work)``, and wrap that
    to ``[(_CommResult(tensor, work)), work]``. In this way, subsequent nodes can
    directly consume ``_CommResult``.
    2. The second node is inserted right before any subsequent node reads from
    ``_CommResult``. It will call ``wait()`` on the stashed work handle to ensure
    that computation waits for communication.
    """
    @staticmethod
    def __new__(cls, tensor: torch.Tensor): ...
    __torch_function__: Incomplete
    @classmethod
    def __torch_dispatch__(cls, func, types, args=(), kwargs: Incomplete | None = None): ...
