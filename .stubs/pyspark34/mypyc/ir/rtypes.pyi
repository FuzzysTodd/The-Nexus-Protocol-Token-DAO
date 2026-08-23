import abc
from _typeshed import Incomplete
from abc import abstractmethod
from mypyc.common import IS_32_BIT_PLATFORM as IS_32_BIT_PLATFORM, JsonDict as JsonDict, PLATFORM_SIZE as PLATFORM_SIZE, short_name as short_name
from mypyc.ir.class_ir import ClassIR as ClassIR
from mypyc.ir.ops import DeserMaps as DeserMaps
from mypyc.namegen import NameGenerator as NameGenerator
from typing import ClassVar, Final, Generic, TypeVar
from typing_extensions import TypeGuard

T = TypeVar('T')

class RType(metaclass=abc.ABCMeta):
    """Abstract base class for runtime types (erased, only concrete; no generics)."""
    name: str
    is_unboxed: bool
    c_undefined: str
    is_refcounted: bool
    error_overlap: bool
    @abstractmethod
    def accept(self, visitor: RTypeVisitor[T]) -> T: ...
    def short_name(self) -> str: ...
    def serialize(self) -> JsonDict | str: ...

def deserialize_type(data: JsonDict | str, ctx: DeserMaps) -> RType:
    """Deserialize a JSON-serialized RType.

    Arguments:
        data: The decoded JSON of the serialized type
        ctx: The deserialization maps to use
    """

class RTypeVisitor(Generic[T], metaclass=abc.ABCMeta):
    """Generic visitor over RTypes (uses the visitor design pattern)."""
    @abstractmethod
    def visit_rprimitive(self, typ: RPrimitive) -> T: ...
    @abstractmethod
    def visit_rinstance(self, typ: RInstance) -> T: ...
    @abstractmethod
    def visit_runion(self, typ: RUnion) -> T: ...
    @abstractmethod
    def visit_rtuple(self, typ: RTuple) -> T: ...
    @abstractmethod
    def visit_rstruct(self, typ: RStruct) -> T: ...
    @abstractmethod
    def visit_rarray(self, typ: RArray) -> T: ...
    @abstractmethod
    def visit_rvoid(self, typ: RVoid) -> T: ...

class RVoid(RType):
    """The void type (no value).

    This is a singleton -- use void_rtype (below) to refer to this instead of
    constructing a new instance.
    """
    is_unboxed: bool
    name: str
    ctype: str
    def accept(self, visitor: RTypeVisitor[T]) -> T: ...
    def serialize(self) -> str: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...

void_rtype: Final[Incomplete]

class RPrimitive(RType):
    """Primitive type such as 'object' or 'int'.

    These often have custom ops associated with them. The 'object'
    primitive type can be used to hold arbitrary Python objects.

    Different primitive types have different representations, and
    primitives may be unboxed or boxed. Primitive types don't need to
    directly correspond to Python types, but most do.

    NOTE: All supported primitive types are defined below
    (e.g. object_rprimitive).
    """
    primitive_map: ClassVar[dict[str, RPrimitive]]
    name: Incomplete
    is_unboxed: Incomplete
    is_refcounted: Incomplete
    is_native_int: Incomplete
    is_signed: Incomplete
    size: Incomplete
    error_overlap: Incomplete
    c_undefined: str
    def __init__(self, name: str, *, is_unboxed: bool, is_refcounted: bool, is_native_int: bool = False, is_signed: bool = False, ctype: str = 'PyObject *', size: int = ..., error_overlap: bool = False) -> None: ...
    def accept(self, visitor: RTypeVisitor[T]) -> T: ...
    def serialize(self) -> str: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...

