from _typeshed import Incomplete
from tensorflow.python.ops.linalg import linear_operator

__all__ = ['LinearOperatorLowRankUpdate']

class LinearOperatorLowRankUpdate(linear_operator.LinearOperator):
    '''Perturb a `LinearOperator` with a rank `K` update.

  This operator acts like a [batch] matrix `A` with shape
  `[B1,...,Bb, M, N]` for some `b >= 0`.  The first `b` indices index a
  batch member.  For every batch index `(i1,...,ib)`, `A[i1,...,ib, : :]` is
  an `M x N` matrix.

  `LinearOperatorLowRankUpdate` represents `A = L + U D V^H`, where

  ```
  L, is a LinearOperator representing [batch] M x N matrices
  U, is a [batch] M x K matrix.  Typically K << M.
  D, is a [batch] K x K matrix.
  V, is a [batch] N x K matrix.  Typically K << N.
  V^H is the Hermitian transpose (adjoint) of V.
  ```

  If `M = N`, determinants and solves are done using the matrix determinant
  lemma and Woodbury identities, and thus require L and D to be non-singular.

  Solves and determinants will be attempted unless the "is_non_singular"
  property of L and D is False.

  In the event that L and D are positive-definite, and U = V, solves and
  determinants can be done using a Cholesky factorization.

  ```python
  # Create a 3 x 3 diagonal linear operator.
  diag_operator = LinearOperatorDiag(
      diag_update=[1., 2., 3.], is_non_singular=True, is_self_adjoint=True,
      is_positive_definite=True)

  # Perturb with a rank 2 perturbation
  operator = LinearOperatorLowRankUpdate(
      operator=diag_operator,
      u=[[1., 2.], [-1., 3.], [0., 0.]],
      diag_update=[11., 12.],
      v=[[1., 2.], [-1., 3.], [10., 10.]])

  operator.shape
  ==> [3, 3]

  operator.log_abs_determinant()
  ==> scalar Tensor

  x = ... Shape [3, 4] Tensor
  operator.matmul(x)
  ==> Shape [3, 4] Tensor
  ```

  ### Shape compatibility

  This operator acts on [batch] matrix with compatible shape.
  `x` is a batch matrix with compatible shape for `matmul` and `solve` if

  ```
  operator.shape = [B1,...,Bb] + [M, N],  with b >= 0
  x.shape =        [B1,...,Bb] + [N, R],  with R >= 0.
  ```

  ### Performance

  Suppose `operator` is a `LinearOperatorLowRankUpdate` of shape `[M, N]`,
  made from a rank `K` update of `base_operator` which performs `.matmul(x)` on
  `x` having `x.shape = [N, R]` with `O(L_matmul*N*R)` complexity (and similarly
  for `solve`, `determinant`.  Then, if `x.shape = [N, R]`,

  * `operator.matmul(x)` is `O(L_matmul*N*R + K*N*R)`

  and if `M = N`,

  * `operator.solve(x)` is `O(L_matmul*N*R + N*K*R + K^2*R + K^3)`
  * `operator.determinant()` is `O(L_determinant + L_solve*N*K + K^2*N + K^3)`

  If instead `operator` and `x` have shape `[B1,...,Bb, M, N]` and
  `[B1,...,Bb, N, R]`, every operation increases in complexity by `B1*...*Bb`.

  #### Matrix property hints

  This `LinearOperator` is initialized with boolean flags of the form `is_X`,
  for `X = non_singular`, `self_adjoint`, `positive_definite`,
  `diag_update_positive` and `square`. These have the following meaning:

  * If `is_X == True`, callers should expect the operator to have the
    property `X`.  This is a promise that should be fulfilled, but is *not* a
    runtime assert.  For example, finite floating point precision may result
    in these promises being violated.
  * If `is_X == False`, callers should expect the operator to not have `X`.
  * If `is_X == None` (the default), callers should have no expectation either
    way.
  '''
    def __init__(self, base_operator, u, diag_update: Incomplete | None = None, v: Incomplete | None = None, is_diag_update_positive: Incomplete | None = None, is_non_singular: Incomplete | None = None, is_self_adjoint: Incomplete | None = None, is_positive_definite: Incomplete | None = None, is_square: Incomplete | None = None, name: str = 'LinearOperatorLowRankUpdate') -> None:
        """Initialize a `LinearOperatorLowRankUpdate`.

    This creates a `LinearOperator` of the form `A = L + U D V^H`, with
    `L` a `LinearOperator`, `U, V` both [batch] matrices, and `D` a [batch]
    diagonal matrix.

    If `L` is non-singular, solves and determinants are available.
    Solves/determinants both involve a solve/determinant of a `K x K` system.
    In the event that L and D are self-adjoint positive-definite, and U = V,
    this can be done using a Cholesky factorization.  The user should set the
    `is_X` matrix property hints, which will trigger the appropriate code path.

    Args:
      base_operator:  Shape `[B1,...,Bb, M, N]`.
      u:  Shape `[B1,...,Bb, M, K]` `Tensor` of same `dtype` as `base_operator`.
        This is `U` above.
      diag_update:  Optional shape `[B1,...,Bb, K]` `Tensor` with same `dtype`
        as `base_operator`.  This is the diagonal of `D` above.
         Defaults to `D` being the identity operator.
      v:  Optional `Tensor` of same `dtype` as `u` and shape `[B1,...,Bb, N, K]`
         Defaults to `v = u`, in which case the perturbation is symmetric.
         If `M != N`, then `v` must be set since the perturbation is not square.
      is_diag_update_positive:  Python `bool`.
        If `True`, expect `diag_update > 0`.
      is_non_singular:  Expect that this operator is non-singular.
        Default is `None`, unless `is_positive_definite` is auto-set to be
        `True` (see below).
      is_self_adjoint:  Expect that this operator is equal to its hermitian
        transpose.  Default is `None`, unless `base_operator` is self-adjoint
        and `v = None` (meaning `u=v`), in which case this defaults to `True`.
      is_positive_definite:  Expect that this operator is positive definite.
        Default is `None`, unless `base_operator` is positive-definite
        `v = None` (meaning `u=v`), and `is_diag_update_positive`, in which case
        this defaults to `True`.
        Note that we say an operator is positive definite when the quadratic
        form `x^H A x` has positive real part for all nonzero `x`.
      is_square:  Expect that this operator acts like square [batch] matrices.
      name: A name for this `LinearOperator`.

    Raises:
      ValueError:  If `is_X` flags are set in an inconsistent way.
    """
    @property
    def u(self):
        """If this operator is `A = L + U D V^H`, this is the `U`."""
    @property
    def v(self):
        """If this operator is `A = L + U D V^H`, this is the `V`."""
    @property
    def is_diag_update_positive(self):
        """If this operator is `A = L + U D V^H`, this hints `D > 0` elementwise."""
    @property
    def diag_update(self):
        """If this operator is `A = L + U D V^H`, this is the diagonal of `D`."""
    @property
    def diag_operator(self):
        """If this operator is `A = L + U D V^H`, this is `D`."""
    @property
    def base_operator(self):
        """If this operator is `A = L + U D V^H`, this is the `L`."""
