from _typeshed import Incomplete
from tensorflow.python.framework import ops as ops
from tensorflow.python.util import tf_decorator as tf_decorator, tf_inspect as tf_inspect, traceback_utils as traceback_utils, type_annotations as type_annotations
from tensorflow.python.util.tf_export import tf_export as tf_export

FALLBACK_DISPATCH_ATTR: str
TYPE_BASED_DISPATCH_ATTR: str

class OpDispatcher:
    """Abstract base class for TensorFlow operator dispatchers.

  Each operation dispatcher acts as an override handler for a single
  TensorFlow operation, and its results are used when the handler indicates
  that it can handle the operation's arguments (by returning any value other
  than `OpDispatcher.NOT_SUPPORTED`).
  """
    NOT_SUPPORTED: Incomplete
    def handle(self, args, kwargs):
        """Handle this dispatcher's operation with the specified arguments.

    If this operation dispatcher can handle the given arguments, then
    return an appropriate value (or raise an appropriate exception).

    Args:
      args: The arguments to the operation.
      kwargs: They keyword arguments to the operation.

    Returns:
      The result of the operation, or `OpDispatcher.NOT_SUPPORTED` if this
      dispatcher can not handle the given arguments.
    """
    def register(self, op) -> None:
        """Register this dispatcher as a handler for `op`.

    Args:
      op: Python function: the TensorFlow operation that should be handled. Must
        have a dispatch list (which is added automatically for generated ops,
        and can be added to Python ops using the `add_dispatch_support`
        decorator).
    """

class GlobalOpDispatcher:
    """Abstract base class for TensorFlow global operator dispatchers."""
    NOT_SUPPORTED: Incomplete
    def handle(self, op, args, kwargs) -> None:
        """Handle the specified operation with the specified arguments."""
    def register(self) -> None:
        """Register this dispatcher as a handler for all ops."""

def dispatch(op, args, kwargs):
    """Returns the result from the first successful dispatcher for a given op.

  Calls the `handle` method of each `OpDispatcher` that has been registered
  to handle `op`, and returns the value from the first successful handler.

  Args:
    op: Python function: the operation to dispatch for.
    args: The arguments to the operation.
    kwargs: They keyword arguments to the operation.

  Returns:
    The result of the operation, or `NOT_SUPPORTED` if no registered
    dispatcher can handle the given arguments.
  """

class _TypeBasedDispatcher(OpDispatcher):
    """Dispatcher that handles op if any arguments have a specified type.

  Checks the types of the arguments and keyword arguments (including elements
  of lists or tuples), and if any argument values have the indicated type(s),
  then delegates to an override function.
  """
    def __init__(self, override_func, types) -> None: ...
    def handle(self, args, kwargs): ...

def dispatch_for_types(op, *types):
    """Decorator to declare that a Python function overrides an op for a type.

  The decorated function is used to override `op` if any of the arguments or
  keyword arguments (including elements of lists or tuples) have one of the
  specified types.

  Example:

  ```python
  @dispatch_for_types(math_ops.add, RaggedTensor, RaggedTensorValue)
  def ragged_add(x, y, name=None): ...
  ```

  Args:
    op: Python function: the operation that should be overridden.
    *types: The argument types for which this function should be used.
  """
def add_fallback_dispatch_list(target):
    """Decorator that adds a dispatch_list attribute to an op."""
add_dispatch_list = add_fallback_dispatch_list

