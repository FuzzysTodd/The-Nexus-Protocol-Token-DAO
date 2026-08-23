from .graph_transformer import transform as transform
from .layers import is_layer as is_layer
from .utils import Constant as Constant
from _typeshed import Incomplete
from nni.utils import OptimizeMode as OptimizeMode

def layer_distance(a, b):
    """The distance between two layers."""
def attribute_difference(att_diff):
    """ The attribute distance.
    """
def layers_distance(list_a, list_b):
    """The distance between the layers of two neural networks."""
def skip_connection_distance(a, b):
    """The distance between two skip-connections."""
def skip_connections_distance(list_a, list_b):
    """The distance between the skip-connections of two neural networks."""
def edit_distance(x, y):
    """The distance between two neural networks.
    Args:
        x: An instance of NetworkDescriptor.
        y: An instance of NetworkDescriptor
    Returns:
        The edit-distance between x and y.
    """

class IncrementalGaussianProcess:
    """Gaussian process regressor.
    Attributes:
        alpha: A hyperparameter.
    """
    alpha: float
    def __init__(self) -> None: ...
    @property
    def kernel_matrix(self):
        """ Kernel matric.
        """
    def fit(self, train_x, train_y) -> None:
        """ Fit the regressor with more data.
        Args:
            train_x: A list of NetworkDescriptor.
            train_y: A list of metric values.
        """
    def incremental_fit(self, train_x, train_y):
        """ Incrementally fit the regressor. """
    @property
    def first_fitted(self):
        """ if it is firsr fitted
        """
    def first_fit(self, train_x, train_y):
        """ Fit the regressor for the first time. """
    def predict(self, train_x):
        """Predict the result.
        Args:
            train_x: A list of NetworkDescriptor.
        Returns:
            y_mean: The predicted mean.
            y_std: The predicted standard deviation.
        """

def edit_distance_matrix(train_x, train_y: Incomplete | None = None):
    """Calculate the edit distance.
    Args:
        train_x: A list of neural architectures.
        train_y: A list of neural architectures.
    Returns:
        An edit-distance matrix.
    """
def vector_distance(a, b):
    """The Euclidean distance between two vectors."""
def bourgain_embedding_matrix(distance_matrix):
    """Use Bourgain algorithm to embed the neural architectures based on their edit-distance.
    Args:
        distance_matrix: A matrix of edit-distances.
    Returns:
        A matrix of distances after embedding.
    """

class BayesianOptimizer:
    """ A Bayesian optimizer for neural architectures.
    Attributes:
        searcher: The Searcher which is calling the Bayesian optimizer.
        t_min: The minimum temperature for simulated annealing.
        metric: An instance of the Metric subclasses.
        gpr: A GaussianProcessRegressor for bayesian optimization.
        beta: The beta in acquisition function. (refer to our paper)
        search_tree: The network morphism search tree.
    """
    searcher: Incomplete
    t_min: Incomplete
    optimizemode: Incomplete
    gpr: Incomplete
    beta: Incomplete
    search_tree: Incomplete
    def __init__(self, searcher, t_min, optimizemode, beta: Incomplete | None = None) -> None: ...
    def fit(self, x_queue, y_queue) -> None:
        """ Fit the optimizer with new architectures and performances.
        Args:
            x_queue: A list of NetworkDescriptor.
            y_queue: A list of metric values.
        """
    def generate(self, descriptors):
        """Generate new architecture.
        Args:
            descriptors: All the searched neural architectures.
        Returns:
            graph: An instance of Graph. A morphed neural network with weights.
            father_id: The father node ID in the search tree.
        """
    def acq(self, graph):
        """ estimate the value of generated graph
        """
    def add_child(self, father_id, model_id) -> None:
        """ add child to the search tree
        Arguments:
            father_id {int} -- father id
            model_id {int} -- model id
        """

class Elem:
    """Elements to be sorted according to metric value."""
    father_id: Incomplete
    graph: Incomplete
    metric_value: Incomplete
    def __init__(self, metric_value, father_id, graph) -> None: ...
    def __eq__(self, other): ...
    def __lt__(self, other): ...

class ReverseElem(Elem):
    """Elements to be reversely sorted according to metric value."""
    def __lt__(self, other): ...

def contain(descriptors, target_descriptor):
    """Check if the target descriptor is in the descriptors."""

class SearchTree:
    """The network morphism search tree."""
    root: Incomplete
    adj_list: Incomplete
    def __init__(self) -> None: ...
    def add_child(self, u, v) -> None:
        """ add child to search tree itself.
        Arguments:
            u {int} -- father id
            v {int} --  child id
        """
    def get_dict(self, u: Incomplete | None = None):
        """ A recursive function to return the content of the tree in a dict."""
