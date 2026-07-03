from _typeshed import Incomplete
from tensorflow.python.ops.linalg import linear_operator

__all__ = ['LinearOperatorTridiag']

class LinearOperatorTridiag(linear_operator.LinearOperator):
    """`LinearOperator` acting like a [batch] square tridiagonal matrix.

  This operator acts like a [batch] square tridiagonal matrix `A` with shape
  `[B1,...,Bb, N, N]` for some `b >= 0`.  The first `b` indices index a
  batch member.  For every batch index `(i1,...,ib)`, `A[i1,...,ib, : :]` is
  an `N x M` matrix.  This matrix `A` is not materialized, but for
  purposes of broadcasting this shape will be relevant.

  Example usage:

  Create a 3 x 3 tridiagonal linear operator.

  >>> superdiag = [3., 4., 5.]
  >>> diag = [1., -1., 2.]
  >>> subdiag = [6., 7., 8]
  >>> operator = tf.linalg.LinearOperatorTridiag(
  ...    [superdiag, diag, subdiag],
  ...    diagonals_format='sequence')
  >>> operator.to_dense()
  <tf.Tensor: shape=(3, 3), dtype=float32, numpy=
  array([[ 1.,  3.,  0.],
         [ 7., -1.,  4.],
         [ 0.,  8.,  2.]], dtype=float32)>
  >>> operator.shape
  TensorShape([3, 3])

  Scalar Tensor output.

  >>> operator.log_abs_determinant()
  <tf.Tensor: shape=(), dtype=float32, numpy=4.3307333>

  Create a [2, 3] batch of 4 x 4 linear operators.

  >>> diagonals = tf.random.normal(shape=[2, 3, 3, 4])
  >>> operator = tf.linalg.LinearOperatorTridiag(
  ...   diagonals,
  ...   diagonals_format='compact')

  Create a shape [2, 1, 4, 2] vector.  Note that this shape is compatible
  since the batch dimensions, [2, 1], are broadcast to
  operator.batch_shape = [2, 3].

  >>> y = tf.random.normal(shape=[2, 1, 4, 2])
  >>> x = operator.solve(y)
  >>> x
  <tf.Tensor: shape=(2, 3, 4, 2), dtype=float32, numpy=...,
  dtype=float32)>

  #### Shape compatibility

  This operator acts on [batch] matrix with compatible shape.
  `x` is a batch matrix with compatible shape for `matmul` and `solve` if

  ```
  operator.shape = [B1,...,Bb] + [N, N],  with b >= 0
  x.shape =   [C1,...,Cc] + [N, R],
  and [C1,...,Cc] broadcasts with [B1,...,Bb].
  ```

  #### Performance

  Suppose `operator` is a `LinearOperatorTridiag` of shape `[N, N]`,
  and `x.shape = [N, R]`.  Then

  * `operator.matmul(x)` will take O(N * R) time.
  * `operator.solve(x)` will take O(N * R) time.

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
    def __init__(self, diagonals, diagonals_format=..., is_non_singular: Incomplete | None = None, is_self_adjoint: Incomplete | None = None, is_positive_definite: Incomplete | None = None, is_square: Incomplete | None = None, name: str = 'LinearOperatorTridiag') -> None:
        """Initialize a `LinearOperatorTridiag`.

    Args:
      diagonals: `Tensor` or list of `Tensor`s depending on `diagonals_format`.

        If `diagonals_format=sequence`, this is a list of three `Tensor`'s each
        with shape `[B1, ..., Bb, N]`, `b >= 0, N >= 0`, representing the
        superdiagonal, diagonal and subdiagonal in that order. Note the
        superdiagonal is padded with an element in the last position, and the
        subdiagonal is padded with an element in the front.

        If `diagonals_format=matrix` this is a `[B1, ... Bb, N, N]` shaped
        `Tensor` representing the full tridiagonal matrix.

        If `diagonals_format=compact` this is a `[B1, ... Bb, 3, N]` shaped
        `Tensor` with the second to last dimension indexing the
        superdiagonal, diagonal and subdiagonal in that order. Note the
        superdiagonal is padded with an element in the last position, and the
        subdiagonal is padded with an element in the front.

        In every case, these `Tensor`s are all floating dtype.
      diagonals_format: one of `matrix`, `sequence`, or `compact`. Default is
        `compact`.
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
    def diagonals(self): ...
    @property
    def diagonals_format(self): ...
