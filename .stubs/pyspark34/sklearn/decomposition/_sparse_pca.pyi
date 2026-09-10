from ..base import BaseEstimator as BaseEstimator, ClassNamePrefixFeaturesOutMixin as ClassNamePrefixFeaturesOutMixin, TransformerMixin as TransformerMixin
from ..linear_model import ridge_regression as ridge_regression
from ..utils import check_random_state as check_random_state
from ..utils._param_validation import Hidden as Hidden, Interval as Interval, StrOptions as StrOptions
from ..utils.extmath import svd_flip as svd_flip
from ..utils.validation import check_array as check_array, check_is_fitted as check_is_fitted
from ._dict_learning import MiniBatchDictionaryLearning as MiniBatchDictionaryLearning, dict_learning as dict_learning
from _typeshed import Incomplete

class _BaseSparsePCA(ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):
    """Base class for SparsePCA and MiniBatchSparsePCA"""
    n_components: Incomplete
    alpha: Incomplete
    ridge_alpha: Incomplete
    max_iter: Incomplete
    tol: Incomplete
    method: Incomplete
    n_jobs: Incomplete
    verbose: Incomplete
    random_state: Incomplete
    def __init__(self, n_components: Incomplete | None = None, *, alpha: int = 1, ridge_alpha: float = 0.01, max_iter: int = 1000, tol: float = 1e-08, method: str = 'lars', n_jobs: Incomplete | None = None, verbose: bool = False, random_state: Incomplete | None = None) -> None: ...
    mean_: Incomplete
    def fit(self, X, y: Incomplete | None = None):
        """Fit the model from data in X.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Training vector, where `n_samples` is the number of samples
            and `n_features` is the number of features.

        y : Ignored
            Not used, present here for API consistency by convention.

        Returns
        -------
        self : object
            Returns the instance itself.
        """
    def transform(self, X):
        """Least Squares projection of the data onto the sparse components.

        To avoid instability issues in case the system is under-determined,
        regularization can be applied (Ridge regression) via the
        `ridge_alpha` parameter.

        Note that Sparse PCA components orthogonality is not enforced as in PCA
        hence one cannot use a simple linear projection.

        Parameters
        ----------
        X : ndarray of shape (n_samples, n_features)
            Test data to be transformed, must have the same number of
            features as the data used to train the model.

        Returns
        -------
        X_new : ndarray of shape (n_samples, n_components)
            Transformed data.
        """
    def inverse_transform(self, X):
        """Transform data from the latent space to the original space.

        This inversion is an approximation due to the loss of information
        induced by the forward decomposition.

        .. versionadded:: 1.2

        Parameters
        ----------
        X : ndarray of shape (n_samples, n_components)
            Data in the latent space.

        Returns
        -------
        X_original : ndarray of shape (n_samples, n_features)
            Reconstructed data in the original space.
        """

