from .._config import config_context as config_context
from ..base import BaseEstimator as BaseEstimator, ClusterMixin as ClusterMixin
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from ..metrics import euclidean_distances as euclidean_distances, pairwise_distances_argmin as pairwise_distances_argmin
from ..utils import check_random_state as check_random_state
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions, validate_params as validate_params
from ..utils.validation import check_is_fitted as check_is_fitted
from _typeshed import Incomplete

def affinity_propagation(S, *, preference: Incomplete | None = None, convergence_iter: int = 15, max_iter: int = 200, damping: float = 0.5, copy: bool = True, verbose: bool = False, return_n_iter: bool = False, random_state: Incomplete | None = None):
    '''Perform Affinity Propagation Clustering of data.

    Read more in the :ref:`User Guide <affinity_propagation>`.

    Parameters
    ----------
    S : array-like of shape (n_samples, n_samples)
        Matrix of similarities between points.

    preference : array-like of shape (n_samples,) or float, default=None
        Preferences for each point - points with larger values of
        preferences are more likely to be chosen as exemplars. The number of
        exemplars, i.e. of clusters, is influenced by the input preferences
        value. If the preferences are not passed as arguments, they will be
        set to the median of the input similarities (resulting in a moderate
        number of clusters). For a smaller amount of clusters, this can be set
        to the minimum value of the similarities.

    convergence_iter : int, default=15
        Number of iterations with no change in the number
        of estimated clusters that stops the convergence.

    max_iter : int, default=200
        Maximum number of iterations.

    damping : float, default=0.5
        Damping factor between 0.5 and 1.

    copy : bool, default=True
        If copy is False, the affinity matrix is modified inplace by the
        algorithm, for memory efficiency.

    verbose : bool, default=False
        The verbosity level.

    return_n_iter : bool, default=False
        Whether or not to return the number of iterations.

    random_state : int, RandomState instance or None, default=None
        Pseudo-random number generator to control the starting state.
        Use an int for reproducible results across function calls.
        See the :term:`Glossary <random_state>`.

        .. versionadded:: 0.23
            this parameter was previously hardcoded as 0.

    Returns
    -------
    cluster_centers_indices : ndarray of shape (n_clusters,)
        Index of clusters centers.

    labels : ndarray of shape (n_samples,)
        Cluster labels for each point.

    n_iter : int
        Number of iterations run. Returned only if `return_n_iter` is
        set to True.

    Notes
    -----
    For an example, see :ref:`examples/cluster/plot_affinity_propagation.py
    <sphx_glr_auto_examples_cluster_plot_affinity_propagation.py>`.

    When the algorithm does not converge, it will still return a arrays of
    ``cluster_center_indices`` and labels if there are any exemplars/clusters,
    however they may be degenerate and should be used with caution.

    When all training samples have equal similarities and equal preferences,
    the assignment of cluster centers and labels depends on the preference.
    If the preference is smaller than the similarities, a single cluster center
    and label ``0`` for every sample will be returned. Otherwise, every
    training sample becomes its own cluster center and is assigned a unique
    label.

    References
    ----------
    Brendan J. Frey and Delbert Dueck, "Clustering by Passing Messages
    Between Data Points", Science Feb. 2007
    '''

