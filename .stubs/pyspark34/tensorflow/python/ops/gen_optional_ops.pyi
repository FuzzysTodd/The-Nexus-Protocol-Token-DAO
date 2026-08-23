from _typeshed import Incomplete
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export

def optional_from_value(components, name: Incomplete | None = None):
    """Constructs an Optional variant from a tuple of tensors.

  Args:
    components: A list of `Tensor` objects.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

OptionalFromValue: Incomplete

def optional_from_value_eager_fallback(components, name, ctx): ...
def optional_get_value(optional, output_types, output_shapes, name: Incomplete | None = None):
    """Returns the value stored in an Optional variant or raises an error if none exists.

  Args:
    optional: A `Tensor` of type `variant`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A list of `Tensor` objects of type `output_types`.
  """

OptionalGetValue: Incomplete

def optional_get_value_eager_fallback(optional, output_types, output_shapes, name, ctx): ...
def optional_has_value(optional, name: Incomplete | None = None):
    """Returns true if and only if the given Optional variant has a value.

  Args:
    optional: A `Tensor` of type `variant`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `bool`.
  """

OptionalHasValue: Incomplete

def optional_has_value_eager_fallback(optional, name, ctx): ...
def optional_none(name: Incomplete | None = None):
    """Creates an Optional variant with no value.

  Args:
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

OptionalNone: Incomplete

def optional_none_eager_fallback(name, ctx): ...
