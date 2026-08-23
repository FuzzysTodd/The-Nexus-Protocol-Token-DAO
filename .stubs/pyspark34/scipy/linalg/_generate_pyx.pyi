from _typeshed import Incomplete

BASE_DIR: Incomplete
fortran_types: Incomplete
c_types: Incomplete

def arg_names_and_types(args): ...

pyx_func_template: str
npy_types: Incomplete

def arg_casts(arg): ...
def pyx_decl_func(name, ret_type, args, header_name): ...

pyx_sub_template: str

def pyx_decl_sub(name, args, header_name): ...

blas_pyx_preamble: str

def make_blas_pyx_preamble(all_sigs): ...

lapack_pyx_preamble: str

def make_lapack_pyx_preamble(all_sigs): ...

blas_py_wrappers: str

def generate_blas_pyx(func_sigs, sub_sigs, all_sigs, header_name): ...

lapack_py_wrappers: str

def generate_lapack_pyx(func_sigs, sub_sigs, all_sigs, header_name): ...

pxd_template: str

def pxd_decl(name, ret_type, args): ...

blas_pxd_preamble: str

def generate_blas_pxd(all_sigs): ...

lapack_pxd_preamble: str

def generate_lapack_pxd(all_sigs): ...

fortran_template: str
dims: Incomplete
xy_specialized_dims: Incomplete
a_specialized_dims: Incomplete
special_cases: Incomplete

def process_fortran_name(name, funcname): ...
def called_name(name): ...
def fort_subroutine_wrapper(name, ret_type, args): ...
def generate_fortran(func_sigs): ...
def make_c_args(args): ...

c_func_template: str

def c_func_decl(name, return_type, args): ...

c_sub_template: str

def c_sub_decl(name, return_type, args): ...

c_preamble: str
lapack_decls: str
cpp_guard: str
c_end: str

def generate_c_header(func_sigs, sub_sigs, all_sigs, lib_name): ...
def split_signature(sig): ...
def filter_lines(lines): ...
def newer(source, target):
    """
    Return true if 'source' exists and is more recently modified than
    'target', or if 'source' exists and 'target' doesn't.  Return false if
    both exist and 'target' is the same age or younger than 'source'.
    """
def all_newer(src_files, dst_files): ...
def make_all(outdir, blas_signature_file: str = 'cython_blas_signatures.txt', lapack_signature_file: str = 'cython_lapack_signatures.txt', blas_name: str = 'cython_blas', lapack_name: str = 'cython_lapack', blas_fortran_name: str = '_blas_subroutine_wrappers.f', lapack_fortran_name: str = '_lapack_subroutine_wrappers.f', blas_header_name: str = '_blas_subroutines.h', lapack_header_name: str = '_lapack_subroutines.h') -> None: ...
