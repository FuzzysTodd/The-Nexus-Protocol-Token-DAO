import torch
from .layer_transformer import add_noise as add_noise, init_bn_weight as init_bn_weight, init_conv_weight as init_conv_weight, init_dense_weight as init_dense_weight, wider_bn as wider_bn, wider_next_conv as wider_next_conv, wider_next_dense as wider_next_dense, wider_pre_conv as wider_pre_conv, wider_pre_dense as wider_pre_dense
from .layers import StubAdd as StubAdd, StubConcatenate as StubConcatenate, StubReLU as StubReLU, get_batch_norm_class as get_batch_norm_class, get_conv_class as get_conv_class, is_layer as is_layer, layer_description_builder as layer_description_builder, layer_description_extractor as layer_description_extractor, layer_width as layer_width, set_keras_weight_to_stub as set_keras_weight_to_stub, set_stub_weight_to_keras as set_stub_weight_to_keras, set_stub_weight_to_torch as set_stub_weight_to_torch, set_torch_weight_to_stub as set_torch_weight_to_stub, to_real_keras_layer as to_real_keras_layer
from .utils import Constant as Constant
from _typeshed import Incomplete

class NetworkDescriptor:
    """A class describing the neural architecture for neural network kernel.
    It only record the width of convolutional and dense layers, and the skip-connection types and positions.
    """
    CONCAT_CONNECT: str
    ADD_CONNECT: str
    skip_connections: Incomplete
    layers: Incomplete
    def __init__(self) -> None: ...
    @property
    def n_layers(self): ...
    def add_skip_connection(self, u, v, connection_type) -> None:
        """ Add a skip-connection to the descriptor.
        Args:
            u: Number of convolutional layers before the starting point.
            v: Number of convolutional layers before the ending point.
            connection_type: Must be either CONCAT_CONNECT or ADD_CONNECT.
        """
    def to_json(self):
        """ NetworkDescriptor to json representation
        """
    def add_layer(self, layer) -> None:
        """ add one layer
        """

class Node:
    """A class for intermediate output tensor (node) in the Graph.
    Attributes:
        shape: A tuple describing the shape of the tensor.
    """
    shape: Incomplete
    def __init__(self, shape) -> None: ...

