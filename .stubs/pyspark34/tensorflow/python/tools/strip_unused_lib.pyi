from tensorflow.core.framework import attr_value_pb2 as attr_value_pb2, graph_pb2 as graph_pb2, node_def_pb2 as node_def_pb2
from tensorflow.python.framework import graph_util as graph_util
from tensorflow.python.platform import gfile as gfile

def strip_unused(input_graph_def, input_node_names, output_node_names, placeholder_type_enum):
    """Removes unused nodes from a GraphDef.

  Args:
    input_graph_def: A graph with nodes we want to prune.
    input_node_names: A list of the nodes we use as inputs.
    output_node_names: A list of the output nodes.
    placeholder_type_enum: The AttrValue enum for the placeholder data type, or
        a list that specifies one value per input node name.

  Returns:
    A `GraphDef` with all unnecessary ops removed.

  Raises:
    ValueError: If any element in `input_node_names` refers to a tensor instead
      of an operation.
    KeyError: If any element in `input_node_names` is not found in the graph.
  """
def strip_unused_from_files(input_graph, input_binary, output_graph, output_binary, input_node_names, output_node_names, placeholder_type_enum):
    """Removes unused nodes from a graph file."""
