from _typeshed import Incomplete
from tensorflow.core.framework import attr_value_pb2 as attr_value_pb2
from tensorflow.core.function import trace_type as trace_type
from tensorflow.core.function.capture import capture_container as capture_container
from tensorflow.python.eager import context as context, execute as execute, tape as tape
from tensorflow.python.eager.graph_only_ops import graph_placeholder as graph_placeholder
from tensorflow.python.eager.polymorphic_function import composite_tensor_utils as composite_tensor_utils
from tensorflow.python.framework import auto_control_deps as auto_control_deps, composite_tensor as composite_tensor, constant_op as constant_op, dtypes as dtypes, errors as errors, indexed_slices as indexed_slices, ops as ops, tensor_spec as tensor_spec, tensor_util as tensor_util, type_spec as type_spec
from tensorflow.python.ops import array_ops as array_ops, handle_data_util as handle_data_util, resource_variable_ops as resource_variable_ops, tensor_array_ops as tensor_array_ops, variable_scope as variable_scope
from tensorflow.python.saved_model import save_context as save_context
from tensorflow.python.types import internal as internal
from tensorflow.python.util import compat as compat, nest as nest, object_identity as object_identity, tf_contextlib as tf_contextlib, tf_decorator as tf_decorator, tf_inspect as tf_inspect, variable_utils as variable_utils
from tensorflow.python.util.tf_export import tf_export as tf_export

ALLOWLIST_COLLECTIONS: Incomplete

class UnknownArgument:
    """Signifies an argument which is not currently handled."""

def convert_structure_to_signature(structure, arg_names: Incomplete | None = None, signature_context: Incomplete | None = None):
    """Convert a potentially nested structure to a signature.

  Args:
    structure: Structure to convert, where top level collection is a list or a
      tuple.
    arg_names: Optional list of arguments that has equal number of elements as
      `structure` and is used for naming corresponding TensorSpecs.
    signature_context: TraceType InternalTracingContext to generate alias_ids
      for mutable objects, like ResourceVariables.

  Returns:
    Identical structure that has TensorSpec objects instead of Tensors and
    UnknownArgument instead of any unsupported types.
  """

