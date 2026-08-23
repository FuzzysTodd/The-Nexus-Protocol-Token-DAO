from _typeshed import Incomplete
from tensorflow.python.ops.linalg import linear_operator

__all__ = ['LinearOperatorDiag']

class LinearOperatorDiag(linear_operator.LinearOperator):
    """`LinearOperator` acting like a [batch] square diagonal matrix.

  This operator acts like a [batch] diagonal matrix `A` with shape
  `[B1,...,Bb, N, N]` for some `b >= 0`.  The first `b` indices index a
  batch member.  For every batch index `(i1,...,ib)`, `A[i1,...,ib, : :]` is
  an `N x N` matrix.  This matrix `A` is not materialized, but for
  purposes of broadcasting this shape will be relevant.

  `LinearOperatorDiag` is initialized with a (batch) vector.

  ```python
  # Create a 2 x 2 diagonal linear operator.
  diag = [1., -1.]
  operator = LinearOperatorDiag(diag)

  operator.to_dense()
  ==> [[1.,  0.]
       [0., -1.]]

  operator.shape
  ==> [2, 2]

  operator.log_abs_determinant()
  ==> scalar Tensor

  x = ... Shape [2, 4] Tensor
  operator.matmul(x)
  ==> Shape [2, 4] Tensor

  # Create a [2, 3] batch of 4 x 4 linear operators.
  diag = tf.random.normal(shape=[2, 3, 4])
  operator = LinearOperatorDiag(diag)

  # Create a shape [2, 1, 4, 2] vector.  Note that this shape is compatible
  # since the batch dimensions, [2, 1], are broadcast to
  # operator.batch_shape = [2, 3].
  y = tf.random.normal(shape=[2, 1, 4, 2])
  x = operator.solve(y)
  ==> operator.matmul(x) = y
  ```

  #### Shape compatibility

  This operator acts on [batch] matrix with compatible shape.
  `x` is a batch matrix with compatible shape for `matmul` and `solve` if

  ```
  operator.shape = [B1,...,Bb] + [N, N],  with b >= 0
  x.shape =   [C1,...,Cc] + [N, R],
  and [C1,...,Cc] broadcasts with [B1,...,Bb] to [D1,...,Dd]
  ```

  #### Performance

  Suppose `operator` is a `LinearOperatorDiag` of shape `[N, N]`,
  and `x.shape = [N, R]`.  Then

  * `operator.matmul(x)` involves `N * R` multiplications.
  * `operator.solve(x)` involves `N` divisions and `N * R` multiplications.
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
    def __init__(self, diag, is_non_singular: Incomplete | None = None, is_self_adjoint: Incomplete | None = None, is_positive_definite: Incomplete | None = None, is_square: Incomplete | None = None, name: str = 'LinearOperatorDiag') -> None:
        """Initialize a `LinearOperatorDiag`.

    Args:
      diag:  Shape `[B1,...,Bb, N]` `Tensor` with `b >= 0` `N >= 0`.
        The diagonal of the operator.  Allowed dtypes: `float16`, `float32`,
          `float64`, `complex64`, `complex128`.
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

    Raises:
      TypeError:  If `diag.dtype` is not an allowed type.
      ValueError:  If `diag.dtype` is real, and `is_self_adjoint` is not `True`.
    """
    @property
    def diag(self): ...
