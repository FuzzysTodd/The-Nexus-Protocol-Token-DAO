import abc
from .graph import Graph as Graph
from .layers import StubDense as StubDense, StubDropout1d as StubDropout1d, StubReLU as StubReLU, get_batch_norm_class as get_batch_norm_class, get_conv_class as get_conv_class, get_dropout_class as get_dropout_class, get_global_avg_pooling_class as get_global_avg_pooling_class, get_pooling_class as get_pooling_class
from .utils import Constant as Constant
from _typeshed import Incomplete
from abc import abstractmethod

class NetworkGenerator(metaclass=abc.ABCMeta):
    """The base class for generating a network.
    It can be used to generate a CNN or Multi-Layer Perceptron.
    Attributes:
        n_output_node: Number of output nodes in the network.
        input_shape: A tuple to represent the input shape.
    """
    n_output_node: Incomplete
    input_shape: Incomplete
    def __init__(self, n_output_node, input_shape) -> None: ...
    @abstractmethod
    def generate(self, model_len, model_width): ...

class CnnGenerator(NetworkGenerator):
    """A class to generate CNN.
    Attributes:
          n_dim: `len(self.input_shape) - 1`
          conv: A class that represents `(n_dim-1)` dimensional convolution.
          dropout: A class that represents `(n_dim-1)` dimensional dropout.
          global_avg_pooling: A class that represents `(n_dim-1)` dimensional Global Average Pooling.
          pooling: A class that represents `(n_dim-1)` dimensional pooling.
          batch_norm: A class that represents `(n_dim-1)` dimensional batch normalization.
    """
    n_dim: Incomplete
    conv: Incomplete
    dropout: Incomplete
    global_avg_pooling: Incomplete
    pooling: Incomplete
    batch_norm: Incomplete
    def __init__(self, n_output_node, input_shape) -> None: ...
    def generate(self, model_len: Incomplete | None = None, model_width: Incomplete | None = None):
        """Generates a CNN.
        Args:
            model_len: An integer. Number of convolutional layers.
            model_width: An integer. Number of filters for the convolutional layers.
        Returns:
            An instance of the class Graph. Represents the neural architecture graph of the generated model.
        """

class MlpGenerator(NetworkGenerator):
    """A class to generate Multi-Layer Perceptron.
    """
    def __init__(self, n_output_node, input_shape) -> None:
        """Initialize the instance.
        Args:
            n_output_node: An integer. Number of output nodes in the network.
            input_shape: A tuple. Input shape of the network. If it is 1D, ensure the value is appended by a comma
                in the tuple.
        """
    def generate(self, model_len: Incomplete | None = None, model_width: Incomplete | None = None):
        """Generates a Multi-Layer Perceptron.
        Args:
            model_len: An integer. Number of hidden layers.
            model_width: An integer or a list of integers of length `model_len`. If it is a list, it represents the
                number of nodes in each hidden layer. If it is an integer, all hidden layers have nodes equal to this
                value.
        Returns:
            An instance of the class Graph. Represents the neural architecture graph of the generated model.
        """
