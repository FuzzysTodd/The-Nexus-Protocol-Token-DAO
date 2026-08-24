import dataclasses
from tensorflow.python.eager import context as context
from tensorflow.python.framework import ops as ops, type_spec as type_spec
from tensorflow.python.types import core as core
from tensorflow.python.util import nest as nest
from typing import Any, Callable, Hashable, Mapping

@dataclasses.dataclass(frozen=True)
class CaptureContainer:
    """A container for both by-reference and by-value captures.

  external: Used to record the tensor external to the func_graph.
     For by-value captures, it would be the original tensor.
     For by-reference captures, it would be the lambda function, which will be
     called later to get the capture's runtime value.
  internal: An internal placeholder for the capture, or a constant tensor.
    The external value of the capture will be fed to this internal placeholder
    when executing the func_graph as a side input.
  idf: A Hashable identifier for the capture.
  is_by_ref: A bool indicates if the capture is call by reference or value.
    This flag will determine how `CaptureContainer.internal` is used.
  """
    external: Any
    internal: core.Tensor
    idf: Hashable
    is_by_ref: bool = ...
    def __init__(self, external, internal, idf, is_by_ref) -> None: ...

class FunctionCaptures:
    """A container for all capture usages within FuncGraph."""
    def __init__(self) -> None: ...
    def capture_by_val(self, value: Any, idf: Hashable = None):
        """Create a by-value capture if not exists."""
    def capture_by_ref(self, lam: Callable[[], Any], idf: Hashable = None):
        """Create a by-referece capture if not exists."""
    def merge_by_ref_with(self, other: FunctionCaptures):
        """Add by-ref captures from `other` to `self` if not exist."""
    def get_by_ref_snapshot(self) -> Mapping[Hashable, Any]:
        """Get a snapshot of current values of by-ref captures."""
    @property
    def by_ref_captures(self): ...
    @property
    def by_val_captures(self): ...
