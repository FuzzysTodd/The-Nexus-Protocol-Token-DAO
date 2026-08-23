import enum
from _typeshed import Incomplete
from llvmlite.binding import ffi as ffi
from llvmlite.binding.typeref import TypeRef as TypeRef

class Linkage(enum.IntEnum):
    external: int
    available_externally: int
    linkonce_any: int
    linkonce_odr: int
    linkonce_odr_autohide: int
    weak_any: int
    weak_odr: int
    appending: int
    internal: int
    private: int
    dllimport: int
    dllexport: int
    external_weak: int
    ghost: int
    common: int
    linker_private: int
    linker_private_weak: int

class Visibility(enum.IntEnum):
    default: int
    hidden: int
    protected: int

class StorageClass(enum.IntEnum):
    default: int
    dllimport: int
    dllexport: int

class ValueKind(enum.IntEnum):
    argument: int
    basic_block: int
    memory_use: int
    memory_def: int
    memory_phi: int
    function: int
    global_alias: int
    global_ifunc: int
    global_variable: int
    block_address: int
    constant_expr: int
    constant_array: int
    constant_struct: int
    constant_vector: int
    undef_value: int
    constant_aggregate_zero: int
    constant_data_array: int
    constant_data_vector: int
    constant_int: int
    constant_fp: int
    constant_pointer_null: int
    constant_token_none: int
    metadata_as_value: int
    inline_asm: int
    instruction: int
    poison_value: int

class ValueRef(ffi.ObjectRef):
    """A weak reference to a LLVM value.
    """
    def __init__(self, ptr, kind, parents) -> None: ...
    @property
    def module(self):
        """
        The module this function or global variable value was obtained from.
        """
    @property
    def function(self):
        """
        The function this argument or basic block value was obtained from.
        """
    @property
    def block(self):
        """
        The block this instruction value was obtained from.
        """
    @property
    def instruction(self):
        """
        The instruction this operand value was obtained from.
        """
    @property
    def is_global(self): ...
    @property
    def is_function(self): ...
    @property
    def is_block(self): ...
    @property
    def is_argument(self): ...
    @property
    def is_instruction(self): ...
    @property
    def is_operand(self): ...
    @property
    def is_constant(self): ...
    @property
    def value_kind(self): ...
    @property
    def name(self): ...
    @name.setter
    def name(self, val) -> None: ...
    @property
    def linkage(self): ...
    @linkage.setter
    def linkage(self, value) -> None: ...
    @property
    def visibility(self): ...
    @visibility.setter
    def visibility(self, value) -> None: ...
    @property
    def storage_class(self): ...
    @storage_class.setter
    def storage_class(self, value) -> None: ...
    def add_function_attribute(self, attr) -> None:
        """Only works on function value

        Parameters
        -----------
        attr : str
            attribute name
        """
    @property
    def type(self):
        """
        This value's LLVM type.
        """
    @property
    def is_declaration(self):
        """
        Whether this value (presumably global) is defined in the current
        module.
        """
    @property
    def attributes(self):
        """
        Return an iterator over this value's attributes.
        The iterator will yield a string for each attribute.
        """
    @property
    def blocks(self):
        """
        Return an iterator over this function's blocks.
        The iterator will yield a ValueRef for each block.
        """
    @property
    def arguments(self):
        """
        Return an iterator over this function's arguments.
        The iterator will yield a ValueRef for each argument.
        """
    @property
    def instructions(self):
        """
        Return an iterator over this block's instructions.
        The iterator will yield a ValueRef for each instruction.
        """
    @property
    def operands(self):
        """
        Return an iterator over this instruction's operands.
        The iterator will yield a ValueRef for each operand.
        """
    @property
    def opcode(self): ...
    @property
    def incoming_blocks(self):
        """
        Return an iterator over this phi instruction's incoming blocks.
        The iterator will yield a ValueRef for each block.
        """
    def get_constant_value(self, signed_int: bool = False, round_fp: bool = False):
        """
        Return the constant value, either as a literal (when supported)
        or as a string.

        Parameters
        -----------
        signed_int : bool
            if True and the constant is an integer, returns a signed version
        round_fp : bool
            if True and the constant is a floating point value, rounds the
            result upon accuracy loss (e.g., when querying an fp128 value).
            By default, raises an exception on accuracy loss
        """

class _ValueIterator(ffi.ObjectRef):
    kind: Incomplete
    def __init__(self, ptr, parents) -> None: ...
    def __next__(self): ...
    next = __next__
    def __iter__(self): ...

class _AttributeIterator(ffi.ObjectRef):
    def __next__(self): ...
    next = __next__
    def __iter__(self): ...

class _AttributeListIterator(_AttributeIterator): ...
class _AttributeSetIterator(_AttributeIterator): ...

class _BlocksIterator(_ValueIterator):
    kind: str

class _ArgumentsIterator(_ValueIterator):
    kind: str

class _InstructionsIterator(_ValueIterator):
    kind: str

class _OperandsIterator(_ValueIterator):
    kind: str

class _IncomingBlocksIterator(_ValueIterator):
    kind: str
