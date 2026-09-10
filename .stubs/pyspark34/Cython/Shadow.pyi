from _typeshed import Incomplete

__version__: str
basestring = str

class _ArrayType:
    is_array: bool
    subtypes: Incomplete
    dtype: Incomplete
    ndim: Incomplete
    is_c_contig: Incomplete
    is_f_contig: Incomplete
    inner_contig: Incomplete
    broadcasting: Incomplete
    def __init__(self, dtype, ndim, is_c_contig: bool = False, is_f_contig: bool = False, inner_contig: bool = False, broadcasting: Incomplete | None = None) -> None: ...

def index_type(base_type, item):
    """
    Support array type creation by slicing, e.g. double[:, :] specifies
    a 2D strided array of doubles. The syntax is the same as for
    Cython memoryviews.
    """

compiled: bool

def locals(**arg_types): ...
def test_assert_path_exists(*paths): ...
def test_fail_if_path_exists(*paths): ...

class _EmptyDecoratorAndManager:
    def __call__(self, x): ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None) -> None: ...

class _Optimization: ...

cclass: Incomplete

ccall: Incomplete

cfunc: Incomplete
annotation_typing: Incomplete
returns: Incomplete
wraparound: Incomplete
boundscheck: Incomplete
initializedcheck: Incomplete
nonecheck: Incomplete
embedsignature: Incomplete
cdivision: Incomplete
cdivision_warnings: Incomplete
always_allows_keywords: Incomplete
profile: Incomplete
linetrace: Incomplete
infer_types: Incomplete
unraisable_tracebacks: Incomplete
freelist: Incomplete
exceptval: Incomplete
overflowcheck: Incomplete
optimize: Incomplete
final: Incomplete
internal: Incomplete
type_version_tag: Incomplete
no_gc_clear: Incomplete
no_gc: Incomplete
total_ordering: Incomplete
binding: Incomplete

def inline(f, *args, **kwds): ...
def compile(f): ...
def cdiv(a, b): ...
def cmod(a, b): ...
def cast(t, *args, **kwargs): ...
def sizeof(arg): ...
def typeof(arg): ...
def address(arg): ...
def declare(t: Incomplete | None = None, value=..., **kwds): ...

class _nogil:
    """Support for 'with nogil' statement and @nogil decorator.
    """
    def __call__(self, x): ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_class: type[BaseException] | None, exc: BaseException | None, tb: types.TracebackType | None): ...

nogil: Incomplete
gil: Incomplete
with_gil: Incomplete

class CythonMetaType(type):
    def __getitem__(type, ix): ...

CythonTypeObject: Incomplete

class CythonType(CythonTypeObject): ...

class PointerType(CythonType):
    def __init__(self, value: Incomplete | None = None) -> None: ...
    def __getitem__(self, ix): ...
    def __setitem__(self, ix, value) -> None: ...
    def __eq__(self, value): ...

class ArrayType(PointerType):
    def __init__(self, value: Incomplete | None = None) -> None: ...

class StructType(CythonType):
    def __init__(self, *posargs, **data) -> None: ...
    def __setattr__(self, key, value) -> None: ...

class UnionType(CythonType):
    def __init__(self, cast_from=..., **data) -> None: ...
    __dict__: Incomplete
    def __setattr__(self, key, value) -> None: ...

def pointer(basetype): ...
def array(basetype, n): ...
def struct(**members): ...
def union(**members): ...

class typedef(CythonType):
    name: Incomplete
    def __init__(self, type, name: Incomplete | None = None) -> None: ...
    def __call__(self, *arg): ...
    __getitem__ = index_type

class _FusedType(CythonType):
    __getitem__ = index_type

def fused_type(*args): ...

py_int: Incomplete
py_long: Incomplete
py_float: Incomplete
py_complex: Incomplete
int_types: Incomplete
float_types: Incomplete
complex_types: Incomplete
other_types: Incomplete
to_repr: Incomplete
gs: Incomplete
reprname: Incomplete
bint: Incomplete
void: Incomplete
Py_tss_t: Incomplete
NULL: Incomplete
integral: Incomplete
floating: Incomplete
numeric: Incomplete
type_ordering: Incomplete

class CythonDotParallel:
    """
    The cython.parallel module.
    """
    def parallel(self, num_threads: Incomplete | None = None): ...
    def prange(self, start: int = 0, stop: Incomplete | None = None, step: int = 1, nogil: bool = False, schedule: Incomplete | None = None, chunksize: Incomplete | None = None, num_threads: Incomplete | None = None): ...
    def threadid(self): ...

class CythonDotImportedFromElsewhere:
    """
    cython.dataclasses just shadows the standard library modules of the same name
    """
    def __init__(self, module) -> None: ...
    def __getattr__(self, attr): ...

class CythonCImports:
    """
    Simplistic module mock to make cimports sort-of work in Python code.
    """
    def __init__(self, module) -> None: ...
    def __getattr__(self, item): ...

dataclasses: Incomplete
