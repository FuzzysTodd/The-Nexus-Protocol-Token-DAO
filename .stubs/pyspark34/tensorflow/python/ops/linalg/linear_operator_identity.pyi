from _typeshed import Incomplete
from tensorflow.python.ops.linalg import linear_operator

__all__ = ['LinearOperatorIdentity', 'LinearOperatorScaledIdentity']

class BaseLinearOperatorIdentity(linear_operator.LinearOperator):
    """Base class for Identity operators."""

class LinearOperatorIdentity(BaseLinearOperatorIdentity):
    """`LinearOperator` acting like a [batch] square identity matrix.

  This operator acts like a [batch] identity matrix `A` with shape
  `[B1,...,Bb, N, N]` for some `b >= 0`.  The first `b` indices index a
  batch member.  For every batch index `(i1,...,ib)`, `A[i1,...,ib, : :]` is
  an `N x N` matrix.  This matrix `A` is not materialized, but for
  purposes of broadcasting this shape will be relevant.

  `LinearOperatorIdentity` is initialized with `num_rows`, and optionally
  `batch_shape`, and `dtype` arguments.  If `batch_shape` is `None`, this
  operator efficiently passes through all arguments.  If `batch_shape` is
  provided, broadcasting may occur, which will require making copies.

  ```python
  # Create a 2 x 2 identity matrix.
  operator = LinearOperatorIdentity(num_rows=2, dtype=tf.float32)

  operator.to_dense()
  ==> [[1., 0.]
       [0., 1.]]

  operator.shape
  ==> [2, 2]

  operator.log_abs_determinant()
  ==> 0.

  x = ... Shape [2, 4] Tensor
  operator.matmul(x)
  ==> Shape [2, 4] Tensor, same as x.

  y = tf.random.normal(shape=[3, 2, 4])
  # Note that y.shape is compatible with operator.shape because operator.shape
  # is broadcast to [3, 2, 2].
  # This broadcast does NOT require copying data, since we can infer that y
  # will be passed through without changing shape.  We are always able to infer
  # this if the operator has no batch_shape.
  x = operator.solve(y)
  ==> Shape [3, 2, 4] Tensor, same as y.

  # Create a 2-batch of 2x2 identity matrices
  operator = LinearOperatorIdentity(num_rows=2, batch_shape=[2])
  operator.to_dense()
  ==> [[[1., 0.]
        [0., 1.]],
       [[1., 0.]
        [0., 1.]]]

  # Here, even though the operator has a batch shape, the input is the same as
  # the output, so x can be passed through without a copy.  The operator is able
  # to detect that no broadcast is necessary because both x and the operator
  # have statically defined shape.
  x = ... Shape [2, 2, 3]
  operator.matmul(x)
  ==> Shape [2, 2, 3] Tensor, same as x

  # Here the operator and x have different batch_shape, and are broadcast.
  # This requires a copy, since the output is different size than the input.
  x = ... Shape [1, 2, 3]
  operator.matmul(x)
  ==> Shape [2, 2, 3] Tensor, equal to [x, x]
  ```

  ### Shape compatibility

  This operator acts on [batch] matrix with compatible shape.
  `x` is a batch matrix with compatible shape for `matmul` and `solve` if

  ```
  operator.shape = [B1,...,Bb] + [N, N],  with b >= 0
  x.shape =   [C1,...,Cc] + [N, R],
  and [C1,...,Cc] broadcasts with [B1,...,Bb] to [D1,...,Dd]
  ```

  ### Performance

  If `batch_shape` initialization arg is `None`:

  * `operator.matmul(x)` is `O(1)`
  * `operator.solve(x)` is `O(1)`
  * `operator.determinant()` is `O(1)`

  If `batch_shape` initialization arg is provided, and static checks cannot
  rule out the need to broadcast:

  * `operator.matmul(x)` is `O(D1*...*Dd*N*R)`
  * `operator.solve(x)` is `O(D1*...*Dd*N*R)`
  * `operator.determinant()` is `O(B1*...*Bb)`

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
    def __init__(self, num_rows, batch_shape: Incomplete | None = None, dtype: Incomplete | None = None, is_non_singular: bool = True, is_self_adjoint: bool = True, is_positive_definite: bool = True, is_square: bool = True, assert_proper_shapes: bool = False, name: str = 'LinearOperatorIdentity') -> None:
        """Initialize a `LinearOperatorIdentity`.

    The `LinearOperatorIdentity` is initialized with arguments defining `dtype`
    and shape.

    This operator is able to broadcast the leading (batch) dimensions, which
    sometimes requires copying data.  If `batch_shape` is `None`, the operator
    can take arguments of any batch shape without copying.  See examples.

    Args:
      num_rows:  Scalar non-negative integer `Tensor`.  Number of rows in the
        corresponding identity matrix.
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
      ValueError:  If `batch_shape` is determined statically to not be 1-D, or
        negative.
      ValueError:  If any of the following is not `True`:
        `{is_self_adjoint, is_non_singular, is_positive_definite}`.
      TypeError:  If `num_rows` or `batch_shape` is ref-type (e.g. Variable).
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

