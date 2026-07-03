from _typeshed import Incomplete
from numba.core import errors as errors, serialize as serialize, utils as utils
from numba.core.utils import PYVERSION as PYVERSION
from typing import NamedTuple

class opcode_info(NamedTuple):
    argsize: Incomplete

def get_function_object(obj):
    '''
    Objects that wraps function should provide a "__numba__" magic attribute
    that contains a name of an attribute that contains the actual python
    function object.
    '''
def get_code_object(obj):
    """Shamelessly borrowed from llpython"""

JREL_OPS: Incomplete
JABS_OPS: Incomplete
JUMP_OPS: Incomplete
TERM_OPS: Incomplete
EXTENDED_ARG: Incomplete
HAVE_ARGUMENT: Incomplete

class ByteCodeInst:
    """
    Attributes
    ----------
    - offset:
        byte offset of opcode
    - opcode:
        opcode integer value
    - arg:
        instruction arg
    - lineno:
        -1 means unknown
    """
    offset: Incomplete
    next: Incomplete
    opcode: Incomplete
    opname: Incomplete
    arg: Incomplete
    lineno: int
    def __init__(self, offset, opcode, arg, nextoffset) -> None: ...
    @property
    def is_jump(self): ...
    @property
    def is_terminator(self): ...
    def get_jump_target(self): ...
    @property
    def block_effect(self):
        """Effect of the block stack
        Returns +1 (push), 0 (none) or -1 (pop)
        """

CODE_LEN: int
ARG_LEN: int
NO_ARG_LEN: int
OPCODE_NOP: Incomplete

class ByteCodeIter:
    code: Incomplete
    iter: Incomplete
    def __init__(self, code) -> None: ...
    def __iter__(self): ...
    def next(self): ...
    __next__ = next
    def read_arg(self, size): ...

class _ByteCode:
    """
    The decoded bytecode of a function, and related information.
    """
    func_id: Incomplete
    co_names: Incomplete
    co_varnames: Incomplete
    co_consts: Incomplete
    co_cellvars: Incomplete
    co_freevars: Incomplete
    table: Incomplete
    labels: Incomplete
    def __init__(self, func_id) -> None: ...
    def __iter__(self): ...
    def __getitem__(self, offset): ...
    def __contains__(self, offset) -> bool: ...
    def dump(self): ...
    def get_used_globals(self):
        """
        Get a {name: value} map of the globals used by this code
        object and any nested code objects.
        """

class ByteCodePy311(_ByteCode):
    exception_entries: Incomplete
    def __init__(self, func_id) -> None: ...
    def find_exception_entry(self, offset):
        """
        Returns the exception entry for the given instruction offset
        """
ByteCode = ByteCodePy311

class FunctionIdentity(serialize.ReduceMixin):
    """
    A function's identity and metadata.

    Note this typically represents a function whose bytecode is
    being compiled, not necessarily the top-level user function
    (the two might be distinct, e.g. in the `@generated_jit` case).
    """
    func: Incomplete
    func_qualname: Incomplete
    func_name: Incomplete
    code: Incomplete
    module: Incomplete
    modname: Incomplete
    is_generator: Incomplete
    pysig: Incomplete
    filename: Incomplete
    firstlineno: Incomplete
    arg_count: Incomplete
    arg_names: Incomplete
    unique_name: Incomplete
    unique_id: Incomplete
    @classmethod
    def from_function(cls, pyfunc):
        """
        Create the FunctionIdentity of the given function.
        """
    def derive(self):
        """Copy the object and increment the unique counter.
        """
