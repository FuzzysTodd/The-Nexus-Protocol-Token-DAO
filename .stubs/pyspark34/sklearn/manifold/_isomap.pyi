from ..base import BaseEstimator as BaseEstimator, ClassNamePrefixFeaturesOutMixin as ClassNamePrefixFeaturesOutMixin, TransformerMixin as TransformerMixin
from ..decomposition import KernelPCA as KernelPCA
from ..neighbors import NearestNeighbors as NearestNeighbors, kneighbors_graph as kneighbors_graph, radius_neighbors_graph as radius_neighbors_graph
from ..preprocessing import KernelCenterer as KernelCenterer
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from ..utils.validation import check_is_fitted as check_is_fitted
from _typeshed import Incomplete

class Isomap(ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):
    '''Isomap Embedding.

    Non-linear dimensionality reduction through Isometric Mapping

    Read more in the :ref:`User Guide <isomap>`.

    Parameters
    ----------
    n_neighbors : int or None, default=5
        Number of neighbors to consider for each point. If `n_neighbors` is an int,
        then `radius` must be `None`.

    radius : float or None, default=None
        Limiting distance of neighbors to return. If `radius` is a float,
        then `n_neighbors` must be set to `None`.

        .. versionadded:: 1.1

    n_components : int, default=2
        Number of coordinates for the manifold.

    eigen_solver : {\'auto\', \'arpack\', \'dense\'}, default=\'auto\'
        \'auto\' : Attempt to choose the most efficient solver
        for the given problem.

        \'arpack\' : Use Arnoldi decomposition to find the eigenvalues
        and eigenvectors.

        \'dense\' : Use a direct solver (i.e. LAPACK)
        for the eigenvalue decomposition.

    tol : float, default=0
        Convergence tolerance passed to arpack or lobpcg.
        not used if eigen_solver == \'dense\'.

    max_iter : int, default=None
        Maximum number of iterations for the arpack solver.
        not used if eigen_solver == \'dense\'.

    path_method : {\'auto\', \'FW\', \'D\'}, default=\'auto\'
        Method to use in finding shortest path.

        \'auto\' : attempt to choose the best algorithm automatically.

        \'FW\' : Floyd-Warshall algorithm.

        \'D\' : Dijkstra\'s algorithm.

    neighbors_algorithm : {\'auto\', \'brute\', \'kd_tree\', \'ball_tree\'},                           default=\'auto\'
        Algorithm to use for nearest neighbors search,
        passed to neighbors.NearestNeighbors instance.

    n_jobs : int or None, default=None
        The number of parallel jobs to run.
        ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
        ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
        for more details.

    metric : str, or callable, default="minkowski"
        The metric to use when calculating distance between instances in a
        feature array. If metric is a string or callable, it must be one of
        the options allowed by :func:`sklearn.metrics.pairwise_distances` for
        its metric parameter.
        If metric is "precomputed", X is assumed to be a distance matrix and
        must be square. X may be a :term:`Glossary <sparse graph>`.

        .. versionadded:: 0.22

    p : int, default=2
        Parameter for the Minkowski metric from
        sklearn.metrics.pairwise.pairwise_distances. When p = 1, this is
        equivalent to using manhattan_distance (l1), and euclidean_distance
        (l2) for p = 2. For arbitrary p, minkowski_distance (l_p) is used.

        .. versionadded:: 0.22

    metric_params : dict, default=None
        Additional keyword arguments for the metric function.

        .. versionadded:: 0.22

    Attributes
    ----------
    embedding_ : array-like, shape (n_samples, n_components)
        Stores the embedding vectors.

    kernel_pca_ : object
        :class:`~sklearn.decomposition.KernelPCA` object used to implement the
        embedding.

    nbrs_ : sklearn.neighbors.NearestNeighbors instance
        Stores nearest neighbors instance, including BallTree or KDtree
        if applicable.

    dist_matrix_ : array-like, shape (n_samples, n_samples)
        Stores the geodesic distance matrix of training data.

    n_features_in_ : int
        Number of features seen during :term:`fit`.

        .. versionadded:: 0.24

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

        .. versionadded:: 1.0

    See Also
    --------
    sklearn.decomposition.PCA : Principal component analysis that is a linear
        dimensionality reduction method.
    sklearn.decomposition.KernelPCA : Non-linear dimensionality reduction using
        kernels and PCA.
    MDS : Manifold learning using multidimensional scaling.
    TSNE : T-distributed Stochastic Neighbor Embedding.
    LocallyLinearEmbedding : Manifold learning using Locally Linear Embedding.
    SpectralEmbedding : Spectral embedding for non-linear dimensionality.

    References
    ----------

    .. [1] Tenenbaum, J.B.; De Silva, V.; & Langford, J.C. A global geometric
           framework for nonlinear dimensionality reduction. Science 290 (5500)

    Examples
    --------
    >>> from sklearn.datasets import load_digits
    >>> from sklearn.manifold import Isomap
    >>> X, _ = load_digits(return_X_y=True)
    >>> X.shape
    (1797, 64)
    >>> embedding = Isomap(n_components=2)
    >>> X_transformed = embedding.fit_transform(X[:100])
    >>> X_transformed.shape
    (100, 2)
    '''
    n_neighbors: Incomplete
    radius: Incomplete
    n_components: Incomplete
    eigen_solver: Incomplete
    tol: Incomplete
    max_iter: Incomplete
    path_method: Incomplete
    neighbors_algorithm: Incomplete
    n_jobs: Incomplete
    metric: Incomplete
    p: Incomplete
    metric_params: Incomplete
    def __init__(self, *, n_neighbors: int = 5, radius: Incomplete | None = None, n_components: int = 2, eigen_solver: str = 'auto', tol: int = 0, max_iter: Incomplete | None = None, path_method: str = 'auto', neighbors_algorithm: str = 'auto', n_jobs: Incomplete | None = None, metric: str = 'minkowski', p: int = 2, metric_params: Incomplete | None = None) -> None: ...
    def reconstruction_error(self):
        """Compute the reconstruction error for the embedding.

        Returns
        -------
        reconstruction_error : float
            Reconstruction error.

        Notes
        -----
        The cost function of an isomap embedding is

        ``E = frobenius_norm[K(D) - K(D_fit)] / n_samples``

        Where D is the matrix of distances for the input data X,
        D_fit is the matrix of distances for the output embedding X_fit,
        and K is the isomap kernel:

        ``K(D) = -0.5 * (I - 1/n_samples) * D^2 * (I - 1/n_samples)``
        """
    def fit(self, X, y: Incomplete | None = None):
        """Compute the embedding vectors for data X.

        Parameters
        ----------
        X : {array-like, sparse matrix, BallTree, KDTree, NearestNeighbors}
            Sample data, shape = (n_samples, n_features), in the form of a
            numpy array, sparse matrix, precomputed tree, or NearestNeighbors
            object.

        y : Ignored
            Not used, present for API consistency by convention.

        Returns
        -------
        self : object
            Returns a fitted instance of self.
        """
    def fit_transform(self, X, y: Incomplete | None = None):
        """Fit the model from data in X and transform X.

        Parameters
        ----------
        X : {array-like, sparse matrix, BallTree, KDTree}
            Training vector, where `n_samples` is the number of samples
            and `n_features` is the number of features.

        y : Ignored
            Not used, present for API consistency by convention.

        Returns
        -------
        X_new : array-like, shape (n_samples, n_components)
            X transformed in the new space.
        """
    def transform(self, X):
        """Transform X.

        This is implemented by linking the points X into the graph of geodesic
        distances of the training data. First the `n_neighbors` nearest
        neighbors of X are found in the training data, and from these the
        shortest geodesic distances from each point in X to each point in
        the training data are computed in order to construct the kernel.
        The embedding of X is the projection of this kernel onto the
        embedding vectors of the training set.

        Parameters
        ----------
        X : {array-like, sparse matrix}, shape (n_queries, n_features)
            If neighbors_algorithm='precomputed', X is assumed to be a
            distance matrix or a sparse graph of shape
            (n_queries, n_samples_fit).

        Returns
        -------
        X_new : array-like, shape (n_queries, n_components)
            X transformed in the new space.
        """
