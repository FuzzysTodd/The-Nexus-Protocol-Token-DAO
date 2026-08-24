import abc
from _typeshed import Incomplete
from tensorflow.core.protobuf import struct_pb2 as struct_pb2
from tensorflow.python.data.util import structure as structure
from tensorflow.python.framework import composite_tensor as composite_tensor, dtypes as dtypes, ops as ops, tensor_spec as tensor_spec, type_spec as type_spec
from tensorflow.python.ops import gen_optional_ops as gen_optional_ops
from tensorflow.python.saved_model import nested_structure_coder as nested_structure_coder
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.tf_export import tf_export as tf_export

class Optional(composite_tensor.CompositeTensor, metaclass=abc.ABCMeta):
    '''Represents a value that may or may not be present.

  A `tf.experimental.Optional` can represent the result of an operation that may
  fail as a value, rather than raising an exception and halting execution. For
  example, `tf.data.Iterator.get_next_as_optional()` returns a
  `tf.experimental.Optional` that either contains the next element of an
  iterator if one exists, or an "empty" value that indicates the end of the
  sequence has been reached.

  `tf.experimental.Optional` can only be used with values that are convertible
  to `tf.Tensor` or `tf.CompositeTensor`.

  One can create a `tf.experimental.Optional` from a value using the
  `from_value()` method:

  >>> optional = tf.experimental.Optional.from_value(42)
  >>> print(optional.has_value())
  tf.Tensor(True, shape=(), dtype=bool)
  >>> print(optional.get_value())
  tf.Tensor(42, shape=(), dtype=int32)

  or without a value using the `empty()` method:

  >>> optional = tf.experimental.Optional.empty(
  ...   tf.TensorSpec(shape=(), dtype=tf.int32, name=None))
  >>> print(optional.has_value())
  tf.Tensor(False, shape=(), dtype=bool)
  '''
    @abc.abstractmethod
    def has_value(self, name: Incomplete | None = None):
        """Returns a tensor that evaluates to `True` if this optional has a value.

    >>> optional = tf.experimental.Optional.from_value(42)
    >>> print(optional.has_value())
    tf.Tensor(True, shape=(), dtype=bool)

    Args:
      name: (Optional.) A name for the created operation.

    Returns:
      A scalar `tf.Tensor` of type `tf.bool`.
    """
    @abc.abstractmethod
    def get_value(self, name: Incomplete | None = None):
        """Returns the value wrapped by this optional.

    If this optional does not have a value (i.e. `self.has_value()` evaluates to
    `False`), this operation will raise `tf.errors.InvalidArgumentError` at
    runtime.

    >>> optional = tf.experimental.Optional.from_value(42)
    >>> print(optional.get_value())
    tf.Tensor(42, shape=(), dtype=int32)

    Args:
      name: (Optional.) A name for the created operation.

    Returns:
      The wrapped value.
    """
    @property
    @abc.abstractmethod
    def element_spec(self):
        """The type specification of an element of this optional.

    >>> optional = tf.experimental.Optional.from_value(42)
    >>> print(optional.element_spec)
    tf.TensorSpec(shape=(), dtype=tf.int32, name=None)

    Returns:
      A (nested) structure of `tf.TypeSpec` objects matching the structure of an
      element of this optional, specifying the type of individual components.
    """
    @staticmethod
    def empty(element_spec):
        """Returns an `Optional` that has no value.

    NOTE: This method takes an argument that defines the structure of the value
    that would be contained in the returned `Optional` if it had a value.

    >>> optional = tf.experimental.Optional.empty(
    ...   tf.TensorSpec(shape=(), dtype=tf.int32, name=None))
    >>> print(optional.has_value())
    tf.Tensor(False, shape=(), dtype=bool)

    Args:
      element_spec: A (nested) structure of `tf.TypeSpec` objects matching the
        structure of an element of this optional.

    Returns:
      A `tf.experimental.Optional` with no value.
    """
    @staticmethod
    def from_value(value):
        """Returns a `tf.experimental.Optional` that wraps the given value.

    >>> optional = tf.experimental.Optional.from_value(42)
    >>> print(optional.has_value())
    tf.Tensor(True, shape=(), dtype=bool)
    >>> print(optional.get_value())
    tf.Tensor(42, shape=(), dtype=int32)

    Args:
      value: A value to wrap. The value must be convertible to `tf.Tensor` or
        `tf.CompositeTensor`.

    Returns:
      A `tf.experimental.Optional` that wraps `value`.
    """

class _OptionalImpl(Optional):
    """Concrete implementation of `tf.experimental.Optional`.

  NOTE(mrry): This implementation is kept private, to avoid defining
  `Optional.__init__()` in the public API.
  """
    def __init__(self, variant_tensor, element_spec) -> None: ...
    def has_value(self, name: Incomplete | None = None): ...
    def get_value(self, name: Incomplete | None = None): ...
    @property
    def element_spec(self): ...

class OptionalSpec(type_spec.TypeSpec):
    """Type specification for `tf.experimental.Optional`.

  For instance, `tf.OptionalSpec` can be used to define a tf.function that takes
  `tf.experimental.Optional` as an input argument:

  >>> @tf.function(input_signature=[tf.OptionalSpec(
  ...   tf.TensorSpec(shape=(), dtype=tf.int32, name=None))])
  ... def maybe_square(optional):
  ...   if optional.has_value():
  ...     x = optional.get_value()
  ...     return x * x
  ...   return -1
  >>> optional = tf.experimental.Optional.from_value(5)
  >>> print(maybe_square(optional))
  tf.Tensor(25, shape=(), dtype=int32)

  Attributes:
    element_spec: A (nested) structure of `TypeSpec` objects that represents the
      type specification of the optional element.
  """
    def __init__(self, element_spec) -> None: ...
    @property
    def value_type(self): ...
    @staticmethod
    def from_value(value): ...
