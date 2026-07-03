from ...base import BaseEstimator as BaseEstimator, ClusterMixin as ClusterMixin
from ...metrics import pairwise_distances as pairwise_distances
from ...metrics._dist_metrics import DistanceMetric as DistanceMetric
from ...neighbors import BallTree as BallTree, KDTree as KDTree, NearestNeighbors as NearestNeighbors
from ...utils._param_validation import Interval as Interval, StrOptions as StrOptions
from ._linkage import MST_edge_dtype as MST_edge_dtype, make_single_linkage as make_single_linkage, mst_from_data_matrix as mst_from_data_matrix, mst_from_mutual_reachability as mst_from_mutual_reachability
from ._reachability import mutual_reachability_graph as mutual_reachability_graph
from ._tree import HIERARCHY_dtype as HIERARCHY_dtype, labelling_at_cut as labelling_at_cut, tree_to_labels as tree_to_labels
from _typeshed import Incomplete

FAST_METRICS: Incomplete

def remap_single_linkage_tree(tree, internal_to_raw, non_finite):
    """
    Takes an internal single_linkage_tree structure and adds back in a set of points
    that were initially detected as non-finite and returns that new tree.
    These points will all be merged into the final node at np.inf distance and
    considered noise points.

    Parameters
    ----------
    tree : ndarray of shape (n_samples - 1,), dtype=HIERARCHY_dtype
        The single-linkage tree tree (dendrogram) built from the MST.
    internal_to_raw: dict
        A mapping from internal integer index to the raw integer index
    non_finite : ndarray
        Boolean array of which entries in the raw data are non-finite
    """

