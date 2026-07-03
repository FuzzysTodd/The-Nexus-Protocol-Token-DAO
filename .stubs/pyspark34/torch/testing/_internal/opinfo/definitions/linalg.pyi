from _typeshed import Incomplete
from collections.abc import Generator
from torch.testing import make_tensor as make_tensor
from torch.testing._internal.common_cuda import with_tf32_off as with_tf32_off
from torch.testing._internal.common_device_type import has_cusolver as has_cusolver, skipCPUIfNoLapack as skipCPUIfNoLapack, skipCUDAIf as skipCUDAIf, skipCUDAIfNoCusolver as skipCUDAIfNoCusolver, skipCUDAIfNoMagma as skipCUDAIfNoMagma, skipCUDAIfNoMagmaAndNoCusolver as skipCUDAIfNoMagmaAndNoCusolver, skipCUDAIfRocm as skipCUDAIfRocm, tol as tol, toleranceOverride as toleranceOverride
from torch.testing._internal.common_dtype import all_types_and_complex as all_types_and_complex, all_types_and_complex_and as all_types_and_complex_and, floating_and_complex_types as floating_and_complex_types, floating_and_complex_types_and as floating_and_complex_types_and
from torch.testing._internal.common_utils import GRADCHECK_NONDET_TOL as GRADCHECK_NONDET_TOL, IS_MACOS as IS_MACOS, make_fullrank_matrices_with_distinct_singular_values as make_fullrank_matrices_with_distinct_singular_values, skipIfSlowGradcheckEnv as skipIfSlowGradcheckEnv, slowTest as slowTest
from torch.testing._internal.opinfo.core import DecorateInfo as DecorateInfo, ErrorInput as ErrorInput, OpInfo as OpInfo, ReductionOpInfo as ReductionOpInfo, S as S, SampleInput as SampleInput, clone_sample as clone_sample, gradcheck_wrapper_hermitian_input as gradcheck_wrapper_hermitian_input
from torch.testing._internal.opinfo.refs import PythonRefInfo as PythonRefInfo, ReductionPythonRefInfo as ReductionPythonRefInfo
from typing import List

def sample_kwargs_vector_norm(t, **kwargs): ...
def sample_inputs_svd(op_info, device, dtype, requires_grad: bool = False, **kwargs) -> Generator[Incomplete, None, Incomplete]: ...
def sample_inputs_cross(op_info, device, dtype, requires_grad, **kwargs) -> Generator[Incomplete, None, None]: ...
def error_inputs_cross(op_info, device, **kwargs) -> Generator[Incomplete, None, None]: ...
def sample_inputs_householder_product(op_info, device, dtype, requires_grad, **kwargs) -> Generator[Incomplete, None, None]:
    """
    This function generates input for torch.linalg.householder_product (torch.orgqr).
    The first argument should be a square matrix or batch of square matrices, the second argument is a vector or batch of vectors.
    Empty, square, rectangular, batched square and batched rectangular input is generated.
    """
def sample_inputs_linalg_det_singular(op_info, device, dtype, requires_grad, **kwargs) -> Generator[Incomplete, None, Incomplete]: ...
def sample_inputs_linalg_matrix_power(op_info, device, dtype, requires_grad, **kwargs) -> Generator[Incomplete, None, None]: ...
def sample_inputs_linalg_det_logdet_slogdet(op_info, device, dtype, requires_grad, **kwargs) -> Generator[Incomplete, None, None]: ...
def sample_inputs_lu_solve(op_info, device, dtype, requires_grad: bool = False, **kwargs) -> Generator[Incomplete, None, Incomplete]:
    """Samples the inputs for both linalg.lu_solve and lu_solve"""
def sample_inputs_linalg_multi_dot(op_info, device, dtype, requires_grad, **kwargs) -> Generator[Incomplete, None, None]: ...
def sample_inputs_linalg_matrix_norm(op_info, device, dtype, requires_grad, **kwargs) -> Generator[Incomplete, None, None]: ...
def sample_inputs_linalg_norm(op_info, device, dtype, requires_grad, *, variant: Incomplete | None = None, **kwargs) -> Generator[Incomplete, None, None]: ...
def sample_inputs_linalg_vecdot(op_info, device, dtype, requires_grad, **kwargs) -> Generator[Incomplete, None, None]: ...
def sample_inputs_linalg_invertible(op_info, device, dtype, requires_grad: bool = False, **kwargs) -> Generator[Incomplete, None, None]:
    """
    This function generates invertible inputs for linear algebra ops
    The input is generated as the itertools.product of 'batches' and 'ns'.
    In total this function generates 8 SampleInputs
    'batches' cases include:
        () - single input,
        (0,) - zero batched dimension,
        (2,) - batch of two matrices,
        (1, 1) - 1x1 batch of matrices
    'ns' gives 0x0 and 5x5 matrices.
    Zeros in dimensions are edge cases in the implementation and important to test for in order to avoid unexpected crashes.
    """
def sample_inputs_matrix_rank(op_info, device, dtype, requires_grad: bool = False, **kwargs) -> Generator[Incomplete, None, Incomplete]:
    """
    This function produces inputs for matrix rank that test
    all possible combinations for atol and rtol
    """
def sample_inputs_linalg_pinv_singular(op_info, device, dtype, requires_grad: bool = False, **kwargs) -> Generator[Incomplete, None, None]:
    """
    This function produces factors `a` and `b` to generate inputs of the form `a @ b.t()` to
    test the backward method of `linalg_pinv`. That way we always preserve the rank of the
    input no matter the perturbations applied to it by the gradcheck.
    Note that `pinv` is Frechet-differentiable in a rank-preserving neighborhood.
    """
