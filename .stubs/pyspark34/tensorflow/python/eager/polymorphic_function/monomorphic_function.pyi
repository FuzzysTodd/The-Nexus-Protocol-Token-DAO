from _typeshed import Incomplete
from tensorflow.core.framework import attr_value_pb2 as attr_value_pb2, function_pb2 as function_pb2
from tensorflow.core.function import trace_type as trace_type
from tensorflow.python import pywrap_tfe as pywrap_tfe
from tensorflow.python.client import pywrap_tf_session as pywrap_tf_session
from tensorflow.python.eager import backprop_util as backprop_util, context as context, execute as execute, forwardprop_util as forwardprop_util, tape as tape
from tensorflow.python.eager.graph_only_ops import graph_placeholder as graph_placeholder
from tensorflow.python.eager.polymorphic_function import function_spec as function_spec, saved_model_exported_concrete as saved_model_exported_concrete
from tensorflow.python.framework import c_api_util as c_api_util, composite_tensor as composite_tensor, dtypes as dtypes, error_interpolation as error_interpolation, errors as errors, indexed_slices as indexed_slices, ops as ops, tensor_shape as tensor_shape, tensor_spec as tensor_spec, type_spec as type_spec
from tensorflow.python.ops import array_ops as array_ops, default_gradient as default_gradient, functional_ops as functional_ops, gradients_util as gradients_util, handle_data_util as handle_data_util, resource_variable_ops as resource_variable_ops
from tensorflow.python.profiler import trace as trace
from tensorflow.python.trackable import base as trackable
from tensorflow.python.types import core as core
from tensorflow.python.util import compat as compat, function_utils as function_utils, nest as nest, object_identity as object_identity, tf_inspect as tf_inspect
from typing import NamedTuple

class _InterpolateFunctionError:
    """Context Manager that interpolates the exception from 'top_level_func'."""
    def __init__(self, top_level_func) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, typ: type[BaseException] | None, exc: BaseException | None, tb: types.TracebackType | None): ...

class _EagerDefinedFunctionDeleter:
    """Unregister function from eager context."""
    name: Incomplete
    def __init__(self, name) -> None: ...
    def __del__(self) -> None: ...

class _EagerDefinedFunction:
    """Callable with the interface of `framework.function._DefinedFunction`.

  `_EagerDefinedFunction` encapsulates a function definition and its properties,
  and it provides a method for calling the encapsulated function. Some Ops
  take functions as attributes, which have type `func`; an instance of this
  class may be provided as the value of these `func` attributes.
  """
    grad_func_name: Incomplete
    python_grad_func: Incomplete
    graph: Incomplete
    def __init__(self, name, graph, inputs, outputs, attrs) -> None:
        """Initializes an eager defined function.

    Args:
      name: str, the name for the created function.
      graph: Graph, the graph containing the operations in the function
      inputs: the tensors in the graph to be used as inputs to the function
      outputs: the tensors in the graph which will be outputs from the function
      attrs: dict mapping names of attributes to their AttrValue values
    """
    @property
    def signature(self): ...
    @property
    def definition(self): ...
    def add_to_graph(self, g: Incomplete | None = None, overwrite: bool = False) -> None:
        """Add the function to the current context or a graph, if supplied.

    Args:
      g: the graph to add the function to. If not supplied, the function will
        be added to the current context.
      overwrite: A bool. If True, this function will overwrite any existing
        function of the same signature name in the graph `g` or context.
    """
    @property
    def name(self): ...
    @property
    def stateful_ops(self): ...
    def call(self, ctx, args, cancellation_manager: Incomplete | None = None):
        """Calls this function with `args` as inputs.

    `ConcreteFunction` execution respects device annotations only if the
    function won't be compiled with xla.

    Args:
      ctx: a Context object
      args: a list of arguments to supply this function with.
      cancellation_manager: a `CancellationManager` object that can be used to
        cancel function execution.

    Returns:
      The outputs of the function call.

    Raises:
      ValueError: if the number of arguments is incorrect.
      FunctionAlreadyGarbageCollectedError: if the function is no longer
        available to be called because it has been garbage collected.
    """

