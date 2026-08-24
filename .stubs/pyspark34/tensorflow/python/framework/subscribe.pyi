from _typeshed import Incomplete
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import array_ops as array_ops, variables as variables

class _ControlOutputCache:
    """Helper class to manage calculating and caching control_outputs in graph."""
    cache: Incomplete
    def __init__(self) -> None: ...
    def calc_control_outputs(self, graph):
        """Returns the map of control_outputs for a given graph.

    Args:
      graph: The graph to parse.

    Returns:
      A map of the control outputs.
    """
    def get_control_outputs(self, op):
        """Return the control outputs for a given op.

    Args:
      op: The op to fetch control outputs for.

    Returns:
      Iterable of control output ops.
    """

def subscribe(tensors, side_effects):
    """Subscribe to a tensor.

  This method will attach side effect graphs to a given set
  of tensors. Set of tensors follows from session.run and supports
  single `Tensor`, `list`, nested `list`, `tuple`, `namedtuple`, or `dict`. It
  returns the tensors in the same passed in structure, but as clones with
  side effects applied. The supplied side effect graphs are specified
  as a constructor function which takes the target tensor and
  constructs a side effect graph and returns a list of ops that should
  be control dependencies on fetching the tensor. It will append
  'subscription' to the name scope of the tensor for every node in
  the side effect graph. These control dependencies are what trigger
  the side effects. Subscribe will construct the additions to your
  graph and return the created identity tensor downstream of the control
  dependencies. Use these tensors as you would normally in the rest of
  your tensorflow code. If a given tensor has already been subscribed or a
  tensor returned by a call to subscribe is passed, the previously created
  identity tensor will be reused and the side effect graphs will be added to
  the existing ones.

  Args:
    tensors: `Tensor` or set of tensors to subscribe to. Set of tensors format
      follows from `Session.run` and supports single `Tensor`, `list`, nested
      `list`, `tuple`, `namedtuple`, or `dict`.
    side_effects: Function(s) that takes a `Tensor`, construct a subgraph, and
      return a nonempty list of control dependencies. This can be a single
      function or list of functions.

  Returns:
    Subscribed tensors, which are identity copies of the passed in tensors
      in the same passed in structure, but the graph has been modified
      such that these are downstream of the control dependencies for
      the side effect graphs. Use these functionally equivalent tensors
      instead of the passed in tensors for further construction or running.
  """