class AffinityPropagation(ClusterMixin, BaseEstimator):
    '''Perform Affinity Propagation Clustering of data.

    Read more in the :ref:`User Guide <affinity_propagation>`.

    Parameters
    ----------
    damping : float, default=0.5
        Damping factor in the range `[0.5, 1.0)` is the extent to
        which the current value is maintained relative to
        incoming values (weighted 1 - damping). This in order
        to avoid numerical oscillations when updating these
        values (messages).

    max_iter : int, default=200
        Maximum number of iterations.

    convergence_iter : int, default=15
        Number of iterations with no change in the number
        of estimated clusters that stops the convergence.

    copy : bool, default=True
        Make a copy of input data.

    preference : array-like of shape (n_samples,) or float, default=None
        Preferences for each point - points with larger values of
        preferences are more likely to be chosen as exemplars. The number
        of exemplars, ie of clusters, is influenced by the input
        preferences value. If the preferences are not passed as arguments,
        they will be set to the median of the input similarities.

    affinity : {\'euclidean\', \'precomputed\'}, default=\'euclidean\'
        Which affinity to use. At the moment \'precomputed\' and
        ``euclidean`` are supported. \'euclidean\' uses the
        negative squared euclidean distance between points.

    verbose : bool, default=False
        Whether to be verbose.

    random_state : int, RandomState instance or None, default=None
        Pseudo-random number generator to control the starting state.
        Use an int for reproducible results across function calls.
        See the :term:`Glossary <random_state>`.

        .. versionadded:: 0.23
            this parameter was previously hardcoded as 0.

    Attributes
    ----------
    cluster_centers_indices_ : ndarray of shape (n_clusters,)
        Indices of cluster centers.

    cluster_centers_ : ndarray of shape (n_clusters, n_features)
        Cluster centers (if affinity != ``precomputed``).

    labels_ : ndarray of shape (n_samples,)
        Labels of each point.

    affinity_matrix_ : ndarray of shape (n_samples, n_samples)
        Stores the affinity matrix used in ``fit``.

    n_iter_ : int
        Number of iterations taken to converge.

    n_features_in_ : int
        Number of features seen during :term:`fit`.

        .. versionadded:: 0.24

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

        .. versionadded:: 1.0

    See Also
    --------
    AgglomerativeClustering : Recursively merges the pair of
        clusters that minimally increases a given linkage distance.
    FeatureAgglomeration : Similar to AgglomerativeClustering,
        but recursively merges features instead of samples.
    KMeans : K-Means clustering.
    MiniBatchKMeans : Mini-Batch K-Means clustering.
    MeanShift : Mean shift clustering using a flat kernel.
    SpectralClustering : Apply clustering to a projection
        of the normalized Laplacian.

    Notes
    -----
    For an example, see :ref:`examples/cluster/plot_affinity_propagation.py
    <sphx_glr_auto_examples_cluster_plot_affinity_propagation.py>`.

    The algorithmic complexity of affinity propagation is quadratic
    in the number of points.

    When the algorithm does not converge, it will still return a arrays of
    ``cluster_center_indices`` and labels if there are any exemplars/clusters,
    however they may be degenerate and should be used with caution.

    When ``fit`` does not converge, ``cluster_centers_`` is still populated
    however it may be degenerate. In such a case, proceed with caution.
    If ``fit`` does not converge and fails to produce any ``cluster_centers_``
    then ``predict`` will label every sample as ``-1``.

    When all training samples have equal similarities and equal preferences,
    the assignment of cluster centers and labels depends on the preference.
    If the preference is smaller than the similarities, ``fit`` will result in
    a single cluster center and label ``0`` for every sample. Otherwise, every
    training sample becomes its own cluster center and is assigned a unique
    label.

    References
    ----------

    Brendan J. Frey and Delbert Dueck, "Clustering by Passing Messages
    Between Data Points", Science Feb. 2007

    Examples
    --------
    >>> from sklearn.cluster import AffinityPropagation
    >>> import numpy as np
    >>> X = np.array([[1, 2], [1, 4], [1, 0],
    ...               [4, 2], [4, 4], [4, 0]])
    >>> clustering = AffinityPropagation(random_state=5).fit(X)
    >>> clustering
    AffinityPropagation(random_state=5)
    >>> clustering.labels_
    array([0, 0, 0, 1, 1, 1])
    >>> clustering.predict([[0, 0], [4, 4]])
    array([0, 1])
    >>> clustering.cluster_centers_
    array([[1, 2],
           [4, 2]])
    '''
    damping: Incomplete
    max_iter: Incomplete
    convergence_iter: Incomplete
    copy: Incomplete
    verbose: Incomplete
    preference: Incomplete
    affinity: Incomplete
    random_state: Incomplete
    def __init__(self, *, damping: float = 0.5, max_iter: int = 200, convergence_iter: int = 15, copy: bool = True, preference: Incomplete | None = None, affinity: str = 'euclidean', verbose: bool = False, random_state: Incomplete | None = None) -> None: ...
    affinity_matrix_: Incomplete
    cluster_centers_: Incomplete
    def fit(self, X, y: Incomplete | None = None):
        """Fit the clustering from features, or affinity matrix.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features), or                 array-like of shape (n_samples, n_samples)
            Training instances to cluster, or similarities / affinities between
            instances if ``affinity='precomputed'``. If a sparse feature matrix
            is provided, it will be converted into a sparse ``csr_matrix``.

        y : Ignored
            Not used, present here for API consistency by convention.

        Returns
        -------
        self
            Returns the instance itself.
        """
    def predict(self, X):
        """Predict the closest cluster each sample in X belongs to.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            New data to predict. If a sparse matrix is provided, it will be
            converted into a sparse ``csr_matrix``.

        Returns
        -------
        labels : ndarray of shape (n_samples,)
            Cluster labels.
        """
    def fit_predict(self, X, y: Incomplete | None = None):
        """Fit clustering from features/affinity matrix; return cluster labels.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features), or                 array-like of shape (n_samples, n_samples)
            Training instances to cluster, or similarities / affinities between
            instances if ``affinity='precomputed'``. If a sparse feature matrix
            is provided, it will be converted into a sparse ``csr_matrix``.

        y : Ignored
            Not used, present here for API consistency by convention.

        Returns
        -------
        labels : ndarray of shape (n_samples,)
            Cluster labels.
        """
