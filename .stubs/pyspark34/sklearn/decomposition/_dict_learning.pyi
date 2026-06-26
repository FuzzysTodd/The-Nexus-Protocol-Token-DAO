from ..base import BaseEstimator as BaseEstimator, ClassNamePrefixFeaturesOutMixin as ClassNamePrefixFeaturesOutMixin, TransformerMixin as TransformerMixin
from ..linear_model import Lars as Lars, Lasso as Lasso, LassoLars as LassoLars, orthogonal_mp_gram as orthogonal_mp_gram
from ..utils import check_array as check_array, check_random_state as check_random_state, gen_batches as gen_batches, gen_even_slices as gen_even_slices
from ..utils._param_validation import Hidden as Hidden, Interval as Interval, StrOptions as StrOptions, validate_params as validate_params
from ..utils.extmath import randomized_svd as randomized_svd, row_norms as row_norms, svd_flip as svd_flip
from ..utils.parallel import Parallel as Parallel, delayed as delayed
from ..utils.validation import check_is_fitted as check_is_fitted
from _typeshed import Incomplete

def sparse_encode(X, dictionary, *, gram: Incomplete | None = None, cov: Incomplete | None = None, algorithm: str = 'lasso_lars', n_nonzero_coefs: Incomplete | None = None, alpha: Incomplete | None = None, copy_cov: bool = True, init: Incomplete | None = None, max_iter: int = 1000, n_jobs: Incomplete | None = None, check_input: bool = True, verbose: int = 0, positive: bool = False):
    """Sparse coding.

    Each row of the result is the solution to a sparse coding problem.
    The goal is to find a sparse array `code` such that::

        X ~= code * dictionary

    Read more in the :ref:`User Guide <SparseCoder>`.

    Parameters
    ----------
    X : array-like of shape (n_samples, n_features)
        Data matrix.

    dictionary : array-like of shape (n_components, n_features)
        The dictionary matrix against which to solve the sparse coding of
        the data. Some of the algorithms assume normalized rows for meaningful
        output.

    gram : array-like of shape (n_components, n_components), default=None
        Precomputed Gram matrix, `dictionary * dictionary'`.

    cov : array-like of shape (n_components, n_samples), default=None
        Precomputed covariance, `dictionary' * X`.

    algorithm : {'lasso_lars', 'lasso_cd', 'lars', 'omp', 'threshold'},             default='lasso_lars'
        The algorithm used:

        * `'lars'`: uses the least angle regression method
          (`linear_model.lars_path`);
        * `'lasso_lars'`: uses Lars to compute the Lasso solution;
        * `'lasso_cd'`: uses the coordinate descent method to compute the
          Lasso solution (`linear_model.Lasso`). lasso_lars will be faster if
          the estimated components are sparse;
        * `'omp'`: uses orthogonal matching pursuit to estimate the sparse
          solution;
        * `'threshold'`: squashes to zero all coefficients less than
          regularization from the projection `dictionary * data'`.

    n_nonzero_coefs : int, default=None
        Number of nonzero coefficients to target in each column of the
        solution. This is only used by `algorithm='lars'` and `algorithm='omp'`
        and is overridden by `alpha` in the `omp` case. If `None`, then
        `n_nonzero_coefs=int(n_features / 10)`.

    alpha : float, default=None
        If `algorithm='lasso_lars'` or `algorithm='lasso_cd'`, `alpha` is the
        penalty applied to the L1 norm.
        If `algorithm='threshold'`, `alpha` is the absolute value of the
        threshold below which coefficients will be squashed to zero.
        If `algorithm='omp'`, `alpha` is the tolerance parameter: the value of
        the reconstruction error targeted. In this case, it overrides
        `n_nonzero_coefs`.
        If `None`, default to 1.

    copy_cov : bool, default=True
        Whether to copy the precomputed covariance matrix; if `False`, it may
        be overwritten.

    init : ndarray of shape (n_samples, n_components), default=None
        Initialization value of the sparse codes. Only used if
        `algorithm='lasso_cd'`.

    max_iter : int, default=1000
        Maximum number of iterations to perform if `algorithm='lasso_cd'` or
        `'lasso_lars'`.

    n_jobs : int, default=None
        Number of parallel jobs to run.
        ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
        ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
        for more details.

    check_input : bool, default=True
        If `False`, the input arrays X and dictionary will not be checked.

    verbose : int, default=0
        Controls the verbosity; the higher, the more messages.

    positive : bool, default=False
        Whether to enforce positivity when finding the encoding.

        .. versionadded:: 0.20

    Returns
    -------
    code : ndarray of shape (n_samples, n_components)
        The sparse codes.

    See Also
    --------
    sklearn.linear_model.lars_path : Compute Least Angle Regression or Lasso
        path using LARS algorithm.
    sklearn.linear_model.orthogonal_mp : Solves Orthogonal Matching Pursuit problems.
    sklearn.linear_model.Lasso : Train Linear Model with L1 prior as regularizer.
    SparseCoder : Find a sparse representation of data from a fixed precomputed
        dictionary.
    """
