from _typeshed import Incomplete
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, control_flow_ops as control_flow_ops, gen_linalg_ops as gen_linalg_ops, linalg_ops as linalg_ops, map_fn as map_fn, math_ops as math_ops, special_math_ops as special_math_ops, stateless_random_ops as stateless_random_ops
from tensorflow.python.util import dispatch as dispatch
from tensorflow.python.util.tf_export import tf_export as tf_export

band_part: Incomplete
cholesky: Incomplete
cholesky_solve: Incomplete
det: Incomplete
slogdet: Incomplete
diag: Incomplete
diag_part: Incomplete
eigh: Incomplete
eigvalsh: Incomplete
einsum = special_math_ops.einsum
eye: Incomplete
inv: Incomplete
logm: Incomplete
lu: Incomplete
lstsq: Incomplete
norm: Incomplete
qr: Incomplete
set_diag: Incomplete
solve: Incomplete
sqrtm: Incomplete
svd: Incomplete
tensordot: Incomplete
trace: Incomplete
transpose: Incomplete
triangular_solve: Incomplete

def logdet(matrix, name: Incomplete | None = None):
    """Computes log of the determinant of a hermitian positive definite matrix.

  ```python
  # Compute the determinant of a matrix while reducing the chance of over- or
  underflow:
  A = ... # shape 10 x 10
  det = tf.exp(tf.linalg.logdet(A))  # scalar
  ```

  Args:
    matrix:  A `Tensor`. Must be `float16`, `float32`, `float64`, `complex64`,
      or `complex128` with shape `[..., M, M]`.
    name:  A name to give this `Op`.  Defaults to `logdet`.

  Returns:
    The natural log of the determinant of `matrix`.

  @compatibility(numpy)
  Equivalent to numpy.linalg.slogdet, although no sign is returned since only
  hermitian positive definite matrices are supported.
  @end_compatibility
  """
def adjoint(matrix, name: Incomplete | None = None):
    """Transposes the last two dimensions of and conjugates tensor `matrix`.

  For example:

  ```python
  x = tf.constant([[1 + 1j, 2 + 2j, 3 + 3j],
                   [4 + 4j, 5 + 5j, 6 + 6j]])
  tf.linalg.adjoint(x)  # [[1 - 1j, 4 - 4j],
                        #  [2 - 2j, 5 - 5j],
                        #  [3 - 3j, 6 - 6j]]
  ```

  Args:
    matrix:  A `Tensor`. Must be `float16`, `float32`, `float64`, `complex64`,
      or `complex128` with shape `[..., M, M]`.
    name:  A name to give this `Op` (optional).

  Returns:
    The adjoint (a.k.a. Hermitian transpose a.k.a. conjugate transpose) of
    matrix.
  """
def matrix_exponential(input, name: Incomplete | None = None):
    '''Computes the matrix exponential of one or more square matrices.

  $$exp(A) = \\sum_{n=0}^\\infty A^n/n!$$

  The exponential is computed using a combination of the scaling and squaring
  method and the Pade approximation. Details can be found in:
  Nicholas J. Higham, "The scaling and squaring method for the matrix
  exponential revisited," SIAM J. Matrix Anal. Applic., 26:1179-1193, 2005.

  The input is a tensor of shape `[..., M, M]` whose inner-most 2 dimensions
  form square matrices. The output is a tensor of the same shape as the input
  containing the exponential for all input submatrices `[..., :, :]`.

  Args:
    input: A `Tensor`. Must be `float16`, `float32`, `float64`, `complex64`, or
      `complex128` with shape `[..., M, M]`.
    name:  A name to give this `Op` (optional).

  Returns:
    the matrix exponential of the input.

  Raises:
    ValueError: An unsupported type is provided as input.

  @compatibility(scipy)
  Equivalent to scipy.linalg.expm
  @end_compatibility
  '''