def dispatch_for_api(api, *signatures):
    '''Decorator that overrides the default implementation for a TensorFlow API.

  The decorated function (known as the "dispatch target") will override the
  default implementation for the API when the API is called with parameters that
  match a specified type signature.  Signatures are specified using dictionaries
  that map parameter names to type annotations.  E.g., in the following example,
  `masked_add` will be called for `tf.add` if both `x` and `y` are
  `MaskedTensor`s:

  >>> class MaskedTensor(tf.experimental.ExtensionType):
  ...   values: tf.Tensor
  ...   mask: tf.Tensor

  >>> @dispatch_for_api(tf.math.add, {\'x\': MaskedTensor, \'y\': MaskedTensor})
  ... def masked_add(x, y, name=None):
  ...   return MaskedTensor(x.values + y.values, x.mask & y.mask)

  >>> mt = tf.add(MaskedTensor([1, 2], [True, False]), MaskedTensor(10, True))
  >>> print(f"values={mt.values.numpy()}, mask={mt.mask.numpy()}")
  values=[11 12], mask=[ True False]

  If multiple type signatures are specified, then the dispatch target will be
  called if any of the signatures match.  For example, the following code
  registers `masked_add` to be called if `x` is a `MaskedTensor` *or* `y` is
  a `MaskedTensor`.

  >>> @dispatch_for_api(tf.math.add, {\'x\': MaskedTensor}, {\'y\':MaskedTensor})
  ... def masked_add(x, y):
  ...   x_values = x.values if isinstance(x, MaskedTensor) else x
  ...   x_mask = x.mask if isinstance(x, MaskedTensor) else True
  ...   y_values = y.values if isinstance(y, MaskedTensor) else y
  ...   y_mask = y.mask if isinstance(y, MaskedTensor) else True
  ...   return MaskedTensor(x_values + y_values, x_mask & y_mask)

  The type annotations in type signatures may be type objects (e.g.,
  `MaskedTensor`), `typing.List` values, or `typing.Union` values.   For
  example, the following will register `masked_concat` to be called if `values`
  is a list of `MaskedTensor` values:

  >>> @dispatch_for_api(tf.concat, {\'values\': typing.List[MaskedTensor]})
  ... def masked_concat(values, axis):
  ...   return MaskedTensor(tf.concat([v.values for v in values], axis),
  ...                       tf.concat([v.mask for v in values], axis))

  Each type signature must contain at least one subclass of `tf.CompositeTensor`
  (which includes subclasses of `tf.ExtensionType`), and dispatch will only be
  triggered if at least one type-annotated parameter contains a
  `CompositeTensor` value.  This rule avoids invoking dispatch in degenerate
  cases, such as the following examples:

  * `@dispatch_for_api(tf.concat, {\'values\': List[MaskedTensor]})`: Will not
    dispatch to the decorated dispatch target when the user calls
    `tf.concat([])`.

  * `@dispatch_for_api(tf.add, {\'x\': Union[MaskedTensor, Tensor], \'y\':
    Union[MaskedTensor, Tensor]})`: Will not dispatch to the decorated dispatch
    target when the user calls `tf.add(tf.constant(1), tf.constant(2))`.

  The dispatch target\'s signature must match the signature of the API that is
  being overridden.  In particular, parameters must have the same names, and
  must occur in the same order.  The dispatch target may optionally elide the
  "name" parameter, in which case it will be wrapped with a call to
  `tf.name_scope` when appropraite.

  Args:
    api: The TensorFlow API to override.
    *signatures: Dictionaries mapping parameter names or indices to type
      annotations, specifying when the dispatch target should be called.  In
      particular, the dispatch target will be called if any signature matches;
      and a signature matches if all of the specified parameters have types that
      match with the indicated type annotations.  If no signatures are
      specified, then a signature will be read from the dispatch target
      function\'s type annotations.

  Returns:
    A decorator that overrides the default implementation for `api`.

  #### Registered APIs

  The TensorFlow APIs that may be overridden by `@dispatch_for_api` are:

  <<API_LIST>>
  '''
def apis_with_type_based_dispatch():
    """Returns a list of TensorFlow APIs that support type-based dispatch."""
def type_based_dispatch_signatures_for(cls):
    """Returns dispatch signatures that have been registered for a given class.

  This function is intended for documentation-generation purposes.

  Args:
    cls: The class to search for.  Type signatures are searched recursively, so
      e.g., if `cls=RaggedTensor`, then information will be returned for all
      dispatch targets that have `RaggedTensor` anywhere in their type
      annotations (including nested in `typing.Union` or `typing.List`.)

  Returns:
    A `dict` mapping `api` -> `signatures`, where `api` is a TensorFlow API
    function; and `signatures` is a list of dispatch signatures for `api`
    that include `cls`.  (Each signature is a dict mapping argument names to
    type annotations; see `dispatch_for_api` for more info.)
  """
