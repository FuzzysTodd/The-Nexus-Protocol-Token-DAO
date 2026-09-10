from ..base import BaseEstimator as BaseEstimator
from ..metrics.pairwise import rbf_kernel as rbf_kernel
from ..neighbors import NearestNeighbors as NearestNeighbors, kneighbors_graph as kneighbors_graph
from ..utils import check_array as check_array, check_random_state as check_random_state, check_symmetric as check_symmetric
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from _typeshed import Incomplete

def spectral_embedding(adjacency, *, n_components: int = 8, eigen_solver: Incomplete | None = None, random_state: Incomplete | None = None, eigen_tol: str = 'auto', norm_laplacian: bool = True, drop_first: bool = True):
    '''Project the sample on the first eigenvectors of the graph Laplacian.

    The adjacency matrix is used to compute a normalized graph Laplacian
    whose spectrum (especially the eigenvectors associated to the
    smallest eigenvalues) has an interpretation in terms of minimal
    number of cuts necessary to split the graph into comparably sized
    components.

    This embedding can also \'work\' even if the ``adjacency`` variable is
    not strictly the adjacency matrix of a graph but more generally
    an affinity or similarity matrix between samples (for instance the
    heat kernel of a euclidean distance matrix or a k-NN matrix).

    However care must taken to always make the affinity matrix symmetric
    so that the eigenvector decomposition works as expected.

    Note : Laplacian Eigenmaps is the actual algorithm implemented here.

    Read more in the :ref:`User Guide <spectral_embedding>`.

    Parameters
    ----------
    adjacency : {array-like, sparse graph} of shape (n_samples, n_samples)
        The adjacency matrix of the graph to embed.

    n_components : int, default=8
        The dimension of the projection subspace.

    eigen_solver : {\'arpack\', \'lobpcg\', \'amg\'}, default=None
        The eigenvalue decomposition strategy to use. AMG requires pyamg
        to be installed. It can be faster on very large, sparse problems,
        but may also lead to instabilities. If None, then ``\'arpack\'`` is
        used.

    random_state : int, RandomState instance or None, default=None
        A pseudo random number generator used for the initialization
        of the lobpcg eigen vectors decomposition when `eigen_solver ==
        \'amg\'`, and for the K-Means initialization. Use an int to make
        the results deterministic across calls (See
        :term:`Glossary <random_state>`).

        .. note::
            When using `eigen_solver == \'amg\'`,
            it is necessary to also fix the global numpy seed with
            `np.random.seed(int)` to get deterministic results. See
            https://github.com/pyamg/pyamg/issues/139 for further
            information.

    eigen_tol : float, default="auto"
        Stopping criterion for eigendecomposition of the Laplacian matrix.
        If `eigen_tol="auto"` then the passed tolerance will depend on the
        `eigen_solver`:

        - If `eigen_solver="arpack"`, then `eigen_tol=0.0`;
        - If `eigen_solver="lobpcg"` or `eigen_solver="amg"`, then
          `eigen_tol=None` which configures the underlying `lobpcg` solver to
          automatically resolve the value according to their heuristics. See,
          :func:`scipy.sparse.linalg.lobpcg` for details.

        Note that when using `eigen_solver="amg"` values of `tol<1e-5` may lead
        to convergence issues and should be avoided.

        .. versionadded:: 1.2
           Added \'auto\' option.

    norm_laplacian : bool, default=True
        If True, then compute symmetric normalized Laplacian.

    drop_first : bool, default=True
        Whether to drop the first eigenvector. For spectral embedding, this
        should be True as the first eigenvector should be constant vector for
        connected graph, but for spectral clustering, this should be kept as
        False to retain the first eigenvector.

    Returns
    -------
    embedding : ndarray of shape (n_samples, n_components)
        The reduced samples.

    Notes
    -----
    Spectral Embedding (Laplacian Eigenmaps) is most useful when the graph
    has one connected component. If there graph has many components, the first
    few eigenvectors will simply uncover the connected components of the graph.

    References
    ----------
    * https://en.wikipedia.org/wiki/LOBPCG

    * :doi:`"Toward the Optimal Preconditioned Eigensolver: Locally Optimal
      Block Preconditioned Conjugate Gradient Method",
      Andrew V. Knyazev
      <10.1137/S1064827500366124>`
    '''

