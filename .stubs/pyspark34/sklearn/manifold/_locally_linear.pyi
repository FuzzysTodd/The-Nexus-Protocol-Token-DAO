from ..base import BaseEstimator as BaseEstimator, ClassNamePrefixFeaturesOutMixin as ClassNamePrefixFeaturesOutMixin, TransformerMixin as TransformerMixin, _UnstableArchMixin
from ..neighbors import NearestNeighbors as NearestNeighbors
from ..utils import check_array as check_array, check_random_state as check_random_state
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from ..utils.extmath import stable_cumsum as stable_cumsum
from ..utils.validation import FLOAT_DTYPES as FLOAT_DTYPES, check_is_fitted as check_is_fitted
from _typeshed import Incomplete

def barycenter_weights(X, Y, indices, reg: float = 0.001):
    """Compute barycenter weights of X from Y along the first axis

    We estimate the weights to assign to each point in Y[indices] to recover
    the point X[i]. The barycenter weights sum to 1.

    Parameters
    ----------
    X : array-like, shape (n_samples, n_dim)

    Y : array-like, shape (n_samples, n_dim)

    indices : array-like, shape (n_samples, n_dim)
            Indices of the points in Y used to compute the barycenter

    reg : float, default=1e-3
        Amount of regularization to add for the problem to be
        well-posed in the case of n_neighbors > n_dim

    Returns
    -------
    B : array-like, shape (n_samples, n_neighbors)

    Notes
    -----
    See developers note for more information.
    """
def barycenter_kneighbors_graph(X, n_neighbors, reg: float = 0.001, n_jobs: Incomplete | None = None):
    """Computes the barycenter weighted graph of k-Neighbors for points in X

    Parameters
    ----------
    X : {array-like, NearestNeighbors}
        Sample data, shape = (n_samples, n_features), in the form of a
        numpy array or a NearestNeighbors object.

    n_neighbors : int
        Number of neighbors for each sample.

    reg : float, default=1e-3
        Amount of regularization when solving the least-squares
        problem. Only relevant if mode='barycenter'. If None, use the
        default.

    n_jobs : int or None, default=None
        The number of parallel jobs to run for neighbors search.
        ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
        ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
        for more details.

    Returns
    -------
    A : sparse matrix in CSR format, shape = [n_samples, n_samples]
        A[i, j] is assigned the weight of edge that connects i to j.

    See Also
    --------
    sklearn.neighbors.kneighbors_graph
    sklearn.neighbors.radius_neighbors_graph
    """
def null_space(M, k, k_skip: int = 1, eigen_solver: str = 'arpack', tol: float = 1e-06, max_iter: int = 100, random_state: Incomplete | None = None):
    """
    Find the null space of a matrix M.

    Parameters
    ----------
    M : {array, matrix, sparse matrix, LinearOperator}
        Input covariance matrix: should be symmetric positive semi-definite

    k : int
        Number of eigenvalues/vectors to return

    k_skip : int, default=1
        Number of low eigenvalues to skip.

    eigen_solver : {'auto', 'arpack', 'dense'}, default='arpack'
        auto : algorithm will attempt to choose the best method for input data
        arpack : use arnoldi iteration in shift-invert mode.
                    For this method, M may be a dense matrix, sparse matrix,
                    or general linear operator.
                    Warning: ARPACK can be unstable for some problems.  It is
                    best to try several random seeds in order to check results.
        dense  : use standard dense matrix operations for the eigenvalue
                    decomposition.  For this method, M must be an array
                    or matrix type.  This method should be avoided for
                    large problems.

    tol : float, default=1e-6
        Tolerance for 'arpack' method.
        Not used if eigen_solver=='dense'.

    max_iter : int, default=100
        Maximum number of iterations for 'arpack' method.
        Not used if eigen_solver=='dense'

    random_state : int, RandomState instance, default=None
        Determines the random number generator when ``solver`` == 'arpack'.
        Pass an int for reproducible results across multiple function calls.
        See :term:`Glossary <random_state>`.
    """
