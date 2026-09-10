import abc
from _typeshed import Incomplete
from abc import abstractmethod
from mypyc.codegen.literals import LiteralValue as LiteralValue
from mypyc.ir.class_ir import ClassIR as ClassIR
from mypyc.ir.func_ir import FuncDecl as FuncDecl, FuncIR as FuncIR
from mypyc.ir.rtypes import RArray as RArray, RInstance as RInstance, RTuple as RTuple, RType as RType, RVoid as RVoid, bit_rprimitive as bit_rprimitive, bool_rprimitive as bool_rprimitive, float_rprimitive as float_rprimitive, int_rprimitive as int_rprimitive, is_bit_rprimitive as is_bit_rprimitive, is_bool_rprimitive as is_bool_rprimitive, is_int_rprimitive as is_int_rprimitive, is_none_rprimitive as is_none_rprimitive, is_pointer_rprimitive as is_pointer_rprimitive, is_short_int_rprimitive as is_short_int_rprimitive, object_rprimitive as object_rprimitive, pointer_rprimitive as pointer_rprimitive, short_int_rprimitive as short_int_rprimitive, void_rtype as void_rtype
from typing import Final, Generic, List, NamedTuple, Sequence, TypeVar

T = TypeVar('T')

class BasicBlock:
    """IR basic block.

    Contains a sequence of Ops and ends with a ControlOp (Goto,
    Branch, Return or Unreachable). Only the last op can be a
    ControlOp.

    All generated Ops live in basic blocks. Basic blocks determine the
    order of evaluation and control flow within a function. A basic
    block is always associated with a single function/method (FuncIR).

    When building the IR, ops that raise exceptions can be included in
    the middle of a basic block, but the exceptions aren't checked.
    Afterwards we perform a transform that inserts explicit checks for
    all error conditions and splits basic blocks accordingly to preserve
    the invariant that a jump, branch or return can only ever appear
    as the final op in a block. Manually inserting error checking ops
    would be boring and error-prone.

    BasicBlocks have an error_handler attribute that determines where
    to jump if an error occurs. If none is specified, an error will
    propagate up out of the function. This is compiled away by the
    `exceptions` module.

    Block labels are used for pretty printing and emitting C code, and
    get filled in by those passes.

    Ops that may terminate the program aren't treated as exits.
    """
    label: Incomplete
    ops: Incomplete
    error_handler: Incomplete
    referenced: bool
    def __init__(self, label: int = -1) -> None: ...
    @property
    def terminated(self) -> bool:
        """Does the block end with a jump, branch or return?

        This should always be true after the basic block has been fully built, but
        this is false during construction.
        """
    @property
    def terminator(self) -> ControlOp:
        """The terminator operation of the block."""

ERR_NEVER: Final[int]
ERR_MAGIC: Final[int]
ERR_FALSE: Final[int]
ERR_ALWAYS: Final[int]
ERR_MAGIC_OVERLAPPING: Final[int]
NO_TRACEBACK_LINE_NO: int

class Value:
    """Abstract base class for all IR values.

    These include references to registers, literals, and all
    operations (Ops), such as assignments, calls and branches.

    Values are often used as inputs of Ops. Register can be used as an
    assignment target.

    A Value is part of the IR being compiled if it's included in a BasicBlock
    that is reachable from a FuncIR (i.e., is part of a function).

    See also: Op is a subclass of Value that is the base class of all
    operations.
    """
    line: int
    type: RType
    is_borrowed: bool
    @property
    def is_void(self) -> bool: ...

class Register(Value):
    """A Register holds a value of a specific type, and it can be read and mutated.

    A Register is always local to a function. Each local variable maps
    to a Register, and they are also used for some (but not all)
    temporary values.

    Note that the term 'register' is overloaded and is sometimes used
    to refer to arbitrary Values (for example, in RegisterOp).
    """
    type: Incomplete
    name: Incomplete
    is_arg: Incomplete
    is_borrowed: Incomplete
    line: Incomplete
    def __init__(self, type: RType, name: str = '', is_arg: bool = False, line: int = -1) -> None: ...
    @property
    def is_void(self) -> bool: ...

