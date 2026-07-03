from _typeshed import Incomplete
from dataclasses import dataclass
from enum import Enum
from torchgen.utils import NamespaceHelper as NamespaceHelper, OrderedSet as OrderedSet, assert_never as assert_never
from typing import Dict, Iterator, List, Sequence, Set, Tuple

@dataclass(frozen=True)
class Location:
    file: str
    line: int
    def __init__(self, file, line) -> None: ...

class Variant(Enum):
    function: Incomplete
    method: Incomplete

DEFAULT_KERNEL_NAMESPACE: str
BACKEND_COMPONENTS: Incomplete
FUNCTIONALITY_KEYS: Incomplete
AUTOGRAD_KEYS: Incomplete
FRAGMENT_NAMESPACES: Incomplete

class DispatchKey(Enum):
    Undefined: int
    CatchAll = Undefined
    FPGA: Incomplete
    ORT: Incomplete
    Vulkan: Incomplete
    Metal: Incomplete
    MKLDNN: Incomplete
    OpenGL: Incomplete
    OpenCL: Incomplete
    IDEEP: Incomplete
    CustomRNGKeyId: Incomplete
    MkldnnCPU: Incomplete
    Sparse: Incomplete
    SparseCsrCPU: Incomplete
    SparseCsrCUDA: Incomplete
    Python: Incomplete
    FuncTorchDynamicLayerBackMode: Incomplete
    ZeroTensor: Incomplete
    BackendSelect: Incomplete
    Named: Incomplete
    AutogradOther: Incomplete
    AutogradFunctionality: Incomplete
    AutogradNestedTensor: Incomplete
    Tracer: Incomplete
    Autocast: Incomplete
    Batched: Incomplete
    VmapMode: Incomplete
    FuncTorchDynamicLayerFrontMode: Incomplete
    Functionalize: Incomplete
    TESTING_ONLY_GenericWrapper: Incomplete
    TESTING_ONLY_GenericMode: Incomplete
    ADInplaceOrView: Incomplete
    Autograd: Incomplete
    CompositeImplicitAutograd: Incomplete
    CompositeImplicitAutogradNestedTensor: Incomplete
    CompositeExplicitAutograd: Incomplete
    CompositeExplicitAutogradNonFunctional: Incomplete
    CPU: Incomplete
    CUDA: Incomplete
    HIP: Incomplete
    XLA: Incomplete
    MPS: Incomplete
    IPU: Incomplete
    XPU: Incomplete
    HPU: Incomplete
    VE: Incomplete
    Lazy: Incomplete
    Meta: Incomplete
    PrivateUse1: Incomplete
    PrivateUse2: Incomplete
    PrivateUse3: Incomplete
    QuantizedCPU: Incomplete
    QuantizedCUDA: Incomplete
    QuantizedHIP: Incomplete
    QuantizedXLA: Incomplete
    QuantizedMPS: Incomplete
    QuantizedIPU: Incomplete
    QuantizedXPU: Incomplete
    QuantizedHPU: Incomplete
    QuantizedVE: Incomplete
    QuantizedLazy: Incomplete
    QuantizedMeta: Incomplete
    QuantizedPrivateUse1: Incomplete
    QuantizedPrivateUse2: Incomplete
    QuantizedPrivateUse3: Incomplete
    SparseCPU: Incomplete
    SparseCUDA: Incomplete
    SparseHIP: Incomplete
    SparseXLA: Incomplete
    SparseMPS: Incomplete
    SparseIPU: Incomplete
    SparseXPU: Incomplete
    SparseHPU: Incomplete
    SparseVE: Incomplete
    SparseLazy: Incomplete
    SparseMeta: Incomplete
    SparsePrivateUse1: Incomplete
    SparsePrivateUse2: Incomplete
    SparsePrivateUse3: Incomplete
    NestedTensorCPU: Incomplete
    NestedTensorCUDA: Incomplete
    NestedTensorHIP: Incomplete
    NestedTensorXLA: Incomplete
    NestedTensorMPS: Incomplete
    NestedTensorIPU: Incomplete
    NestedTensorXPU: Incomplete
    NestedTensorHPU: Incomplete
    NestedTensorVE: Incomplete
    NestedTensorLazy: Incomplete
    NestedTensorMeta: Incomplete
    NestedTensorPrivateUse1: Incomplete
    NestedTensorPrivateUse2: Incomplete
    NestedTensorPrivateUse3: Incomplete
    AutogradCPU: Incomplete
    AutogradCUDA: Incomplete
    AutogradHIP: Incomplete
    AutogradXLA: Incomplete
    AutogradMPS: Incomplete
    AutogradIPU: Incomplete
    AutogradXPU: Incomplete
    AutogradHPU: Incomplete
    AutogradVE: Incomplete
    AutogradLazy: Incomplete
    AutogradMeta: Incomplete
    AutogradPrivateUse1: Incomplete
    AutogradPrivateUse2: Incomplete
    AutogradPrivateUse3: Incomplete
    def lower(self) -> str: ...
    @staticmethod
    def parse(value: str) -> DispatchKey: ...

