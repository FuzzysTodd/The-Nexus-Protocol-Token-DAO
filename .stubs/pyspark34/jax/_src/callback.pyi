from _typeshed import Incomplete
from collections.abc import Sequence
from jax._src import core as core, dispatch as dispatch, dtypes as dtypes, effects as effects, sharding_impls as sharding_impls, tree_util as tree_util, util as util
from jax._src.interpreters import ad as ad, batching as batching, mlir as mlir
from jax._src.sharding_impls import SingleDeviceSharding as SingleDeviceSharding
from typing import Any, Callable

pure_callback_p: Incomplete
map: Incomplete
unsafe_map: Incomplete

def pure_callback_impl(*args, result_avals, callback: Callable[..., Any], sharding: SingleDeviceSharding | None, vectorized: bool): ...
def pure_callback_abstract_eval(*avals, callback: Callable[..., Any], result_avals, sharding: SingleDeviceSharding | None, vectorized: bool): ...
def pure_callback_jvp_rule(*args, **kwargs) -> None: ...
def pure_callback_transpose_rule(*args, **kwargs) -> None: ...
def pure_callback_batching_rule(args, dims, *, callback, sharding: SingleDeviceSharding | None, vectorized: bool, result_avals: Sequence[core.ShapedArray]): ...
def pure_callback_lowering(ctx, *args, callback, sharding: SingleDeviceSharding | None, **params): ...
def pure_callback(callback: Callable[..., Any], result_shape_dtypes: Any, *args: Any, sharding: SingleDeviceSharding | None = None, vectorized: bool = False, **kwargs: Any):
    """Calls a pure Python callback.

  For more explanation, see `External Callbacks`_.

  Args:
    callback: function to execute on the host. The callback is assumed to be a pure
      function (i.e. one without side-effects): if an impure function is passed, it
      may behave in unexpected ways, particularly under transformation.
    result_shape_dtypes: pytree whose leaves have ``shape`` and ``dtype`` attributes,
      whose structure matches the expected output of the callback function at runtime.
    *args: arguments to be passed to the callback function
    sharding: optional sharding that specifies the device from which the callback should
      be invoked.
    vectorized: boolean specifying whether the callback function can operate in a
      vectorized manner.
    **kwargs: keyword arguments to be passed to the callback function

  Returns:
    result: a pytree of :class:`jax.Array` objects whose structure matches that of
      ``result_shape_dtypes``.

  See Also:
    - :func:`jax.experimental.io_callback`: callback designed for impure functions.
    - :func:`jax.debug.callback`: callback designed for general-purpose debugging.
    - :func:`jax.debug.print`: callback designed for printing.

  .. _External Callbacks: https://jax.readthedocs.io/en/latest/notebooks/external_callbacks.html
  """
def pure_callback_api(callback: Callable[..., Any], result_shape_dtypes: Any, *args: Any, sharding: SingleDeviceSharding | None = None, vectorized: bool = False, **kwargs: Any):
    """Applies a functionally pure Python callable. Works under :func:`jit`/:func:`~pmap`/etc.

  ``pure_callback`` enables calling a Python function in JIT-ed JAX functions.
  The input ``callback`` will be passed NumPy arrays in place of JAX arrays and
  should also return NumPy arrays. Execution takes place on CPU, like any
  Python+NumPy function.

  The callback is treated as functionally pure, meaning it has no side-effects
  and its output value depends only on its argument values. As a consequence, it
  is safe to be called multiple times (e.g. when transformed by :func:`~vmap` or
  :func:`~pmap`), or not to be called at all when e.g. the output of a
  `jit`-decorated function has no data dependence on its value. Pure callbacks
  may also be reordered if data-dependence allows.

  When :func:`~pmap`-ed, the pure callback will be called several times (one on each
  axis of the map). When `vmap`-ed the behavior will depend on the value of the
  ``vectorized`` keyword argument. When ``vectorized`` is ``True``, the callback
  is assumed to obey
  ``jax.vmap(callback)(xs) == callback(xs) == jnp.stack([callback(x) for x in xs])``.
  Therefore, the callback will be called directly on batched inputs (where the
  batch axes are the leading dimensions). Additionally, the callbacks should
  return outputs that have corresponding leading batch axes. If not vectorized
  ``callback`` will be mapped sequentially across the batched axis.
  For example, if ``callback = lambda x, y: np.matmul(x, y)``, then we are free
  to set ``vectorized=True`` because the ``np.matmul`` function handles
  arbitrary leading batch dimensions.

  Args:
    callback: A Python callable. The callable will be passed PyTrees of NumPy
      arrays as arguments, and should return a PyTree of NumPy arrays that
      matches ``result_shape_dtypes``.
    result_shape_dtypes: A PyTree with leaves that are objects with ``shape``
      and ``dtype`` attributes which represent to the shapes and dtypes of the
      value of ``callback`` applied to ``args`` and ``kwargs``.
    *args: The positional arguments to the callback. Must be PyTrees of JAX
      types.
    sharding: optional sharding that specifies the device from which the
      callback should be invoked.
    vectorized: A boolean that indicates whether or not ``callback`` is
      vectorized, meaning it can handle arrays with additional leading
      dimensions. If ``vectorized`` is `True`, when the callback is mapped
      via `jax.vmap`, it will be called directly on inputs with leading batch
      dimensions instead of executing ``callback`` on each mapped input
      individually. The callback should also return outputs batched across the
      leading axis. By default, ``vectorized`` is ``False``.
    **kwargs: The keyword arguments to the callback. Must be PyTrees of JAX
      types.

  Returns:
    The value of ``callback(*args, **kwargs)``.
  """

io_callback_p: Incomplete

class IOEffect(effects.Effect): ...
class OrderedIOEffect(effects.Effect): ...

def io_callback_impl(*args, result_avals, callback: Callable[..., Any], sharding: SingleDeviceSharding | None, ordered: bool): ...
def io_callback_abstract_eval(*avals, callback: Callable[..., Any], result_avals, sharding: SingleDeviceSharding | None, ordered: bool): ...
def io_callback_jvp_rule(*args, **kwargs) -> None: ...
def io_callback_transpose_rule(*args, **kwargs) -> None: ...
def io_callback_batching_rule(args, dims, callback, result_avals, sharding, ordered): ...
def io_callback_lowering(ctx, *args, callback, sharding, ordered, **params): ...
def io_callback(callback: Callable[..., Any], result_shape_dtypes: Any, *args: Any, sharding: SingleDeviceSharding | None = None, ordered: bool = False, **kwargs: Any):
    """Calls an impure Python callback.

  For more explanation, see `External Callbacks`_.

  Args:
    callback: function to execute on the host. It is assumet to be an impure function.
      If ``callback`` is pure, using :func:`jax.pure_callback` instead may lead to
      more efficient execution.
    result_shape_dtypes: pytree whose leaves have ``shape`` and ``dtype`` attributes,
      whose structure matches the expected output of the callback function at runtime.
    *args: arguments to be passed to the callback function
    sharding: optional sharding that specifies the device from which the callback should
      be invoked.
    ordered: boolean specifying whether sequential calls to callback must be ordered.
    **kwargs: keyword arguments to be passed to the callback function

  Returns:
    result: a pytree of :class:`jax.Array` objects whose structure matches that of
      ``result_shape_dtypes``.

  See Also:
    - :func:`jax.pure_callback`: callback designed for pure functions.
    - :func:`jax.debug.callback`: callback designed for general-purpose debugging.
    - :func:`jax.debug.print`: callback designed for printing.

  .. _External Callbacks: https://jax.readthedocs.io/en/latest/notebooks/external_callbacks.html
  """
