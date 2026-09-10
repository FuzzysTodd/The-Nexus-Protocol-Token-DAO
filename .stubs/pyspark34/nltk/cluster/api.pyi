from abc import ABCMeta, abstractmethod
from nltk.probability import DictionaryProbDist as DictionaryProbDist

class ClusterI(metaclass=ABCMeta):
    """
    Interface covering basic clustering functionality.
    """
    @abstractmethod
    def cluster(self, vectors, assign_clusters: bool = False):
        """
        Assigns the vectors to clusters, learning the clustering parameters
        from the data. Returns a cluster identifier for each vector.
        """
    @abstractmethod
    def classify(self, token):
        """
        Classifies the token into a cluster, setting the token's CLUSTER
        parameter to that cluster identifier.
        """
    def likelihood(self, vector, label):
        """
        Returns the likelihood (a float) of the token having the
        corresponding cluster.
        """
    def classification_probdist(self, vector):
        """
        Classifies the token into a cluster, returning
        a probability distribution over the cluster identifiers.
        """
    @abstractmethod
    def num_clusters(self):
        """
        Returns the number of clusters.
        """
    def cluster_names(self):
        """
        Returns the names of the clusters.
        :rtype: list
        """
    def cluster_name(self, index):
        """
        Returns the names of the cluster at index.
        """