class SpectralEmbedding(BaseEstimator):
    '''Spectral embedding for non-linear dimensionality reduction.

    Forms an affinity matrix given by the specified function and
    applies spectral decomposition to the corresponding graph laplacian.
    The resulting transformation is given by the value of the
    eigenvectors for each data point.

    Note : Laplacian Eigenmaps is the actual algorithm implemented here.

    Read more in the :ref:`User Guide <spectral_embedding>`.

    Parameters
    ----------
    n_components : int, default=2
        The dimension of the projected subspace.

    affinity : {\'nearest_neighbors\', \'rbf\', \'precomputed\',                 \'precomputed_nearest_neighbors\'} or callable,                 default=\'nearest_neighbors\'
        How to construct the affinity matrix.
         - \'nearest_neighbors\' : construct the affinity matrix by computing a
           graph of nearest neighbors.
         - \'rbf\' : construct the affinity matrix by computing a radial basis
           function (RBF) kernel.
         - \'precomputed\' : interpret ``X`` as a precomputed affinity matrix.
         - \'precomputed_nearest_neighbors\' : interpret ``X`` as a sparse graph
           of precomputed nearest neighbors, and constructs the affinity matrix
           by selecting the ``n_neighbors`` nearest neighbors.
         - callable : use passed in function as affinity
           the function takes in data matrix (n_samples, n_features)
           and return affinity matrix (n_samples, n_samples).

    gamma : float, default=None
        Kernel coefficient for rbf kernel. If None, gamma will be set to
        1/n_features.

    random_state : int, RandomState instance or None, default=None
        A pseudo random number generator used for the initialization
        of the lobpcg eigen vectors decomposition when `eigen_solver ==
        \'amg\'`, and for the K-Means initialization. Use an int to make
        the results deterministic across calls (See
        :term:`Glossary <random_state>`).

        .. note::
            When using `eigen_solver == \'amg\'`,
            it is necessary to also fix the global numpy seed with
            `np.random.seed(int)` to get deterministic results. See
            https://github.com/pyamg/pyamg/issues/139 for further
            information.

    eigen_solver : {\'arpack\', \'lobpcg\', \'amg\'}, default=None
        The eigenvalue decomposition strategy to use. AMG requires pyamg
        to be installed. It can be faster on very large, sparse problems.
        If None, then ``\'arpack\'`` is used.

    eigen_tol : float, default="auto"
        Stopping criterion for eigendecomposition of the Laplacian matrix.
        If `eigen_tol="auto"` then the passed tolerance will depend on the
        `eigen_solver`:

        - If `eigen_solver="arpack"`, then `eigen_tol=0.0`;
        - If `eigen_solver="lobpcg"` or `eigen_solver="amg"`, then
          `eigen_tol=None` which configures the underlying `lobpcg` solver to
          automatically resolve the value according to their heuristics. See,
          :func:`scipy.sparse.linalg.lobpcg` for details.

        Note that when using `eigen_solver="lobpcg"` or `eigen_solver="amg"`
        values of `tol<1e-5` may lead to convergence issues and should be
        avoided.

        .. versionadded:: 1.2

    n_neighbors : int, default=None
        Number of nearest neighbors for nearest_neighbors graph building.
        If None, n_neighbors will be set to max(n_samples/10, 1).

    n_jobs : int, default=None
        The number of parallel jobs to run.
        ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
        ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
        for more details.

    Attributes
    ----------
    embedding_ : ndarray of shape (n_samples, n_components)
        Spectral embedding of the training matrix.

    affinity_matrix_ : ndarray of shape (n_samples, n_samples)
        Affinity_matrix constructed from samples or precomputed.

    n_features_in_ : int
        Number of features seen during :term:`fit`.

        .. versionadded:: 0.24

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

        .. versionadded:: 1.0

    n_neighbors_ : int
        Number of nearest neighbors effectively used.

    See Also
    --------
    Isomap : Non-linear dimensionality reduction through Isometric Mapping.

    References
    ----------

    - :doi:`A Tutorial on Spectral Clustering, 2007
      Ulrike von Luxburg
      <10.1007/s11222-007-9033-z>`

    - `On Spectral Clustering: Analysis and an algorithm, 2001
      Andrew Y. Ng, Michael I. Jordan, Yair Weiss
      <https://citeseerx.ist.psu.edu/doc_view/pid/796c5d6336fc52aa84db575fb821c78918b65f58>`_

    - :doi:`Normalized cuts and image segmentation, 2000
      Jianbo Shi, Jitendra Malik
      <10.1109/34.868688>`

    Examples
    --------
    >>> from sklearn.datasets import load_digits
    >>> from sklearn.manifold import SpectralEmbedding
    >>> X, _ = load_digits(return_X_y=True)
    >>> X.shape
    (1797, 64)
    >>> embedding = SpectralEmbedding(n_components=2)
    >>> X_transformed = embedding.fit_transform(X[:100])
    >>> X_transformed.shape
    (100, 2)
    '''
    n_components: Incomplete
    affinity: Incomplete
    gamma: Incomplete
    random_state: Incomplete
    eigen_solver: Incomplete
    eigen_tol: Incomplete
    n_neighbors: Incomplete
    n_jobs: Incomplete
    def __init__(self, n_components: int = 2, *, affinity: str = 'nearest_neighbors', gamma: Incomplete | None = None, random_state: Incomplete | None = None, eigen_solver: Incomplete | None = None, eigen_tol: str = 'auto', n_neighbors: Incomplete | None = None, n_jobs: Incomplete | None = None) -> None: ...
    embedding_: Incomplete
    def fit(self, X, y: Incomplete | None = None):
        '''Fit the model from data in X.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            Training vector, where `n_samples` is the number of samples
            and `n_features` is the number of features.

            If affinity is "precomputed"
            X : {array-like, sparse matrix}, shape (n_samples, n_samples),
            Interpret X as precomputed adjacency graph computed from
            samples.

        y : Ignored
            Not used, present for API consistency by convention.

        Returns
        -------
        self : object
            Returns the instance itself.
        '''
    def fit_transform(self, X, y: Incomplete | None = None):
        '''Fit the model from data in X and transform X.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            Training vector, where `n_samples` is the number of samples
            and `n_features` is the number of features.

            If affinity is "precomputed"
            X : {array-like, sparse matrix} of shape (n_samples, n_samples),
            Interpret X as precomputed adjacency graph computed from
            samples.

        y : Ignored
            Not used, present for API consistency by convention.

        Returns
        -------
        X_new : array-like of shape (n_samples, n_components)
            Spectral embedding of the training matrix.
        '''