def banded_triangular_solve(bands, rhs, lower: bool = True, adjoint: bool = False, name: Incomplete | None = None):
    """Solve triangular systems of equations with a banded solver.

  `bands` is a tensor of shape `[..., K, M]`, where `K` represents the number
  of bands stored. This corresponds to a batch of `M` by `M` matrices, whose
  `K` subdiagonals (when `lower` is `True`) are stored.

  This operator broadcasts the batch dimensions of `bands` and the batch
  dimensions of `rhs`.


  Examples:

  Storing 2 bands of a 3x3 matrix.
  Note that first element in the second row is ignored due to
  the 'LEFT_RIGHT' padding.

  >>> x = [[2., 3., 4.], [1., 2., 3.]]
  >>> x2 = [[2., 3., 4.], [10000., 2., 3.]]
  >>> y = tf.zeros([3, 3])
  >>> z = tf.linalg.set_diag(y, x, align='LEFT_RIGHT', k=(-1, 0))
  >>> z
  <tf.Tensor: shape=(3, 3), dtype=float32, numpy=
  array([[2., 0., 0.],
         [2., 3., 0.],
         [0., 3., 4.]], dtype=float32)>
  >>> soln = tf.linalg.banded_triangular_solve(x, tf.ones([3, 1]))
  >>> soln
  <tf.Tensor: shape=(3, 1), dtype=float32, numpy=
  array([[0.5 ],
         [0.  ],
         [0.25]], dtype=float32)>
  >>> are_equal = soln == tf.linalg.banded_triangular_solve(x2, tf.ones([3, 1]))
  >>> tf.reduce_all(are_equal).numpy()
  True
  >>> are_equal = soln == tf.linalg.triangular_solve(z, tf.ones([3, 1]))
  >>> tf.reduce_all(are_equal).numpy()
  True

  Storing 2 superdiagonals of a 4x4 matrix. Because of the 'LEFT_RIGHT' padding
  the last element of the first row is ignored.

  >>> x = [[2., 3., 4., 5.], [-1., -2., -3., -4.]]
  >>> y = tf.zeros([4, 4])
  >>> z = tf.linalg.set_diag(y, x, align='LEFT_RIGHT', k=(0, 1))
  >>> z
  <tf.Tensor: shape=(4, 4), dtype=float32, numpy=
  array([[-1.,  2.,  0.,  0.],
         [ 0., -2.,  3.,  0.],
         [ 0.,  0., -3.,  4.],
         [ 0.,  0., -0., -4.]], dtype=float32)>
  >>> soln = tf.linalg.banded_triangular_solve(x, tf.ones([4, 1]), lower=False)
  >>> soln
  <tf.Tensor: shape=(4, 1), dtype=float32, numpy=
  array([[-4.       ],
         [-1.5      ],
         [-0.6666667],
         [-0.25     ]], dtype=float32)>
  >>> are_equal = (soln == tf.linalg.triangular_solve(
  ...   z, tf.ones([4, 1]), lower=False))
  >>> tf.reduce_all(are_equal).numpy()
  True


  Args:
    bands: A `Tensor` describing the bands of the left hand side, with shape
      `[..., K, M]`. The `K` rows correspond to the diagonal to the `K - 1`-th
      diagonal (the diagonal is the top row) when `lower` is `True` and
      otherwise the `K - 1`-th superdiagonal to the diagonal (the diagonal is
      the bottom row) when `lower` is `False`. The bands are stored with
      'LEFT_RIGHT' alignment, where the superdiagonals are padded on the right
      and subdiagonals are padded on the left. This is the alignment cuSPARSE
      uses.  See  `tf.linalg.set_diag` for more details.
    rhs: A `Tensor` of shape [..., M] or [..., M, N] and with the same dtype as
      `diagonals`. Note that if the shape of `rhs` and/or `diags` isn't known
      statically, `rhs` will be treated as a matrix rather than a vector.
    lower: An optional `bool`. Defaults to `True`. Boolean indicating whether
      `bands` represents a lower or upper triangular matrix.
    adjoint: An optional `bool`. Defaults to `False`. Boolean indicating whether
      to solve with the matrix's block-wise adjoint.
    name:  A name to give this `Op` (optional).

  Returns:
    A `Tensor` of shape [..., M] or [..., M, N] containing the solutions.
  """
