from _typeshed import Incomplete
from llvmlite.ir._utils import _StrCaching

class Type(_StrCaching):
    """
    The base class for all LLVM types.
    """
    is_pointer: bool
    null: str
    def as_pointer(self, addrspace: int = 0): ...
    def __ne__(self, other): ...
    def get_abi_size(self, target_data, context: Incomplete | None = None):
        """
        Get the ABI size of this type according to data layout *target_data*.
        """
    def get_abi_alignment(self, target_data, context: Incomplete | None = None):
        """
        Get the minimum ABI alignment of this type according to data layout
        *target_data*.
        """
    def format_constant(self, value):
        """
        Format constant *value* of this type.  This method may be overriden
        by subclasses.
        """
    def wrap_constant_value(self, value):
        """
        Wrap constant *value* if necessary.  This method may be overriden
        by subclasses (especially aggregate types).
        """
    def __call__(self, value):
        """
        Create a LLVM constant of this type with the given Python value.
        """

class MetaDataType(Type):
    def as_pointer(self) -> None: ...
    def __eq__(self, other): ...
    def __hash__(self): ...

class LabelType(Type):
    """
    The label type is the type of e.g. basic blocks.
    """

class PointerType(Type):
    """
    The type of all pointer values.
    """
    is_pointer: bool
    null: str
    pointee: Incomplete
    addrspace: Incomplete
    def __init__(self, pointee, addrspace: int = 0) -> None: ...
    def __eq__(self, other): ...
    def __hash__(self): ...
    def gep(self, i):
        """
        Resolve the type of the i-th element (for getelementptr lookups).
        """
    @property
    def intrinsic_name(self): ...

class VoidType(Type):
    """
    The type for empty values (e.g. a function returning no value).
    """
    def __eq__(self, other): ...
    def __hash__(self): ...

class FunctionType(Type):
    """
    The type for functions.
    """
    return_type: Incomplete
    args: Incomplete
    var_arg: Incomplete
    def __init__(self, return_type, args, var_arg: bool = False) -> None: ...
    def __eq__(self, other): ...
    def __hash__(self): ...

class IntType(Type):
    """
    The type for integers.
    """
    null: str
    width: int
    def __new__(cls, bits): ...
    def __getnewargs__(self): ...
    def __copy__(self): ...
    def __eq__(self, other): ...
    def __hash__(self): ...
    def format_constant(self, val): ...
    def wrap_constant_value(self, val): ...
    @property
    def intrinsic_name(self): ...

class _BaseFloatType(Type):
    def __new__(cls): ...
    def __eq__(self, other): ...
    def __hash__(self): ...

class HalfType(_BaseFloatType):
    """
    The type for single-precision floats.
    """
    null: str
    intrinsic_name: str
    def format_constant(self, value): ...

class FloatType(_BaseFloatType):
    """
    The type for single-precision floats.
    """
    null: str
    intrinsic_name: str
    def format_constant(self, value): ...

class DoubleType(_BaseFloatType):
    """
    The type for double-precision floats.
    """
    null: str
    intrinsic_name: str
    def format_constant(self, value): ...

class _Repeat:
    value: Incomplete
    size: Incomplete
    def __init__(self, value, size) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, item): ...

class VectorType(Type):
    '''
    The type for vectors of primitive data items (e.g. "<f32 x 4>").
    '''
    element: Incomplete
    count: Incomplete
    def __init__(self, element, count) -> None: ...
    @property
    def elements(self): ...
    def __len__(self) -> int: ...
    def __eq__(self, other): ...
    def __hash__(self): ...
    def __copy__(self): ...
    def format_constant(self, value): ...
    def wrap_constant_value(self, values): ...

class Aggregate(Type):
    """
    Base class for aggregate types.
    See http://llvm.org/docs/LangRef.html#t-aggregate
    """
    def wrap_constant_value(self, values): ...

class ArrayType(Aggregate):
    '''
    The type for fixed-size homogenous arrays (e.g. "[f32 x 3]").
    '''
    element: Incomplete
    count: Incomplete
    def __init__(self, element, count) -> None: ...
    @property
    def elements(self): ...
    def __len__(self) -> int: ...
    def __eq__(self, other): ...
    def __hash__(self): ...
    def gep(self, i):
        """
        Resolve the type of the i-th element (for getelementptr lookups).
        """
    def format_constant(self, value): ...

class BaseStructType(Aggregate):
    """
    The base type for heterogenous struct types.
    """
    @property
    def packed(self):
        """
        A boolean attribute that indicates whether the structure uses
        packed layout.
        """
    @packed.setter
    def packed(self, val) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self): ...
    @property
    def is_opaque(self): ...
    def structure_repr(self):
        """
        Return the LLVM IR for the structure representation
        """
    def format_constant(self, value): ...
    def gep(self, i):
        """
        Resolve the type of the i-th element (for getelementptr lookups).

        *i* needs to be a LLVM constant, so that the type can be determined
        at compile-time.
        """

class LiteralStructType(BaseStructType):
    '''
    The type of "literal" structs, i.e. structs with a literally-defined
    type (by contrast with IdentifiedStructType).
    '''
    null: str
    elements: Incomplete
    packed: Incomplete
    def __init__(self, elems, packed: bool = False) -> None:
        """
        *elems* is a sequence of types to be used as members.
        *packed* controls the use of packed layout.
        """
    def __eq__(self, other): ...
    def __hash__(self): ...

class IdentifiedStructType(BaseStructType):
    """
    A type which is a named alias for another struct type, akin to a typedef.
    While literal struct types can be structurally equal (see
    LiteralStructType), identified struct types are compared by name.

    Do not use this directly.
    """
    null: str
    context: Incomplete
    name: Incomplete
    elements: Incomplete
    packed: Incomplete
    def __init__(self, context, name, packed: bool = False) -> None:
        """
        *context* is a llvmlite.ir.Context.
        *name* is the identifier for the new struct type.
        *packed* controls the use of packed layout.
        """
    def get_declaration(self):
        """
        Returns the string for the declaration of the type
        """
    def __eq__(self, other): ...
    def __hash__(self): ...
    def set_body(self, *elems) -> None: ...