def dict_learning_online(X, n_components: int = 2, *, alpha: int = 1, n_iter: str = 'deprecated', max_iter: Incomplete | None = None, return_code: bool = True, dict_init: Incomplete | None = None, callback: Incomplete | None = None, batch_size: int = 256, verbose: bool = False, shuffle: bool = True, n_jobs: Incomplete | None = None, method: str = 'lars', iter_offset: str = 'deprecated', random_state: Incomplete | None = None, return_inner_stats: str = 'deprecated', inner_stats: str = 'deprecated', return_n_iter: str = 'deprecated', positive_dict: bool = False, positive_code: bool = False, method_max_iter: int = 1000, tol: float = 0.001, max_no_improvement: int = 10):
    """Solve a dictionary learning matrix factorization problem online.

    Finds the best dictionary and the corresponding sparse code for
    approximating the data matrix X by solving::

        (U^*, V^*) = argmin 0.5 || X - U V ||_Fro^2 + alpha * || U ||_1,1
                     (U,V)
                     with || V_k ||_2 = 1 for all  0 <= k < n_components

    where V is the dictionary and U is the sparse code. ||.||_Fro stands for
    the Frobenius norm and ||.||_1,1 stands for the entry-wise matrix norm
    which is the sum of the absolute values of all the entries in the matrix.
    This is accomplished by repeatedly iterating over mini-batches by slicing
    the input data.

    Read more in the :ref:`User Guide <DictionaryLearning>`.

    Parameters
    ----------
    X : ndarray of shape (n_samples, n_features)
        Data matrix.

    n_components : int or None, default=2
        Number of dictionary atoms to extract. If None, then ``n_components``
        is set to ``n_features``.

    alpha : float, default=1
        Sparsity controlling parameter.

    n_iter : int, default=100
        Number of mini-batch iterations to perform.

        .. deprecated:: 1.1
           `n_iter` is deprecated in 1.1 and will be removed in 1.4. Use
           `max_iter` instead.

    max_iter : int, default=None
        Maximum number of iterations over the complete dataset before
        stopping independently of any early stopping criterion heuristics.
        If ``max_iter`` is not None, ``n_iter`` is ignored.

        .. versionadded:: 1.1

    return_code : bool, default=True
        Whether to also return the code U or just the dictionary `V`.

    dict_init : ndarray of shape (n_components, n_features), default=None
        Initial values for the dictionary for warm restart scenarios.
        If `None`, the initial values for the dictionary are created
        with an SVD decomposition of the data via :func:`~sklearn.utils.randomized_svd`.

    callback : callable, default=None
        A callable that gets invoked at the end of each iteration.

    batch_size : int, default=256
        The number of samples to take in each batch.

        .. versionchanged:: 1.3
           The default value of `batch_size` changed from 3 to 256 in version 1.3.

    verbose : bool, default=False
        To control the verbosity of the procedure.

    shuffle : bool, default=True
        Whether to shuffle the data before splitting it in batches.

    n_jobs : int, default=None
        Number of parallel jobs to run.
        ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
        ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
        for more details.

    method : {'lars', 'cd'}, default='lars'
        * `'lars'`: uses the least angle regression method to solve the lasso
          problem (`linear_model.lars_path`);
        * `'cd'`: uses the coordinate descent method to compute the
          Lasso solution (`linear_model.Lasso`). Lars will be faster if
          the estimated components are sparse.

    iter_offset : int, default=0
        Number of previous iterations completed on the dictionary used for
        initialization.

        .. deprecated:: 1.1
           `iter_offset` serves internal purpose only and will be removed in 1.4.

    random_state : int, RandomState instance or None, default=None
        Used for initializing the dictionary when ``dict_init`` is not
        specified, randomly shuffling the data when ``shuffle`` is set to
        ``True``, and updating the dictionary. Pass an int for reproducible
        results across multiple function calls.
        See :term:`Glossary <random_state>`.

    return_inner_stats : bool, default=False
        Return the inner statistics A (dictionary covariance) and B
        (data approximation). Useful to restart the algorithm in an
        online setting. If `return_inner_stats` is `True`, `return_code` is
        ignored.

        .. deprecated:: 1.1
           `return_inner_stats` serves internal purpose only and will be removed in 1.4.

    inner_stats : tuple of (A, B) ndarrays, default=None
        Inner sufficient statistics that are kept by the algorithm.
        Passing them at initialization is useful in online settings, to
        avoid losing the history of the evolution.
        `A` `(n_components, n_components)` is the dictionary covariance matrix.
        `B` `(n_features, n_components)` is the data approximation matrix.

        .. deprecated:: 1.1
           `inner_stats` serves internal purpose only and will be removed in 1.4.

    return_n_iter : bool, default=False
        Whether or not to return the number of iterations.

        .. deprecated:: 1.1
           `return_n_iter` will be removed in 1.4 and n_iter will never be returned.

    positive_dict : bool, default=False
        Whether to enforce positivity when finding the dictionary.

        .. versionadded:: 0.20

    positive_code : bool, default=False
        Whether to enforce positivity when finding the code.

        .. versionadded:: 0.20

    method_max_iter : int, default=1000
        Maximum number of iterations to perform when solving the lasso problem.

        .. versionadded:: 0.22

    tol : float, default=1e-3
        Control early stopping based on the norm of the differences in the
        dictionary between 2 steps. Used only if `max_iter` is not None.

        To disable early stopping based on changes in the dictionary, set
        `tol` to 0.0.

        .. versionadded:: 1.1

    max_no_improvement : int, default=10
        Control early stopping based on the consecutive number of mini batches
        that does not yield an improvement on the smoothed cost function. Used only if
        `max_iter` is not None.

        To disable convergence detection based on cost function, set
        `max_no_improvement` to None.

        .. versionadded:: 1.1

    Returns
    -------
    code : ndarray of shape (n_samples, n_components),
        The sparse code (only returned if `return_code=True`).

    dictionary : ndarray of shape (n_components, n_features),
        The solutions to the dictionary learning problem.

    n_iter : int
        Number of iterations run. Returned only if `return_n_iter` is
        set to `True`.

    See Also
    --------
    dict_learning : Solve a dictionary learning matrix factorization problem.
    DictionaryLearning : Find a dictionary that sparsely encodes data.
    MiniBatchDictionaryLearning : A faster, less accurate, version of the dictionary
        learning algorithm.
    SparsePCA : Sparse Principal Components Analysis.
    MiniBatchSparsePCA : Mini-batch Sparse Principal Components Analysis.
    """
