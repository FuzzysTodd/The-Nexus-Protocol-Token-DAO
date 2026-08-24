from _typeshed import Incomplete
from torch.utils.tensorboard._pytorch_graph import NodePy
from typing import List

CLASSTYPE_KIND: str
GETATTR_KIND: str
CAT_KIND: str
LIST_CONSTRUCT_KIND: str
LIST_UNPACK_KIND: str
TUPLE_CONSTRUCT_KIND: str
TUPLE_UNPACK_KIND: str
CONSTANT_KIND: str

def build_module_graph(model, dummy_input): ...
def build_graph(model, dummy_input, verbose: bool = False): ...
def parse_traced_name(module_name): ...

class TorchGraph:
    """
    This class is to extract pytorch model topology graph by tracing
    """
    trace: Incomplete
    bound_model: Incomplete
    def __init__(self, model: Incomplete | None = None, dummy_input: Incomplete | None = None, traced_model: Incomplete | None = None) -> None:
        """
        Parameters
        ----------
        model : pytorch model
            The model user wants to speedup
        dummy_input : pytorch tensor
            The dummy input for ```jit.trace```, users should put it on right device before pass in
        traced_model : torch._C.torch.jit.TopLevelTracedModule
            An alredy traced model, if traced_model is not None, then TorchGraph will build the graph
            based on this traced model and won't trace the model again.
        """

class TorchProtoGraph(TorchGraph):
    """
    Generates model graph for pytorch models in protobuf, this implementation
    is borrowed from pytorch v1.4.0, and fixed following issues:
    https://github.com/pytorch/pytorch/issues/33691
    https://github.com/pytorch/pytorch/issues/33670

    """
    stepstats: Incomplete
    graph_def: Incomplete
    def __init__(self, model, dummy_input, verbose: bool = False) -> None: ...
    def parse(self, graph, trace, args: Incomplete | None = None, omit_useless_nodes: bool = True):
        """This method parses an optimized PyTorch model graph and produces
        a list of nodes and node stats for eventual conversion to TensorBoard
        protobuf format.

        Args:
        graph (PyTorch module): The model graph to be parsed.
        trace (PyTorch JIT TracedModule): The model trace to be parsed.
        args (tuple): input tensor[s] for the model.
        omit_useless_nodes (boolean): Whether to remove nodes from the graph.
        """

class NodePyGroup(NodePy):
    """
    This class is used to represent a graph node which consists of multiple jit traced nodes. In a pytorch trace graph,
    there are multiple nodes are traced for one torch.nn.Module object, we group them together to form a single node to
    represent the torch.nn.Module object. We also group some functional call trace nodes together to form a new node.
    """
    node_cpps: Incomplete
    name: Incomplete
    unique_name: Incomplete
    op_type: Incomplete
    type: Incomplete
    nodes: Incomplete
    auxiliary: Incomplete
    inputs: Incomplete
    outputs: Incomplete
    key_node: Incomplete
    def __init__(self, name, unique_name, node_type, op_type, node_cpps, inputs: Incomplete | None = None, outputs: Incomplete | None = None, key_node: Incomplete | None = None) -> None:
        """
        Parameters:
        -----------
        name: str
            node name, such as `conv1`, `backbone.classifier`
        unique_name: str
            A global unique name for current node. Due to some modules,
            such as relu, may be reused several times, so the scopename
            is not suitable as the global unique identifier, so we add a
            unique_name for each node as the global unique identifier.
            We should use the unique_name to traverset the module graph.
        node_type: str
            `module` or `func`
        op_type: str
            operation type, such as `Conv2d`, `aten::view`
        node_cpps: list of torch._C.Node
            jit trace nodes which are included in this new node
        inputs: list of str
            All the inputs of this node, each element is debugName of one input
        outputs: list of str
            All the outputs of this node, each element is debugName of one output
        key_node: torch._C.Node
            The key node of this NodePyGroup.
        """
    def add_nodes(self, node_cpps) -> None: ...
    def sub_node_names(self): ...

class TorchModuleGraph(TorchGraph):
    """
    Generates model graph, each node is created from single or multiple jit trace nodes.
    """
    name_to_node: Incomplete
    global_count: int
    reused_module: Incomplete
    def __init__(self, model: Incomplete | None = None, dummy_input: Incomplete | None = None, traced_model: Incomplete | None = None) -> None: ...
    unpacked: bool
    def unpack_manually(self) -> None:
        """
        Unpack the tensor tuple or tensor list manually,
        and remove the ListUnpack/TupleUnpack node from
        the graph. Note: this function will change the
        graph structure.
        """
    def find_predecessors(self, unique_name) -> List[str]:
        """
        Find predecessor node of the given node

        Parameters
        ----------
        unique_name : str
            The unique name of the node

        Returns
        -------
        list
            a list of nodes who are the given node's predecessor
        """
    def find_successors(self, unique_name) -> List[str]:
        """
        Find successor nodes of the given node

        Parameters
        ----------
        unique_name : str
            The unique name of the node

        Returns
        -------
        list
            a list of nodes who are the given node's successor
        """