class _DelayedRewriteGradientFunctions:
    """Caches forward/backward functions with a delayed forward rewrite."""
    def __init__(self, func_graph, attrs, func_graph_deleter) -> None:
        """Construct an inference function and initialize caches."""
    def forward_backward(self, num_doutputs: Incomplete | None = None):
        """A possibly-cached pair of forward and backward functions."""
    def get_gradient_function(self):
        """Returns gradient function.

    The gradient rewrites an inference call op to a forward call op, but does
    not modify a pre-existing forward call op. It then computes the gradient
    from the output's gradients and the side outputs of the forward op.
    """
    def forward(self, inference_args: Incomplete | None = None, input_tangents: Incomplete | None = None):
        """A forward function with only user-specified outputs.

    The call operation for the returned inference function can be rewritten into
    a forward function. This only happens if the backward function (from the
    `backward` method) ends up being used to compute gradients.

    This approach avoids constructing unnecessary graphs, but it only works if
    we are calling this function when not executing eagerly.

    Args:
      inference_args: A flat list of Tensors, arguments to the inference
        function. Unused, but taken for compatibility with
        _TapeGradientFunctions.
      input_tangents: A flat list of Tensors, jvps associated with
        `inference_args`. Unused; if required, tape functions must be used
        instead.

    Returns:
      An _EagerDefinedFunction.
    """
    def record(self, flat_outputs, inference_args, input_tangents) -> None:
        """Record the function call operation.

    _DelayedRewriteGradientFunctions supports only first-order backprop tape
    gradients (and then only when graph building). It does not work with
    higher-order tape gradients or forward autodiff, but does work with
    higher-order symbolic gradients (tf.gradients).

    Args:
      flat_outputs: The result of running `forward`.
      inference_args: A flat list of Tensors with inference inputs to the
        operation.
      input_tangents: A flat list of Tensors with input tangents consumed by the
        operation.
    """

class _ForwardWrapper(NamedTuple):
    graph: Incomplete
    outputs: Incomplete
    output_indices: Incomplete
    output_tangents: Incomplete

class _TapeGradientFunctions:
    """Caches forward and backward functions compatible with eager gradients.

  In contrast to the delayed-rewrite approach in
  `_DelayedRewriteGradientFunctions` which only works with delayed execution,
  the forward function generated by this class has a fixed set of outputs which
  may be preserved by a tape in order to compute gradients later.

  This class is abstract; its child classes differ in how many side outputs of
  the forward function their backward function accepts gradients for, which
  determines whether higher-order tape gradients are possible.
  """
    def __init__(self, func_graph, attrs, func_graph_deleter, forwardprop_input_indices, delayed_rewrite_functions, need_gradients_for_jvps) -> None: ...
    def forward(self, inference_args, input_tangents):
        """Construct or fetch a forward function with side-outputs.

    When graph building without a tape active, symbolic gradients rely on
    regenerating the backward function for higher-order gradients (to account
    for new side outputs of the rewritten forward function call). Thus there is
    no fixed backward function for this case. However, when a tape is active
    (eager or graph building), we generate fixed backward and forward functions
    at forward function call time.

    This difference between the tape and non-tape cases is to avoid building
    unneeded backward functions while graph building (where we may or may not
    eventually need gradients).

    Args:
      inference_args: A flat list of Tensors, arguments to the inference
        function.
      input_tangents: A flat list of Tensors, jvps associated with
        `inference_args`.

    Returns:
      A forward _EagerDefinedFunction.
    """
    def record(self, flat_outputs, inference_args, input_tangents) -> None:
        """Record the function call operation.

    For backprop, indicates the backward function to use and which new Tensors
    must be watched. For forwardprop from eager, the function call itself will
    have produced tangents which need to be recorded.

    Args:
      flat_outputs: The result of running `forward`.
      inference_args: A flat list of Tensors with inference inputs to the
        operation.
      input_tangents: A flat list of Tensors with input tangents consumed by the
        operation.
    """

class _FirstOrderTapeGradientFunctions(_TapeGradientFunctions):
    """Caches tape-friendly functions for first-order gradients."""
    def __init__(self, func_graph, attrs, func_graph_deleter, forwardprop_input_indices, delayed_rewrite_functions, need_gradients_for_jvps) -> None: ...

class _HigherOrderTapeGradientFunctions(_TapeGradientFunctions):
    """Caches tape-friendly functions for higher-order gradients."""

