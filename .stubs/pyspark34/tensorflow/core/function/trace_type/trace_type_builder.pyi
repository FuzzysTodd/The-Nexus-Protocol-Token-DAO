from _typeshed import Incomplete
from tensorflow.core.function.trace_type import default_types as default_types, util as util
from tensorflow.python.types import trace as trace
from typing import Any, Callable, Dict, Hashable, Optional

class WeakrefDeletionObserver:
    """An observer for the event of deleting a weakref.

  This allows users of FunctionTraceType to be notified when an instance which
  depends on a weakref becomes invalid by the deletion of the weakref. In
  particular, tf.function caches can use this mechanism to clear the cache of
  keys that are no longer valid.

  We use the observer pattern and not just basic callbacks because the keys
  are typically created before they are used by the cache.
  """
    def __init__(self) -> None: ...
    def add_listener(self, on_delete: Callable[[], None]): ...
    def weakref_deleted(self) -> None: ...
    def __call__(self, _) -> None:
        """Call handler for convenience of use with weakref."""

class InternalTracingContext(trace.TracingContext):
    """Container for variables and flags shared across TraceType generation."""
    def __init__(self, is_legacy_signature: bool = False) -> None: ...
    def alias_global_id(self, global_id: Hashable) -> Hashable: ...
    def add_placeholder(self, alias_id: Hashable, variable) -> None: ...
    def get_placeholder_mapping(self) -> Dict[Hashable, Any]: ...
    def add_handledata(self, spec_id: Hashable, handledata: Any) -> None: ...
    def get_handledata_mapping(self) -> Dict[Hashable, Any]: ...
    @property
    def deletion_observer(self) -> WeakrefDeletionObserver:
        """Returns a functor which invalidates the current key when called."""
    @property
    def is_legacy_signature(self) -> bool:
        """If the value is from a legacy signature representation.

    Legacy signature representations include tf.function.input_signature and
    ConcreteFunction.structured_input_signature.
    """

class InternalPlaceholderContext(trace.PlaceholderContext):
    """Container with mappings shared across TraceTypes for placeholder values."""
    def __init__(self, context_graph: Incomplete | None = None, placeholder_mapping: Incomplete | None = None, handledata_mapping: Incomplete | None = None, unnest_only: bool = False) -> None: ...
    def has_placeholder(self, alias_id: Hashable) -> bool: ...
    def get_placeholder(self, alias_id: Hashable) -> Hashable: ...
    def add_placeholder(self, alias_id: Hashable, placeholder: Hashable) -> None: ...
    def has_handledata(self, spec_id: Hashable) -> bool: ...
    def get_handledata(self, spec_id: Hashable) -> Any: ...
    def update_naming_scope(self, naming_scope: Optional[str]) -> None: ...
    @property
    def naming_scope(self) -> Optional[str]: ...
    @property
    def context_graph(self): ...
    @property
    def unnest_only(self) -> bool: ...

class InternalCastContext(trace.CastContext):
    """Default casting behaviors."""

def from_value(value: Any, context: trace.TracingContext = None) -> trace.TraceType:
    """Returns a TraceType corresponding to the value based on the context.

  Args:
    value: The value to generate a TraceType for.
    context: The TracingContext to be shared during protocol calls.

  Returns:
    A TraceType object representing the given value.
  """