class FuncGraph(ops.Graph):
    '''Graph representing a function body.

  Attributes:
    name: The name of the function.
    inputs: Placeholder tensors representing the inputs to this function. The
      tensors are in this FuncGraph. This represents "regular" inputs as well as
      captured inputs (i.e. the values of self.captures), with the regular
      inputs coming first.
    outputs: Tensors that will be returned by this function. The tensors are in
      this FuncGraph.
    control_outputs: Operations that must be executed before the function
      represented by this graph can be said to have been executed.
    structured_input_signature: A tuple of (args, kwargs), which are both
      possibly-nested python objects that were received by this function. Note
      that these structures might contain Python `None`s.
    structured_outputs: A possibly-nested python object which will be returned
      by this function. The Tensors in this structure are the same as those of
      self.outputs. Note that this structure might contain Python `None`s.
    variables: Variables that should be watched during function execution.
    outer_graph: The graph this function is defined in. May be another FuncGraph
      or the global default Graph.
    captures: Maps external tensor -> internal tensor (i.e. input placeholder).
      The entries are in the order they were captured.
    control_captures: Set of external ops on which this graph has a control
      dependency.
    seed: The graph-level random seed.
    capture_by_value: If True, the func graph will capture Variables by value
      instead of reference.
  '''
    name: Incomplete
    inputs: Incomplete
    outputs: Incomplete
    control_outputs: Incomplete
    control_captures: Incomplete
    structured_input_signature: Incomplete
    structured_outputs: Incomplete
    is_control_flow_graph: bool
    capture_by_value: Incomplete
    seed: Incomplete
    def __init__(self, name, collections: Incomplete | None = None, capture_by_value: Incomplete | None = None, structured_input_signature: Incomplete | None = None, structured_outputs: Incomplete | None = None) -> None:
        """Construct a new FuncGraph.

    The graph will inherit its graph key, collections, seed, and distribution
    strategy stack from the current context or graph.

    Args:
      name: the name of the function.
      collections: a dictionary of collections this FuncGraph should start with.
        If not specified (None), the FuncGraph will read (but not write to) the
        outer graph's collections that are not allowlisted, and both read and
        write to the outer graph's collections that are allowlisted. The current
        allowlisted collections are the global variables, the local variables,
        and the trainable variables. Defaults to None.
      capture_by_value: An optional boolean. If True, the func graph will
        capture Variables by value instead of reference. By default inherit from
        outer graphs, and failing that will default to False.
      structured_input_signature: Optional. The structured input signature to
        use for initializing the FuncGraph. See the docstring for FuncGraph for
        more information.
      structured_outputs: Optional. The structured outputs to use for
        initializing the FuncGraph. See the docstring for FuncGraph for more
        information.
    """
    def watch_variable(self, v) -> None:
        """Marks the variable v as accessed while building this graph."""
    def capture_call_time_value(self, closure, spec, key: Incomplete | None = None, default_value: Incomplete | None = None, placeholder: Incomplete | None = None):
        '''Returns a placeholder which at call time has the value closure().

    The `tf.function` supports the notion of captures, that is, it allows Python
    functions to have closure variables, which bind over some value outside the
    function. However, this name binding is "early binding" performed before the
    program is run, i.e.,
    ```
    @tf.function
    def f():
      return x

    x = tf.constant(1)
    f()  # returns 1

    x = tf.constant(2)
    f()  # still returns 1!
    ```
    while in Python, name binding is performed as the program is running.
    ```
    def f():
      return x

    x = 1
    f()  # returns 1

    x = 2
    f()  # returns 2
    ```
    `capture_call_time_value` allows tf.function to mimic late binding as a
    Python function does, by passing in a `closure` callable argument to be
    executed when the tf.function is invoked eagerly.  E.g.
    ```
    @tf.function
    def f():
      return ops.get_default_graph.capture_call_time_value(lambda: x)

    x = tf.constant(1)
    f()  # returns 1

    x = tf.constant(2)
    f()  # returns 2
    ```
    Note that a `capture_call_time_value` function itself does not work well in
    the saving process (since the tf.function in which it\'s called is not
    invoked eagerly) unless passed a `default_value` argument. At saving time,
    the `default_value` argument is returned instead.

    Args:
      closure: function which takes no arguments, to be evaluated at function
        call time, returning a nest of tensors compatible with `spec`.
      spec: nest of TypeSpec for the value to capture.
      key: optional. If not None, multiple calls to lazy_capture with the same
        key in the same graph will return the same placeholder, and the first
        closure will be used at function call time.
      default_value: optional value to return in environments that cannot safely
        evaluate closure.
      placeholder: optional. If not None, the graph will take the passed-in
        `placeholder` as the internal capture instead of creating a new one.
        This is useful when loading from a SavedModel.

    Returns:
      Nest of placeholders which, at function call time, will be fed with the
      result of calling closure().

    Raises:
      ValueError: at function call time, if the return value of closure() is
       not compatible with `spec`.
    '''
    def control_dependencies(self, control_inputs):
        """Handles control dependencies.

    FuncGraph wraps Graph's control_dependencies logic by first filtering out
    any external tensors / operations and storing them in the graph's
    control_captures member. Any consumers of this function graph must then
    decide how to handle the control captures.

    Args:
      control_inputs: A list of `Operation` or `Tensor` objects which must be
        executed or computed before running the operations defined in the
        context.  Can also be `None` to clear the control dependencies.

    Returns:
     A context manager that specifies control dependencies for all
     operations constructed within the context.

    Raises:
      TypeError: If `control_inputs` is not a list of `Operation` or
        `Tensor` objects.
    """
    def as_default(self): ...
    @property
    def outer_graph(self):
        """The Graph this FuncGraph is nested in.

    Functions may capture Tensors from graphs they are nested in (transitive).

    Returns:
      A Graph object. Initially set to the current default graph when the
      FuncGraph was created. If the previous `outer_graph` was deleted because
      the function that owns it was deleted, `outer_graph` is reset to the
      outermost default graph active when the FuncGraph was created. This
      FuncGraph won't have captured anything from the new `outer_graph` (and
      likely not from the previous setting, since that would have created a
      strong reference), but it is returned so that FuncGraphs always have a
      parent.
    """
    @outer_graph.setter
    def outer_graph(self, new_outer_graph) -> None:
        """Sets `outer_graph` to `new_outer_graph`."""
    @property
    def output_types(self): ...
    @property
    def output_shapes(self): ...
    @property
    def trainable_variables(self):
        """A sequence of trainable variables accessed by this FuncGraph.

    Note that functions keep only weak references to variables. Calling the
    function after a variable it accesses has been deleted is an error.

    Returns:
      Sequence of trainable variables for this func graph.
    """
    @property
    def variables(self):
        """A sequence of variables accessed by this FuncGraph.

    Note that functions keep only weak references to variables. Calling the
    function after a variable it accesses has been deleted is an error.

    Returns:
      Sequence of variables for this func graph.
    """
    @variables.setter
    def variables(self, var_list) -> None: ...
    def capture(self, tensor, name: Incomplete | None = None, shape: Incomplete | None = None):
        """Captures `tensor` if it's external to this graph.

    If `tensor` is from a different graph, returns a placeholder for it.
    `tensor` and the placeholder will appear in self.captures, and the
    placeholder will appear in self.inputs.  Multiple calls to this method with
    the same `tensor` argument will return the same placeholder. If `tensor` is
    from this graph, returns `tensor`.

    Args:
      tensor: Tensor. May be from this FuncGraph or a different graph.
      name: Optional name if a placeholder is created.
      shape: Optional shape if a placeholder is created.

    Returns:
      Tensor from this FuncGraph.

    Raises:
      InaccessibleTensorError: if any tensors are accessed in a manner that
      bypasses the mechanisms required for the data dependencies to be correctly
      wired.
    """
    @property
    def captures(self):
        """Order list of tuples containing external and internal captures."""
    def add_capture(self, tensor, placeholder) -> None:
        """Capture a specific tensor and utilize the provided placeholder.

    Args:
      tensor: Tensor to captures.
      placeholder: Provided placeholder for the tensor.
    """
    def replace_capture(self, tensor, placeholder) -> None:
        """Replace already existing capture."""
    def replace_capture_with_deferred_capture(self, tensor, closure, spec, placeholder, default_value: Incomplete | None = None) -> None:
        """Replaces existing capture `tensor` with a deferred capture `closure`.

    Caution: It is the caller's responsibility to make sure that, after calling
    this function, the TypeSpec of the `inputs` (i.e. internal placeholders) and
    the `_captured_inputs` (i.e. external captures) of a concrete function that
    wraps this function graph are still compatible. Thus user should pairing
    usage of this function with `ConcreteFunction.set_external_captures` to make
    sure the order still matches. For example,
    ```
    # concrete_fn._captured_inputs == [tensor1, tensor2, tensor3]
    # concrete_fn.inputs == [placeholder1, placeholder2, placeholder3]
    # replace external capture `tensor2` with a deferred_capture, i.e., a
    # closure, `closure2`
    concrete_fn.graph.replace_capture_with_deferred_capture(tensor2,
                                                            closure2,
                                                            placeholder2,
                                                            some_spec,
                                                            some_default)
    concrete_fn.set_external_captures([tensor1, closure2, tensor3])
    ```

    Args:
      tensor: Tensor already captured.
      closure: function which takes no arguments, to be evaluated at function
        call time, returning a nest of tensors compatible with `spec`.
      spec: nest of TypeSpec for the value to capture.
      placeholder: the internal placeholder corresponding to the captured
        `tensor`.
      default_value: optional value to use in environments that cannot safely
        evaluate closure.
    """
    def reset_captures(self, capture_list) -> None:
        """Set the captures with the provided list of captures & placeholder."""
    def pop_capture(self, tensor):
        """Remove the capture and return the generated placeholder."""
    def clear_captures(self) -> None: ...
    def capture_eager_tensor(self, tensor, name): ...
    def captured(self, tensor):
        """Check if the specified tensor has been captured."""
    @property
    def external_captures(self):
        """External tensors captured by this function."""
    @property
    def internal_captures(self):
        """Placeholders in this function corresponding captured tensors."""
    @property
    def deferred_external_captures(self):
        """Ordered nest of tensors whose placeholders will be fed at call time."""
    @property
    def deferred_internal_captures(self):
        """List of nest of placeholders which at call time will be fed."""
    @property
    def variable_captures(self):
        """Map of python object ids of variables to variables which are captured."""
    def mark_as_unsaveable(self, error_message) -> None:
        """Marks this FuncGraph as unsaveable.

    Any attempts to export this FuncGraph will raise an error with the specified
    message.

    Args:
      error_message: List or string containing the error message to be raised
        when saving this FuncGraph to SavedModel.
    """
    @property
    def saveable(self):
        """Returns whether this FuncGraph is saveable."""
    @property
    def saving_errors(self):
        """Returns set of errors preventing this FuncGraph from being saved."""

