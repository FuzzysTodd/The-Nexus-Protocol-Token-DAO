from . import Buffer as Buffer, ExprNodes as ExprNodes, ModuleNode as ModuleNode, Options as Options, PyrexTypes as PyrexTypes
from .Code import TempitaUtilityCode as TempitaUtilityCode, UtilityCode as UtilityCode
from .Errors import CompileError as CompileError, error as error
from .ExprNodes import AttributeNode as AttributeNode, IntNode as IntNode, NameNode as NameNode
from .UtilityCode import CythonUtilityCode as CythonUtilityCode
from _typeshed import Incomplete

START_ERR: str
STOP_ERR: str
STEP_ERR: str
BOTH_CF_ERR: str
INVALID_ERR: str
NOT_CIMPORTED_ERR: str
EXPR_ERR: str
CF_ERR: str
ERR_UNINITIALIZED: str
format_flag: str
memview_c_contiguous: str
memview_f_contiguous: str
memview_any_contiguous: str
memview_full_access: str
memview_strided_access: str
MEMVIEW_DIRECT: str
MEMVIEW_PTR: str
MEMVIEW_FULL: str
MEMVIEW_CONTIG: str
MEMVIEW_STRIDED: str
MEMVIEW_FOLLOW: str
memslice_entry_init: str
memview_name: str
memview_typeptr_cname: str
memview_objstruct_cname: str
memviewslice_cname: str

def put_init_entry(mv_cname, code) -> None: ...
def put_acquire_memoryviewslice(lhs_cname, lhs_type, lhs_pos, rhs, code, have_gil: bool = False, first_assignment: bool = True) -> None:
    """We can avoid decreffing the lhs if we know it is the first assignment"""
def put_assign_to_memviewslice(lhs_cname, rhs, rhs_cname, memviewslicetype, code, have_gil: bool = False, first_assignment: bool = False) -> None: ...
def get_buf_flags(specs): ...
def insert_newaxes(memoryviewtype, n): ...
def broadcast_types(src, dst): ...
def valid_memslice_dtype(dtype, i: int = 0):
    """
    Return whether type dtype can be used as the base type of a
    memoryview slice.

    We support structs, numeric types and objects
    """

class MemoryViewSliceBufferEntry(Buffer.BufferEntry):
    """
    May be used during code generation time to be queried for
    shape/strides/suboffsets attributes, or to perform indexing or slicing.
    """
    entry: Incomplete
    type: Incomplete
    cname: Incomplete
    buf_ptr: Incomplete
    buf_ptr_type: Incomplete
    def __init__(self, entry) -> None: ...
    def get_buf_suboffsetvars(self): ...
    def get_buf_stridevars(self): ...
    def get_buf_shapevars(self): ...
    def generate_buffer_lookup_code(self, code, index_cnames): ...
    def generate_buffer_slice_code(self, code, indices, dst, dst_type, have_gil, have_slices, directives):
        """
        Slice a memoryviewslice.

        indices     - list of index nodes. If not a SliceNode, or NoneNode,
                      then it must be coercible to Py_ssize_t

        Simply call __pyx_memoryview_slice_memviewslice with the right
        arguments, unless the dimension is omitted or a bare ':', in which
        case we copy over the shape/strides/suboffsets attributes directly
        for that dimension.
        """

def empty_slice(pos): ...
def unellipsify(indices, ndim): ...
def get_memoryview_flag(access, packing): ...
def get_is_contig_func_name(contig_type, ndim): ...
def get_is_contig_utility(contig_type, ndim): ...
def slice_iter(slice_type, slice_result, ndim, code, force_strided: bool = False): ...

class SliceIter:
    slice_type: Incomplete
    slice_result: Incomplete
    code: Incomplete
    ndim: Incomplete
    def __init__(self, slice_type, slice_result, ndim, code) -> None: ...

class ContigSliceIter(SliceIter):
    def start_loops(self): ...
    def end_loops(self) -> None: ...

class StridedSliceIter(SliceIter):
    def start_loops(self): ...
    def end_loops(self) -> None: ...

def copy_c_or_fortran_cname(memview): ...
def get_copy_new_utility(pos, from_memview, to_memview): ...
def get_axes_specs(env, axes):
    """
    get_axes_specs(env, axes) -> list of (access, packing) specs for each axis.
    access is one of 'full', 'ptr' or 'direct'
    packing is one of 'contig', 'strided' or 'follow'
    """
def validate_axes(pos, axes): ...
def is_cf_contig(specs): ...
def get_mode(specs): ...

view_constant_to_access_packing: Incomplete

def validate_axes_specs(positions, specs, is_c_contig, is_f_contig) -> None: ...
def load_memview_cy_utility(util_code_name, context: Incomplete | None = None, **kwargs): ...
def load_memview_c_utility(util_code_name, context: Incomplete | None = None, **kwargs): ...
def use_cython_array_utility_code(env) -> None: ...

context: Incomplete
memviewslice_declare_code: Incomplete
atomic_utility: Incomplete
memviewslice_init_code: Incomplete
memviewslice_index_helpers: Incomplete
typeinfo_to_format_code: Incomplete
is_contig_utility: Incomplete
overlapping_utility: Incomplete
copy_contents_new_utility: Incomplete
view_utility_code: Incomplete
view_utility_allowlist: Incomplete