def codegen_per_backend_entries() -> str: ...

r: Incomplete
STRUCTURED_DISPATCH_KEYS: Incomplete
UFUNC_DISPATCH_KEYS: Incomplete
dispatch_keys: Incomplete

def is_generic_dispatch_key(dk: DispatchKey) -> bool: ...
def is_cuda_dispatch_key(dk: DispatchKey) -> bool: ...
def is_structured_dispatch_key(dk: DispatchKey) -> bool: ...
def is_ufunc_dispatch_key(dk: DispatchKey) -> bool: ...

class ScalarType(Enum):
    Byte: Incomplete
    Char: Incomplete
    Short: Incomplete
    Int: Incomplete
    Long: Incomplete
    Half: Incomplete
    Float: Incomplete
    Double: Incomplete
    ComplexHalf: Incomplete
    ComplexFloat: Incomplete
    ComplexDouble: Incomplete
    Bool: Incomplete
    BFloat16: Incomplete
    @staticmethod
    def maybe_parse(value: str) -> ScalarType | None: ...
    @staticmethod
    def parse(value: str) -> ScalarType: ...
    @staticmethod
    def parse_set(values: str) -> OrderedSet['ScalarType']: ...

DTYPE_CLASSES: Dict[str, OrderedSet[ScalarType]]

class UfuncKey(Enum):
    CUDAFunctor: Incomplete
    CUDAFunctorOnOther: Incomplete
    CUDAFunctorOnSelf: Incomplete
    CPUScalar: Incomplete
    CPUVector: Incomplete
    ScalarOnly: Incomplete
    Generic: Incomplete
    @staticmethod
    def parse(value: str) -> UfuncKey: ...

class DeviceCheckType(Enum):
    NoCheck: int
    ExactSame: int

class ViewSchemaKind(Enum):
    aliasing: Incomplete
    aliasing_inplace: Incomplete
    non_aliasing: Incomplete

@dataclass(frozen=True)
class NativeFunction:
    namespace: str
    func: FunctionSchema
    use_const_ref_for_mutable_tensors: bool
    device_guard: bool
    device_check: DeviceCheckType
    python_module: str | None
    category_override: str | None
    variants: Set[Variant]
    manual_kernel_registration: bool
    manual_cpp_binding: bool
    loc: Location
    autogen: List['OperatorName']
    ufunc_inner_loop: Dict[UfuncKey, 'UfuncInnerLoop']
    structured: bool
    structured_delegate: OperatorName | None
    structured_inherits: str | None
    precomputed: Precompute | None
    cpp_no_default_args: Set[str]
    is_abstract: bool
    has_composite_implicit_autograd_kernel: bool
    has_composite_implicit_autograd_nested_tensor_kernel: bool
    has_composite_explicit_autograd_kernel: bool
    has_composite_explicit_autograd_non_functional_kernel: bool
    tags: Set[str]
    @staticmethod
    def from_yaml(ei: Dict[str, object], loc: Location, valid_tags: Set[str], ignore_keys: Set[DispatchKey] | None = None) -> Tuple['NativeFunction', Dict[DispatchKey, Dict['OperatorName', 'BackendMetadata']]]:
        """
        Parse a NativeFunction from a dictionary as directly parsed
        from native_functions.yaml
        """
    def validate_unstructured(self) -> None: ...
    def __post_init__(self) -> None: ...
    @property
    def has_composite_kernel(self) -> bool: ...
    @property
    def is_view_op(self) -> bool: ...
    @property
    def view_schema_kind(self) -> ViewSchemaKind: ...
    @property
    def root_name(self) -> str: ...
    @property
    def part_of_structured_group(self) -> bool: ...
    def __init__(self, namespace, func, use_const_ref_for_mutable_tensors, device_guard, device_check, python_module, category_override, variants, manual_kernel_registration, manual_cpp_binding, loc, autogen, ufunc_inner_loop, structured, structured_delegate, structured_inherits, precomputed, cpp_no_default_args, is_abstract, has_composite_implicit_autograd_kernel, has_composite_implicit_autograd_nested_tensor_kernel, has_composite_explicit_autograd_kernel, has_composite_explicit_autograd_non_functional_kernel, tags) -> None: ...