class HDBSCAN(ClusterMixin, BaseEstimator):
    '''Cluster data using hierarchical density-based clustering.

    HDBSCAN - Hierarchical Density-Based Spatial Clustering of Applications
    with Noise. Performs :class:`~sklearn.cluster.DBSCAN` over varying epsilon
    values and integrates the result to find a clustering that gives the best
    stability over epsilon.
    This allows HDBSCAN to find clusters of varying densities (unlike
    :class:`~sklearn.cluster.DBSCAN`), and be more robust to parameter selection.
    Read more in the :ref:`User Guide <hdbscan>`.

    For an example of how to use HDBSCAN, as well as a comparison to
    :class:`~sklearn.cluster.DBSCAN`, please see the :ref:`plotting demo
    <sphx_glr_auto_examples_cluster_plot_hdbscan.py>`.

    .. versionadded:: 1.3

    Parameters
    ----------
    min_cluster_size : int, default=5
        The minimum number of samples in a group for that group to be
        considered a cluster; groupings smaller than this size will be left
        as noise.

    min_samples : int, default=None
        The number of samples in a neighborhood for a point
        to be considered as a core point. This includes the point itself.
        When `None`, defaults to `min_cluster_size`.

    cluster_selection_epsilon : float, default=0.0
        A distance threshold. Clusters below this value will be merged.
        See [5]_ for more information.

    max_cluster_size : int, default=None
        A limit to the size of clusters returned by the `"eom"` cluster
        selection algorithm. There is no limit when `max_cluster_size=None`.
        Has no effect if `cluster_selection_method="leaf"`.

    metric : str or callable, default=\'euclidean\'
        The metric to use when calculating distance between instances in a
        feature array.

        - If metric is a string or callable, it must be one of
          the options allowed by :func:`~sklearn.metrics.pairwise.pairwise_distances`
          for its metric parameter.

        - If metric is "precomputed", X is assumed to be a distance matrix and
          must be square.

    metric_params : dict, default=None
        Arguments passed to the distance metric.

    alpha : float, default=1.0
        A distance scaling parameter as used in robust single linkage.
        See [3]_ for more information.

    algorithm : {"auto", "brute", "kdtree", "balltree"}, default="auto"
        Exactly which algorithm to use for computing core distances; By default
        this is set to `"auto"` which attempts to use a
        :class:`~sklearn.neighbors.KDTree` tree if possible, otherwise it uses
        a :class:`~sklearn.neighbors.BallTree` tree. Both `"KDTree"` and
        `"BallTree"` algorithms use the
        :class:`~sklearn.neighbors.NearestNeighbors` estimator.

        If the `X` passed during `fit` is sparse or `metric` is invalid for
        both :class:`~sklearn.neighbors.KDTree` and
        :class:`~sklearn.neighbors.BallTree`, then it resolves to use the
        `"brute"` algorithm.

    leaf_size : int, default=40
        Leaf size for trees responsible for fast nearest neighbour queries when
        a KDTree or a BallTree are used as core-distance algorithms. A large
        dataset size and small `leaf_size` may induce excessive memory usage.
        If you are running out of memory consider increasing the `leaf_size`
        parameter. Ignored for `algorithm="brute"`.

    n_jobs : int, default=None
        Number of jobs to run in parallel to calculate distances.
        `None` means 1 unless in a :obj:`joblib.parallel_backend` context.
        `-1` means using all processors. See :term:`Glossary <n_jobs>`
        for more details.

    cluster_selection_method : {"eom", "leaf"}, default="eom"
        The method used to select clusters from the condensed tree. The
        standard approach for HDBSCAN* is to use an Excess of Mass (`"eom"`)
        algorithm to find the most persistent clusters. Alternatively you can
        instead select the clusters at the leaves of the tree -- this provides
        the most fine grained and homogeneous clusters.

    allow_single_cluster : bool, default=False
        By default HDBSCAN* will not produce a single cluster, setting this
        to True will override this and allow single cluster results in
        the case that you feel this is a valid result for your dataset.

    store_centers : str, default=None
        Which, if any, cluster centers to compute and store. The options are:

        - `None` which does not compute nor store any centers.
        - `"centroid"` which calculates the center by taking the weighted
          average of their positions. Note that the algorithm uses the
          euclidean metric and does not guarantee that the output will be
          an observed data point.
        - `"medoid"` which calculates the center by taking the point in the
          fitted data which minimizes the distance to all other points in
          the cluster. This is slower than "centroid" since it requires
          computing additional pairwise distances between points of the
          same cluster but guarantees the output is an observed data point.
          The medoid is also well-defined for arbitrary metrics, and does not
          depend on a euclidean metric.
        - `"both"` which computes and stores both forms of centers.

    copy : bool, default=False
        If `copy=True` then any time an in-place modifications would be made
        that would overwrite data passed to :term:`fit`, a copy will first be
        made, guaranteeing that the original data will be unchanged.
        Currently, it only applies when `metric="precomputed"`, when passing
        a dense array or a CSR sparse matrix and when `algorithm="brute"`.

    Attributes
    ----------
    labels_ : ndarray of shape (n_samples,)
        Cluster labels for each point in the dataset given to :term:`fit`.
        Outliers are labeled as follows:

        - Noisy samples are given the label -1.
        - Samples with infinite elements (+/- np.inf) are given the label -2.
        - Samples with missing data are given the label -3, even if they
          also have infinite elements.

    probabilities_ : ndarray of shape (n_samples,)
        The strength with which each sample is a member of its assigned
        cluster.

        - Clustered samples have probabilities proportional to the degree that
          they persist as part of the cluster.
        - Noisy samples have probability zero.
        - Samples with infinite elements (+/- np.inf) have probability 0.
        - Samples with missing data have probability `np.nan`.

    n_features_in_ : int
        Number of features seen during :term:`fit`.

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

    centroids_ : ndarray of shape (n_clusters, n_features)
        A collection containing the centroid of each cluster calculated under
        the standard euclidean metric. The centroids may fall "outside" their
        respective clusters if the clusters themselves are non-convex.

        Note that `n_clusters` only counts non-outlier clusters. That is to
        say, the `-1, -2, -3` labels for the outlier clusters are excluded.

    medoids_ : ndarray of shape (n_clusters, n_features)
        A collection containing the medoid of each cluster calculated under
        the whichever metric was passed to the `metric` parameter. The
        medoids are points in the original cluster which minimize the average
        distance to all other points in that cluster under the chosen metric.
        These can be thought of as the result of projecting the `metric`-based
        centroid back onto the cluster.

        Note that `n_clusters` only counts non-outlier clusters. That is to
        say, the `-1, -2, -3` labels for the outlier clusters are excluded.

    See Also
    --------
    DBSCAN : Density-Based Spatial Clustering of Applications
        with Noise.
    OPTICS : Ordering Points To Identify the Clustering Structure.
    Birch : Memory-efficient, online-learning algorithm.

    References
    ----------

    .. [1] :doi:`Campello, R. J., Moulavi, D., & Sander, J. Density-based clustering
      based on hierarchical density estimates.
      <10.1007/978-3-642-37456-2_14>`
    .. [2] :doi:`Campello, R. J., Moulavi, D., Zimek, A., & Sander, J.
       Hierarchical density estimates for data clustering, visualization,
       and outlier detection.<10.1145/2733381>`

    .. [3] `Chaudhuri, K., & Dasgupta, S. Rates of convergence for the
       cluster tree.
       <https://papers.nips.cc/paper/2010/hash/
       b534ba68236ba543ae44b22bd110a1d6-Abstract.html>`_

    .. [4] `Moulavi, D., Jaskowiak, P.A., Campello, R.J., Zimek, A. and
       Sander, J. Density-Based Clustering Validation.
       <https://www.dbs.ifi.lmu.de/~zimek/publications/SDM2014/DBCV.pdf>`_

    .. [5] :arxiv:`Malzer, C., & Baum, M. "A Hybrid Approach To Hierarchical
       Density-based Cluster Selection."<1911.02282>`.

    Examples
    --------
    >>> from sklearn.cluster import HDBSCAN
    >>> from sklearn.datasets import load_digits
    >>> X, _ = load_digits(return_X_y=True)
    >>> hdb = HDBSCAN(min_cluster_size=20)
    >>> hdb.fit(X)
    HDBSCAN(min_cluster_size=20)
    >>> hdb.labels_
    array([ 2,  6, -1, ..., -1, -1, -1])
    '''
    min_cluster_size: Incomplete
    min_samples: Incomplete
    alpha: Incomplete
    max_cluster_size: Incomplete
    cluster_selection_epsilon: Incomplete
    metric: Incomplete
    metric_params: Incomplete
    algorithm: Incomplete
    leaf_size: Incomplete
    n_jobs: Incomplete
    cluster_selection_method: Incomplete
    allow_single_cluster: Incomplete
    store_centers: Incomplete
    copy: Incomplete
    def __init__(self, min_cluster_size: int = 5, min_samples: Incomplete | None = None, cluster_selection_epsilon: float = 0.0, max_cluster_size: Incomplete | None = None, metric: str = 'euclidean', metric_params: Incomplete | None = None, alpha: float = 1.0, algorithm: str = 'auto', leaf_size: int = 40, n_jobs: Incomplete | None = None, cluster_selection_method: str = 'eom', allow_single_cluster: bool = False, store_centers: Incomplete | None = None, copy: bool = False) -> None: ...
    labels_: Incomplete
    probabilities_: Incomplete
    def fit(self, X, y: Incomplete | None = None):
        """Find clusters based on hierarchical density-based clustering.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features), or                 ndarray of shape (n_samples, n_samples)
            A feature array, or array of distances between samples if
            `metric='precomputed'`.

        y : None
            Ignored.

        Returns
        -------
        self : object
            Returns self.
        """
    def fit_predict(self, X, y: Incomplete | None = None):
        """Cluster X and return the associated cluster labels.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features), or                 ndarray of shape (n_samples, n_samples)
            A feature array, or array of distances between samples if
            `metric='precomputed'`.

        y : None
            Ignored.

        Returns
        -------
        y : ndarray of shape (n_samples,)
            Cluster labels.
        """
    def dbscan_clustering(self, cut_distance, min_cluster_size: int = 5):
        """Return clustering given by DBSCAN without border points.

        Return clustering that would be equivalent to running DBSCAN* for a
        particular cut_distance (or epsilon) DBSCAN* can be thought of as
        DBSCAN without the border points.  As such these results may differ
        slightly from `cluster.DBSCAN` due to the difference in implementation
        over the non-core points.

        This can also be thought of as a flat clustering derived from constant
        height cut through the single linkage tree.

        This represents the result of selecting a cut value for robust single linkage
        clustering. The `min_cluster_size` allows the flat clustering to declare noise
        points (and cluster smaller than `min_cluster_size`).

        Parameters
        ----------
        cut_distance : float
            The mutual reachability distance cut value to use to generate a
            flat clustering.

        min_cluster_size : int, default=5
            Clusters smaller than this value with be called 'noise' and remain
            unclustered in the resulting flat clustering.

        Returns
        -------
        labels : ndarray of shape (n_samples,)
            An array of cluster labels, one per datapoint.
            Outliers are labeled as follows:

            - Noisy samples are given the label -1.
            - Samples with infinite elements (+/- np.inf) are given the label -2.
            - Samples with missing data are given the label -3, even if they
              also have infinite elements.
        """
