from _typeshed import Incomplete
from jax import lax as lax
from jax._src import ad_util as ad_util, api as api, dispatch as dispatch, dtypes as dtypes
from jax._src.core import Primitive as Primitive, ShapedArray as ShapedArray, is_constant_dim as is_constant_dim, is_constant_shape as is_constant_shape, raise_to_shaped as raise_to_shaped
from jax._src.interpreters import ad as ad, batching as batching, mlir as mlir
from jax._src.lax import control_flow as control_flow
from jax._src.lax.lax import naryop_dtype_rule as naryop_dtype_rule, standard_primitive as standard_primitive, standard_unop as standard_unop
from jax._src.lib import gpu_linalg as gpu_linalg, gpu_solver as gpu_solver, gpu_sparse as gpu_sparse, lapack as lapack, xla_client as xla_client
from jax._src.lib.mlir import ir as ir
from jax._src.lib.mlir.dialects import chlo as chlo, hlo as hlo
from jax._src.numpy import reductions as reductions, ufuncs as ufuncs
from jax._src.numpy.vectorize import vectorize as vectorize
from jax._src.typing import Array as Array, ArrayLike as ArrayLike
from typing import Any, Callable, Literal, TypeVar, overload

xops: Incomplete
TFun = TypeVar('TFun', bound=Callable[..., Any])

def cholesky(x: Array, *, symmetrize_input: bool = True) -> Array:
    """Cholesky decomposition.

  Computes the Cholesky decomposition

  .. math::
    A = L . L^H

  of square matrices, :math:`A`, such that :math:`L`
  is lower triangular. The matrices of :math:`A` must be positive-definite and
  either Hermitian, if complex, or symmetric, if real.

  Args:
    x: A batch of square Hermitian (symmetric if real) positive-definite
      matrices with shape ``[..., n, n]``.
    symmetrize_input: If ``True``, the matrix is symmetrized before Cholesky
      decomposition by computing :math:`\\frac{1}{2}(x + x^H)`. If ``False``,
      only the lower triangle of ``x`` is used; the upper triangle is ignored
      and not accessed.

  Returns:
    The Cholesky decomposition as a matrix with the same dtype as ``x`` and
    shape ``[..., n, n]``. If Cholesky decomposition fails, returns a matrix
    full of NaNs. The behavior on failure may change in the future.
  """
def eig(x: ArrayLike, *, compute_left_eigenvectors: bool = True, compute_right_eigenvectors: bool = True) -> list[Array]:
    """Eigendecomposition of a general matrix.

  Nonsymmetric eigendecomposition is at present only implemented on CPU.
  """
def eigh(x: Array, *, lower: bool = True, symmetrize_input: bool = True, sort_eigenvalues: bool = True) -> tuple[Array, Array]:
    """Eigendecomposition of a Hermitian matrix.

  Computes the eigenvectors and eigenvalues of a complex Hermitian or real
  symmetric square matrix.

  Args:
    x: A batch of square complex Hermitian or real symmetric matrices with shape
      ``[..., n, n]``.
    lower: If ``symmetrize_input`` is ``False``, describes which triangle of the
      input matrix to use. If ``symmetrize_input`` is ``False``, only the
      triangle given by ``lower`` is accessed; the other triangle is ignored and
      not accessed.
    symmetrize_input: If ``True``, the matrix is symmetrized before the
      eigendecomposition by computing :math:`\\frac{1}{2}(x + x^H)`.
    sort_eigenvalues: If ``True``, the eigenvalues will be sorted in ascending
      order. If ``False`` the eigenvalues are returned in an
      implementation-defined order.

  Returns:
    A tuple ``(v, w)``.

    ``v`` is an array with the same dtype as ``x`` such that ``v[..., :, i]`` is
    the normalized eigenvector corresponding to eigenvalue ``w[..., i]``.

    ``w`` is an array with the same dtype as ``x`` (or its real counterpart if
    complex) with shape ``[..., n]`` containing the eigenvalues of ``x`` in
    ascending order(each repeated according to its multiplicity).
  """
def lu_pivots_to_permutation(pivots: ArrayLike, permutation_size: int) -> Array:
    """Converts the pivots (row swaps) returned by LU to a permutation.

  We build a permutation rather than applying `pivots` directly to the rows
  of a matrix because lax loops aren't differentiable.

  Args:
    pivots: an int32 array of shape (..., k) of row swaps to perform
    permutation_size: the size of the output permutation. Has to be >= k.

  Returns:
    An int32 array of shape (..., permutation_size).
  """