class Integer(Value):
    """Short integer literal.

    Integer literals are treated as constant values and are generally
    not included in data flow analyses and such, unlike Register and
    Op subclasses.

    Integer can represent multiple types:

     * Short tagged integers (short_int_primitive type; the tag bit is clear)
     * Ordinary fixed-width integers (e.g., int32_rprimitive)
     * Values of other unboxed primitive types that are represented as integers
       (none_rprimitive, bool_rprimitive)
     * Null pointers (value 0) of various types, including object_rprimitive
    """
    value: Incomplete
    type: Incomplete
    line: Incomplete
    def __init__(self, value: int, rtype: RType = ..., line: int = -1) -> None: ...
    def numeric_value(self) -> int: ...

class Float(Value):
    """Float literal.

    Floating point literals are treated as constant values and are generally
    not included in data flow analyses and such, unlike Register and
    Op subclasses.
    """
    value: Incomplete
    type: Incomplete
    line: Incomplete
    def __init__(self, value: float, line: int = -1) -> None: ...

class Op(Value, metaclass=abc.ABCMeta):
    """Abstract base class for all IR operations.

    Each operation must be stored in a BasicBlock (in 'ops') to be
    active in the IR. This is different from non-Op values, including
    Register and Integer, where a reference from an active Op is
    sufficient to be considered active.

    In well-formed IR an active Op has no references to inactive ops
    or ops used in another function.
    """
    line: Incomplete
    def __init__(self, line: int) -> None: ...
    def can_raise(self) -> bool: ...
    @abstractmethod
    def sources(self) -> list[Value]:
        """All the values the op may read."""
    def stolen(self) -> list[Value]:
        """Return arguments that have a reference count stolen by this op"""
    def unique_sources(self) -> list[Value]: ...
    @abstractmethod
    def accept(self, visitor: OpVisitor[T]) -> T: ...

class BaseAssign(Op, metaclass=abc.ABCMeta):
    """Base class for ops that assign to a register."""
    dest: Incomplete
    def __init__(self, dest: Register, line: int = -1) -> None: ...

class Assign(BaseAssign):
    """Assign a value to a Register (dest = src)."""
    error_kind = ERR_NEVER
    src: Incomplete
    def __init__(self, dest: Register, src: Value, line: int = -1) -> None: ...
    def sources(self) -> list[Value]: ...
    def stolen(self) -> list[Value]: ...
    def accept(self, visitor: OpVisitor[T]) -> T: ...

class AssignMulti(BaseAssign):
    """Assign multiple values to a Register (dest = src1, src2, ...).

    This is used to initialize RArray values. It's provided to avoid
    very verbose IR for common vectorcall operations.

    Note that this interacts atypically with reference counting. We
    assume that each RArray register is initialized exactly once
    with this op.
    """
    error_kind = ERR_NEVER
    src: Incomplete
    def __init__(self, dest: Register, src: list[Value], line: int = -1) -> None: ...
    def sources(self) -> list[Value]: ...
    def stolen(self) -> list[Value]: ...
    def accept(self, visitor: OpVisitor[T]) -> T: ...

class ControlOp(Op, metaclass=abc.ABCMeta):
    """Control flow operation."""
    def targets(self) -> Sequence[BasicBlock]:
        """Get all basic block targets of the control operation."""
    def set_target(self, i: int, new: BasicBlock) -> None:
        """Update a basic block target."""

class Goto(ControlOp):
    """Unconditional jump."""
    error_kind = ERR_NEVER
    label: Incomplete
    def __init__(self, label: BasicBlock, line: int = -1) -> None: ...
    def targets(self) -> Sequence[BasicBlock]: ...
    def set_target(self, i: int, new: BasicBlock) -> None: ...
    def sources(self) -> list[Value]: ...
    def accept(self, visitor: OpVisitor[T]) -> T: ...

class Branch(ControlOp):
    """Branch based on a value.

    If op is BOOL, branch based on a bit/bool value:
       if [not] r1 goto L1 else goto L2

    If op is IS_ERROR, branch based on whether there is an error value:
       if [not] is_error(r1) goto L1 else goto L2
    """
    error_kind = ERR_NEVER
    BOOL: Final[int]
    IS_ERROR: Final[int]
    value: Incomplete
    true: Incomplete
    false: Incomplete
    op: Incomplete
    negated: bool
    traceback_entry: Incomplete
    rare: Incomplete
    def __init__(self, value: Value, true_label: BasicBlock, false_label: BasicBlock, op: int, line: int = -1, *, rare: bool = False) -> None: ...
    def targets(self) -> Sequence[BasicBlock]: ...
    def set_target(self, i: int, new: BasicBlock) -> None: ...
    def sources(self) -> list[Value]: ...
    def invert(self) -> None: ...
    def accept(self, visitor: OpVisitor[T]) -> T: ...