def tridiagonal_solve(diagonals, rhs, diagonals_format: str = 'compact', transpose_rhs: bool = False, conjugate_rhs: bool = False, name: Incomplete | None = None, partial_pivoting: bool = True, perturb_singular: bool = False):
    """Solves tridiagonal systems of equations.

  The input can be supplied in various formats: `matrix`, `sequence` and
  `compact`, specified by the `diagonals_format` arg.

  In `matrix` format, `diagonals` must be a tensor of shape `[..., M, M]`, with
  two inner-most dimensions representing the square tridiagonal matrices.
  Elements outside of the three diagonals will be ignored.

  In `sequence` format, `diagonals` are supplied as a tuple or list of three
  tensors of shapes `[..., N]`, `[..., M]`, `[..., N]` representing
  superdiagonals, diagonals, and subdiagonals, respectively. `N` can be either
  `M-1` or `M`; in the latter case, the last element of superdiagonal and the
  first element of subdiagonal will be ignored.

  In `compact` format the three diagonals are brought together into one tensor
  of shape `[..., 3, M]`, with last two dimensions containing superdiagonals,
  diagonals, and subdiagonals, in order. Similarly to `sequence` format,
  elements `diagonals[..., 0, M-1]` and `diagonals[..., 2, 0]` are ignored.

  The `compact` format is recommended as the one with best performance. In case
  you need to cast a tensor into a compact format manually, use `tf.gather_nd`.
  An example for a tensor of shape [m, m]:

  ```python
  rhs = tf.constant([...])
  matrix = tf.constant([[...]])
  m = matrix.shape[0]
  dummy_idx = [0, 0]  # An arbitrary element to use as a dummy
  indices = [[[i, i + 1] for i in range(m - 1)] + [dummy_idx],  # Superdiagonal
           [[i, i] for i in range(m)],                          # Diagonal
           [dummy_idx] + [[i + 1, i] for i in range(m - 1)]]    # Subdiagonal
  diagonals=tf.gather_nd(matrix, indices)
  x = tf.linalg.tridiagonal_solve(diagonals, rhs)
  ```

  Regardless of the `diagonals_format`, `rhs` is a tensor of shape `[..., M]` or
  `[..., M, K]`. The latter allows to simultaneously solve K systems with the
  same left-hand sides and K different right-hand sides. If `transpose_rhs`
  is set to `True` the expected shape is `[..., M]` or `[..., K, M]`.

  The batch dimensions, denoted as `...`, must be the same in `diagonals` and
  `rhs`.

  The output is a tensor of the same shape as `rhs`: either `[..., M]` or
  `[..., M, K]`.

  The op isn't guaranteed to raise an error if the input matrix is not
  invertible. `tf.debugging.check_numerics` can be applied to the output to
  detect invertibility problems.

  **Note**: with large batch sizes, the computation on the GPU may be slow, if
  either `partial_pivoting=True` or there are multiple right-hand sides
  (`K > 1`). If this issue arises, consider if it's possible to disable pivoting
  and have `K = 1`, or, alternatively, consider using CPU.

  On CPU, solution is computed via Gaussian elimination with or without partial
  pivoting, depending on `partial_pivoting` parameter. On GPU, Nvidia's cuSPARSE
  library is used: https://docs.nvidia.com/cuda/cusparse/index.html#gtsv

  Args:
    diagonals: A `Tensor` or tuple of `Tensor`s describing left-hand sides. The
      shape depends of `diagonals_format`, see description above. Must be
      `float32`, `float64`, `complex64`, or `complex128`.
    rhs: A `Tensor` of shape [..., M] or [..., M, K] and with the same dtype as
      `diagonals`. Note that if the shape of `rhs` and/or `diags` isn't known
      statically, `rhs` will be treated as a matrix rather than a vector.
    diagonals_format: one of `matrix`, `sequence`, or `compact`. Default is
      `compact`.
    transpose_rhs: If `True`, `rhs` is transposed before solving (has no effect
      if the shape of rhs is [..., M]).
    conjugate_rhs: If `True`, `rhs` is conjugated before solving.
    name:  A name to give this `Op` (optional).
    partial_pivoting: whether to perform partial pivoting. `True` by default.
      Partial pivoting makes the procedure more stable, but slower. Partial
      pivoting is unnecessary in some cases, including diagonally dominant and
      symmetric positive definite matrices (see e.g. theorem 9.12 in [1]).
    perturb_singular: whether to perturb singular matrices to return a finite
      result. `False` by default. If true, solutions to systems involving
      a singular matrix will be computed by perturbing near-zero pivots in
      the partially pivoted LU decomposition. Specifically, tiny pivots are
      perturbed by an amount of order `eps * max_{ij} |U(i,j)|` to avoid
      overflow. Here `U` is the upper triangular part of the LU decomposition,
      and `eps` is the machine precision. This is useful for solving
      numerically singular systems when computing eigenvectors by inverse
      iteration.
      If `partial_pivoting` is `False`, `perturb_singular` must be `False` as
      well.

  Returns:
    A `Tensor` of shape [..., M] or [..., M, K] containing the solutions.
    If the input matrix is singular, the result is undefined.

  Raises:
    ValueError: Is raised if any of the following conditions hold:
      1. An unsupported type is provided as input,
      2. the input tensors have incorrect shapes,
      3. `perturb_singular` is `True` but `partial_pivoting` is not.
    UnimplementedError: Whenever `partial_pivoting` is true and the backend is
      XLA, or whenever `perturb_singular` is true and the backend is
      XLA or GPU.

  [1] Nicholas J. Higham (2002). Accuracy and Stability of Numerical Algorithms:
  Second Edition. SIAM. p. 175. ISBN 978-0-89871-802-7.

  """