def locally_linear_embedding(X, *, n_neighbors, n_components, reg: float = 0.001, eigen_solver: str = 'auto', tol: float = 1e-06, max_iter: int = 100, method: str = 'standard', hessian_tol: float = 0.0001, modified_tol: float = 1e-12, random_state: Incomplete | None = None, n_jobs: Incomplete | None = None):
    """Perform a Locally Linear Embedding analysis on the data.

    Read more in the :ref:`User Guide <locally_linear_embedding>`.

    Parameters
    ----------
    X : {array-like, NearestNeighbors}
        Sample data, shape = (n_samples, n_features), in the form of a
        numpy array or a NearestNeighbors object.

    n_neighbors : int
        Number of neighbors to consider for each point.

    n_components : int
        Number of coordinates for the manifold.

    reg : float, default=1e-3
        Regularization constant, multiplies the trace of the local covariance
        matrix of the distances.

    eigen_solver : {'auto', 'arpack', 'dense'}, default='auto'
        auto : algorithm will attempt to choose the best method for input data

        arpack : use arnoldi iteration in shift-invert mode.
                    For this method, M may be a dense matrix, sparse matrix,
                    or general linear operator.
                    Warning: ARPACK can be unstable for some problems.  It is
                    best to try several random seeds in order to check results.

        dense  : use standard dense matrix operations for the eigenvalue
                    decomposition.  For this method, M must be an array
                    or matrix type.  This method should be avoided for
                    large problems.

    tol : float, default=1e-6
        Tolerance for 'arpack' method
        Not used if eigen_solver=='dense'.

    max_iter : int, default=100
        Maximum number of iterations for the arpack solver.

    method : {'standard', 'hessian', 'modified', 'ltsa'}, default='standard'
        standard : use the standard locally linear embedding algorithm.
                   see reference [1]_
        hessian  : use the Hessian eigenmap method.  This method requires
                   n_neighbors > n_components * (1 + (n_components + 1) / 2.
                   see reference [2]_
        modified : use the modified locally linear embedding algorithm.
                   see reference [3]_
        ltsa     : use local tangent space alignment algorithm
                   see reference [4]_

    hessian_tol : float, default=1e-4
        Tolerance for Hessian eigenmapping method.
        Only used if method == 'hessian'.

    modified_tol : float, default=1e-12
        Tolerance for modified LLE method.
        Only used if method == 'modified'.

    random_state : int, RandomState instance, default=None
        Determines the random number generator when ``solver`` == 'arpack'.
        Pass an int for reproducible results across multiple function calls.
        See :term:`Glossary <random_state>`.

    n_jobs : int or None, default=None
        The number of parallel jobs to run for neighbors search.
        ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
        ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
        for more details.

    Returns
    -------
    Y : array-like, shape [n_samples, n_components]
        Embedding vectors.

    squared_error : float
        Reconstruction error for the embedding vectors. Equivalent to
        ``norm(Y - W Y, 'fro')**2``, where W are the reconstruction weights.

    References
    ----------

    .. [1] Roweis, S. & Saul, L. Nonlinear dimensionality reduction
        by locally linear embedding.  Science 290:2323 (2000).
    .. [2] Donoho, D. & Grimes, C. Hessian eigenmaps: Locally
        linear embedding techniques for high-dimensional data.
        Proc Natl Acad Sci U S A.  100:5591 (2003).
    .. [3] `Zhang, Z. & Wang, J. MLLE: Modified Locally Linear
        Embedding Using Multiple Weights.
        <https://citeseerx.ist.psu.edu/doc_view/pid/0b060fdbd92cbcc66b383bcaa9ba5e5e624d7ee3>`_
    .. [4] Zhang, Z. & Zha, H. Principal manifolds and nonlinear
        dimensionality reduction via tangent space alignment.
        Journal of Shanghai Univ.  8:406 (2004)
    """

