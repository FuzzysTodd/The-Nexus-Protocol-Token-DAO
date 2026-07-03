import threading
from _typeshed import Incomplete
from collections.abc import Generator, Sequence
from jax import config as config, custom_derivatives as custom_derivatives, lax as lax, random as random, sharding as sharding, tree_util as tree_util
from jax._src import ad_checkpoint as ad_checkpoint, ad_util as ad_util, api as api, api_util as api_util, core as core, dispatch as dispatch, dtypes as dtypes, linear_util as lu, op_shardings as op_shardings, pjit as pjit, prng as prng, sharding_impls as sharding_impls, source_info_util as source_info_util, util as util
from jax._src.interpreters import ad as ad, mlir as mlir
from jax._src.lib import xla_client as xla_client
from jax._src.numpy.ufuncs import logaddexp as logaddexp
from jax.experimental import maps as maps
from jax.experimental.export import export as export, shape_poly as shape_poly
from jax.experimental.jax2tf import impl_no_xla as impl_no_xla
from jax.interpreters import xla as xla
from typing import Any, Callable

NameStack: Incomplete
PolyShape = shape_poly.PolyShape
DType = Any
DisabledSafetyCheck = export.DisabledSafetyCheck
map: Incomplete
zip: Incomplete
TfVal = Any
PrecisionType = int

class _DefaultNativeSerialization: ...

DEFAULT_NATIVE_SERIALIZATION: Incomplete
tf_impl: dict[core.Primitive, Callable[..., Any]]
tf_impl_with_avals: dict[core.Primitive, Callable[..., Any]]
tf_impl_no_xla: Incomplete

class _ThreadLocalState(threading.local):
    enable_xla: bool
    inside_call_tf: bool
    shape_env: Incomplete
    include_xla_op_metadata: bool
    constant_cache: Incomplete
    tf_outer_name_scope: str
    call_tf_concrete_function_list: Incomplete
    def __init__(self) -> None: ...

def inside_call_tf() -> Generator[None, None, None]: ...
def get_thread_local_state_call_tf_concrete_function_list() -> list[Any] | None: ...
def convert(fun_jax: Callable, *, polymorphic_shapes: str | None = None, with_gradient: bool = True, enable_xla: bool = True, native_serialization: bool | _DefaultNativeSerialization = ..., native_serialization_platforms: Sequence[str] = (), native_serialization_disabled_checks: Sequence[DisabledSafetyCheck] = ()) -> Callable:
    '''Allows calling a JAX function from a TensorFlow program.

  See
  [README](https://github.com/google/jax/blob/main/jax/experimental/jax2tf/README.md)
  for more details about usage and common problems.

  Args:
    fun_jax: target JAX function to be called. Its arguments and return value
      should be JAX arrays, or nested standard Python containers
      (tuple/list/dict) thereof (pytrees).
    polymorphic_shapes: Specifies input shapes to be treated polymorphically
      during lowering.

      .. warning:: The shape-polymorphic lowering is an experimental feature.
        It is meant to be sound, but it is known to reject some JAX programs
        that are shape polymorphic. The details of this feature can change.

      It should be `None` (all arguments are monomorphic), a single PolyShape
      or string (applies to all arguments), or a tuple/list of the same length
      as the function arguments. For each argument the shape specification
      should be `None` (monomorphic argument), or a Python object with the
      same pytree structure as the argument.
      See [how optional parameters are matched to
      arguments](https://jax.readthedocs.io/en/latest/pytrees.html#applying-optional-parameters-to-pytrees).

      A shape specification for an array argument should be an object
      `PolyShape(dim0, dim1, ..., dimn)`
      where each `dim` is a dimension specification: a positive integer denoting
      a monomorphic dimension of the given size, or a string denoting a
      dimension variable assumed to range over non-zero dimension sizes, or
      the special placeholder string "_" denoting a monomorphic dimension
      whose size is given by the actual argument. As a shortcut, an Ellipsis
      suffix in the list of dimension specifications stands for a list of "_"
      placeholders.

      For convenience, a shape specification can also be given as a string
      representation, e.g.: "batch, ...", "batch, height, width, _", possibly
      with surrounding parentheses: "(batch, ...)".

      The lowering fails if it cannot ensure that the it would produce the same
      sequence of TF ops for any non-zero values of the dimension variables.

      polymorphic_shapes are only supported for positional arguments; shape
      polymorphism is not supported for keyword arguments.

      See [the README](https://github.com/google/jax/blob/main/jax/experimental/jax2tf/README.md#shape-polymorphic-conversion)
      for more details.

    with_gradient: if set (default), add a tf.custom_gradient to the lowered
      function, by converting the ``jax.vjp(fun)``. This means that reverse-mode
      TensorFlow AD is supported for the output TensorFlow function, and the
      value of the gradient will be JAX-accurate.
    enable_xla: if set (default), use the simplest conversion
      and use XLA TF ops when necessary. These ops are known to create issues
      for the TFLite and TFjs converters. For those cases, unset this parameter
      so the lowering tries harder to use non-XLA TF ops to lower the
      function and aborts if this is not possible. Cannot be set to `False`
      when using `native_serialization`.
    native_serialization: serialize the JAX function natively to
      StableHLO with compatibility guarantees. This makes it easier to have
      confidence that the code executed when calling this function from
      TensorFlow is exactly the same as JAX would run natively.
      The DEFAULT_NATIVE_SERIALIZATION value defers to `False` if `enable_xla`
      is set to `False` or to the configuration flag
      `--jax2tf_default_native_serialization` otherwise.
      Native serialization cannot be used with `enable_xla=False`.
    native_serialization_platforms: In conjunction with
      `native_serialization`, specify the platform(s)
      for which to lower the code. Must be a tuple of
      strings, including a subset of: \'cpu\', \'cuda\', \'rocm\', \'tpu\'.
      The default (empty tuple), specifies the JAX default
      backend on the machine where the lowering is done.
    native_serialization_disabled_checks: In conjunction with
      `native_serialization`, disable the specified safety checks.
      See docstring of `DisabledSafetyCheck`.

  Returns:
    A version of `fun_jax` that expects TfVals as arguments (or
    tuple/lists/dicts thereof), and returns TfVals as outputs, and uses
    only TensorFlow ops and thus can be called from a TensorFlow program.
  '''

