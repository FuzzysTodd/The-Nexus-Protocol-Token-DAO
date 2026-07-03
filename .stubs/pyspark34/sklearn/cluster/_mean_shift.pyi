from .._config import config_context as config_context
from ..base import BaseEstimator as BaseEstimator, ClusterMixin as ClusterMixin
from ..metrics.pairwise import pairwise_distances_argmin as pairwise_distances_argmin
from ..neighbors import NearestNeighbors as NearestNeighbors
from ..utils import check_array as check_array, check_random_state as check_random_state, gen_batches as gen_batches
from ..utils._param_validation import Interval as Interval, validate_params as validate_params
from ..utils.parallel import Parallel as Parallel, delayed as delayed
from ..utils.validation import check_is_fitted as check_is_fitted
from _typeshed import Incomplete

def estimate_bandwidth(X, *, quantile: float = 0.3, n_samples: Incomplete | None = None, random_state: int = 0, n_jobs: Incomplete | None = None):
    """Estimate the bandwidth to use with the mean-shift algorithm.

    This function takes time at least quadratic in `n_samples`. For large
    datasets, it is wise to subsample by setting `n_samples`. Alternatively,
    the parameter `bandwidth` can be set to a small value without estimating
    it.

    Parameters
    ----------
    X : array-like of shape (n_samples, n_features)
        Input points.

    quantile : float, default=0.3
        Should be between [0, 1]
        0.5 means that the median of all pairwise distances is used.

    n_samples : int, default=None
        The number of samples to use. If not given, all samples are used.

    random_state : int, RandomState instance, default=None
        The generator used to randomly select the samples from input points
        for bandwidth estimation. Use an int to make the randomness
        deterministic.
        See :term:`Glossary <random_state>`.

    n_jobs : int, default=None
        The number of parallel jobs to run for neighbors search.
        ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
        ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
        for more details.

    Returns
    -------
    bandwidth : float
        The bandwidth parameter.
    """
def mean_shift(X, *, bandwidth: Incomplete | None = None, seeds: Incomplete | None = None, bin_seeding: bool = False, min_bin_freq: int = 1, cluster_all: bool = True, max_iter: int = 300, n_jobs: Incomplete | None = None):
    """Perform mean shift clustering of data using a flat kernel.

    Read more in the :ref:`User Guide <mean_shift>`.

    Parameters
    ----------

    X : array-like of shape (n_samples, n_features)
        Input data.

    bandwidth : float, default=None
        Kernel bandwidth. If not None, must be in the range [0, +inf).

        If None, the bandwidth is determined using a heuristic based on
        the median of all pairwise distances. This will take quadratic time in
        the number of samples. The sklearn.cluster.estimate_bandwidth function
        can be used to do this more efficiently.

    seeds : array-like of shape (n_seeds, n_features) or None
        Point used as initial kernel locations. If None and bin_seeding=False,
        each data point is used as a seed. If None and bin_seeding=True,
        see bin_seeding.

    bin_seeding : bool, default=False
        If true, initial kernel locations are not locations of all
        points, but rather the location of the discretized version of
        points, where points are binned onto a grid whose coarseness
        corresponds to the bandwidth. Setting this option to True will speed
        up the algorithm because fewer seeds will be initialized.
        Ignored if seeds argument is not None.

    min_bin_freq : int, default=1
       To speed up the algorithm, accept only those bins with at least
       min_bin_freq points as seeds.

    cluster_all : bool, default=True
        If true, then all points are clustered, even those orphans that are
        not within any kernel. Orphans are assigned to the nearest kernel.
        If false, then orphans are given cluster label -1.

    max_iter : int, default=300
        Maximum number of iterations, per seed point before the clustering
        operation terminates (for that seed point), if has not converged yet.

    n_jobs : int, default=None
        The number of jobs to use for the computation. The following tasks benefit
        from the parallelization:

        - The search of nearest neighbors for bandwidth estimation and label
          assignments. See the details in the docstring of the
          ``NearestNeighbors`` class.
        - Hill-climbing optimization for all seeds.

        See :term:`Glossary <n_jobs>` for more details.

        ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
        ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
        for more details.

        .. versionadded:: 0.17
           Parallel Execution using *n_jobs*.

    Returns
    -------

    cluster_centers : ndarray of shape (n_clusters, n_features)
        Coordinates of cluster centers.

    labels : ndarray of shape (n_samples,)
        Cluster labels for each point.

    Notes
    -----
    For an example, see :ref:`examples/cluster/plot_mean_shift.py
    <sphx_glr_auto_examples_cluster_plot_mean_shift.py>`.
    """
def get_bin_seeds(X, bin_size, min_bin_freq: int = 1):
    """Find seeds for mean_shift.

    Finds seeds by first binning data onto a grid whose lines are
    spaced bin_size apart, and then choosing those bins with at least
    min_bin_freq points.

    Parameters
    ----------

    X : array-like of shape (n_samples, n_features)
        Input points, the same points that will be used in mean_shift.

    bin_size : float
        Controls the coarseness of the binning. Smaller values lead
        to more seeding (which is computationally more expensive). If you're
        not sure how to set this, set it to the value of the bandwidth used
        in clustering.mean_shift.

    min_bin_freq : int, default=1
        Only bins with at least min_bin_freq will be selected as seeds.
        Raising this value decreases the number of seeds found, which
        makes mean_shift computationally cheaper.

    Returns
    -------
    bin_seeds : array-like of shape (n_samples, n_features)
        Points used as initial kernel positions in clustering.mean_shift.
    """

