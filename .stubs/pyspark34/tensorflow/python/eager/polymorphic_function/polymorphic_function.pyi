from _typeshed import Incomplete
from tensorflow.core.framework import attr_value_pb2 as attr_value_pb2
from tensorflow.core.function.trace_type import default_types as default_types
from tensorflow.python.distribute.parallel_device import parallel_device as parallel_device
from tensorflow.python.eager import context as context, lift_to_graph as lift_to_graph, monitoring as monitoring
from tensorflow.python.eager.polymorphic_function import compiler_ir as compiler_ir, tracing_compiler as tracing_compiler
from tensorflow.python.framework import composite_tensor as composite_tensor, errors as errors, ops as ops, tensor_spec as tensor_spec
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, control_flow_util as control_flow_util, math_ops as math_ops, resource_variable_ops as resource_variable_ops
from tensorflow.python.profiler import trace as trace
from tensorflow.python.trackable import base as trackable
from tensorflow.python.types import core as core
from tensorflow.python.util import deprecation as deprecation, nest as nest, object_identity as object_identity, tf_decorator as tf_decorator, traceback_utils as traceback_utils
from tensorflow.python.util.tf_export import tf_export as tf_export

FREQUENT_TRACING_WARNING_MAX_CALL_HISTORY: int
FREQUENT_TRACING_WARNING_THRESHOLD: int
FREQUENT_TRACING_WARNING_MAX_WARNING_PER_DETECTOR: int
ALLOW_DYNAMIC_VARIABLE_CREATION: bool

def set_dynamic_variable_creation(is_allowed) -> None: ...

class _FrequentTracingDetector:
    """Class keeping track of how many recent calls triggered tracing."""
    def __init__(self) -> None: ...
    def called_with_tracing(self, function_name, omit_warning) -> None:
        """Updates the list of most recent calls' tracing information.

    Warns the user when recent calls caused retracing too often.

    Args:
      function_name: the python function being traced.
      omit_warning: If 'True', this call will not warn the user even if
        retracing happens too often.
    """
    def called_without_tracing(self) -> None: ...

class _FrequentTracingDetectorManager:
    """Class for the management of all _FrequentTracingDetector objects."""
    def __init__(self) -> None: ...
    def called_without_tracing(self, key) -> None: ...
    def called_with_tracing(self, key, function_name, omit_warning) -> None: ...

class UnliftedInitializerVariable(resource_variable_ops.UninitializedVariable):
    """Variable which does not lift its initializer out of function context.

  Instances of this variable, when created, build a graph which runs their
  initializer inside a tf.cond(is_initialized) block.

  This can only be created inside a TracingCompiler called from
  (eventually) eager mode. That is, non-function-building graphs are not
  supported.
  """
    def __init__(self, initial_value: Incomplete | None = None, trainable: Incomplete | None = None, caching_device: Incomplete | None = None, name: Incomplete | None = None, dtype: Incomplete | None = None, constraint: Incomplete | None = None, add_initializers_to: Incomplete | None = None, lifted_initializer_graph: Incomplete | None = None, synchronization: Incomplete | None = None, aggregation: Incomplete | None = None, shape: Incomplete | None = None, **unused_kwargs) -> None:
        """Creates a variable.

    Args:
      initial_value: A `Tensor`, or Python object convertible to a `Tensor`,
        which is the initial value for the Variable. The initial value must have
        a shape specified unless `validate_shape` is set to False. Can also be a
        callable with no argument that returns the initial value when called.
        (Note that initializer functions from init_ops.py must first be bound
         to a shape before being used here.)
      trainable: If `True`, GradientTapes automatically watch uses of this
        Variable.
      caching_device: Optional device string or function describing where the
        Variable should be cached for reading.  Defaults to the Variable's
        device.  If not `None`, caches on another device.  Typical use is to
        cache on the device where the Ops using the Variable reside, to
        deduplicate copying through `Switch` and other conditional statements.
      name: Optional name for the variable. Defaults to `'Variable'` and gets
        uniquified automatically.
      dtype: If set, initial_value will be converted to the given type.
        If None, either the datatype will be kept (if initial_value is
       a Tensor) or float32 will be used (if it is a Python object convertible
       to a Tensor).
      constraint: An optional projection function to be applied to the variable
        after being updated by an `Optimizer` (e.g. used to implement norm
        constraints or value constraints for layer weights). The function must
        take as input the unprojected Tensor representing the value of the
        variable and return the Tensor for the projected value
        (which must have the same shape). Constraints are not safe to
        use when doing asynchronous distributed training.
      add_initializers_to: if not None and not in legacy graph mode, the
        initializer tensor will be added to this map in addition to adding the
        assignment to the function.
      lifted_initializer_graph: FuncGraph to try to lift initializers to.
      synchronization: Indicates when a distributed variable will be
        aggregated. Accepted values are constants defined in the class
        `tf.VariableSynchronization`. By default the synchronization is set to
        `AUTO` and the current `DistributionStrategy` chooses
        when to synchronize.
      aggregation: Indicates how a distributed variable will be aggregated.
        Accepted values are constants defined in the class
        `tf.VariableAggregation`.
      shape: (optional) The shape of this variable. If None, the shape of
        `initial_value` will be used. When setting this argument to
        `tf.TensorShape(None)` (representing an unspecified shape), the variable
        can be assigned with values of different shapes.

    Raises:
      ValueError: If the initial value is not specified, or does not have a
        shape and `validate_shape` is `True`.
      RuntimeError: If called outside of a function definition.
    """

