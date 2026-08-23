import abc
from _typeshed import Incomplete
from abc import abstractmethod
from nltk.cluster.api import ClusterI as ClusterI

class VectorSpaceClusterer(ClusterI, metaclass=abc.ABCMeta):
    """
    Abstract clusterer which takes tokens and maps them into a vector space.
    Optionally performs singular value decomposition to reduce the
    dimensionality.
    """
    def __init__(self, normalise: bool = False, svd_dimensions: Incomplete | None = None) -> None:
        """
        :param normalise:       should vectors be normalised to length 1
        :type normalise:        boolean
        :param svd_dimensions:  number of dimensions to use in reducing vector
                                dimensionsionality with SVD
        :type svd_dimensions:   int
        """
    def cluster(self, vectors, assign_clusters: bool = False, trace: bool = False): ...
    @abstractmethod
    def cluster_vectorspace(self, vectors, trace):
        """
        Finds the clusters using the given set of vectors.
        """
    def classify(self, vector): ...
    @abstractmethod
    def classify_vectorspace(self, vector):
        """
        Returns the index of the appropriate cluster for the vector.
        """
    def likelihood(self, vector, label): ...
    def likelihood_vectorspace(self, vector, cluster):
        """
        Returns the likelihood of the vector belonging to the cluster.
        """
    def vector(self, vector):
        """
        Returns the vector after normalisation and dimensionality reduction
        """

def euclidean_distance(u, v):
    """
    Returns the euclidean distance between vectors u and v. This is equivalent
    to the length of the vector (u - v).
    """
def cosine_distance(u, v):
    """
    Returns 1 minus the cosine of the angle between vectors v and u. This is
    equal to ``1 - (u.v / |u||v|)``.
    """

class _DendrogramNode:
    """Tree node of a dendrogram."""
    def __init__(self, value, *children) -> None: ...
    def leaves(self, values: bool = True): ...
    def groups(self, n): ...
    def __lt__(self, comparator): ...

class Dendrogram:
    """
    Represents a dendrogram, a tree with a specified branching order.  This
    must be initialised with the leaf items, then iteratively call merge for
    each branch. This class constructs a tree representing the order of calls
    to the merge function.
    """
    def __init__(self, items=[]) -> None:
        """
        :param  items: the items at the leaves of the dendrogram
        :type   items: sequence of (any)
        """
    def merge(self, *indices) -> None:
        """
        Merges nodes at given indices in the dendrogram. The nodes will be
        combined which then replaces the first node specified. All other nodes
        involved in the merge will be removed.

        :param  indices: indices of the items to merge (at least two)
        :type   indices: seq of int
        """
    def groups(self, n):
        """
        Finds the n-groups of items (leaves) reachable from a cut at depth n.
        :param  n: number of groups
        :type   n: int
        """
    def show(self, leaf_labels=[]):
        """
        Print the dendrogram in ASCII art to standard out.

        :param leaf_labels: an optional list of strings to use for labeling the
                            leaves
        :type leaf_labels: list
        """
