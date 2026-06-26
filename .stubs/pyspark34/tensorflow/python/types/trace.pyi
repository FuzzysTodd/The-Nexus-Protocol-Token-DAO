import abc
from _typeshed import Incomplete
from tensorflow.python.util.tf_export import tf_export as tf_export
from tensorflow.tools.docs import doc_controls as doc_controls
from typing import Any, Optional, Sequence
from typing_extensions import Protocol

class TraceType(metaclass=abc.ABCMeta):
    """Represents the type of object(s) for tf.function tracing purposes.

  `TraceType` is an abstract class that other classes might inherit from to
  provide information regarding associated class(es) for the purposes of
  tf.function tracing. The typing logic provided through this mechanism will be
  used to make decisions regarding usage of cached concrete functions and
  retracing.

  For example, if we have the following tf.function and classes:
  ```python
  @tf.function
  def get_mixed_flavor(fruit_a, fruit_b):
    return fruit_a.flavor + fruit_b.flavor

  class Fruit:
    flavor = tf.constant([0, 0])

  class Apple(Fruit):
    flavor = tf.constant([1, 2])

  class Mango(Fruit):
    flavor = tf.constant([3, 4])
  ```

  tf.function does not know when to re-use an existing concrete function in
  regards to the `Fruit` class so naively it retraces for every new instance.
  ```python
  get_mixed_flavor(Apple(), Mango()) # Traces a new concrete function
  get_mixed_flavor(Apple(), Mango()) # Traces a new concrete function again
  ```

  However, we, as the designers of the `Fruit` class, know that each subclass
  has a fixed flavor and we can reuse an existing traced concrete function if
  it was the same subclass. Avoiding such unnecessary tracing of concrete
  functions can have significant performance benefits.

  ```python
  class FruitTraceType(tf.types.experimental.TraceType):
    def __init__(self, fruit):
      self.fruit_type = type(fruit)
      self.fruit_value = fruit

    def is_subtype_of(self, other):
       return (type(other) is FruitTraceType and
               self.fruit_type is other.fruit_type)

    def most_specific_common_supertype(self, others):
       return self if all(self == other for other in others) else None

    def placeholder_value(self, placeholder_context=None):
      return self.fruit_value

  class Fruit:

   def __tf_tracing_type__(self, context):
     return FruitTraceType(self)
  ```

  Now if we try calling it again:
  ```python
  get_mixed_flavor(Apple(), Mango()) # Traces a new concrete function
  get_mixed_flavor(Apple(), Mango()) # Re-uses the traced concrete function
  ```
  """
    @abc.abstractmethod
    def is_subtype_of(self, other: TraceType) -> bool:
        """Returns True if `self` is a subtype of `other`.

    For example, `tf.function` uses subtyping for dispatch:
    if `a.is_subtype_of(b)` is True, then an argument of `TraceType`
    `a` can be used as argument to a `ConcreteFunction` traced with an
    a `TraceType` `b`.

    Args:
     other: A TraceType object to be compared against.

    Example:

    ```python
    class Dimension(TraceType):
      def __init__(self, value: Optional[int]):
        self.value = value

      def is_subtype_of(self, other):
        # Either the value is the same or other has a generalized value that
        # can represent any specific ones.
        return (self.value == other.value) or (other.value is None)
    ```
    """
    @abc.abstractmethod
    def most_specific_common_supertype(self, others: Sequence['TraceType']) -> Optional['TraceType']:
        """Returns the most specific supertype of `self` and `others`, if exists.

    The returned `TraceType` is a supertype of `self` and `others`, that is,
    they are all subtypes (see `is_subtype_of`) of it.
    It is also most specific, that is, there it has no subtype that is also
    a common supertype of `self` and `others`.

    If `self` and `others` have no common supertype, this returns `None`.

    Args:
     others: A sequence of TraceTypes.

    Example:
    ```python
     class Dimension(TraceType):
       def __init__(self, value: Optional[int]):
         self.value = value

       def most_specific_common_supertype(self, other):
          # Either the value is the same or other has a generalized value that
          # can represent any specific ones.
          if self.value == other.value:
            return self.value
          else:
            return Dimension(None)
    ```
    """
    @abc.abstractmethod
    def placeholder_value(self, placeholder_context: Incomplete | None = None) -> Any:
        """Creates a placeholder for tracing.

    tf.funcion traces with the placeholder value rather than the actual value.
    For example, a placeholder value can represent multiple different
    actual values. This means that the trace generated with that placeholder
    value is more general and reusable which saves expensive retracing.

    Args:
      placeholder_context: A `PlaceholderContext` container for context
                           information when creating a placeholder value.

    For the `Fruit` example shared above, implementing:

    ```python
    class FruitTraceType:
      def placeholder_value(self, placeholder_context=None):
        return Fruit()
    ```
    instructs tf.function to trace with the `Fruit()` objects
    instead of the actual `Apple()` and `Mango()` objects when it receives a
    call to `get_mixed_flavor(Apple(), Mango())`. For example, Tensor arguments
    are replaced with Tensors of similar shape and dtype, output from
    a tf.Placeholder op.

    More generally, placeholder values are the arguments of a tf.function,
    as seen from the function's body:
    ```python
    @tf.function
    def foo(x):
      # Here `x` is be the placeholder value
      ...

    foo(x) # Here `x` is the actual value
    ```
    """
    @abc.abstractmethod
    def __hash__(self) -> int: ...
    @abc.abstractmethod
    def __eq__(self, other) -> bool: ...

class TracingContext(metaclass=abc.ABCMeta):
    """Contains information scoped to the tracing of multiple objects.

  `TracingContext` is a container class for flags and variables that have
  any kind of influence on the tracing behaviour of the class implementing
  the __tf_tracing_type__. This context will be shared across all
  __tf_tracing_type__ calls while constructing the TraceType for a particular
  set of objects.
  """
class PlaceholderContext:
    """Contains context information for generating placeholders within a scope."""
class CastContext:
    """Contains context info and rules for casting values to a TypeSpec."""

class SupportsTracingProtocol(Protocol):
    """A protocol allowing custom classes to control tf.function retracing."""
    @abc.abstractmethod
    def __tf_tracing_type__(self, context: TracingContext) -> TraceType:
        """Returns the tracing type of this object.

    The tracing type is used to build the signature of a tf.function
    when traced, and to match arguments with existing signatures.
    When a Function object is called, tf.function looks at the tracing type
    of the call arguments. If an existing signature of matching type exists,
    it will be used. Otherwise, a new function is traced, and its signature
    will use the tracing type of the call arguments.

    Args:
      context: a context object created for each function call for tracking
        information about the call arguments as a whole
    Returns:
      The tracing type of this object.
    """
