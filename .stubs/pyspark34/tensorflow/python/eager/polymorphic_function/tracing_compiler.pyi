from _typeshed import Incomplete
from tensorflow.core.function import trace_type as trace_type
from tensorflow.core.function.capture import capture_container as capture_container
from tensorflow.core.function.polymorphism import function_cache as function_cache
from tensorflow.python.eager import monitoring as monitoring
from tensorflow.python.eager.polymorphic_function import function_context as function_context, function_spec as function_spec, monomorphic_function as monomorphic_function
from tensorflow.python.profiler import trace as trace
from tensorflow.python.util import compat as compat, lazy_loader as lazy_loader, tf_decorator as tf_decorator, tf_inspect as tf_inspect

ag_ctx: Incomplete

class TracingCompiler:
    """Generates, caches and dispatchs traced Monomorphic Concrete Functions.

  The tracing is done using the Python source function with respect to inputs
  and other options specified by constructor.

  See the documentation for `tf.function` for more information on the semantics
  of defined functions.

  `TracingCompiler` class is thread-compatible meaning that minimal usage of
  tf.function (defining and calling) is thread-safe, but if users call other
  methods or invoke the base `python_function` themselves, external
  synchronization is necessary.

  In addition, TracingCompiler is not reentrant, so recursive functions need
  to call the wrapped function, not the wrapper.
  """
    tracing_count: int
    def __init__(self, python_function, name, input_signature: Incomplete | None = None, attributes: Incomplete | None = None, autograph: bool = True, autograph_options: Incomplete | None = None, reduce_retracing: bool = False, capture_by_value: Incomplete | None = None, jit_compile: Incomplete | None = None) -> None:
        """Initializes a `TracingCompiler`.

    Args:
      python_function: the function to be wrapped.
      name: the name given to it.
      input_signature: a possibly nested sequence of `TensorSpec` objects
        specifying the input signature of this function. If `None`, a separate
        function is instantiated for each inferred input signature.
      attributes: dict, extra keyword arguments that will be added as attribute
        of the function.
      autograph: whether to use autograph to compile `python_function`. See
        https://www.tensorflow.org/guide/autograph for more information.
      autograph_options: Experimental knobs to control behavior `when
        autograph=True`. See https://www.tensorflow.org/guide/autograph for more
        information.
      reduce_retracing: When True, `tf.function` uses
        `tf.types.experimental.TraceType` to trace supertypes of arguments to
        reduce the number of traces.
      capture_by_value: Experimental. Whether to capture resource variables by
        value or reference. If None, will inherit from a parent context or
        default to False.
      jit_compile: Force-compile the function with XLA, cf. tf.function doc on
        jit_compile.

    Raises:
      ValueError: if `input_signature` is not None and the `python_function`'s
        argspec has keyword arguments.
    """
    def __call__(self, *args, **kwargs):
        """Calls a graph function specialized to the inputs."""
    @property
    def python_function(self):
        """Returns the wrapped Python function."""
    @property
    def function_spec(self): ...
    @property
    def input_signature(self):
        """Returns the input signature."""
    def get_concrete_function(self, *args, **kwargs):
        """Returns a `ConcreteFunction` specialized to inputs and execution context.

    Args:
      *args: inputs to specialize on. Can be concrete values (e.g. 1) or
        `tf.Tensor` or `tf.TensorSpec`.
      **kwargs: keyword inputs to specialize on. Concrete values (e.g. 1) or
        `tf.Tensor` or `tf.TensorSpec`.
    """
    def __get__(self, instance, owner):
        """Makes it possible to decorate instance methods."""

class TfMethodTarget:
    """Binding target for methods replaced by function and defun."""
    weakrefself_target__: Incomplete
    weakrefself_func__: Incomplete
    def __init__(self, target, original_python_function) -> None: ...
    @property
    def target(self): ...
    @property
    def target_class(self): ...
    def call(self, args, kwargs): ...

def class_method_to_instance_method(original_function, instance):
    """Constructs a new `TracingCompiler` with `self` bound."""
