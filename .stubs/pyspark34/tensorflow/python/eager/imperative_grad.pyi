from _typeshed import Incomplete
from tensorflow.python import pywrap_tfe as pywrap_tfe
from tensorflow.python.ops.unconnected_gradients import UnconnectedGradients as UnconnectedGradients
from tensorflow.python.util import compat as compat
from typing import NamedTuple

class VSpace(NamedTuple):
    aggregate_fn: Incomplete
    num_elements_fn: Incomplete
    zeros_fn: Incomplete
    ones_fn: Incomplete
    zeros_like_fn: Incomplete
    ones_like_fn: Incomplete
    graph_shape_fn: Incomplete

def imperative_grad(tape, target, sources, output_gradients: Incomplete | None = None, sources_raw: Incomplete | None = None, unconnected_gradients=...):
    """Computes gradients from the imperatively defined tape on top of the stack.

  Works by filtering the tape, computing how many downstream usages are of each
  tensor and entry, and repeatedly applying backward functions until we have
  gradients for all sources.

  Args:
   tape: the gradient tape which stores the trace.
   target: either a Tensor or list of Tensors to be differentiated.
   sources: list of Tensors for which we want gradients
   output_gradients: if not None, a list of gradient provided for each Target,
    or None if we are to use the target's computed downstream gradient.
   sources_raw: if not None, a list of the source python objects from which the
    sources were generated. Should have the same length as sources. Only needs
    to be populated if unconnected_gradients is 'zero'.
   unconnected_gradients: determines the value returned if the target and
    sources are unconnected. When 'none' the value returned is None wheras when
    'zero' a zero tensor in the same shape as the sources is returned.

  Returns:
   the gradient wrt each of the sources.

  Raises:
    ValueError: if the arguments are invalid.
    RuntimeError: if something goes wrong.
  """
