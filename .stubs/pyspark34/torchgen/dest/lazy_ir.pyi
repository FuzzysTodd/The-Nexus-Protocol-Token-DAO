from abc import ABC
from dataclasses import dataclass
from torchgen.api.lazy import LazyArgument as LazyArgument, LazyIrProperties as LazyIrProperties, LazyIrSchema as LazyIrSchema, getValueT as getValueT, isValueType as isValueType, tensorListValueT as tensorListValueT
from torchgen.api.translate import translate as translate
from torchgen.api.types import BaseCType as BaseCType, Binding as Binding, DispatcherSignature as DispatcherSignature, NativeSignature as NativeSignature, OptionalCType as OptionalCType, VectorCType as VectorCType, deviceT as deviceT, kernel_signature as kernel_signature
from torchgen.context import method_with_native_function as method_with_native_function
from torchgen.dest.lazy_ts_lowering import ts_lowering_body as ts_lowering_body
from torchgen.model import Argument as Argument, BackendIndex as BackendIndex, BackendMetadata as BackendMetadata, BaseTy as BaseTy, BaseType as BaseType, FunctionSchema as FunctionSchema, ListType as ListType, NativeFunction as NativeFunction, NativeFunctionsGroup as NativeFunctionsGroup
from typing import Any, Dict, List, Tuple

def node_ctor_arg_rvalue_string(arg: LazyArgument) -> str:
    """
    Given a LazyArgument,
    generate a c++ string for materializing an rvalue of that arg for passing into
    a lazy Node constructor.
    """
def node_ctor_inputs(schema: LazyIrSchema) -> str:
    """
    Produce a formatted string with the arguments as passed into the constructor of a node class.
    """
def gen_fallback_code(schema: LazyIrSchema, sig: DispatcherSignature | NativeSignature, overload_name: str) -> str:
    """
    Generate code that falls back to eager conditioned on a predicate
    """
def aten_symbol(schema: LazyIrSchema) -> str: ...
def convert_to_meta_tensors(sig: DispatcherSignature) -> Tuple[str, List[Binding]]: ...

@dataclass(frozen=True)
class GenLazyIR(ABC):
    backend_index: BackendIndex
    backend_name: str
    node_base: str
    use_lazy_shape: bool
    def __call__(self, f: NativeFunctionsGroup | NativeFunction) -> List[str]: ...
    def lowering_function(self, schema: LazyIrSchema) -> str: ...
    def create_function(self, schema: LazyIrSchema, node_ctor_args: str) -> str: ...
    def can_be_reused_function(self, schema: LazyIrSchema, node_ctor_args: str) -> str: ...
    def node_base_ctor_call(self, schema: LazyIrSchema) -> str: ...
    def gen(self, schema: LazyIrSchema) -> List[str]: ...
    def __init__(self, backend_index, backend_name, node_base, use_lazy_shape) -> None: ...

@dataclass(frozen=True)
class GenTSLazyIR(GenLazyIR):
    def lowering_function(self, schema: LazyIrSchema) -> str: ...
    def create_function(self, schema: LazyIrSchema, node_ctor_args: str) -> str: ...
    def can_be_reused_function(self, schema: LazyIrSchema, node_ctor_args: str) -> str: ...
    def __init__(self, backend_index, backend_name, node_base, use_lazy_shape) -> None: ...

@dataclass(frozen=True)
class GenLazyNativeFuncDefinition:
    class_method_name: str
    backend_index: BackendIndex
    tensor_class: str
    gen_forced_fallback_code: bool
    backend_namespace: str
    get_tensorlist: str
    get_tensor_or_wrap_number: str
    try_get_tensor: str
    metrics_counter: str
    create_tensor: str
    create_from_first_tensor: bool
    create_aten_from_ltc_tensor: str
    tuple_aten_from_ltc_tensors: str
    lazy_tensor_ptr: str
    get_device_fn: str
    def lazy_tensor_decls(self, func: NativeFunction, schema: LazyIrSchema) -> str: ...
    def force_eager_fallback(self, func: NativeFunction, schema: LazyIrSchema, metadata: BackendMetadata, sig: DispatcherSignature | NativeSignature) -> str: ...
    def metrics(self, func: NativeFunction, schema: LazyIrSchema) -> str: ...
    def get_device(self, func: NativeFunction, schema: LazyIrSchema) -> str: ...
    def shape_inference(self, func: NativeFunction, schema: LazyIrSchema) -> str: ...
    def build_ir_node(self, func: NativeFunction, schema: LazyIrSchema) -> str: ...
    def create_lazy_tensor(self, first_tensor_name: str | None = None) -> str: ...
    def return_aten_tensor(self, func: NativeFunction, schema: LazyIrSchema) -> str: ...
    def __call__(self, func: NativeFunction) -> List[str]: ...
    def __init__(self, class_method_name, backend_index, tensor_class, gen_forced_fallback_code, backend_namespace, get_tensorlist, get_tensor_or_wrap_number, try_get_tensor, metrics_counter, create_tensor, create_from_first_tensor, create_aten_from_ltc_tensor, tuple_aten_from_ltc_tensors, lazy_tensor_ptr, get_device_fn) -> None: ...

class ComputeShapeSignature:
    """
    Here we use the base name as the suffix of the signature to avoid generating for in-place variants.
    """
    def __init__(self, kernel_name: str, f: NativeFunction, *, symint: bool) -> None: ...
    @property
    def shape_decl(self) -> str: ...
    @property
    def shape_call(self) -> str: ...

@dataclass(frozen=True)
class GenLazyShapeInferenceDefinition:
    backend_index: BackendIndex
    tensor_class: str
    def __call__(self, f: NativeFunction) -> List[str]: ...
    def __init__(self, backend_index, tensor_class) -> None: ...

def generate_non_native_lazy_ir_nodes(non_native: List[Dict[str, Any]], gen_lazy_ir: GenLazyIR) -> List[str]:
    """Generate the non-native lazy IR node classes"""
