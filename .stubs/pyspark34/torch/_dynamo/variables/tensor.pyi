import torch
import torch.fx
from .. import config as config, variables as variables
from ..exc import unimplemented as unimplemented
from ..guards import GuardBuilder as GuardBuilder
from ..source import AttrSource as AttrSource
from ..utils import HAS_NUMPY as HAS_NUMPY, fqn as fqn, get_fake_value as get_fake_value, get_real_value as get_real_value, np as np, product as product, proxy_args_kwargs as proxy_args_kwargs, tensortype_to_dtype as tensortype_to_dtype
from .base import VariableTracker as VariableTracker
from .constant import ConstantVariable as ConstantVariable
from .lists import ShapeVariable as ShapeVariable, SizeVariable as SizeVariable
from _typeshed import Incomplete
from torch.fx.experimental.symbolic_shapes import guard_scalar as guard_scalar
from typing import Dict, List

supported_tensor_comparison_ops: Incomplete
supported_const_comparison_ops: Incomplete

class TensorVariable(VariableTracker):
    """A torch.Tensor input or an intermediate value in the FX graph"""
    def get_real_value(self):
        """
        Get the actual value represented by this variable if computation is run
        using the user-provided inputs.
        NOTE: this runs actual tensor computation and may be
        slow and memory-intensive.
        """
    proxy: Incomplete
    dtype: Incomplete
    device: Incomplete
    layout: Incomplete
    ndim: Incomplete
    size: Incomplete
    stride: Incomplete
    requires_grad: Incomplete
    is_quantized: Incomplete
    is_contiguous: Incomplete
    is_sparse: Incomplete
    class_type: Incomplete
    specialized_value: Incomplete
    def __init__(self, proxy: torch.fx.Proxy, dtype: Incomplete | None = None, device: Incomplete | None = None, layout: Incomplete | None = None, ndim: Incomplete | None = None, size: Incomplete | None = None, stride: Incomplete | None = None, requires_grad: Incomplete | None = None, is_quantized: Incomplete | None = None, is_contiguous: Incomplete | None = None, is_sparse: Incomplete | None = None, class_type=..., specialized_value: Incomplete | None = None, **kwargs) -> None: ...
    def as_proxy(self): ...
    def python_type(self): ...
    def call_isinstance(self, tensor_type): ...
    @staticmethod
    def specialize(value: torch.Tensor): ...
    def var_getattr(self, tx, name): ...
    def has_unpack_var_sequence(self, tx): ...
    def unpack_var_sequence(self, tx, idxes: Incomplete | None = None): ...
    def call_method(self, tx, name, args: List[VariableTracker], kwargs: Dict[str, VariableTracker]) -> VariableTracker: ...

class SymNodeVariable(VariableTracker):
    """
    Represents a symbolic size, e.g., as returned by tensor.size(0)
    """
    @classmethod
    def create(cls, tx, proxy, sym_num, **options): ...
    proxy: Incomplete
    sym_num: Incomplete
    def __init__(self, proxy, sym_num, **kwargs) -> None: ...
    def python_type(self): ...
    def unpack_var_sequence(self, tx) -> None: ...
    def as_proxy(self): ...
    def evaluate_expr(self, output_graph): ...
    def call_method(self, tx, name, args: List[VariableTracker], kwargs: Dict[str, VariableTracker]) -> VariableTracker: ...

class TensorWithTFOverrideVariable(VariableTracker):
    """
    Represents a tensor subclass instance with a __torch_function__ override.
    """
    tensor_variable: Incomplete
    orig_tensor_variable_source: Incomplete
    subclass_torch_function__func: Incomplete
    subclass_type: Incomplete
    def __init__(self, tensor_variable, orig_tensor_variable_source, subclass_torch_function__func, subclass_type, **kwargs) -> None: ...
    def call_method(self, tx, name, args: List[VariableTracker], kwargs: Dict[str, VariableTracker]) -> VariableTracker: ...
    @staticmethod
    def inline_torch_function_unwrapped(tx, original_func_var, tensor_with_tf_override_source, tf_func, subclass_type, options, args, kwargs):
        """
        This function inlines the `__torch_function__` override for `original_func_var`.
        For example, if the user code is

           x1 = torch.sigmoid(x0)

        And `x0` has an override, then:
        * `original_func_var` will be a `VariableTracker` object wrapping `torch.sigmoid`
        * `tensor_with_tf_override_source` will be the `Source` object from
          the original tensor override instance in the beginning of the program
        * `tf_func` will be the custom `__torch_function__` function
        * `subclass_type` will be `type(x0)`

        The caller is expected to properly massage args and kwargs before
        passing them into this function.

        The caller is responsible for wrapping the return value, if needed.
        """

class UnspecializedPythonVariable(TensorVariable):
    """
    This is a 1-element tensor represents unspecialized python float/int.
    """
    raw_value: Incomplete
    need_unwrap: Incomplete
    def __init__(self, proxy: torch.fx.Proxy, **kwargs) -> None: ...
    @classmethod
    def from_tensor_variable(cls, tensor_variable, raw_value, need_unwrap: bool = True): ...
    def as_specialized(self, tx): ...

class FakeItemVariable(TensorVariable):
    """An unspecialized python variable which prevents access to the underlying raw value.
    This is needed if item is called on a FakeTensor."""
    need_unwrap: Incomplete
    def __init__(self, proxy: torch.fx.Proxy, **kwargs) -> None: ...
    @classmethod
    def from_tensor_variable(cls, tensor_variable): ...