def tridiagonal_matmul(diagonals, rhs, diagonals_format: str = 'compact', name: Incomplete | None = None):
    """Multiplies tridiagonal matrix by matrix.

  `diagonals` is representation of 3-diagonal NxN matrix, which depends on
  `diagonals_format`.

  In `matrix` format, `diagonals` must be a tensor of shape `[..., M, M]`, with
  two inner-most dimensions representing the square tridiagonal matrices.
  Elements outside of the three diagonals will be ignored.

  If `sequence` format, `diagonals` is list or tuple of three tensors:
  `[superdiag, maindiag, subdiag]`, each having shape [..., M]. Last element
  of `superdiag` first element of `subdiag` are ignored.

  In `compact` format the three diagonals are brought together into one tensor
  of shape `[..., 3, M]`, with last two dimensions containing superdiagonals,
  diagonals, and subdiagonals, in order. Similarly to `sequence` format,
  elements `diagonals[..., 0, M-1]` and `diagonals[..., 2, 0]` are ignored.

  The `sequence` format is recommended as the one with the best performance.

  `rhs` is matrix to the right of multiplication. It has shape `[..., M, N]`.

  Example:

  ```python
  superdiag = tf.constant([-1, -1, 0], dtype=tf.float64)
  maindiag = tf.constant([2, 2, 2], dtype=tf.float64)
  subdiag = tf.constant([0, -1, -1], dtype=tf.float64)
  diagonals = [superdiag, maindiag, subdiag]
  rhs = tf.constant([[1, 1], [1, 1], [1, 1]], dtype=tf.float64)
  x = tf.linalg.tridiagonal_matmul(diagonals, rhs, diagonals_format='sequence')
  ```

  Args:
    diagonals: A `Tensor` or tuple of `Tensor`s describing left-hand sides. The
      shape depends of `diagonals_format`, see description above. Must be
      `float32`, `float64`, `complex64`, or `complex128`.
    rhs: A `Tensor` of shape [..., M, N] and with the same dtype as `diagonals`.
    diagonals_format: one of `sequence`, or `compact`. Default is `compact`.
    name:  A name to give this `Op` (optional).

  Returns:
    A `Tensor` of shape [..., M, N] containing the result of multiplication.

  Raises:
    ValueError: An unsupported type is provided as input, or when the input
    tensors have incorrect shapes.
  """
