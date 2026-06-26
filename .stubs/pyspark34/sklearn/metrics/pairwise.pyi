from .. import config_context as config_context
from ..exceptions import DataConversionWarning as DataConversionWarning
from ..preprocessing import normalize as normalize
from ..utils import check_array as check_array, gen_batches as gen_batches, gen_even_slices as gen_even_slices, get_chunk_n_rows as get_chunk_n_rows, is_scalar_nan as is_scalar_nan
from ..utils._param_validation import Hidden as Hidden, Integral as Integral, Interval as Interval, MissingValues as MissingValues, Options as Options, Real as Real, StrOptions as StrOptions, validate_params as validate_params
from ..utils.extmath import row_norms as row_norms, safe_sparse_dot as safe_sparse_dot
from ..utils.fixes import parse_version as parse_version, sp_base_version as sp_base_version
from ..utils.parallel import Parallel as Parallel, delayed as delayed
from ..utils.validation import check_non_negative as check_non_negative
from ._pairwise_distances_reduction import ArgKmin as ArgKmin
from _typeshed import Incomplete
from collections.abc import Generator

def check_pairwise_arrays(X, Y, *, precomputed: bool = False, dtype: Incomplete | None = None, accept_sparse: str = 'csr', force_all_finite: bool = True, copy: bool = False):
    """Set X and Y appropriately and checks inputs.

    If Y is None, it is set as a pointer to X (i.e. not a copy).
    If Y is given, this does not happen.
    All distance metrics should use this function first to assert that the
    given parameters are correct and safe to use.

    Specifically, this function first ensures that both X and Y are arrays,
    then checks that they are at least two dimensional while ensuring that
    their elements are floats (or dtype if provided). Finally, the function
    checks that the size of the second dimension of the two arrays is equal, or
    the equivalent check for a precomputed distance matrix.

    Parameters
    ----------
    X : {array-like, sparse matrix} of shape (n_samples_X, n_features)

    Y : {array-like, sparse matrix} of shape (n_samples_Y, n_features)

    precomputed : bool, default=False
        True if X is to be treated as precomputed distances to the samples in
        Y.

    dtype : str, type, list of type, default=None
        Data type required for X and Y. If None, the dtype will be an
        appropriate float type selected by _return_float_dtype.

        .. versionadded:: 0.18

    accept_sparse : str, bool or list/tuple of str, default='csr'
        String[s] representing allowed sparse matrix formats, such as 'csc',
        'csr', etc. If the input is sparse but not in the allowed format,
        it will be converted to the first listed format. True allows the input
        to be any format. False means that a sparse matrix input will
        raise an error.

    force_all_finite : bool or 'allow-nan', default=True
        Whether to raise an error on np.inf, np.nan, pd.NA in array. The
        possibilities are:

        - True: Force all values of array to be finite.
        - False: accepts np.inf, np.nan, pd.NA in array.
        - 'allow-nan': accepts only np.nan and pd.NA values in array. Values
          cannot be infinite.

        .. versionadded:: 0.22
           ``force_all_finite`` accepts the string ``'allow-nan'``.

        .. versionchanged:: 0.23
           Accepts `pd.NA` and converts it into `np.nan`.

    copy : bool, default=False
        Whether a forced copy will be triggered. If copy=False, a copy might
        be triggered by a conversion.

        .. versionadded:: 0.22

    Returns
    -------
    safe_X : {array-like, sparse matrix} of shape (n_samples_X, n_features)
        An array equal to X, guaranteed to be a numpy array.

    safe_Y : {array-like, sparse matrix} of shape (n_samples_Y, n_features)
        An array equal to Y if Y was not None, guaranteed to be a numpy array.
        If Y was None, safe_Y will be a pointer to X.
    """
def check_paired_arrays(X, Y):
    """Set X and Y appropriately and checks inputs for paired distances.

    All paired distance metrics should use this function first to assert that
    the given parameters are correct and safe to use.

    Specifically, this function first ensures that both X and Y are arrays,
    then checks that they are at least two dimensional while ensuring that
    their elements are floats. Finally, the function checks that the size
    of the dimensions of the two arrays are equal.

    Parameters
    ----------
    X : {array-like, sparse matrix} of shape (n_samples_X, n_features)

    Y : {array-like, sparse matrix} of shape (n_samples_Y, n_features)

    Returns
    -------
    safe_X : {array-like, sparse matrix} of shape (n_samples_X, n_features)
        An array equal to X, guaranteed to be a numpy array.

    safe_Y : {array-like, sparse matrix} of shape (n_samples_Y, n_features)
        An array equal to Y if Y was not None, guaranteed to be a numpy array.
        If Y was None, safe_Y will be a pointer to X.
    """