object_rprimitive: Final[Incomplete]
object_pointer_rprimitive: Final[Incomplete]
int_rprimitive: Final[Incomplete]
short_int_rprimitive: Final[Incomplete]
int16_rprimitive: Final[Incomplete]
int32_rprimitive: Final[Incomplete]
int64_rprimitive: Final[Incomplete]
uint8_rprimitive: Final[Incomplete]
u16_rprimitive: Final[Incomplete]
uint32_rprimitive: Final[Incomplete]
uint64_rprimitive: Final[Incomplete]
c_int_rprimitive = int32_rprimitive
c_size_t_rprimitive = uint32_rprimitive
c_pyssize_t_rprimitive: Incomplete
c_size_t_rprimitive = uint64_rprimitive
pointer_rprimitive: Final[Incomplete]
c_pointer_rprimitive: Final[Incomplete]
bitmap_rprimitive: Final[Incomplete]
float_rprimitive: Final[Incomplete]
bool_rprimitive: Final[Incomplete]
bit_rprimitive: Final[Incomplete]
none_rprimitive: Final[Incomplete]
list_rprimitive: Final[Incomplete]
dict_rprimitive: Final[Incomplete]
set_rprimitive: Final[Incomplete]
str_rprimitive: Final[Incomplete]
bytes_rprimitive: Final[Incomplete]
tuple_rprimitive: Final[Incomplete]
range_rprimitive: Final[Incomplete]

def is_tagged(rtype: RType) -> bool: ...
def is_int_rprimitive(rtype: RType) -> bool: ...
def is_short_int_rprimitive(rtype: RType) -> bool: ...
def is_int16_rprimitive(rtype: RType) -> TypeGuard[RPrimitive]: ...
def is_int32_rprimitive(rtype: RType) -> TypeGuard[RPrimitive]: ...
def is_int64_rprimitive(rtype: RType) -> bool: ...
def is_fixed_width_rtype(rtype: RType) -> TypeGuard[RPrimitive]: ...
def is_uint8_rprimitive(rtype: RType) -> TypeGuard[RPrimitive]: ...
def is_uint32_rprimitive(rtype: RType) -> bool: ...
def is_uint64_rprimitive(rtype: RType) -> bool: ...
def is_c_py_ssize_t_rprimitive(rtype: RType) -> bool: ...
def is_pointer_rprimitive(rtype: RType) -> bool: ...
def is_float_rprimitive(rtype: RType) -> bool: ...
def is_bool_rprimitive(rtype: RType) -> bool: ...
def is_bit_rprimitive(rtype: RType) -> bool: ...
def is_object_rprimitive(rtype: RType) -> bool: ...
def is_none_rprimitive(rtype: RType) -> bool: ...
def is_list_rprimitive(rtype: RType) -> bool: ...
def is_dict_rprimitive(rtype: RType) -> bool: ...
def is_set_rprimitive(rtype: RType) -> bool: ...
def is_str_rprimitive(rtype: RType) -> bool: ...
def is_bytes_rprimitive(rtype: RType) -> bool: ...
def is_tuple_rprimitive(rtype: RType) -> bool: ...
def is_range_rprimitive(rtype: RType) -> bool: ...
def is_sequence_rprimitive(rtype: RType) -> bool: ...

class TupleNameVisitor(RTypeVisitor[str]):
    """Produce a tuple name based on the concrete representations of types."""
    def visit_rinstance(self, t: RInstance) -> str: ...
    def visit_runion(self, t: RUnion) -> str: ...
    def visit_rprimitive(self, t: RPrimitive) -> str: ...
    def visit_rtuple(self, t: RTuple) -> str: ...
    def visit_rstruct(self, t: RStruct) -> str: ...
    def visit_rarray(self, t: RArray) -> str: ...
    def visit_rvoid(self, t: RVoid) -> str: ...

class RTuple(RType):
    """Fixed-length unboxed tuple (represented as a C struct).

    These are used to represent mypy TupleType values (fixed-length
    Python tuples). Since this is unboxed, the identity of a tuple
    object is not preserved within compiled code. If the identity of a
    tuple is important, or there is a need to have multiple references
    to a single tuple object, a variable-length tuple should be used
    (tuple_rprimitive or Tuple[T, ...]  with explicit '...'), as they
    are boxed.

    These aren't immutable. However, user code won't be able to mutate
    individual tuple items.
    """
    is_unboxed: bool
    name: str
    types: Incomplete
    is_refcounted: Incomplete
    unique_id: Incomplete
    struct_name: Incomplete
    error_overlap: Incomplete
    def __init__(self, types: list[RType]) -> None: ...
    def accept(self, visitor: RTypeVisitor[T]) -> T: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def serialize(self) -> JsonDict: ...
    @classmethod
    def deserialize(cls, data: JsonDict, ctx: DeserMaps) -> RTuple: ...

