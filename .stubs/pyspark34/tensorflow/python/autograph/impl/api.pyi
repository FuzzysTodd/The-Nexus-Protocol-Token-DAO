from _typeshed import Incomplete
from tensorflow.python.autograph import operators as operators, utils as utils
from tensorflow.python.autograph.converters import asserts as asserts, break_statements as break_statements, call_trees as call_trees, conditional_expressions as conditional_expressions, continue_statements as continue_statements, control_flow as control_flow, directives as directives, functions as functions, lists as lists, logical_expressions as logical_expressions, return_statements as return_statements, slices as slices, variables as variables
from tensorflow.python.autograph.core import ag_ctx as ag_ctx, converter as converter, function_wrappers as function_wrappers, unsupported_features_checker as unsupported_features_checker
from tensorflow.python.autograph.impl import conversion as conversion
from tensorflow.python.autograph.lang import special_functions as special_functions
from tensorflow.python.autograph.operators import py_builtins as py_builtins
from tensorflow.python.autograph.pyct import anno as anno, cfg as cfg, error_utils as error_utils, errors as errors, inspect_utils as inspect_utils, origin_info as origin_info, qual_names as qual_names, transpiler as transpiler
from tensorflow.python.autograph.pyct.static_analysis import activity as activity, reaching_definitions as reaching_definitions
from tensorflow.python.eager import function as function
from tensorflow.python.framework import errors_impl as errors_impl
from tensorflow.python.util import tf_decorator as tf_decorator, tf_inspect as tf_inspect, tf_stack as tf_stack
from tensorflow.python.util.tf_export import tf_export as tf_export

def is_autograph_strict_conversion_mode(): ...

class AutoGraphError(errors.PyCTError):
    """Base class for all AutoGraph exceptions."""
class ConversionError(AutoGraphError):
    """Raised during the conversion process."""
class StagingError(AutoGraphError):
    """Raised during the staging (i.e. Python execution) of converted code."""

class _ErrorMetadata(error_utils.ErrorMetadataBase):
    """AutoGraph-specific error metadata. See base class."""
    def create_exception(self, source_error): ...

class StackTraceMapper(tf_stack.StackTraceMapper):
    """Remaps generated code to code it originated from."""
    def __init__(self, converted_fn) -> None: ...
    def get_effective_source_map(self): ...

class PyToTF(transpiler.PyToPy):
    """The TensorFlow AutoGraph transformer."""
    def __init__(self) -> None: ...
    def get_transformed_name(self, node): ...
    def get_extra_locals(self): ...
    def get_caching_key(self, ctx): ...
    def initial_analysis(self, node, ctx): ...
    def transform_ast(self, node, ctx): ...

def autograph_artifact(entity, extras: Incomplete | None = None): ...
def is_autograph_artifact(entity): ...
def converted_call(f, args, kwargs, caller_fn_scope: Incomplete | None = None, options: Incomplete | None = None):
    """Converts a function call inline.

  For internal use only.

  Note: The argument list is optimized for readability of generated code, which
  may look like this:

    ag__.converted_call(f, (arg1, arg2), None, fscope)
    ag__.converted_call(f, (), dict(arg1=val1, **kwargs), fscope)
    ag__.converted_call(f, (arg1, arg2) + varargs, dict(**kwargs), lscope)

  Args:
    f: The function to convert.
    args: Tuple, the original positional arguments of f
    kwargs: Optional[Dict], the original keyword arguments of f
    caller_fn_scope: Optional[function_wrappers.FunctionScope], the function
      scope of the converted function in which this call was originally made.
    options: Optional[converter.ConversionOptions], conversion options. If not
      specified, the value of caller_fn_scope.callopts is used. Either options
      or caller_fn_scope must be present.

  Returns:
    Any, the result of executing a possibly-converted `f` with the given
      arguments.
  """