JIT_COMPILE_FUNCTIONS: Incomplete
RUN_FUNCTIONS_EAGERLY: bool

def run_functions_eagerly(run_eagerly) -> None:
    '''Enables / disables eager execution of `tf.function`s.

  Calling `tf.config.run_functions_eagerly(True)` will make all
  invocations of `tf.function` run eagerly instead of running as a traced graph
  function. This can be useful for debugging. As the code now runs line-by-line,
  you can add arbitrary `print` messages or pdb breakpoints to monitor the
  inputs/outputs of each Tensorflow operation. However, you should avoid using
  this for actual production because it significantly slows down execution.

  >>> def my_func(a):
  ...  print(f\'a: {a}\')
  ...  return a + a
  >>> a_fn = tf.function(my_func)

  >>> # A side effect the first time the function is traced
  >>> # In tracing time, `a` is printed with shape and dtype only
  >>> a_fn(tf.constant(1))
  a: Tensor("a:0", shape=(), dtype=int32)
  <tf.Tensor: shape=(), dtype=int32, numpy=2>

  >>> # `print` is a python side effect, it won\'t execute as the traced function
  >>> # is called
  >>> a_fn(tf.constant(2))
  <tf.Tensor: shape=(), dtype=int32, numpy=4>

  >>> # Now, switch to eager running
  >>> tf.config.run_functions_eagerly(True)
  >>> # The code now runs eagerly and the actual value of `a` is printed
  >>> a_fn(tf.constant(2))
  a: 2
  <tf.Tensor: shape=(), dtype=int32, numpy=4>

  >>> # Turn this back off
  >>> tf.config.run_functions_eagerly(False)

  Note: This flag has no effect on functions passed into tf.data transformations
  as arguments. tf.data functions are never executed eagerly and are always
  executed as a compiled Tensorflow Graph.

  Args:
    run_eagerly: Boolean. Whether to run functions eagerly.
  '''
def functions_run_eagerly():
    """Returns the value of the `run_functions_eagerly` setting."""

class FunctionDeleter:
    """An object responsible for cleaning up the function graph."""
    func_graph: Incomplete
    def __init__(self, func_graph) -> None: ...
    def __del__(self) -> None: ...

class OptionalXlaContext:
    """Wrapper for XLA context optionally applied under a context manager."""
    xla_context: Incomplete
    def __init__(self, is_compiled) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, t: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> None: ...