def euclidean_distances(X, Y: Incomplete | None = None, *, Y_norm_squared: Incomplete | None = None, squared: bool = False, X_norm_squared: Incomplete | None = None):
    '''
    Compute the distance matrix between each pair from a vector array X and Y.

    For efficiency reasons, the euclidean distance between a pair of row
    vector x and y is computed as::

        dist(x, y) = sqrt(dot(x, x) - 2 * dot(x, y) + dot(y, y))

    This formulation has two advantages over other ways of computing distances.
    First, it is computationally efficient when dealing with sparse data.
    Second, if one argument varies but the other remains unchanged, then
    `dot(x, x)` and/or `dot(y, y)` can be pre-computed.

    However, this is not the most precise way of doing this computation,
    because this equation potentially suffers from "catastrophic cancellation".
    Also, the distance matrix returned by this function may not be exactly
    symmetric as required by, e.g., ``scipy.spatial.distance`` functions.

    Read more in the :ref:`User Guide <metrics>`.

    Parameters
    ----------
    X : {array-like, sparse matrix} of shape (n_samples_X, n_features)
        An array where each row is a sample and each column is a feature.

    Y : {array-like, sparse matrix} of shape (n_samples_Y, n_features),             default=None
        An array where each row is a sample and each column is a feature.
        If `None`, method uses `Y=X`.

    Y_norm_squared : array-like of shape (n_samples_Y,) or (n_samples_Y, 1)             or (1, n_samples_Y), default=None
        Pre-computed dot-products of vectors in Y (e.g.,
        ``(Y**2).sum(axis=1)``)
        May be ignored in some cases, see the note below.

    squared : bool, default=False
        Return squared Euclidean distances.

    X_norm_squared : array-like of shape (n_samples_X,) or (n_samples_X, 1)             or (1, n_samples_X), default=None
        Pre-computed dot-products of vectors in X (e.g.,
        ``(X**2).sum(axis=1)``)
        May be ignored in some cases, see the note below.

    Returns
    -------
    distances : ndarray of shape (n_samples_X, n_samples_Y)
        Returns the distances between the row vectors of `X`
        and the row vectors of `Y`.

    See Also
    --------
    paired_distances : Distances between pairs of elements of X and Y.

    Notes
    -----
    To achieve a better accuracy, `X_norm_squared`\xa0and `Y_norm_squared` may be
    unused if they are passed as `np.float32`.

    Examples
    --------
    >>> from sklearn.metrics.pairwise import euclidean_distances
    >>> X = [[0, 1], [1, 1]]
    >>> # distance between rows of X
    >>> euclidean_distances(X, X)
    array([[0., 1.],
           [1., 0.]])
    >>> # get distance to origin
    >>> euclidean_distances(X, [[0, 0]])
    array([[1.        ],
           [1.41421356]])
    '''
def nan_euclidean_distances(X, Y: Incomplete | None = None, *, squared: bool = False, missing_values=..., copy: bool = True):
    '''Calculate the euclidean distances in the presence of missing values.

    Compute the euclidean distance between each pair of samples in X and Y,
    where Y=X is assumed if Y=None. When calculating the distance between a
    pair of samples, this formulation ignores feature coordinates with a
    missing value in either sample and scales up the weight of the remaining
    coordinates:

        dist(x,y) = sqrt(weight * sq. distance from present coordinates)
        where,
        weight = Total # of coordinates / # of present coordinates

    For example, the distance between ``[3, na, na, 6]`` and ``[1, na, 4, 5]``
    is:

        .. math::
            \\sqrt{\\frac{4}{2}((3-1)^2 + (6-5)^2)}

    If all the coordinates are missing or if there are no common present
    coordinates then NaN is returned for that pair.

    Read more in the :ref:`User Guide <metrics>`.

    .. versionadded:: 0.22

    Parameters
    ----------
    X : array-like of shape (n_samples_X, n_features)
        An array where each row is a sample and each column is a feature.

    Y : array-like of shape (n_samples_Y, n_features), default=None
        An array where each row is a sample and each column is a feature.
        If `None`, method uses `Y=X`.

    squared : bool, default=False
        Return squared Euclidean distances.

    missing_values : np.nan, float or int, default=np.nan
        Representation of missing value.

    copy : bool, default=True
        Make and use a deep copy of X and Y (if Y exists).

    Returns
    -------
    distances : ndarray of shape (n_samples_X, n_samples_Y)
        Returns the distances between the row vectors of `X`
        and the row vectors of `Y`.

    See Also
    --------
    paired_distances : Distances between pairs of elements of X and Y.

    References
    ----------
    * John K. Dixon, "Pattern Recognition with Partly Missing Data",
      IEEE Transactions on Systems, Man, and Cybernetics, Volume: 9, Issue:
      10, pp. 617 - 621, Oct. 1979.
      http://ieeexplore.ieee.org/abstract/document/4310090/

    Examples
    --------
    >>> from sklearn.metrics.pairwise import nan_euclidean_distances
    >>> nan = float("NaN")
    >>> X = [[0, 1], [1, nan]]
    >>> nan_euclidean_distances(X, X) # distance between rows of X
    array([[0.        , 1.41421356],
           [1.41421356, 0.        ]])

    >>> # get distance to origin
    >>> nan_euclidean_distances(X, [[0, 0]])
    array([[1.        ],
           [1.41421356]])
    '''
def pairwise_distances_argmin_min(X, Y, *, axis: int = 1, metric: str = 'euclidean', metric_kwargs: Incomplete | None = None):
    """Compute minimum distances between one point and a set of points.

    This function computes for each row in X, the index of the row of Y which
    is closest (according to the specified distance). The minimal distances are
    also returned.

    This is mostly equivalent to calling:

        (pairwise_distances(X, Y=Y, metric=metric).argmin(axis=axis),
         pairwise_distances(X, Y=Y, metric=metric).min(axis=axis))

    but uses much less memory, and is faster for large arrays.

    Parameters
    ----------
    X : {array-like, sparse matrix} of shape (n_samples_X, n_features)
        Array containing points.

    Y : {array-like, sparse matrix} of shape (n_samples_Y, n_features)
        Array containing points.

    axis : int, default=1
        Axis along which the argmin and distances are to be computed.

    metric : str or callable, default='euclidean'
        Metric to use for distance computation. Any metric from scikit-learn
        or scipy.spatial.distance can be used.

        If metric is a callable function, it is called on each
        pair of instances (rows) and the resulting value recorded. The callable
        should take two arrays as input and return one value indicating the
        distance between them. This works for Scipy's metrics, but is less
        efficient than passing the metric name as a string.

        Distance matrices are not supported.

        Valid values for metric are:

        - from scikit-learn: ['cityblock', 'cosine', 'euclidean', 'l1', 'l2',
          'manhattan']

        - from scipy.spatial.distance: ['braycurtis', 'canberra', 'chebyshev',
          'correlation', 'dice', 'hamming', 'jaccard', 'kulsinski',
          'mahalanobis', 'minkowski', 'rogerstanimoto', 'russellrao',
          'seuclidean', 'sokalmichener', 'sokalsneath', 'sqeuclidean',
          'yule']

        See the documentation for scipy.spatial.distance for details on these
        metrics.

        .. note::
           `'kulsinski'` is deprecated from SciPy 1.9 and will be removed in SciPy 1.11.

        .. note::
           `'matching'` has been removed in SciPy 1.9 (use `'hamming'` instead).

    metric_kwargs : dict, default=None
        Keyword arguments to pass to specified metric function.

    Returns
    -------
    argmin : ndarray
        Y[argmin[i], :] is the row in Y that is closest to X[i, :].

    distances : ndarray
        The array of minimum distances. `distances[i]` is the distance between
        the i-th row in X and the argmin[i]-th row in Y.

    See Also
    --------
    pairwise_distances : Distances between every pair of samples of X and Y.
    pairwise_distances_argmin : Same as `pairwise_distances_argmin_min` but only
        returns the argmins.
    """