class SparsePCA(_BaseSparsePCA):
    """Sparse Principal Components Analysis (SparsePCA).

    Finds the set of sparse components that can optimally reconstruct
    the data.  The amount of sparseness is controllable by the coefficient
    of the L1 penalty, given by the parameter alpha.

    Read more in the :ref:`User Guide <SparsePCA>`.

    Parameters
    ----------
    n_components : int, default=None
        Number of sparse atoms to extract. If None, then ``n_components``
        is set to ``n_features``.

    alpha : float, default=1
        Sparsity controlling parameter. Higher values lead to sparser
        components.

    ridge_alpha : float, default=0.01
        Amount of ridge shrinkage to apply in order to improve
        conditioning when calling the transform method.

    max_iter : int, default=1000
        Maximum number of iterations to perform.

    tol : float, default=1e-8
        Tolerance for the stopping condition.

    method : {'lars', 'cd'}, default='lars'
        Method to be used for optimization.
        lars: uses the least angle regression method to solve the lasso problem
        (linear_model.lars_path)
        cd: uses the coordinate descent method to compute the
        Lasso solution (linear_model.Lasso). Lars will be faster if
        the estimated components are sparse.

    n_jobs : int, default=None
        Number of parallel jobs to run.
        ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
        ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
        for more details.

    U_init : ndarray of shape (n_samples, n_components), default=None
        Initial values for the loadings for warm restart scenarios. Only used
        if `U_init` and `V_init` are not None.

    V_init : ndarray of shape (n_components, n_features), default=None
        Initial values for the components for warm restart scenarios. Only used
        if `U_init` and `V_init` are not None.

    verbose : int or bool, default=False
        Controls the verbosity; the higher, the more messages. Defaults to 0.

    random_state : int, RandomState instance or None, default=None
        Used during dictionary learning. Pass an int for reproducible results
        across multiple function calls.
        See :term:`Glossary <random_state>`.

    Attributes
    ----------
    components_ : ndarray of shape (n_components, n_features)
        Sparse components extracted from the data.

    error_ : ndarray
        Vector of errors at each iteration.

    n_components_ : int
        Estimated number of components.

        .. versionadded:: 0.23

    n_iter_ : int
        Number of iterations run.

    mean_ : ndarray of shape (n_features,)
        Per-feature empirical mean, estimated from the training set.
        Equal to ``X.mean(axis=0)``.

    n_features_in_ : int
        Number of features seen during :term:`fit`.

        .. versionadded:: 0.24

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

        .. versionadded:: 1.0

    See Also
    --------
    PCA : Principal Component Analysis implementation.
    MiniBatchSparsePCA : Mini batch variant of `SparsePCA` that is faster but less
        accurate.
    DictionaryLearning : Generic dictionary learning problem using a sparse code.

    Examples
    --------
    >>> import numpy as np
    >>> from sklearn.datasets import make_friedman1
    >>> from sklearn.decomposition import SparsePCA
    >>> X, _ = make_friedman1(n_samples=200, n_features=30, random_state=0)
    >>> transformer = SparsePCA(n_components=5, random_state=0)
    >>> transformer.fit(X)
    SparsePCA(...)
    >>> X_transformed = transformer.transform(X)
    >>> X_transformed.shape
    (200, 5)
    >>> # most values in the components_ are zero (sparsity)
    >>> np.mean(transformer.components_ == 0)
    0.9666...
    """
    U_init: Incomplete
    V_init: Incomplete
    def __init__(self, n_components: Incomplete | None = None, *, alpha: int = 1, ridge_alpha: float = 0.01, max_iter: int = 1000, tol: float = 1e-08, method: str = 'lars', n_jobs: Incomplete | None = None, U_init: Incomplete | None = None, V_init: Incomplete | None = None, verbose: bool = False, random_state: Incomplete | None = None) -> None: ...