def unregister_dispatch_for(dispatch_target) -> None:
    """Unregisters a function that was registered with `@dispatch_for_*`.

  This is primarily intended for testing purposes.

  Example:

  >>> # Define a type and register a dispatcher to override `tf.abs`:
  >>> class MyTensor(tf.experimental.ExtensionType):
  ...   value: tf.Tensor
  >>> @tf.experimental.dispatch_for_api(tf.abs)
  ... def my_abs(x: MyTensor):
  ...   return MyTensor(tf.abs(x.value))
  >>> tf.abs(MyTensor(5))
  MyTensor(value=<tf.Tensor: shape=(), dtype=int32, numpy=5>)

  >>> # Unregister the dispatcher, so `tf.abs` no longer calls `my_abs`.
  >>> unregister_dispatch_for(my_abs)
  >>> tf.abs(MyTensor(5))
  Traceback (most recent call last):
  ...
  ValueError: Attempt to convert a value ... to a Tensor.

  Args:
    dispatch_target: The function to unregister.

  Raises:
    ValueError: If `dispatch_target` was not registered using `@dispatch_for`,
      `@dispatch_for_unary_elementwise_apis`, or
      `@dispatch_for_binary_elementwise_apis`.
  """
def register_dispatchable_type(cls):
    """Class decorator that registers a type for use with type-based dispatch.

  Should *not* be used with subclasses of `CompositeTensor` or `ExtensionType`
  (which are automatically registered).

  Note: this function is intended to support internal legacy use cases (such
  as RaggedTensorValue), and will probably not be exposed as a public API.

  Args:
    cls: The class to register.

  Returns:
    `cls`.
  """
def add_type_based_api_dispatcher(target):
    """Adds a PythonAPIDispatcher to the given TensorFlow API function."""
def make_type_checker(annotation):
    """Builds a PyTypeChecker for the given type annotation."""
def dispatch_for_unary_elementwise_apis(x_type):
    '''Decorator to override default implementation for unary elementwise APIs.

  The decorated function (known as the "elementwise api handler") overrides
  the default implementation for any unary elementwise API whenever the value
  for the first argument (typically named `x`) matches the type annotation
  `x_type`. The elementwise api handler is called with two arguments:

    `elementwise_api_handler(api_func, x)`

  Where `api_func` is a function that takes a single parameter and performs the
  elementwise operation (e.g., `tf.abs`), and `x` is the first argument to the
  elementwise api.

  The following example shows how this decorator can be used to update all
  unary elementwise operations to handle a `MaskedTensor` type:

  >>> class MaskedTensor(tf.experimental.ExtensionType):
  ...   values: tf.Tensor
  ...   mask: tf.Tensor
  >>> @dispatch_for_unary_elementwise_apis(MaskedTensor)
  ... def unary_elementwise_api_handler(api_func, x):
  ...   return MaskedTensor(api_func(x.values), x.mask)
  >>> mt = MaskedTensor([1, -2, -3], [True, False, True])
  >>> abs_mt = tf.abs(mt)
  >>> print(f"values={abs_mt.values.numpy()}, mask={abs_mt.mask.numpy()}")
  values=[1 2 3], mask=[ True False True]

  For unary elementwise operations that take extra arguments beyond `x`, those
  arguments are *not* passed to the elementwise api handler, but are
  automatically added when `api_func` is called.  E.g., in the following
  example, the `dtype` parameter is not passed to
  `unary_elementwise_api_handler`, but is added by `api_func`.

  >>> ones_mt = tf.ones_like(mt, dtype=tf.float32)
  >>> print(f"values={ones_mt.values.numpy()}, mask={ones_mt.mask.numpy()}")
  values=[1.0 1.0 1.0], mask=[ True False True]

  Args:
    x_type: A type annotation indicating when the api handler should be called.
      See `dispatch_for_api` for a list of supported annotation types.

  Returns:
    A decorator.

  #### Registered APIs

  The unary elementwise APIs are:

  <<API_LIST>>
  '''