def pairwise_distances_argmin(X, Y, *, axis: int = 1, metric: str = 'euclidean', metric_kwargs: Incomplete | None = None):
    '''Compute minimum distances between one point and a set of points.

    This function computes for each row in X, the index of the row of Y which
    is closest (according to the specified distance).

    This is mostly equivalent to calling:

        pairwise_distances(X, Y=Y, metric=metric).argmin(axis=axis)

    but uses much less memory, and is faster for large arrays.

    This function works with dense 2D arrays only.

    Parameters
    ----------
    X : {array-like, sparse matrix} of shape (n_samples_X, n_features)
        Array containing points.

    Y : {array-like, sparse matrix} of shape (n_samples_Y, n_features)
        Arrays containing points.

    axis : int, default=1
        Axis along which the argmin and distances are to be computed.

    metric : str or callable, default="euclidean"
        Metric to use for distance computation. Any metric from scikit-learn
        or scipy.spatial.distance can be used.

        If metric is a callable function, it is called on each
        pair of instances (rows) and the resulting value recorded. The callable
        should take two arrays as input and return one value indicating the
        distance between them. This works for Scipy\'s metrics, but is less
        efficient than passing the metric name as a string.

        Distance matrices are not supported.

        Valid values for metric are:

        - from scikit-learn: [\'cityblock\', \'cosine\', \'euclidean\', \'l1\', \'l2\',
          \'manhattan\']

        - from scipy.spatial.distance: [\'braycurtis\', \'canberra\', \'chebyshev\',
          \'correlation\', \'dice\', \'hamming\', \'jaccard\', \'kulsinski\',
          \'mahalanobis\', \'minkowski\', \'rogerstanimoto\', \'russellrao\',
          \'seuclidean\', \'sokalmichener\', \'sokalsneath\', \'sqeuclidean\',
          \'yule\']

        See the documentation for scipy.spatial.distance for details on these
        metrics.

        .. note::
           `\'kulsinski\'` is deprecated from SciPy 1.9 and will be removed in SciPy 1.11.

        .. note::
           `\'matching\'` has been removed in SciPy 1.9 (use `\'hamming\'` instead).

    metric_kwargs : dict, default=None
        Keyword arguments to pass to specified metric function.

    Returns
    -------
    argmin : numpy.ndarray
        Y[argmin[i], :] is the row in Y that is closest to X[i, :].

    See Also
    --------
    pairwise_distances : Distances between every pair of samples of X and Y.
    pairwise_distances_argmin_min : Same as `pairwise_distances_argmin` but also
        returns the distances.
    '''
def haversine_distances(X, Y: Incomplete | None = None):
    """Compute the Haversine distance between samples in X and Y.

    The Haversine (or great circle) distance is the angular distance between
    two points on the surface of a sphere. The first coordinate of each point
    is assumed to be the latitude, the second is the longitude, given
    in radians. The dimension of the data must be 2.

    .. math::
       D(x, y) = 2\\arcsin[\\sqrt{\\sin^2((x_{lat} - y_{lat}) / 2)
                                + \\cos(x_{lat})\\cos(y_{lat})\\\n                                sin^2((x_{lon} - y_{lon}) / 2)}]

    Parameters
    ----------
    X : {array-like, sparse matrix} of shape (n_samples_X, 2)
        A feature array.

    Y : {array-like, sparse matrix} of shape (n_samples_Y, 2), default=None
        An optional second feature array. If `None`, uses `Y=X`.

    Returns
    -------
    distance : ndarray of shape (n_samples_X, n_samples_Y)
        The distance matrix.

    Notes
    -----
    As the Earth is nearly spherical, the haversine formula provides a good
    approximation of the distance between two points of the Earth surface, with
    a less than 1% error on average.

    Examples
    --------
    We want to calculate the distance between the Ezeiza Airport
    (Buenos Aires, Argentina) and the Charles de Gaulle Airport (Paris,
    France).

    >>> from sklearn.metrics.pairwise import haversine_distances
    >>> from math import radians
    >>> bsas = [-34.83333, -58.5166646]
    >>> paris = [49.0083899664, 2.53844117956]
    >>> bsas_in_radians = [radians(_) for _ in bsas]
    >>> paris_in_radians = [radians(_) for _ in paris]
    >>> result = haversine_distances([bsas_in_radians, paris_in_radians])
    >>> result * 6371000/1000  # multiply by Earth radius to get kilometers
    array([[    0.        , 11099.54035582],
           [11099.54035582,     0.        ]])
    """
