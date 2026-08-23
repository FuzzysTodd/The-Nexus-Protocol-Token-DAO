from _typeshed import Incomplete
from tensorflow.python.framework import func_graph as func_graph, ops as ops
from tensorflow.python.ops import array_ops as array_ops, op_selector as op_selector, resource_variable_ops as resource_variable_ops
from tensorflow.python.util import compat as compat, object_identity as object_identity
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import NamedTuple

UnliftableError = op_selector.UnliftableError

class _InputMutation(NamedTuple):
    copied_op: Incomplete
    input_index: Incomplete
    old_graph_tensor: Incomplete

class _ControlMutation(NamedTuple):
    copied_op: Incomplete
    old_graph_op: Incomplete

def lift_to_graph(tensors, graph, sources: Incomplete | None = None, disallowed_placeholders: Incomplete | None = None, add_sources: bool = False, handle_captures: bool = False, base_graph: Incomplete | None = None, op_map: Incomplete | None = None):
    """Copies the tensor and all its inputs recursively to the outer graph.

  Args:
    tensors: The Tensors to lift.
    graph: The graph to lift to.
    sources: Optional sequence of nodes to start from. If omitted the whole
      subgraph which feeds into `init_tensor` is lifted.
    disallowed_placeholders: An optional set of ops which may not appear in the
      lifted graph. Defaults to all placeholders.
    add_sources: A boolean indicating whether placeholders which are not in
      sources should be allowed.
    handle_captures: A boolean indicating whether to re-capture s in the new
      graph or simply create a vanilla placeholder.
    base_graph: The graph from which to lift ops. This will be inferred if not
      specified.
    op_map: A map contains all the existing nodes that have been lifted to the
      destination graph, so they won't be lifted and copied again.

  Returns:
    A mapping from ops in the current default graph to ops in `graph`.

  Raises:
    UnliftableError: If a placeholder blocks lifting.
  """