def dispatch_for_binary_elementwise_apis(x_type, y_type):
    '''Decorator to override default implementation for binary elementwise APIs.

  The decorated function (known as the "elementwise api handler") overrides
  the default implementation for any binary elementwise API whenever the value
  for the first two arguments (typically named `x` and `y`) match the specified
  type annotations.  The elementwise api handler is called with two arguments:

    `elementwise_api_handler(api_func, x, y)`

  Where `x` and `y` are the first two arguments to the elementwise api, and
  `api_func` is a TensorFlow function that takes two parameters and performs the
  elementwise operation (e.g., `tf.add`).

  The following example shows how this decorator can be used to update all
  binary elementwise operations to handle a `MaskedTensor` type:

  >>> class MaskedTensor(tf.experimental.ExtensionType):
  ...   values: tf.Tensor
  ...   mask: tf.Tensor
  >>> @dispatch_for_binary_elementwise_apis(MaskedTensor, MaskedTensor)
  ... def binary_elementwise_api_handler(api_func, x, y):
  ...   return MaskedTensor(api_func(x.values, y.values), x.mask & y.mask)
  >>> a = MaskedTensor([1, 2, 3, 4, 5], [True, True, True, True, False])
  >>> b = MaskedTensor([2, 4, 6, 8, 0], [True, True, True, False, True])
  >>> c = tf.add(a, b)
  >>> print(f"values={c.values.numpy()}, mask={c.mask.numpy()}")
  values=[ 3 6 9 12 5], mask=[ True True True False False]

  Args:
    x_type: A type annotation indicating when the api handler should be called.
    y_type: A type annotation indicating when the api handler should be called.

  Returns:
    A decorator.

  #### Registered APIs

  The binary elementwise APIs are:

  <<API_LIST>>
  '''
def dispatch_for_binary_elementwise_assert_apis(x_type, y_type):
    '''Decorator to override default implementation for binary elementwise assert APIs.

  The decorated function (known as the "elementwise assert handler")
  overrides the default implementation for any binary elementwise assert API
  whenever the value for the first two arguments (typically named `x` and `y`)
  match the specified type annotations.  The handler is called with two
  arguments:

    `elementwise_assert_handler(assert_func, x, y)`

  Where `x` and `y` are the first two arguments to the binary elementwise assert
  operation, and `assert_func` is a TensorFlow function that takes two
  parameters and performs the elementwise assert operation (e.g.,
  `tf.debugging.assert_equal`).

  The following example shows how this decorator can be used to update all
  binary elementwise assert operations to handle a `MaskedTensor` type:

  >>> class MaskedTensor(tf.experimental.ExtensionType):
  ...   values: tf.Tensor
  ...   mask: tf.Tensor
  >>> @dispatch_for_binary_elementwise_assert_apis(MaskedTensor, MaskedTensor)
  ... def binary_elementwise_assert_api_handler(assert_func, x, y):
  ...   merged_mask = tf.logical_and(x.mask, y.mask)
  ...   selected_x_values = tf.boolean_mask(x.values, merged_mask)
  ...   selected_y_values = tf.boolean_mask(y.values, merged_mask)
  ...   assert_func(selected_x_values, selected_y_values)
  >>> a = MaskedTensor([1, 1, 0, 1, 1], [False, False, True, True, True])
  >>> b = MaskedTensor([2, 2, 0, 2, 2], [True, True, True, False, False])
  >>> tf.debugging.assert_equal(a, b) # assert passed; no exception was thrown

  >>> a = MaskedTensor([1, 1, 1, 1, 1], [True, True, True, True, True])
  >>> b = MaskedTensor([0, 0, 0, 0, 2], [True, True, True, True, True])
  >>> tf.debugging.assert_greater(a, b)
  Traceback (most recent call last):
  ...
  InvalidArgumentError: Condition x > y did not hold.

  Args:
    x_type: A type annotation indicating when the api handler should be called.
    y_type: A type annotation indicating when the api handler should be called.

  Returns:
    A decorator.

  #### Registered APIs

  The binary elementwise assert APIs are:

  <<API_LIST>>
  '''
