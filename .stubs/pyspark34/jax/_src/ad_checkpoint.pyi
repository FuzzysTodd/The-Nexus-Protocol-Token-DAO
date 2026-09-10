from _typeshed import Incomplete
from collections.abc import Sequence
from jax._src import ad_util as ad_util, api as api, core as core, dispatch as dispatch, effects as effects, source_info_util as source_info_util, traceback_util as traceback_util, util as util
from jax._src.api_util import flatten_fun as flatten_fun, shaped_abstractify as shaped_abstractify
from jax._src.config import config as config
from jax._src.interpreters import ad as ad, batching as batching, mlir as mlir
from jax._src.lib.mlir.dialects import hlo as hlo
from jax._src.traceback_util import api_boundary as api_boundary
from jax._src.tree_util import keystr as keystr, tree_flatten as tree_flatten, tree_structure as tree_structure, tree_unflatten as tree_unflatten
from jax._src.util import merge_lists as merge_lists, partition_list as partition_list, safe_map as safe_map, safe_zip as safe_zip, split_list as split_list, unzip2 as unzip2, weakref_lru_cache as weakref_lru_cache, wraps as wraps
from typing import Any, Callable

map = safe_map
zip = safe_zip
logger: Incomplete

def everything_saveable(*_, **__) -> bool: ...
def nothing_saveable(*_, **__) -> bool: ...
def dots_saveable(prim, *_, **__) -> bool: ...
checkpoint_dots = dots_saveable

def dot_with_no_batch_dims_saveable(prim, *_, **params) -> bool: ...

name_p: Incomplete

def save_anything_except_these_names(*names_not_to_save):
    """Save any values (not just named ones) excluding the names given."""
def save_any_names_but_these(*names_not_to_save):
    """Save only named values, excluding the names given."""
def save_only_these_names(*names_which_can_be_saved):
    """Save only named values, and only among the names given."""
def save_from_both_policies(policy_1, policy_2): ...

checkpoint_policies: Incomplete

def checkpoint(fun: Callable, *, prevent_cse: bool = True, policy: Callable[..., bool] | None = None, static_argnums: int | tuple[int, ...] = ()) -> Callable:
    """Make ``fun`` recompute internal linearization points when differentiated.

  The :func:`jax.checkpoint` decorator, aliased to :func:`jax.remat`, provides a
  way to trade off computation time and memory cost in the context of automatic
  differentiation, especially with reverse-mode autodiff like :func:`jax.grad`
  and :func:`jax.vjp` but also with :func:`jax.linearize`.

  When differentiating a function in reverse-mode, by default all the
  linearization points (e.g. inputs to elementwise nonlinear primitive
  operations) are stored when evaluating the forward pass so that they can be
  reused on the backward pass. This evaluation strategy can lead to a high
  memory cost, or even to poor performance on hardware accelerators where memory
  access is much more expensive than FLOPs.

  An alternative evaluation strategy is for some of the linearization points to
  be recomputed (i.e. rematerialized) rather than stored. This approach can
  reduce memory usage at the cost of increased computation.

  This function decorator produces a new version of ``fun`` which follows
  the rematerialization strategy rather than the default store-everything
  strategy. That is, it returns a new version of ``fun`` which, when
  differentiated, doesn't store any of its intermediate linearization points.
  Instead, these linearization points are recomputed from the function's saved
  inputs.

  See the examples below.

  Args:
    fun: Function for which the autodiff evaluation strategy is to be changed
      from the default of storing all intermediate linearization points to
      recomputing them. Its arguments and return value should be arrays,
      scalars, or (nested) standard Python containers (tuple/list/dict) thereof.
    prevent_cse: Optional, boolean keyword-only argument indicating whether to
      prevent common subexpression elimination (CSE) optimizations in the HLO
      generated from differentiation. This CSE prevention has costs because it
      can foil other optimizations, and because it can incur high overheads on
      some backends, especially GPU. The default is True because otherwise,
      under a :func:`~jax.jit` or :func:`~jax.pmap`, CSE can defeat the purpose
      of this decorator.
      But in some settings, like when used inside a :func:`~jax.lax.scan`, this
      CSE prevention mechanism is unnecessary, in which case ``prevent_cse`` can
      be set to False.
    static_argnums: Optional, int or sequence of ints, a keyword-only argument
      indicating which argument values on which to specialize for tracing and
      caching purposes. Specifying arguments as static can avoid
      ConcretizationTypeErrors when tracing, but at the cost of more retracing
      overheads. See the example below.
    policy: Optional, callable keyword-only argument. It should be one of the
      attributes of ``jax.checkpoint_policies``. The callable takes as input a
      type-level specification of a first-order primitive application and
      returns a boolean indicating whether the corresponding output value(s) can
      be saved as residuals (or instead must be recomputed in the (co)tangent
      computation if needed).

  Returns:
    A function (callable) with the same input/output behavior as ``fun`` but
    which, when differentiated using e.g. :func:`jax.grad`, :func:`jax.vjp`, or
    :func:`jax.linearize`, recomputes rather than stores intermediate
    linearization points, thus potentially saving memory at the cost of extra
    computation.

  Here is a simple example:

  >>> import jax
  >>> import jax.numpy as jnp

  >>> @jax.checkpoint
  ... def g(x):
  ...   y = jnp.sin(x)
  ...   z = jnp.sin(y)
  ...   return z
  ...
  >>> jax.value_and_grad(g)(2.0)
  (Array(0.78907233, dtype=float32, weak_type=True), Array(-0.2556391, dtype=float32, weak_type=True))

  Here, the same value is produced whether or not the :func:`jax.checkpoint`
  decorator is present. When the decorator is not present, the values
  ``jnp.cos(2.0)`` and ``jnp.cos(jnp.sin(2.0))`` are computed on the forward
  pass and are stored for use in the backward pass, because they are needed
  on the backward pass and depend only on the primal inputs. When using
  :func:`jax.checkpoint`, the forward pass will compute only the primal outputs
  and only the primal inputs (``2.0``) will be stored for the backward pass.
  At that time, the value ``jnp.sin(2.0)`` is recomputed, along with the values
  ``jnp.cos(2.0)`` and ``jnp.cos(jnp.sin(2.0))``.

  While :func:`jax.checkpoint` controls what values are stored from the
  forward-pass to be used on the backward pass, the total amount of memory
  required to evaluate a function or its VJP depends on many additional internal
  details of that function. Those details include which numerical primitives are
  used, how they're composed, where jit and control flow primitives like scan
  are used, and other factors.

  The :func:`jax.checkpoint` decorator can be applied recursively to express
  sophisticated autodiff rematerialization strategies. For example:

  >>> def recursive_checkpoint(funs):
  ...   if len(funs) == 1:
  ...     return funs[0]
  ...   elif len(funs) == 2:
  ...     f1, f2 = funs
  ...     return lambda x: f1(f2(x))
  ...   else:
  ...     f1 = recursive_checkpoint(funs[:len(funs)//2])
  ...     f2 = recursive_checkpoint(funs[len(funs)//2:])
  ...     return lambda x: f1(jax.checkpoint(f2)(x))
  ...

  If ``fun`` involves Python control flow that depends on argument values,
  it may be necessary to use the ``static_argnums`` parameter. For example,
  consider a boolean flag argument::

    from functools import partial

    @partial(jax.checkpoint, static_argnums=(1,))
    def foo(x, is_training):
      if is_training:
        ...
      else:
        ...

  Here, the use of ``static_argnums`` allows the ``if`` statement's condition
  to depends on the value of ``is_training``. The cost to using
  ``static_argnums`` is that it introduces re-tracing overheads across calls:
  in the example, ``foo`` is re-traced every time it is called with a new value
  of ``is_training``. In some situations, ``jax.ensure_compile_time_eval``
  is needed as well::

    @partial(jax.checkpoint, static_argnums=(1,))
    def foo(x, y):
      with jax.ensure_compile_time_eval():
        y_pos = y > 0
      if y_pos:
        ...
      else:
        ...

  As an alternative to using ``static_argnums`` (and
  ``jax.ensure_compile_time_eval``), it may be easier to compute some values
  outside the :func:`jax.checkpoint`-decorated function and then close over them.
  """
