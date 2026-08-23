from .graph_op import Operation
from _typeshed import Incomplete
from enum import Enum
from nni.nas.evaluator import Evaluator as Evaluator
from nni.nas.mutable import Mutator
from typing import Any, Dict, Iterable, List, Set, Tuple, overload

__all__ = ['Evaluator', 'Model', 'ModelStatus', 'Graph', 'Node', 'Edge', 'Mutation', 'IllegalGraphError', 'MetricData', 'DebugEvaluator']

MetricData = Any

class Model:
    '''
    Represents a neural network model.

    During mutation, one :class:`Model` object is created for each trainable snapshot.
    For example, consider a mutator that insert a node at an edge for each iteration.
    In one iteration, the mutator invokes 4 primitives: add node, remove edge, add edge to head, add edge to tail.
    These 4 primitives operates in one :class:`Model` object.
    When they are all done the model will be set to "frozen" (trainable) status and be submitted to execution engine.
    And then a new iteration starts, and a new :class:`Model` object is created by forking last model.

    Attributes
    ----------
    python_object
        Python object of base model. It will be none when the base model is not available.
    python_class
        Python class that base model is converted from.
    python_init_params
        Initialization parameters of python class.
    status
        See :class:`ModelStatus`.
    root_graph
        The outermost graph which usually takes dataset as input and feeds output to loss function.
    graphs
        All graphs (subgraphs) in this model.
    evaluator
        Model evaluator
    history
        Mutation history.
        ``self`` is directly mutated from ``self.history[-1]``;
        ``self.history[-1]`` is mutated from ``self.history[-2]``, and so on.
        ``self.history[0]`` is the base graph.
    metric
        Training result of the model, or ``None`` if it\'s not yet trained or has failed to train.
    intermediate_metrics
        Intermediate training metrics. If the model is not trained, it\'s an empty list.
    '''
    model_id: Incomplete
    python_object: Incomplete
    python_class: Incomplete
    python_init_params: Incomplete
    status: Incomplete
    graphs: Incomplete
    evaluator: Incomplete
    history: Incomplete
    metric: Incomplete
    intermediate_metrics: Incomplete
    def __init__(self, _internal: bool = False) -> None: ...
    @property
    def root_graph(self) -> Graph: ...
    def fork(self) -> Model:
        """
        Create a new model which has same topology, names, and IDs to current one.

        Can only be invoked on a frozen model.
        The new model will be in `Mutating` state.

        This API is used in mutator base class.
        """
    def get_nodes(self) -> Iterable['Node']:
        """
        Traverse through all the nodes.
        """
    def get_nodes_by_label(self, label: str) -> List['Node']:
        """
        Traverse all the nodes to find the matched node(s) with the given label.
        There could be multiple nodes with the same label. Name space name can uniquely
        identify a graph or node.

        NOTE: the implementation does not support the class abstraction
        """
    def get_nodes_by_type(self, type_name: str) -> List['Node']:
        """
        Traverse all the nodes to find the matched node(s) with the given type.
        """
    def get_node_by_name(self, node_name: str) -> Node | None:
        """
        Traverse all the nodes to find the matched node with the given name.
        """
    def get_node_by_python_name(self, python_name: str) -> Node | None:
        """
        Traverse all the nodes to find the matched node with the given python_name.
        """
    def get_cell_nodes(self) -> List['Node']: ...

class ModelStatus(Enum):
    """
    The status of model.

    A model is created in `Mutating` status.
    When the mutation is done and the model get ready to train, its status becomes `Frozen`.
    When training started, the model's status becomes `Training`.
    If training is successfully ended, model's `metric` attribute get set and its status becomes `Trained`.
    If training failed, the status becomes `Failed`.
    """
    Mutating: str
    Frozen: str
    Training: str
    Trained: str
    Failed: str