def manhattan_distances(X, Y: Incomplete | None = None, *, sum_over_features: str = 'deprecated'):
    """Compute the L1 distances between the vectors in X and Y.

    With sum_over_features equal to False it returns the componentwise
    distances.

    Read more in the :ref:`User Guide <metrics>`.

    Parameters
    ----------
    X : {array-like, sparse matrix} of shape (n_samples_X, n_features)
        An array where each row is a sample and each column is a feature.

    Y : {array-like, sparse matrix} of shape (n_samples_Y, n_features), default=None
        An array where each row is a sample and each column is a feature.
        If `None`, method uses `Y=X`.

    sum_over_features : bool, default=True
        If True the function returns the pairwise distance matrix
        else it returns the componentwise L1 pairwise-distances.
        Not supported for sparse matrix inputs.

        .. deprecated:: 1.2
            ``sum_over_features`` was deprecated in version 1.2 and will be removed in
            1.4.

    Returns
    -------
    D : ndarray of shape (n_samples_X * n_samples_Y, n_features) or             (n_samples_X, n_samples_Y)
        If sum_over_features is False shape is
        (n_samples_X * n_samples_Y, n_features) and D contains the
        componentwise L1 pairwise-distances (ie. absolute difference),
        else shape is (n_samples_X, n_samples_Y) and D contains
        the pairwise L1 distances.

    Notes
    -----
    When X and/or Y are CSR sparse matrices and they are not already
    in canonical format, this function modifies them in-place to
    make them canonical.

    Examples
    --------
    >>> from sklearn.metrics.pairwise import manhattan_distances
    >>> manhattan_distances([[3]], [[3]])
    array([[0.]])
    >>> manhattan_distances([[3]], [[2]])
    array([[1.]])
    >>> manhattan_distances([[2]], [[3]])
    array([[1.]])
    >>> manhattan_distances([[1, 2], [3, 4]],         [[1, 2], [0, 3]])
    array([[0., 2.],
           [4., 4.]])
    """
def cosine_distances(X, Y: Incomplete | None = None):
    """Compute cosine distance between samples in X and Y.

    Cosine distance is defined as 1.0 minus the cosine similarity.

    Read more in the :ref:`User Guide <metrics>`.

    Parameters
    ----------
    X : {array-like, sparse matrix} of shape (n_samples_X, n_features)
        Matrix `X`.

    Y : {array-like, sparse matrix} of shape (n_samples_Y, n_features),             default=None
        Matrix `Y`.

    Returns
    -------
    distance matrix : ndarray of shape (n_samples_X, n_samples_Y)
        Returns the cosine distance between samples in X and Y.

    See Also
    --------
    cosine_similarity : Compute cosine similarity between samples in X and Y.
    scipy.spatial.distance.cosine : Dense matrices only.
    """
def paired_euclidean_distances(X, Y):
    """Compute the paired euclidean distances between X and Y.

    Read more in the :ref:`User Guide <metrics>`.

    Parameters
    ----------
    X : {array-like, sparse matrix} of shape (n_samples, n_features)
        Input array/matrix X.

    Y : {array-like, sparse matrix} of shape (n_samples, n_features)
        Input array/matrix Y.

    Returns
    -------
    distances : ndarray of shape (n_samples,)
        Output array/matrix containing the calculated paired euclidean
        distances.
    """
def paired_manhattan_distances(X, Y):
    """Compute the paired L1 distances between X and Y.

    Distances are calculated between (X[0], Y[0]), (X[1], Y[1]), ...,
    (X[n_samples], Y[n_samples]).

    Read more in the :ref:`User Guide <metrics>`.

    Parameters
    ----------
    X : {array-like, sparse matrix} of shape (n_samples, n_features)
        An array-like where each row is a sample and each column is a feature.

    Y : {array-like, sparse matrix} of shape (n_samples, n_features)
        An array-like where each row is a sample and each column is a feature.

    Returns
    -------
    distances : ndarray of shape (n_samples,)
        L1 paired distances between the row vectors of `X`
        and the row vectors of `Y`.

    Examples
    --------
    >>> from sklearn.metrics.pairwise import paired_manhattan_distances
    >>> import numpy as np
    >>> X = np.array([[1, 1, 0], [0, 1, 0], [0, 0, 1]])
    >>> Y = np.array([[0, 1, 0], [0, 0, 1], [0, 0, 0]])
    >>> paired_manhattan_distances(X, Y)
    array([1., 2., 1.])
    """
def paired_cosine_distances(X, Y):
    """
    Compute the paired cosine distances between X and Y.

    Read more in the :ref:`User Guide <metrics>`.

    Parameters
    ----------
    X : {array-like, sparse matrix} of shape (n_samples, n_features)
        An array where each row is a sample and each column is a feature.

    Y : {array-like, sparse matrix} of shape (n_samples, n_features)
        An array where each row is a sample and each column is a feature.

    Returns
    -------
    distances : ndarray of shape (n_samples,)
        Returns the distances between the row vectors of `X`
        and the row vectors of `Y`, where `distances[i]` is the
        distance between `X[i]` and `Y[i]`.

    Notes
    -----
    The cosine distance is equivalent to the half the squared
    euclidean distance if each sample is normalized to unit norm.
    """

PAIRED_DISTANCES: Incomplete

def paired_distances(X, Y, *, metric: str = 'euclidean', **kwds):
    '''
    Compute the paired distances between X and Y.

    Compute the distances between (X[0], Y[0]), (X[1], Y[1]), etc...

    Read more in the :ref:`User Guide <metrics>`.

    Parameters
    ----------
    X : ndarray of shape (n_samples, n_features)
        Array 1 for distance computation.

    Y : ndarray of shape (n_samples, n_features)
        Array 2 for distance computation.

    metric : str or callable, default="euclidean"
        The metric to use when calculating distance between instances in a
        feature array. If metric is a string, it must be one of the options
        specified in PAIRED_DISTANCES, including "euclidean",
        "manhattan", or "cosine".
        Alternatively, if metric is a callable function, it is called on each
        pair of instances (rows) and the resulting value recorded. The callable
        should take two arrays from `X` as input and return a value indicating
        the distance between them.

    **kwds : dict
        Unused parameters.

    Returns
    -------
    distances : ndarray of shape (n_samples,)
        Returns the distances between the row vectors of `X`
        and the row vectors of `Y`.

    See Also
    --------
    pairwise_distances : Computes the distance between every pair of samples.

    Examples
    --------
    >>> from sklearn.metrics.pairwise import paired_distances
    >>> X = [[0, 1], [1, 1]]
    >>> Y = [[0, 1], [2, 1]]
    >>> paired_distances(X, Y)
    array([0., 1.])
    '''