exc_rtuple: Incomplete
dict_next_rtuple_pair: Incomplete
dict_next_rtuple_single: Incomplete

def compute_rtype_alignment(typ: RType) -> int:
    """Compute alignment of a given type based on platform alignment rule"""
def compute_rtype_size(typ: RType) -> int:
    """Compute unaligned size of rtype"""
def compute_aligned_offsets_and_size(types: list[RType]) -> tuple[list[int], int]:
    """Compute offsets and total size of a list of types after alignment

    Note that the types argument are types of values that are stored
    sequentially with platform default alignment.
    """

class RStruct(RType):
    """C struct type"""
    name: Incomplete
    names: Incomplete
    types: Incomplete
    def __init__(self, name: str, names: list[str], types: list[RType]) -> None: ...
    def accept(self, visitor: RTypeVisitor[T]) -> T: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def serialize(self) -> JsonDict: ...
    @classmethod
    def deserialize(cls, data: JsonDict, ctx: DeserMaps) -> RStruct: ...

class RInstance(RType):
    """Instance of user-defined class (compiled to C extension class).

    The runtime representation is 'PyObject *', and these are always
    boxed and thus reference-counted.

    These support fast method calls and fast attribute access using
    vtables, and they usually use a dict-free, struct-based
    representation of attributes. Method calls and attribute access
    can skip the vtable if we know that there is no overriding.

    These are also sometimes called 'native' types, since these have
    the most efficient representation and ops (along with certain
    RPrimitive types and RTuple).
    """
    is_unboxed: bool
    name: Incomplete
    class_ir: Incomplete
    def __init__(self, class_ir: ClassIR) -> None: ...
    def accept(self, visitor: RTypeVisitor[T]) -> T: ...
    def struct_name(self, names: NameGenerator) -> str: ...
    def getter_index(self, name: str) -> int: ...
    def setter_index(self, name: str) -> int: ...
    def method_index(self, name: str) -> int: ...
    def attr_type(self, name: str) -> RType: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def serialize(self) -> str: ...

class RUnion(RType):
    """union[x, ..., y]"""
    is_unboxed: bool
    name: str
    items: Incomplete
    items_set: Incomplete
    def __init__(self, items: list[RType]) -> None: ...
    @staticmethod
    def make_simplified_union(items: list[RType]) -> RType:
        """Return a normalized union that covers the given items.

        Flatten nested unions and remove duplicate items.

        Overlapping items are *not* simplified. For example,
        [object, str] will not be simplified.
        """
    def accept(self, visitor: RTypeVisitor[T]) -> T: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def serialize(self) -> JsonDict: ...
    @classmethod
    def deserialize(cls, data: JsonDict, ctx: DeserMaps) -> RUnion: ...

def flatten_nested_unions(types: list[RType]) -> list[RType]: ...
def optional_value_type(rtype: RType) -> RType | None:
    """If rtype is the union of none_rprimitive and another type X, return X.

    Otherwise return None.
    """
def is_optional_type(rtype: RType) -> bool:
    """Is rtype an optional type with exactly two union items?"""

class RArray(RType):
    """Fixed-length C array type (for example, int[5]).

    Note that the implementation is a bit limited, and these can basically
    be only used for local variables that are initialized in one location.
    """
    item_type: Incomplete
    length: Incomplete
    is_refcounted: bool
    def __init__(self, item_type: RType, length: int) -> None: ...
    def accept(self, visitor: RTypeVisitor[T]) -> T: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def serialize(self) -> JsonDict: ...
    @classmethod
    def deserialize(cls, data: JsonDict, ctx: DeserMaps) -> RArray: ...

PyObject: Incomplete
PyVarObject: Incomplete
setentry: Incomplete
smalltable: Incomplete
PySetObject: Incomplete
PyListObject: Incomplete

def check_native_int_range(rtype: RPrimitive, n: int) -> bool:
    """Is n within the range of a native, fixed-width int type?

    Assume the type is a fixed-width int type.
    """
