from _typeshed import Incomplete
from jax import dtypes as dtypes, random as random, vmap as vmap
from jax.experimental import sparse as sparse
from jax.util import split_list as split_list

def random_bcoo(key, shape, *, dtype=..., indices_dtype: Incomplete | None = None, nse: float = 0.2, n_batch: int = 0, n_dense: int = 0, unique_indices: bool = True, sorted_indices: bool = False, generator=..., **kwds):
    """Generate a random BCOO matrix.

  Args:
    key : random.PRNGKey to be passed to ``generator`` function.
    shape : tuple specifying the shape of the array to be generated.
    dtype : dtype of the array to be generated.
    indices_dtype: dtype of the BCOO indices.
    nse : number of specified elements in the matrix, or if 0 < nse < 1, a
      fraction of sparse dimensions to be specified (default: 0.2).
    n_batch : number of batch dimensions. must satisfy ``n_batch >= 0`` and
      ``n_batch + n_dense <= len(shape)``.
    n_dense : number of batch dimensions. must satisfy ``n_dense >= 0`` and
      ``n_batch + n_dense <= len(shape)``.
    unique_indices : boolean specifying whether indices should be unique
      (default: True).
    sorted_indices : boolean specifying whether indices should be row-sorted in
      lexicographical order (default: False).
    generator : function for generating random values accepting a key, shape,
      and dtype. It defaults to :func:`jax.random.uniform`, and may be any
      function with a similar signature.
    **kwds : additional keyword arguments to pass to ``generator``.

  Returns:
    arr : a sparse.BCOO array with the specified properties.
  """