def matrix_rank(a, tol: Incomplete | None = None, validate_args: bool = False, name: Incomplete | None = None):
    """Compute the matrix rank of one or more matrices.

  Args:
    a: (Batch of) `float`-like matrix-shaped `Tensor`(s) which are to be
      pseudo-inverted.
    tol: Threshold below which the singular value is counted as 'zero'.
      Default value: `None` (i.e., `eps * max(rows, cols) * max(singular_val)`).
    validate_args: When `True`, additional assertions might be embedded in the
      graph.
      Default value: `False` (i.e., no graph assertions are added).
    name: Python `str` prefixed to ops created by this function.
      Default value: 'matrix_rank'.

  Returns:
    matrix_rank: (Batch of) `int32` scalars representing the number of non-zero
      singular values.
  """
def pinv(a, rcond: Incomplete | None = None, validate_args: bool = False, name: Incomplete | None = None):
    """Compute the Moore-Penrose pseudo-inverse of one or more matrices.

  Calculate the [generalized inverse of a matrix](
  https://en.wikipedia.org/wiki/Moore%E2%80%93Penrose_inverse) using its
  singular-value decomposition (SVD) and including all large singular values.

  The pseudo-inverse of a matrix `A`, is defined as: 'the matrix that 'solves'
  [the least-squares problem] `A @ x = b`,' i.e., if `x_hat` is a solution, then
  `A_pinv` is the matrix such that `x_hat = A_pinv @ b`. It can be shown that if
  `U @ Sigma @ V.T = A` is the singular value decomposition of `A`, then
  `A_pinv = V @ inv(Sigma) U^T`. [(Strang, 1980)][1]

  This function is analogous to [`numpy.linalg.pinv`](
  https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.pinv.html).
  It differs only in default value of `rcond`. In `numpy.linalg.pinv`, the
  default `rcond` is `1e-15`. Here the default is
  `10. * max(num_rows, num_cols) * np.finfo(dtype).eps`.

  Args:
    a: (Batch of) `float`-like matrix-shaped `Tensor`(s) which are to be
      pseudo-inverted.
    rcond: `Tensor` of small singular value cutoffs.  Singular values smaller
      (in modulus) than `rcond` * largest_singular_value (again, in modulus) are
      set to zero. Must broadcast against `tf.shape(a)[:-2]`.
      Default value: `10. * max(num_rows, num_cols) * np.finfo(a.dtype).eps`.
    validate_args: When `True`, additional assertions might be embedded in the
      graph.
      Default value: `False` (i.e., no graph assertions are added).
    name: Python `str` prefixed to ops created by this function.
      Default value: 'pinv'.

  Returns:
    a_pinv: (Batch of) pseudo-inverse of input `a`. Has same shape as `a` except
      rightmost two dimensions are transposed.

  Raises:
    TypeError: if input `a` does not have `float`-like `dtype`.
    ValueError: if input `a` has fewer than 2 dimensions.

  #### Examples

  ```python
  import tensorflow as tf
  import tensorflow_probability as tfp

  a = tf.constant([[1.,  0.4,  0.5],
                   [0.4, 0.2,  0.25],
                   [0.5, 0.25, 0.35]])
  tf.matmul(tf.linalg.pinv(a), a)
  # ==> array([[1., 0., 0.],
               [0., 1., 0.],
               [0., 0., 1.]], dtype=float32)

  a = tf.constant([[1.,  0.4,  0.5,  1.],
                   [0.4, 0.2,  0.25, 2.],
                   [0.5, 0.25, 0.35, 3.]])
  tf.matmul(tf.linalg.pinv(a), a)
  # ==> array([[ 0.76,  0.37,  0.21, -0.02],
               [ 0.37,  0.43, -0.33,  0.02],
               [ 0.21, -0.33,  0.81,  0.01],
               [-0.02,  0.02,  0.01,  1.  ]], dtype=float32)
  ```

  #### References

  [1]: G. Strang. 'Linear Algebra and Its Applications, 2nd Ed.' Academic Press,
       Inc., 1980, pp. 139-142.
  """
