from _typeshed import Incomplete
from collections.abc import Sequence
from jax import lax as lax
from jax._src import ad_util as ad_util, core as core, dispatch as dispatch, dtypes as dtypes, source_info_util as source_info_util
from jax._src.interpreters import ad as ad, batching as batching, mlir as mlir
from jax._src.lax.control_flow import loops as loops
from jax._src.state.types import AbstractRef as AbstractRef, ReadEffect as ReadEffect, StateEffect as StateEffect
from jax._src.typing import Array as Array
from jax._src.util import merge_lists as merge_lists, partition_list as partition_list, safe_map as safe_map, safe_zip as safe_zip, split_dict as split_dict, split_list as split_list
from jax.api_util import flatten_fun_nokwargs as flatten_fun_nokwargs
from jax.tree_util import PyTreeDef as PyTreeDef, tree_flatten as tree_flatten, tree_leaves as tree_leaves, tree_map as tree_map, tree_structure as tree_structure, tree_unflatten as tree_unflatten, treedef_tuple as treedef_tuple
from typing import Callable, Generic, TypeVar

map: Incomplete
unsafe_map: Incomplete
zip: Incomplete
unsafe_zip: Incomplete
S = TypeVar('S')
T = TypeVar('T')

class Ref(Generic[T]): ...

ref_set: Incomplete
ref_get: Incomplete
ref_addupdate: Incomplete
discharge_state: Incomplete
for_p: Incomplete

def for_loop(nsteps: int | Sequence[int], body: Callable[[Array, Ref[S]], None], init_state: S, *, reverse: bool = False, unroll: int = 1) -> S:
    """A for-loop combinator that allows read/write semantics in the loop body.

  `for_loop` is a higher-order function that enables writing loops that can be
  staged out in JIT-ted JAX computations. Unlike `jax.lax.fori_loop`, it allows
  mutation in its body using `Ref`s.

  `for_loop` will initialize `Ref`s with the values in `init_state`. Each
  iteration, `body` will be called with the current `Ref`s, which can be read
  from and written to using `ref_get` and `ref_set`.

  `for_loop` is semantically equivalent to the following Python code:

  ```python
  def for_loop(nsteps, body, init_state):
    refs = tree_map(make_ref, init_state)
    for i in range(nsteps):
      body(i, refs)
    return tree_map(ref_get, refs)
  ```

  Args:
    nsteps: Number of iterations
    body: A callable that takes in the iteration number as its first argument
      and `Ref`s corresponding to `init_state` as its second argument.
      `body` is free to read from and write to its `Ref`s. `body` should
       not return anything.
    init_state: A Pytree of JAX-compatible values used to initialize the `Ref`s
      that will be passed into the for loop body.
    unroll: A positive int specifying, in the underlying operation of the
      `for` primitive, how many iterations to unroll within a single iteration
      of a loop. Higher values may speed up execution time at the cost of longer
      compilation time.
  Returns:
    A Pytree of values representing the output of the for loop.
  """
Carry = TypeVar('Carry')
X = TypeVar('X')
Y = TypeVar('Y')

def scan(f: Callable[[Carry, X], tuple[Carry, Y]], init: Carry, xs: X, length: int | None = None, reverse: bool = False, unroll: int = 1) -> tuple[Carry, Y]: ...
def transpose_jaxpr(jaxpr: core.Jaxpr, which_linear: list[bool]) -> core.Jaxpr: ...
def discharged_for_loop(nsteps, body, init_state, *, reverse: bool = False):
    """A `for_loop` implementation that discharges its body right away.

  Potentially useful for testing and benchmarking.
  """
def run_state(f, init_state): ...