def linear_kernel(X, Y: Incomplete | None = None, dense_output: bool = True):
    """
    Compute the linear kernel between X and Y.

    Read more in the :ref:`User Guide <linear_kernel>`.

    Parameters
    ----------
    X : {array-like, sparse matrix} of shape (n_samples_X, n_features)
        A feature array.

    Y : {array-like, sparse matrix} of shape (n_samples_Y, n_features), default=None
        An optional second feature array. If `None`, uses `Y=X`.

    dense_output : bool, default=True
        Whether to return dense output even when the input is sparse. If
        ``False``, the output is sparse if both input arrays are sparse.

        .. versionadded:: 0.20

    Returns
    -------
    Gram matrix : ndarray of shape (n_samples_X, n_samples_Y)
        The Gram matrix of the linear kernel, i.e. `X @ Y.T`.
    """
def polynomial_kernel(X, Y: Incomplete | None = None, degree: int = 3, gamma: Incomplete | None = None, coef0: int = 1):
    """
    Compute the polynomial kernel between X and Y.

        K(X, Y) = (gamma <X, Y> + coef0) ^ degree

    Read more in the :ref:`User Guide <polynomial_kernel>`.

    Parameters
    ----------
    X : {array-like, sparse matrix} of shape (n_samples_X, n_features)
        A feature array.

    Y : {array-like, sparse matrix} of shape (n_samples_Y, n_features), default=None
        An optional second feature array. If `None`, uses `Y=X`.

    degree : float, default=3
        Kernel degree.

    gamma : float, default=None
        Coefficient of the vector inner product. If None, defaults to 1.0 / n_features.

    coef0 : float, default=1
        Constant offset added to scaled inner product.

    Returns
    -------
    Gram matrix : ndarray of shape (n_samples_X, n_samples_Y)
        The polynomial kernel.
    """
def sigmoid_kernel(X, Y: Incomplete | None = None, gamma: Incomplete | None = None, coef0: int = 1):
    """Compute the sigmoid kernel between X and Y.

        K(X, Y) = tanh(gamma <X, Y> + coef0)

    Read more in the :ref:`User Guide <sigmoid_kernel>`.

    Parameters
    ----------
    X : {array-like, sparse matrix} of shape (n_samples_X, n_features)
        A feature array.

    Y : {array-like, sparse matrix} of shape (n_samples_Y, n_features), default=None
        An optional second feature array. If `None`, uses `Y=X`.

    gamma : float, default=None
        Coefficient of the vector inner product. If None, defaults to 1.0 / n_features.

    coef0 : float, default=1
        Constant offset added to scaled inner product.

    Returns
    -------
    Gram matrix : ndarray of shape (n_samples_X, n_samples_Y)
        Sigmoid kernel between two arrays.
    """
def rbf_kernel(X, Y: Incomplete | None = None, gamma: Incomplete | None = None):
    """Compute the rbf (gaussian) kernel between X and Y.

        K(x, y) = exp(-gamma ||x-y||^2)

    for each pair of rows x in X and y in Y.

    Read more in the :ref:`User Guide <rbf_kernel>`.

    Parameters
    ----------
    X : {array-like, sparse matrix} of shape (n_samples_X, n_features)
        A feature array.

    Y : {array-like, sparse matrix} of shape (n_samples_Y, n_features), default=None
        An optional second feature array. If `None`, uses `Y=X`.

    gamma : float, default=None
        If None, defaults to 1.0 / n_features.

    Returns
    -------
    kernel_matrix : ndarray of shape (n_samples_X, n_samples_Y)
        The RBF kernel.
    """
def laplacian_kernel(X, Y: Incomplete | None = None, gamma: Incomplete | None = None):
    """Compute the laplacian kernel between X and Y.

    The laplacian kernel is defined as::

        K(x, y) = exp(-gamma ||x-y||_1)

    for each pair of rows x in X and y in Y.
    Read more in the :ref:`User Guide <laplacian_kernel>`.

    .. versionadded:: 0.17

    Parameters
    ----------
    X : {array-like, sparse matrix} of shape (n_samples_X, n_features)
        A feature array.

    Y : {array-like, sparse matrix} of shape (n_samples_Y, n_features), default=None
        An optional second feature array. If `None`, uses `Y=X`.

    gamma : float, default=None
        If None, defaults to 1.0 / n_features. Otherwise it should be strictly positive.

    Returns
    -------
    kernel_matrix : ndarray of shape (n_samples_X, n_samples_Y)
        The kernel matrix.
    """
def cosine_similarity(X, Y: Incomplete | None = None, dense_output: bool = True):
    """Compute cosine similarity between samples in X and Y.

    Cosine similarity, or the cosine kernel, computes similarity as the
    normalized dot product of X and Y:

        K(X, Y) = <X, Y> / (||X||*||Y||)

    On L2-normalized data, this function is equivalent to linear_kernel.

    Read more in the :ref:`User Guide <cosine_similarity>`.

    Parameters
    ----------
    X : {array-like, sparse matrix} of shape (n_samples_X, n_features)
        Input data.

    Y : {array-like, sparse matrix} of shape (n_samples_Y, n_features),             default=None
        Input data. If ``None``, the output will be the pairwise
        similarities between all samples in ``X``.

    dense_output : bool, default=True
        Whether to return dense output even when the input is sparse. If
        ``False``, the output is sparse if both input arrays are sparse.

        .. versionadded:: 0.17
           parameter ``dense_output`` for dense output.

    Returns
    -------
    kernel matrix : ndarray of shape (n_samples_X, n_samples_Y)
        Returns the cosine similarity between samples in X and Y.
    """
