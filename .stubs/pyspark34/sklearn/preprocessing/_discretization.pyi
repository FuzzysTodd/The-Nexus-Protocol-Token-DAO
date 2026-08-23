from ..base import BaseEstimator as BaseEstimator, TransformerMixin as TransformerMixin
from ..utils._param_validation import Hidden as Hidden, Interval as Interval, Options as Options, StrOptions as StrOptions
from ..utils.validation import check_array as check_array, check_is_fitted as check_is_fitted, check_random_state as check_random_state
from ._encoders import OneHotEncoder as OneHotEncoder
from _typeshed import Incomplete

class KBinsDiscretizer(TransformerMixin, BaseEstimator):
    '''
    Bin continuous data into intervals.

    Read more in the :ref:`User Guide <preprocessing_discretization>`.

    .. versionadded:: 0.20

    Parameters
    ----------
    n_bins : int or array-like of shape (n_features,), default=5
        The number of bins to produce. Raises ValueError if ``n_bins < 2``.

    encode : {\'onehot\', \'onehot-dense\', \'ordinal\'}, default=\'onehot\'
        Method used to encode the transformed result.

        - \'onehot\': Encode the transformed result with one-hot encoding
          and return a sparse matrix. Ignored features are always
          stacked to the right.
        - \'onehot-dense\': Encode the transformed result with one-hot encoding
          and return a dense array. Ignored features are always
          stacked to the right.
        - \'ordinal\': Return the bin identifier encoded as an integer value.

    strategy : {\'uniform\', \'quantile\', \'kmeans\'}, default=\'quantile\'
        Strategy used to define the widths of the bins.

        - \'uniform\': All bins in each feature have identical widths.
        - \'quantile\': All bins in each feature have the same number of points.
        - \'kmeans\': Values in each bin have the same nearest center of a 1D
          k-means cluster.

    dtype : {np.float32, np.float64}, default=None
        The desired data-type for the output. If None, output dtype is
        consistent with input dtype. Only np.float32 and np.float64 are
        supported.

        .. versionadded:: 0.24

    subsample : int or None, default=\'warn\'
        Maximum number of samples, used to fit the model, for computational
        efficiency. Defaults to 200_000 when `strategy=\'quantile\'` and to `None`
        when `strategy=\'uniform\'` or `strategy=\'kmeans\'`.
        `subsample=None` means that all the training samples are used when
        computing the quantiles that determine the binning thresholds.
        Since quantile computation relies on sorting each column of `X` and
        that sorting has an `n log(n)` time complexity,
        it is recommended to use subsampling on datasets with a
        very large number of samples.

        .. versionchanged:: 1.3
            The default value of `subsample` changed from `None` to `200_000` when
            `strategy="quantile"`.

        .. versionchanged:: 1.5
            The default value of `subsample` changed from `None` to `200_000` when
            `strategy="uniform"` or `strategy="kmeans"`.

    random_state : int, RandomState instance or None, default=None
        Determines random number generation for subsampling.
        Pass an int for reproducible results across multiple function calls.
        See the `subsample` parameter for more details.
        See :term:`Glossary <random_state>`.

        .. versionadded:: 1.1

    Attributes
    ----------
    bin_edges_ : ndarray of ndarray of shape (n_features,)
        The edges of each bin. Contain arrays of varying shapes ``(n_bins_, )``
        Ignored features will have empty arrays.

    n_bins_ : ndarray of shape (n_features,), dtype=np.int_
        Number of bins per feature. Bins whose width are too small
        (i.e., <= 1e-8) are removed with a warning.

    n_features_in_ : int
        Number of features seen during :term:`fit`.

        .. versionadded:: 0.24

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

        .. versionadded:: 1.0

    See Also
    --------
    Binarizer : Class used to bin values as ``0`` or
        ``1`` based on a parameter ``threshold``.

    Notes
    -----
    In bin edges for feature ``i``, the first and last values are used only for
    ``inverse_transform``. During transform, bin edges are extended to::

      np.concatenate([-np.inf, bin_edges_[i][1:-1], np.inf])

    You can combine ``KBinsDiscretizer`` with
    :class:`~sklearn.compose.ColumnTransformer` if you only want to preprocess
    part of the features.

    ``KBinsDiscretizer`` might produce constant features (e.g., when
    ``encode = \'onehot\'`` and certain bins do not contain any data).
    These features can be removed with feature selection algorithms
    (e.g., :class:`~sklearn.feature_selection.VarianceThreshold`).

    Examples
    --------
    >>> from sklearn.preprocessing import KBinsDiscretizer
    >>> X = [[-2, 1, -4,   -1],
    ...      [-1, 2, -3, -0.5],
    ...      [ 0, 3, -2,  0.5],
    ...      [ 1, 4, -1,    2]]
    >>> est = KBinsDiscretizer(
    ...     n_bins=3, encode=\'ordinal\', strategy=\'uniform\', subsample=None
    ... )
    >>> est.fit(X)
    KBinsDiscretizer(...)
    >>> Xt = est.transform(X)
    >>> Xt  # doctest: +SKIP
    array([[ 0., 0., 0., 0.],
           [ 1., 1., 1., 0.],
           [ 2., 2., 2., 1.],
           [ 2., 2., 2., 2.]])

    Sometimes it may be useful to convert the data back into the original
    feature space. The ``inverse_transform`` function converts the binned
    data into the original feature space. Each value will be equal to the mean
    of the two bin edges.

    >>> est.bin_edges_[0]
    array([-2., -1.,  0.,  1.])
    >>> est.inverse_transform(Xt)
    array([[-1.5,  1.5, -3.5, -0.5],
           [-0.5,  2.5, -2.5, -0.5],
           [ 0.5,  3.5, -1.5,  0.5],
           [ 0.5,  3.5, -1.5,  1.5]])
    '''
    n_bins: Incomplete
    encode: Incomplete
    strategy: Incomplete
    dtype: Incomplete
    subsample: Incomplete
    random_state: Incomplete
    def __init__(self, n_bins: int = 5, *, encode: str = 'onehot', strategy: str = 'quantile', dtype: Incomplete | None = None, subsample: str = 'warn', random_state: Incomplete | None = None) -> None: ...
    bin_edges_: Incomplete
    n_bins_: Incomplete
    def fit(self, X, y: Incomplete | None = None, sample_weight: Incomplete | None = None):
        '''
        Fit the estimator.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Data to be discretized.

        y : None
            Ignored. This parameter exists only for compatibility with
            :class:`~sklearn.pipeline.Pipeline`.

        sample_weight : ndarray of shape (n_samples,)
            Contains weight values to be associated with each sample.
            Only possible when `strategy` is set to `"quantile"`.

            .. versionadded:: 1.3

        Returns
        -------
        self : object
            Returns the instance itself.
        '''
    def transform(self, X):
        """
        Discretize the data.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Data to be discretized.

        Returns
        -------
        Xt : {ndarray, sparse matrix}, dtype={np.float32, np.float64}
            Data in the binned space. Will be a sparse matrix if
            `self.encode='onehot'` and ndarray otherwise.
        """
    def inverse_transform(self, Xt):
        """
        Transform discretized data back to original feature space.

        Note that this function does not regenerate the original data
        due to discretization rounding.

        Parameters
        ----------
        Xt : array-like of shape (n_samples, n_features)
            Transformed data in the binned space.

        Returns
        -------
        Xinv : ndarray, dtype={np.float32, np.float64}
            Data in the original feature space.
        """
    def get_feature_names_out(self, input_features: Incomplete | None = None):
        '''Get output feature names.

        Parameters
        ----------
        input_features : array-like of str or None, default=None
            Input features.

            - If `input_features` is `None`, then `feature_names_in_` is
              used as feature names in. If `feature_names_in_` is not defined,
              then the following input feature names are generated:
              `["x0", "x1", ..., "x(n_features_in_ - 1)"]`.
            - If `input_features` is an array-like, then `input_features` must
              match `feature_names_in_` if `feature_names_in_` is defined.

        Returns
        -------
        feature_names_out : ndarray of str objects
            Transformed feature names.
        '''
