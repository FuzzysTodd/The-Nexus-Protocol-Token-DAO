from ..base import BaseEstimator as BaseEstimator
from ..isotonic import IsotonicRegression as IsotonicRegression
from ..metrics import euclidean_distances as euclidean_distances
from ..utils import check_array as check_array, check_random_state as check_random_state, check_symmetric as check_symmetric
from ..utils._param_validation import Hidden as Hidden, Interval as Interval, StrOptions as StrOptions
from ..utils.parallel import Parallel as Parallel, delayed as delayed
from _typeshed import Incomplete

def smacof(dissimilarities, *, metric: bool = True, n_components: int = 2, init: Incomplete | None = None, n_init: int = 8, n_jobs: Incomplete | None = None, max_iter: int = 300, verbose: int = 0, eps: float = 0.001, random_state: Incomplete | None = None, return_n_iter: bool = False, normalized_stress: str = 'warn'):
    '''Compute multidimensional scaling using the SMACOF algorithm.

    The SMACOF (Scaling by MAjorizing a COmplicated Function) algorithm is a
    multidimensional scaling algorithm which minimizes an objective function
    (the *stress*) using a majorization technique. Stress majorization, also
    known as the Guttman Transform, guarantees a monotone convergence of
    stress, and is more powerful than traditional techniques such as gradient
    descent.

    The SMACOF algorithm for metric MDS can be summarized by the following
    steps:

    1. Set an initial start configuration, randomly or not.
    2. Compute the stress
    3. Compute the Guttman Transform
    4. Iterate 2 and 3 until convergence.

    The nonmetric algorithm adds a monotonic regression step before computing
    the stress.

    Parameters
    ----------
    dissimilarities : ndarray of shape (n_samples, n_samples)
        Pairwise dissimilarities between the points. Must be symmetric.

    metric : bool, default=True
        Compute metric or nonmetric SMACOF algorithm.
        When ``False`` (i.e. non-metric MDS), dissimilarities with 0 are considered as
        missing values.

    n_components : int, default=2
        Number of dimensions in which to immerse the dissimilarities. If an
        ``init`` array is provided, this option is overridden and the shape of
        ``init`` is used to determine the dimensionality of the embedding
        space.

    init : ndarray of shape (n_samples, n_components), default=None
        Starting configuration of the embedding to initialize the algorithm. By
        default, the algorithm is initialized with a randomly chosen array.

    n_init : int, default=8
        Number of times the SMACOF algorithm will be run with different
        initializations. The final results will be the best output of the runs,
        determined by the run with the smallest final stress. If ``init`` is
        provided, this option is overridden and a single run is performed.

    n_jobs : int, default=None
        The number of jobs to use for the computation. If multiple
        initializations are used (``n_init``), each run of the algorithm is
        computed in parallel.

        ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
        ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
        for more details.

    max_iter : int, default=300
        Maximum number of iterations of the SMACOF algorithm for a single run.

    verbose : int, default=0
        Level of verbosity.

    eps : float, default=1e-3
        Relative tolerance with respect to stress at which to declare
        convergence. The value of `eps` should be tuned separately depending
        on whether or not `normalized_stress` is being used.

    random_state : int, RandomState instance or None, default=None
        Determines the random number generator used to initialize the centers.
        Pass an int for reproducible results across multiple function calls.
        See :term:`Glossary <random_state>`.

    return_n_iter : bool, default=False
        Whether or not to return the number of iterations.

    normalized_stress : bool or "auto" default=False
        Whether use and return normed stress value (Stress-1) instead of raw
        stress calculated by default. Only supported in non-metric MDS.

        .. versionadded:: 1.2

    Returns
    -------
    X : ndarray of shape (n_samples, n_components)
        Coordinates of the points in a ``n_components``-space.

    stress : float
        The final value of the stress (sum of squared distance of the
        disparities and the distances for all constrained points).
        If `normalized_stress=True`, and `metric=False` returns Stress-1.
        A value of 0 indicates "perfect" fit, 0.025 excellent, 0.05 good,
        0.1 fair, and 0.2 poor [1]_.

    n_iter : int
        The number of iterations corresponding to the best stress. Returned
        only if ``return_n_iter`` is set to ``True``.

    References
    ----------
    .. [1] "Nonmetric multidimensional scaling: a numerical method" Kruskal, J.
           Psychometrika, 29 (1964)

    .. [2] "Multidimensional scaling by optimizing goodness of fit to a nonmetric
           hypothesis" Kruskal, J. Psychometrika, 29, (1964)

    .. [3] "Modern Multidimensional Scaling - Theory and Applications" Borg, I.;
           Groenen P. Springer Series in Statistics (1997)
    '''

