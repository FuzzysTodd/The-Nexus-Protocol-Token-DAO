from _typeshed import Incomplete
from tensorflow.python.ops.linalg import linear_operator

__all__ = ['LinearOperatorLowerTriangular']

class LinearOperatorLowerTriangular(linear_operator.LinearOperator):
    """`LinearOperator` acting like a [batch] square lower triangular matrix.

  This operator acts like a [batch] lower triangular matrix `A` with shape
  `[B1,...,Bb, N, N]` for some `b >= 0`.  The first `b` indices index a
  batch member.  For every batch index `(i1,...,ib)`, `A[i1,...,ib, : :]` is
  an `N x N` matrix.

  `LinearOperatorLowerTriangular` is initialized with a `Tensor` having
  dimensions `[B1,...,Bb, N, N]`. The upper triangle of the last two
  dimensions is ignored.

  ```python
  # Create a 2 x 2 lower-triangular linear operator.
  tril = [[1., 2.], [3., 4.]]
  operator = LinearOperatorLowerTriangular(tril)

  # The upper triangle is ignored.
  operator.to_dense()
  ==> [[1., 0.]
       [3., 4.]]

  operator.shape
  ==> [2, 2]

  operator.log_abs_determinant()
  ==> scalar Tensor

  x = ... Shape [2, 4] Tensor
  operator.matmul(x)
  ==> Shape [2, 4] Tensor

  # Create a [2, 3] batch of 4 x 4 linear operators.
  tril = tf.random.normal(shape=[2, 3, 4, 4])
  operator = LinearOperatorLowerTriangular(tril)
  ```

  #### Shape compatibility

  This operator acts on [batch] matrix with compatible shape.
  `x` is a batch matrix with compatible shape for `matmul` and `solve` if

  ```
  operator.shape = [B1,...,Bb] + [N, N],  with b >= 0
  x.shape =        [B1,...,Bb] + [N, R],  with R >= 0.
  ```

  #### Performance

  Suppose `operator` is a `LinearOperatorLowerTriangular` of shape `[N, N]`,
  and `x.shape = [N, R]`.  Then

  * `operator.matmul(x)` involves `N^2 * R` multiplications.
  * `operator.solve(x)` involves `N * R` size `N` back-substitutions.
  * `operator.determinant()` involves a size `N` `reduce_prod`.

  If instead `operator` and `x` have shape `[B1,...,Bb, N, N]` and
  `[B1,...,Bb, N, R]`, every operation increases in complexity by `B1*...*Bb`.

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
    def __init__(self, tril, is_non_singular: Incomplete | None = None, is_self_adjoint: Incomplete | None = None, is_positive_definite: Incomplete | None = None, is_square: Incomplete | None = None, name: str = 'LinearOperatorLowerTriangular') -> None:
        """Initialize a `LinearOperatorLowerTriangular`.

    Args:
      tril:  Shape `[B1,...,Bb, N, N]` with `b >= 0`, `N >= 0`.
        The lower triangular part of `tril` defines this operator.  The strictly
        upper triangle is ignored.
      is_non_singular:  Expect that this operator is non-singular.
        This operator is non-singular if and only if its diagonal elements are
        all non-zero.
      is_self_adjoint:  Expect that this operator is equal to its hermitian
        transpose.  This operator is self-adjoint only if it is diagonal with
        real-valued diagonal entries.  In this case it is advised to use
        `LinearOperatorDiag`.
      is_positive_definite:  Expect that this operator is positive definite,
        meaning the quadratic form `x^H A x` has positive real part for all
        nonzero `x`.  Note that we do not require the operator to be
        self-adjoint to be positive-definite.  See:
        https://en.wikipedia.org/wiki/Positive-definite_matrix#Extension_for_non-symmetric_matrices
      is_square:  Expect that this operator acts like square [batch] matrices.
      name: A name for this `LinearOperator`.

    Raises:
      ValueError:  If `is_square` is `False`.
    """
    @property
    def tril(self):
        """The lower triangular matrix defining this operator."""