class SerializationImpl:
    """Implementation details for jax2tf serialization.

  Abstract superclass for subclassing.
  """
    def before_conversion(self) -> None:
        """Called in the resulting TF function, before any other method.

    Useful to set any global context."""
    def after_conversion(self) -> None:
        """Called in the resulting TF function, after conversion is done.

    Useful to restore any global context set up by `before_conversion`."""
    def run_fun_tf(self, args_flat_tf: Sequence[TfVal]) -> tuple[Sequence[TfVal], Sequence[core.ShapedArray], tree_util.PyTreeDef]:
        """Runs the resulting TF function.

    Args:
      args_flat_tf: a flat tuple of tf.Tensor arguments

    Returns: a tuple with:
      outs_tfs: a flat tuple of tf.Tensor results
      outs_avals: a flat tuple of JAX abstract values for the underlying JAX
        function.
      outs_tree: the PyTreeDef for the outputs
    """
    def get_vjp_fun(self) -> tuple[Callable, Sequence[core.AbstractValue]]:
        """Returns the VJP function, and the VJP in_avals."""

class NativeSerializationImpl(SerializationImpl):
    convert_kwargs: Incomplete
    fun_jax: Incomplete
    args_specs: Incomplete
    kwargs_specs: Incomplete
    native_serialization_disabled_checks: Incomplete
    lowering_platform: Incomplete
    def __init__(self, fun_jax, *, args_specs, kwargs_specs, native_serialization_platforms: Sequence[str], native_serialization_disabled_checks: Sequence[DisabledSafetyCheck]) -> None: ...
    exported: Incomplete
    def before_conversion(self) -> None: ...
    def after_conversion(self) -> None: ...
    def run_fun_tf(self, args_flat_tf: Sequence[TfVal]) -> tuple[Sequence[TfVal], Sequence[core.ShapedArray], tree_util.PyTreeDef]: ...
    def get_vjp_fun(self) -> tuple[Callable, Sequence[core.AbstractValue]]: ...

