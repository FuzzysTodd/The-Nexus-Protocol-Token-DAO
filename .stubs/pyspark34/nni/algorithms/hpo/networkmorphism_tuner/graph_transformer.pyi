from .graph import NetworkDescriptor as NetworkDescriptor
from .layers import StubDense as StubDense, StubReLU as StubReLU, get_batch_norm_class as get_batch_norm_class, get_conv_class as get_conv_class, get_dropout_class as get_dropout_class, get_pooling_class as get_pooling_class, is_layer as is_layer
from .utils import Constant as Constant

def to_wider_graph(graph):
    """ wider graph
    """
def to_skip_connection_graph(graph):
    """ skip connection graph
    """
def create_new_layer(layer, n_dim):
    """ create  new layer for the graph
    """
def to_deeper_graph(graph):
    """ deeper graph
    """
def legal_graph(graph):
    """judge if a graph is legal or not.
    """
def transform(graph):
    """core transform function for graph.
    """
