from _typeshed import Incomplete
from tensorflow.python.framework import ops as ops
from tensorflow.python.util import object_identity as object_identity

def is_differentiable(op): ...
def is_iterable(obj):
    """Return true if the object is iterable."""
def concatenate_unique(la, lb):
    """Add all the elements of `lb` to `la` if they are not there already.

  The elements added to `la` maintain ordering with respect to `lb`.

  Args:
    la: List of Python objects.
    lb: List of Python objects.
  Returns:
    `la`: The list `la` with missing elements from `lb`.
  """
def get_tensors(graph):
    """get all the tensors which are input or output of an op in the graph.

  Args:
    graph: a `tf.Graph`.
  Returns:
    A list of `tf.Tensor`.
  Raises:
    TypeError: if graph is not a `tf.Graph`.
  """
def get_unique_graph(tops, check_types: Incomplete | None = None, none_if_empty: bool = False):
    """Return the unique graph used by the all the elements in tops.

  Args:
    tops: iterable of elements to check (usually a list of tf.Operation and/or
      tf.Tensor). Or a tf.Graph.
    check_types: check that the element in tops are of given type(s). If None,
      the types (tf.Operation, tf.Tensor) are used.
    none_if_empty: don't raise an error if tops is an empty list, just return
      None.
  Returns:
    The unique graph used by all the tops.
  Raises:
    TypeError: if tops is not a iterable of tf.Operation.
    ValueError: if the graph is not unique.
  """
def check_graphs(*args) -> None:
    """Check that all the element in args belong to the same graph.

  Args:
    *args: a list of object with a obj.graph property.
  Raises:
    ValueError: if all the elements do not belong to the same graph.
  """
def make_list_of_t(ts, check_graph: bool = True, allow_graph: bool = True, ignore_ops: bool = False):
    """Convert ts to a list of `tf.Tensor`.

  Args:
    ts: can be an iterable of `tf.Tensor`, a `tf.Graph` or a single tensor.
    check_graph: if `True` check if all the tensors belong to the same graph.
    allow_graph: if `False` a `tf.Graph` cannot be converted.
    ignore_ops: if `True`, silently ignore `tf.Operation`.
  Returns:
    A newly created list of `tf.Tensor`.
  Raises:
    TypeError: if `ts` cannot be converted to a list of `tf.Tensor` or,
     if `check_graph` is `True`, if all the ops do not belong to the same graph.
  """
def get_generating_ops(ts):
    """Return all the generating ops of the tensors in `ts`.

  Args:
    ts: a list of `tf.Tensor`
  Returns:
    A list of all the generating `tf.Operation` of the tensors in `ts`.
  Raises:
    TypeError: if `ts` cannot be converted to a list of `tf.Tensor`.
  """
def get_consuming_ops(ts):
    """Return all the consuming ops of the tensors in ts.

  Args:
    ts: a list of `tf.Tensor`
  Returns:
    A list of all the consuming `tf.Operation` of the tensors in `ts`.
  Raises:
    TypeError: if ts cannot be converted to a list of `tf.Tensor`.
  """
def make_list_of_op(tops, check_graph: bool = True, allow_graph: bool = True, ignore_ts: bool = False):
    """Convert ops to a list of `tf.Operation`.

  Args:
    tops: can be an iterable of `tf.Operation`, a `tf.Graph` or a single
      operation.
    check_graph: if `True` check if all the operations belong to the same graph.
    allow_graph: if `False` a `tf.Graph` cannot be converted.
    ignore_ts: if True, silently ignore `tf.Tensor`.
  Returns:
    A newly created list of `tf.Operation`.
  Raises:
    TypeError: if tops cannot be converted to a list of `tf.Operation` or,
     if `check_graph` is `True`, if all the ops do not belong to the
     same graph.
  """
def get_backward_walk_ops(seed_ops, inclusive: bool = True, within_ops: Incomplete | None = None, within_ops_fn: Incomplete | None = None, stop_at_ts=(), control_inputs: bool = False, only_differentiable: bool = False):
    """Do a backward graph walk and return all the visited ops.

  Args:
    seed_ops: an iterable of operations from which the backward graph
      walk starts. If a list of tensors is given instead, the seed_ops are set
      to be the generators of those tensors.
    inclusive: if True the given seed_ops are also part of the resulting set.
    within_ops: an iterable of `tf.Operation` within which the search is
      restricted. If `within_ops` is `None`, the search is performed within
      the whole graph.
    within_ops_fn: if provided, a function on ops that should return True iff
      the op is within the graph traversal. This can be used along within_ops,
      in which case an op is within if it is also in within_ops.
    stop_at_ts: an iterable of tensors at which the graph walk stops.
    control_inputs: if True, control inputs will be used while moving backward.
    only_differentiable: if True, only traverse ops which are differentiable.
      This includes natively differentiable ops, or ops with custom gradients.
  Returns:
    A Python set of all the `tf.Operation` behind `seed_ops`.
  Raises:
    TypeError: if `seed_ops` or `within_ops` cannot be converted to a list of
      `tf.Operation`.
  """

class UnliftableError(Exception):
    """Raised if a Tensor cannot be lifted from the graph."""
    ag_pass_through: bool

def graph_inputs(op): ...
def show_path(from_op, tensors, sources):
    '''Find one path from `from_op` to any of `tensors`, ignoring `sources`.

  Args:
    from_op: A `tf.Operation`.
    tensors: A `tf.Operation`, a `tf.Tensor`, or a list thereof.
    sources: A list of `tf.Tensor`.

  Returns:
    A python string containing the path, or "??" if none is found.
  '''
def map_subgraph(init_tensor, sources, disallowed_placeholders, visited_ops, op_outputs, add_sources):
    """Walk a Graph and capture the subgraph between init_tensor and sources.

  Note: This function mutates visited_ops and op_outputs.

  Args:
    init_tensor:  A Tensor or Operation where the subgraph terminates.
    sources:  A set of Tensors where subgraph extraction should stop.
    disallowed_placeholders: An optional set of ops which may not appear in the
      lifted graph. Defaults to all placeholders.
    visited_ops: A set of operations which were visited in a prior pass.
    op_outputs: A defaultdict containing the outputs of an op which are to be
      copied into the new subgraph.
    add_sources: A boolean indicating whether placeholders which are not in
      sources should be allowed.

  Returns:
    The set of placeholders upon which init_tensor depends and are not in
    sources.

  Raises:
    UnliftableError: if init_tensor depends on a placeholder which is not in
      sources and add_sources is False.
  """
