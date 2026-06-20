from _typeshed import Incomplete
from nltk.cluster.util import VectorSpaceClusterer as VectorSpaceClusterer

class EMClusterer(VectorSpaceClusterer):
    """
    The Gaussian EM clusterer models the vectors as being produced by
    a mixture of k Gaussian sources. The parameters of these sources
    (prior probability, mean and covariance matrix) are then found to
    maximise the likelihood of the given data. This is done with the
    expectation maximisation algorithm. It starts with k arbitrarily
    chosen means, priors and covariance matrices. It then calculates
    the membership probabilities for each vector in each of the
    clusters; this is the 'E' step. The cluster parameters are then
    updated in the 'M' step using the maximum likelihood estimate from
    the cluster membership probabilities. This process continues until
    the likelihood of the data does not significantly increase.
    """
    def __init__(self, initial_means, priors: Incomplete | None = None, covariance_matrices: Incomplete | None = None, conv_threshold: float = 1e-06, bias: float = 0.1, normalise: bool = False, svd_dimensions: Incomplete | None = None) -> None:
        """
        Creates an EM clusterer with the given starting parameters,
        convergence threshold and vector mangling parameters.

        :param  initial_means: the means of the gaussian cluster centers
        :type   initial_means: [seq of] numpy array or seq of SparseArray
        :param  priors: the prior probability for each cluster
        :type   priors: numpy array or seq of float
        :param  covariance_matrices: the covariance matrix for each cluster
        :type   covariance_matrices: [seq of] numpy array
        :param  conv_threshold: maximum change in likelihood before deemed
                    convergent
        :type   conv_threshold: int or float
        :param  bias: variance bias used to ensure non-singular covariance
                      matrices
        :type   bias: float
        :param  normalise:  should vectors be normalised to length 1
        :type   normalise:  boolean
        :param  svd_dimensions: number of dimensions to use in reducing vector
                               dimensionsionality with SVD
        :type   svd_dimensions: int
        """
    def num_clusters(self): ...
    def cluster_vectorspace(self, vectors, trace: bool = False) -> None: ...
    def classify_vectorspace(self, vector): ...
    def likelihood_vectorspace(self, vector, cluster): ...

def demo() -> None:
    """
    Non-interactive demonstration of the clusterers with simple 2-D data.
    """
