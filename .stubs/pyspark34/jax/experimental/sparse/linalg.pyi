import jax
from _typeshed import Incomplete
from jax._src import core as core
from jax._src.interpreters import ad as ad
from jax._src.lib import gpu_solver as gpu_solver
from jax.experimental import sparse as sparse
from jax.interpreters import mlir as mlir, xla as xla
from typing import Callable

def lobpcg_standard(A: jax.Array | Callable[[jax.Array], jax.Array], X: jax.Array, m: int = 100, tol: jax.Array | float | None = None):
    """Compute the top-k standard eigenvalues using the LOBPCG routine.

  LOBPCG [1] stands for Locally Optimal Block Preconditioned Conjugate Gradient.
  The method enables finding top-k eigenvectors in an accelerator-friendly
  manner.

  This initial experimental version has several caveats.

    - Only the standard eigenvalue problem `A U = lambda U` is supported,
      general eigenvalues are not.
    - Gradient code is not available.
    - f64 will only work where jnp.linalg.eigh is supported for that type.
    - Finding the smallest eigenvectors is not yet supported. As a result,
      we don't yet support preconditioning, which is mostly needed for this
      case.

  The implementation is based on [2] and [3]; however, we deviate from these
  sources in several ways to improve robustness or facilitate implementation:

    - Despite increased iteration cost, we always maintain an orthonormal basis
      for the block search directions.
    - We change the convergence criterion; see the `tol` argument.
    - Soft locking [4] is intentionally not implemented; it relies on
      choosing an appropriate problem-specific tolerance to prevent
      blow-up near convergence from catastrophic cancellation of
      near-0 residuals. Instead, the approach implemented favors
      truncating the iteration basis.

  [1]: http://ccm.ucdenver.edu/reports/rep149.pdf
  [2]: https://arxiv.org/abs/1704.07458
  [3]: https://arxiv.org/abs/0705.2626
  [4]: DOI 10.13140/RG.2.2.11794.48327

  Args:
    A : An `(n, n)` array representing a square Hermitian matrix or a
        callable with its action.
    X : An `(n, k)` array representing the initial search directions for the `k`
        desired top eigenvectors. This need not be orthogonal, but must be
        numerically linearly independent (`X` will be orthonormalized).
        Note that we must have `0 < k * 5 < n`.
    m : Maximum integer iteration count; LOBPCG will only ever explore (a
        subspace of) the Krylov basis `{X, A X, A^2 X, ..., A^m X}`.
    tol : A float convergence tolerance; an eigenpair `(lambda, v)` is converged
          when its residual L2 norm `r = |A v - lambda v|` is below
          `tol * 10 * n * (lambda + |A v|)`, which
          roughly estimates the worst-case floating point error for an ideal
          eigenvector. If all `k` eigenvectors satisfy the tolerance
          comparison, then LOBPCG exits early. If left as None, then this is set
          to the float epsilon of `A.dtype`.

  Returns:
    `theta, U, i`, where `theta` is a `(k,)` array
    of eigenvalues, `U` is a `(n, k)` array of eigenvectors, `i` is the
    number of iterations performed.

  Raises:
    ValueError : if `A,X` dtypes or `n` dimensions do not match, or `k` is too
                 large (only `k * 5 < n` supported), or `k == 0`.
  """

spsolve_p: Incomplete

def spsolve(data, indices, indptr, b, tol: float = 1e-06, reorder: int = 1):
    """A sparse direct solver using QR factorization.

  Accepts a sparse matrix in CSR format `data, indices, indptr` arrays.
  Currently only the CUDA GPU backend is implemented.

  Args:
    data : An array containing the non-zero entries of the CSR matrix.
    indices : The column indices of the CSR matrix.
    indptr : The row pointer array of the CSR matrix.
    b : The right hand side of the linear system.
    tol : Tolerance to decide if singular or not. Defaults to 1e-6.
    reorder : The reordering scheme to use to reduce fill-in. No reordering if
      ``reorder=0``. Otherwise, symrcm, symamd, or csrmetisnd (``reorder=1,2,3``),
      respectively. Defaults to symrcm.

  Returns:
    An array with the same dtype and size as b representing the solution to
    the sparse linear system.
  """