def lu_solve(lower_upper, perm, rhs, validate_args: bool = False, name: Incomplete | None = None):
    """Solves systems of linear eqns `A X = RHS`, given LU factorizations.

  Note: this function does not verify the implied matrix is actually invertible
  nor is this condition checked even when `validate_args=True`.

  Args:
    lower_upper: `lu` as returned by `tf.linalg.lu`, i.e., if `matmul(P,
      matmul(L, U)) = X` then `lower_upper = L + U - eye`.
    perm: `p` as returned by `tf.linag.lu`, i.e., if `matmul(P, matmul(L, U)) =
      X` then `perm = argmax(P)`.
    rhs: Matrix-shaped float `Tensor` representing targets for which to solve;
      `A X = RHS`. To handle vector cases, use: `lu_solve(..., rhs[...,
        tf.newaxis])[..., 0]`.
    validate_args: Python `bool` indicating whether arguments should be checked
      for correctness. Note: this function does not verify the implied matrix is
        actually invertible, even when `validate_args=True`.
      Default value: `False` (i.e., don't validate arguments).
    name: Python `str` name given to ops managed by this object.
      Default value: `None` (i.e., 'lu_solve').

  Returns:
    x: The `X` in `A @ X = RHS`.

  #### Examples

  ```python
  import numpy as np
  import tensorflow as tf
  import tensorflow_probability as tfp

  x = [[[1., 2],
        [3, 4]],
       [[7, 8],
        [3, 4]]]
  inv_x = tf.linalg.lu_solve(*tf.linalg.lu(x), rhs=tf.eye(2))
  tf.assert_near(tf.matrix_inverse(x), inv_x)
  # ==> True
  ```

  """
def lu_matrix_inverse(lower_upper, perm, validate_args: bool = False, name: Incomplete | None = None):
    """Computes the inverse given the LU decomposition(s) of one or more matrices.

  This op is conceptually identical to,

  ```python
  inv_X = tf.lu_matrix_inverse(*tf.linalg.lu(X))
  tf.assert_near(tf.matrix_inverse(X), inv_X)
  # ==> True
  ```

  Note: this function does not verify the implied matrix is actually invertible
  nor is this condition checked even when `validate_args=True`.

  Args:
    lower_upper: `lu` as returned by `tf.linalg.lu`, i.e., if `matmul(P,
      matmul(L, U)) = X` then `lower_upper = L + U - eye`.
    perm: `p` as returned by `tf.linag.lu`, i.e., if `matmul(P, matmul(L, U)) =
      X` then `perm = argmax(P)`.
    validate_args: Python `bool` indicating whether arguments should be checked
      for correctness. Note: this function does not verify the implied matrix is
        actually invertible, even when `validate_args=True`.
      Default value: `False` (i.e., don't validate arguments).
    name: Python `str` name given to ops managed by this object.
      Default value: `None` (i.e., 'lu_matrix_inverse').

  Returns:
    inv_x: The matrix_inv, i.e.,
      `tf.matrix_inverse(tf.linalg.lu_reconstruct(lu, perm))`.

  #### Examples

  ```python
  import numpy as np
  import tensorflow as tf
  import tensorflow_probability as tfp

  x = [[[3., 4], [1, 2]],
       [[7., 8], [3, 4]]]
  inv_x = tf.linalg.lu_matrix_inverse(*tf.linalg.lu(x))
  tf.assert_near(tf.matrix_inverse(x), inv_x)
  # ==> True
  ```

  """