def func_graph_from_py_func(name, python_func, args, kwargs, signature: Incomplete | None = None, func_graph: Incomplete | None = None, autograph: bool = False, autograph_options: Incomplete | None = None, add_control_dependencies: bool = True, arg_names: Incomplete | None = None, op_return_value: Incomplete | None = None, collections: Incomplete | None = None, capture_by_value: Incomplete | None = None, create_placeholders: bool = True, acd_record_initial_resource_uses: bool = False):
    '''Returns a `FuncGraph` generated from `python_func`.

  Args:
    name: an identifier for the function.
    python_func: the Python function to trace.
    args: the positional args with which the Python function should be called;
      ignored if a signature is provided.
    kwargs: the keyword args with which the Python function should be called;
      ignored if a signature is provided.
    signature: a possibly nested sequence of `TensorSpecs` specifying the shapes
      and dtypes of the arguments. When a signature is provided, `args` and
      `kwargs` are ignored, and `python_func` is traced with Tensors conforming
      to `signature`. If `None`, the shapes and dtypes are inferred from the
      inputs.
    func_graph: Optional. An instance of FuncGraph. If provided, we will use
      this graph else a new one is built and returned.
    autograph: whether to use autograph to compile `python_func`.
      See https://www.tensorflow.org/guide/autograph for more information.
    autograph_options: additional knobs to control when `autograph=True`.
      See https://www.tensorflow.org/guide/autograph for more information.
    add_control_dependencies: If True, automatically adds control dependencies
      to ensure program order matches execution order and stateful ops always
      execute.
    arg_names: Optional list of argument names, used to give input placeholders
      recognizable names.
    op_return_value: Optional. A Tensor. If set and `python_func` returns
      Operations, those return values will be replaced with this value. If not
      set, returning an Operation triggers an error.
    collections: a dictionary of collections this FuncGraph should start with.
      If not specified (None), the FuncGraph will read (but not write to) the
      outer graph\'s collections that are not allowlisted, and both read and
      write to the outer graph\'s collections that are allowlisted. The current
      allowlisted collections are the global variables, the local variables, and
      the trainable variables. Defaults to None.
    capture_by_value: An optional boolean. If True, the func graph will capture
      Variables by value instead of reference. By default inherit from outer
      graphs, and failing that will default to False.
    create_placeholders: An optional boolean. If True, then func graph will
      create placeholders for the inputs as graph ops. If False, the input args
      and kwargs will be treated as the input placeholders.
    acd_record_initial_resource_uses: If `True` and `add_control_dependencies`
      is enabled, the results (those marked with
      AutomaticControlDependencies.mark_result) will be annotated with a private
      attribute, "_res_first_used_by", which points to the first nodes which
      used the any of the resources that the result op is using.

  Returns:
    A FuncGraph.

  Raises:
    TypeError: If any of `python_func`\'s return values is neither `None`, a
      `Tensor` or a `tf.experimental.ExtensionType`.
  '''
