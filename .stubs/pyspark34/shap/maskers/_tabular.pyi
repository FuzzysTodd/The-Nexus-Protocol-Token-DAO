from .. import utils as utils
from .._serializable import Deserializer as Deserializer, Serializer as Serializer
from ..utils import MaskedModel as MaskedModel, safe_isinstance as safe_isinstance
from ..utils._exceptions import DimensionError as DimensionError, InvalidClusteringError as InvalidClusteringError
from ._masker import Masker as Masker
from _typeshed import Incomplete

log: Incomplete

class Tabular(Masker):
    """ A common base class for Independent and Partition.
    """
    output_dataframe: bool
    feature_names: Incomplete
    mean: Incomplete
    cov: Incomplete
    data: Incomplete
    clustering: Incomplete
    max_samples: Incomplete
    shape: Incomplete
    supports_delta_masking: bool
    def __init__(self, data, max_samples: int = 100, clustering: Incomplete | None = None) -> None:
        """ This masks out tabular features by integrating over the given background dataset.

        Parameters
        ----------
        data : np.array, pandas.DataFrame
            The background dataset that is used for masking.

        max_samples : int
            The maximum number of samples to use from the passed background data. If data has more
            than max_samples then shap.utils.sample is used to subsample the dataset. The number of
            samples coming out of the masker (to be integrated over) matches the number of samples in
            the background dataset. This means larger background dataset cause longer runtimes. Normally
            about 1, 10, 100, or 1000 background samples are reasonable choices.

        clustering : string or None (default) or numpy.ndarray
            The distance metric to use for creating the clustering of the features. The
            distance function can be any valid scipy.spatial.distance.pdist's metric argument.
            However we suggest using 'correlation' in most cases. The full list of options is
            `braycurtis`, `canberra`, `chebyshev`, `cityblock`, `correlation`, `cosine`, `dice`,
            `euclidean`, `hamming`, `jaccard`, `jensenshannon`, `kulsinski`, `mahalanobis`,
            `matching`, `minkowski`, `rogerstanimoto`, `russellrao`, `seuclidean`,
            `sokalmichener`, `sokalsneath`, `sqeuclidean`, `yule`. These are all
            the options from scipy.spatial.distance.pdist's metric argument.
        """
    def __call__(self, mask, x): ...
    def invariants(self, x):
        """ This returns a mask of which features change when we mask them.

        This optional masking method allows explainers to avoid re-evaluating the model when
        the features that would have been masked are all invariant.
        """
    def save(self, out_file) -> None:
        """ Write a Tabular masker to a file stream.
        """
    @classmethod
    def load(cls, in_file, instantiate: bool = True):
        """ Load a Tabular masker from a file stream.
        """

class Independent(Tabular):
    """ This masks out tabular features by integrating over the given background dataset.
    """
    def __init__(self, data, max_samples: int = 100) -> None:
        """ Build a Independent masker with the given background data.

        Parameters
        ----------
        data : numpy.ndarray, pandas.DataFrame
            The background dataset that is used for masking.

        max_samples : int
            The maximum number of samples to use from the passed background data. If data has more
            than max_samples then shap.utils.sample is used to subsample the dataset. The number of
            samples coming out of the masker (to be integrated over) matches the number of samples in
            the background dataset. This means larger background dataset cause longer runtimes. Normally
            about 1, 10, 100, or 1000 background samples are reasonable choices.
        """

class Partition(Tabular):
    """ This masks out tabular features by integrating over the given background dataset.

    Unlike Independent, Partition respects a hierarchical structure of the data.
    """
    def __init__(self, data, max_samples: int = 100, clustering: str = 'correlation') -> None:
        """ Build a Partition masker with the given background data and clustering.

        Parameters
        ----------
        data : numpy.ndarray, pandas.DataFrame
            The background dataset that is used for masking.

        max_samples : int
            The maximum number of samples to use from the passed background data. If data has more
            than max_samples then shap.utils.sample is used to subsample the dataset. The number of
            samples coming out of the masker (to be integrated over) matches the number of samples in
            the background dataset. This means larger background dataset cause longer runtimes. Normally
            about 1, 10, 100, or 1000 background samples are reasonable choices.

        clustering : string or numpy.ndarray
            If a string, then this is the distance metric to use for creating the clustering of
            the features. The distance function can be any valid scipy.spatial.distance.pdist's metric
            argument. However we suggest using 'correlation' in most cases. The full list of options is
            `braycurtis`, `canberra`, `chebyshev`, `cityblock`, `correlation`, `cosine`, `dice`,
            `euclidean`, `hamming`, `jaccard`, `jensenshannon`, `kulsinski`, `mahalanobis`,
            `matching`, `minkowski`, `rogerstanimoto`, `russellrao`, `seuclidean`,
            `sokalmichener`, `sokalsneath`, `sqeuclidean`, `yule`. These are all
            the options from scipy.spatial.distance.pdist's metric argument.
            If an array, then this is assumed to be the clustering of the features.
        """

class Impute(Masker):
    """ This imputes the values of missing features using the values of the observed features.

    Unlike Independent, Gaussian imputes missing values based on correlations with observed data points.
    """
    mean: Incomplete
    cov: Incomplete
    data: Incomplete
    method: Incomplete
    def __init__(self, data, method: str = 'linear') -> None:
        ''' Build a Partition masker with the given background data and clustering.

        Parameters
        ----------
        data : numpy.ndarray, pandas.DataFrame or {"mean: numpy.ndarray, "cov": numpy.ndarray} dictionary
            The background dataset that is used for masking.
        '''