def additive_chi2_kernel(X, Y: Incomplete | None = None):
    """Compute the additive chi-squared kernel between observations in X and Y.

    The chi-squared kernel is computed between each pair of rows in X and Y.  X
    and Y have to be non-negative. This kernel is most commonly applied to
    histograms.

    The chi-squared kernel is given by::

        k(x, y) = -Sum [(x - y)^2 / (x + y)]

    It can be interpreted as a weighted difference per entry.

    Read more in the :ref:`User Guide <chi2_kernel>`.

    Parameters
    ----------
    X : array-like of shape (n_samples_X, n_features)
        A feature array.

    Y : array-like of shape (n_samples_Y, n_features), default=None
        An optional second feature array. If `None`, uses `Y=X`.

    Returns
    -------
    kernel_matrix : ndarray of shape (n_samples_X, n_samples_Y)
        The kernel matrix.

    See Also
    --------
    chi2_kernel : The exponentiated version of the kernel, which is usually
        preferable.
    sklearn.kernel_approximation.AdditiveChi2Sampler : A Fourier approximation
        to this kernel.

    Notes
    -----
    As the negative of a distance, this kernel is only conditionally positive
    definite.

    References
    ----------
    * Zhang, J. and Marszalek, M. and Lazebnik, S. and Schmid, C.
      Local features and kernels for classification of texture and object
      categories: A comprehensive study
      International Journal of Computer Vision 2007
      https://hal.archives-ouvertes.fr/hal-00171412/document
    """
def chi2_kernel(X, Y: Incomplete | None = None, gamma: float = 1.0):
    """Compute the exponential chi-squared kernel between X and Y.

    The chi-squared kernel is computed between each pair of rows in X and Y.  X
    and Y have to be non-negative. This kernel is most commonly applied to
    histograms.

    The chi-squared kernel is given by::

        k(x, y) = exp(-gamma Sum [(x - y)^2 / (x + y)])

    It can be interpreted as a weighted difference per entry.

    Read more in the :ref:`User Guide <chi2_kernel>`.

    Parameters
    ----------
    X : array-like of shape (n_samples_X, n_features)
        A feature array.

    Y : ndarray of shape (n_samples_Y, n_features), default=None
        An optional second feature array. If `None`, uses `Y=X`.

    gamma : float, default=1
        Scaling parameter of the chi2 kernel.

    Returns
    -------
    kernel_matrix : ndarray of shape (n_samples_X, n_samples_Y)
        The kernel matrix.

    See Also
    --------
    additive_chi2_kernel : The additive version of this kernel.
    sklearn.kernel_approximation.AdditiveChi2Sampler : A Fourier approximation
        to the additive version of this kernel.

    References
    ----------
    * Zhang, J. and Marszalek, M. and Lazebnik, S. and Schmid, C.
      Local features and kernels for classification of texture and object
      categories: A comprehensive study
      International Journal of Computer Vision 2007
      https://hal.archives-ouvertes.fr/hal-00171412/document
    """

PAIRWISE_DISTANCE_FUNCTIONS: Incomplete

def distance_metrics():
    """Valid metrics for pairwise_distances.

    This function simply returns the valid pairwise distance metrics.
    It exists to allow for a description of the mapping for
    each of the valid strings.

    The valid distance metrics, and the function they map to, are:

    =============== ========================================
    metric          Function
    =============== ========================================
    'cityblock'     metrics.pairwise.manhattan_distances
    'cosine'        metrics.pairwise.cosine_distances
    'euclidean'     metrics.pairwise.euclidean_distances
    'haversine'     metrics.pairwise.haversine_distances
    'l1'            metrics.pairwise.manhattan_distances
    'l2'            metrics.pairwise.euclidean_distances
    'manhattan'     metrics.pairwise.manhattan_distances
    'nan_euclidean' metrics.pairwise.nan_euclidean_distances
    =============== ========================================

    Read more in the :ref:`User Guide <metrics>`.

    Returns
    -------
    distance_metrics : dict
        Returns valid metrics for pairwise_distances.
    """
