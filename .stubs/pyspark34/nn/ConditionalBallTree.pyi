from _typeshed import Incomplete

basestring = str

class ConditionalBallTree:
    def __init__(self, keys, values, labels, leafSize, java_obj: Incomplete | None = None) -> None:
        """
        Create a conditional ball tree.
        :param keys: 2D array representing the data, shape: n_points x n_features
        :param values: 1D array
        :param labels: 1D array
        :param leafSize: int
        """
    def findMaximumInnerProducts(self, queryPoint, conditioner, k):
        """
        Find the best match to the queryPoint given the conditioner and k from self.
        :param queryPoint: array vector to use to query for NNs
        :param conditioner: set of labels that will subset or condition the NN query
        :param k: int representing the maximum number of neighbors to return
        :return: array of tuples representing the index of the match and its distance
        """
    def save(self, filename) -> None: ...
    @staticmethod
    def load(filename): ...