class SchemaKind(Enum):
    functional: Incomplete
    inplace: Incomplete
    out: Incomplete
    mutable: Incomplete
    scratch: Incomplete

@dataclass(frozen=True)
class NativeFunctionsGroup:
    functional: NativeFunction
    inplace: NativeFunction | None
    mutable: NativeFunction | None
    out: NativeFunction
    @property
    def structured(self) -> bool: ...
    def __post_init__(self) -> None: ...
    def signature(self) -> FunctionSchema: ...
    def functions(self) -> Iterator[NativeFunction]: ...
    @property
    def root_name(self) -> str: ...
    @staticmethod
    def from_dict(d: Dict[SchemaKind, NativeFunction]) -> NativeFunctionsGroup | None: ...
    def __init__(self, functional, inplace, mutable, out) -> None: ...

@dataclass(frozen=True)
class BackendMetadata:
    kernel: str
    structured: bool
    cpp_namespace: str
    def supports_symint(self) -> bool: ...
    def __init__(self, kernel, structured, cpp_namespace) -> None: ...

@dataclass(frozen=True)
class UfuncInnerLoop:
    name: str
    supported_dtypes: OrderedSet[ScalarType]
    ufunc_key: UfuncKey
    @staticmethod
    def parse(value: str, ufunc_key: UfuncKey) -> UfuncInnerLoop: ...
    def __init__(self, name, supported_dtypes, ufunc_key) -> None: ...

@dataclass(frozen=True)
class BackendIndex:
    dispatch_key: DispatchKey
    use_out_as_primary: bool
    device_guard: bool
    external: bool
    index: Dict['OperatorName', BackendMetadata]
    @staticmethod
    def grow_index(parent_index: Dict[DispatchKey, Dict['OperatorName', BackendMetadata]], child_index: Dict[DispatchKey, Dict['OperatorName', BackendMetadata]]) -> None: ...
    def primary(self, g: NativeFunctionsGroup) -> NativeFunction: ...
    def has_kernel(self, g: NativeFunction | NativeFunctionsGroup) -> bool: ...
    def get_kernel(self, g: NativeFunction | NativeFunctionsGroup) -> BackendMetadata | None: ...
    def native_function_class_name(self) -> str | None: ...
    def __init__(self, dispatch_key, use_out_as_primary, device_guard, external, index) -> None: ...

@dataclass(frozen=True)
class FunctionSchema:
    name: OperatorName
    arguments: Arguments
    returns: Tuple['Return', ...]
    def schema_order_arguments(self) -> Iterator['Argument']: ...
    decl_re = ...
    @staticmethod
    def parse(func: str) -> FunctionSchema: ...
    def returns_are_aliased(self) -> bool: ...
    def __post_init__(self) -> None: ...
    def is_functional_fn(self) -> bool: ...
    def is_out_fn(self) -> bool: ...
    def kind(self) -> SchemaKind:
        """
        What kind of schema is this?  A functional schema is one
        that returns a newly allocated output; an inplace schema
        modifies the self argument inplace; an out schema writes
        the result into an explicitly provided out argument.
        """
    def aliased_return_names(self) -> List[str | None]: ...
    def signature(self, *, strip_default: bool = False, strip_view_copy_name: bool = False, keep_return_names: bool = False) -> FunctionSchema:
        '''
                Certain schemas are \'related\', in that they are simply
                inplace/out/functional versions of the same function.  This method
                factors these schemas into the "core" functional signature which
                is equal across all versions.

                Here is what normalization happens to the schema to convert
                it to a signature:
                - The overload name is stripped (name is retained, since
                  it expresses semantic content about what the function does)
                - Inplace is set False
                - Out arguments are stripped
                - Mutable post_self_positional args are converted to returns
                - Mutability annotations are stripped  (this is sound
                  because you cannot overload on mutability annotation)
                - Return names are stripped since they are not overloadable and
                  some variants have return names but some not
                - TensorOptions are dropped
                  because out= variants of factory functions don\'t include them
                  (and we want to be able to pair up factory functions with their out variants)

                Finally, we want to be able to pair up related "view" and their
                corresponding "view_copy" operators. We do this by optionally
                stripping the trailing "_copy" from the base name.

                Example of a mutable op before and after:

                f.func (Mutable operator):
        _fused_moving_avg_obs_fq_helper(Tensor self, Tensor observer_on, Tensor fake_quant_on, Tensor(a!) running_min, Tensor(b!) running_max, Tensor(c!) scale, Tensor(d!) zero_point, float averaging_const, int quant_min, int quant_max, int ch_axis, bool per_row_fake_quant=False, bool symmetric_quant=False) -> (Tensor output, Tensor mask)  # noqa: B950

                f.func (Corresponding functional operator):
        _fused_moving_avg_obs_fq_helper.functional(Tensor self, Tensor observer_on, Tensor fake_quant_on, Tensor running_min, Tensor running_max, Tensor scale, Tensor zero_point, float averaging_const, int quant_min, int quant_max, int ch_axis, bool per_row_fake_quant=False, bool symmetric_quant=False) -> (Tensor output, Tensor mask, Tensor running_min_out, Tensor running_max_out, Tensor scale_out, Tensor zero_point_out)  # noqa: B950

                f.func.signature() output:
        _fused_moving_avg_obs_fq_helper(Tensor self, Tensor observer_on, Tensor fake_quant_on, Tensor running_min, Tensor running_max, Tensor scale, Tensor zero_point, float averaging_const, int quant_min, int quant_max, int ch_axis, bool per_row_fake_quant=False, bool symmetric_quant=False) -> (Tensor, Tensor, Tensor, Tensor, Tensor, Tensor)  # noqa: B950
        '''
    def view_signature(self) -> FunctionSchema: ...
    def with_name(self, name: OperatorName) -> FunctionSchema: ...
    @property
    def modifies_arguments(self) -> bool: ...
    def has_symint(self) -> bool: ...
    def __init__(self, name, arguments, returns) -> None: ...