remat = checkpoint

class WrapHashably:
    val: Any
    hash: int
    hashable: bool
    def __init__(self, val) -> None: ...
    def __hash__(self): ...
    def __eq__(self, other): ...

def saved_residuals(f, *args, **kwargs) -> list[tuple[core.AbstractValue, str]]: ...
def print_saved_residuals(f, *args, **kwargs) -> None: ...

remat_p: Incomplete

def remat_impl(*args, jaxpr, prevent_cse, differentiated, policy): ...
def remat_abstract_eval(*args, jaxpr, prevent_cse, differentiated, policy): ...
def remat_jvp(primals, tangents, jaxpr, prevent_cse, differentiated, policy): ...
def remat_partial_eval(trace, *tracers, jaxpr, **params): ...
def remat_partial_eval_custom_params_updater(*args): ...
def remat_transpose(reduce_axes, out_cts, *in_primals, jaxpr, **params): ...
def transpose_jaxpr(jaxpr: core.ClosedJaxpr, in_linear: bool | Sequence[bool], out_zeros: bool | Sequence[bool], reduce_axes: Sequence[core.AxisName]) -> tuple[core.ClosedJaxpr, list[bool]]: ...
def remat_vmap(spmd_axis_name, axis_size, axis_name, main_type, args, dims, *, jaxpr, **params): ...
def remat_dce(used_outputs: list[bool], eqn: core.JaxprEqn) -> tuple[list[bool], core.JaxprEqn | None]: ...
def remat_lowering(*args, jaxpr: core.Jaxpr, prevent_cse: bool, differentiated: bool, is_gpu_platform: bool = False, **_): ...

optimization_barrier_p: Incomplete

def checkpoint_name(x, name): ...
def name_jvp(primals, tangents, *, name): ...
def name_batcher(args, dims, *, name): ...
def checkpoint_wrapper(fun: Callable, *, concrete: bool = False, prevent_cse: bool = True, static_argnums: int | tuple[int, ...] = (), policy: Callable[..., bool] | None = None) -> Callable: ...
