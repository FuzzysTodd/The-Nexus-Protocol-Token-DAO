from _typeshed import Incomplete
from collections.abc import Generator
from tensorflow.core.framework import attr_value_pb2 as attr_value_pb2, function_pb2 as function_pb2
from tensorflow.python.eager import context as context
from tensorflow.python.framework import c_api_util as c_api_util, dtypes as dtypes, graph_to_function_def as graph_to_function_def, ops as ops
from tensorflow.python.ops import array_ops as array_ops, resource_variable_ops as resource_variable_ops
from tensorflow.python.util import compat as compat, function_utils as function_utils, tf_contextlib as tf_contextlib, tf_inspect as tf_inspect

class Defun:
    """Obsolete. Slated for deletion. Please use tf.function instead.

  Known feature gaps while migrating to tf.function (could be outdated):
  - tf.function doesn’t support Send/Recv capability since it doesn’t share
    rendezvous with the main graph but always creates a new one.
  - tf.function doesn’t support custom gradient function directly, instead you
    need to define the function inside a tf.custom_gradient wrapper together
    with the gradient function.
  - Unlike Defun, Keras layers used inside a tf.function need to be created only
    once to avoid variable recreation.
  - Defun respects the device assignments and applies them to the function body
    but tf.function needs it to be done manually.
  - Defun might prune out unused ops automatically but tf.function doesn't.

  Limitations of Defun:
  - Original source locations are not preserved so errors do not include
    full/valid stack traces.
  - Only supports linear sequence of arguments and return values, putting the
    burden on the caller to pack/unpack everything across a Defun boundary into
    tuples (as opposed to passing list and dict-like structures directly).
  - Does not support overloading or late-bound specializations.
  - Has its own way for defining gradient overrides which does not follow
    current conventions.
  - Cannot support imperative control flow or automatic control dependencies.
  - Does not reflect statefulness in the graph and has a calling convention that
    differs from how more modern tools interact.
  - Is only compatible with graph building mode.

  Decorator used to define TensorFlow functions.

  Use this decorator to make a Python function usable directly as a TensorFlow
  function.

  The decorated function must add ops to the default graph and return zero or
  more `Tensor` objects.  Call the decorator with named arguments, one for each
  argument of the function to decorate, with the expected type of the argument
  as value.

  For example if the function to decorate accepts two `tf.float32` arguments
  named `x` and `y`, call the decorator with:

      @Defun(tf.float32, tf.float32)
      def foo(x, y):
        ...

  When you call the decorated function, it adds the `call` ops to the
  default graph. In addition, it adds the definition of the function into the
  default graph. Because the addition of the function into the graph
  is deferred, the decorator can be used anywhere in the program.

  Any variables created inside of the function are hoisted into the outer graph.
  Note that the variables are created in the variable scope that was active
  during the first call to the function. Subsequent function calls will refer to
  the same set of variables.

  Definitions of functions in a graph are frozen as soon as the graph is used to
  create a session. However, new functions and new calls to existing functions
  may be added to the graph, with the new functions themselves becoming
  immediately frozen.

  Example, but also see the [How To on functions](link_needed).

  ```python
  # Defining the function.
  @tf.Defun(tf.float32, tf.float32)
  def MyFunc(x, y):
    return x + y, x - y

  # Building the graph.
  a = tf.constant([1.0])
  b = tf.constant([2.0])
  c, d = MyFunc(a, b, name='mycall')
  ```
  """
    def __init__(self, *input_types, **kwargs) -> None:
        """Create a `Defun` decorator.

    Args:
      *input_types: A list of `tf.DType`
      **kwargs: Optional keyword arguments, including
         func_name - (optional).  A python string, the name to use to
           declare this `Function` in the graph.

         grad_func - (optional).  A function implementing the gradient
           of the function-to-register.  This is must be a
           `_DefinedFunction` object. The gradient
           function must satisfy the criterion defined in
           function.proto:GradientDef.

         python_grad_func - (optional).  A function implementing the
           gradient of the function python-side. This function must
           take the current op and the gradients w.r.t. its outputs,
           and return the gradients w.r.t. the inputs. That is it must
           implement the interface expected by `tf.RegisterGradient`).
           This will be called by tf.gradients to add the gradient ops
           to the graph. At most one of grad_func and python_grad_func
           can be specified.

         out_names = (optional). A list of strings, one per output
           tensor.

         shape_func - (optional). A function taking the op and returning a list
           of static shapes to set for the function's outputs.
    """
    def __call__(self, func): ...