class Return(ControlOp):
    """Return a value from a function."""
    error_kind = ERR_NEVER
    value: Incomplete
    def __init__(self, value: Value, line: int = -1) -> None: ...
    def sources(self) -> list[Value]: ...
    def stolen(self) -> list[Value]: ...
    def accept(self, visitor: OpVisitor[T]) -> T: ...

class Unreachable(ControlOp):
    """Mark the end of basic block as unreachable.

    This is sometimes necessary when the end of a basic block is never
    reached. This can also be explicitly added to the end of non-None
    returning functions (in None-returning function we can just return
    None).

    Mypy statically guarantees that the end of the function is not
    unreachable if there is not a return statement.

    This prevents the block formatter from being confused due to lack
    of a leave and also leaves a nifty note in the IR. It is not
    generally processed by visitors.
    """
    error_kind = ERR_NEVER
    def __init__(self, line: int = -1) -> None: ...
    def sources(self) -> list[Value]: ...
    def accept(self, visitor: OpVisitor[T]) -> T: ...

class RegisterOp(Op, metaclass=abc.ABCMeta):
    """Abstract base class for operations that can be written as r1 = f(r2, ..., rn).

    Takes some values, performs an operation, and generates an output
    (unless the 'type' attribute is void_rtype, which is the default).
    Other ops can refer to the result of the Op by referring to the Op
    instance. This doesn't do any explicit control flow, but can raise an
    error.

    Note that the operands can be arbitrary Values, not just Register
    instances, even though the naming may suggest otherwise.
    """
    error_kind: int
    def __init__(self, line: int) -> None: ...
    def can_raise(self) -> bool: ...

class IncRef(RegisterOp):
    """Increase reference count (inc_ref src)."""
    error_kind = ERR_NEVER
    src: Incomplete
    def __init__(self, src: Value, line: int = -1) -> None: ...
    def sources(self) -> list[Value]: ...
    def accept(self, visitor: OpVisitor[T]) -> T: ...

class DecRef(RegisterOp):
    """Decrease reference count and free object if zero (dec_ref src).

    The is_xdec flag says to use an XDECREF, which checks if the
    pointer is NULL first.
    """
    error_kind = ERR_NEVER
    src: Incomplete
    is_xdec: Incomplete
    def __init__(self, src: Value, is_xdec: bool = False, line: int = -1) -> None: ...
    def sources(self) -> list[Value]: ...
    def accept(self, visitor: OpVisitor[T]) -> T: ...

class Call(RegisterOp):
    """Native call f(arg, ...).

    The call target can be a module-level function or a class.
    """
    fn: Incomplete
    args: Incomplete
    type: Incomplete
    error_kind: Incomplete
    def __init__(self, fn: FuncDecl, args: Sequence[Value], line: int) -> None: ...
    def sources(self) -> list[Value]: ...
    def accept(self, visitor: OpVisitor[T]) -> T: ...

class MethodCall(RegisterOp):
    """Native method call obj.method(arg, ...)"""
    obj: Incomplete
    method: Incomplete
    args: Incomplete
    receiver_type: Incomplete
    type: Incomplete
    error_kind: Incomplete
    def __init__(self, obj: Value, method: str, args: list[Value], line: int = -1) -> None: ...
    def sources(self) -> list[Value]: ...
    def accept(self, visitor: OpVisitor[T]) -> T: ...

class LoadErrorValue(RegisterOp):
    """Load an error value.

    Each type has one reserved value that signals an error (exception). This
    loads the error value for a specific type.
    """
    error_kind = ERR_NEVER
    type: Incomplete
    is_borrowed: Incomplete
    undefines: Incomplete
    def __init__(self, rtype: RType, line: int = -1, is_borrowed: bool = False, undefines: bool = False) -> None: ...
    def sources(self) -> list[Value]: ...
    def accept(self, visitor: OpVisitor[T]) -> T: ...