def sample_inputs_linalg_cond(op_info, device, dtype, requires_grad: bool = False, **kwargs) -> Generator[Incomplete, None, None]: ...
def sample_inputs_linalg_vander(op_info, device, dtype, requires_grad: bool = False, **kwargs) -> Generator[Incomplete, None, None]: ...
def np_vander_batched(x, N: Incomplete | None = None): ...
def sample_inputs_linalg_cholesky_inverse(op_info, device, dtype, requires_grad: bool = False, **kwargs) -> Generator[Incomplete, None, None]: ...
def sample_inputs_linalg_ldl_factor(op_info, device, dtype, requires_grad: bool = False, **kwargs) -> Generator[Incomplete, None, None]: ...
def sample_inputs_linalg_ldl_solve(op_info, device, dtype, requires_grad: bool = False, **kwargs) -> Generator[Incomplete, None, None]: ...
def sample_inputs_linalg_lstsq(op_info, device, dtype, requires_grad: bool = False, **kwargs) -> Generator[Incomplete, None, None]: ...
def error_inputs_lstsq(op_info, device, **kwargs) -> Generator[Incomplete, None, None]: ...
def error_inputs_lstsq_grad_oriented(op_info, device, **kwargs) -> Generator[Incomplete, None, None]: ...
def sample_inputs_linalg_cholesky(op_info, device, dtype, requires_grad: bool = False, **kwargs) -> Generator[Incomplete, None, None]:
    """
    This function generates always positive-definite input for torch.linalg.cholesky using
    random_hermitian_pd_matrix.
    The input is generated as the itertools.product of 'batches' and 'ns'.
    In total this function generates 8 SampleInputs
    'batches' cases include:
        () - single input,
        (0,) - zero batched dimension,
        (2,) - batch of two matrices,
        (1, 1) - 1x1 batch of matrices
    'ns' gives 0x0 and 5x5 matrices.
    Zeros in dimensions are edge cases in the implementation and important to test for in order to avoid unexpected crashes.
    """
def sample_inputs_linalg_eig(op_info, device, dtype, requires_grad: bool = False, **kwargs) -> Generator[Incomplete, None, Incomplete]:
    """
    This function generates input for torch.linalg.eig
    """
def sample_inputs_linalg_eigh(op_info, device, dtype, requires_grad: bool = False, **kwargs) -> Generator[Incomplete, None, Incomplete]:
    '''
    This function generates input for torch.linalg.eigh/eigvalsh with UPLO="U" or "L" keyword argument.
    '''
def sample_inputs_linalg_pinv(op_info, device, dtype, requires_grad: bool = False, **kwargs) -> Generator[Incomplete, None, None]:
    """
    This function generates input for torch.linalg.pinv with hermitian=False keyword argument.
    """
def sample_inputs_linalg_pinv_hermitian(op_info, device, dtype, requires_grad: bool = False, **kwargs) -> Generator[Incomplete, None, None]:
    """
    This function generates input for torch.linalg.pinv with hermitian=True keyword argument.
    """
def sample_inputs_linalg_solve(op_info, device, dtype, requires_grad: bool = False, vector_rhs_allowed: bool = True, **kwargs) -> Generator[Incomplete, None, None]:
    """
    This function generates always solvable input for torch.linalg.solve
    We sample a fullrank square matrix (i.e. invertible) A
    The first input to torch.linalg.solve is generated as the itertools.product of 'batches' and 'ns'.
    The second input is generated as the product of 'batches', 'ns' and 'nrhs'.
    In total this function generates 18 SampleInputs
    'batches' cases include:
        () - single input,
        (0,) - zero batched dimension,
        (2,) - batch of two matrices.
    'ns' gives 0x0 and 5x5 matrices.
    and 'nrhs' controls the number of vectors to solve for:
        () - using 1 as the number of vectors implicitly
        (1,) - same as () but explicit
        (3,) - solve for 3 vectors.
    Zeros in dimensions are edge cases in the implementation and important to test for in order to avoid unexpected crashes.
    'vector_rhs_allowed' controls whether to include nrhs = () to the list of SampleInputs.
    torch.solve / triangular_solve / cholesky_solve (opposed to torch.linalg.solve) do not allow
    1D tensors (vectors) as the right-hand-side.
    Once torch.solve / triangular_solve / cholesky_solve and its testing are removed,
    'vector_rhs_allowed' may be removed here as well.
    """
def sample_inputs_linalg_solve_triangular(op_info, device, dtype, requires_grad: bool = False, **kwargs) -> Generator[Incomplete, None, None]: ...
def sample_inputs_legacy_solve(op_info, device, dtype, requires_grad: bool = False, **kwargs) -> Generator[Incomplete, None, Incomplete]:
    """
    This function generates always solvable input for legacy solve functions
    (the ones that are not in torch.linalg module).
    The difference from sample_inputs_linalg_solve is that here the right-hand-side of A x = b equation
    should have b.ndim >= 2, vectors are not allowed.
    Also the arguments order is swapped.
    """
def sample_inputs_linalg_lu(op_info, device, dtype, requires_grad: bool = False, **kwargs) -> Generator[Incomplete, None, Incomplete]: ...
def sample_inputs_linalg_svdvals(op_info, device, dtype, requires_grad: bool = False, **kwargs) -> Generator[Incomplete, None, None]: ...
def sample_inputs_linalg_qr_geqrf(op_info, device, dtype, requires_grad: bool = False, **kwargs) -> Generator[Incomplete, None, None]: ...
def sample_inputs_tensorsolve(op_info, device, dtype, requires_grad, **kwargs) -> Generator[Incomplete, None, None]: ...
def sample_inputs_tensorinv(op_info, device, dtype, requires_grad, **kwargs) -> Generator[Incomplete, None, Incomplete]: ...

op_db: List[OpInfo]
python_ref_db: List[OpInfo]