@dataclass(frozen=True)
class Annotation:
    alias_set: Tuple[str, ...]
    is_write: bool
    alias_set_after: Tuple[str, ...]
    @staticmethod
    def parse(ann: str) -> Annotation: ...
    def __init__(self, alias_set, is_write, alias_set_after) -> None: ...

@dataclass(frozen=True)
class Type:
    @staticmethod
    def parse(t: str) -> Type: ...
    def is_base_ty_like(self, base_ty: BaseTy) -> bool: ...
    def is_tensor_like(self) -> bool: ...
    def is_generator_like(self) -> bool: ...
    def is_symint_like(self) -> bool: ...
    def is_nullable(self) -> bool: ...
    def is_list_like(self) -> ListType | None: ...

class BaseTy(Enum):
    Generator: Incomplete
    ScalarType: Incomplete
    Tensor: Incomplete
    int: Incomplete
    Dimname: Incomplete
    DimVector: Incomplete
    float: Incomplete
    str: Incomplete
    bool: Incomplete
    Layout: Incomplete
    Device: Incomplete
    Scalar: Incomplete
    MemoryFormat: Incomplete
    QScheme: Incomplete
    Storage: Incomplete
    Stream: Incomplete
    SymInt: Incomplete
    ConstQuantizerPtr: Incomplete

@dataclass(frozen=True)
class BaseType(Type):
    name: BaseTy
    def is_base_ty_like(self, base_ty: BaseTy) -> bool: ...
    def is_nullable(self) -> bool: ...
    def is_list_like(self) -> ListType | None: ...
    def is_symint_like(self) -> bool: ...
    def __init__(self, name) -> None: ...

@dataclass(frozen=True)
class OptionalType(Type):
    elem: Type
    def is_base_ty_like(self, base_ty: BaseTy) -> bool: ...
    def is_symint_like(self) -> bool: ...
    def is_nullable(self) -> bool: ...
    def is_list_like(self) -> ListType | None: ...
    def __init__(self, elem) -> None: ...

@dataclass(frozen=True)
class CustomClassType(Type):
    class_name: str
    def is_base_ty_like(self, base_ty: BaseTy) -> bool: ...
    def is_symint_like(self) -> bool: ...
    def is_nullable(self) -> bool:
        """
        Assume a custom class is not nullable.
        """
    def is_list_like(self) -> ListType | None: ...
    def __init__(self, class_name) -> None: ...

@dataclass(frozen=True)
class ListType(Type):
    elem: Type
    size: int | None
    def is_base_ty_like(self, base_ty: BaseTy) -> bool: ...
    def is_symint_like(self) -> bool: ...
    def is_nullable(self) -> bool: ...
    def is_list_like(self) -> ListType | None: ...
    def __init__(self, elem, size) -> None: ...

@dataclass(frozen=True)
class Argument:
    name: str
    type: Type
    default: str | None
    annotation: Annotation | None
    @staticmethod
    def parse(arg: str) -> Argument: ...
    @property
    def is_write(self) -> bool: ...
    def __init__(self, name, type, default, annotation) -> None: ...