def dict_learning(X, n_components, *, alpha, max_iter: int = 100, tol: float = 1e-08, method: str = 'lars', n_jobs: Incomplete | None = None, dict_init: Incomplete | None = None, code_init: Incomplete | None = None, callback: Incomplete | None = None, verbose: bool = False, random_state: Incomplete | None = None, return_n_iter: bool = False, positive_dict: bool = False, positive_code: bool = False, method_max_iter: int = 1000):
    """Solve a dictionary learning matrix factorization problem.

    Finds the best dictionary and the corresponding sparse code for
    approximating the data matrix X by solving::

        (U^*, V^*) = argmin 0.5 || X - U V ||_Fro^2 + alpha * || U ||_1,1
                     (U,V)
                    with || V_k ||_2 = 1 for all  0 <= k < n_components

    where V is the dictionary and U is the sparse code. ||.||_Fro stands for
    the Frobenius norm and ||.||_1,1 stands for the entry-wise matrix norm
    which is the sum of the absolute values of all the entries in the matrix.

    Read more in the :ref:`User Guide <DictionaryLearning>`.

    Parameters
    ----------
    X : array-like of shape (n_samples, n_features)
        Data matrix.

    n_components : int
        Number of dictionary atoms to extract.

    alpha : int or float
        Sparsity controlling parameter.

    max_iter : int, default=100
        Maximum number of iterations to perform.

    tol : float, default=1e-8
        Tolerance for the stopping condition.

    method : {'lars', 'cd'}, default='lars'
        The method used:

        * `'lars'`: uses the least angle regression method to solve the lasso
           problem (`linear_model.lars_path`);
        * `'cd'`: uses the coordinate descent method to compute the
          Lasso solution (`linear_model.Lasso`). Lars will be faster if
          the estimated components are sparse.

    n_jobs : int, default=None
        Number of parallel jobs to run.
        ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
        ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
        for more details.

    dict_init : ndarray of shape (n_components, n_features), default=None
        Initial value for the dictionary for warm restart scenarios. Only used
        if `code_init` and `dict_init` are not None.

    code_init : ndarray of shape (n_samples, n_components), default=None
        Initial value for the sparse code for warm restart scenarios. Only used
        if `code_init` and `dict_init` are not None.

    callback : callable, default=None
        Callable that gets invoked every five iterations.

    verbose : bool, default=False
        To control the verbosity of the procedure.

    random_state : int, RandomState instance or None, default=None
        Used for randomly initializing the dictionary. Pass an int for
        reproducible results across multiple function calls.
        See :term:`Glossary <random_state>`.

    return_n_iter : bool, default=False
        Whether or not to return the number of iterations.

    positive_dict : bool, default=False
        Whether to enforce positivity when finding the dictionary.

        .. versionadded:: 0.20

    positive_code : bool, default=False
        Whether to enforce positivity when finding the code.

        .. versionadded:: 0.20

    method_max_iter : int, default=1000
        Maximum number of iterations to perform.

        .. versionadded:: 0.22

    Returns
    -------
    code : ndarray of shape (n_samples, n_components)
        The sparse code factor in the matrix factorization.

    dictionary : ndarray of shape (n_components, n_features),
        The dictionary factor in the matrix factorization.

    errors : array
        Vector of errors at each iteration.

    n_iter : int
        Number of iterations run. Returned only if `return_n_iter` is
        set to True.

    See Also
    --------
    dict_learning_online : Solve a dictionary learning matrix factorization
        problem online.
    DictionaryLearning : Find a dictionary that sparsely encodes data.
    MiniBatchDictionaryLearning : A faster, less accurate version
        of the dictionary learning algorithm.
    SparsePCA : Sparse Principal Components Analysis.
    MiniBatchSparsePCA : Mini-batch Sparse Principal Components Analysis.
    """

