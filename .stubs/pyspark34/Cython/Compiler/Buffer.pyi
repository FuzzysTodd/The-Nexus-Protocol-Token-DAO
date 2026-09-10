from . import Interpreter as Interpreter, Naming as Naming, Options as Options, PyrexTypes as PyrexTypes, Symtab as Symtab
from .Code import TempitaUtilityCode as TempitaUtilityCode, UtilityCode as UtilityCode
from .Errors import CompileError as CompileError
from .ModuleNode import ModuleNode as ModuleNode
from .UtilityCode import CythonUtilityCode as CythonUtilityCode
from .Visitor import CythonTransform as CythonTransform
from _typeshed import Incomplete

def dedent(text, reindent: int = 0): ...

class IntroduceBufferAuxiliaryVars(CythonTransform):
    buffers_exists: bool
    using_memoryview: bool
    max_ndim: int
    def __call__(self, node): ...
    scope: Incomplete
    def handle_scope(self, node, scope): ...
    def visit_ModuleNode(self, node): ...
    def visit_FuncDefNode(self, node): ...

buffer_options: Incomplete
buffer_defaults: Incomplete
buffer_positional_options_count: int
ERR_BUF_OPTION_UNKNOWN: str
ERR_BUF_TOO_MANY: str
ERR_BUF_DUP: str
ERR_BUF_MISSING: str
ERR_BUF_MODE: str
ERR_BUF_NDIM: str
ERR_BUF_DTYPE: str
ERR_BUF_BOOL: str

def analyse_buffer_options(globalpos, env, posargs, dictargs, defaults: Incomplete | None = None, need_complete: bool = True):
    """
    Must be called during type analysis, as analyse is called
    on the dtype argument.

    posargs and dictargs should consist of a list and a dict
    of tuples (value, pos). Defaults should be a dict of values.

    Returns a dict containing all the options a buffer can have and
    its value (with the positions stripped).
    """

class BufferEntry:
    entry: Incomplete
    type: Incomplete
    cname: Incomplete
    buf_ptr: Incomplete
    buf_ptr_type: Incomplete
    def __init__(self, entry) -> None: ...
    shape: Incomplete
    strides: Incomplete
    suboffsets: Incomplete
    def init_attributes(self) -> None: ...
    def get_buf_suboffsetvars(self): ...
    def get_buf_stridevars(self): ...
    def get_buf_shapevars(self): ...
    def generate_buffer_lookup_code(self, code, index_cnames): ...

def get_flags(buffer_aux, buffer_type): ...
def used_buffer_aux_vars(entry) -> None: ...
def put_unpack_buffer_aux_into_scope(buf_entry, code) -> None: ...
def put_init_vars(entry, code) -> None: ...
def put_acquire_arg_buffer(entry, code, pos) -> None: ...
def put_release_buffer_code(code, entry) -> None: ...
def get_getbuffer_call(code, obj_cname, buffer_aux, buffer_type): ...
def put_assign_to_buffer(lhs_cname, rhs_cname, buf_entry, is_initialized, pos, code) -> None:
    """
    Generate code for reassigning a buffer variables. This only deals with getting
    the buffer auxiliary structure and variables set up correctly, the assignment
    itself and refcounting is the responsibility of the caller.

    However, the assignment operation may throw an exception so that the reassignment
    never happens.

    Depending on the circumstances there are two possible outcomes:
    - Old buffer released, new acquired, rhs assigned to lhs
    - Old buffer released, new acquired which fails, reaqcuire old lhs buffer
      (which may or may not succeed).
    """
def put_buffer_lookup_code(entry, index_signeds, index_cnames, directives, pos, code, negative_indices, in_nogil_context):
    """
    Generates code to process indices and calculate an offset into
    a buffer. Returns a C string which gives a pointer which can be
    read from or written to at will (it is an expression so caller should
    store it in a temporary if it is used more than once).

    As the bounds checking can have any number of combinations of unsigned
    arguments, smart optimizations etc. we insert it directly in the function
    body. The lookup however is delegated to a inline function that is instantiated
    once per ndim (lookup with suboffsets tend to get quite complicated).

    entry is a BufferEntry
    """
def use_bufstruct_declare_code(env) -> None: ...
def buf_lookup_full_code(proto, defin, name, nd) -> None:
    """
    Generates a buffer lookup function for the right number
    of dimensions. The function gives back a void* at the right location.
    """
def buf_lookup_strided_code(proto, defin, name, nd) -> None:
    """
    Generates a buffer lookup function for the right number
    of dimensions. The function gives back a void* at the right location.
    """
def buf_lookup_c_code(proto, defin, name, nd) -> None:
    """
    Similar to strided lookup, but can assume that the last dimension
    doesn't need a multiplication as long as.
    Still we keep the same signature for now.
    """
def buf_lookup_fortran_code(proto, defin, name, nd) -> None:
    """
    Like C lookup, but the first index is optimized instead.
    """
def use_py2_buffer_functions(env) -> None: ...

class GetAndReleaseBufferUtilityCode:
    requires: Incomplete
    is_cython_utility: bool
    def __init__(self) -> None: ...
    def __eq__(self, other): ...
    def __hash__(self): ...
    def get_tree(self, **kwargs) -> None: ...
    def put_code(self, output) -> None: ...

def mangle_dtype_name(dtype): ...
def get_type_information_cname(code, dtype, maxdepth: Incomplete | None = None):
    """
    Output the run-time type information (__Pyx_TypeInfo) for given dtype,
    and return the name of the type info struct.

    Structs with two floats of the same size are encoded as complex numbers.
    One can separate between complex numbers declared as struct or with native
    encoding by inspecting to see if the fields field of the type is
    filled in.
    """
def load_buffer_utility(util_code_name, context: Incomplete | None = None, **kwargs): ...

context: Incomplete
buffer_struct_declare_code: Incomplete
buffer_formats_declare_code: Incomplete
raise_indexerror_code: Incomplete
raise_indexerror_nogil: Incomplete
raise_buffer_fallback_code: Incomplete
acquire_utility_code: Incomplete
buffer_format_check_code: Incomplete
