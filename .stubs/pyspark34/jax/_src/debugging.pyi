import string
from _typeshed import Incomplete
from collections.abc import Generator, Sequence
from jax import lax as lax
from jax._src import core as core, effects as effects, sharding_impls as sharding_impls, tree_util as tree_util, util as util
from jax._src.interpreters import ad as ad, batching as batching, mlir as mlir
from jax._src.lib.mlir import ir as ir
from jax._src.lib.mlir.dialects import hlo as hlo
from jax._src.sharding import Sharding as Sharding
from jax._src.sharding_impls import GSPMDSharding as GSPMDSharding, NamedSharding as NamedSharding, parse_flatten_op_sharding as parse_flatten_op_sharding
from typing import Any, Callable

RICH_ENABLED: bool

class DebugEffect(effects.Effect): ...

debug_effect: Incomplete

class OrderedDebugEffect(effects.Effect): ...

ordered_debug_effect: Incomplete
debug_callback_p: Incomplete
map: Incomplete
unsafe_map: Incomplete

def debug_callback_impl(*args, callback: Callable[..., Any], effect: DebugEffect): ...
def debug_callback_abstract_eval(*flat_avals, callback: Callable[..., Any], effect: DebugEffect): ...
def debug_callback_batching_rule(args, dims, **params):
    """Unrolls the debug callback across the mapped axis."""
def debug_callback_jvp_rule(primals, tangents, **params): ...
def debug_callback_transpose_rule(*flat_args, callback: Callable[..., Any], effect: DebugEffect): ...
def debug_callback_lowering(ctx, *args, effect, callback, **params): ...
def debug_callback(callback: Callable[..., Any], *args: Any, ordered: bool = False, **kwargs: Any) -> None:
    '''Calls a stageable Python callback.

  For more explanation, see `External Callbacks`_.

  ``jax.debug.callback`` enables you to pass in a Python function that can be called
  inside of a staged JAX program. A ``jax.debug.callback`` follows existing JAX
  transformation *pure* operational semantics, which are therefore unaware of
  side-effects. This means the effect could be dropped, duplicated, or
  potentially reordered in the presence of higher-order primitives and
  transformations.

  We want this behavior because we\'d like ``jax.debug.callback`` to be "innocuous",
  i.e. we want these primitives to change the JAX computation as little as
  possible while revealing as much about them as possible, such as which parts
  of the computation are duplicated or dropped.

  Args:
    callback: A Python callable. Its return value will be ignored.
    *args: The positional arguments to the callback.
    ordered: A keyword only argument used to indicate whether or not the
      staged out computation will enforce ordering of this callback w.r.t.
      other ordered callbacks.
    **kwargs: The keyword arguments to the callback.

  Returns:
    None

  See Also:
    - :func:`jax.experimental.io_callback`: callback designed for impure functions.
    - :func:`jax.pure_callback`: callback designed for pure functions.
    - :func:`jax.debug.print`: callback designed for printing.

  .. _External Callbacks: https://jax.readthedocs.io/en/latest/notebooks/external_callbacks.html
  '''

class _DebugPrintFormatChecker(string.Formatter):
    def check_unused_args(self, used_args, args, kwargs) -> None: ...

formatter: Incomplete

def debug_print(fmt: str, *args, ordered: bool = False, **kwargs) -> None:
    '''Prints values and works in staged out JAX functions.

  Note: This function does *not* work with f-strings because the formatting is
  done lazily.

  Args:
    fmt: A format string, e.g. ``"hello {x}"``, that will be used to format
      input arguments.
    *args: A list of positional arguments to be formatted.
    ordered: A keyword only argument used to indicate whether or not the
      staged out computation will enforce ordering of this ``jax.debug.print``
      w.r.t. other ordered ``jax.debug.print`` calls.
    **kwargs: Additional keyword arguments to be formatted.
  '''

inspect_sharding_p: Incomplete
sharding_callbacks: Incomplete

class ShardingCallbackInfo:
    callback: Incomplete
    module_context: Incomplete
    def __init__(self, callback, module_context) -> None: ...

def inspect_sharding_prop_user_sharding(sharding, backend_string): ...
def inspect_sharding_partition(shapes, arg_shardings, result_shape, result_sharding, backend_string): ...
def inspect_sharding_infer_sharding_from_operands(arg_shapes, arg_shardings, shape, backend_string): ...
Color = tuple[float, float, float] | str
ColorMap = Callable[[float], tuple[float, float, float, float]]

def make_color_iter(color_map, num_rows, num_cols) -> Generator[Incomplete, None, None]: ...
def visualize_sharding(shape: Sequence[int], sharding: Sharding, *, use_color: bool = True, scale: float = 1.0, min_width: int = 9, max_width: int = 80, color_map: ColorMap | None = None):
    """Visualizes a ``Sharding`` using ``rich``."""
def inspect_array_sharding(value, *, callback: Callable[[Sharding], None]):
    """Enables inspecting array sharding inside JIT-ted functions.

  This function, when provided with a Pytree of arrays, calls back with each of
  their shardings and works in ``pjit``-ted computations, enabling inspecting
  the chosen intermediate shardings.

  The policy for when ``callback`` is called is *as early as possible* when the
  sharding information is available. This means if ``inspect_array_callback`` is
  called without any transformations, the callback will happen immediately
  since we have the array and its sharding readily available. Inside of a
  ``jax.jit``, the callback will happen at lowering time, meaning you can
  trigger the callback using the AOT API (``jit(f).lower(...)``). When inside of
  a ``pjit``, the callback happens *at compile time* since the sharding is
  determined by XLA. You can trigger the callback by using JAX's AOT API
  (``pjit(f).lower(...).compile()``). In all cases, the callback will be
  triggered by running the function, since running a function entails lowering
  and compiling it first. However, once the function is compiled and cached,
  the callback will no longer occur.

  This function is experimental and its behavior may change in the future.

  Args:
    value: A Pytree of JAX arrays.
    callback: A callable that takes in a ``Sharding`` and doesn't return a value.

  In the following example, we print out the sharding of an intermediate value
  in a ``pjit``-ted computation:

  >>> import jax
  >>> import jax.numpy as jnp
  >>> from jax.experimental.pjit import pjit
  >>> from jax.sharding import Mesh, PartitionSpec
  >>>
  >>> x = jnp.arange(8, dtype=jnp.float32)
  >>> def f_(x):
  ...   x = jnp.sin(x)
  ...   jax.debug.inspect_array_sharding(x, callback=print)
  ...   return jnp.square(x)
  >>> f = pjit(f_, in_shardings=PartitionSpec('dev'),
  ...          out_shardings=PartitionSpec('dev'))
  >>> with Mesh(jax.devices(), ('dev',)):
  ...   f.lower(x).compile()  # doctest: +SKIP
  ...
  NamedSharding(mesh={'dev': 8}, partition_spec=PartitionSpec(('dev',),))
  """
def visualize_array_sharding(arr, **kwargs):
    """Visualizes an array's sharding."""
