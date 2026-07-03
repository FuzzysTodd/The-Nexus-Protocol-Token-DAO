from _typeshed import Incomplete
from collections.abc import Sequence
from jax import tree_util as tree_util
from jax._src import core as core
from jax._src.traceback_util import api_boundary as api_boundary
from jax._src.util import split_list as split_list, wraps as wraps
from jax.experimental.sparse._base import JAXSparse as JAXSparse
from jax.util import safe_zip as safe_zip
from typing import Any, Callable

is_sparse: Incomplete

def flatten_fun_for_sparse_ad(fun, argnums: int | tuple[int], args: tuple[Any]): ...
def value_and_grad(fun: Callable, argnums: int | Sequence[int] = 0, has_aux: bool = False, **kwargs) -> Callable[..., tuple[Any, Any]]:
    """Sparse-aware version of :func:`jax.value_and_grad`

  Arguments and return values are the same as :func:`jax.value_and_grad`, but when
  taking the gradient with respect to a :class:`jax.experimental.sparse` array, the
  gradient is computed in the subspace defined by the array's sparsity pattern.

  Example:

    >>> from jax.experimental import sparse
    >>> X = sparse.BCOO.fromdense(jnp.arange(6.))
    >>> y = jnp.ones(6)
    >>> sparse.value_and_grad(lambda X, y: X @ y)(X, y)
    (Array(15., dtype=float32), BCOO(float32[6], nse=5))
  """
def grad(fun: Callable, argnums: int | Sequence[int] = 0, has_aux: bool = False, **kwargs) -> Callable:
    """Sparse-aware version of :func:`jax.grad`

  Arguments and return values are the same as :func:`jax.grad`, but when taking
  the gradient with respect to a :class:`jax.experimental.sparse` array, the
  gradient is computed in the subspace defined by the array's sparsity pattern.

  Example:

    >>> from jax.experimental import sparse
    >>> X = sparse.BCOO.fromdense(jnp.arange(6.))
    >>> y = jnp.ones(6)
    >>> sparse.grad(lambda X, y: X @ y)(X, y)
    BCOO(float32[6], nse=5)
  """
def jacfwd(fun: Callable, argnums: int | Sequence[int] = 0, has_aux: bool = False, **kwargs) -> Callable:
    """Sparse-aware version of :func:`jax.jacfwd`

  Arguments and return values are the same as :func:`jax.jacfwd`, but when taking
  the gradient with respect to a :class:`jax.experimental.sparse` array, the
  gradient is computed in the subspace defined by the array's sparsity pattern.
  Currently this is only implemented for dense outputs.
  """
def jacrev(fun: Callable, argnums: int | Sequence[int] = 0, has_aux: bool = False, **kwargs) -> Callable:
    """Sparse-aware version of :func:`jax.jacrev`

  Arguments and return values are the same as :func:`jax.jacrev`, but when taking
  the gradient with respect to a :class:`jax.experimental.sparse` array, the
  gradient is computed in the subspace defined by the array's sparsity pattern.
  Currently this is only implemented for dense outputs.
  """
jacobian = jacrev
