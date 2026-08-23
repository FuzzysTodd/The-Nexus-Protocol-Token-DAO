import abc
from _typeshed import Incomplete
from torch import optim as optim
from torch.distributed.optim import DistributedOptimizer as DistributedOptimizer
from torch.testing._internal.dist_utils import dist_init as dist_init
from torch.testing._internal.distributed.rpc.rpc_agent_test_fixture import RpcAgentTestFixture as RpcAgentTestFixture

class MyModule:
    lock: Incomplete
    w: Incomplete
    def __init__(self, requires_grad: bool = True) -> None: ...
    def forward(self, t1): ...
    def get_w(self): ...

class FailingOptimizer(optim.Optimizer):
    def __init__(self, params) -> None: ...
    def step(self, closure: Incomplete | None = None) -> None: ...

class OptimizerFailingOnConstructor(optim.Optimizer):
    def __init__(self, params) -> None: ...
    def step(self, closure: Incomplete | None = None) -> None: ...

def remote_method(method, obj_rref, *args, **kwargs):
    """
    Call rpc.remote on a method in a remote object.

    Args:
        method: the method (for example, Class.method)
        obj_rref (RRef): remote reference to the object
        args: positional arguments to pass to the method
        kwargs: keyword arguments to pass to the method

    Returns a RRef to the remote method call result.
    """
def rpc_async_method(method, obj_rref, *args, **kwargs):
    """
    Call rpc.rpc_async on a method in a remote object.

    Args:
        method: the method (for example, Class.method)
        obj_rref (RRef): remote reference to the object
        args: positional arguments to pass to the method
        kwargs: keyword arguments to pass to the method

    Returns a Future to the method call result.
    """

class DistOptimizerTest(RpcAgentTestFixture, metaclass=abc.ABCMeta):
    def test_dist_optim_exception(self) -> None: ...
    def test_dist_optim_exception_on_constructor(self) -> None: ...
    def test_dist_optim(self) -> None: ...
    def test_dist_optim_none_grads(self) -> None: ...
