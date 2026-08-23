from jax import lax as lax
from jax._src import dtypes as dtypes
from jax._src.tree_util import tree_flatten as tree_flatten, tree_unflatten as tree_unflatten
from jax._src.util import HashablePartial as HashablePartial, safe_zip as safe_zip, unzip2 as unzip2

zip = safe_zip

def ravel_pytree(pytree):
    """Ravel (flatten) a pytree of arrays down to a 1D array.

  Args:
    pytree: a pytree of arrays and scalars to ravel.

  Returns:
    A pair where the first element is a 1D array representing the flattened and
    concatenated leaf values, with dtype determined by promoting the dtypes of
    leaf values, and the second element is a callable for unflattening a 1D
    vector of the same length back to a pytree of of the same structure as the
    input ``pytree``. If the input pytree is empty (i.e. has no leaves) then as
    a convention a 1D empty array of dtype float32 is returned in the first
    component of the output.

  For details on dtype promotion, see
  https://jax.readthedocs.io/en/latest/type_promotion.html.

  """
def unravel_pytree(treedef, unravel_list, flat): ...