class MiniBatchSparsePCA(_BaseSparsePCA):
    """Mini-batch Sparse Principal Components Analysis.

    Finds the set of sparse components that can optimally reconstruct
    the data.  The amount of sparseness is controllable by the coefficient
    of the L1 penalty, given by the parameter alpha.

    Read more in the :ref:`User Guide <SparsePCA>`.

    Parameters
    ----------
    n_components : int, default=None
        Number of sparse atoms to extract. If None, then ``n_components``
        is set to ``n_features``.

    alpha : int, default=1
        Sparsity controlling parameter. Higher values lead to sparser
        components.

    ridge_alpha : float, default=0.01
        Amount of ridge shrinkage to apply in order to improve
        conditioning when calling the transform method.

    n_iter : int, default=100
        Number of iterations to perform for each mini batch.

        .. deprecated:: 1.2
           `n_iter` is deprecated in 1.2 and will be removed in 1.4. Use
           `max_iter` instead.

    max_iter : int, default=None
        Maximum number of iterations over the complete dataset before
        stopping independently of any early stopping criterion heuristics.
        If `max_iter` is not `None`, `n_iter` is ignored.

        .. versionadded:: 1.2

    callback : callable, default=None
        Callable that gets invoked every five iterations.

    batch_size : int, default=3
        The number of features to take in each mini batch.

    verbose : int or bool, default=False
        Controls the verbosity; the higher, the more messages. Defaults to 0.

    shuffle : bool, default=True
        Whether to shuffle the data before splitting it in batches.

    n_jobs : int, default=None
        Number of parallel jobs to run.
        ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
        ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
        for more details.

    method : {'lars', 'cd'}, default='lars'
        Method to be used for optimization.
        lars: uses the least angle regression method to solve the lasso problem
        (linear_model.lars_path)
        cd: uses the coordinate descent method to compute the
        Lasso solution (linear_model.Lasso). Lars will be faster if
        the estimated components are sparse.

    random_state : int, RandomState instance or None, default=None
        Used for random shuffling when ``shuffle`` is set to ``True``,
        during online dictionary learning. Pass an int for reproducible results
        across multiple function calls.
        See :term:`Glossary <random_state>`.

    tol : float, default=1e-3
        Control early stopping based on the norm of the differences in the
        dictionary between 2 steps. Used only if `max_iter` is not None.

        To disable early stopping based on changes in the dictionary, set
        `tol` to 0.0.

        .. versionadded:: 1.1

    max_no_improvement : int or None, default=10
        Control early stopping based on the consecutive number of mini batches
        that does not yield an improvement on the smoothed cost function. Used only if
        `max_iter` is not None.

        To disable convergence detection based on cost function, set
        `max_no_improvement` to `None`.

        .. versionadded:: 1.1

    Attributes
    ----------
    components_ : ndarray of shape (n_components, n_features)
        Sparse components extracted from the data.

    n_components_ : int
        Estimated number of components.

        .. versionadded:: 0.23

    n_iter_ : int
        Number of iterations run.

    mean_ : ndarray of shape (n_features,)
        Per-feature empirical mean, estimated from the training set.
        Equal to ``X.mean(axis=0)``.

    n_features_in_ : int
        Number of features seen during :term:`fit`.

        .. versionadded:: 0.24

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

        .. versionadded:: 1.0

    See Also
    --------
    DictionaryLearning : Find a dictionary that sparsely encodes data.
    IncrementalPCA : Incremental principal components analysis.
    PCA : Principal component analysis.
    SparsePCA : Sparse Principal Components Analysis.
    TruncatedSVD : Dimensionality reduction using truncated SVD.

    Examples
    --------
    >>> import numpy as np
    >>> from sklearn.datasets import make_friedman1
    >>> from sklearn.decomposition import MiniBatchSparsePCA
    >>> X, _ = make_friedman1(n_samples=200, n_features=30, random_state=0)
    >>> transformer = MiniBatchSparsePCA(n_components=5, batch_size=50,
    ...                                  max_iter=10, random_state=0)
    >>> transformer.fit(X)
    MiniBatchSparsePCA(...)
    >>> X_transformed = transformer.transform(X)
    >>> X_transformed.shape
    (200, 5)
    >>> # most values in the components_ are zero (sparsity)
    >>> np.mean(transformer.components_ == 0)
    0.9...
    """
    n_iter: Incomplete
    callback: Incomplete
    batch_size: Incomplete
    shuffle: Incomplete
    max_no_improvement: Incomplete
    def __init__(self, n_components: Incomplete | None = None, *, alpha: int = 1, ridge_alpha: float = 0.01, n_iter: str = 'deprecated', max_iter: Incomplete | None = None, callback: Incomplete | None = None, batch_size: int = 3, verbose: bool = False, shuffle: bool = True, n_jobs: Incomplete | None = None, method: str = 'lars', random_state: Incomplete | None = None, tol: float = 0.001, max_no_improvement: int = 10) -> None: ...