def tf_convert(f, ctx, convert_by_default: bool = True, user_requested: bool = False):
    """Decorator that applies AutoGraph to a function.

  Use in internal APIs.

  This API is suitable for high order functions internal to the TensorFlow API,
  and more generally any function to which AutoGraph is not applied.

  Guidance: `convert` was a decorator meant for use directly by developers, but
  most of today's uses go through `tf.function`. `tf_convert` is to be called
  from high order functions internal to TF. By default, all the internal
  TensorFlow functions are skipped when AutoGraph processes the code. This may
  lead to user-supplied functions to be incorrectly skipped as well.
  `tf_convert` helps avoid that. See the following example for more details.

  ```
  =====tf_internal_module.py=====

  def unconverted(input_fn):
    return input_fn()

  def converted(input_fn):
    return tf.__internal__.autograph.tf_convert(
       input_fn, ctx=tf.__internal__.autograph.control_status_ctx())()

  ======user_module.py======

  @tf.function
  def foo(input_fn)
    return unconverted(input_fn)

  @tf.function
  def bar(input_fn)
    return converted(input_fn)

  @tf.function(autograph=False)
  def baz(input_fn)
    return converted(input_fn)
  ```

  The `foo` method above will execute the `input_fn` without autograph
  conversion, while the `bar` method will run an autographed `input_fn`. The
  `baz` method will run an unconverted `input_fn`, since `tf_convert` respect
  the control status context.

  Note that both methods in `tf_internal_module` are skipped by autograph when
  tracing the `tf.function`. The configuration of whether a module/package
  should be skipped by autograph is controlled in
  tensorflow/python/autograph/core/config.py.

  Args:
    f: Callable.
    ctx: ag_ctx.ControlStatusCtx, the Autograph context in which `f` is used.
    convert_by_default: bool, whether to use AutoGraph when the context doesn't
      specify.
    user_requested: bool, whether to ignore the conversion allowlist. See
      ConversionOptions.user_requested.

  Returns:
    Either `f or the converted version of `f`.
  """
def call_with_unspecified_conversion_status(func):
    """Decorator that resets the conversion context to the unspecified status."""
def do_not_convert(func: Incomplete | None = None):
    """Decorator that suppresses the conversion of a function.

  Args:
    func: function to decorate.

  Returns:
    If `func` is not None, returns a `Callable` which is equivalent to
    `func`, but is not converted by AutoGraph.
    If `func` is None, returns a decorator that, when invoked with a
    single `func` argument, returns a `Callable` equivalent to the
    above case.
  """
def convert(recursive: bool = False, optional_features: Incomplete | None = None, user_requested: bool = True, conversion_ctx=...):
    """Decorator that compiles a function to use TensorFlow ops.

  The decorator is dynamic - it recompiles the target whenever the decorated
  function is called. This means the parameter values are known at conversion.
  It also means that repeated calls with different types of parameters will be
  correctly processed.

  Args:
    recursive: bool, whether to recursively convert any functions or classes
      that the converted function may use.
    optional_features: converted.Feature, allows toggling optional or
      experimental features. When set to None, only the core features are
      enabled.
    user_requested: bool, whether this is a function that the user explicitly
      asked to be converted. See ConversionOptions.user_requested.
    conversion_ctx: Optional ag_ctx.ControlStatusCtx, the Autograph context in
      which `f` is used.

  Returns:
    Callable, a decorator that converts the given function into an equivalent
    function that uses TensorFlow ops.
  """
def to_graph(entity, recursive: bool = True, experimental_optional_features: Incomplete | None = None):
    """Converts a Python entity into a TensorFlow graph.

  Also see: `tf.autograph.to_code`, `tf.function`.

  Unlike `tf.function`, `to_graph` is a low-level transpiler that converts
  Python code to TensorFlow graph code. It does not implement any caching,
  variable management or create any actual ops, and is best used where greater
  control over the generated TensorFlow graph is desired. Another difference
  from `tf.function` is that `to_graph` will not wrap the graph into a
  TensorFlow function or a Python callable. Internally, `tf.function` uses
  `to_graph`.

  Example usage:

  >>> def f(x):
  ...   if x > 0:
  ...     y = x * x
  ...   else:
  ...     y = -x
  ...   return y
  ...
  >>> converted_f = to_graph(f)
  >>> x = tf.constant(2)
  >>> converted_f(x)  # converted_foo is like a TensorFlow Op.
  <tf.Tensor: shape=(), dtype=int32, numpy=4>

  Supported Python entities include:
    * functions
    * classes
    * object methods

  Functions are converted into new functions with converted code.

  Classes are converted by generating a new class whose methods use converted
  code.

  Methods are converted into unbound function that have an additional first
  argument called `self`.

  For a tutorial, see the
  [tf.function and AutoGraph guide](https://www.tensorflow.org/guide/function).
  For more detailed information, see the
  [AutoGraph reference documentation](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/autograph/g3doc/reference/index.md).

  Args:
    entity: Python callable or class to convert.
    recursive: Whether to recursively convert any functions that the converted
      function may call.
    experimental_optional_features: `None`, a tuple of, or a single
      `tf.autograph.experimental.Feature` value.

  Returns:
    Same as `entity`, the converted Python function or class.

  Raises:
    ValueError: If the entity could not be converted.
  """