class LoadLiteral(RegisterOp):
    """Load a Python literal object (dest = 'foo' / b'foo' / ...).

    This is used to load a static PyObject * value corresponding to
    a literal of one of the supported types.

    Tuple / frozenset literals must contain only valid literal values as items.

    NOTE: You can use this to load boxed (Python) int objects. Use
          Integer to load unboxed, tagged integers or fixed-width,
          low-level integers.

          For int literals, both int_rprimitive (CPyTagged) and
          object_primitive (PyObject *) are supported as rtype. However,
          when using int_rprimitive, the value must *not* be small enough
          to fit in an unboxed integer.
    """
    error_kind = ERR_NEVER
    is_borrowed: bool
    value: Incomplete
    type: Incomplete
    def __init__(self, value: LiteralValue, rtype: RType) -> None: ...
    def sources(self) -> list[Value]: ...
    def accept(self, visitor: OpVisitor[T]) -> T: ...

class GetAttr(RegisterOp):
    """obj.attr (for a native object)"""
    error_kind = ERR_MAGIC
    obj: Incomplete
    attr: Incomplete
    class_type: Incomplete
    type: Incomplete
    is_borrowed: Incomplete
    def __init__(self, obj: Value, attr: str, line: int, *, borrow: bool = False) -> None: ...
    def sources(self) -> list[Value]: ...
    def accept(self, visitor: OpVisitor[T]) -> T: ...

class SetAttr(RegisterOp):
    """obj.attr = src (for a native object)

    Steals the reference to src.
    """
    error_kind = ERR_FALSE
    obj: Incomplete
    attr: Incomplete
    src: Incomplete
    class_type: Incomplete
    type: Incomplete
    is_init: bool
    def __init__(self, obj: Value, attr: str, src: Value, line: int) -> None: ...
    def mark_as_initializer(self) -> None: ...
    def sources(self) -> list[Value]: ...
    def stolen(self) -> list[Value]: ...
    def accept(self, visitor: OpVisitor[T]) -> T: ...

NAMESPACE_STATIC: Final[str]
NAMESPACE_TYPE: Final[str]
NAMESPACE_MODULE: Final[str]

class LoadStatic(RegisterOp):
    """Load a static name (name :: static).

    Load a C static variable/pointer. The namespace for statics is shared
    for the entire compilation group. You can optionally provide a module
    name and a sub-namespace identifier for additional namespacing to avoid
    name conflicts. The static namespace does not overlap with other C names,
    since the final C name will get a prefix, so conflicts only must be
    avoided with other statics.
    """
    error_kind = ERR_NEVER
    is_borrowed: bool
    identifier: Incomplete
    module_name: Incomplete
    namespace: Incomplete
    type: Incomplete
    ann: Incomplete
    def __init__(self, type: RType, identifier: str, module_name: str | None = None, namespace: str = ..., line: int = -1, ann: object = None) -> None: ...
    def sources(self) -> list[Value]: ...
    def accept(self, visitor: OpVisitor[T]) -> T: ...

class InitStatic(RegisterOp):
    """static = value :: static

    Initialize a C static variable/pointer. See everything in LoadStatic.
    """
    error_kind = ERR_NEVER
    identifier: Incomplete
    module_name: Incomplete
    namespace: Incomplete
    value: Incomplete
    def __init__(self, value: Value, identifier: str, module_name: str | None = None, namespace: str = ..., line: int = -1) -> None: ...
    def sources(self) -> list[Value]: ...
    def accept(self, visitor: OpVisitor[T]) -> T: ...

class TupleSet(RegisterOp):
    """dest = (reg, ...) (for fixed-length tuple)"""
    error_kind = ERR_NEVER
    items: Incomplete
    tuple_type: Incomplete
    type: Incomplete
    def __init__(self, items: list[Value], line: int) -> None: ...
    def sources(self) -> list[Value]: ...
    def stolen(self) -> list[Value]: ...
    def accept(self, visitor: OpVisitor[T]) -> T: ...

class TupleGet(RegisterOp):
    """Get item of a fixed-length tuple (src[index])."""
    error_kind = ERR_NEVER
    src: Incomplete
    index: Incomplete
    type: Incomplete
    is_borrowed: Incomplete
    def __init__(self, src: Value, index: int, line: int = -1, *, borrow: bool = False) -> None: ...
    def sources(self) -> list[Value]: ...
    def accept(self, visitor: OpVisitor[T]) -> T: ...

