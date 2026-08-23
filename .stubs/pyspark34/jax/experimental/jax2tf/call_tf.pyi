from _typeshed import Incomplete
from collections.abc import Sequence
from jax import dlpack as dlpack, dtypes as dtypes, tree_util as tree_util
from jax._src import ad_checkpoint as ad_checkpoint, ad_util as ad_util, core as core, custom_derivatives as custom_derivatives, effects as effects, util as util
from jax._src.lib import xla_client as xla_client
from jax._src.lib.mlir import ir as ir
from jax._src.lib.mlir.dialects import hlo as hlo
from jax.interpreters import mlir as mlir, xla as xla
from typing import Any, Callable

map: Incomplete
zip: Incomplete
TfConcreteFunction = Any
TfVal: Incomplete

class UnspecifiedOutputShapeDtype: ...

def call_tf(callable_tf: Callable, has_side_effects: bool = True, ordered: bool = False, output_shape_dtype=..., call_tf_graph: bool = False) -> Callable:
    """Calls a TensorFlow function from JAX, with support for reverse autodiff.

  The ``callable_tf`` will be called with TensorFlow-compatible arguments (
  numpy.ndarray, ``tf.Tensor`` or ``tf.Variable``) or pytrees thereof. The
  function must return the same type of results.

  If ``call_tf`` appears in a JAX staging context (:func:`jax.jit`,
  or :func:`jax.pmap`, or :func:`jax.xmap`, or a control-flow primitive) then
  ``callable_tf`` will be compiled with ``tf.function(callable_tf,
  jit_compile=True)``
  and the resulting XLA computation will be embedded in JAX's XLA computation.

  If ``call_tf`` appears outside a JAX staging context, it will be called inline
  using TensorFlow eager mode.

  The ``call_tf`` supports JAX's reverse-mode autodiff, in which case the
  ``callable_tf`` will be differentiated using ``tf.GradientTape``. This means
  that the gradient will be TensorFlow-accurate, e.g., will respect the
  custom gradients that may be defined for the code in ``callable_tf``.

  For an example and more details see the
  `README
  <https://github.com/google/jax/blob/main/jax/experimental/jax2tf/README.md#calling-tensorflow-functions-from-jax>`_.

  Args:
    callable_tf: a TensorFlow Callable that can take a pytree of TensorFlow
      arguments.
    has_side_effects: if True then it ensures that instances of this primitive
      are not removed or replicated by JAX optimizations such as dead-code
      elimination.
    ordered: If true, calls are modeled as having ordered effects.
    output_shape_dtype: An optional declaration of the expected shape and dtype
      of the result of the called TensorFlow function. If given it will be used
      during JAX tracing to form the abstract values of the results of the
      `call_tf`. If not given then we form a `tf.Graph` for the called
      TensorFlow function and we use the TensorFlow-inferred shapes and types.
      Must be a pytree matching the structure of the nested structure returned
      from the TensorFlow function, containing objects with `.shape` and
      `.dtype` attributes, e.g., `jax.ShapeDtypeStruct` or `jax.Array`.
    call_tf_graph: EXPERIMENTAL, DO NOT USE. We may change the name in the
      future.

  Returns: a JAX callable that can be invoked with JAX pytree arguments, in
    op-by-op mode or in a staged context. This callable can be used with JAX's
    reverse-mode autodiff (:func:`jax.grad`).
  """
def check_tf_result(idx: int, r_tf: TfVal, r_aval: core.ShapedArray | None) -> TfVal: ...

call_tf_p: Incomplete

class CallTfEffect(effects.Effect): ...

call_tf_effect: Incomplete

class CallTfOrderedEffect(effects.Effect): ...

call_tf_ordered_effect: Incomplete

def emit_tf_embedded_graph_custom_call(ctx: mlir.LoweringRuleContext, concrete_function_flat_tf, operands: Sequence[ir.Value], has_side_effects, ordered, output_avals):
    """Emits a custom call referencing a tf.Graph embedding of the TF function.

  All call_tf called function information is stored in tf.metadata.
  This includes:
  (1) The called function name: This name will be used by the runtime to execute
  the callback.
  (2) The called function index in the XLACallModule `function_list` attribute.
  """
def add_to_call_tf_concrete_function_list(concrete_tf_fn: Any, call_tf_concrete_function_list: list[Any]) -> int: ...
