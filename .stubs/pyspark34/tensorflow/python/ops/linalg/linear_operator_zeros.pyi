from _typeshed import Incomplete
from tensorflow.python.ops.linalg import linear_operator

__all__ = ['LinearOperatorZeros']

class LinearOperatorZeros(linear_operator.LinearOperator):
    """`LinearOperator` acting like a [batch] zero matrix.

  This operator acts like a [batch] zero matrix `A` with shape
  `[B1,...,Bb, N, M]` for some `b >= 0`.  The first `b` indices index a
  batch member.  For every batch index `(i1,...,ib)`, `A[i1,...,ib, : :]` is
  an `N x M` matrix.  This matrix `A` is not materialized, but for
  purposes of broadcasting this shape will be relevant.

  `LinearOperatorZeros` is initialized with `num_rows`, and optionally
  `num_columns, `batch_shape`, and `dtype` arguments.  If `num_columns` is
  `None`, then this operator will be initialized as a square matrix. If
  `batch_shape` is `None`, this operator efficiently passes through all
  arguments.  If `batch_shape` is provided, broadcasting may occur, which will
  require making copies.

  ```python
  # Create a 2 x 2 zero matrix.
  operator = LinearOperatorZero(num_rows=2, dtype=tf.float32)

  operator.to_dense()
  ==> [[0., 0.]
       [0., 0.]]

  operator.shape
  ==> [2, 2]

  operator.determinant()
  ==> 0.

  x = ... Shape [2, 4] Tensor
  operator.matmul(x)
  ==> Shape [2, 4] Tensor, same as x.

  # Create a 2-batch of 2x2 zero matrices
  operator = LinearOperatorZeros(num_rows=2, batch_shape=[2])
  operator.to_dense()
  ==> [[[0., 0.]
        [0., 0.]],
       [[0., 0.]
        [0., 0.]]]

  # Here, even though the operator has a batch shape, the input is the same as
  # the output, so x can be passed through without a copy.  The operator is able
  # to detect that no broadcast is necessary because both x and the operator
  # have statically defined shape.
  x = ... Shape [2, 2, 3]
  operator.matmul(x)
  ==> Shape [2, 2, 3] Tensor, same as tf.zeros_like(x)

  # Here the operator and x have different batch_shape, and are broadcast.
  # This requires a copy, since the output is different size than the input.
  x = ... Shape [1, 2, 3]
  operator.matmul(x)
  ==> Shape [2, 2, 3] Tensor, equal to tf.zeros_like([x, x])
  ```

  ### Shape compatibility

  This operator acts on [batch] matrix with compatible shape.
  `x` is a batch matrix with compatible shape for `matmul` and `solve` if

  ```
  operator.shape = [B1,...,Bb] + [N, M],  with b >= 0
  x.shape =   [C1,...,Cc] + [M, R],
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
    def __init__(self, num_rows, num_columns: Incomplete | None = None, batch_shape: Incomplete | None = None, dtype: Incomplete | None = None, is_non_singular: bool = False, is_self_adjoint: bool = True, is_positive_definite: bool = False, is_square: bool = True, assert_proper_shapes: bool = False, name: str = 'LinearOperatorZeros') -> None:
        """Initialize a `LinearOperatorZeros`.

    The `LinearOperatorZeros` is initialized with arguments defining `dtype`
    and shape.

    This operator is able to broadcast the leading (batch) dimensions, which
    sometimes requires copying data.  If `batch_shape` is `None`, the operator
    can take arguments of any batch shape without copying.  See examples.

    Args:
      num_rows:  Scalar non-negative integer `Tensor`.  Number of rows in the
        corresponding zero matrix.
      num_columns:  Scalar non-negative integer `Tensor`.  Number of columns in
        the corresponding zero matrix. If `None`, defaults to the value of
        `num_rows`.
      batch_shape:  Optional `1-D` integer `Tensor`.  The shape of the leading
        dimensions.  If `None`, this operator has no leading dimensions.
      dtype:  Data type of the matrix that this operator represents.
      is_non_singular:  Expect that this operator is non-singular.
      is_self_adjoint:  Expect that this operator is equal to its hermitian
        transpose.
      is_positive_definite:  Expect that this operator is positive definite,
        meaning the quadratic form `x^H A x` has positive real part for all
        nonzero `x`.  Note that we do not require the operator to be
        self-adjoint to be positive-definite.  See:
        https://en.wikipedia.org/wiki/Positive-definite_matrix#Extension_for_non-symmetric_matrices
      is_square:  Expect that this operator acts like square [batch] matrices.
      assert_proper_shapes:  Python `bool`.  If `False`, only perform static
        checks that initialization and method arguments have proper shape.
        If `True`, and static checks are inconclusive, add asserts to the graph.
      name: A name for this `LinearOperator`

    Raises:
      ValueError:  If `num_rows` is determined statically to be non-scalar, or
        negative.
      ValueError:  If `num_columns` is determined statically to be non-scalar,
        or negative.
      ValueError:  If `batch_shape` is determined statically to not be 1-D, or
        negative.
      ValueError:  If any of the following is not `True`:
        `{is_self_adjoint, is_non_singular, is_positive_definite}`.
    """
    def add_to_tensor(self, mat, name: str = 'add_to_tensor'):
        """Add matrix represented by this operator to `mat`.  Equiv to `I + mat`.

    Args:
      mat:  `Tensor` with same `dtype` and shape broadcastable to `self`.
      name:  A name to give this `Op`.

    Returns:
      A `Tensor` with broadcast shape and same `dtype` as `self`.
    """
    def __getitem__(self, slices): ...
