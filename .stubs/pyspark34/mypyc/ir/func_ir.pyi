from _typeshed import Incomplete
from mypy.nodes import ArgKind
from mypyc.common import BITMAP_BITS as BITMAP_BITS, JsonDict as JsonDict, bitmap_name as bitmap_name, get_id_from_name as get_id_from_name, short_id_from_name as short_id_from_name
from mypyc.ir.ops import Assign as Assign, AssignMulti as AssignMulti, BasicBlock as BasicBlock, ControlOp as ControlOp, DeserMaps as DeserMaps, LoadAddress as LoadAddress, Register as Register, Value as Value
from mypyc.ir.rtypes import RType as RType, bitmap_rprimitive as bitmap_rprimitive, deserialize_type as deserialize_type
from mypyc.namegen import NameGenerator as NameGenerator
from typing import Final, Sequence

class RuntimeArg:
    """Description of a function argument in IR.

    Argument kind is one of ARG_* constants defined in mypy.nodes.
    """
    name: Incomplete
    type: Incomplete
    kind: Incomplete
    pos_only: Incomplete
    def __init__(self, name: str, typ: RType, kind: ArgKind = ..., pos_only: bool = False) -> None: ...
    @property
    def optional(self) -> bool: ...
    def serialize(self) -> JsonDict: ...
    @classmethod
    def deserialize(cls, data: JsonDict, ctx: DeserMaps) -> RuntimeArg: ...

class FuncSignature:
    """Signature of a function in IR."""
    args: Incomplete
    ret_type: Incomplete
    num_bitmap_args: Incomplete
    def __init__(self, args: Sequence[RuntimeArg], ret_type: RType) -> None: ...
    def real_args(self) -> tuple[RuntimeArg, ...]:
        """Return arguments without any synthetic bitmap arguments."""
    def bound_sig(self) -> FuncSignature: ...
    def serialize(self) -> JsonDict: ...
    @classmethod
    def deserialize(cls, data: JsonDict, ctx: DeserMaps) -> FuncSignature: ...

def num_bitmap_args(args: tuple[RuntimeArg, ...]) -> int: ...

FUNC_NORMAL: Final[int]
FUNC_STATICMETHOD: Final[int]
FUNC_CLASSMETHOD: Final[int]

class FuncDecl:
    """Declaration of a function in IR (without body or implementation).

    A function can be a regular module-level function, a method, a
    static method, a class method, or a property getter/setter.
    """
    name: Incomplete
    class_name: Incomplete
    module_name: Incomplete
    sig: Incomplete
    kind: Incomplete
    is_prop_setter: Incomplete
    is_prop_getter: Incomplete
    bound_sig: Incomplete
    implicit: Incomplete
    def __init__(self, name: str, class_name: str | None, module_name: str, sig: FuncSignature, kind: int = ..., is_prop_setter: bool = False, is_prop_getter: bool = False, implicit: bool = False) -> None: ...
    @property
    def line(self) -> int: ...
    @line.setter
    def line(self, line: int) -> None: ...
    @property
    def id(self) -> str: ...
    @staticmethod
    def compute_shortname(class_name: str | None, name: str) -> str: ...
    @property
    def shortname(self) -> str: ...
    @property
    def fullname(self) -> str: ...
    def cname(self, names: NameGenerator) -> str: ...
    def serialize(self) -> JsonDict: ...
    @staticmethod
    def get_id_from_json(func_ir: JsonDict) -> str:
        """Get the id from the serialized FuncIR associated with this FuncDecl"""
    @classmethod
    def deserialize(cls, data: JsonDict, ctx: DeserMaps) -> FuncDecl: ...

class FuncIR:
    """Intermediate representation of a function with contextual information.

    Unlike FuncDecl, this includes the IR of the body (basic blocks).
    """
    decl: Incomplete
    arg_regs: Incomplete
    blocks: Incomplete
    traceback_name: Incomplete
    def __init__(self, decl: FuncDecl, arg_regs: list[Register], blocks: list[BasicBlock], line: int = -1, traceback_name: str | None = None) -> None: ...
    @property
    def line(self) -> int: ...
    @property
    def args(self) -> Sequence[RuntimeArg]: ...
    @property
    def ret_type(self) -> RType: ...
    @property
    def class_name(self) -> str | None: ...
    @property
    def sig(self) -> FuncSignature: ...
    @property
    def name(self) -> str: ...
    @property
    def fullname(self) -> str: ...
    @property
    def id(self) -> str: ...
    def cname(self, names: NameGenerator) -> str: ...
    def serialize(self) -> JsonDict: ...
    @classmethod
    def deserialize(cls, data: JsonDict, ctx: DeserMaps) -> FuncIR: ...

INVALID_FUNC_DEF: Final[Incomplete]

def all_values(args: list[Register], blocks: list[BasicBlock]) -> list[Value]:
    """Return the set of all values that may be initialized in the blocks.

    This omits registers that are only read.
    """
def all_values_full(args: list[Register], blocks: list[BasicBlock]) -> list[Value]:
    """Return set of all values that are initialized or accessed."""