def lu(x: ArrayLike) -> tuple[Array, Array, Array]:
    """LU decomposition with partial pivoting.

  Computes the matrix decomposition:

  .. math::
    P.A = L.U

  where :math:`P` is a permutation of the rows of :math:`A`, :math:`L` is a
  lower-triangular matrix with unit-diagonal elements, and :math:`U` is an
  upper-triangular matrix.

  Args:
    x: A batch of matrices with shape ``[..., m, n]``.

  Returns:
    A tuple ``(lu, pivots, permutation)``.

    ``lu`` is a batch of matrices with the same shape and dtype as ``x``
    containing the :math:`L` matrix in its lower triangle and the :math:`U`
    matrix in its upper triangle. The (unit) diagonal elements of :math:`L` are
    not represented explicitly.

    ``pivots`` is an int32 array with shape ``[..., min(m, n)]`` representing a
    sequence of row swaps that should be performed on :math:`A`.

    ``permutation`` is an alternative representation of the sequence of row
    swaps as a permutation, represented as an int32 array with shape
    ``[..., m]``.
  """
def qr(x: ArrayLike, *, full_matrices: bool = True) -> tuple[Array, Array]:
    """QR decomposition.

  Computes the QR decomposition

  .. math::
    A = Q . R

  of matrices :math:`A`, such that :math:`Q` is a unitary (orthogonal) matrix,
  and :math:`R` is an upper-triangular matrix.

  Args:
    x: A batch of matrices with shape ``[..., m, n]``.
    full_matrices: Determines if full or reduced matrices are returned; see
      below.

  Returns:
    A pair of arrays ``(q, r)``.

    Array ``q`` is a unitary (orthogonal) matrix,
    with shape ``[..., m, m]`` if ``full_matrices=True``, or
    ``[..., m, min(m, n)]`` if ``full_matrices=False``.

    Array ``r`` is an upper-triangular matrix with shape ``[..., m, n]`` if
    ``full_matrices=True``, or ``[..., min(m, n), n]`` if
    ``full_matrices=False``.
  """
@overload
def svd(x: ArrayLike, *, full_matrices: bool = True, compute_uv: Literal[True]) -> tuple[Array, Array, Array]: ...
@overload
def svd(x: ArrayLike, *, full_matrices: bool = True, compute_uv: Literal[False]) -> Array: ...
@overload
def svd(x: ArrayLike, *, full_matrices: bool = True, compute_uv: bool = True) -> Array | tuple[Array, Array, Array]: ...
def triangular_solve(a: ArrayLike, b: ArrayLike, *, left_side: bool = False, lower: bool = False, transpose_a: bool = False, conjugate_a: bool = False, unit_diagonal: bool = False) -> Array:
    """Triangular solve.

  Solves either the matrix equation

  .. math::
    \\mathit{op}(A) . X = B

  if ``left_side`` is ``True`` or

  .. math::
    X . \\mathit{op}(A) = B

  if ``left_side`` is ``False``.

  ``A`` must be a lower or upper triangular square matrix, and where
  :math:`\\mathit{op}(A)` may either transpose :math:`A` if ``transpose_a``
  is ``True`` and/or take its complex conjugate if ``conjugate_a`` is ``True``.

  Args:
    a: A batch of matrices with shape ``[..., m, m]``.
    b: A batch of matrices with shape ``[..., m, n]`` if ``left_side`` is
      ``True`` or shape ``[..., n, m]`` otherwise.
    left_side: describes which of the two matrix equations to solve; see above.
    lower: describes which triangle of ``a`` should be used. The other triangle
      is ignored.
    transpose_a: if ``True``, the value of ``a`` is transposed.
    conjugate_a: if ``True``, the complex conjugate of ``a`` is used in the
      solve. Has no effect if ``a`` is real.
    unit_diagonal: if ``True``, the diagonal of ``a`` is assumed to be unit
      (all 1s) and not accessed.

  Returns:
    A batch of matrices the same shape and dtype as ``b``.
  """
def symmetrize(x: Array) -> Array: ...

cholesky_p: Incomplete

def eig_impl(operand, *, compute_left_eigenvectors, compute_right_eigenvectors): ...
def eig_lower(*args, **kw) -> None: ...
def eig_abstract_eval(operand, *, compute_left_eigenvectors, compute_right_eigenvectors): ...
def eig_batching_rule(batched_args, batch_dims, *, compute_left_eigenvectors, compute_right_eigenvectors): ...
def eig_jvp_rule(primals, tangents, *, compute_left_eigenvectors, compute_right_eigenvectors): ...

eig_p: Incomplete

def eigh_jacobi(x: ArrayLike, *, lower: bool = True, sort_eigenvalues: bool = True) -> tuple[Array, Array]:
    """Helper Jacobi eigendecomposition implemented by XLA.

  Used as a subroutine of QDWH-eig on TPU."""