def lu_reconstruct(lower_upper, perm, validate_args: bool = False, name: Incomplete | None = None):
    """The reconstruct one or more matrices from their LU decomposition(s).

  Args:
    lower_upper: `lu` as returned by `tf.linalg.lu`, i.e., if `matmul(P,
      matmul(L, U)) = X` then `lower_upper = L + U - eye`.
    perm: `p` as returned by `tf.linag.lu`, i.e., if `matmul(P, matmul(L, U)) =
      X` then `perm = argmax(P)`.
    validate_args: Python `bool` indicating whether arguments should be checked
      for correctness.
      Default value: `False` (i.e., don't validate arguments).
    name: Python `str` name given to ops managed by this object.
      Default value: `None` (i.e., 'lu_reconstruct').

  Returns:
    x: The original input to `tf.linalg.lu`, i.e., `x` as in,
      `lu_reconstruct(*tf.linalg.lu(x))`.

  #### Examples

  ```python
  import numpy as np
  import tensorflow as tf
  import tensorflow_probability as tfp

  x = [[[3., 4], [1, 2]],
       [[7., 8], [3, 4]]]
  x_reconstructed = tf.linalg.lu_reconstruct(*tf.linalg.lu(x))
  tf.assert_near(x, x_reconstructed)
  # ==> True
  ```

  """
def lu_reconstruct_assertions(lower_upper, perm, validate_args):
    """Returns list of assertions related to `lu_reconstruct` assumptions."""
def eigh_tridiagonal(alpha, beta, eigvals_only: bool = True, select: str = 'a', select_range: Incomplete | None = None, tol: Incomplete | None = None, name: Incomplete | None = None):
    """Computes the eigenvalues of a Hermitian tridiagonal matrix.

  Args:
    alpha: A real or complex tensor of shape (n), the diagonal elements of the
      matrix. NOTE: If alpha is complex, the imaginary part is ignored (assumed
        zero) to satisfy the requirement that the matrix be Hermitian.
    beta: A real or complex tensor of shape (n-1), containing the elements of
      the first super-diagonal of the matrix. If beta is complex, the first
      sub-diagonal of the matrix is assumed to be the conjugate of beta to
      satisfy the requirement that the matrix be Hermitian
    eigvals_only: If False, both eigenvalues and corresponding eigenvectors are
      computed. If True, only eigenvalues are computed. Default is True.
    select: Optional string with values in {‘a’, ‘v’, ‘i’} (default is 'a') that
      determines which eigenvalues to calculate:
        'a': all eigenvalues.
        ‘v’: eigenvalues in the interval (min, max] given by `select_range`.
        'i’: eigenvalues with indices min <= i <= max.
    select_range: Size 2 tuple or list or tensor specifying the range of
      eigenvalues to compute together with select. If select is 'a',
      select_range is ignored.
    tol: Optional scalar. The absolute tolerance to which each eigenvalue is
      required. An eigenvalue (or cluster) is considered to have converged if it
      lies in an interval of this width. If tol is None (default), the value
      eps*|T|_2 is used where eps is the machine precision, and |T|_2 is the
      2-norm of the matrix T.
    name: Optional name of the op.

  Returns:
    eig_vals: The eigenvalues of the matrix in non-decreasing order.
    eig_vectors: If `eigvals_only` is False the eigenvectors are returned in
      the second output argument.

  Raises:
     ValueError: If input values are invalid.
     NotImplemented: Computing eigenvectors for `eigvals_only` = False is
       not implemented yet.

  This op implements a subset of the functionality of
  scipy.linalg.eigh_tridiagonal.

  Note: The result is undefined if the input contains +/-inf or NaN, or if
  any value in beta has a magnitude greater than
  `numpy.sqrt(numpy.finfo(beta.dtype.as_numpy_dtype).max)`.


  TODO(b/187527398):
    Add support for outer batch dimensions.

  #### Examples

  ```python
  import numpy
  eigvals = tf.linalg.eigh_tridiagonal([0.0, 0.0, 0.0], [1.0, 1.0])
  eigvals_expected = [-numpy.sqrt(2.0), 0.0, numpy.sqrt(2.0)]
  tf.assert_near(eigvals_expected, eigvals)
  # ==> True
  ```

  """