def pairwise_distances_chunked(X, Y: Incomplete | None = None, *, reduce_func: Incomplete | None = None, metric: str = 'euclidean', n_jobs: Incomplete | None = None, working_memory: Incomplete | None = None, **kwds) -> Generator[Incomplete, None, None]:
    '''Generate a distance matrix chunk by chunk with optional reduction.

    In cases where not all of a pairwise distance matrix needs to be
    stored at once, this is used to calculate pairwise distances in
    ``working_memory``-sized chunks.  If ``reduce_func`` is given, it is
    run on each chunk and its return values are concatenated into lists,
    arrays or sparse matrices.

    Parameters
    ----------
    X : ndarray of shape (n_samples_X, n_samples_X) or             (n_samples_X, n_features)
        Array of pairwise distances between samples, or a feature array.
        The shape the array should be (n_samples_X, n_samples_X) if
        metric=\'precomputed\' and (n_samples_X, n_features) otherwise.

    Y : ndarray of shape (n_samples_Y, n_features), default=None
        An optional second feature array. Only allowed if
        metric != "precomputed".

    reduce_func : callable, default=None
        The function which is applied on each chunk of the distance matrix,
        reducing it to needed values.  ``reduce_func(D_chunk, start)``
        is called repeatedly, where ``D_chunk`` is a contiguous vertical
        slice of the pairwise distance matrix, starting at row ``start``.
        It should return one of: None; an array, a list, or a sparse matrix
        of length ``D_chunk.shape[0]``; or a tuple of such objects.
        Returning None is useful for in-place operations, rather than
        reductions.

        If None, pairwise_distances_chunked returns a generator of vertical
        chunks of the distance matrix.

    metric : str or callable, default=\'euclidean\'
        The metric to use when calculating distance between instances in a
        feature array. If metric is a string, it must be one of the options
        allowed by scipy.spatial.distance.pdist for its metric parameter,
        or a metric listed in pairwise.PAIRWISE_DISTANCE_FUNCTIONS.
        If metric is "precomputed", X is assumed to be a distance matrix.
        Alternatively, if metric is a callable function, it is called on
        each pair of instances (rows) and the resulting value recorded.
        The callable should take two arrays from X as input and return a
        value indicating the distance between them.

    n_jobs : int, default=None
        The number of jobs to use for the computation. This works by
        breaking down the pairwise matrix into n_jobs even slices and
        computing them in parallel.

        ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
        ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
        for more details.

    working_memory : int, default=None
        The sought maximum memory for temporary distance matrix chunks.
        When None (default), the value of
        ``sklearn.get_config()[\'working_memory\']`` is used.

    **kwds : optional keyword parameters
        Any further parameters are passed directly to the distance function.
        If using a scipy.spatial.distance metric, the parameters are still
        metric dependent. See the scipy docs for usage examples.

    Yields
    ------
    D_chunk : {ndarray, sparse matrix}
        A contiguous slice of distance matrix, optionally processed by
        ``reduce_func``.

    Examples
    --------
    Without reduce_func:

    >>> import numpy as np
    >>> from sklearn.metrics import pairwise_distances_chunked
    >>> X = np.random.RandomState(0).rand(5, 3)
    >>> D_chunk = next(pairwise_distances_chunked(X))
    >>> D_chunk
    array([[0.  ..., 0.29..., 0.41..., 0.19..., 0.57...],
           [0.29..., 0.  ..., 0.57..., 0.41..., 0.76...],
           [0.41..., 0.57..., 0.  ..., 0.44..., 0.90...],
           [0.19..., 0.41..., 0.44..., 0.  ..., 0.51...],
           [0.57..., 0.76..., 0.90..., 0.51..., 0.  ...]])

    Retrieve all neighbors and average distance within radius r:

    >>> r = .2
    >>> def reduce_func(D_chunk, start):
    ...     neigh = [np.flatnonzero(d < r) for d in D_chunk]
    ...     avg_dist = (D_chunk * (D_chunk < r)).mean(axis=1)
    ...     return neigh, avg_dist
    >>> gen = pairwise_distances_chunked(X, reduce_func=reduce_func)
    >>> neigh, avg_dist = next(gen)
    >>> neigh
    [array([0, 3]), array([1]), array([2]), array([0, 3]), array([4])]
    >>> avg_dist
    array([0.039..., 0.        , 0.        , 0.039..., 0.        ])

    Where r is defined per sample, we need to make use of ``start``:

    >>> r = [.2, .4, .4, .3, .1]
    >>> def reduce_func(D_chunk, start):
    ...     neigh = [np.flatnonzero(d < r[i])
    ...              for i, d in enumerate(D_chunk, start)]
    ...     return neigh
    >>> neigh = next(pairwise_distances_chunked(X, reduce_func=reduce_func))
    >>> neigh
    [array([0, 3]), array([0, 1]), array([2]), array([0, 3]), array([4])]

    Force row-by-row generation by reducing ``working_memory``:

    >>> gen = pairwise_distances_chunked(X, reduce_func=reduce_func,
    ...                                  working_memory=0)
    >>> next(gen)
    [array([0, 3])]
    >>> next(gen)
    [array([0, 1])]
    '''
def pairwise_distances(X, Y: Incomplete | None = None, metric: str = 'euclidean', *, n_jobs: Incomplete | None = None, force_all_finite: bool = True, **kwds):
    '''Compute the distance matrix from a vector array X and optional Y.

    This method takes either a vector array or a distance matrix, and returns
    a distance matrix. If the input is a vector array, the distances are
    computed. If the input is a distances matrix, it is returned instead.

    This method provides a safe way to take a distance matrix as input, while
    preserving compatibility with many other algorithms that take a vector
    array.

    If Y is given (default is None), then the returned matrix is the pairwise
    distance between the arrays from both X and Y.

    Valid values for metric are:

    - From scikit-learn: [\'cityblock\', \'cosine\', \'euclidean\', \'l1\', \'l2\',
      \'manhattan\']. These metrics support sparse matrix
      inputs.
      [\'nan_euclidean\'] but it does not yet support sparse matrices.

    - From scipy.spatial.distance: [\'braycurtis\', \'canberra\', \'chebyshev\',
      \'correlation\', \'dice\', \'hamming\', \'jaccard\', \'kulsinski\', \'mahalanobis\',
      \'minkowski\', \'rogerstanimoto\', \'russellrao\', \'seuclidean\',
      \'sokalmichener\', \'sokalsneath\', \'sqeuclidean\', \'yule\']
      See the documentation for scipy.spatial.distance for details on these
      metrics. These metrics do not support sparse matrix inputs.

    .. note::
        `\'kulsinski\'` is deprecated from SciPy 1.9 and will be removed in SciPy 1.11.

    .. note::
        `\'matching\'` has been removed in SciPy 1.9 (use `\'hamming\'` instead).

    Note that in the case of \'cityblock\', \'cosine\' and \'euclidean\' (which are
    valid scipy.spatial.distance metrics), the scikit-learn implementation
    will be used, which is faster and has support for sparse matrices (except
    for \'cityblock\'). For a verbose description of the metrics from
    scikit-learn, see :func:`sklearn.metrics.pairwise.distance_metrics`
    function.

    Read more in the :ref:`User Guide <metrics>`.

    Parameters
    ----------
    X : ndarray of shape (n_samples_X, n_samples_X) or             (n_samples_X, n_features)
        Array of pairwise distances between samples, or a feature array.
        The shape of the array should be (n_samples_X, n_samples_X) if
        metric == "precomputed" and (n_samples_X, n_features) otherwise.

    Y : ndarray of shape (n_samples_Y, n_features), default=None
        An optional second feature array. Only allowed if
        metric != "precomputed".

    metric : str or callable, default=\'euclidean\'
        The metric to use when calculating distance between instances in a
        feature array. If metric is a string, it must be one of the options
        allowed by scipy.spatial.distance.pdist for its metric parameter, or
        a metric listed in ``pairwise.PAIRWISE_DISTANCE_FUNCTIONS``.
        If metric is "precomputed", X is assumed to be a distance matrix.
        Alternatively, if metric is a callable function, it is called on each
        pair of instances (rows) and the resulting value recorded. The callable
        should take two arrays from X as input and return a value indicating
        the distance between them.

    n_jobs : int, default=None
        The number of jobs to use for the computation. This works by breaking
        down the pairwise matrix into n_jobs even slices and computing them in
        parallel.

        ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
        ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
        for more details.

    force_all_finite : bool or \'allow-nan\', default=True
        Whether to raise an error on np.inf, np.nan, pd.NA in array. Ignored
        for a metric listed in ``pairwise.PAIRWISE_DISTANCE_FUNCTIONS``. The
        possibilities are:

        - True: Force all values of array to be finite.
        - False: accepts np.inf, np.nan, pd.NA in array.
        - \'allow-nan\': accepts only np.nan and pd.NA values in array. Values
          cannot be infinite.

        .. versionadded:: 0.22
           ``force_all_finite`` accepts the string ``\'allow-nan\'``.

        .. versionchanged:: 0.23
           Accepts `pd.NA` and converts it into `np.nan`.

    **kwds : optional keyword parameters
        Any further parameters are passed directly to the distance function.
        If using a scipy.spatial.distance metric, the parameters are still
        metric dependent. See the scipy docs for usage examples.

    Returns
    -------
    D : ndarray of shape (n_samples_X, n_samples_X) or             (n_samples_X, n_samples_Y)
        A distance matrix D such that D_{i, j} is the distance between the
        ith and jth vectors of the given matrix X, if Y is None.
        If Y is not None, then D_{i, j} is the distance between the ith array
        from X and the jth array from Y.

    See Also
    --------
    pairwise_distances_chunked : Performs the same calculation as this
        function, but returns a generator of chunks of the distance matrix, in
        order to limit memory usage.
    paired_distances : Computes the distances between corresponding elements
        of two arrays.
    '''