class _DefinedFunctionDeleter:
    """Unregister function from eager context."""
    name: Incomplete
    def __init__(self, name) -> None: ...
    def __del__(self) -> None: ...

class _DefinedFunction:
    """_DefinedFunction encapsulates a function definition and its properties.

  Attributes:
    name: The function name.
    definition: The definition of this function. A FunctionDef proto.
    grad_func_name: If not None, the name of this function's gradient function.
    python_grad_func: A python callable implementing the gradient of
      the function python-side.
  """
    def __init__(self, func, argnames, input_types, func_name: Incomplete | None = None, grad_func: Incomplete | None = None, python_grad_func: Incomplete | None = None, out_names: Incomplete | None = None, shape_func: Incomplete | None = None, capture_by_value: bool = False, allowlisted_stateful_ops: Incomplete | None = None, capture_resource_var_by_value: bool = True, **kwargs) -> None:
        """Creates _DefinedFunction.

    Args:
      func:  A python callable which constructs a tf function body.
      argnames: A list of strings for function argument names.
      input_types: The function's argument types. Can be a tuple, list of
        tf data types.
      func_name: The function name. Defaults to None, in which derives from
        'func'.
      grad_func: This function's gradient function, if not None. Defaults
        to None.
      python_grad_func: A python callable implementing the gradient of
        the function python-side.
      out_names: An optional list of strings for the function return value
        names.
      shape_func: An optional function mapping an op to a list of static
        output shapes.
      capture_by_value: Boolean (defaults to False). If True, captured values
        will be copied into the function body.
      allowlisted_stateful_ops: A set of ops that if stateful we ignore and
        copy into the function body, when `capture_by_value` is True.
      capture_resource_var_by_value: Boolean (defaults to True). If False,
        captured resource variable returns the handle instead of value.
      **kwargs: The keyword arguments. **kwargs is passed to every call
        site of this function.

    Raises:
      ValueError: The function definition is invalid.

    """
    @property
    def name(self):
        """Function name."""
    @property
    def definition(self):
        """Function definition proto."""
    def set_grad_func(self, grad_func) -> None:
        """Specifies the gradient function of this function."""
    @property
    def grad_func_name(self):
        """Returns the name of the gradient function."""
    @property
    def python_grad_func(self):
        """Python gradient function callable."""
    @property
    def declared_input_types(self):
        """Returns the list of data types of explicit declared inputs."""
    @property
    def captured_inputs(self):
        """Returns the list of implicitly captured inputs."""
    @property
    def stateful_ops(self):
        """Returns the list of stateful ops in function definition.

    Returns:
      A list of (op.name, op.type) pairs.
    """
    def add_to_graph(self, g) -> None:
        """Adds this function into the graph g."""
    def __call__(self, *args, **kwargs): ...

class _OverloadedFunction:
    """_OverloadedFunction encapsulates an overloaded function.

  _OverloadedFunction maintains a mapping from input types to
  instantiated _DefinedFunction in self._overload.

  """
    def __init__(self, func, argnames, func_name: Incomplete | None = None, grad_func: Incomplete | None = None, python_grad_func: Incomplete | None = None, out_names: Incomplete | None = None, **kwargs) -> None:
        """Creates _DefinedFunction.

    Args:
      func:  A python callable which constructs a tf function body.
      argnames: A list of strings for function argument names.
      func_name: The function name. Defaults to None, in which derives from
        'func'.
      grad_func: This function's gradient function, if not None. Defaults
        to None.
      python_grad_func: A python callable implementing the gradient of
        the function python-side.
      out_names: A list of strings for the function return value names.
      **kwargs: The keyword arguments. **kwargs is passed to every call
        site of this function.

    Raises:
      ValueError: The function definition is invalid.

    """
    def instantiate(self, input_types):
        """Instantiate this function given input argument types.

    Args:
      input_types: A list of data types for the inputs.

    Returns:
      _DefinedFunction for the given input types.

    """
    def __call__(self, *args, **kwargs): ...

