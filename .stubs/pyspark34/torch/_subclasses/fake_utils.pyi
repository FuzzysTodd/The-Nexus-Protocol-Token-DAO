from _typeshed import Incomplete
from torch._ops import OpOverload as OpOverload
from torch._subclasses.fake_tensor import FakeTensorMode as FakeTensorMode, UnsupportedFakeTensorException as UnsupportedFakeTensorException, tree_flatten_only as tree_flatten_only
from torch.utils._python_dispatch import TorchDispatchMode as TorchDispatchMode
from torch.utils._pytree import tree_flatten as tree_flatten
from typing import Callable

aten: Incomplete

def outputs_alias_inputs(outputs, inputs): ...
def outputs_are_inputs(outputs, inputs): ...
def output_alias_each_other(outputs): ...

class CrossRefFakeMode(TorchDispatchMode):
    ignore_op_fn: Incomplete
    check_strides: Incomplete
    check_aliasing: Incomplete
    def __init__(self, ignore_op_fn: Callable[[OpOverload], bool] | None = None, *, check_strides: bool = True, check_aliasing: bool = True) -> None: ...
    def __torch_dispatch__(self, func, types, args=(), kwargs: Incomplete | None = None): ...
