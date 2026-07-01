from _typeshed import Incomplete
from tensorflow.core.protobuf import meta_graph_pb2 as meta_graph_pb2, struct_pb2 as struct_pb2
from tensorflow.python.eager import context as context, function as function, lift_to_graph as lift_to_graph
from tensorflow.python.framework import composite_tensor as composite_tensor, func_graph as func_graph, importer as importer, ops as ops, sparse_tensor as sparse_tensor, tensor_shape as tensor_shape, tensor_spec as tensor_spec, tensor_util as tensor_util
from tensorflow.python.ops import resource_variable_ops as resource_variable_ops, variable_scope as variable_scope
from tensorflow.python.saved_model import nested_structure_coder as nested_structure_coder
from tensorflow.python.trackable import data_structures as data_structures
from tensorflow.python.util import nest as nest
from tensorflow.python.util.tf_export import tf_export as tf_export

class VariableHolder:
    """Holds variables for a python function."""
    def __init__(self, fn: Incomplete | None = None, share_variables: bool = False) -> None: ...
    @property
    def variables(self): ...
    def variable_creator_scope(self, next_creator, **kwargs):
        """Creates variables & adds them to collections to match legacy code."""
    def __call__(self, *args, **kwargs): ...
    def call_with_variable_creator_scope(self, fn): ...

class WrappedFunction(function.ConcreteFunction):
    """Wraps a tf V1 piece of code in a function."""
    def __init__(self, fn_graph, variable_holder, attrs: Incomplete | None = None, signature: Incomplete | None = None) -> None: ...
    def prune(self, feeds, fetches, name: Incomplete | None = None, input_signature: Incomplete | None = None):
        '''Extract a subgraph of this function\'s underlying graph.

    Wraps the subgraph in a new `WrappedFunction` object.

    Args:
      feeds: Input tensors to the subgraph to extract, as `Tensor` objects.
      fetches: Possibly-nested Python data structure containing information
        about outputs of the target subgraph. Each entry can either be a
        `Tensor` object (for data outputs), an `Operation` object (for control
        outputs), or a `TensorInfo` proto. Any additional shape/dtype
        information provided in a `TensorInfo` and not present in the original
        graph will be added to the returned subgraph.
      name: (optional) Name to give to the underlying `FuncGraph` of the
        returned object. If no name is provided, the graph\'s name will be
        `"pruned"`.
      input_signature: (optional) possibly-nested Python data structure
        containing `TensorSpec` objects, with which to populate the returned
        functions\'s `FuncGraph`\'s `structured_input_signature` field.

    Returns:
      A new `WrappedFunction` object containing a copy of the portion of this
        object\'s graph that goes from `feeds` to `fetches`.
    '''

class WrappedGraph:
    """Class for wrapping multiple TF 1.X functions in a single graph.

  Maintains a dictionary mapping names to wrapped functions. See
  `tf.compat.v1.wrap_function` to learn more about wrapping V1 functions.

  Functions wrapped using this class have access to variables and collections
  created in other wrapped functions, using the standard TF 1.X API (
  `tf.compat.v1.get_variable` or
  `tf.compat.v1.get_default_graph().get_collection(...)`)

  Outside a function, variables and collections may be accessed using the
  `variables` and `graph` properties.

  Example:

  ```
  def add_v1(x):
    with tf.compat.v1.variable_scope('vars', reuse=tf.compat.v1.AUTO_REUSE):
      v = tf.compat.v1.get_variable('v', shape=[], dtype=tf.int32)
    return v + x

  def increment_var_v1(x):
    with tf.compat.v1.variable_scope('vars', reuse=tf.compat.v1.AUTO_REUSE):
      v = tf.compat.v1.get_variable('v', shape=[], dtype=tf.int32)
    return v.assign_add(x)

  g = WrappedGraph()
  add = g.wrap_function(add_v1, [tf.TensorSpec([], tf.int32)])
  increment_var = g.wrap_function(increment_var_v1,
                                  [tf.TensorSpec([], tf.int32)])

  assert len(g.variables) == 1
  assert g.variables[0].numpy() == 0
  increment_var(tf.constant(5))
  assert g.variables[0].numpy() == 5

  ```
  """
    graph: Incomplete
    def __init__(self, variable_holder: Incomplete | None = None, **kwargs) -> None: ...
    @property
    def functions(self): ...
    @property
    def variables(self): ...
    def wrap_function(self, fn, signature, name: Incomplete | None = None):
        """Wraps a TF 1.X function and returns an eager-compatible function.

    All functions wrapped in the same `WrappedGraph` will have access to the
    same graph (`tf.compat.v1.get_default_graph` to get the graph object
    within a function, or `WrappedGraph.graph` to get the graph outside a
    function). Variables created within the function will be added to the
    `variables` list.

    Function inputs: All inputs to the function must be tensors (nested ok),
    with their shapes and dtypes defined in the `signature` argument.

    Function outputs:

      * The 1.X function may return tensors, variables, and ops. The wrapped
        eager-compatible function will always return tensors in the same nested
        structure.
      * Variables are replaced with a tensor containing the latest read values.
      * Returned ops are executed, and replaced with None.
      * The order of op execution and variable reads in the return is
        nondeterministic. For example:

        ```
        def update_var(x):
          v = tf.Variable(0)
          op = tf.compat.v1.assign(v, x).op
          return v, op

        g = WrappedGraph()
        fn = g.wrap_function(update_var)
        read_value, _ = fn(tf.constant(3))
        print(read_value.numpy())  # could be 0 or 3
        print(g.variables[0].numpy()) # always 3
        ```

    To ensure that ops in the function are executed (e.g. ops added to the
    `tf.GraphKeys.UPDATE_OPS` collection), include them in the function returns.

    Args:
      fn: a 1.X tensorflow function.
      signature: a possibly nested sequence of `TensorSpecs` specifying the
        shapes and dtypes of the arguments.
      name: an optional string name for the function. The function will be saved
        with key `name` in the `functions` dictionary.

    Returns:
      An eager-compatible function.
    """