class _FuncGraph(ops.Graph):
    """A helper for constructing a function.

  _FuncGraph overrides ops.Graph's create_op() so that we can keep
  track of all inputs into every op created inside the function.  If
  any input is from other graphs, we keep track of it in self.capture
  and substitute the input with a place holder.

  Each captured input's corresponding place holder is converted into a
  function argument and the caller passes in the captured tensor.
  """
    name: Incomplete
    inputs: Incomplete
    outputs: Incomplete
    extra_inputs: Incomplete
    extra_args: Incomplete
    extra_vars: Incomplete
    def __init__(self, name, capture_by_value, allowlisted_stateful_ops, capture_resource_var_by_value, *args, **kwargs) -> None: ...
    @property
    def outer_graph(self):
        """The graph active when this _FuncGraph was created."""
    def container(self, container_name) -> Generator[Incomplete, None, None]:
        """Returns a context manager that specifies the resource container to use.

    Overridden from `tf.Graph` to update both the init_scope container
    and the present inner container. This is necessary to make sure setting
    containers applies correctly both to created variables and to stateful
    ops.

    Args:
      container_name: container name string.

    Returns:
      A context manager for defining resource containers for stateful ops,
        yields the container name.
    """
    def getvar(self, getter, name, shape: Incomplete | None = None, dtype: Incomplete | None = None, initializer: Incomplete | None = None, reuse: Incomplete | None = None, trainable: bool = True, collections: Incomplete | None = None, use_resource: Incomplete | None = None, **kwargs):
        """A custom variable getter."""
    def capture(self, tensor, name: Incomplete | None = None):
        """Adds the given tensor to this graph and returns the captured tensor."""
    @property
    def captures(self):
        """Pairs of tensors and captured tensor."""

def func_graph_from_py_func(func, arg_names, arg_types, name: Incomplete | None = None, capture_by_value: bool = False, device: Incomplete | None = None, colocation_stack: Incomplete | None = None, container: Incomplete | None = None, collections_ref: Incomplete | None = None, arg_shapes: Incomplete | None = None, allowlisted_stateful_ops: Incomplete | None = None, capture_resource_var_by_value: bool = True):
    """Returns a _FuncGraph generated from `func`.

  Args:
    func: A Python callable which constructs a TF function body. The arguments
      must correspond to `arg_types`. Returns a value or list/tuple of values.
      No returned value can be None.
    arg_names: A sequence of strings for the function argument names.
    arg_types: A sequence of the function's argument types.
    name: The function name. If None, the name is derived from `func`.
    capture_by_value: boolean. If True, captured values will be copied into the
      function body.
    device: device name or function.
    colocation_stack: A colocation stack (list) the _FuncGraph should use.
    container: A container name the _FuncGraph should start with.
    collections_ref: A reference to a collections dict the _FuncGraph should
      use internally.
    arg_shapes: A sequence of the function's argument shapes.
    allowlisted_stateful_ops: A set of ops that if stateful we ignore and
      re-create.
    capture_resource_var_by_value: Boolean (defaults to True). If False,
      captured resource variable returns the handle instead of value.

  Returns:
    A _FuncGraph.

  Raises:
    ValueError: if func returns None.
  """
def from_library(lib):
    """Creates _DefinedFunctions initialized from a FunctionDefLibrary proto.

  This method handles assigning the correct gradient functions to each
  function.

  Args:
    lib: a FunctionDefLibrary

  Returns:
    A list of _DefinedFunctions

  Raises:
    ValueError: `lib` is invalid
  """
def get_extra_vars():
    """Returns the captured variables by the function.

  Returns:
    If the default graph is being used to define a function, the
    returned list of variables are those created inside the function
    body so far. Otherwise, returns an empty list.
  """
def get_extra_inputs():
    """Returns the captured input tensors by the function.

  Returns:
    If the default graph is being used to define a function, the
    returned list of tensors are those accessed inside the function body
    but defined outside the function body so far. Otherwise, returns an
    empty list.
  """
def get_extra_args():
    """Returns the corresponding function arguments for the captured inputs.

  Returns:
    If the default graph is being used to define a function, the
    returned list of place holders are those used inside the function
    body corresponding those returned by get_extra_inputs(). Otherwise,
    returns an empty list.
  """
