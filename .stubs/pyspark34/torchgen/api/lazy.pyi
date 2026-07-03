from _typeshed import Incomplete
from torchgen.api.types import BaseCType as BaseCType, BaseCppType as BaseCppType, CType as CType, ListCType as ListCType, NamedCType as NamedCType, OptionalCType as OptionalCType, SymIntT as SymIntT, VectorCType as VectorCType, boolT as boolT, deviceT as deviceT, doubleT as doubleT, layoutT as layoutT, longT as longT, memoryFormatT as memoryFormatT, scalarT as scalarT, scalarTypeT as scalarTypeT, stringT as stringT
from torchgen.model import Argument as Argument, BaseTy as BaseTy, BaseType as BaseType, FunctionSchema as FunctionSchema, ListType as ListType, OperatorName as OperatorName, OptionalType as OptionalType, Return as Return, TensorOptionsArguments as TensorOptionsArguments, Type as Type
from typing import Any, List, Tuple

def getValueT() -> BaseCppType: ...
def setValueT(val: BaseCppType) -> None: ...

tensorListValueT: Incomplete

def process_ir_type(typ: Type, properties: LazyIrProperties, *, symint: bool) -> BaseCType | VectorCType | OptionalCType | ListCType:
    """
    This function takes a type from NativeFunctions and converts it for use with
    lazy tensor codegen.

    Type conversion for lazy currently consists of
     (1) changing at::Tensors into lazy::Values
     (2) wrapping everything in a BaseCType
     (3) making cpp-reference types into cpp-value types (e.g. vector instead of IntArrayRef)

    (1) converts at::Tensors to lazy::Values (which wrap lazy::Nodes, with which Lazy IR represents tensors.)
    There is special handling for Optional[Tensor] or List[Tensor], etc- hence 'tensor-like'

    This is incomplete- there are assertions in places that it's expected to need to add
    more types as the codegen is used with more operators.
    """
def isValueType(typ: CType, properties: LazyIrProperties | None = None) -> bool:
    """
    Given a type, determine if it is a Value-like type.  This is equivalent to
    being Tensor-like, but assumes the type has already been transformed.
    """
def isSymIntType(typ: Type) -> bool: ...
def isWrappedScalarType(typ: Type) -> bool:
    """
    Given a type, determine if it is a c10::scalar which we will wrap in a lazy Value.
    Since we literally change the type from scalarT to valueT, information is lost.
    This function helps build a list of wrapped scalars to save that information
    """
def isGeneratorType(typ: Type) -> bool: ...

class LazyArgument:
    name: str
    orig_type: Type
    lazy_type_: CType | None
    is_wrapped_scalar: bool
    is_generator: bool
    is_symint_or_list: bool
    symint: bool
    is_lazy_value: bool
    is_optional: Incomplete
    def __init__(self, arg: Argument, properties: LazyIrProperties, *, symint: bool) -> None: ...
    @property
    def lazy_type(self) -> CType: ...

class LazyIrProperties:
    """Collection of properties for an IR node

    The property groups are listed below. Each group is mutually
    exclusive, meaning that only one property from each group can be True
    at any one time. The properties can be accessed as if they were normal
    attributes. The mutual exclusivity is automatically handled.
    """
    Properties: Tuple[Tuple[str, ...], ...]
    def __init__(self, *default_properties: str) -> None: ...
    def __getattr__(self, key: str) -> Any: ...
    def __setattr__(self, key: str, value: Any) -> Any: ...

class LazyIrSchema:
    name: OperatorName
    positional_args: Tuple[LazyArgument, ...]
    keyword_args: Tuple[LazyArgument, ...]
    returns: Tuple['Return', ...]
    generator_arg: NamedCType | None
    func: FunctionSchema
    symint: bool
    properties: LazyIrProperties
    opkind: str | None
    def __init__(self, func: FunctionSchema, properties: LazyIrProperties | None = None, *, symint: bool) -> None: ...
    @property
    def node_name(self) -> str:
        """
        Return camel-case version of op in node.

        Note: This function also appends any `overload_name` in the operation.
        For example, if the op is `bitwise_and.Tensor`, the returned name
        will be `BitwiseAndTensor`.
        """
    @property
    def aten_name(self) -> str: ...
    @property
    def base_name(self) -> str: ...
    def filtered_args(self, positional: bool = True, keyword: bool = True, values: bool = True, scalars: bool = True, generator: bool = False) -> List[LazyArgument]: ...
    @property
    def positional_values(self) -> List[LazyArgument]: ...
    @property
    def positional_scalars(self) -> List[LazyArgument]: ...
    @property
    def keyword_values(self) -> List[LazyArgument]: ...
    @property
    def keyword_scalars(self) -> List[LazyArgument]: ...
