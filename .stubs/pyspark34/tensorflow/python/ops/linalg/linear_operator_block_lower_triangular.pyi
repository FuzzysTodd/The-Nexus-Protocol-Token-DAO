from _typeshed import Incomplete
from tensorflow.python.ops.linalg import linear_operator

__all__ = ['LinearOperatorBlockLowerTriangular']

class LinearOperatorBlockLowerTriangular(linear_operator.LinearOperator):
    """Combines `LinearOperators` into a blockwise lower-triangular matrix.

  This operator is initialized with a nested list of linear operators, which
  are combined into a new `LinearOperator` whose underlying matrix
  representation is square and has each operator on or below the main diagonal,
  and zero's elsewhere. Each element of the outer list is a list of
  `LinearOperators` corresponding to a row-partition of the blockwise structure.
  The number of `LinearOperator`s in row-partion `i` must be equal to `i`.

  For example, a blockwise `3 x 3` `LinearOperatorBlockLowerTriangular` is
  initialized with the list `[[op_00], [op_10, op_11], [op_20, op_21, op_22]]`,
  where the `op_ij`, `i < 3, j <= i`, are `LinearOperator` instances. The
  `LinearOperatorBlockLowerTriangular` behaves as the following blockwise
  matrix, where `0` represents appropriately-sized [batch] matrices of zeros:

  ```none
  [[op_00,     0,     0],
   [op_10, op_11,     0],
   [op_20, op_21, op_22]]
  ```

  Each `op_jj` on the diagonal is required to represent a square matrix, and
  hence will have shape `batch_shape_j + [M_j, M_j]`. `LinearOperator`s in row
  `j` of the blockwise structure must have `range_dimension` equal to that of
  `op_jj`, and `LinearOperators` in column `j` must have `domain_dimension`
  equal to that of `op_jj`.

  If each `op_jj` on the diagonal has shape `batch_shape_j + [M_j, M_j]`, then
  the combined operator has shape `broadcast_batch_shape + [sum M_j, sum M_j]`,
  where `broadcast_batch_shape` is the mutual broadcast of `batch_shape_j`,
  `j = 0, 1, ..., J`, assuming the intermediate batch shapes broadcast.
  Even if the combined shape is well defined, the combined operator's
  methods may fail due to lack of broadcasting ability in the defining
  operators' methods.

  For example, to create a 4 x 4 linear operator combined of three 2 x 2
  operators:
  >>> operator_0 = tf.linalg.LinearOperatorFullMatrix([[1., 2.], [3., 4.]])
  >>> operator_1 = tf.linalg.LinearOperatorFullMatrix([[1., 0.], [0., 1.]])
  >>> operator_2 = tf.linalg.LinearOperatorLowerTriangular([[5., 6.], [7., 8]])
  >>> operator = LinearOperatorBlockLowerTriangular(
  ...   [[operator_0], [operator_1, operator_2]])

  >>> operator.to_dense()
  <tf.Tensor: shape=(4, 4), dtype=float32, numpy=
  array([[1., 2., 0., 0.],
         [3., 4., 0., 0.],
         [1., 0., 5., 0.],
         [0., 1., 7., 8.]], dtype=float32)>

  >>> operator.shape
  TensorShape([4, 4])

  >>> operator.log_abs_determinant()
  <tf.Tensor: shape=(), dtype=float32, numpy=4.3820267>

  >>> x0 = [[1., 6.], [-3., 4.]]
  >>> x1 = [[0., 2.], [4., 0.]]
  >>> x = tf.concat([x0, x1], 0)  # Shape [2, 4] Tensor
  >>> operator.matmul(x)
  <tf.Tensor: shape=(4, 2), dtype=float32, numpy=
  array([[-5., 14.],
         [-9., 34.],
         [ 1., 16.],
         [29., 18.]], dtype=float32)>

  The above `matmul` is equivalent to:
  >>> tf.concat([operator_0.matmul(x0),
  ...   operator_1.matmul(x0) + operator_2.matmul(x1)], axis=0)
  <tf.Tensor: shape=(4, 2), dtype=float32, numpy=
  array([[-5., 14.],
         [-9., 34.],
         [ 1., 16.],
         [29., 18.]], dtype=float32)>

  #### Shape compatibility

  This operator acts on [batch] matrix with compatible shape.
  `x` is a batch matrix with compatible shape for `matmul` and `solve` if

  ```
  operator.shape = [B1,...,Bb] + [M, N],  with b >= 0
  x.shape =        [B1,...,Bb] + [N, R],  with R >= 0.
  ```

  For example:

  Create a [2, 3] batch of 4 x 4 linear operators:
  >>> matrix_44 = tf.random.normal(shape=[2, 3, 4, 4])
  >>> operator_44 = tf.linalg.LinearOperatorFullMatrix(matrix_44)

  Create a [1, 3] batch of 5 x 4 linear operators:
  >>> matrix_54 = tf.random.normal(shape=[1, 3, 5, 4])
  >>> operator_54 = tf.linalg.LinearOperatorFullMatrix(matrix_54)

  Create a [1, 3] batch of 5 x 5 linear operators:
  >>> matrix_55 = tf.random.normal(shape=[1, 3, 5, 5])
  >>> operator_55 = tf.linalg.LinearOperatorFullMatrix(matrix_55)

  Combine to create a [2, 3] batch of 9 x 9 operators:
  >>> operator_99 = LinearOperatorBlockLowerTriangular(
  ...   [[operator_44], [operator_54, operator_55]])
  >>> operator_99.shape
  TensorShape([2, 3, 9, 9])

  Create a shape [2, 1, 9] batch of vectors and apply the operator to it.
  >>> x = tf.random.normal(shape=[2, 1, 9])
  >>> y = operator_99.matvec(x)
  >>> y.shape
  TensorShape([2, 3, 9])

  Create a blockwise list of vectors and apply the operator to it. A blockwise
  list is returned.
  >>> x4 = tf.random.normal(shape=[2, 1, 4])
  >>> x5 = tf.random.normal(shape=[2, 3, 5])
  >>> y_blockwise = operator_99.matvec([x4, x5])
  >>> y_blockwise[0].shape
  TensorShape([2, 3, 4])
  >>> y_blockwise[1].shape
  TensorShape([2, 3, 5])

  #### Performance

  Suppose `operator` is a `LinearOperatorBlockLowerTriangular` consisting of `D`
  row-partitions and `D` column-partitions, such that the total number of
  operators is `N = D * (D + 1) // 2`.

  * `operator.matmul` has complexity equal to the sum of the `matmul`
    complexities of the individual operators.
  * `operator.solve` has complexity equal to the sum of the `solve` complexities
    of the operators on the diagonal and the `matmul` complexities of the
    operators off the diagonal.
  * `operator.determinant` has complexity equal to the sum of the `determinant`
    complexities of the operators on the diagonal.

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
    def __init__(self, operators, is_non_singular: Incomplete | None = None, is_self_adjoint: Incomplete | None = None, is_positive_definite: Incomplete | None = None, is_square: Incomplete | None = None, name: str = 'LinearOperatorBlockLowerTriangular') -> None:
        """Initialize a `LinearOperatorBlockLowerTriangular`.

    `LinearOperatorBlockLowerTriangular` is initialized with a list of lists of
    operators `[[op_0], [op_1, op_2], [op_3, op_4, op_5],...]`.

    Args:
      operators:  Iterable of iterables of `LinearOperator` objects, each with
        the same `dtype`. Each element of `operators` corresponds to a row-
        partition, in top-to-bottom order. The operators in each row-partition
        are filled in left-to-right. For example,
        `operators = [[op_0], [op_1, op_2], [op_3, op_4, op_5]]` creates a
        `LinearOperatorBlockLowerTriangular` with full block structure
        `[[op_0, 0, 0], [op_1, op_2, 0], [op_3, op_4, op_5]]`. The number of
        operators in the `i`th row must be equal to `i`, such that each operator
        falls on or below the diagonal of the blockwise structure.
        `LinearOperator`s that fall on the diagonal (the last elements of each
        row) must be square. The other `LinearOperator`s must have domain
        dimension equal to the domain dimension of the `LinearOperator`s in the
        same column-partition, and range dimension equal to the range dimension
        of the `LinearOperator`s in the same row-partition.
      is_non_singular:  Expect that this operator is non-singular.
      is_self_adjoint:  Expect that this operator is equal to its hermitian
        transpose.
      is_positive_definite:  Expect that this operator is positive definite,
        meaning the quadratic form `x^H A x` has positive real part for all
        nonzero `x`.  Note that we do not require the operator to be
        self-adjoint to be positive-definite.  See:
        https://en.wikipedia.org/wiki/Positive-definite_matrix#Extension_for_non-symmetric_matrices
      is_square:  Expect that this operator acts like square [batch] matrices.
        This will raise a `ValueError` if set to `False`.
      name: A name for this `LinearOperator`.

    Raises:
      TypeError:  If all operators do not have the same `dtype`.
      ValueError:  If `operators` is empty, contains an erroneous number of
        elements, or contains operators with incompatible shapes.
    """
    @property
    def operators(self): ...
    def matmul(self, x, adjoint: bool = False, adjoint_arg: bool = False, name: str = 'matmul'):
        """Transform [batch] matrix `x` with left multiplication:  `x --> Ax`.

    ```python
    # Make an operator acting like batch matrix A.  Assume A.shape = [..., M, N]
    operator = LinearOperator(...)
    operator.shape = [..., M, N]

    X = ... # shape [..., N, R], batch matrix, R > 0.

    Y = operator.matmul(X)
    Y.shape
    ==> [..., M, R]

    Y[..., :, r] = sum_j A[..., :, j] X[j, r]
    ```

    Args:
      x: `LinearOperator`, `Tensor` with compatible shape and same `dtype` as
        `self`, or a blockwise iterable of `LinearOperator`s or `Tensor`s. See
        class docstring for definition of shape compatibility.
      adjoint: Python `bool`.  If `True`, left multiply by the adjoint: `A^H x`.
      adjoint_arg:  Python `bool`.  If `True`, compute `A x^H` where `x^H` is
        the hermitian transpose (transposition and complex conjugation).
      name:  A name for this `Op`.

    Returns:
      A `LinearOperator` or `Tensor` with shape `[..., M, R]` and same `dtype`
        as `self`, or if `x` is blockwise, a list of `Tensor`s with shapes that
        concatenate to `[..., M, R]`.
    """
    def matvec(self, x, adjoint: bool = False, name: str = 'matvec'):
        """Transform [batch] vector `x` with left multiplication:  `x --> Ax`.

    ```python
    # Make an operator acting like batch matrix A.  Assume A.shape = [..., M, N]
    operator = LinearOperator(...)

    X = ... # shape [..., N], batch vector

    Y = operator.matvec(X)
    Y.shape
    ==> [..., M]

    Y[..., :] = sum_j A[..., :, j] X[..., j]
    ```

    Args:
      x: `Tensor` with compatible shape and same `dtype` as `self`, or an
        iterable of `Tensor`s. `Tensor`s are treated a [batch] vectors, meaning
        for every set of leading dimensions, the last dimension defines a
        vector.
        See class docstring for definition of compatibility.
      adjoint: Python `bool`.  If `True`, left multiply by the adjoint: `A^H x`.
      name:  A name for this `Op`.

    Returns:
      A `Tensor` with shape `[..., M]` and same `dtype` as `self`.
    """
    def solve(self, rhs, adjoint: bool = False, adjoint_arg: bool = False, name: str = 'solve'):
        """Solve (exact or approx) `R` (batch) systems of equations: `A X = rhs`.

    The returned `Tensor` will be close to an exact solution if `A` is well
    conditioned. Otherwise closeness will vary. See class docstring for details.

    Given the blockwise `n + 1`-by-`n + 1` linear operator:

    op = [[A_00     0  ...     0  ...    0],
          [A_10  A_11  ...     0  ...    0],
          ...
          [A_k0  A_k1  ...  A_kk  ...    0],
          ...
          [A_n0  A_n1  ...  A_nk  ... A_nn]]

    we find `x = op.solve(y)` by observing that

    `y_k = A_k0.matmul(x_0) + A_k1.matmul(x_1) + ... + A_kk.matmul(x_k)`

    and therefore

    `x_k = A_kk.solve(y_k -
                      A_k0.matmul(x_0) - ... - A_k(k-1).matmul(x_(k-1)))`

    where `x_k` and `y_k` are the `k`th blocks obtained by decomposing `x`
    and `y` along their appropriate axes.

    We first solve `x_0 = A_00.solve(y_0)`. Proceeding inductively, we solve
    for `x_k`, `k = 1..n`, given `x_0..x_(k-1)`.

    The adjoint case is solved similarly, beginning with
    `x_n = A_nn.solve(y_n, adjoint=True)` and proceeding backwards.

    Examples:

    ```python
    # Make an operator acting like batch matrix A.  Assume A.shape = [..., M, N]
    operator = LinearOperator(...)
    operator.shape = [..., M, N]

    # Solve R > 0 linear systems for every member of the batch.
    RHS = ... # shape [..., M, R]

    X = operator.solve(RHS)
    # X[..., :, r] is the solution to the r'th linear system
    # sum_j A[..., :, j] X[..., j, r] = RHS[..., :, r]

    operator.matmul(X)
    ==> RHS
    ```

    Args:
      rhs: `Tensor` with same `dtype` as this operator and compatible shape,
        or a list of `Tensor`s. `Tensor`s are treated like a [batch] matrices
        meaning for every set of leading dimensions, the last two dimensions
        defines a matrix.
        See class docstring for definition of compatibility.
      adjoint: Python `bool`.  If `True`, solve the system involving the adjoint
        of this `LinearOperator`:  `A^H X = rhs`.
      adjoint_arg:  Python `bool`.  If `True`, solve `A X = rhs^H` where `rhs^H`
        is the hermitian transpose (transposition and complex conjugation).
      name:  A name scope to use for ops added by this method.

    Returns:
      `Tensor` with shape `[...,N, R]` and same `dtype` as `rhs`.

    Raises:
      NotImplementedError:  If `self.is_non_singular` or `is_square` is False.
    """
    def solvevec(self, rhs, adjoint: bool = False, name: str = 'solve'):
        """Solve single equation with best effort: `A X = rhs`.

    The returned `Tensor` will be close to an exact solution if `A` is well
    conditioned. Otherwise closeness will vary. See class docstring for details.

    Examples:

    ```python
    # Make an operator acting like batch matrix A.  Assume A.shape = [..., M, N]
    operator = LinearOperator(...)
    operator.shape = [..., M, N]

    # Solve one linear system for every member of the batch.
    RHS = ... # shape [..., M]

    X = operator.solvevec(RHS)
    # X is the solution to the linear system
    # sum_j A[..., :, j] X[..., j] = RHS[..., :]

    operator.matvec(X)
    ==> RHS
    ```

    Args:
      rhs: `Tensor` with same `dtype` as this operator, or list of `Tensor`s
        (for blockwise operators). `Tensor`s are treated as [batch] vectors,
        meaning for every set of leading dimensions, the last dimension defines
        a vector.  See class docstring for definition of compatibility regarding
        batch dimensions.
      adjoint: Python `bool`.  If `True`, solve the system involving the adjoint
        of this `LinearOperator`:  `A^H X = rhs`.
      name:  A name scope to use for ops added by this method.

    Returns:
      `Tensor` with shape `[...,N]` and same `dtype` as `rhs`.

    Raises:
      NotImplementedError:  If `self.is_non_singular` or `is_square` is False.
    """