def to_graph_v1(entity, recursive: bool = True, arg_values: Incomplete | None = None, arg_types: Incomplete | None = None, experimental_optional_features: Incomplete | None = None):
    """Converts a Python entity into a TensorFlow graph.

  Also see: `tf.autograph.to_code`, `tf.function`.

  Unlike `tf.function`, `to_graph` is a low-level transpiler that converts
  Python code to TensorFlow graph code. It does not implement any caching,
  variable management or create any actual ops, and is best used where greater
  control over the generated TensorFlow graph is desired. Another difference
  from `tf.function` is that `to_graph` will not wrap the graph into a
  TensorFlow function or a Python callable. Internally, `tf.function` uses
  `to_graph`.

  _Example Usage_

  ```python
    def foo(x):
      if x > 0:
        y = x * x
      else:
        y = -x
      return y

    converted_foo = to_graph(foo)

    x = tf.constant(1)
    y = converted_foo(x)  # converted_foo is a TensorFlow Op-like.
    assert is_tensor(y)
  ```

  Supported Python entities include:
    * functions
    * classes
    * object methods

  Functions are converted into new functions with converted code.

  Classes are converted by generating a new class whose methods use converted
  code.

  Methods are converted into unbound function that have an additional first
  argument called `self`.

  Args:
    entity: Python callable or class to convert.
    recursive: Whether to recursively convert any functions that the converted
      function may call.
    arg_values: Deprecated.
    arg_types: Deprecated.
    experimental_optional_features: `None`, a tuple of, or a single
      `tf.autograph.experimental.Feature` value.

  Returns:
    Same as `entity`, the converted Python function or class.

  Raises:
    ValueError: If the entity could not be converted.
  """
def to_code_v1(entity, recursive: bool = True, arg_values: Incomplete | None = None, arg_types: Incomplete | None = None, indentation: str = '  ', experimental_optional_features: Incomplete | None = None):
    '''Returns the source code generated by AutoGraph, as a string.

  Example usage:

  >>> def f(x):
  ...   if x < 0:
  ...     x = -x
  ...   return x
  >>> tf.autograph.to_code(f)
  "...def tf__f(x):..."

  Also see: `tf.autograph.to_graph`.

  Note: If a function has been decorated with `tf.function`, pass its
  underlying Python function, rather than the callable that `tf.function
  creates:

  >>> @tf.function
  ... def f(x):
  ...   if x < 0:
  ...     x = -x
  ...   return x
  >>> tf.autograph.to_code(f.python_function)
  "...def tf__f(x):..."

  Args:
    entity: Python callable or class.
    recursive: Whether to recursively convert any functions that the converted
      function may call.
    arg_values: Deprecated.
    arg_types: Deprecated.
    indentation: Deprecated.
    experimental_optional_features: `None`, a tuple of, or a single
      `tf.autograph.experimental.Feature` value.

  Returns:
    The converted code as string.
  '''
def to_code(entity, recursive: bool = True, experimental_optional_features: Incomplete | None = None):
    '''Returns the source code generated by AutoGraph, as a string.

  Example usage:

  >>> def f(x):
  ...   if x < 0:
  ...     x = -x
  ...   return x
  >>> tf.autograph.to_code(f)
  "...def tf__f(x):..."

  Also see: `tf.autograph.to_graph`.

  Note: If a function has been decorated with `tf.function`, pass its
  underlying Python function, rather than the callable that `tf.function
  creates:

  >>> @tf.function
  ... def f(x):
  ...   if x < 0:
  ...     x = -x
  ...   return x
  >>> tf.autograph.to_code(f.python_function)
  "...def tf__f(x):..."

  Args:
    entity: Python callable or class to convert.
    recursive: Whether to recursively convert any functions that the converted
      function may call.
    experimental_optional_features: `None`, a tuple of, or a single
      `tf.autograph.experimental.Feature` value.

  Returns:
    The converted code as string.
  '''