PAIRWISE_BOOLEAN_FUNCTIONS: Incomplete
PAIRWISE_KERNEL_FUNCTIONS: Incomplete

def kernel_metrics():
    """Valid metrics for pairwise_kernels.

    This function simply returns the valid pairwise distance metrics.
    It exists, however, to allow for a verbose description of the mapping for
    each of the valid strings.

    The valid distance metrics, and the function they map to, are:
      ===============   ========================================
      metric            Function
      ===============   ========================================
      'additive_chi2'   sklearn.pairwise.additive_chi2_kernel
      'chi2'            sklearn.pairwise.chi2_kernel
      'linear'          sklearn.pairwise.linear_kernel
      'poly'            sklearn.pairwise.polynomial_kernel
      'polynomial'      sklearn.pairwise.polynomial_kernel
      'rbf'             sklearn.pairwise.rbf_kernel
      'laplacian'       sklearn.pairwise.laplacian_kernel
      'sigmoid'         sklearn.pairwise.sigmoid_kernel
      'cosine'          sklearn.pairwise.cosine_similarity
      ===============   ========================================

    Read more in the :ref:`User Guide <metrics>`.

    Returns
    -------
    kernal_metrics : dict
        Returns valid metrics for pairwise_kernels.
    """

KERNEL_PARAMS: Incomplete

def pairwise_kernels(X, Y: Incomplete | None = None, metric: str = 'linear', *, filter_params: bool = False, n_jobs: Incomplete | None = None, **kwds):
    '''Compute the kernel between arrays X and optional array Y.

    This method takes either a vector array or a kernel matrix, and returns
    a kernel matrix. If the input is a vector array, the kernels are
    computed. If the input is a kernel matrix, it is returned instead.

    This method provides a safe way to take a kernel matrix as input, while
    preserving compatibility with many other algorithms that take a vector
    array.

    If Y is given (default is None), then the returned matrix is the pairwise
    kernel between the arrays from both X and Y.

    Valid values for metric are:
        [\'additive_chi2\', \'chi2\', \'linear\', \'poly\', \'polynomial\', \'rbf\',
        \'laplacian\', \'sigmoid\', \'cosine\']

    Read more in the :ref:`User Guide <metrics>`.

    Parameters
    ----------
    X : ndarray of shape (n_samples_X, n_samples_X) or (n_samples_X, n_features)
        Array of pairwise kernels between samples, or a feature array.
        The shape of the array should be (n_samples_X, n_samples_X) if
        metric == "precomputed" and (n_samples_X, n_features) otherwise.

    Y : ndarray of shape (n_samples_Y, n_features), default=None
        A second feature array only if X has shape (n_samples_X, n_features).

    metric : str or callable, default="linear"
        The metric to use when calculating kernel between instances in a
        feature array. If metric is a string, it must be one of the metrics
        in pairwise.PAIRWISE_KERNEL_FUNCTIONS.
        If metric is "precomputed", X is assumed to be a kernel matrix.
        Alternatively, if metric is a callable function, it is called on each
        pair of instances (rows) and the resulting value recorded. The callable
        should take two rows from X as input and return the corresponding
        kernel value as a single number. This means that callables from
        :mod:`sklearn.metrics.pairwise` are not allowed, as they operate on
        matrices, not single samples. Use the string identifying the kernel
        instead.

    filter_params : bool, default=False
        Whether to filter invalid parameters or not.

    n_jobs : int, default=None
        The number of jobs to use for the computation. This works by breaking
        down the pairwise matrix into n_jobs even slices and computing them in
        parallel.

        ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
        ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
        for more details.

    **kwds : optional keyword parameters
        Any further parameters are passed directly to the kernel function.

    Returns
    -------
    K : ndarray of shape (n_samples_X, n_samples_X) or (n_samples_X, n_samples_Y)
        A kernel matrix K such that K_{i, j} is the kernel between the
        ith and jth vectors of the given matrix X, if Y is None.
        If Y is not None, then K_{i, j} is the kernel between the ith array
        from X and the jth array from Y.

    Notes
    -----
    If metric is \'precomputed\', Y is ignored and X is returned.
    '''