class _ForwardBackwardCall:
    """Holds the state of a function call between execution and recording."""
    def __init__(self, functions, inference_args, input_tangents, tape_watching) -> None:
        """Collects information about the function call.

    Args:
      functions: An object which produces forward and backward functions, either
        a _DelayedRewriteGradientFunctions or a _TapeGradientFunctions object.
      inference_args: A flat list of Tensors, arguments to the inference
        function.
      input_tangents: A flat list of Tensors, jvps associated with
        `inference_args`.
      tape_watching: Boolean, with True indicating that recording is necessary.
    """
    def forward(self):
        """Builds or retrieves a forward function for this call."""
    def record(self, flat_outputs) -> None:
        """Given outputs from the execution of `forward`, records the operation."""

class ConcreteFunction(core.ConcreteFunction, trackable.Trackable):
    """A `tf.types.experimental.ConcreteFunction` created from `tf.function`."""
    def __init__(self, func_graph, attrs: Incomplete | None = None, shared_func_graph: bool = True, spec: Incomplete | None = None) -> None:
        """Initialize a `ConcreteFunction`.

    Args:
      func_graph: An instance of FuncGraph: the function body to wrap.
      attrs: (optional) dict mapping names of attributes to their AttrValue
        values. Attributes in `attrs` will be included in this function's
        definition.
     shared_func_graph: If False, the ConcreteFunction takes ownership of
       `func_graph` and will break reference cycles when it is deleted. This
       makes the FuncGraph inoperable.
     spec: FunctionSpec for the original function.  If not specified, then this
       ConcreteFunction may only be called using the flat signature.

    Raises:
      ValueError: If number of input_placeholders is not equal to the number
        of function inputs.
    """
    @property
    def variables(self):
        """Sequence of variables for this function."""
    def set_variables(self, variables) -> None: ...
    @property
    def trainable_variables(self):
        """Sequence of trainable variables for this function."""
    def __call__(self, *args, **kwargs):
        """Executes the wrapped function.

    ConcreteFunctions have two signatures:

    * The signature of the original function wrapped by this ConcreteFunction.
    * A flat signature, where each argument accepts a single Tensor.

    The original function signature is generally preferred, but the flat input
    signature is supported for backward compatibility.

    ### Original Function Signature

    When calling a ConcreteFunction with the signature of the original function,
    each argument must match the type or value that was used when the
    ConcreteFunction's graph was traced.  In particular:

    * Tensor arguments (including CompositeTensors, such as RaggedTensor) must
      have matching `TypeSpec`s.
    * Non-Tensor arguments (such as booleans or ints) must have equal values.
    * Nested arguments (such as lists, tuples, or dictionaries) must have the
      same nesting structure; and each nested value must have a matching type
      or value.

    The default value for any arguments that were traced with non-Tensor values
    is the value that was used in the trace.  Arguments that were traced with
    tensor arguments do not have a default value (even if the original function
    had a default value for that argument).

    ### Flat Signature

    When calling a ConcreteFunction with the flat signature, the arguments
    correspond to the flattened component tensors of the arguments that were
    used to construct the ConcreteFunction.  Parameter names are assigned based
    on `TensorSpec.name` (when specified) or the original argument names (with
    suffixes automatically added for nested arguments or composite tensors with
    multiple components).

    Args:
      *args: Positional arguments to the concrete function.
      **kwargs: Keyword arguments to the concrete function.

    Returns:
      The result of applying the TF function on the given Tensors.

    Raises:
      AssertionError: If this `ConcreteFunction` was not created through
        `get_concrete_function`.
      TypeError: If the arguments do not match the function's signature.
    """
    @property
    def name(self):
        """`ConcreteFunction` name."""
    @property
    def graph(self):
        """Returns the graph from which this function was constructed."""
    @property
    def inputs(self):
        """Returns tensors in `self.graph` corresponding to arguments."""
    @property
    def structured_input_signature(self):
        """Returns structured signature for this concrete function.

    Returns:
      A tuple `(args, kwargs)`, where:

        * `args` is a tuple that specifies the expected type or value each for
          positional argument.
        * `kwargs` is a dictionary that specifies the expected type or value
          for each keyword-only argument.

      The type or value for each argument is specified using one of the
      following:

        * A `tf.TypeSpec`, indicating that a Tensor or other TensorFlow-native
          value is expected.
        * A Python value, such as an integer, indicating that an equal value
          is expected.
        * A nested structure of `tf.TypeSpec`s and Python values, indicating
          that a corresponding nested structure is expected.
    """
    @property
    def outputs(self):
        """Returns tensors in `self.graph` corresponding to returned tensors."""
    @property
    def structured_outputs(self):
        """Returns outputs in `self.graph` as returned by the original function."""
    def set_external_captures(self, captures) -> None:
        """Updates the function capture values.

    The new values must have tensor types and shapes consistent with the
    original captures of the concrete function, but it is allowed to change a
    value captured with a deferred one and vice-versa.

    Args:
      captures: A list of tensors or closures. Tensors are value captures, and
        closures are call-time (deferred captures).
    """
    def replace_capture_with_deferred_capture(self, tensor, closure, spec, placeholder: Incomplete | None = None, default_value: Incomplete | None = None) -> None:
        """Replaces existing capture `tensor` with a deferred capture `closure`.

    This API replaces the capture `tensor` from the concrete function's captured
    inputs list, and places the deferred capture `closure` in
    its spot so the order of captured inputs is preserved. This is important
    because the old `tensor` and the new `closure` will have the same internal
    placeholder, which can be passed through the `placeholder` argument, or
    skipped, in which case we find the placeholder from internal inputs by
    indexing `tensor` in the external captured inputs list. Thus, it is
    important that the new deferred capture has output spec (specified by the
    `spec` argument) compatible with the internal placeholder (`placeholder`)
    and the original capture (`tensor`).

    For example,

    ```python
    bool_captured_tensor = tf.constant(True)
    float_captured_tensor = tf.constant([3.], dtype=tf.float32)
    value = tf.constant([2.], dtype=tf.float32)

    @tf.function
    def fn():
      deferred_tensor = ops.get_default_graph().capture_call_time_value(
          lambda: value,
          tf.TensorSpec(shape=(1,), dtype=tf.float32))
      if bool_captured_tensor:
        return deferred_tensor
      else:
        return deferred_tensor + float_captured_tensor

    concrete_fn = fn.get_concrete_function()
    print(concrete_fn())  # tf.Tensor([2.], shape=(1,), dtype=float32)

    new_bool_captured_tensor = constant_op.constant(False)
    def bool_closure():
      return new_bool_captured_tensor

    concrete_fn.replace_capture_with_deferred_capture(
        bool_captured_tensor,
        bool_closure,
        spec=tensor_spec.TensorSpec(shape=(), dtype=dtypes.bool))

    print(concrete_fn())  # tf.Tensor([5.], shape=(1,), dtype=float32)
    ```

    Args:
      tensor: Tensor already captured. This `tensor` should be listed in
        concrete_function.captured_inputs except when it's empty such as when
        the concrete function is restored from SavedModel.
      closure: function which takes no arguments, to be evaluated at function
        call time, returning a nest of tensors compatible with `spec`.
      spec: nest of TypeSpec for the value to capture.
      placeholder: optional. The internal placeholder corresponding to the
        captured `tensor` and the new `closure`.
      default_value: optional value to use in environments that cannot safely
        evaluate closure.
    """
    @property
    def captured_inputs(self):
        """Returns external Tensors captured by this function.

    self.__call__(*args) passes `args + self.captured_inputs` to the function.
    """
    @property
    def function_def(self):
        """Returns a `FunctionDef` object representing this function."""
    @property
    def output_shapes(self):
        """The function's output shapes."""
    @property
    def output_dtypes(self): ...
    def add_to_graph(self, g: Incomplete | None = None, overwrite: bool = False) -> None:
        """Registers the function, adds it to the graph g or default graph.

    Args:
      g: If specified, registers the function with this graph. Defaults to the
        current context (either the default graph or the eager context).
      overwrite: A bool. If True, its forward function will overwrite
        any existing function of the same signature name in the graph `g`.
    """
    def add_gradient_functions_to_graph(self, g: Incomplete | None = None) -> None:
        """Add forward/backward functions to graph `g` or the current context."""
    def pretty_printed_signature(self, verbose: bool = True):
        """Returns a string summarizing the signature of this concrete function."""

class ConcreteFunctionGarbageCollector:
    """Cleans up reference cycles when a `ConcreteFunction` goes out of scope."""
    def __init__(self, func_graph) -> None: ...
    def release(self) -> None:
        """Call off the FuncGraph deletion."""
    def __del__(self) -> None: ...

class _Marker:
    """Markers used to pretty-print nested args in function signatures."""
    def __init__(self, s) -> None: ...