class Cast(RegisterOp):
    """cast(type, src)

    Perform a runtime type check (no representation or value conversion).

    DO NOT increment reference counts.
    """
    error_kind = ERR_MAGIC
    src: Incomplete
    type: Incomplete
    is_borrowed: Incomplete
    def __init__(self, src: Value, typ: RType, line: int, *, borrow: bool = False) -> None: ...
    def sources(self) -> list[Value]: ...
    def stolen(self) -> list[Value]: ...
    def accept(self, visitor: OpVisitor[T]) -> T: ...

class Box(RegisterOp):
    """box(type, src)

    This converts from a potentially unboxed representation to a straight Python object.
    Only supported for types with an unboxed representation.
    """
    error_kind = ERR_NEVER
    src: Incomplete
    type: Incomplete
    is_borrowed: bool
    def __init__(self, src: Value, line: int = -1) -> None: ...
    def sources(self) -> list[Value]: ...
    def stolen(self) -> list[Value]: ...
    def accept(self, visitor: OpVisitor[T]) -> T: ...

class Unbox(RegisterOp):
    """unbox(type, src)

    This is similar to a cast, but it also changes to a (potentially) unboxed runtime
    representation. Only supported for types with an unboxed representation.
    """
    src: Incomplete
    type: Incomplete
    error_kind: Incomplete
    def __init__(self, src: Value, typ: RType, line: int) -> None: ...
    def sources(self) -> list[Value]: ...
    def accept(self, visitor: OpVisitor[T]) -> T: ...

class RaiseStandardError(RegisterOp):
    """Raise built-in exception with an optional error string.

    We have a separate opcode for this for convenience and to
    generate smaller, more idiomatic C code.
    """
    error_kind = ERR_FALSE
    VALUE_ERROR: Final[str]
    ASSERTION_ERROR: Final[str]
    STOP_ITERATION: Final[str]
    UNBOUND_LOCAL_ERROR: Final[str]
    RUNTIME_ERROR: Final[str]
    NAME_ERROR: Final[str]
    ZERO_DIVISION_ERROR: Final[str]
    class_name: Incomplete
    value: Incomplete
    type: Incomplete
    def __init__(self, class_name: str, value: str | Value | None, line: int) -> None: ...
    def sources(self) -> list[Value]: ...
    def accept(self, visitor: OpVisitor[T]) -> T: ...
StealsDescription = bool | List[bool]

class CallC(RegisterOp):
    """result = function(arg0, arg1, ...)

    Call a C function that is not a compiled/native function (for
    example, a Python C API function). Use Call to call native
    functions.
    """
    error_kind: Incomplete
    function_name: Incomplete
    args: Incomplete
    type: Incomplete
    steals: Incomplete
    is_borrowed: Incomplete
    var_arg_idx: Incomplete
    def __init__(self, function_name: str, args: list[Value], ret_type: RType, steals: StealsDescription, is_borrowed: bool, error_kind: int, line: int, var_arg_idx: int = -1) -> None: ...
    def sources(self) -> list[Value]: ...
    def stolen(self) -> list[Value]: ...
    def accept(self, visitor: OpVisitor[T]) -> T: ...

class Truncate(RegisterOp):
    """result = truncate src from src_type to dst_type

    Truncate a value from type with more bits to type with less bits.

    dst_type and src_type can be native integer types, bools or tagged
    integers. Tagged integers should have the tag bit unset.
    """
    error_kind = ERR_NEVER
    src: Incomplete
    type: Incomplete
    src_type: Incomplete
    def __init__(self, src: Value, dst_type: RType, line: int = -1) -> None: ...
    def sources(self) -> list[Value]: ...
    def stolen(self) -> list[Value]: ...
    def accept(self, visitor: OpVisitor[T]) -> T: ...

class Extend(RegisterOp):
    """result = extend src from src_type to dst_type

    Extend a value from a type with fewer bits to a type with more bits.

    dst_type and src_type can be native integer types, bools or tagged
    integers. Tagged integers should have the tag bit unset.

    If 'signed' is true, perform sign extension. Otherwise, the result will be
    zero extended.
    """
    error_kind = ERR_NEVER
    src: Incomplete
    type: Incomplete
    src_type: Incomplete
    signed: Incomplete
    def __init__(self, src: Value, dst_type: RType, signed: bool, line: int = -1) -> None: ...
    def sources(self) -> list[Value]: ...
    def stolen(self) -> list[Value]: ...
    def accept(self, visitor: OpVisitor[T]) -> T: ...