class MeanShift(ClusterMixin, BaseEstimator):
    '''Mean shift clustering using a flat kernel.

    Mean shift clustering aims to discover "blobs" in a smooth density of
    samples. It is a centroid-based algorithm, which works by updating
    candidates for centroids to be the mean of the points within a given
    region. These candidates are then filtered in a post-processing stage to
    eliminate near-duplicates to form the final set of centroids.

    Seeding is performed using a binning technique for scalability.

    Read more in the :ref:`User Guide <mean_shift>`.

    Parameters
    ----------
    bandwidth : float, default=None
        Bandwidth used in the flat kernel.

        If not given, the bandwidth is estimated using
        sklearn.cluster.estimate_bandwidth; see the documentation for that
        function for hints on scalability (see also the Notes, below).

    seeds : array-like of shape (n_samples, n_features), default=None
        Seeds used to initialize kernels. If not set,
        the seeds are calculated by clustering.get_bin_seeds
        with bandwidth as the grid size and default values for
        other parameters.

    bin_seeding : bool, default=False
        If true, initial kernel locations are not locations of all
        points, but rather the location of the discretized version of
        points, where points are binned onto a grid whose coarseness
        corresponds to the bandwidth. Setting this option to True will speed
        up the algorithm because fewer seeds will be initialized.
        The default value is False.
        Ignored if seeds argument is not None.

    min_bin_freq : int, default=1
       To speed up the algorithm, accept only those bins with at least
       min_bin_freq points as seeds.

    cluster_all : bool, default=True
        If true, then all points are clustered, even those orphans that are
        not within any kernel. Orphans are assigned to the nearest kernel.
        If false, then orphans are given cluster label -1.

    n_jobs : int, default=None
        The number of jobs to use for the computation. The following tasks benefit
        from the parallelization:

        - The search of nearest neighbors for bandwidth estimation and label
          assignments. See the details in the docstring of the
          ``NearestNeighbors`` class.
        - Hill-climbing optimization for all seeds.

        See :term:`Glossary <n_jobs>` for more details.

        ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
        ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
        for more details.

    max_iter : int, default=300
        Maximum number of iterations, per seed point before the clustering
        operation terminates (for that seed point), if has not converged yet.

        .. versionadded:: 0.22

    Attributes
    ----------
    cluster_centers_ : ndarray of shape (n_clusters, n_features)
        Coordinates of cluster centers.

    labels_ : ndarray of shape (n_samples,)
        Labels of each point.

    n_iter_ : int
        Maximum number of iterations performed on each seed.

        .. versionadded:: 0.22

    n_features_in_ : int
        Number of features seen during :term:`fit`.

        .. versionadded:: 0.24

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

        .. versionadded:: 1.0

    See Also
    --------
    KMeans : K-Means clustering.

    Notes
    -----

    Scalability:

    Because this implementation uses a flat kernel and
    a Ball Tree to look up members of each kernel, the complexity will tend
    towards O(T*n*log(n)) in lower dimensions, with n the number of samples
    and T the number of points. In higher dimensions the complexity will
    tend towards O(T*n^2).

    Scalability can be boosted by using fewer seeds, for example by using
    a higher value of min_bin_freq in the get_bin_seeds function.

    Note that the estimate_bandwidth function is much less scalable than the
    mean shift algorithm and will be the bottleneck if it is used.

    References
    ----------

    Dorin Comaniciu and Peter Meer, "Mean Shift: A robust approach toward
    feature space analysis". IEEE Transactions on Pattern Analysis and
    Machine Intelligence. 2002. pp. 603-619.

    Examples
    --------
    >>> from sklearn.cluster import MeanShift
    >>> import numpy as np
    >>> X = np.array([[1, 1], [2, 1], [1, 0],
    ...               [4, 7], [3, 5], [3, 6]])
    >>> clustering = MeanShift(bandwidth=2).fit(X)
    >>> clustering.labels_
    array([1, 1, 1, 0, 0, 0])
    >>> clustering.predict([[0, 0], [5, 5]])
    array([1, 0])
    >>> clustering
    MeanShift(bandwidth=2)
    '''
    bandwidth: Incomplete
    seeds: Incomplete
    bin_seeding: Incomplete
    cluster_all: Incomplete
    min_bin_freq: Incomplete
    n_jobs: Incomplete
    max_iter: Incomplete
    def __init__(self, *, bandwidth: Incomplete | None = None, seeds: Incomplete | None = None, bin_seeding: bool = False, min_bin_freq: int = 1, cluster_all: bool = True, n_jobs: Incomplete | None = None, max_iter: int = 300) -> None: ...
    n_iter_: Incomplete
    def fit(self, X, y: Incomplete | None = None):
        """Perform clustering.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Samples to cluster.

        y : Ignored
            Not used, present for API consistency by convention.

        Returns
        -------
        self : object
               Fitted instance.
        """
    def predict(self, X):
        """Predict the closest cluster each sample in X belongs to.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            New data to predict.

        Returns
        -------
        labels : ndarray of shape (n_samples,)
            Index of the cluster each sample belongs to.
        """