class Graph:
    """
    Graph topology.

    This class simply represents the topology, with no semantic meaning.
    All other information like metric, non-graph functions, mutation history, etc should go to :class:`Model`.

    Each graph belongs to and only belongs to one :class:`Model`.

    Attributes
    ----------
    model
        The model containing (and owning) this graph.
    id
        Unique ID in the model.
        If two models have graphs of identical ID, they are semantically the same graph.
        Typically this means one graph is mutated from another, or they are both mutated from one ancestor.
    name
        Mnemonic name of this graph. It should have an one-to-one mapping with ID.
    input_names
        Optional mnemonic names of input parameters.
    output_names
        Optional mnemonic names of output values.
    input_node
        Incoming node.
    output_node
        Output node.
    hidden_nodes
        Hidden nodes
    nodes
        All input/output/hidden nodes.
    edges
        Edges.
    python_name
        The name of torch.nn.Module, should have one-to-one mapping with items in python model.
    """
    model: Incomplete
    id: Incomplete
    name: Incomplete
    python_name: Incomplete
    input_node: Incomplete
    output_node: Incomplete
    hidden_nodes: Incomplete
    edges: Incomplete
    def __init__(self, model: Model, graph_id: int, name: str = ..., _internal: bool = False) -> None: ...
    @property
    def nodes(self) -> List['Node']: ...
    @overload
    def add_node(self, name: str, operation: Operation) -> Node: ...
    @overload
    def add_node(self, name: str, type_name: str, parameters: Dict[str, Any] = ...) -> Node: ...
    @overload
    def insert_node_on_edge(self, edge: Edge, name: str, operation: Operation) -> Node: ...
    @overload
    def insert_node_on_edge(self, edge: Edge, name: str, type_name: str, parameters: Dict[str, Any] = ...) -> Node: ...
    def add_edge(self, head: EdgeEndpoint, tail: EdgeEndpoint) -> Edge: ...
    def del_edge(self, edge: Edge) -> None: ...
    def get_node_by_name(self, name: str) -> Node | None:
        """
        Returns the node which has specified name; or returns `None` if no node has this name.
        """
    def get_node_by_python_name(self, python_name: str) -> Node | None:
        """
        Returns the node which has specified python_name; or returns `None` if no node has this python_name.
        """
    def get_nodes_by_type(self, operation_type: str) -> List['Node']:
        """
        Returns nodes whose operation is specified typed.
        """
    def get_node_by_id(self, node_id: int) -> Node | None:
        """
        Returns the node which has specified name; or returns `None` if no node has this name.
        """
    def get_nodes_by_label(self, label: str) -> List['Node']: ...
    def get_nodes_by_name(self, name: str) -> List['Node']: ...
    def get_nodes_by_python_name(self, python_name: str) -> List['Node']: ...
    def topo_sort(self) -> List['Node']: ...
    def fork(self) -> Graph:
        '''
        Fork the model and returns corresponding graph in new model.
        This shortcut might be helpful because many algorithms only cares about "stem" subgraph instead of whole model.
        '''
    def __eq__(self, other: object) -> bool: ...