class LoadGlobal(RegisterOp):
    """Load a low-level global variable/pointer.

    Note that can't be used to directly load Python module-level
    global variable, since they are stored in a globals dictionary
    and accessed using dictionary operations.
    """
    error_kind = ERR_NEVER
    is_borrowed: bool
    identifier: Incomplete
    type: Incomplete
    ann: Incomplete
    def __init__(self, type: RType, identifier: str, line: int = -1, ann: object = None) -> None: ...
    def sources(self) -> list[Value]: ...
    def accept(self, visitor: OpVisitor[T]) -> T: ...

class IntOp(RegisterOp):
    """Binary arithmetic or bitwise op on integer operands (e.g., r1 = r2 + r3).

    These ops are low-level and are similar to the corresponding C
    operations.

    The left and right values must have low-level integer types with
    compatible representations. Fixed-width integers, short_int_rprimitive,
    bool_rprimitive and bit_rprimitive are supported.

    For tagged (arbitrary-precision) integer ops look at mypyc.primitives.int_ops.
    """
    error_kind = ERR_NEVER
    ADD: Final[int]
    SUB: Final[int]
    MUL: Final[int]
    DIV: Final[int]
    MOD: Final[int]
    AND: Final[int]
    OR: Final[int]
    XOR: Final[int]
    LEFT_SHIFT: Final[int]
    RIGHT_SHIFT: Final[int]
    op_str: Final[Incomplete]
    type: Incomplete
    lhs: Incomplete
    rhs: Incomplete
    op: Incomplete
    def __init__(self, type: RType, lhs: Value, rhs: Value, op: int, line: int = -1) -> None: ...
    def sources(self) -> list[Value]: ...
    def accept(self, visitor: OpVisitor[T]) -> T: ...

int_op_to_id: Final[Incomplete]

class ComparisonOp(RegisterOp):
    """Low-level comparison op for integers and pointers.

    Both unsigned and signed comparisons are supported. Supports
    comparisons between fixed-width integer types and pointer types.
    The operands should have matching sizes.

    The result is always a bit (representing a boolean).

    Python semantics, such as calling __eq__, are not supported.
    """
    error_kind = ERR_NEVER
    EQ: Final[int]
    NEQ: Final[int]
    SLT: Final[int]
    SGT: Final[int]
    SLE: Final[int]
    SGE: Final[int]
    ULT: Final[int]
    UGT: Final[int]
    ULE: Final[int]
    UGE: Final[int]
    op_str: Final[Incomplete]
    signed_ops: Final[Incomplete]
    unsigned_ops: Final[Incomplete]
    type: Incomplete
    lhs: Incomplete
    rhs: Incomplete
    op: Incomplete
    def __init__(self, lhs: Value, rhs: Value, op: int, line: int = -1) -> None: ...
    def sources(self) -> list[Value]: ...
    def accept(self, visitor: OpVisitor[T]) -> T: ...

class FloatOp(RegisterOp):
    """Binary float arithmetic op (e.g., r1 = r2 + r3).

    These ops are low-level and are similar to the corresponding C
    operations (and somewhat different from Python operations).

    The left and right values must be floats.
    """
    error_kind = ERR_NEVER
    ADD: Final[int]
    SUB: Final[int]
    MUL: Final[int]
    DIV: Final[int]
    MOD: Final[int]
    op_str: Final[Incomplete]
    type: Incomplete
    lhs: Incomplete
    rhs: Incomplete
    op: Incomplete
    def __init__(self, lhs: Value, rhs: Value, op: int, line: int = -1) -> None: ...
    def sources(self) -> list[Value]: ...
    def accept(self, visitor: OpVisitor[T]) -> T: ...

float_op_to_id: Final[Incomplete]

class FloatNeg(RegisterOp):
    """Float negation op (r1 = -r2)."""
    error_kind = ERR_NEVER
    type: Incomplete
    src: Incomplete
    def __init__(self, src: Value, line: int = -1) -> None: ...
    def sources(self) -> list[Value]: ...
    def accept(self, visitor: OpVisitor[T]) -> T: ...