class LocallyLinearEmbedding(ClassNamePrefixFeaturesOutMixin, TransformerMixin, _UnstableArchMixin, BaseEstimator):
    """Locally Linear Embedding.

    Read more in the :ref:`User Guide <locally_linear_embedding>`.

    Parameters
    ----------
    n_neighbors : int, default=5
        Number of neighbors to consider for each point.

    n_components : int, default=2
        Number of coordinates for the manifold.

    reg : float, default=1e-3
        Regularization constant, multiplies the trace of the local covariance
        matrix of the distances.

    eigen_solver : {'auto', 'arpack', 'dense'}, default='auto'
        The solver used to compute the eigenvectors. The available options are:

        - `'auto'` : algorithm will attempt to choose the best method for input
          data.
        - `'arpack'` : use arnoldi iteration in shift-invert mode. For this
          method, M may be a dense matrix, sparse matrix, or general linear
          operator.
        - `'dense'`  : use standard dense matrix operations for the eigenvalue
          decomposition. For this method, M must be an array or matrix type.
          This method should be avoided for large problems.

        .. warning::
           ARPACK can be unstable for some problems.  It is best to try several
           random seeds in order to check results.

    tol : float, default=1e-6
        Tolerance for 'arpack' method
        Not used if eigen_solver=='dense'.

    max_iter : int, default=100
        Maximum number of iterations for the arpack solver.
        Not used if eigen_solver=='dense'.

    method : {'standard', 'hessian', 'modified', 'ltsa'}, default='standard'
        - `standard`: use the standard locally linear embedding algorithm. see
          reference [1]_
        - `hessian`: use the Hessian eigenmap method. This method requires
          ``n_neighbors > n_components * (1 + (n_components + 1) / 2``. see
          reference [2]_
        - `modified`: use the modified locally linear embedding algorithm.
          see reference [3]_
        - `ltsa`: use local tangent space alignment algorithm. see
          reference [4]_

    hessian_tol : float, default=1e-4
        Tolerance for Hessian eigenmapping method.
        Only used if ``method == 'hessian'``.

    modified_tol : float, default=1e-12
        Tolerance for modified LLE method.
        Only used if ``method == 'modified'``.

    neighbors_algorithm : {'auto', 'brute', 'kd_tree', 'ball_tree'},                           default='auto'
        Algorithm to use for nearest neighbors search, passed to
        :class:`~sklearn.neighbors.NearestNeighbors` instance.

    random_state : int, RandomState instance, default=None
        Determines the random number generator when
        ``eigen_solver`` == 'arpack'. Pass an int for reproducible results
        across multiple function calls. See :term:`Glossary <random_state>`.

    n_jobs : int or None, default=None
        The number of parallel jobs to run.
        ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
        ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
        for more details.

    Attributes
    ----------
    embedding_ : array-like, shape [n_samples, n_components]
        Stores the embedding vectors

    reconstruction_error_ : float
        Reconstruction error associated with `embedding_`

    n_features_in_ : int
        Number of features seen during :term:`fit`.

        .. versionadded:: 0.24

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

        .. versionadded:: 1.0

    nbrs_ : NearestNeighbors object
        Stores nearest neighbors instance, including BallTree or KDtree
        if applicable.

    See Also
    --------
    SpectralEmbedding : Spectral embedding for non-linear dimensionality
        reduction.
    TSNE : Distributed Stochastic Neighbor Embedding.

    References
    ----------

    .. [1] Roweis, S. & Saul, L. Nonlinear dimensionality reduction
        by locally linear embedding.  Science 290:2323 (2000).
    .. [2] Donoho, D. & Grimes, C. Hessian eigenmaps: Locally
        linear embedding techniques for high-dimensional data.
        Proc Natl Acad Sci U S A.  100:5591 (2003).
    .. [3] `Zhang, Z. & Wang, J. MLLE: Modified Locally Linear
        Embedding Using Multiple Weights.
        <https://citeseerx.ist.psu.edu/doc_view/pid/0b060fdbd92cbcc66b383bcaa9ba5e5e624d7ee3>`_
    .. [4] Zhang, Z. & Zha, H. Principal manifolds and nonlinear
        dimensionality reduction via tangent space alignment.
        Journal of Shanghai Univ.  8:406 (2004)

    Examples
    --------
    >>> from sklearn.datasets import load_digits
    >>> from sklearn.manifold import LocallyLinearEmbedding
    >>> X, _ = load_digits(return_X_y=True)
    >>> X.shape
    (1797, 64)
    >>> embedding = LocallyLinearEmbedding(n_components=2)
    >>> X_transformed = embedding.fit_transform(X[:100])
    >>> X_transformed.shape
    (100, 2)
    """
    n_neighbors: Incomplete
    n_components: Incomplete
    reg: Incomplete
    eigen_solver: Incomplete
    tol: Incomplete
    max_iter: Incomplete
    method: Incomplete
    hessian_tol: Incomplete
    modified_tol: Incomplete
    random_state: Incomplete
    neighbors_algorithm: Incomplete
    n_jobs: Incomplete
    def __init__(self, *, n_neighbors: int = 5, n_components: int = 2, reg: float = 0.001, eigen_solver: str = 'auto', tol: float = 1e-06, max_iter: int = 100, method: str = 'standard', hessian_tol: float = 0.0001, modified_tol: float = 1e-12, neighbors_algorithm: str = 'auto', random_state: Incomplete | None = None, n_jobs: Incomplete | None = None) -> None: ...
    def fit(self, X, y: Incomplete | None = None):
        """Compute the embedding vectors for data X.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Training set.

        y : Ignored
            Not used, present here for API consistency by convention.

        Returns
        -------
        self : object
            Fitted `LocallyLinearEmbedding` class instance.
        """
    def fit_transform(self, X, y: Incomplete | None = None):
        """Compute the embedding vectors for data X and transform X.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Training set.

        y : Ignored
            Not used, present here for API consistency by convention.

        Returns
        -------
        X_new : array-like, shape (n_samples, n_components)
            Returns the instance itself.
        """
    def transform(self, X):
        """
        Transform new points into embedding space.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Training set.

        Returns
        -------
        X_new : ndarray of shape (n_samples, n_components)
            Returns the instance itself.

        Notes
        -----
        Because of scaling performed by this method, it is discouraged to use
        it together with methods that are not scale-invariant (like SVMs).
        """