def register_unary_elementwise_api(func):
    """Decorator that registers a TensorFlow op as a unary elementwise API."""
def register_binary_elementwise_api(func):
    """Decorator that registers a TensorFlow op as a binary elementwise API."""
def register_binary_elementwise_assert_api(func):
    """Decorator that registers a TensorFlow op as a binary elementwise assert API.

  Different from `dispatch_for_binary_elementwise_apis`, this decorator is used
  for assert apis, such as assert_equal, assert_none_equal, etc, which return
  None in eager mode and an op in graph mode.

  Args:
    func: The function that implements the binary elementwise assert API.

  Returns:
    `func`
  """
def unary_elementwise_apis():
    """Returns a list of APIs that have been registered as unary elementwise."""
def binary_elementwise_apis():
    """Returns a list of APIs that have been registered as binary elementwise."""
def update_docstrings_with_api_lists() -> None:
    """Updates the docstrings of dispatch decorators with API lists.

  Updates docstrings for `dispatch_for_api`,
  `dispatch_for_unary_elementwise_apis`, and
  `dispatch_for_binary_elementwise_apis`, by replacing the string '<<API_LIST>>'
  with a list of APIs that have been registered for that decorator.
  """
def add_dispatch_support(target: Incomplete | None = None, iterable_parameters: Incomplete | None = None):
    """Decorator that adds a dispatch handling wrapper to a TensorFlow Python API.

  This wrapper adds the decorated function as an API that can be overridden
  using the `@dispatch_for_api` decorator.  In the following example, we first
  define a new API (`double`) that supports dispatch, then define a custom type
  (`MaskedTensor`) and finally use `dispatch_for_api` to override the default
  implementation of `double` when called with `MaskedTensor` values:

  >>> @add_dispatch_support
  ... def double(x):
  ...   return x * 2
  >>> class MaskedTensor(tf.experimental.ExtensionType):
  ...   values: tf.Tensor
  ...   mask: tf.Tensor
  >>> @dispatch_for_api(double, {'x': MaskedTensor})
  ... def masked_double(x):
  ...   return MaskedTensor(x.values * 2, y.mask)

  The optional `iterable_parameter` argument can be used to mark parameters that
  can take arbitrary iterable values (such as generator expressions).  These
  need to be handled specially during dispatch, since just iterating over an
  iterable uses up its values.  In the following example, we define a new API
  whose second argument can be an iterable value; and then override the default
  implementatio of that API when the iterable contains MaskedTensors:

  >>> @add_dispatch_support(iterable_parameters=['ys'])
  ... def add_tensor_to_list_of_tensors(x, ys):
  ...   return [x + y for y in ys]
  >>> @dispatch_for_api(add_tensor_to_list_of_tensors,
  ...               {'ys': typing.List[MaskedTensor]})
  ... def masked_add_tensor_to_list_of_tensors(x, ys):
  ...   return [MaskedTensor(x+y.values, y.mask) for y in ys]

  (Note: the only TensorFlow API that currently supports iterables is `add_n`.)

  Args:
    target: The TensorFlow API that should support dispatch.
    iterable_parameters: Optional list of parameter names that may be called
      with iterables (such as the `inputs` parameter for `tf.add_n`).

  Returns:
    A decorator.
  """
def replace_iterable_params(args, kwargs, iterable_params):
    """Returns (args, kwargs) with any iterable parameters converted to lists.

  Args:
    args: Positional rguments to a function
    kwargs: Keyword arguments to a function.
    iterable_params: A list of (name, index) tuples for iterable parameters.

  Returns:
    A tuple (args, kwargs), where any positional or keyword parameters in
    `iterable_params` have their value converted to a `list`.
  """
