from _typeshed import Incomplete
from tensorflow.python.ops.linalg import linear_operator

__all__ = ['LinearOperatorToeplitz']

class LinearOperatorToeplitz(linear_operator.LinearOperator):
    """`LinearOperator` acting like a [batch] of toeplitz matrices.

  This operator acts like a [batch] Toeplitz matrix `A` with shape
  `[B1,...,Bb, N, N]` for some `b >= 0`.  The first `b` indices index a
  batch member.  For every batch index `(i1,...,ib)`, `A[i1,...,ib, : :]` is
  an `N x N` matrix.  This matrix `A` is not materialized, but for
  purposes of broadcasting this shape will be relevant.

  #### Description in terms of toeplitz matrices

  Toeplitz means that `A` has constant diagonals. Hence, `A` can be generated
  with two vectors. One represents the first column of the matrix, and the
  other represents the first row.

  Below is a 4 x 4 example:

  ```
  A = |a b c d|
      |e a b c|
      |f e a b|
      |g f e a|
  ```

  #### Example of a Toeplitz operator.

  ```python
  # Create a 3 x 3 Toeplitz operator.
  col = [1., 2., 3.]
  row = [1., 4., -9.]
  operator = LinearOperatorToeplitz(col, row)

  operator.to_dense()
  ==> [[1., 4., -9.],
       [2., 1., 4.],
       [3., 2., 1.]]

  operator.shape
  ==> [3, 3]

  operator.log_abs_determinant()
  ==> scalar Tensor

  x = ... Shape [3, 4] Tensor
  operator.matmul(x)
  ==> Shape [3, 4] Tensor
  ```

  #### Shape compatibility

  This operator acts on [batch] matrix with compatible shape.
  `x` is a batch matrix with compatible shape for `matmul` and `solve` if

  ```
  operator.shape = [B1,...,Bb] + [N, N],  with b >= 0
  x.shape =   [C1,...,Cc] + [N, R],
  and [C1,...,Cc] broadcasts with [B1,...,Bb] to [D1,...,Dd]
  ```

  #### Matrix property hints

  This `LinearOperator` is initialized with boolean flags of the form `is_X`,
  for `X = non_singular, self_adjoint, positive_definite, square`.
  These have the following meaning:

  * If `is_X == True`, callers should expect the operator to have the
    property `X`.  This is a promise that should be fulfilled, but is *not* a
    runtime assert.  For example, finite floating point precision may result
    in these promises being violated.
  * If `is_X == False`, callers should expect the operator to not have `X`.
  * If `is_X == None` (the default), callers should have no expectation either
    way.
  """
    def __init__(self, col, row, is_non_singular: Incomplete | None = None, is_self_adjoint: Incomplete | None = None, is_positive_definite: Incomplete | None = None, is_square: Incomplete | None = None, name: str = 'LinearOperatorToeplitz') -> None:
        """Initialize a `LinearOperatorToeplitz`.

    Args:
      col: Shape `[B1,...,Bb, N]` `Tensor` with `b >= 0` `N >= 0`.
        The first column of the operator. Allowed dtypes: `float16`, `float32`,
          `float64`, `complex64`, `complex128`. Note that the first entry of
          `col` is assumed to be the same as the first entry of `row`.
      row: Shape `[B1,...,Bb, N]` `Tensor` with `b >= 0` `N >= 0`.
        The first row of the operator. Allowed dtypes: `float16`, `float32`,
          `float64`, `complex64`, `complex128`. Note that the first entry of
          `row` is assumed to be the same as the first entry of `col`.
      is_non_singular:  Expect that this operator is non-singular.
      is_self_adjoint:  Expect that this operator is equal to its hermitian
        transpose.  If `diag.dtype` is real, this is auto-set to `True`.
      is_positive_definite:  Expect that this operator is positive definite,
        meaning the quadratic form `x^H A x` has positive real part for all
        nonzero `x`.  Note that we do not require the operator to be
        self-adjoint to be positive-definite.  See:
        https://en.wikipedia.org/wiki/Positive-definite_matrix#Extension_for_non-symmetric_matrices
      is_square:  Expect that this operator acts like square [batch] matrices.
      name: A name for this `LinearOperator`.
    """
    @property
    def col(self): ...
    @property
    def row(self): ...