class MDS(BaseEstimator):
    '''Multidimensional scaling.

    Read more in the :ref:`User Guide <multidimensional_scaling>`.

    Parameters
    ----------
    n_components : int, default=2
        Number of dimensions in which to immerse the dissimilarities.

    metric : bool, default=True
        If ``True``, perform metric MDS; otherwise, perform nonmetric MDS.
        When ``False`` (i.e. non-metric MDS), dissimilarities with 0 are considered as
        missing values.

    n_init : int, default=4
        Number of times the SMACOF algorithm will be run with different
        initializations. The final results will be the best output of the runs,
        determined by the run with the smallest final stress.

    max_iter : int, default=300
        Maximum number of iterations of the SMACOF algorithm for a single run.

    verbose : int, default=0
        Level of verbosity.

    eps : float, default=1e-3
        Relative tolerance with respect to stress at which to declare
        convergence. The value of `eps` should be tuned separately depending
        on whether or not `normalized_stress` is being used.

    n_jobs : int, default=None
        The number of jobs to use for the computation. If multiple
        initializations are used (``n_init``), each run of the algorithm is
        computed in parallel.

        ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
        ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
        for more details.

    random_state : int, RandomState instance or None, default=None
        Determines the random number generator used to initialize the centers.
        Pass an int for reproducible results across multiple function calls.
        See :term:`Glossary <random_state>`.

    dissimilarity : {\'euclidean\', \'precomputed\'}, default=\'euclidean\'
        Dissimilarity measure to use:

        - \'euclidean\':
            Pairwise Euclidean distances between points in the dataset.

        - \'precomputed\':
            Pre-computed dissimilarities are passed directly to ``fit`` and
            ``fit_transform``.

    normalized_stress : bool or "auto" default=False
        Whether use and return normed stress value (Stress-1) instead of raw
        stress calculated by default. Only supported in non-metric MDS.

        .. versionadded:: 1.2

    Attributes
    ----------
    embedding_ : ndarray of shape (n_samples, n_components)
        Stores the position of the dataset in the embedding space.

    stress_ : float
        The final value of the stress (sum of squared distance of the
        disparities and the distances for all constrained points).
        If `normalized_stress=True`, and `metric=False` returns Stress-1.
        A value of 0 indicates "perfect" fit, 0.025 excellent, 0.05 good,
        0.1 fair, and 0.2 poor [1]_.

    dissimilarity_matrix_ : ndarray of shape (n_samples, n_samples)
        Pairwise dissimilarities between the points. Symmetric matrix that:

        - either uses a custom dissimilarity matrix by setting `dissimilarity`
          to \'precomputed\';
        - or constructs a dissimilarity matrix from data using
          Euclidean distances.

    n_features_in_ : int
        Number of features seen during :term:`fit`.

        .. versionadded:: 0.24

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

        .. versionadded:: 1.0

    n_iter_ : int
        The number of iterations corresponding to the best stress.

    See Also
    --------
    sklearn.decomposition.PCA : Principal component analysis that is a linear
        dimensionality reduction method.
    sklearn.decomposition.KernelPCA : Non-linear dimensionality reduction using
        kernels and PCA.
    TSNE : T-distributed Stochastic Neighbor Embedding.
    Isomap : Manifold learning based on Isometric Mapping.
    LocallyLinearEmbedding : Manifold learning using Locally Linear Embedding.
    SpectralEmbedding : Spectral embedding for non-linear dimensionality.

    References
    ----------
    .. [1] "Nonmetric multidimensional scaling: a numerical method" Kruskal, J.
       Psychometrika, 29 (1964)

    .. [2] "Multidimensional scaling by optimizing goodness of fit to a nonmetric
       hypothesis" Kruskal, J. Psychometrika, 29, (1964)

    .. [3] "Modern Multidimensional Scaling - Theory and Applications" Borg, I.;
       Groenen P. Springer Series in Statistics (1997)

    Examples
    --------
    >>> from sklearn.datasets import load_digits
    >>> from sklearn.manifold import MDS
    >>> X, _ = load_digits(return_X_y=True)
    >>> X.shape
    (1797, 64)
    >>> embedding = MDS(n_components=2, normalized_stress=\'auto\')
    >>> X_transformed = embedding.fit_transform(X[:100])
    >>> X_transformed.shape
    (100, 2)
    '''
    n_components: Incomplete
    dissimilarity: Incomplete
    metric: Incomplete
    n_init: Incomplete
    max_iter: Incomplete
    eps: Incomplete
    verbose: Incomplete
    n_jobs: Incomplete
    random_state: Incomplete
    normalized_stress: Incomplete
    def __init__(self, n_components: int = 2, *, metric: bool = True, n_init: int = 4, max_iter: int = 300, verbose: int = 0, eps: float = 0.001, n_jobs: Incomplete | None = None, random_state: Incomplete | None = None, dissimilarity: str = 'euclidean', normalized_stress: str = 'warn') -> None: ...
    def fit(self, X, y: Incomplete | None = None, init: Incomplete | None = None):
        """
        Compute the position of the points in the embedding space.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features) or                 (n_samples, n_samples)
            Input data. If ``dissimilarity=='precomputed'``, the input should
            be the dissimilarity matrix.

        y : Ignored
            Not used, present for API consistency by convention.

        init : ndarray of shape (n_samples, n_components), default=None
            Starting configuration of the embedding to initialize the SMACOF
            algorithm. By default, the algorithm is initialized with a randomly
            chosen array.

        Returns
        -------
        self : object
            Fitted estimator.
        """
    dissimilarity_matrix_: Incomplete
    def fit_transform(self, X, y: Incomplete | None = None, init: Incomplete | None = None):
        """
        Fit the data from `X`, and returns the embedded coordinates.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features) or                 (n_samples, n_samples)
            Input data. If ``dissimilarity=='precomputed'``, the input should
            be the dissimilarity matrix.

        y : Ignored
            Not used, present for API consistency by convention.

        init : ndarray of shape (n_samples, n_components), default=None
            Starting configuration of the embedding to initialize the SMACOF
            algorithm. By default, the algorithm is initialized with a randomly
            chosen array.

        Returns
        -------
        X_new : ndarray of shape (n_samples, n_components)
            X transformed in the new space.
        """