class Node:
    '''
    An operation or an opaque subgraph inside a graph.

    Each node belongs to and only belongs to one :class:`Graph`.
    Nodes should never be created with constructor. Use :meth:`Graph.add_node` instead.

    The node itself is for topology only.
    Information of tensor calculation should all go inside ``operation`` attribute.

    TODO: parameter of subgraph (cell)
    It\'s easy to assign parameters on cell node, but it\'s hard to "use" them.
    We need to design a way to reference stored cell parameters in inner node operations.
    e.g. ``self.fc = Linear(self.units)``  <-  how to express ``self.units`` in IR?

    Attributes
    ----------
    graph
        The graph containing this node.
    id
        Unique ID in the model.
        If two models have nodes with same ID, they are semantically the same node.
    name
        Mnemonic name. It should have an one-to-one mapping with ID.
    python_name
        The name of torch.nn.Module, should have one-to-one mapping with items in python model.
    label
        Optional. If two nodes have the same label, they are considered same by the mutator.
    operation
        Operation.
    cell
        Read only shortcut to get the referenced subgraph.
        If this node is not a subgraph (is a primitive operation), accessing ``cell`` will raise an error.
    predecessors
        Predecessor nodes of this node in the graph. This is an optional mutation helper.
    successors
        Successor nodes of this node in the graph. This is an optional mutation helper.
    incoming_edges
        Incoming edges of this node in the graph. This is an optional mutation helper.
    outgoing_edges
        Outgoing edges of this node in the graph. This is an optional mutation helper.
    '''
    graph: Incomplete
    id: Incomplete
    name: Incomplete
    python_name: Incomplete
    operation: Incomplete
    label: Incomplete
    def __init__(self, graph, node_id, name, operation, _internal: bool = False) -> None: ...
    @property
    def predecessors(self) -> List['Node']: ...
    @property
    def successors(self) -> List['Node']: ...
    @property
    def successor_slots(self) -> Set[Tuple['Node', int | None]]: ...
    @property
    def incoming_edges(self) -> List['Edge']: ...
    @property
    def outgoing_edges(self) -> List['Edge']: ...
    @property
    def cell(self) -> Graph: ...
    def update_label(self, label: str | None) -> None: ...
    @overload
    def update_operation(self, operation: Operation) -> None: ...
    @overload
    def update_operation(self, type_name: str, parameters: Dict[str, Any] = ...) -> None: ...
    def remove(self) -> None: ...
    def specialize_cell(self) -> Graph:
        """
        Only available if the operation is a cell.
        Duplicate the cell template and let this node reference to newly created copy.
        """
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...

class Edge:
    '''
    A tensor, or "data flow", between two nodes.

    Example forward code snippet: ::

        a, b, c = split(x)
        p = concat(a, c)
        q = sum(b, p)
        z = relu(q)

    Edges in above snippet: ::

        + head: (split, 0), tail: (concat, 0)  # a in concat
        + head: (split, 2), tail: (concat, 1)  # c in concat
        + head: (split, 1), tail: (sum, -1 or 0)  # b in sum
        + head: (concat, null), tail: (sum, -1 or 1)  # p in sum
        + head: (sum, null), tail: (relu, null)  # q in relu

    Attributes
    ----------
    graph
        Graph.
    head
        Head node.
    tail
        Tail node.
    head_slot
        Index of outputs in head node.
        If the node has only one output, this should be ``null``.
    tail_slot
        Index of inputs in tail node.
        If the node has only one input, this should be ``null``.
        If the node does not care about order, this can be ``-1``.
    '''
    graph: Incomplete
    head: Incomplete
    tail: Incomplete
    head_slot: Incomplete
    tail_slot: Incomplete
    def __init__(self, head: EdgeEndpoint, tail: EdgeEndpoint, _internal: bool = False) -> None: ...
    def remove(self) -> None: ...

class Mutation:
    """
    An execution of mutation, which consists of four parts: a mutator, a list of decisions (choices),
    the model that it comes from, and the model that it becomes.

    In general cases, the mutation logs are not reliable and should not be replayed as the mutators can
    be arbitrarily complex. However, for inline mutations, the labels correspond to mutator labels here,
    this can be useful for metadata visualization and python execution mode.

    Attributes
    ----------
    mutator
        Mutator.
    samples
        Decisions/choices.
    from_
        Model that is comes from.
    to
        Model that it becomes.
    """
    mutator: Incomplete
    samples: Incomplete
    from_: Incomplete
    to: Incomplete
    def __init__(self, mutator: Mutator, samples: List[Any], from_: Model, to: Model) -> None: ...

class IllegalGraphError(ValueError):
    def __init__(self, graph, *args) -> None: ...

class DebugEvaluator(Evaluator):
    def __eq__(self, other) -> bool: ...