class GraphSerializationImpl(SerializationImpl):
    convert_kwargs: Incomplete
    fun_jax: Incomplete
    args_specs: Incomplete
    kwargs_specs: Incomplete
    enable_xla: Incomplete
    name_stack: Incomplete
    args_flat_tf: Incomplete
    def __init__(self, fun_jax, *, args_specs, kwargs_specs, args_flat_tf: Sequence[TfVal], enable_xla: bool) -> None: ...
    args_avals_flat: Incomplete
    def before_conversion(self): ...
    def after_conversion(self) -> None: ...
    def run_fun_tf(self, args_flat_tf: Sequence[TfVal]) -> tuple[Sequence[TfVal], Sequence[core.ShapedArray], tree_util.PyTreeDef]: ...
    def get_vjp_fun(self) -> tuple[Callable, Sequence[core.AbstractValue]]: ...

def dtype_of_val(val: TfVal) -> DType:
    """Computes the TensorFlow dtype using JAX's typing rules.

  If the value is a tf.Tensor, it starts with its dtype. If the value is a
  constant it uses JAX to infer its dtype. The resulting dtype follows the
  JAX type inference rules, and depends on the value of the
  JAX_ENABLE_X64 flag.

  See README.md for how 64-bit values are treated.
  """
def eval_polymorphic_shape(fun_jax: Callable, *, polymorphic_shapes: Incomplete | None = None) -> Callable:
    '''Evaluates the output shape in presence of shape polymorphism.

  This is done without lowering or executing the function, same as for
  `jax.eval_shape`.

  Args:
    fun_jax: target JAX function to be called. Its arguments and return value
      should be JAX arrays, or nested standard Python containers
      (tuple/list/dict) thereof (pytrees).
    polymorphic_shapes: Specifies input shapes to be treated polymorphically
      during shape evaluation. See discussion for `jax2tf.convert`.

      .. warning:: The shape-polymorphic lowering is an experimental feature.

  Returns: a function that takes `jax.ShapeDtypeStruct`s (or any values
    with `.shape` and `.dtype` attributes) corresponding to the inputs for
    `fun_jax`, and returns a tuple with:

      * the jax.ShapeDtypeStruct corresponding to the result, as for
       `jax.eval_shape`. The shape may contain symbolic dimension expressions.
      * the value that can be passed to `polymorphic_shapes` for a subsequent
        call to `jax2tf.eval_polymorphic_shape`, or `jax2tf.convert`.

  For example:

  >>> import jax
  >>> from jax.experimental import jax2tf
  >>> from jax import numpy as jnp
  >>>
  >>> f = lambda A, x: jnp.sin(jnp.dot(A, x))
  >>> A = jax.ShapeDtypeStruct((2000, 3000), jnp.float32)
  >>> x = jax.ShapeDtypeStruct((3000, 1000), jnp.float32)
  >>> out_spec, out_poly_shape = jax2tf.eval_polymorphic_shape(f, polymorphic_shapes=["a, b", "b, c"])(A, x)
  >>> print(out_spec.shape)
  ("a", "c")
  >>> print(out_poly_shape)
  (a, c)
  >>> res_spec, res_poly_shape = jax2tf.eval_polymorphic_shape(lambda x: x.T, polymorphic_shapes=[out_poly_shape])(out_spec)
  >>> print(res_poly_shape)
  (c, a)
  '''
def flatten_fun_jax(fun_jax: Callable, in_tree) -> tuple[Callable, Callable]:
    """Wraps the function to take a (flat) list of positional args.

  jax2tf works better and is simpler when the JAX function takes and returns
  just a tuple of values (no pytrees, no kwargs). This is in part because
  jax.vjp does not support kwargs and we can only set
  tf.custom_gradient on functions with flat arguments and results

  Returns:
     * the wrapped JAX function taking and returning a flat list of arguments
     * a thunk that can be called after the wrapped function has been called
       to return the output pytree.
  """
def preprocess_arg_tf(arg_idx: int, arg_tf: TfVal) -> TfVal:
    """Pre-processes the TF args.

  Returns: a tuple with the pre-processed TF arg, the TF shape, and the
      JAX dtype.
  """

class TensorFlowTracer(core.Tracer):
    '''Tracer class that boxes a TF value and a JAX abstract value.

  In addition to the TF value we carry the JAX abstract value because
  there are some cases when it cannot be recovered from the value:
  when we are converting with polymorphic shapes or when the JAX aval
  has a custom element type. In these cases the shape of the value may
  have dimensions set to `None`, or it may only correspond to the JAX
  "physical" (TF/lowering-compatible) shape, so the JAX abstract value
  may contain more precise information.

  When the value has a partially-known shape, the dimensions marked as `None`
  must correspond to non-constant dimensions in the abstract value.

  See README.md for details.
  '''
    val: Incomplete
    def __init__(self, trace: TensorFlowTrace, val: TfVal, aval: core.AbstractValue) -> None: ...
    @property
    def aval(self): ...
    def full_lower(self): ...

