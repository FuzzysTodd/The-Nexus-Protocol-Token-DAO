from _typeshed import Incomplete
from tensorflow.core.framework import graph_pb2 as graph_pb2, node_def_pb2 as node_def_pb2
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.util import deprecation as deprecation, lazy_loader as lazy_loader
from tensorflow.python.util.tf_export import tf_export as tf_export

convert_to_constants: Incomplete

def must_run_on_cpu(node, pin_variables_on_cpu: bool = False):
    """Returns True if the given node_def must run on CPU, otherwise False.

  Args:
    node: The node to be assigned to a device. Could be either an ops.Operation
      or NodeDef.
    pin_variables_on_cpu: If True, this function will return False if node_def
      represents a variable-related op.

  Returns:
    True if the given node must run on CPU, otherwise False.
  """
def extract_sub_graph(graph_def, dest_nodes):
    """Extract the subgraph that can reach any of the nodes in 'dest_nodes'.

  Args:
    graph_def: A graph_pb2.GraphDef proto.
    dest_nodes: An iterable of strings specifying the destination node names.
  Returns:
    The GraphDef of the sub-graph.

  Raises:
    TypeError: If 'graph_def' is not a graph_pb2.GraphDef proto.
  """
def tensor_shape_from_node_def_name(graph, input_name):
    """Convenience function to get a shape from a NodeDef's input string."""
def convert_variables_to_constants(sess, input_graph_def, output_node_names, variable_names_whitelist: Incomplete | None = None, variable_names_blacklist: Incomplete | None = None):
    """Replaces all the variables in a graph with constants of the same values.

  If you have a trained graph containing Variable ops, it can be convenient to
  convert them all to Const ops holding the same values. This makes it possible
  to describe the network fully with a single GraphDef file, and allows the
  removal of a lot of ops related to loading and saving the variables.

  Args:
    sess: Active TensorFlow session containing the variables.
    input_graph_def: GraphDef object holding the network.
    output_node_names: List of name strings for the result nodes of the graph.
    variable_names_whitelist: The set of variable names to convert (by default,
                              all variables are converted).
    variable_names_blacklist: The set of variable names to omit converting
                              to constants.

  Returns:
    GraphDef containing a simplified version of the original.

  Raises:
    RuntimeError: if a DT_RESOURCE op is found whose ancestor Variables are both
      denylisted AND whitelisted for freezing.
  """
def remove_training_nodes(input_graph, protected_nodes: Incomplete | None = None):
    """Prunes out nodes that aren't needed for inference.

  There are nodes like Identity and CheckNumerics that are only useful
  during training, and can be removed in graphs that will be used for
  nothing but inference. Here we identify and remove them, returning an
  equivalent graph. To be specific, CheckNumerics nodes are always removed, and
  Identity nodes that aren't involved in control edges are spliced out so that
  their input and outputs are directly connected.

  Args:
    input_graph: Model to analyze and prune.
    protected_nodes: An optional list of names of nodes to be kept
      unconditionally. This is for example useful to preserve Identity output
      nodes.

  Returns:
    A list of nodes with the unnecessary ones removed.
  """
def graph_defs_equal(graph_def_1: graph_pb2.GraphDef, graph_def_2: graph_pb2.GraphDef, treat_nan_as_equal: bool = False) -> bool:
    """Returns True iff the graph def arguments are structurally equivalent.

  The notion of equivalence encoded here checks that the set of NodeDefs in
  the GraphDef's function library and main graph body are identical.
  Additionally, it checks that the functions in the function library are equal
  as sets.

  Example usage:

  ```
  with tf.Graph().as_default() as g1:
    tf.constant(1)

  with tf.Graph().as_default() as g2:
    tf.constant(2)

  with tf.Graph().as_default() as g3:
    tf.constant(1)

  assert tf.__internal__.graph_util.graph_defs_equal(g1.as_graph_def(),
                                                     g3.as_graph_def())

  assert not tf.__internal__.graph_util.graph_defs_equal(g1.as_graph_def(),
                                                         g2.as_graph_def())
  ```

  Args:
    graph_def_1: Instance of `graph_pb2.GraphDef` to compare.
    graph_def_2: Instance of `graph_pb2.GraphDef` to compare.
    treat_nan_as_equal: Boolean indicating whether or not to treat nan
      floating-point values as equal. This is crucial for any equivalence
      relation defined over GraphDefs, to ensure symmetry.

  Returns:
    Boolean indicating structural equivalence as described above.

  Raises:
    TypeError: If either of the GraphDefs are not instances of
      `graph_pb2.GraphDef`.
  """
