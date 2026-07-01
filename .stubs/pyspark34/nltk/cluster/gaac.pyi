from _typeshed import Incomplete
from nltk.cluster.util import Dendrogram as Dendrogram, VectorSpaceClusterer as VectorSpaceClusterer, cosine_distance as cosine_distance

class GAAClusterer(VectorSpaceClusterer):
    """
    The Group Average Agglomerative starts with each of the N vectors as singleton
    clusters. It then iteratively merges pairs of clusters which have the
    closest centroids.  This continues until there is only one cluster. The
    order of merges gives rise to a dendrogram: a tree with the earlier merges
    lower than later merges. The membership of a given number of clusters c, 1
    <= c <= N, can be found by cutting the dendrogram at depth c.

    This clusterer uses the cosine similarity metric only, which allows for
    efficient speed-up in the clustering process.
    """
    def __init__(self, num_clusters: int = 1, normalise: bool = True, svd_dimensions: Incomplete | None = None) -> None: ...
    def cluster(self, vectors, assign_clusters: bool = False, trace: bool = False): ...
    def cluster_vectorspace(self, vectors, trace: bool = False) -> None: ...
    def update_clusters(self, num_clusters) -> None: ...
    def classify_vectorspace(self, vector): ...
    def dendrogram(self):
        """
        :return: The dendrogram representing the current clustering
        :rtype:  Dendrogram
        """
    def num_clusters(self): ...

def demo() -> None:
    """
    Non-interactive demonstration of the clusterers with simple 2-D data.
    """
