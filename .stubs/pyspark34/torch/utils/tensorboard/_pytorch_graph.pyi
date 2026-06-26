from ._proto_graph import node_proto as node_proto
from _typeshed import Incomplete

methods_OP: Incomplete
methods_IO: Incomplete
GETATTR_KIND: str
CLASSTYPE_KIND: str

class NodeBase:
    debugName: Incomplete
    inputs: Incomplete
    tensor_size: Incomplete
    kind: Incomplete
    attributes: Incomplete
    scope: Incomplete
    def __init__(self, debugName: Incomplete | None = None, inputs: Incomplete | None = None, scope: Incomplete | None = None, tensor_size: Incomplete | None = None, op_type: str = 'UnSpecified', attributes: str = '') -> None: ...

class NodePy(NodeBase):
    inputs: Incomplete
    def __init__(self, node_cpp, valid_methods) -> None: ...

class NodePyIO(NodePy):
    tensor_size: Incomplete
    kind: str
    input_or_output: Incomplete
    def __init__(self, node_cpp, input_or_output: Incomplete | None = None) -> None: ...

class NodePyOP(NodePy):
    attributes: Incomplete
    kind: Incomplete
    def __init__(self, node_cpp) -> None: ...

class GraphPy:
    """Helper class to convert torch.nn.Module to GraphDef proto and visualization
    with TensorBoard.

    GraphDef generation operates in two passes:

    In the first pass, all nodes are read and saved to two lists.
    One list is for input/output nodes (nodes_io), which only have inbound
    or outbound connections, but not both. Another list is for internal
    operator nodes (nodes_op). The first pass also saves all scope name
    appeared in the nodes in scope_name_appeared list for later processing.

    In the second pass, scope names are fully applied to all nodes.
    debugNameToScopedName is a mapping from a node's ID to its fully qualified
    scope name. e.g. Net1/Linear[0]/1. Unfortunately torch.jit doesn't have
    totally correct scope output, so this is nontrivial. The function
    populate_namespace_from_OP_to_IO and find_common_root are used to
    assign scope name to a node based on the connection between nodes
    in a heuristic kind of way. Bookkeeping is done with shallowest_scope_name
    and scope_name_appeared.
    """
    nodes_op: Incomplete
    nodes_io: Incomplete
    unique_name_to_scoped_name: Incomplete
    shallowest_scope_name: str
    scope_name_appeared: Incomplete
    def __init__(self) -> None: ...
    def append(self, x) -> None: ...
    def printall(self) -> None: ...
    def find_common_root(self) -> None: ...
    def populate_namespace_from_OP_to_IO(self) -> None: ...
    def to_proto(self):
        """
        Converts graph representation of GraphPy object to TensorBoard
        required format.
        """

def parse(graph, trace, args: Incomplete | None = None, omit_useless_nodes: bool = True):
    """This method parses an optimized PyTorch model graph and produces
    a list of nodes and node stats for eventual conversion to TensorBoard
    protobuf format.

    Args:
      graph (PyTorch module): The model graph to be parsed.
      trace (PyTorch JIT TracedModule): The model trace to be parsed.
      args (tuple): input tensor[s] for the model.
      omit_useless_nodes (boolean): Whether to remove nodes from the graph.
    """
def graph(model, args, verbose: bool = False, use_strict_trace: bool = True):
    """
    This method processes a PyTorch model and produces a `GraphDef` proto
    that can be logged to TensorBoard.

    Args:
      model (PyTorch module): The model to be parsed.
      args (tuple): input tensor[s] for the model.
      verbose (bool): Whether to print out verbose information while
        processing.
      use_strict_trace (bool): Whether to pass keyword argument `strict` to
        `torch.jit.trace`. Pass False when you want the tracer to
        record your mutable container types (list, dict)
    """