def maybe_captured(tensor):
    """If t is a captured value placeholder, returns the original captured value.

  Args:
    tensor: Tensor.

  Returns:
    A tensor, potentially from a different Graph/FuncGraph.
  """
def device_stack_has_callable(device_stack):
    """Checks whether a device stack contains a callable."""
def has_mutation(n1, n2):
    """Returns true if n1 and n2 are different (using `is` to compare leaves)."""
def check_func_mutation(old_args, old_kwargs, new_args, new_kwargs, func) -> None:
    """Checks that the arguments to a function are not modified."""
def flatten(sequence):
    """Like nest.flatten w/ expand_composites, but returns flow for TensorArrays.

  Args:
    sequence: A nested structure of Tensors, CompositeTensors, and TensorArrays.

  Returns:
    A list of tensors.
  """
def pack_sequence_as(structure, flat_sequence):
    """Like `nest.pack_sequence_as` but also builds TensorArrays from flows.

  Args:
    structure: The structure to pack into. May contain Tensors,
      CompositeTensors, or TensorArrays.
    flat_sequence: An iterable containing tensors.

  Returns:
    A nested structure.

  Raises:
    AssertionError if `structure` and `flat_sequence` are not compatible.
  """
def dismantle_func_graph(func_graph) -> None:
    """Removes reference cycles in `func_graph` FuncGraph.

  Helpful for making sure the garbage collector doesn't need to run when
  the FuncGraph goes out of scope, e.g. in tests using defun with
  @test_util.run_in_graph_and_eager_modes(assert_no_eager_garbage=True).

  Args:
    func_graph: A `FuncGraph` object to destroy. `func_graph` is unusable after
      this function.
  """
def override_func_graph_name_scope(func_graph, name_scope) -> None: ...
