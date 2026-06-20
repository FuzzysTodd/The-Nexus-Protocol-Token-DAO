from torch._prims.context import NvfuserPrimsMode as NvfuserPrimsMode, TorchRefsMode as TorchRefsMode
from torch._prims.nvfuser_executor import nvfuser_execute as nvfuser_execute, nvfuser_execute_partitioned as nvfuser_execute_partitioned
from torch.fx import GraphModule as GraphModule
from torch.fx.experimental.proxy_tensor import make_fx as make_fx, wrapper_and_args_for_make_fx as wrapper_and_args_for_make_fx
from typing import Callable

def execute(gm: GraphModule, *args, executor: str = 'aten', executor_parameters: dict | None = None):
    """
    Prototype ATen executor.

    Just executes the context's graph.
    """
def make_traced(fn: Callable):
    """
    Returns a function that, when called, will
    trace its torch operations to prims and then
    execute those prims on the requested trace executor
    (possibly lowering them to that trace executor first).

    Only supports the torch operations defined in _torch_to_reference_map
    in context.py and operations with positional args. All args must
    be tensors.
    In the near future all these restrictions will be lifted.

    Example usage:

    def foo(a, b):
      return torch.add(a, b)

    traced_foo = make_traced(foo)

    a = torch.randn((1, 2, 3, 4, 5), device='cuda')
    b = torch.randn((1, 2, 3, 4, 5), device='cuda')
    result = traced_foo(a, b, executor='nvfuser')

    Executor may be either 'aten' or 'nvfuser'.
    """
