from _typeshed import Incomplete
from collections.abc import Generator
from tensorflow.python.util import object_identity as object_identity

def is_layer(obj):
    """Implicit check for Layer-like objects."""
def has_weights(obj):
    """Implicit check for Layer-like objects."""
def invalidate_recursive_cache(key):
    """Convenience decorator to invalidate the cache when setting attributes."""

class MutationSentinel:
    """Container for tracking whether a property is in a cached state."""
    def mark_as(self, value: bool) -> bool: ...
    @property
    def in_cached_state(self): ...

class AttributeSentinel:
    """Container for managing attribute cache state within a Layer.

  The cache can be invalidated either on an individual basis (for instance when
  an attribute is mutated) or a layer-wide basis (such as when a new dependency
  is added).
  """
    attributes: Incomplete
    always_propagate: Incomplete
    def __init__(self, always_propagate: bool = False) -> None: ...
    def add_parent(self, node: AttributeSentinel) -> None: ...
    def get(self, key: str) -> bool: ...
    def mark_cached(self, key: str) -> None: ...
    def invalidate(self, key: str) -> None: ...
    def invalidate_all(self) -> None: ...

def filter_empty_layer_containers(layer_list) -> Generator[Incomplete, None, None]:
    """Filter out empty Layer-like containers and uniquify."""