eigh_jacobi_p: Incomplete
eigh_p: Incomplete
triangular_solve_p: Incomplete
lu_pivots_to_permutation_p: Incomplete
lu_p: Incomplete

def lu_solve(lu: ArrayLike, permutation: ArrayLike, b: ArrayLike, trans: int = 0) -> Array:
    """LU solve with broadcasting."""
def geqrf(a: ArrayLike) -> tuple[Array, Array]:
    """Computes the QR decomposition of a matrix.

  Args:
    a: an ``[..., m, n]`` batch of matrices, with floating-point or complex type.
  Returns:
    An ``(a, taus)`` pair where ``r`` is in the upper triangle of ``a``,
    ``q`` is represented in the lower triangle of ``a`` and in ``taus`` as
    elementary Householder reflectors.
  """

geqrf_p: Incomplete

def householder_product(a: ArrayLike, taus: ArrayLike) -> Array:
    """Product of elementary Householder reflectors.

  Args:
    a: A matrix with shape ``[..., m, n]``, whose lower triangle contains
      elementary Householder reflectors.
    taus: A vector with shape ``[..., k]``, where ``k < min(m, n)``, containing
      the scalar factors of the elementary Householder reflectors.

  Returns:
    A batch of orthogonal (unitary) matrices with the same shape as ``a``,
    containing the products of the elementary Householder reflectors.
  """

householder_product_p: Incomplete

def qr_jvp_rule(primals, tangents, *, full_matrices): ...

qr_p: Incomplete
svd_p: Incomplete
tridiagonal_solve_p: Incomplete

def tridiagonal_solve(dl: Array, d: Array, du: Array, b: Array) -> Array:
    """Computes the solution of a tridiagonal linear system.

  This function computes the solution of a tridiagonal linear system:

  .. math::
    A . X = B

  Args:

    dl: A batch of vectors with shape ``[..., m]``.
      The lower diagonal of A: ``dl[i] := A[i, i-1]`` for i in ``[0,m)``.
      Note that ``dl[0] = 0``.
    d: A batch of vectors with shape ``[..., m]``.
      The middle diagonal of A: ``d[i]  := A[i, i]`` for i in ``[0,m)``.
    du: A batch of vectors with shape ``[..., m]``.
      The upper diagonal of A: ``du[i] := A[i, i+1]`` for i in ``[0,m)``.
      Note that ``dl[m - 1] = 0``.
    b: Right hand side matrix.

  Returns:
    Solution ``X`` of tridiagonal system.
  """
def schur(x: ArrayLike, *, compute_schur_vectors: bool = True, sort_eig_vals: bool = False, select_callable: Callable[..., Any] | None = None) -> tuple[Array, Array]: ...

schur_p: Incomplete

def hessenberg(a: ArrayLike) -> tuple[Array, Array]:
    """Reduces a square matrix to upper Hessenberg form.

  Currently implemented on CPU only.

  Args:
    a: A floating point or complex square matrix or batch of matrices.

  Returns:
  A ``(a, taus)`` pair, where the upper triangle and first subdiagonal of ``a``
  contain the upper Hessenberg matrix, and the elements below the first
  subdiagonal contain the Householder reflectors. For each Householder
  reflector ``taus`` contains the scalar factors of the elementary Householder
  reflectors.
  """

hessenberg_p: Incomplete

def tridiagonal(a: ArrayLike, *, lower: bool = True) -> tuple[Array, Array, Array, Array]:
    """Reduces a symmetric/Hermitian matrix to tridiagonal form.

  Currently implemented on CPU and GPU only.

  Args:
    a: A floating point or complex matrix or batch of matrices.
    lower: Describes which triangle of the input matrices to use.
      The other triangle is ignored and not accessed.

  Returns:
  A ``(a, d, e, taus)`` pair. If ``lower=True``, the diagonal and first subdiagonal of
  matrix (or batch of matrices) ``a`` contain the tridiagonal representation,
  and elements below the first subdiagonal contain the elementary Householder
  reflectors, where additionally ``d`` contains the diagonal of the matrix and ``e`` contains
  the first subdiagonal.If ``lower=False`` the diagonal and first superdiagonal of the
  matrix contains the tridiagonal representation, and elements above the first
  superdiagonal contain the elementary Householder reflectors, where
  additionally ``d`` contains the diagonal of the matrix and ``e`` contains the
  first superdiagonal. ``taus`` contains the scalar factors of the elementary
  Householder reflectors.
  """

tridiagonal_p: Incomplete