class Graph:
    """A class representing the neural architecture graph of a model.
    Graph extracts the neural architecture graph from a model.
    Each node in the graph is a intermediate tensor between layers.
    Each layer is an edge in the graph.
    Notably, multiple edges may refer to the same layer.
    (e.g. Add layer is adding two tensor into one tensor. So it is related to two edges.)
    Attributes:
        weighted: A boolean of whether the weights and biases in the neural network
            should be included in the graph.
        input_shape: A tuple of integers, which does not include the batch axis.
        node_list: A list of integers. The indices of the list are the identifiers.
        layer_list: A list of stub layers. The indices of the list are the identifiers.
        node_to_id: A dict instance mapping from node integers to their identifiers.
        layer_to_id: A dict instance mapping from stub layers to their identifiers.
        layer_id_to_input_node_ids: A dict instance mapping from layer identifiers
            to their input nodes identifiers.
        layer_id_to_output_node_ids: A dict instance mapping from layer identifiers
            to their output nodes identifiers.
        adj_list: A two dimensional list. The adjacency list of the graph. The first dimension is
            identified by tensor identifiers. In each edge list, the elements are two-element tuples
            of (tensor identifier, layer identifier).
        reverse_adj_list: A reverse adjacent list in the same format as adj_list.
        operation_history: A list saving all the network morphism operations.
        vis: A dictionary of temporary storage for whether an local operation has been done
            during the network morphism.
    """
    input_shape: Incomplete
    weighted: Incomplete
    node_list: Incomplete
    layer_list: Incomplete
    node_to_id: Incomplete
    layer_to_id: Incomplete
    layer_id_to_input_node_ids: Incomplete
    layer_id_to_output_node_ids: Incomplete
    adj_list: Incomplete
    reverse_adj_list: Incomplete
    operation_history: Incomplete
    n_dim: Incomplete
    conv: Incomplete
    batch_norm: Incomplete
    vis: Incomplete
    def __init__(self, input_shape, weighted: bool = True) -> None:
        """Initializer for Graph.
        """
    def add_layer(self, layer, input_node_id):
        """Add a layer to the Graph.
        Args:
            layer: An instance of the subclasses of StubLayer in layers.py.
            input_node_id: An integer. The ID of the input node of the layer.
        Returns:
            output_node_id: An integer. The ID of the output node of the layer.
        """
    def clear_operation_history(self) -> None: ...
    @property
    def n_nodes(self):
        """Return the number of nodes in the model."""
    @property
    def n_layers(self):
        """Return the number of layers in the model."""
    @property
    def topological_order(self):
        """Return the topological order of the node IDs from the input node to the output node."""
    def to_deeper_model(self, target_id, new_layer) -> None:
        """Insert a relu-conv-bn block after the target block.
        Args:
            target_id: A convolutional layer ID. The new block should be inserted after the block.
            new_layer: An instance of StubLayer subclasses.
        """
    def to_wider_model(self, pre_layer_id, n_add) -> None:
        """Widen the last dimension of the output of the pre_layer.
        Args:
            pre_layer_id: The ID of a convolutional layer or dense layer.
            n_add: The number of dimensions to add.
        """
    def to_add_skip_model(self, start_id, end_id) -> None:
        """Add a weighted add skip-connection from after start node to end node.
        Args:
            start_id: The convolutional layer ID, after which to start the skip-connection.
            end_id: The convolutional layer ID, after which to end the skip-connection.
        """
    def to_concat_skip_model(self, start_id, end_id) -> None:
        """Add a weighted add concatenate connection from after start node to end node.
        Args:
            start_id: The convolutional layer ID, after which to start the skip-connection.
            end_id: The convolutional layer ID, after which to end the skip-connection.
        """
    def extract_descriptor(self):
        """Extract the the description of the Graph as an instance of NetworkDescriptor."""
    def clear_weights(self) -> None:
        """ clear weights of the graph
        """
    def produce_torch_model(self):
        """Build a new Torch model based on the current graph."""
    def produce_keras_model(self):
        """Build a new keras model based on the current graph."""
    def produce_onnx_model(self):
        """Build a new ONNX model based on the current graph."""
    def parsing_onnx_model(self, onnx_model):
        """to do in the future to use the onnx model
        """
    def produce_json_model(self):
        """Build a new Json model based on the current graph."""
    @classmethod
    def parsing_json_model(cls, json_model):
        """build a graph from json
        """
    def get_main_chain_layers(self):
        """Return a list of layer IDs in the main chain."""
    def deep_layer_ids(self): ...
    def wide_layer_ids(self): ...
    def skip_connection_layer_ids(self): ...
    def size(self): ...
    def get_main_chain(self):
        """Returns the main chain node ID list."""

class TorchModel(torch.nn.Module):
    """A neural network class using pytorch constructed from an instance of Graph."""
    graph: Incomplete
    layers: Incomplete
    def __init__(self, graph) -> None: ...
    def forward(self, input_tensor): ...
    def set_weight_to_graph(self) -> None: ...

class KerasModel:
    graph: Incomplete
    layers: Incomplete
    model: Incomplete
    def __init__(self, graph) -> None: ...
    def set_weight_to_graph(self) -> None: ...

class ONNXModel:
    def __init__(self, graph) -> None: ...

class JSONModel:
    data: Incomplete
    def __init__(self, graph) -> None: ...

def graph_to_onnx(graph, onnx_model_path): ...
def onnx_to_graph(onnx_model, input_shape): ...
def graph_to_json(graph, json_model_path): ...
def json_to_graph(json_model: str): ...