@dataclass(frozen=True)
class Return:
    name: str | None
    type: Type
    annotation: Annotation | None
    @staticmethod
    def parse(arg: str) -> Return: ...
    @property
    def is_write(self) -> bool: ...
    def __init__(self, name, type, annotation) -> None: ...

@dataclass(frozen=True)
class SelfArgument:
    argument: Argument
    def __init__(self, argument) -> None: ...

@dataclass(frozen=True)
class TensorOptionsArguments:
    dtype: Argument
    layout: Argument
    device: Argument
    pin_memory: Argument
    def all(self) -> Sequence[Argument]: ...
    def __init__(self, dtype, layout, device, pin_memory) -> None: ...

@dataclass(frozen=True)
class Arguments:
    pre_self_positional: Tuple[Argument, ...]
    self_arg: SelfArgument | None
    post_self_positional: Tuple[Argument, ...]
    pre_tensor_options_kwarg_only: Tuple[Argument, ...]
    tensor_options: TensorOptionsArguments | None
    post_tensor_options_kwarg_only: Tuple[Argument, ...]
    out: Tuple[Argument, ...]
    @property
    def flat_non_out(self) -> Sequence[Argument]: ...
    @property
    def flat_positional(self) -> Sequence[Argument]: ...
    @property
    def post_self_positional_mutable(self) -> Sequence[Argument]: ...
    @property
    def flat_kwarg_only(self) -> Sequence[Argument]: ...
    @property
    def flat_all(self) -> Sequence[Argument]: ...
    @property
    def non_out(self) -> Sequence[Argument | SelfArgument | TensorOptionsArguments]: ...
    @property
    def positional(self) -> Sequence[Argument | SelfArgument]: ...
    @property
    def kwarg_only(self) -> Sequence[Argument | TensorOptionsArguments]: ...
    @property
    def all(self) -> Sequence[Argument | SelfArgument | TensorOptionsArguments]: ...
    def mutable_arg_names(self) -> List[str]: ...
    def has_tensor_arg(self) -> bool: ...
    def has_symint_arg(self) -> bool: ...
    def has_generator_arg(self) -> bool: ...
    def signature(self, *, strip_default: bool = False) -> Arguments: ...
    def remove_self_annotation(self) -> Arguments: ...
    def with_out_args(self, outs: List[Argument]) -> Arguments: ...
    @staticmethod
    def parse(args: str) -> Arguments:
        """
        Input: 'int x, int y, int z'
        """
    def __post_init__(self) -> None: ...
    def __init__(self, pre_self_positional, self_arg, post_self_positional, pre_tensor_options_kwarg_only, tensor_options, post_tensor_options_kwarg_only, out) -> None: ...

AUGMENTED_ASSIGNMENT_NAMES: Incomplete

@dataclass(frozen=True)
class BaseOperatorName:
    base: str
    inplace: bool
    dunder_method: bool
    functional_overload: bool = ...
    @staticmethod
    def parse(op: str) -> BaseOperatorName: ...
    def __init__(self, base, inplace, dunder_method, functional_overload) -> None: ...

@dataclass(frozen=True)
class OperatorName:
    name: BaseOperatorName
    overload_name: str
    @staticmethod
    def parse(op_name: str) -> OperatorName: ...
    def unambiguous_name(self) -> str: ...
    def remove_inplace(self) -> OperatorName: ...
    def with_overload(self, overload: str) -> OperatorName: ...
    def __init__(self, name, overload_name) -> None: ...

def gets_generated_out_inplace_wrapper(f: NativeFunction, g: NativeFunctionsGroup, b: BackendIndex) -> bool: ...

@dataclass(frozen=True)
class NativeFunctionsViewGroup:
    view: NativeFunction
    view_copy: NativeFunction | None
    view_inplace: NativeFunction | None
    def __post_init__(self) -> None: ...
    def functions(self, *, include_copy: bool = True) -> Iterator[NativeFunction]: ...
    @property
    def root_name(self) -> str: ...
    @property
    def composite(self) -> bool: ...
    def __init__(self, view, view_copy, view_inplace) -> None: ...

def gets_generated_view_copy(f: NativeFunction) -> bool: ...
def get_view_copy_name(f: NativeFunction) -> OperatorName: ...
def parse_returns(return_decl: str) -> Tuple[Return, ...]:
    """
    Input: '()'
    Output: []
    """

@dataclass(frozen=True)
class Precompute:
    replace: Dict[str, List[Argument]]
    add: List[Argument]
    @staticmethod
    def parse(src: object) -> Precompute: ...
    def __post_init__(self) -> None: ...
    def to_list(self) -> List[str]: ...
    def __init__(self, replace, add) -> None: ...
