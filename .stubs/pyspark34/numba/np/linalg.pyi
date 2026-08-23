from .arrayobj import array_copy as array_copy, make_array as make_array
from _typeshed import Incomplete
from collections.abc import Generator
from numba.core import cgutils as cgutils, types as types
from numba.core.errors import NumbaPerformanceWarning as NumbaPerformanceWarning, NumbaTypeError as NumbaTypeError, TypingError as TypingError
from numba.core.extending import intrinsic as intrinsic, overload as overload, register_jitable as register_jitable
from numba.core.imputils import impl_ret_borrowed as impl_ret_borrowed, impl_ret_new_ref as impl_ret_new_ref, impl_ret_untracked as impl_ret_untracked, lower_builtin as lower_builtin
from numba.core.typing import signature as signature

ll_char: Incomplete
ll_char_p: Incomplete
ll_void_p = ll_char_p
ll_intc: Incomplete
ll_intc_p: Incomplete
intp_t: Incomplete
ll_intp_p: Incomplete
F_INT_nptype: Incomplete
F_INT_nbtype: Incomplete

def get_blas_kind(dtype, func_name: str = '<BLAS function>'): ...
def ensure_blas() -> None: ...
def ensure_lapack() -> None: ...
def make_constant_slot(context, builder, ty, val): ...

class _BLAS:
    """
    Functions to return type signatures for wrapped
    BLAS functions.
    """
    def __init__(self) -> None: ...
    @classmethod
    def numba_xxnrm2(cls, dtype): ...
    @classmethod
    def numba_xxgemm(cls, dtype): ...

class _LAPACK:
    """
    Functions to return type signatures for wrapped
    LAPACK functions.
    """
    def __init__(self) -> None: ...
    @classmethod
    def numba_xxgetrf(cls, dtype): ...
    @classmethod
    def numba_ez_xxgetri(cls, dtype): ...
    @classmethod
    def numba_ez_rgeev(cls, dtype): ...
    @classmethod
    def numba_ez_cgeev(cls, dtype): ...
    @classmethod
    def numba_ez_xxxevd(cls, dtype): ...
    @classmethod
    def numba_xxpotrf(cls, dtype): ...
    @classmethod
    def numba_ez_gesdd(cls, dtype): ...
    @classmethod
    def numba_ez_geqrf(cls, dtype): ...
    @classmethod
    def numba_ez_xxgqr(cls, dtype): ...
    @classmethod
    def numba_ez_gelsd(cls, dtype): ...
    @classmethod
    def numba_xgesv(cls, dtype): ...

def make_contiguous(context, builder, sig, args) -> Generator[Incomplete, None, None]:
    """
    Ensure that all array arguments are contiguous, if necessary by
    copying them.
    A new (sig, args) tuple is yielded.
    """
def check_c_int(context, builder, n) -> None:
    """
    Check whether *n* fits in a C `int`.
    """
def check_blas_return(context, builder, res) -> None:
    """
    Check the integer error return from one of the BLAS wrappers in
    _helperlib.c.
    """
def check_lapack_return(context, builder, res) -> None:
    """
    Check the integer error return from one of the LAPACK wrappers in
    _helperlib.c.
    """
def call_xxdot(context, builder, conjugate, dtype, n, a_data, b_data, out_data) -> None:
    """
    Call the BLAS vector * vector product function for the given arguments.
    """
def call_xxgemv(context, builder, do_trans, m_type, m_shapes, m_data, v_data, out_data) -> None:
    """
    Call the BLAS matrix * vector product function for the given arguments.
    """
def call_xxgemm(context, builder, x_type, x_shapes, x_data, y_type, y_shapes, y_data, out_type, out_shapes, out_data):
    """
    Call the BLAS matrix * matrix product function for the given arguments.
    """
def dot_2_mm(context, builder, sig, args):
    """
    np.dot(matrix, matrix)
    """
def dot_2_vm(context, builder, sig, args):
    """
    np.dot(vector, matrix)
    """
def dot_2_mv(context, builder, sig, args):
    """
    np.dot(matrix, vector)
    """
def dot_2_vv(context, builder, sig, args, conjugate: bool = False):
    """
    np.dot(vector, vector)
    np.vdot(vector, vector)
    """
def dot_2(left, right):
    """
    np.dot(a, b)
    """
def matmul_2(left, right):
    """
    a @ b
    """
def dot_2_impl(name, left, right): ...
def vdot(left, right):
    """
    np.vdot(a, b)
    """
def dot_3_vm_check_args(a, b, out) -> None: ...
def dot_3_mv_check_args(a, b, out) -> None: ...
def dot_3_vm(context, builder, sig, args):
    """
    np.dot(vector, matrix, out)
    np.dot(matrix, vector, out)
    """
def dot_3_mm(context, builder, sig, args):
    """
    np.dot(matrix, matrix, out)
    """
def dot_3(left, right, out):
    """
    np.dot(a, b, out)
    """

fatal_error_func: Incomplete

def ol_copy_to_fortran_order(a): ...
def inv_impl(a): ...
def cho_impl(a): ...
def eig_impl(a): ...
def eigvals_impl(a): ...
def eigh_impl(a): ...
def eigvalsh_impl(a): ...
def svd_impl(a, full_matrices: int = 1): ...
def qr_impl(a): ...
def lstsq_impl(a, b, rcond: float = -1.0): ...
def solve_impl(a, b): ...
def pinv_impl(a, rcond: float = 1e-15): ...
def slogdet_impl(a): ...
def det_impl(a): ...
def norm_impl(a, ord: Incomplete | None = None): ...
def cond_impl(a, p: Incomplete | None = None): ...
def matrix_rank_impl(a, tol: Incomplete | None = None):
    """
    Computes rank for matrices and vectors.
    The only issue that may arise is that because numpy uses double
    precision lapack calls whereas numba uses type specific lapack
    calls, some singular values may differ and therefore counting the
    number of them above a tolerance may lead to different counts,
    and therefore rank, in some cases.
    """
def matrix_power_impl(a, n):
    """
    Computes matrix power. Only integer powers are supported in numpy.
    """
def matrix_trace_impl(a, offset: int = 0):
    """
    Computes the trace of an array.
    """
def outer_impl_none(a, b, out): ...
def outer_impl_arr(a, b, out): ...
def outer_impl(a, b, out: Incomplete | None = None): ...
def kron_impl(a, b): ...