class Function(core.GenericFunction, trackable.Trackable):
    """A `tf.types.experimental.GenericFunction` created by `tf.function`.

  Currently, individual methods/attributes under this class are not guaranteed
  by the TF API contract, and are subject to future changes.
  """
    def __init__(self, python_function, name, input_signature: Incomplete | None = None, autograph: bool = True, jit_compile: Incomplete | None = None, reduce_retracing: bool = False, experimental_implements: Incomplete | None = None, experimental_autograph_options: Incomplete | None = None, experimental_attributes: Incomplete | None = None) -> None:
        """Initializes a `Function`.

    Args:
      python_function: the function to be wrapped.
      name: the name given to it.
      input_signature: See the documentation for `tf.function`.
      autograph: See the documentation for `tf.function`.
      jit_compile: See the documentation for `tf.function`.
      reduce_retracing: See the documentation for `tf.function`.
      experimental_implements: See the documentation for `tf.function`.
      experimental_autograph_options: See the documentation for `tf.function`.
      experimental_attributes: See the documentation for `tf.function`.

    Raises:
      ValueError: if `input_signature` is not None and the `python_function`'s
        argspec has keyword arguments.
    """
    @property
    def name(self): ...
    def experimental_get_tracing_count(self):
        '''Returns the number of times the function has been traced.

    For more information on when a function is traced and when it is
    traced multiple times see https://www.tensorflow.org/guide/function.
    Example:

    >>> @tf.function
    ... def double(a):
    ...   return a + a
    >>> double(tf.constant(1))
    >>> double(tf.constant(2))
    >>> double.experimental_get_tracing_count()
    1
    >>> double(tf.constant("a"))
    >>> double.experimental_get_tracing_count()
    2


    The first time experimental_get_tracing_count is called
    it returns 1, as the function is traced the first
    time it is called, and the second time the same graph is used
    since we\'re calling it with a parameter of the same type.

    The second time experimental_get_tracing_count is called
    it returns 2, as we called double with a
    different argument type, and so it was traced again.

    '''
    def __call__(self, *args, **kwds): ...
    def experimental_get_compiler_ir(self, *args, **kwargs): ...
    @property
    def python_function(self):
        """The python function wrapped in this tf.function."""
    @property
    def input_signature(self): ...
    @property
    def function_spec(self): ...
    def pretty_printed_concrete_signatures(self, verbose: bool = True): ...
    def get_initialization_function(self, *args, **kwargs):
        """Returns a `ConcreteFunction` which initializes this function's variables.

    Requires that this function hasn't been accessed yet through either calling
    it or calling get_concrete_function. Fails if we cannot build an initializer
    function which does not depend on the concrete values of the inputs to this
    function.

    Note that running this function will overwrite any values currently assigned
    to variables, for example restores from a checkpoint.

    Args:
      *args: arguments to the underlying python callable.
      **kwargs: keyword arguments to the python callable.

    Returns:
      A `ConcreteFunction` object which initializes the variables of this
      function.

    Raises:
      RuntimeError: if called after the variables have been initialized.
    """
    def get_concrete_function(self, *args, **kwargs): ...
    def __tf_tracing_type__(self, signature_context): ...
    def __get__(self, instance, owner):
        """Makes it possible to decorate instance methods."""

