from ...base import BaseEstimator as BaseEstimator, TransformerMixin as TransformerMixin
from ...utils import check_array as check_array, check_random_state as check_random_state
from ...utils.fixes import percentile as percentile
from ...utils.validation import check_is_fitted as check_is_fitted
from ._bitset import set_bitset_memoryview as set_bitset_memoryview
from .common import ALMOST_INF as ALMOST_INF, X_BINNED_DTYPE as X_BINNED_DTYPE, X_BITSET_INNER_DTYPE as X_BITSET_INNER_DTYPE, X_DTYPE as X_DTYPE
from _typeshed import Incomplete

class _BinMapper(TransformerMixin, BaseEstimator):
    """Transformer that maps a dataset into integer-valued bins.

    For continuous features, the bins are created in a feature-wise fashion,
    using quantiles so that each bins contains approximately the same number
    of samples. For large datasets, quantiles are computed on a subset of the
    data to speed-up the binning, but the quantiles should remain stable.

    For categorical features, the raw categorical values are expected to be
    in [0, 254] (this is not validated here though) and each category
    corresponds to a bin. All categorical values must be known at
    initialization: transform() doesn't know how to bin unknown categorical
    values. Note that transform() is only used on non-training data in the
    case of early stopping.

    Features with a small number of values may be binned into less than
    ``n_bins`` bins. The last bin (at index ``n_bins - 1``) is always reserved
    for missing values.

    Parameters
    ----------
    n_bins : int, default=256
        The maximum number of bins to use (including the bin for missing
        values). Should be in [3, 256]. Non-missing values are binned on
        ``max_bins = n_bins - 1`` bins. The last bin is always reserved for
        missing values. If for a given feature the number of unique values is
        less than ``max_bins``, then those unique values will be used to
        compute the bin thresholds, instead of the quantiles. For categorical
        features indicated by ``is_categorical``, the docstring for
        ``is_categorical`` details on this procedure.
    subsample : int or None, default=2e5
        If ``n_samples > subsample``, then ``sub_samples`` samples will be
        randomly chosen to compute the quantiles. If ``None``, the whole data
        is used.
    is_categorical : ndarray of bool of shape (n_features,), default=None
        Indicates categorical features. By default, all features are
        considered continuous.
    known_categories : list of {ndarray, None} of shape (n_features,),             default=none
        For each categorical feature, the array indicates the set of unique
        categorical values. These should be the possible values over all the
        data, not just the training data. For continuous features, the
        corresponding entry should be None.
    random_state: int, RandomState instance or None, default=None
        Pseudo-random number generator to control the random sub-sampling.
        Pass an int for reproducible output across multiple
        function calls.
        See :term:`Glossary <random_state>`.
    n_threads : int, default=None
        Number of OpenMP threads to use. `_openmp_effective_n_threads` is called
        to determine the effective number of threads use, which takes cgroups CPU
        quotes into account. See the docstring of `_openmp_effective_n_threads`
        for details.

    Attributes
    ----------
    bin_thresholds_ : list of ndarray
        For each feature, each array indicates how to map a feature into a
        binned feature. The semantic and size depends on the nature of the
        feature:
        - for real-valued features, the array corresponds to the real-valued
          bin thresholds (the upper bound of each bin). There are ``max_bins
          - 1`` thresholds, where ``max_bins = n_bins - 1`` is the number of
          bins used for non-missing values.
        - for categorical features, the array is a map from a binned category
          value to the raw category value. The size of the array is equal to
          ``min(max_bins, category_cardinality)`` where we ignore missing
          values in the cardinality.
    n_bins_non_missing_ : ndarray, dtype=np.uint32
        For each feature, gives the number of bins actually used for
        non-missing values. For features with a lot of unique values, this is
        equal to ``n_bins - 1``.
    is_categorical_ : ndarray of shape (n_features,), dtype=np.uint8
        Indicator for categorical features.
    missing_values_bin_idx_ : np.uint8
        The index of the bin where missing values are mapped. This is a
        constant across all features. This corresponds to the last bin, and
        it is always equal to ``n_bins - 1``. Note that if ``n_bins_missing_``
        is less than ``n_bins - 1`` for a given feature, then there are
        empty (and unused) bins.
    """
    n_bins: Incomplete
    subsample: Incomplete
    is_categorical: Incomplete
    known_categories: Incomplete
    random_state: Incomplete
    n_threads: Incomplete
    def __init__(self, n_bins: int = 256, subsample=..., is_categorical: Incomplete | None = None, known_categories: Incomplete | None = None, random_state: Incomplete | None = None, n_threads: Incomplete | None = None) -> None: ...
    is_categorical_: Incomplete
    missing_values_bin_idx_: Incomplete
    bin_thresholds_: Incomplete
    n_bins_non_missing_: Incomplete
    def fit(self, X, y: Incomplete | None = None):
        """Fit data X by computing the binning thresholds.

        The last bin is reserved for missing values, whether missing values
        are present in the data or not.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            The data to bin.
        y: None
            Ignored.

        Returns
        -------
        self : object
        """
    def transform(self, X):
        """Bin data X.

        Missing values will be mapped to the last bin.

        For categorical features, the mapping will be incorrect for unknown
        categories. Since the BinMapper is given known_categories of the
        entire training data (i.e. before the call to train_test_split() in
        case of early-stopping), this never happens.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            The data to bin.

        Returns
        -------
        X_binned : array-like of shape (n_samples, n_features)
            The binned data (fortran-aligned).
        """
    def make_known_categories_bitsets(self):
        """Create bitsets of known categories.

        Returns
        -------
        - known_cat_bitsets : ndarray of shape (n_categorical_features, 8)
            Array of bitsets of known categories, for each categorical feature.
        - f_idx_map : ndarray of shape (n_features,)
            Map from original feature index to the corresponding index in the
            known_cat_bitsets array.
        """
