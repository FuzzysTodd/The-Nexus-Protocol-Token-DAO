from _typeshed import Incomplete
from tensorflow.python.ops.linalg import linear_operator

__all__ = ['LinearOperatorHouseholder']

class LinearOperatorHouseholder(linear_operator.LinearOperator):
    """`LinearOperator` acting like a [batch] of Householder transformations.

  This operator acts like a [batch] of householder reflections with shape
  `[B1,...,Bb, N, N]` for some `b >= 0`.  The first `b` indices index a
  batch member.  For every batch index `(i1,...,ib)`, `A[i1,...,ib, : :]` is
  an `N x N` matrix.  This matrix `A` is not materialized, but for
  purposes of broadcasting this shape will be relevant.

  `LinearOperatorHouseholder` is initialized with a (batch) vector.

  A Householder reflection, defined via a vector `v`, which reflects points
  in `R^n` about the hyperplane orthogonal to `v` and through the origin.

  ```python
  # Create a 2 x 2 householder transform.
  vec = [1 / np.sqrt(2), 1. / np.sqrt(2)]
  operator = LinearOperatorHouseholder(vec)

  operator.to_dense()
  ==> [[0.,  -1.]
       [-1., -0.]]

  operator.shape
  ==> [2, 2]

  operator.log_abs_determinant()
  ==> scalar Tensor

  x = ... Shape [2, 4] Tensor
  operator.matmul(x)
  ==> Shape [2, 4] Tensor
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
    def __init__(self, reflection_axis, is_non_singular: Incomplete | None = None, is_self_adjoint: Incomplete | None = None, is_positive_definite: Incomplete | None = None, is_square: Incomplete | None = None, name: str = 'LinearOperatorHouseholder') -> None:
        """Initialize a `LinearOperatorHouseholder`.

    Args:
      reflection_axis:  Shape `[B1,...,Bb, N]` `Tensor` with `b >= 0` `N >= 0`.
        The vector defining the hyperplane to reflect about.
        Allowed dtypes: `float16`, `float32`, `float64`, `complex64`,
        `complex128`.
      is_non_singular:  Expect that this operator is non-singular.
      is_self_adjoint:  Expect that this operator is equal to its hermitian
        transpose.  This is autoset to true
      is_positive_definite:  Expect that this operator is positive definite,
        meaning the quadratic form `x^H A x` has positive real part for all
        nonzero `x`.  Note that we do not require the operator to be
        self-adjoint to be positive-definite.  See:
        https://en.wikipedia.org/wiki/Positive-definite_matrix#Extension_for_non-symmetric_matrices
        This is autoset to false.
      is_square:  Expect that this operator acts like square [batch] matrices.
        This is autoset to true.
      name: A name for this `LinearOperator`.

    Raises:
      ValueError:  `is_self_adjoint` is not `True`, `is_positive_definite` is
        not `False` or `is_square` is not `True`.
    """
    @property
    def reflection_axis(self): ...
