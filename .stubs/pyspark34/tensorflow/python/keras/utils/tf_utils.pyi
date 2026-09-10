from _typeshed import Incomplete
from collections.abc import Generator
from tensorflow.python.data.experimental.ops import cardinality as cardinality
from tensorflow.python.eager import context as context
from tensorflow.python.framework import composite_tensor as composite_tensor, ops as ops, sparse_tensor as sparse_tensor, tensor_shape as tensor_shape, tensor_spec as tensor_spec, tensor_util as tensor_util, type_spec as type_spec
from tensorflow.python.keras.engine import keras_tensor as keras_tensor
from tensorflow.python.keras.utils import object_identity as object_identity, tf_contextlib as tf_contextlib
from tensorflow.python.ops import math_ops as math_ops, variables as variables
from tensorflow.python.ops.ragged import ragged_tensor as ragged_tensor, ragged_tensor_value as ragged_tensor_value
from tensorflow.python.util import nest as nest
from tensorflow.python.util.tf_export import keras_export as keras_export

def is_tensor_or_tensor_list(v): ...
def get_reachable_from_inputs(inputs, targets: Incomplete | None = None):
    """Returns the set of tensors/ops reachable from `inputs`.

  Stops if all targets have been found (target is optional).

  Only valid in Symbolic mode, not Eager mode.

  Args:
    inputs: List of tensors.
    targets: List of tensors.

  Returns:
    A set of tensors reachable from the inputs (includes the inputs themselves).
  """
def map_structure_with_atomic(is_atomic_fn, map_fn, nested):
    """Maps the atomic elements of a nested structure.

  Args:
    is_atomic_fn: A function that determines if an element of `nested` is
      atomic.
    map_fn: The function to apply to atomic elements of `nested`.
    nested: A nested structure.

  Returns:
    The nested structure, with atomic elements mapped according to `map_fn`.

  Raises:
    ValueError: If an element that is neither atomic nor a sequence is
      encountered.
  """
def get_shapes(tensors):
    """Gets shapes from tensors."""
def convert_shapes(input_shape, to_tuples: bool = True):
    """Converts nested shape representations to desired format.

  Performs:

  TensorShapes -> tuples if `to_tuples=True`.
  tuples of int or None -> TensorShapes if `to_tuples=False`.

  Valid objects to be converted are:
  - TensorShapes
  - tuples with elements of type int or None.
  - ints
  - None

  Args:
    input_shape: A nested structure of objects to be converted to TensorShapes.
    to_tuples: If `True`, converts all TensorShape to tuples. Otherwise converts
      all tuples representing shapes to TensorShapes.

  Returns:
    Nested structure of shapes in desired format.

  Raises:
    ValueError: when the input tensor shape can't be converted to tuples, eg
      unknown tensor shape.
  """

class ListWrapper:
    """A wrapper for lists to be treated as elements for `nest`."""
    def __init__(self, list_to_wrap) -> None: ...
    def as_list(self): ...

def convert_inner_node_data(nested, wrap: bool = False):
    """Either wraps or unwraps innermost node data lists in `ListWrapper` objects.

  Args:
    nested: A nested data structure.
    wrap: If `True`, wrap innermost lists in `ListWrapper` objects. If `False`,
      unwraps `ListWrapper` objects into lists.

  Returns:
    Structure of same type as nested, with lists wrapped/unwrapped.
  """
def shape_type_conversion(fn):
    """Decorator that handles tuple/TensorShape conversion.

  Used in `compute_output_shape` and `build`.

  Args:
    fn: function to wrap.

  Returns:
    Wrapped function.
  """
def are_all_symbolic_tensors(tensors): ...
def is_extension_type(tensor):
    """Returns whether a tensor is of an ExtensionType.

  github.com/tensorflow/community/pull/269
  Currently it works by checking if `tensor` is a `CompositeTensor` instance,
  but this will be changed to use an appropriate extensiontype protocol
  check once ExtensionType is made public.

  Args:
    tensor: An object to test

  Returns:
    True if the tensor is an extension type object, false if not.
  """
def is_symbolic_tensor(tensor):
    """Returns whether a tensor is symbolic (from a TF graph) or an eager tensor.

  A Variable can be seen as either: it is considered symbolic
  when we are in a graph scope, and eager when we are in an eager scope.

  Args:
    tensor: A tensor instance to test.

  Returns:
    True for symbolic tensors, False for eager tensors.
  """
def register_symbolic_tensor_type(cls) -> None:
    """Allows users to specify types regarded as symbolic `Tensor`s.

  Used in conjunction with `tf.register_tensor_conversion_function`, calling
  `tf.keras.__internal__.utils.register_symbolic_tensor_type(cls)`
  allows non-`Tensor` objects to be plumbed through Keras layers.

  Example:

  ```python
  # One-time setup.
  class Foo(object):
    def __init__(self, input_):
      self._input = input_
    def value(self):
      return tf.constant(42.)

  tf.register_tensor_conversion_function(
      Foo, lambda x, *args, **kwargs: x.value())

  tf.keras.__internal__.utils.register_symbolic_tensor_type(Foo)

  # User-land.
  layer = tf.keras.layers.Lambda(lambda input_: Foo(input_))
  ```

  Args:
    cls: A `class` type which shall be regarded as a symbolic `Tensor`.
  """
def type_spec_from_value(value):
    """Grab type_spec without converting array-likes to tensors."""
def is_ragged(tensor):
    """Returns true if `tensor` is a ragged tensor or ragged tensor value."""
def is_sparse(tensor):
    """Returns true if `tensor` is a sparse tensor or sparse tensor value."""
def is_tensor_or_variable(x): ...
def assert_no_legacy_layers(layers) -> None:
    """Prevent tf.layers.Layers from being used with Keras.

  Certain legacy layers inherit from their keras analogs; however they are
  not supported with keras and can lead to subtle and hard to diagnose bugs.

  Args:
    layers: A list of layers to check

  Raises:
    TypeError: If any elements of layers are tf.layers.Layers
  """
def maybe_init_scope(layer) -> Generator[None, None, None]:
    """Open an `init_scope` if in V2 mode and using the keras graph.

  Args:
    layer: The Layer/Model that is currently active.

  Yields:
    None
  """
def graph_context_for_symbolic_tensors(*args, **kwargs) -> Generator[None, None, None]:
    """Returns graph context manager if any of the inputs is a symbolic tensor."""
def dataset_is_infinite(dataset):
    """True if the passed dataset is infinite."""
def get_tensor_spec(t, dynamic_batch: bool = False, name: Incomplete | None = None):
    """Returns a `TensorSpec` given a single `Tensor` or `TensorSpec`."""
def sync_to_numpy_or_python_type(tensors):
    """Syncs and converts a structure of `Tensor`s to `NumPy` arrays or Python scalar types.

  For each tensor, it calls `tensor.numpy()`. If the result is a scalar value,
  it converts it to a Python type, such as a float or int, by calling
  `result.item()`.

  Numpy scalars are converted, as Python types are often more convenient to deal
  with. This is especially useful for bfloat16 Numpy scalars, which don't
  support as many operations as other Numpy values.

  Async strategies (such as `TPUStrategy` and `ParameterServerStrategy`) are
  forced to
  sync during this process.

  Args:
    tensors: A structure of tensors.

  Returns:
    `tensors`, but scalar tensors are converted to Python types and non-scalar
    tensors are converted to Numpy arrays.
  """