class TensorFlowTrace(core.Trace):
    """Trace class that underlies the jax2tf transformation.

  We are going to ensure that jax2tf.convert is never nested inside other
  transformations. This is sufficient for intended use cases (converting
  fully-transformed JAX code). It also simplifies our job because we do not have
  to handle situations where we apply primitives on a mix of TF values and
  JAX tracers from an outer transformation. E.g., for addition both the TF
  values
  and the JAX tracers have an override and they get confused if they see values
  from the other world.

  Hence a TFT trace does not interact with non-TFT traces at lower-level. For
  higher-order control-flow primitives we invoke recursively
  _interpret_fun on the body of the conditional, which will create a nested TFT.

  We do want to allow transformations nested inside a TensorFlowTrace (TFT), but
  those will introduce their own MainTrace, and any operations involving those
  will be done on those traces, i.e., not a concern for TFT.
  """
    def pure(self, val: TfVal) -> TensorFlowTracer:
        """Lifts a non-Tracer into the TensorFlowTracer.

    This function may be called by way of trace.full_raise.
    """
    def lift(self, val: core.Tracer) -> TensorFlowTracer: ...
    def sublift(self, val: TensorFlowTracer) -> TensorFlowTracer: ...
    def process_primitive(self, primitive: core.Primitive, tracers: Sequence[TensorFlowTracer], params) -> TensorFlowTracer: ...
    def process_call(self, call_primitive: core.Primitive, fun: lu.WrappedFun, tracers: Sequence[TensorFlowTracer], params): ...
    def post_process_call(self, call_primitive: core.Primitive, out_tracers: Sequence[TensorFlowTracer], params): ...
    def process_map(self, map_primitive, f, tracers, params) -> None: ...
    def post_process_map(self, map_primitive, out_tracers, params) -> None: ...
    def process_custom_jvp_call(self, prim, fun, jvp, tracers, *, symbolic_zeros): ...
    def post_process_custom_jvp_call(self, out_tracers, _) -> None: ...
    def process_custom_vjp_call(self, prim, fun, fwd, bwd, tracers, out_trees, symbolic_zeros): ...
    def post_process_custom_vjp_call(self, out_tracers, _) -> None: ...
    def post_process_custom_vjp_call_fwd(self, *_, **__) -> None: ...
    def get_primitive_impl(self, p: core.Primitive) -> tuple[Callable, bool]: ...

tf_not_yet_impl: Incomplete

def handle_boolean_args(f, argnums: Sequence[int], boolean_f: Incomplete | None = None):
    """Computes functions with some bool args and bool results using int8.

  This is needed because some TF ops do not work for bool args, e.g.,
  inequalities, min/max.

  Args:
    f: a TF callable to wrap. It will be called with non-boolean arguments.
    argnums: the positional arguments that may be booleans.
    boolean_f: [Optional] a TF callable compatible with boolean
      arguments.

  Returns: a TF callable that can take a mix of boolean positional arguments
    (in the positions specified by `argnums`) and some non-boolean positional
    arguments. If there are no boolean arguments, just calls `f`. Otherwise,
    it calls `boolean_f` if defined. Otherwise, casts the boolean
    arguments to `int8`, calls `f`, then casts the result to `bool`.
  """

boolean_greater: Incomplete
boolean_less: Incomplete
boolean_greater_or_equal: Incomplete
boolean_less_or_equal: Incomplete
axes_to_axis: Incomplete
PartitionsOrReplicated = tuple[int, ...] | None

def split_to_logical_devices(tensor: TfVal, partition_dimensions: PartitionsOrReplicated):
    """Like TPUMPStrategy.experimental_split_to_logical_devices.

  For jax2tf purposes we want to avoid needing to thread the `strategy` object
  through the generated computation. It seems that the original function needs
  the strategy object only for error checking, which we assume is done upstream
  by JAX.

  Args:
    tensor: Input tensor to annotate.
    partition_dimensions: A list of integers, with one integer per tensor
      dimension, specifying in how many parts the dimension should be split. The
      product of integers must equal the number of devices per replica.
    use_sharding_op: whether to use a sharding op, or not.

  Returns:
    an annotated tensor.
  """
