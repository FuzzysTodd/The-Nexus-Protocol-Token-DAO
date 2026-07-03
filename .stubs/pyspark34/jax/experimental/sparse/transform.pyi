from _typeshed import Incomplete
from collections.abc import Generator, Sequence
from jax import lax as lax
from jax._src import core as core, linear_util as lu, pjit as pjit, sharding_impls as sharding_impls
from jax._src.api_util import flatten_fun_nokwargs as flatten_fun_nokwargs
from jax._src.config import config as config
from jax._src.custom_derivatives import lift_jvp as lift_jvp
from jax._src.lib import pytree as pytree
from jax._src.numpy import lax_numpy as lax_numpy
from jax.experimental import sparse as sparse
from jax.experimental.sparse import BCOO as BCOO, BCSR as BCSR
from jax.experimental.sparse.bcoo import bcoo_multiply_dense as bcoo_multiply_dense, bcoo_multiply_sparse as bcoo_multiply_sparse
from jax.tree_util import tree_flatten as tree_flatten, tree_map as tree_map, tree_unflatten as tree_unflatten
from jax.util import safe_map as safe_map, safe_zip as safe_zip, split_list as split_list
from typing import Any, Callable, NamedTuple

sparse_rules_bcoo: dict[core.Primitive, Callable]
sparse_rules_bcsr: dict[core.Primitive, Callable]
Array = Any
ArrayOrSparse = Any

class SparsifyEnv:
    """Environment for sparse jaxpr evaluation.

  The environment is essentially a collection of buffers and/or tracers
  that may be shared between one or more SparsifyValue objects, which
  represent sparse or dense arrays via indices into the list of buffers.
  """
    def __init__(self, bufs=()) -> None: ...
    def data(self, spvalue: SparsifyValue) -> Array:
        """Get the data buffer associated with a SparsifyValue."""
    def indices(self, spvalue: SparsifyValue) -> Array:
        """Get the indices buffer associated with a SparsifyValue."""
    def indptr(self, spvalue: SparsifyValue) -> Array:
        """Get the BCSR indptr buffer associated with a SparsifyValue."""
    def dense(self, data):
        """Add a new dense array to the sparsify environment."""
    def sparse(self, shape, data: Incomplete | None = None, indices: Incomplete | None = None, indptr: Incomplete | None = None, *, data_ref: Incomplete | None = None, indices_ref: Incomplete | None = None, indptr_ref: Incomplete | None = None, indices_sorted: bool = False, unique_indices: bool = False):
        """Add a new sparse array to the sparsify environment."""

class SparsifyValue(NamedTuple):
    shape: tuple[int, ...]
    data_ref: int | None
    indices_ref: int | None = ...
    indptr_ref: int | None = ...
    indices_sorted: bool | None = ...
    unique_indices: bool | None = ...
    @property
    def ndim(self): ...
    def is_sparse(self): ...
    def is_dense(self): ...
    def is_bcoo(self): ...
    def is_bcsr(self): ...

def arrays_to_spvalues(spenv: SparsifyEnv, args: Any) -> Any:
    """Convert a pytree of (sparse) arrays to an equivalent pytree of spvalues."""
def spvalues_to_arrays(spenv: SparsifyEnv, spvalues: Any) -> Any:
    """Convert a pytree of spvalues to an equivalent pytree of (sparse) arrays."""
def spvalues_to_avals(spenv: SparsifyEnv, spvalues: Any) -> Any:
    """Convert a pytree of spvalues to an equivalent pytree of abstract values."""
def popattr(obj: Any, name: str) -> Any: ...
def setnewattr(obj: Any, name: str, val: Any): ...

class SparseTracer(core.Tracer):
    def __init__(self, trace: core.Trace, *, spvalue) -> None: ...
    @property
    def spenv(self): ...
    @property
    def aval(self): ...
    def full_lower(self): ...

class SparseTrace(core.Trace):
    def pure(self, val: Any): ...
    def lift(self, val: core.Tracer): ...
    def sublift(self, val: SparseTracer): ...
    def process_primitive(self, primitive, tracers, params): ...
    def process_call(self, call_primitive, f: lu.WrappedFun, tracers, params): ...
    def process_custom_jvp_call(self, primitive, fun, jvp, tracers, *, symbolic_zeros): ...

def sparsify_subtrace(main, spvalues, *bufs) -> Generator[Incomplete, Incomplete, None]: ...
def sparsify_fun(wrapped_fun, args: list[ArrayOrSparse]): ...
def eval_sparse(jaxpr: core.Jaxpr, consts: Sequence[Array], spvalues: Sequence[SparsifyValue], spenv: SparsifyEnv) -> Sequence[SparsifyValue]: ...
def sparsify_raw(f): ...
def sparsify(f, use_tracer: bool = False):
    """Experimental sparsification transform.

  Examples:

    Decorate JAX functions to make them compatible with :class:`jax.experimental.sparse.BCOO`
    matrices:

    >>> from jax.experimental import sparse

    >>> @sparse.sparsify
    ... def f(M, v):
    ...   return 2 * M.T @ v

    >>> M = sparse.BCOO.fromdense(jnp.arange(12).reshape(3, 4))

    >>> v = jnp.array([3, 4, 2])

    >>> f(M, v)
    Array([ 64,  82, 100, 118], dtype=int32)
  """