def wrap_function(fn, signature, name: Incomplete | None = None):
    """Wraps the TF 1.x function fn into a graph function.

  The python function `fn` will be called once with symbolic arguments specified
  in the `signature`, traced, and turned into a graph function. Any variables
  created by `fn` will be owned by the object returned by `wrap_function`. The
  resulting graph function can be called with tensors which match the
  signature.

  ```python
  def f(x, do_add):
    v = tf.Variable(5.0)
    if do_add:
      op = v.assign_add(x)
    else:
      op = v.assign_sub(x)
    with tf.control_dependencies([op]):
      return v.read_value()

  f_add = tf.compat.v1.wrap_function(f, [tf.TensorSpec((), tf.float32), True])

  assert float(f_add(1.0)) == 6.0
  assert float(f_add(1.0)) == 7.0

  # Can call tf.compat.v1.wrap_function again to get a new trace, a new set
  # of variables, and possibly different non-template arguments.
  f_sub= tf.compat.v1.wrap_function(f, [tf.TensorSpec((), tf.float32), False])

  assert float(f_sub(1.0)) == 4.0
  assert float(f_sub(1.0)) == 3.0
  ```

  Both `tf.compat.v1.wrap_function` and `tf.function` create a callable
  TensorFlow graph. But while `tf.function` runs all stateful operations
  (e.g. `tf.print`) and sequences operations to provide the same semantics as
  eager execution, `wrap_function` is closer to the behavior of `session.run` in
  TensorFlow 1.x. It will not run any operations unless they are required to
  compute the function's outputs, either through a data dependency or a control
  dependency. Nor will it sequence operations.

  Unlike `tf.function`, `wrap_function` will only trace the Python function
  once. As with placeholders in TF 1.x, shapes and dtypes must be provided to
  `wrap_function`'s `signature` argument.

  Since it is only traced once, variables and state may be created inside the
  function and owned by the function wrapper object.

  Args:
    fn: python function to be wrapped
    signature: the placeholder and python arguments to be passed to the wrapped
      function
    name: Optional. The name of the function.

  Returns:
    the wrapped graph function.
  """
def function_from_graph_def(graph_def, inputs, outputs, captures: Incomplete | None = None):
    """Creates a ConcreteFunction from a GraphDef.

  Args:
    graph_def: A GraphDef to make a function out of.
    inputs: A Tensor name or nested structure of names in `graph_def` which
      should be inputs to the function.
    outputs: A Tensor name or nested structure of names in `graph_def` which
      should be outputs of the function.
    captures: (Optional) A dictionary mapping node names in `graph_def` that
      should be captured as inputs to tensors containing the value of the
      captured inputs.

  Returns:
    A ConcreteFunction.
  """
