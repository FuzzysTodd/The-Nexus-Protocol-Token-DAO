from dataclasses import dataclass
from torchgen.api import cpp as cpp
from torchgen.api.types import BaseCType as BaseCType, Binding as Binding, NamedCType as NamedCType, tensorListT as tensorListT
from torchgen.model import FunctionSchema as FunctionSchema, NativeFunction as NativeFunction, NativeFunctionsViewGroup as NativeFunctionsViewGroup, SchemaKind as SchemaKind, Type as Type
from torchgen.utils import IDENT_REGEX as IDENT_REGEX
from typing import Dict, List, Sequence, Set, Tuple

@dataclass(frozen=True)
class SavedAttribute:
    nctype: NamedCType
    expr: str
    def __init__(self, nctype, expr) -> None: ...

@dataclass(frozen=True)
class Derivative:
    formula: str
    original_formula: str
    var_names: Tuple[str, ...]
    saved_inputs: Tuple[SavedAttribute, ...]
    saved_outputs: Tuple[SavedAttribute, ...]
    named_gradients: Set[str]
    def __init__(self, formula, original_formula, var_names, saved_inputs, saved_outputs, named_gradients) -> None: ...

@dataclass(frozen=True)
class ForwardDerivative:
    formula: str
    var_names: Tuple[str, ...]
    var_types: Tuple[Type, ...]
    required_inputs_fw_grad: Tuple[str, ...] | None
    required_inputs_primal: Tuple[str, ...] | None
    required_original_self_value: bool
    is_reusing_outplace_formula: bool
    def __init__(self, formula, var_names, var_types, required_inputs_fw_grad, required_inputs_primal, required_original_self_value, is_reusing_outplace_formula) -> None: ...

@dataclass(frozen=True)
class DifferentiabilityInfo:
    name: str
    func: NativeFunction
    op: str | None
    derivatives: Sequence[Derivative]
    forward_derivatives: Sequence[ForwardDerivative]
    all_saved_inputs: Sequence[SavedAttribute]
    all_saved_outputs: Sequence[SavedAttribute]
    available_named_gradients: Sequence[str]
    used_named_gradients: Set[str]
    args_with_derivatives: Sequence[Binding]
    non_differentiable_arg_names: Sequence[str]
    output_differentiability: List[bool] | None
    output_differentiability_conditions: List[str] | None
    @property
    def has_derivatives(self) -> bool: ...
    def create_view_copy_from_view_derivative(self, g: NativeFunctionsViewGroup) -> DifferentiabilityInfo | None: ...
    def __init__(self, name, func, op, derivatives, forward_derivatives, all_saved_inputs, all_saved_outputs, available_named_gradients, used_named_gradients, args_with_derivatives, non_differentiable_arg_names, output_differentiability, output_differentiability_conditions) -> None: ...

def uses_ident(info: DifferentiabilityInfo | None, ident: str) -> bool: ...
def uses_retain_variables(info: DifferentiabilityInfo | None) -> bool: ...
def uses_single_grad(info: DifferentiabilityInfo | None) -> bool: ...

@dataclass(frozen=True)
class DifferentiableInput:
    name: str
    type: Type
    cpp_type: str
    def __init__(self, name, type, cpp_type) -> None: ...

@dataclass(frozen=True)
class DifferentiableOutput:
    name: str
    type: Type
    cpp_type: str
    def __init__(self, name, type, cpp_type) -> None: ...

@dataclass(frozen=True)
class NativeFunctionWithDifferentiabilityInfo:
    func: NativeFunction
    info: Dict[str, DifferentiabilityInfo] | None
    fw_derivatives: Dict[str, Sequence[ForwardDerivative]] | None
    def __init__(self, func, info, fw_derivatives) -> None: ...

def dispatch_strategy(fn: NativeFunctionWithDifferentiabilityInfo) -> str:
    """How are we going to call the underlying implementation of a
    declaration?  There are two strategies:
        - use_derived: we want to call the implementation on CPUDoubleType
          (or a similar, derived Type instance).  Because these derived
          instances deal in Tensors, not Variables (it's a completely different
          object, so it doesn't dispatch back to VariableType), code on
          this dispatch path needs to wrap/unwrap tensors.  If the
          derived implementation takes and returns tensors, the
          implementation is usually differentiable (although we also use
          the derived dispatch path for non-differentiable functions
          that we still want to dispatch on the derived Type instance;
          e.g., size())
        - use_type: we want to call the implementation on Type, because
          it is implemented concretely, and the functions it invokes will
          get dispatched back to VariableType (which will ensure that they
          are differentiable.)
    """
def match_differentiability_info(native_functions: List[NativeFunction], differentiability_infos: Dict[FunctionSchema, Dict[str, DifferentiabilityInfo]]) -> List[NativeFunctionWithDifferentiabilityInfo]:
    '''Sets the "derivative" key on declarations to matching autograd function
    In-place functions will use the out-of-place derivative definition if there
    is no in-place specific derivative.
    '''
def is_differentiable(name: str, type: Type, info: DifferentiabilityInfo | None) -> bool: ...
def gen_differentiable_outputs(fn: NativeFunctionWithDifferentiabilityInfo, key: str = 'Default') -> List[DifferentiableOutput]: ...