def function(func: Incomplete | None = None, input_signature: Incomplete | None = None, autograph: bool = True, jit_compile: Incomplete | None = None, reduce_retracing: bool = False, experimental_implements: Incomplete | None = None, experimental_autograph_options: Incomplete | None = None, experimental_attributes: Incomplete | None = None, experimental_relax_shapes: Incomplete | None = None, experimental_compile: Incomplete | None = None, experimental_follow_type_hints: Incomplete | None = None) -> core.GenericFunction:
    '''Compiles a function into a callable TensorFlow graph.

  `tf.function` constructs a `tf.types.experimental.GenericFunction` that
  executes a TensorFlow graph (`tf.Graph`) created by trace-compiling the
  TensorFlow operations in `func`. More information on the topic can be found
  in [Introduction to Graphs and tf.function]
  (https://www.tensorflow.org/guide/intro_to_graphs).

  See [Better Performance with tf.function]
  (https://www.tensorflow.org/guide/function) for tips on performance and
  known limitations.

  Example usage:

  >>> @tf.function
  ... def f(x, y):
  ...   return x ** 2 + y
  >>> x = tf.constant([2, 3])
  >>> y = tf.constant([3, -2])
  >>> f(x, y)
  <tf.Tensor: ... numpy=array([7, 7], ...)>

  The trace-compilation allows non-TensorFlow operations to execute, but under
  special conditions. In general, only TensorFlow operations are guaranteed to
  run and create fresh results whenever the `GenericFunction` is called.

  ## Features

  `func` may use data-dependent Python control flow statements, including `if`,
  `for`, `while` `break`, `continue` and `return`:

  >>> @tf.function
  ... def f(x):
  ...   if tf.reduce_sum(x) > 0:
  ...     return x * x
  ...   else:
  ...     return -x // 2
  >>> f(tf.constant(-2))
  <tf.Tensor: ... numpy=1>

  `func`\'s closure may include `tf.Tensor` and `tf.Variable` objects:

  >>> @tf.function
  ... def f():
  ...   return x ** 2 + y
  >>> x = tf.constant([-2, -3])
  >>> y = tf.Variable([3, -2])
  >>> f()
  <tf.Tensor: ... numpy=array([7, 7], ...)>

  `func` may also use ops with side effects, such as `tf.print`, `tf.Variable`
  and others:

  >>> v = tf.Variable(1)
  >>> @tf.function
  ... def f(x):
  ...   for i in tf.range(x):
  ...     v.assign_add(i)
  >>> f(3)
  >>> v
  <tf.Variable ... numpy=4>

  Important: Any Python side-effects (appending to a list, printing with
  `print`, etc) will only happen once, when `func` is traced. To have
  side-effects executed into your `tf.function` they need to be written
  as TF ops:

  >>> l = []
  >>> @tf.function
  ... def f(x):
  ...   for i in x:
  ...     l.append(i + 1)    # Caution! Will only happen once when tracing
  >>> f(tf.constant([1, 2, 3]))
  >>> l
  [<tf.Tensor ...>]

  Instead, use TensorFlow collections like `tf.TensorArray`:

  >>> @tf.function
  ... def f(x):
  ...   ta = tf.TensorArray(dtype=tf.int32, size=0, dynamic_size=True)
  ...   for i in range(len(x)):
  ...     ta = ta.write(i, x[i] + 1)
  ...   return ta.stack()
  >>> f(tf.constant([1, 2, 3]))
  <tf.Tensor: ..., numpy=array([2, 3, 4], ...)>

  ## `tf.function` creates polymorphic callables

  Internally, `tf.types.experimental.GenericFunction` may contain multiple
  `tf.types.experimental.ConcreteFunction`s, each specialized to arguments with
  different data types or shapes, since TensorFlow can perform more
  optimizations on graphs of specific shapes, dtypes and values of constant
  arguments. `tf.function` treats any pure Python values as opaque objects (best
  thought of as compile-time constants), and builds a separate `tf.Graph` for
  each set of Python arguments that it encounters.
  For more information, see the
  [tf.function guide](https://www.tensorflow.org/guide/function#rules_of_tracing)

  Executing a `GenericFunction` will select and execute the appropriate
  `ConcreteFunction` based on the argument types and values.

  To obtain an individual `ConcreteFunction`, use the
  `GenericFunction.get_concrete_function` method. It can be called with the
  same arguments as `func` and returns a
  `tf.types.experimental.ConcreteFunction`. `ConcreteFunction`s are backed by a
  single `tf.Graph`:

  >>> @tf.function
  ... def f(x):
  ...   return x + 1
  >>> isinstance(f.get_concrete_function(1).graph, tf.Graph)
  True

  `ConcreteFunction`s can be executed just like `GenericFunction`s, but their
  input is resticted to the types to which they\'re specialized.

  ## Retracing

  `ConcreteFunctions` are built (traced) on the fly, as the `GenericFunction` is
  called with new TensorFlow types or shapes, or with new Python values as
  arguments. When `GenericFunction` builds a new trace, it is said that `func`
  is retraced. Retracing is a frequent performance concern for `tf.function` as
  it can be considerably slower than executing a graph that\'s already been
  traced. It is ideal to minimize the amount of retracing in your code.

  Caution: Passing python scalars or lists as arguments to `tf.function` will
  usually retrace. To avoid this, pass numeric arguments as Tensors whenever
  possible:

  >>> @tf.function
  ... def f(x):
  ...   return tf.abs(x)
  >>> f1 = f.get_concrete_function(1)
  >>> f2 = f.get_concrete_function(2)  # Slow - compiles new graph
  >>> f1 is f2
  False
  >>> f1 = f.get_concrete_function(tf.constant(1))
  >>> f2 = f.get_concrete_function(tf.constant(2))  # Fast - reuses f1
  >>> f1 is f2
  True

  Python numerical arguments should only be used when they take few distinct
  values, such as hyperparameters like the number of layers in a neural network.

  ## Input signatures

  For Tensor arguments, `GenericFunction`creates a new `ConcreteFunction` for
  every unique set of input shapes and datatypes. The example below creates two
  separate `ConcreteFunction`s, each specialized to a different shape:

  >>> @tf.function
  ... def f(x):
  ...   return x + 1
  >>> vector = tf.constant([1.0, 1.0])
  >>> matrix = tf.constant([[3.0]])
  >>> f.get_concrete_function(vector) is f.get_concrete_function(matrix)
  False

  An "input signature" can be optionally provided to `tf.function` to control
  this process. The input signature specifies the shape and type of each
  Tensor argument to the function using a `tf.TensorSpec` object. More general
  shapes can be used. This ensures only one `ConcreteFunction` is created, and
  restricts the `GenericFunction` to the specified shapes and types. It is
  an effective way to limit retracing when Tensors have dynamic shapes.

  >>> @tf.function(
  ...     input_signature=[tf.TensorSpec(shape=None, dtype=tf.float32)])
  ... def f(x):
  ...   return x + 1
  >>> vector = tf.constant([1.0, 1.0])
  >>> matrix = tf.constant([[3.0]])
  >>> f.get_concrete_function(vector) is f.get_concrete_function(matrix)
  True

  ## Variables may only be created once

  `tf.function` only allows creating new `tf.Variable` objects when it is called
  for the first time:

  >>> class MyModule(tf.Module):
  ...   def __init__(self):
  ...     self.v = None
  ...
  ...   @tf.function
  ...   def __call__(self, x):
  ...     if self.v is None:
  ...       self.v = tf.Variable(tf.ones_like(x))
  ...     return self.v * x

  In general, it is recommended to create `tf.Variable`s outside of
  `tf.function`.
  In simple cases, persisting state across `tf.function` boundaries may be
  implemented using a pure functional style in which state is represented by
  `tf.Tensor`s passed as arguments and returned as return values.

  Contrast the two styles below:

  >>> state = tf.Variable(1)
  >>> @tf.function
  ... def f(x):
  ...   state.assign_add(x)
  >>> f(tf.constant(2))  # Non-pure functional style
  >>> state
  <tf.Variable ... numpy=3>

  >>> state = tf.constant(1)
  >>> @tf.function
  ... def f(state, x):
  ...   state += x
  ...   return state
  >>> state = f(state, tf.constant(2))  # Pure functional style
  >>> state
  <tf.Tensor: ... numpy=3>

  ## Python operations execute only once per trace

  `func` may contain TensorFlow operations mixed with pure Python operations.
  However, when the function is executed, only the TensorFlow operations will
  run. The Python operations run only once, at trace time. If TensorFlow
  operations depend on results from Python operations, those results will be
  frozen into the graph.

  >>> @tf.function
  ... def f(a, b):
  ...   print(\'this runs at trace time; a is\', a, \'and b is\', b)
  ...   return b
  >>> f(1, tf.constant(1))
  this runs at trace time; a is 1 and b is Tensor("...", shape=(), dtype=int32)
  <tf.Tensor: shape=(), dtype=int32, numpy=1>

  >>> f(1, tf.constant(2))
  <tf.Tensor: shape=(), dtype=int32, numpy=2>

  >>> f(2, tf.constant(1))
  this runs at trace time; a is 2 and b is Tensor("...", shape=(), dtype=int32)
  <tf.Tensor: shape=(), dtype=int32, numpy=1>

  >>> f(2, tf.constant(2))
  <tf.Tensor: shape=(), dtype=int32, numpy=2>

  Args:
    func: The function to be compiled. If `func` is None, `tf.function` returns
      a decorator that can be invoked with a single argument - `func`. In other
      words, `tf.function(input_signature=...)(func)` is equivalent to
      `tf.function(func, input_signature=...)`. The former can be used as
      decorator.
    input_signature: A possibly nested sequence of `tf.TensorSpec` objects
      specifying the shapes and dtypes of the Tensors that will be supplied to
      this function. If `None`, a separate function is instantiated for each
      inferred input signature.  If input_signature is specified, every input to
      `func` must be a `Tensor`, and `func` cannot accept `**kwargs`.
    autograph: Whether autograph should be applied on `func` before tracing a
      graph. Data-dependent Python control flow statements require
      `autograph=True`. For more information, see the
      [tf.function and AutoGraph guide](
      https://www.tensorflow.org/guide/function#autograph_transformations).
    jit_compile: If `True`, compiles the function using
      [XLA](https://tensorflow.org/xla). XLA performs compiler optimizations,
      such as fusion, and attempts to emit more efficient code. This may
      drastically improve the performance. If set to `True`,
      the whole function needs to be compilable by XLA, or an
      `errors.InvalidArgumentError` is thrown.
      If `None` (default), compiles the function with XLA when running on TPU
      and goes through the regular function execution path when running on
      other devices.
      If `False`, executes the function without XLA compilation.  Set this value
      to `False` when directly running a multi-device function on TPUs (e.g. two
      TPU cores, one TPU core and its host CPU).
      Not all functions are compilable, see a list of
      [sharp corners](https://tensorflow.org/xla/known_issues).
    reduce_retracing: When True, `tf.function` attempts to reduce the
      amount of retracing, for example by using more generic shapes. This
      can be controlled for user objects by customizing their associated
      `tf.types.experimental.TraceType`.
    experimental_implements: If provided, contains a name of a "known" function
      this implements. For example "mycompany.my_recurrent_cell".
      This is stored as an attribute in inference function,
      which can then be detected when processing serialized function.
      See [standardizing composite ops](https://github.com/tensorflow/community/blob/master/rfcs/20190610-standardizing-composite_ops.md)  # pylint: disable=line-too-long
      for details.  For an example of utilizing this attribute see this
      [example](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/compiler/mlir/lite/transforms/prepare_composite_functions_tf.cc)
      The code above automatically detects and substitutes function that
      implements "embedded_matmul" and allows TFLite to substitute its own
      implementations. For instance, a tensorflow user can use this
       attribute to mark that their function also implements
      `embedded_matmul` (perhaps more efficiently!)
      by specifying it using this parameter:
      `@tf.function(experimental_implements="embedded_matmul")`
      This can either be specified as just the string name of the function or
      a NameAttrList corresponding to a list of key-value attributes associated
      with the function name. The name of the function will be in the \'name\'
      field of the NameAttrList. To define a formal TF op for this function
      implements, try the experimental [composite TF](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/compiler/mlir/tfr)
      project.
    experimental_autograph_options: Optional tuple of
      `tf.autograph.experimental.Feature` values.
    experimental_attributes: Optional dictionary of attributes to include in the
      generated FunctionDefs.
    experimental_relax_shapes: Deprecated. Use `reduce_retracing`
      instead.
    experimental_compile: Deprecated alias to \'jit_compile\'.
    experimental_follow_type_hints: Deprecated. Please use input_signature or
      reduce_retracing instead.

  Returns:
     If `func` is not None, returns a `tf.types.experimental.GenericFunction`.
     If `func` is None, returns a decorator that, when invoked with a single
     `func` argument, returns a `tf.types.experimental.GenericFunction`.

  Raises:
     `ValueError` when attempting to use `jit_compile=True`, but XLA support is
     not available.
  '''