class FloatComparisonOp(RegisterOp):
    """Low-level comparison op for floats."""
    error_kind = ERR_NEVER
    EQ: Final[int]
    NEQ: Final[int]
    LT: Final[int]
    GT: Final[int]
    LE: Final[int]
    GE: Final[int]
    op_str: Final[Incomplete]
    type: Incomplete
    lhs: Incomplete
    rhs: Incomplete
    op: Incomplete
    def __init__(self, lhs: Value, rhs: Value, op: int, line: int = -1) -> None: ...
    def sources(self) -> list[Value]: ...
    def accept(self, visitor: OpVisitor[T]) -> T: ...

float_comparison_op_to_id: Final[Incomplete]

class LoadMem(RegisterOp):
    """Read a memory location: result = *(type *)src.

    Attributes:
      type: Type of the read value
      src: Pointer to memory to read
    """
    error_kind = ERR_NEVER
    type: Incomplete
    src: Incomplete
    is_borrowed: bool
    def __init__(self, type: RType, src: Value, line: int = -1) -> None: ...
    def sources(self) -> list[Value]: ...
    def accept(self, visitor: OpVisitor[T]) -> T: ...

class SetMem(Op):
    """Write to a memory location: *(type *)dest = src

    Attributes:
      type: Type of the written value
      dest: Pointer to memory to write
      src: Source value
    """
    error_kind = ERR_NEVER
    type: Incomplete
    dest_type: Incomplete
    src: Incomplete
    dest: Incomplete
    def __init__(self, type: RType, dest: Value, src: Value, line: int = -1) -> None: ...
    def sources(self) -> list[Value]: ...
    def stolen(self) -> list[Value]: ...
    def accept(self, visitor: OpVisitor[T]) -> T: ...

class GetElementPtr(RegisterOp):
    """Get the address of a struct element.

    Note that you may need to use KeepAlive to avoid the struct
    being freed, if it's reference counted, such as PyObject *.
    """
    error_kind = ERR_NEVER
    type: Incomplete
    src: Incomplete
    src_type: Incomplete
    field: Incomplete
    def __init__(self, src: Value, src_type: RType, field: str, line: int = -1) -> None: ...
    def sources(self) -> list[Value]: ...
    def accept(self, visitor: OpVisitor[T]) -> T: ...

class LoadAddress(RegisterOp):
    """Get the address of a value: result = (type)&src

    Attributes:
      type: Type of the loaded address(e.g. ptr/object_ptr)
      src: Source value (str for globals like 'PyList_Type',
           Register for temporary values or locals, LoadStatic
           for statics.)
    """
    error_kind = ERR_NEVER
    is_borrowed: bool
    type: Incomplete
    src: Incomplete
    def __init__(self, type: RType, src: str | Register | LoadStatic, line: int = -1) -> None: ...
    def sources(self) -> list[Value]: ...
    def accept(self, visitor: OpVisitor[T]) -> T: ...

class KeepAlive(RegisterOp):
    '''A no-op operation that ensures source values aren\'t freed.

    This is sometimes useful to avoid decref when a reference is still
    being held but not seen by the compiler.

    A typical use case is like this (C-like pseudocode):

      ptr = &x.item
      r = *ptr
      keep_alive x  # x must not be freed here
      # x may be freed here

    If we didn\'t have "keep_alive x", x could be freed immediately
    after taking the address of \'item\', resulting in a read after free
    on the second line.

    If \'steal\' is true, the value is considered to be stolen at
    this op, i.e. it won\'t be decref\'d. You need to ensure that
    the value is freed otherwise, perhaps by using borrowing
    followed by Unborrow.

    Be careful with steal=True -- this can cause memory leaks.
    '''
    error_kind = ERR_NEVER
    src: Incomplete
    steal: Incomplete
    def __init__(self, src: list[Value], *, steal: bool = False) -> None: ...
    def sources(self) -> list[Value]: ...
    def stolen(self) -> list[Value]: ...
    def accept(self, visitor: OpVisitor[T]) -> T: ...