class _BaseSparseCoding(ClassNamePrefixFeaturesOutMixin, TransformerMixin):
    """Base class from SparseCoder and DictionaryLearning algorithms."""
    transform_algorithm: Incomplete
    transform_n_nonzero_coefs: Incomplete
    transform_alpha: Incomplete
    transform_max_iter: Incomplete
    split_sign: Incomplete
    n_jobs: Incomplete
    positive_code: Incomplete
    def __init__(self, transform_algorithm, transform_n_nonzero_coefs, transform_alpha, split_sign, n_jobs, positive_code, transform_max_iter) -> None: ...
    def transform(self, X):
        """Encode the data as a sparse combination of the dictionary atoms.

        Coding method is determined by the object parameter
        `transform_algorithm`.

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

class SparseCoder(_BaseSparseCoding, BaseEstimator):
    """Sparse coding.

    Finds a sparse representation of data against a fixed, precomputed
    dictionary.

    Each row of the result is the solution to a sparse coding problem.
    The goal is to find a sparse array `code` such that::

        X ~= code * dictionary

    Read more in the :ref:`User Guide <SparseCoder>`.

    Parameters
    ----------
    dictionary : ndarray of shape (n_components, n_features)
        The dictionary atoms used for sparse coding. Lines are assumed to be
        normalized to unit norm.

    transform_algorithm : {'lasso_lars', 'lasso_cd', 'lars', 'omp',             'threshold'}, default='omp'
        Algorithm used to transform the data:

        - `'lars'`: uses the least angle regression method
          (`linear_model.lars_path`);
        - `'lasso_lars'`: uses Lars to compute the Lasso solution;
        - `'lasso_cd'`: uses the coordinate descent method to compute the
          Lasso solution (linear_model.Lasso). `'lasso_lars'` will be faster if
          the estimated components are sparse;
        - `'omp'`: uses orthogonal matching pursuit to estimate the sparse
          solution;
        - `'threshold'`: squashes to zero all coefficients less than alpha from
          the projection ``dictionary * X'``.

    transform_n_nonzero_coefs : int, default=None
        Number of nonzero coefficients to target in each column of the
        solution. This is only used by `algorithm='lars'` and `algorithm='omp'`
        and is overridden by `alpha` in the `omp` case. If `None`, then
        `transform_n_nonzero_coefs=int(n_features / 10)`.

    transform_alpha : float, default=None
        If `algorithm='lasso_lars'` or `algorithm='lasso_cd'`, `alpha` is the
        penalty applied to the L1 norm.
        If `algorithm='threshold'`, `alpha` is the absolute value of the
        threshold below which coefficients will be squashed to zero.
        If `algorithm='omp'`, `alpha` is the tolerance parameter: the value of
        the reconstruction error targeted. In this case, it overrides
        `n_nonzero_coefs`.
        If `None`, default to 1.

    split_sign : bool, default=False
        Whether to split the sparse feature vector into the concatenation of
        its negative part and its positive part. This can improve the
        performance of downstream classifiers.

    n_jobs : int, default=None
        Number of parallel jobs to run.
        ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
        ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
        for more details.

    positive_code : bool, default=False
        Whether to enforce positivity when finding the code.

        .. versionadded:: 0.20

    transform_max_iter : int, default=1000
        Maximum number of iterations to perform if `algorithm='lasso_cd'` or
        `lasso_lars`.

        .. versionadded:: 0.22

    Attributes
    ----------
    n_components_ : int
        Number of atoms.

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
    MiniBatchDictionaryLearning : A faster, less accurate, version of the
        dictionary learning algorithm.
    MiniBatchSparsePCA : Mini-batch Sparse Principal Components Analysis.
    SparsePCA : Sparse Principal Components Analysis.
    sparse_encode : Sparse coding where each row of the result is the solution
        to a sparse coding problem.

    Examples
    --------
    >>> import numpy as np
    >>> from sklearn.decomposition import SparseCoder
    >>> X = np.array([[-1, -1, -1], [0, 0, 3]])
    >>> dictionary = np.array(
    ...     [[0, 1, 0],
    ...      [-1, -1, 2],
    ...      [1, 1, 1],
    ...      [0, 1, 1],
    ...      [0, 2, 1]],
    ...    dtype=np.float64
    ... )
    >>> coder = SparseCoder(
    ...     dictionary=dictionary, transform_algorithm='lasso_lars',
    ...     transform_alpha=1e-10,
    ... )
    >>> coder.transform(X)
    array([[ 0.,  0., -1.,  0.,  0.],
           [ 0.,  1.,  1.,  0.,  0.]])
    """
    dictionary: Incomplete
    def __init__(self, dictionary, *, transform_algorithm: str = 'omp', transform_n_nonzero_coefs: Incomplete | None = None, transform_alpha: Incomplete | None = None, split_sign: bool = False, n_jobs: Incomplete | None = None, positive_code: bool = False, transform_max_iter: int = 1000) -> None: ...
    def fit(self, X, y: Incomplete | None = None):
        """Do nothing and return the estimator unchanged.

        This method is just there to implement the usual API and hence
        work in pipelines.

        Parameters
        ----------
        X : Ignored
            Not used, present for API consistency by convention.

        y : Ignored
            Not used, present for API consistency by convention.

        Returns
        -------
        self : object
            Returns the instance itself.
        """
    def transform(self, X, y: Incomplete | None = None):
        """Encode the data as a sparse combination of the dictionary atoms.

        Coding method is determined by the object parameter
        `transform_algorithm`.

        Parameters
        ----------
        X : ndarray of shape (n_samples, n_features)
            Training vector, where `n_samples` is the number of samples
            and `n_features` is the number of features.

        y : Ignored
            Not used, present for API consistency by convention.

        Returns
        -------
        X_new : ndarray of shape (n_samples, n_components)
            Transformed data.
        """
    @property
    def n_components_(self):
        """Number of atoms."""
    @property
    def n_features_in_(self):
        """Number of features seen during `fit`."""

class DictionaryLearning(_BaseSparseCoding, BaseEstimator):
    """Dictionary learning.

    Finds a dictionary (a set of atoms) that performs well at sparsely
    encoding the fitted data.

    Solves the optimization problem::

        (U^*,V^*) = argmin 0.5 || X - U V ||_Fro^2 + alpha * || U ||_1,1
                    (U,V)
                    with || V_k ||_2 <= 1 for all  0 <= k < n_components

    ||.||_Fro stands for the Frobenius norm and ||.||_1,1 stands for
    the entry-wise matrix norm which is the sum of the absolute values
    of all the entries in the matrix.

    Read more in the :ref:`User Guide <DictionaryLearning>`.

    Parameters
    ----------
    n_components : int, default=None
        Number of dictionary elements to extract. If None, then ``n_components``
        is set to ``n_features``.

    alpha : float, default=1.0
        Sparsity controlling parameter.

    max_iter : int, default=1000
        Maximum number of iterations to perform.

    tol : float, default=1e-8
        Tolerance for numerical error.

    fit_algorithm : {'lars', 'cd'}, default='lars'
        * `'lars'`: uses the least angle regression method to solve the lasso
          problem (:func:`~sklearn.linear_model.lars_path`);
        * `'cd'`: uses the coordinate descent method to compute the
          Lasso solution (:class:`~sklearn.linear_model.Lasso`). Lars will be
          faster if the estimated components are sparse.

        .. versionadded:: 0.17
           *cd* coordinate descent method to improve speed.

    transform_algorithm : {'lasso_lars', 'lasso_cd', 'lars', 'omp',             'threshold'}, default='omp'
        Algorithm used to transform the data:

        - `'lars'`: uses the least angle regression method
          (:func:`~sklearn.linear_model.lars_path`);
        - `'lasso_lars'`: uses Lars to compute the Lasso solution.
        - `'lasso_cd'`: uses the coordinate descent method to compute the
          Lasso solution (:class:`~sklearn.linear_model.Lasso`). `'lasso_lars'`
          will be faster if the estimated components are sparse.
        - `'omp'`: uses orthogonal matching pursuit to estimate the sparse
          solution.
        - `'threshold'`: squashes to zero all coefficients less than alpha from
          the projection ``dictionary * X'``.

        .. versionadded:: 0.17
           *lasso_cd* coordinate descent method to improve speed.

    transform_n_nonzero_coefs : int, default=None
        Number of nonzero coefficients to target in each column of the
        solution. This is only used by `algorithm='lars'` and
        `algorithm='omp'`. If `None`, then
        `transform_n_nonzero_coefs=int(n_features / 10)`.

    transform_alpha : float, default=None
        If `algorithm='lasso_lars'` or `algorithm='lasso_cd'`, `alpha` is the
        penalty applied to the L1 norm.
        If `algorithm='threshold'`, `alpha` is the absolute value of the
        threshold below which coefficients will be squashed to zero.
        If `None`, defaults to `alpha`.

        .. versionchanged:: 1.2
            When None, default value changed from 1.0 to `alpha`.

    n_jobs : int or None, default=None
        Number of parallel jobs to run.
        ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
        ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
        for more details.

    code_init : ndarray of shape (n_samples, n_components), default=None
        Initial value for the code, for warm restart. Only used if `code_init`
        and `dict_init` are not None.

    dict_init : ndarray of shape (n_components, n_features), default=None
        Initial values for the dictionary, for warm restart. Only used if
        `code_init` and `dict_init` are not None.

    callback : callable, default=None
        Callable that gets invoked every five iterations.

        .. versionadded:: 1.3

    verbose : bool, default=False
        To control the verbosity of the procedure.

    split_sign : bool, default=False
        Whether to split the sparse feature vector into the concatenation of
        its negative part and its positive part. This can improve the
        performance of downstream classifiers.

    random_state : int, RandomState instance or None, default=None
        Used for initializing the dictionary when ``dict_init`` is not
        specified, randomly shuffling the data when ``shuffle`` is set to
        ``True``, and updating the dictionary. Pass an int for reproducible
        results across multiple function calls.
        See :term:`Glossary <random_state>`.

    positive_code : bool, default=False
        Whether to enforce positivity when finding the code.

        .. versionadded:: 0.20

    positive_dict : bool, default=False
        Whether to enforce positivity when finding the dictionary.

        .. versionadded:: 0.20

    transform_max_iter : int, default=1000
        Maximum number of iterations to perform if `algorithm='lasso_cd'` or
        `'lasso_lars'`.

        .. versionadded:: 0.22

    Attributes
    ----------
    components_ : ndarray of shape (n_components, n_features)
        dictionary atoms extracted from the data

    error_ : array
        vector of errors at each iteration

    n_features_in_ : int
        Number of features seen during :term:`fit`.

        .. versionadded:: 0.24

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

        .. versionadded:: 1.0

    n_iter_ : int
        Number of iterations run.

    See Also
    --------
    MiniBatchDictionaryLearning: A faster, less accurate, version of the
        dictionary learning algorithm.
    MiniBatchSparsePCA : Mini-batch Sparse Principal Components Analysis.
    SparseCoder : Find a sparse representation of data from a fixed,
        precomputed dictionary.
    SparsePCA : Sparse Principal Components Analysis.

    References
    ----------

    J. Mairal, F. Bach, J. Ponce, G. Sapiro, 2009: Online dictionary learning
    for sparse coding (https://www.di.ens.fr/sierra/pdfs/icml09.pdf)

    Examples
    --------
    >>> import numpy as np
    >>> from sklearn.datasets import make_sparse_coded_signal
    >>> from sklearn.decomposition import DictionaryLearning
    >>> X, dictionary, code = make_sparse_coded_signal(
    ...     n_samples=100, n_components=15, n_features=20, n_nonzero_coefs=10,
    ...     random_state=42,
    ... )
    >>> dict_learner = DictionaryLearning(
    ...     n_components=15, transform_algorithm='lasso_lars', transform_alpha=0.1,
    ...     random_state=42,
    ... )
    >>> X_transformed = dict_learner.fit(X).transform(X)

    We can check the level of sparsity of `X_transformed`:

    >>> np.mean(X_transformed == 0)
    0.41...

    We can compare the average squared euclidean norm of the reconstruction
    error of the sparse coded signal relative to the squared euclidean norm of
    the original signal:

    >>> X_hat = X_transformed @ dict_learner.components_
    >>> np.mean(np.sum((X_hat - X) ** 2, axis=1) / np.sum(X ** 2, axis=1))
    0.07...
    """
    n_components: Incomplete
    alpha: Incomplete
    max_iter: Incomplete
    tol: Incomplete
    fit_algorithm: Incomplete
    code_init: Incomplete
    dict_init: Incomplete
    callback: Incomplete
    verbose: Incomplete
    random_state: Incomplete
    positive_dict: Incomplete
    def __init__(self, n_components: Incomplete | None = None, *, alpha: int = 1, max_iter: int = 1000, tol: float = 1e-08, fit_algorithm: str = 'lars', transform_algorithm: str = 'omp', transform_n_nonzero_coefs: Incomplete | None = None, transform_alpha: Incomplete | None = None, n_jobs: Incomplete | None = None, code_init: Incomplete | None = None, dict_init: Incomplete | None = None, callback: Incomplete | None = None, verbose: bool = False, split_sign: bool = False, random_state: Incomplete | None = None, positive_code: bool = False, positive_dict: bool = False, transform_max_iter: int = 1000) -> None: ...
    def fit(self, X, y: Incomplete | None = None):
        """Fit the model from data in X.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Training vector, where `n_samples` is the number of samples
            and `n_features` is the number of features.

        y : Ignored
            Not used, present for API consistency by convention.

        Returns
        -------
        self : object
            Returns the instance itself.
        """
    components_: Incomplete
    error_: Incomplete
    def fit_transform(self, X, y: Incomplete | None = None):
        """Fit the model from data in X and return the transformed data.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Training vector, where `n_samples` is the number of samples
            and `n_features` is the number of features.

        y : Ignored
            Not used, present for API consistency by convention.

        Returns
        -------
        V : ndarray of shape (n_samples, n_components)
            Transformed data.
        """

class MiniBatchDictionaryLearning(_BaseSparseCoding, BaseEstimator):
    """Mini-batch dictionary learning.

    Finds a dictionary (a set of atoms) that performs well at sparsely
    encoding the fitted data.

    Solves the optimization problem::

       (U^*,V^*) = argmin 0.5 || X - U V ||_Fro^2 + alpha * || U ||_1,1
                    (U,V)
                    with || V_k ||_2 <= 1 for all  0 <= k < n_components

    ||.||_Fro stands for the Frobenius norm and ||.||_1,1 stands for
    the entry-wise matrix norm which is the sum of the absolute values
    of all the entries in the matrix.

    Read more in the :ref:`User Guide <DictionaryLearning>`.

    Parameters
    ----------
    n_components : int, default=None
        Number of dictionary elements to extract.

    alpha : float, default=1
        Sparsity controlling parameter.

    n_iter : int, default=1000
        Total number of iterations over data batches to perform.

        .. deprecated:: 1.1
           ``n_iter`` is deprecated in 1.1 and will be removed in 1.4. Use
           ``max_iter`` instead.

    max_iter : int, default=None
        Maximum number of iterations over the complete dataset before
        stopping independently of any early stopping criterion heuristics.
        If ``max_iter`` is not None, ``n_iter`` is ignored.

        .. versionadded:: 1.1

    fit_algorithm : {'lars', 'cd'}, default='lars'
        The algorithm used:

        - `'lars'`: uses the least angle regression method to solve the lasso
          problem (`linear_model.lars_path`)
        - `'cd'`: uses the coordinate descent method to compute the
          Lasso solution (`linear_model.Lasso`). Lars will be faster if
          the estimated components are sparse.

    n_jobs : int, default=None
        Number of parallel jobs to run.
        ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
        ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
        for more details.

    batch_size : int, default=256
        Number of samples in each mini-batch.

        .. versionchanged:: 1.3
           The default value of `batch_size` changed from 3 to 256 in version 1.3.

    shuffle : bool, default=True
        Whether to shuffle the samples before forming batches.

    dict_init : ndarray of shape (n_components, n_features), default=None
        Initial value of the dictionary for warm restart scenarios.

    transform_algorithm : {'lasso_lars', 'lasso_cd', 'lars', 'omp',             'threshold'}, default='omp'
        Algorithm used to transform the data:

        - `'lars'`: uses the least angle regression method
          (`linear_model.lars_path`);
        - `'lasso_lars'`: uses Lars to compute the Lasso solution.
        - `'lasso_cd'`: uses the coordinate descent method to compute the
          Lasso solution (`linear_model.Lasso`). `'lasso_lars'` will be faster
          if the estimated components are sparse.
        - `'omp'`: uses orthogonal matching pursuit to estimate the sparse
          solution.
        - `'threshold'`: squashes to zero all coefficients less than alpha from
          the projection ``dictionary * X'``.

    transform_n_nonzero_coefs : int, default=None
        Number of nonzero coefficients to target in each column of the
        solution. This is only used by `algorithm='lars'` and
        `algorithm='omp'`. If `None`, then
        `transform_n_nonzero_coefs=int(n_features / 10)`.

    transform_alpha : float, default=None
        If `algorithm='lasso_lars'` or `algorithm='lasso_cd'`, `alpha` is the
        penalty applied to the L1 norm.
        If `algorithm='threshold'`, `alpha` is the absolute value of the
        threshold below which coefficients will be squashed to zero.
        If `None`, defaults to `alpha`.

        .. versionchanged:: 1.2
            When None, default value changed from 1.0 to `alpha`.

    verbose : bool or int, default=False
        To control the verbosity of the procedure.

    split_sign : bool, default=False
        Whether to split the sparse feature vector into the concatenation of
        its negative part and its positive part. This can improve the
        performance of downstream classifiers.

    random_state : int, RandomState instance or None, default=None
        Used for initializing the dictionary when ``dict_init`` is not
        specified, randomly shuffling the data when ``shuffle`` is set to
        ``True``, and updating the dictionary. Pass an int for reproducible
        results across multiple function calls.
        See :term:`Glossary <random_state>`.

    positive_code : bool, default=False
        Whether to enforce positivity when finding the code.

        .. versionadded:: 0.20

    positive_dict : bool, default=False
        Whether to enforce positivity when finding the dictionary.

        .. versionadded:: 0.20

    transform_max_iter : int, default=1000
        Maximum number of iterations to perform if `algorithm='lasso_cd'` or
        `'lasso_lars'`.

        .. versionadded:: 0.22

    callback : callable, default=None
        A callable that gets invoked at the end of each iteration.

        .. versionadded:: 1.1

    tol : float, default=1e-3
        Control early stopping based on the norm of the differences in the
        dictionary between 2 steps. Used only if `max_iter` is not None.

        To disable early stopping based on changes in the dictionary, set
        `tol` to 0.0.

        .. versionadded:: 1.1

    max_no_improvement : int, default=10
        Control early stopping based on the consecutive number of mini batches
        that does not yield an improvement on the smoothed cost function. Used only if
        `max_iter` is not None.

        To disable convergence detection based on cost function, set
        `max_no_improvement` to None.

        .. versionadded:: 1.1

    Attributes
    ----------
    components_ : ndarray of shape (n_components, n_features)
        Components extracted from the data.

    n_features_in_ : int
        Number of features seen during :term:`fit`.

        .. versionadded:: 0.24

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

        .. versionadded:: 1.0

    n_iter_ : int
        Number of iterations over the full dataset.

    n_steps_ : int
        Number of mini-batches processed.

        .. versionadded:: 1.1

    See Also
    --------
    DictionaryLearning : Find a dictionary that sparsely encodes data.
    MiniBatchSparsePCA : Mini-batch Sparse Principal Components Analysis.
    SparseCoder : Find a sparse representation of data from a fixed,
        precomputed dictionary.
    SparsePCA : Sparse Principal Components Analysis.

    References
    ----------

    J. Mairal, F. Bach, J. Ponce, G. Sapiro, 2009: Online dictionary learning
    for sparse coding (https://www.di.ens.fr/sierra/pdfs/icml09.pdf)

    Examples
    --------
    >>> import numpy as np
    >>> from sklearn.datasets import make_sparse_coded_signal
    >>> from sklearn.decomposition import MiniBatchDictionaryLearning
    >>> X, dictionary, code = make_sparse_coded_signal(
    ...     n_samples=100, n_components=15, n_features=20, n_nonzero_coefs=10,
    ...     random_state=42)
    >>> dict_learner = MiniBatchDictionaryLearning(
    ...     n_components=15, batch_size=3, transform_algorithm='lasso_lars',
    ...     transform_alpha=0.1, random_state=42)
    >>> X_transformed = dict_learner.fit_transform(X)

    We can check the level of sparsity of `X_transformed`:

    >>> np.mean(X_transformed == 0) < 0.5
    True

    We can compare the average squared euclidean norm of the reconstruction
    error of the sparse coded signal relative to the squared euclidean norm of
    the original signal:

    >>> X_hat = X_transformed @ dict_learner.components_
    >>> np.mean(np.sum((X_hat - X) ** 2, axis=1) / np.sum(X ** 2, axis=1))
    0.057...
    """
    n_components: Incomplete
    alpha: Incomplete
    n_iter: Incomplete
    max_iter: Incomplete
    fit_algorithm: Incomplete
    dict_init: Incomplete
    verbose: Incomplete
    shuffle: Incomplete
    batch_size: Incomplete
    split_sign: Incomplete
    random_state: Incomplete
    positive_dict: Incomplete
    callback: Incomplete
    max_no_improvement: Incomplete
    tol: Incomplete
    def __init__(self, n_components: Incomplete | None = None, *, alpha: int = 1, n_iter: str = 'deprecated', max_iter: Incomplete | None = None, fit_algorithm: str = 'lars', n_jobs: Incomplete | None = None, batch_size: int = 256, shuffle: bool = True, dict_init: Incomplete | None = None, transform_algorithm: str = 'omp', transform_n_nonzero_coefs: Incomplete | None = None, transform_alpha: Incomplete | None = None, verbose: bool = False, split_sign: bool = False, random_state: Incomplete | None = None, positive_code: bool = False, positive_dict: bool = False, transform_max_iter: int = 1000, callback: Incomplete | None = None, tol: float = 0.001, max_no_improvement: int = 10) -> None: ...
    n_steps_: Incomplete
    n_iter_: Incomplete
    components_: Incomplete
    def fit(self, X, y: Incomplete | None = None):
        """Fit the model from data in X.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Training vector, where `n_samples` is the number of samples
            and `n_features` is the number of features.

        y : Ignored
            Not used, present for API consistency by convention.

        Returns
        -------
        self : object
            Returns the instance itself.
        """
    def partial_fit(self, X, y: Incomplete | None = None):
        """Update the model using the data in X as a mini-batch.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Training vector, where `n_samples` is the number of samples
            and `n_features` is the number of features.

        y : Ignored
            Not used, present for API consistency by convention.

        Returns
        -------
        self : object
            Return the instance itself.
        """
