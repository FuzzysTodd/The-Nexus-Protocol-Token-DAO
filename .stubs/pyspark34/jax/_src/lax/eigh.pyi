import jax
from _typeshed import Incomplete
from jax import lax as lax
from jax._src.lax import qdwh as qdwh
from jax._src.lax.stack import Stack as Stack
from jax._src.numpy import reductions as reductions, ufuncs as ufuncs
from typing import NamedTuple

def split_spectrum(H, n, split_point, V0: Incomplete | None = None):
    """ The Hermitian matrix `H` is split into two matrices `H_minus`
  `H_plus`, respectively sharing its eigenspaces beneath and above
  its `split_point`th eigenvalue.

  Returns, in addition, `V_minus` and `V_plus`, isometries such that
  `Hi = Vi.conj().T @ H @ Vi`. If `V0` is not None, `V0 @ Vi` are
  returned instead; this allows the overall isometries mapping from
  an initial input matrix to progressively smaller blocks to be formed.

  Args:
    H: The Hermitian matrix to split.
    split_point: The eigenvalue to split along.
    V0: Matrix of isometries to be updated.
  Returns:
    H_minus: A Hermitian matrix sharing the eigenvalues of `H` beneath
      `split_point`.
    V_minus: An isometry from the input space of `V0` to `H_minus`.
    H_plus: A Hermitian matrix sharing the eigenvalues of `H` above
      `split_point`.
    V_plus: An isometry from the input space of `V0` to `H_plus`.
    rank: The dynamic size of the m subblock.
  """

class _Subproblem(NamedTuple):
    """Describes a subproblem of _eigh_work.

  Each subproblem is a `size` x `size` Hermitian matrix, starting at `offset`
  in the workspace.
  """
    offset: jax.Array
    size: jax.Array

def eigh(H, *, precision: str = 'float32', termination_size: int = 256, n: Incomplete | None = None, sort_eigenvalues: bool = True):
    """ Computes the eigendecomposition of the symmetric/Hermitian matrix H.

  Args:
    H: The `n x n` Hermitian input, padded to `N x N`.
    precision: :class:`~jax.lax.Precision` object specifying the matmul precision.
    termination_size: Recursion ends once the blocks reach this linear size.
    n: the true (dynamic) size of the matrix.
    sort_eigenvalues: If `True`, the eigenvalues will be sorted from lowest to
      highest.
  Returns:
    vals: The `n` eigenvalues of `H`.
    vecs: A unitary matrix such that `vecs[:, i]` is a normalized eigenvector
      of `H` corresponding to `vals[i]`. We have `H @ vecs = vals * vecs` up
      to numerical error.
  """
