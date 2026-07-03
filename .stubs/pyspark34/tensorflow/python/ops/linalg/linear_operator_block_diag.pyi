from _typeshed import Incomplete
from tensorflow.python.ops.linalg import linear_operator

__all__ = ['LinearOperatorBlockDiag']

class LinearOperatorBlockDiag(linear_operator.LinearOperator):
    """Combines one or more `LinearOperators` in to a Block Diagonal matrix.

  This operator combines one or more linear operators `[op1,...,opJ]`,
  building a new `LinearOperator`, whose underlying matrix representation
  has each operator `opi` on the main diagonal, and zero's elsewhere.

  #### Shape compatibility

  If `opj` acts like a [batch] matrix `Aj`, then `op_combined` acts like
  the [batch] matrix formed by having each matrix `Aj` on the main
  diagonal.

  Each `opj` is required to represent a matrix, and hence will have
  shape `batch_shape_j + [M_j, N_j]`.

  If `opj` has shape `batch_shape_j + [M_j, N_j]`, then the combined operator
  has shape `broadcast_batch_shape + [sum M_j, sum N_j]`, where
  `broadcast_batch_shape` is the mutual broadcast of `batch_shape_j`,
  `j = 1,...,J`, assuming the intermediate batch shapes broadcast.

  Arguments to `matmul`, `matvec`, `solve`, and `solvevec` may either be single
  `Tensor`s or lists of `Tensor`s that are interpreted as blocks. The `j`th
  element of a blockwise list of `Tensor`s must have dimensions that match
  `opj` for the given method. If a list of blocks is input, then a list of
  blocks is returned as well.

  When the `opj` are not guaranteed to be square, this operator's methods might
  fail due to the combined operator not being square and/or lack of efficient
  methods.

  ```python
  # Create a 4 x 4 linear operator combined of two 2 x 2 operators.
  operator_1 = LinearOperatorFullMatrix([[1., 2.], [3., 4.]])
  operator_2 = LinearOperatorFullMatrix([[1., 0.], [0., 1.]])
  operator = LinearOperatorBlockDiag([operator_1, operator_2])

  operator.to_dense()
  ==> [[1., 2., 0., 0.],
       [3., 4., 0., 0.],
       [0., 0., 1., 0.],
       [0., 0., 0., 1.]]

  operator.shape
  ==> [4, 4]

  operator.log_abs_determinant()
  ==> scalar Tensor

  x1 = ... # Shape [2, 2] Tensor
  x2 = ... # Shape [2, 2] Tensor
  x = tf.concat([x1, x2], 0)  # Shape [2, 4] Tensor
  operator.matmul(x)
  ==> tf.concat([operator_1.matmul(x1), operator_2.matmul(x2)])

  # Create a 5 x 4 linear operator combining three blocks.
  operator_1 = LinearOperatorFullMatrix([[1.], [3.]])
  operator_2 = LinearOperatorFullMatrix([[1., 6.]])
  operator_3 = LinearOperatorFullMatrix([[2.], [7.]])
  operator = LinearOperatorBlockDiag([operator_1, operator_2, operator_3])

  operator.to_dense()
  ==> [[1., 0., 0., 0.],
       [3., 0., 0., 0.],
       [0., 1., 6., 0.],
       [0., 0., 0., 2.]]
       [0., 0., 0., 7.]]

  operator.shape
  ==> [5, 4]


  # Create a [2, 3] batch of 4 x 4 linear operators.
  matrix_44 = tf.random.normal(shape=[2, 3, 4, 4])
  operator_44 = LinearOperatorFullMatrix(matrix)

  # Create a [1, 3] batch of 5 x 5 linear operators.
  matrix_55 = tf.random.normal(shape=[1, 3, 5, 5])
  operator_55 = LinearOperatorFullMatrix(matrix_55)

  # Combine to create a [2, 3] batch of 9 x 9 operators.
  operator_99 = LinearOperatorBlockDiag([operator_44, operator_55])

  # Create a shape [2, 3, 9] vector.
  x = tf.random.normal(shape=[2, 3, 9])
  operator_99.matmul(x)
  ==> Shape [2, 3, 9] Tensor

  # Create a blockwise list of vectors.
  x = [tf.random.normal(shape=[2, 3, 4]), tf.random.normal(shape=[2, 3, 5])]
  operator_99.matmul(x)
  ==> [Shape [2, 3, 4] Tensor, Shape [2, 3, 5] Tensor]
  ```

  #### Performance

  The performance of `LinearOperatorBlockDiag` on any operation is equal to
  the sum of the individual operators' operations.


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
    def __init__(self, operators, is_non_singular: Incomplete | None = None, is_self_adjoint: Incomplete | None = None, is_positive_definite: Incomplete | None = None, is_square: bool = True, name: Incomplete | None = None) -> None:
        """Initialize a `LinearOperatorBlockDiag`.

    `LinearOperatorBlockDiag` is initialized with a list of operators
    `[op_1,...,op_J]`.

    Args:
      operators:  Iterable of `LinearOperator` objects, each with
        the same `dtype` and composable shape.
      is_non_singular:  Expect that this operator is non-singular.
      is_self_adjoint:  Expect that this operator is equal to its hermitian
        transpose.
      is_positive_definite:  Expect that this operator is positive definite,
        meaning the quadratic form `x^H A x` has positive real part for all
        nonzero `x`.  Note that we do not require the operator to be
        self-adjoint to be positive-definite.  See:
        https://en.wikipedia.org/wiki/Positive-definite_matrix#Extension_for_non-symmetric_matrices
      is_square:  Expect that this operator acts like square [batch] matrices.
        This is true by default, and will raise a `ValueError` otherwise.
      name: A name for this `LinearOperator`.  Default is the individual
        operators names joined with `_o_`.

    Raises:
      TypeError:  If all operators do not have the same `dtype`.
      ValueError:  If `operators` is empty or are non-square.
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
    # Make an operator acting like batch matric A.  Assume A.shape = [..., M, N]
    operator = LinearOperator(...)

    X = ... # shape [..., N], batch vector

    Y = operator.matvec(X)
    Y.shape
    ==> [..., M]

    Y[..., :] = sum_j A[..., :, j] X[..., j]
    ```

    Args:
      x: `Tensor` with compatible shape and same `dtype` as `self`, or an
        iterable of `Tensor`s (for blockwise operators). `Tensor`s are treated
        a [batch] vectors, meaning for every set of leading dimensions, the last
        dimension defines a vector.
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
        or a list of `Tensor`s (for blockwise operators). `Tensor`s are treated
        like a [batch] matrices meaning for every set of leading dimensions, the
        last two dimensions defines a matrix.
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
