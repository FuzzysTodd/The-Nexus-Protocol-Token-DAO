from _typeshed import Incomplete
from collections.abc import Generator
from tensorflow.python import pywrap_tfe as pywrap_tfe
from typing import NamedTuple

class TangentInfo(NamedTuple('TangentInfo', [('indices', Incomplete), ('tangents', Incomplete)])):
    """Packed forward accumulator state. The return value of `pack_tangents`."""
    def __new__(cls, indices: Incomplete | None = None, tangents: Incomplete | None = None): ...

def pack_tangents(tensors):
    """Packs forward accumulator state into a TangentInfo tuple.

  Args:
    tensors: A flat list of Tensors to pack forward accumulator state for.

  Returns:
    A tuple of (indices, tangents):
      indices: A sequence of sequences of two-element tuples. Each forward
        accumulator is represented as a sequence of tuples with (primal_index,
        jvp_index). Both integers index into the concatenated `tensors + jvps`
        array.
      tangents: A flat list of Tensors. Best interpreted as a sequence to be
        appended to `tensors`.
  """
def push_forwardprop_state() -> Generator[None, None, None]:
    """Temporarily push or pop transient state for accumulators in the active set.

  Allows an accumulator which is currently processing an operation to
  temporarily reset its state. This is useful when building forwardprop versions
  of functions, where an accumulator will trigger function building and then
  must process captured symbolic tensors while building it. Without pushing and
  popping, accumulators ignore operations executed as a direct result of their
  own jvp computations.

  Yields:
    None (used for its side effect).
  """