class Unborrow(RegisterOp):
    '''A no-op op to create a regular reference from a borrowed one.

    Borrowed references can only be used temporarily and the reference
    counts won\'t be managed. This value will be refcounted normally.

    This is mainly useful if you split an aggregate value, such as
    a tuple, into components using borrowed values (to avoid increfs),
    and want to treat the components as sharing the original managed
    reference. You\'ll also need to use KeepAlive with steal=True to
    "consume" the original tuple reference:

      # t is a 2-tuple
      r0 = borrow t[0]
      r1 = borrow t[1]
      r2 = unborrow r0
      r3 = unborrow r1
      # now (r2, r3) represent the tuple as separate items, and the
      # original tuple can be considered dead and available to be
      # stolen
      keep_alive steal t

    Be careful with this -- this can easily cause double freeing.
    '''
    error_kind = ERR_NEVER
    src: Incomplete
    type: Incomplete
    def __init__(self, src: Value) -> None: ...
    def sources(self) -> list[Value]: ...
    def stolen(self) -> list[Value]: ...
    def accept(self, visitor: OpVisitor[T]) -> T: ...

class OpVisitor(Generic[T], metaclass=abc.ABCMeta):
    """Generic visitor over ops (uses the visitor design pattern)."""
    @abstractmethod
    def visit_goto(self, op: Goto) -> T: ...
    @abstractmethod
    def visit_branch(self, op: Branch) -> T: ...
    @abstractmethod
    def visit_return(self, op: Return) -> T: ...
    @abstractmethod
    def visit_unreachable(self, op: Unreachable) -> T: ...
    @abstractmethod
    def visit_assign(self, op: Assign) -> T: ...
    @abstractmethod
    def visit_assign_multi(self, op: AssignMulti) -> T: ...
    @abstractmethod
    def visit_load_error_value(self, op: LoadErrorValue) -> T: ...
    @abstractmethod
    def visit_load_literal(self, op: LoadLiteral) -> T: ...
    @abstractmethod
    def visit_get_attr(self, op: GetAttr) -> T: ...
    @abstractmethod
    def visit_set_attr(self, op: SetAttr) -> T: ...
    @abstractmethod
    def visit_load_static(self, op: LoadStatic) -> T: ...
    @abstractmethod
    def visit_init_static(self, op: InitStatic) -> T: ...
    @abstractmethod
    def visit_tuple_get(self, op: TupleGet) -> T: ...
    @abstractmethod
    def visit_tuple_set(self, op: TupleSet) -> T: ...
    def visit_inc_ref(self, op: IncRef) -> T: ...
    def visit_dec_ref(self, op: DecRef) -> T: ...
    @abstractmethod
    def visit_call(self, op: Call) -> T: ...
    @abstractmethod
    def visit_method_call(self, op: MethodCall) -> T: ...
    @abstractmethod
    def visit_cast(self, op: Cast) -> T: ...
    @abstractmethod
    def visit_box(self, op: Box) -> T: ...
    @abstractmethod
    def visit_unbox(self, op: Unbox) -> T: ...
    @abstractmethod
    def visit_raise_standard_error(self, op: RaiseStandardError) -> T: ...
    @abstractmethod
    def visit_call_c(self, op: CallC) -> T: ...
    @abstractmethod
    def visit_truncate(self, op: Truncate) -> T: ...
    @abstractmethod
    def visit_extend(self, op: Extend) -> T: ...
    @abstractmethod
    def visit_load_global(self, op: LoadGlobal) -> T: ...
    @abstractmethod
    def visit_int_op(self, op: IntOp) -> T: ...
    @abstractmethod
    def visit_comparison_op(self, op: ComparisonOp) -> T: ...
    @abstractmethod
    def visit_float_op(self, op: FloatOp) -> T: ...
    @abstractmethod
    def visit_float_neg(self, op: FloatNeg) -> T: ...
    @abstractmethod
    def visit_float_comparison_op(self, op: FloatComparisonOp) -> T: ...
    @abstractmethod
    def visit_load_mem(self, op: LoadMem) -> T: ...
    @abstractmethod
    def visit_set_mem(self, op: SetMem) -> T: ...
    @abstractmethod
    def visit_get_element_ptr(self, op: GetElementPtr) -> T: ...
    @abstractmethod
    def visit_load_address(self, op: LoadAddress) -> T: ...
    @abstractmethod
    def visit_keep_alive(self, op: KeepAlive) -> T: ...
    @abstractmethod
    def visit_unborrow(self, op: Unborrow) -> T: ...

class DeserMaps(NamedTuple):
    classes: dict[str, ClassIR]
    functions: dict[str, FuncIR]