class LinearOperatorScaledIdentity(BaseLinearOperatorIdentity):
    """`LinearOperator` acting like a scaled [batch] identity matrix `A = c I`.

  This operator acts like a scaled [batch] identity matrix `A` with shape
  `[B1,...,Bb, N, N]` for some `b >= 0`.  The first `b` indices index a
  batch member.  For every batch index `(i1,...,ib)`, `A[i1,...,ib, : :]` is
  a scaled version of the `N x N` identity matrix.

  `LinearOperatorIdentity` is initialized with `num_rows`, and a `multiplier`
  (a `Tensor`) of shape `[B1,...,Bb]`.  `N` is set to `num_rows`, and the
  `multiplier` determines the scale for each batch member.

  ```python
  # Create a 2 x 2 scaled identity matrix.
  operator = LinearOperatorIdentity(num_rows=2, multiplier=3.)

  operator.to_dense()
  ==> [[3., 0.]
       [0., 3.]]

  operator.shape
  ==> [2, 2]

  operator.log_abs_determinant()
  ==> 2 * Log[3]

  x = ... Shape [2, 4] Tensor
  operator.matmul(x)
  ==> 3 * x

  y = tf.random.normal(shape=[3, 2, 4])
  # Note that y.shape is compatible with operator.shape because operator.shape
  # is broadcast to [3, 2, 2].
  x = operator.solve(y)
  ==> 3 * x

  # Create a 2-batch of 2x2 identity matrices
  operator = LinearOperatorIdentity(num_rows=2, multiplier=5.)
  operator.to_dense()
  ==> [[[5., 0.]
        [0., 5.]],
       [[5., 0.]
        [0., 5.]]]

  x = ... Shape [2, 2, 3]
  operator.matmul(x)
  ==> 5 * x

  # Here the operator and x have different batch_shape, and are broadcast.
  x = ... Shape [1, 2, 3]
  operator.matmul(x)
  ==> 5 * x
  ```

  ### Shape compatibility

  This operator acts on [batch] matrix with compatible shape.
  `x` is a batch matrix with compatible shape for `matmul` and `solve` if

  ```
  operator.shape = [B1,...,Bb] + [N, N],  with b >= 0
  x.shape =   [C1,...,Cc] + [N, R],
  and [C1,...,Cc] broadcasts with [B1,...,Bb] to [D1,...,Dd]
  ```

  ### Performance

  * `operator.matmul(x)` is `O(D1*...*Dd*N*R)`
  * `operator.solve(x)` is `O(D1*...*Dd*N*R)`
  * `operator.determinant()` is `O(D1*...*Dd)`

  #### Matrix property hints

  This `LinearOperator` is initialized with boolean flags of the form `is_X`,
  for `X = non_singular, self_adjoint, positive_definite, square`.
  These have the following meaning
  * If `is_X == True`, callers should expect the operator to have the
    property `X`.  This is a promise that should be fulfilled, but is *not* a
    runtime assert.  For example, finite floating point precision may result
    in these promises being violated.
  * If `is_X == False`, callers should expect the operator to not have `X`.
  * If `is_X == None` (the default), callers should have no expectation either
    way.
  """
    def __init__(self, num_rows, multiplier, is_non_singular: Incomplete | None = None, is_self_adjoint: Incomplete | None = None, is_positive_definite: Incomplete | None = None, is_square: bool = True, assert_proper_shapes: bool = False, name: str = 'LinearOperatorScaledIdentity') -> None:
        """Initialize a `LinearOperatorScaledIdentity`.

    The `LinearOperatorScaledIdentity` is initialized with `num_rows`, which
    determines the size of each identity matrix, and a `multiplier`,
    which defines `dtype`, batch shape, and scale of each matrix.

    This operator is able to broadcast the leading (batch) dimensions.

    Args:
      num_rows:  Scalar non-negative integer `Tensor`.  Number of rows in the
        corresponding identity matrix.
      multiplier:  `Tensor` of shape `[B1,...,Bb]`, or `[]` (a scalar).
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
    """
    def add_to_tensor(self, mat, name: str = 'add_to_tensor'):
        """Add matrix represented by this operator to `mat`.  Equiv to `I + mat`.

    Args:
      mat:  `Tensor` with same `dtype` and shape broadcastable to `self`.
      name:  A name to give this `Op`.

    Returns:
      A `Tensor` with broadcast shape and same `dtype` as `self`.
    """
    @property
    def multiplier(self):
        """The [batch] scalar `Tensor`, `c` in `cI`."""
