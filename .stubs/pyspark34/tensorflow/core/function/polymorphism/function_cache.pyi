from tensorflow.core.function import trace_type as trace_type
from tensorflow.core.function.polymorphism import function_type as function_type_lib, type_dispatch as type_dispatch
from typing import Any, NamedTuple, Optional

DELETE_WITH_WEAKREF: bool

class FunctionContext(NamedTuple):
    """Contains information regarding tf.function execution context."""
    context: Any

class FunctionCache:
    """A container for managing concrete functions."""
    def __init__(self) -> None: ...
    def lookup(self, context: FunctionContext, function_type: function_type_lib.FunctionType) -> Optional[Any]:
        """Looks up a concrete function based on the context and type."""
    def delete(self, context: FunctionContext, function_type: function_type_lib.FunctionType) -> bool:
        """Deletes a concrete function given the context and type."""
    def add(self, context: FunctionContext, function_type: function_type_lib.FunctionType, deletion_observer: trace_type.WeakrefDeletionObserver, concrete_fn: Any):
        """Adds a new concrete function alongside its key.

    Args:
      context: A FunctionContext representing the current context.
      function_type: A FunctionType representing concrete_fn signature.
      deletion_observer: A WeakrefDeletionObserver for the concrete_fn validity.
      concrete_fn: The concrete function to be added to the cache.
    """
    def generalize(self, context: FunctionContext, function_type: function_type_lib.FunctionType) -> function_type_lib.FunctionType:
        """Try to generalize a FunctionType within a FunctionContext."""
    def clear(self) -> None:
        """Removes all concrete functions from the cache."""
    def values(self):
        """Returns a list of all `ConcreteFunction` instances held by this cache."""
