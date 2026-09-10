from . import EmpiricalCovariance as EmpiricalCovariance, empirical_covariance as empirical_covariance, log_likelihood as log_likelihood
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from ..linear_model import lars_path_gram as lars_path_gram
from ..model_selection import check_cv as check_cv, cross_val_score as cross_val_score
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions, validate_params as validate_params
from ..utils.parallel import Parallel as Parallel, delayed as delayed
from ..utils.validation import check_random_state as check_random_state, check_scalar as check_scalar
from _typeshed import Incomplete

def alpha_max(emp_cov):
    """Find the maximum alpha for which there are some non-zeros off-diagonal.

    Parameters
    ----------
    emp_cov : ndarray of shape (n_features, n_features)
        The sample covariance matrix.

    Notes
    -----
    This results from the bound for the all the Lasso that are solved
    in GraphicalLasso: each time, the row of cov corresponds to Xy. As the
    bound for alpha is given by `max(abs(Xy))`, the result follows.
    """
def graphical_lasso(emp_cov, alpha, *, cov_init: Incomplete | None = None, mode: str = 'cd', tol: float = 0.0001, enet_tol: float = 0.0001, max_iter: int = 100, verbose: bool = False, return_costs: bool = False, eps=..., return_n_iter: bool = False):
    """L1-penalized covariance estimator.

    Read more in the :ref:`User Guide <sparse_inverse_covariance>`.

    .. versionchanged:: v0.20
        graph_lasso has been renamed to graphical_lasso

    Parameters
    ----------
    emp_cov : array-like of shape (n_features, n_features)
        Empirical covariance from which to compute the covariance estimate.

    alpha : float
        The regularization parameter: the higher alpha, the more
        regularization, the sparser the inverse covariance.
        Range is (0, inf].

    cov_init : array of shape (n_features, n_features), default=None
        The initial guess for the covariance. If None, then the empirical
        covariance is used.

        .. deprecated:: 1.3
           `cov_init` is deprecated in 1.3 and will be removed in 1.5.
           It currently has no effect.

    mode : {'cd', 'lars'}, default='cd'
        The Lasso solver to use: coordinate descent or LARS. Use LARS for
        very sparse underlying graphs, where p > n. Elsewhere prefer cd
        which is more numerically stable.

    tol : float, default=1e-4
        The tolerance to declare convergence: if the dual gap goes below
        this value, iterations are stopped. Range is (0, inf].

    enet_tol : float, default=1e-4
        The tolerance for the elastic net solver used to calculate the descent
        direction. This parameter controls the accuracy of the search direction
        for a given column update, not of the overall parameter estimate. Only
        used for mode='cd'. Range is (0, inf].

    max_iter : int, default=100
        The maximum number of iterations.

    verbose : bool, default=False
        If verbose is True, the objective function and dual gap are
        printed at each iteration.

    return_costs : bool, default=False
        If return_costs is True, the objective function and dual gap
        at each iteration are returned.

    eps : float, default=eps
        The machine-precision regularization in the computation of the
        Cholesky diagonal factors. Increase this for very ill-conditioned
        systems. Default is `np.finfo(np.float64).eps`.

    return_n_iter : bool, default=False
        Whether or not to return the number of iterations.

    Returns
    -------
    covariance : ndarray of shape (n_features, n_features)
        The estimated covariance matrix.

    precision : ndarray of shape (n_features, n_features)
        The estimated (sparse) precision matrix.

    costs : list of (objective, dual_gap) pairs
        The list of values of the objective function and the dual gap at
        each iteration. Returned only if return_costs is True.

    n_iter : int
        Number of iterations. Returned only if `return_n_iter` is set to True.

    See Also
    --------
    GraphicalLasso : Sparse inverse covariance estimation
        with an l1-penalized estimator.
    GraphicalLassoCV : Sparse inverse covariance with
        cross-validated choice of the l1 penalty.

    Notes
    -----
    The algorithm employed to solve this problem is the GLasso algorithm,
    from the Friedman 2008 Biostatistics paper. It is the same algorithm
    as in the R `glasso` package.

    One possible difference with the `glasso` R package is that the
    diagonal coefficients are not penalized.
    """

class BaseGraphicalLasso(EmpiricalCovariance):
    tol: Incomplete
    enet_tol: Incomplete
    max_iter: Incomplete
    mode: Incomplete
    verbose: Incomplete
    eps: Incomplete
    def __init__(self, tol: float = 0.0001, enet_tol: float = 0.0001, max_iter: int = 100, mode: str = 'cd', verbose: bool = False, eps=..., assume_centered: bool = False) -> None: ...

class GraphicalLasso(BaseGraphicalLasso):
    '''Sparse inverse covariance estimation with an l1-penalized estimator.

    Read more in the :ref:`User Guide <sparse_inverse_covariance>`.

    .. versionchanged:: v0.20
        GraphLasso has been renamed to GraphicalLasso

    Parameters
    ----------
    alpha : float, default=0.01
        The regularization parameter: the higher alpha, the more
        regularization, the sparser the inverse covariance.
        Range is (0, inf].

    mode : {\'cd\', \'lars\'}, default=\'cd\'
        The Lasso solver to use: coordinate descent or LARS. Use LARS for
        very sparse underlying graphs, where p > n. Elsewhere prefer cd
        which is more numerically stable.

    covariance : "precomputed", default=None
        If covariance is "precomputed", the input data in `fit` is assumed
        to be the covariance matrix. If `None`, the empirical covariance
        is estimated from the data `X`.

        .. versionadded:: 1.3

    tol : float, default=1e-4
        The tolerance to declare convergence: if the dual gap goes below
        this value, iterations are stopped. Range is (0, inf].

    enet_tol : float, default=1e-4
        The tolerance for the elastic net solver used to calculate the descent
        direction. This parameter controls the accuracy of the search direction
        for a given column update, not of the overall parameter estimate. Only
        used for mode=\'cd\'. Range is (0, inf].

    max_iter : int, default=100
        The maximum number of iterations.

    verbose : bool, default=False
        If verbose is True, the objective function and dual gap are
        plotted at each iteration.

    eps : float, default=eps
        The machine-precision regularization in the computation of the
        Cholesky diagonal factors. Increase this for very ill-conditioned
        systems. Default is `np.finfo(np.float64).eps`.

        .. versionadded:: 1.3

    assume_centered : bool, default=False
        If True, data are not centered before computation.
        Useful when working with data whose mean is almost, but not exactly
        zero.
        If False, data are centered before computation.

    Attributes
    ----------
    location_ : ndarray of shape (n_features,)
        Estimated location, i.e. the estimated mean.

    covariance_ : ndarray of shape (n_features, n_features)
        Estimated covariance matrix

    precision_ : ndarray of shape (n_features, n_features)
        Estimated pseudo inverse matrix.

    n_iter_ : int
        Number of iterations run.

    costs_ : list of (objective, dual_gap) pairs
        The list of values of the objective function and the dual gap at
        each iteration. Returned only if return_costs is True.

        .. versionadded:: 1.3

    n_features_in_ : int
        Number of features seen during :term:`fit`.

        .. versionadded:: 0.24

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

        .. versionadded:: 1.0

    See Also
    --------
    graphical_lasso : L1-penalized covariance estimator.
    GraphicalLassoCV : Sparse inverse covariance with
        cross-validated choice of the l1 penalty.

    Examples
    --------
    >>> import numpy as np
    >>> from sklearn.covariance import GraphicalLasso
    >>> true_cov = np.array([[0.8, 0.0, 0.2, 0.0],
    ...                      [0.0, 0.4, 0.0, 0.0],
    ...                      [0.2, 0.0, 0.3, 0.1],
    ...                      [0.0, 0.0, 0.1, 0.7]])
    >>> np.random.seed(0)
    >>> X = np.random.multivariate_normal(mean=[0, 0, 0, 0],
    ...                                   cov=true_cov,
    ...                                   size=200)
    >>> cov = GraphicalLasso().fit(X)
    >>> np.around(cov.covariance_, decimals=3)
    array([[0.816, 0.049, 0.218, 0.019],
           [0.049, 0.364, 0.017, 0.034],
           [0.218, 0.017, 0.322, 0.093],
           [0.019, 0.034, 0.093, 0.69 ]])
    >>> np.around(cov.location_, decimals=3)
    array([0.073, 0.04 , 0.038, 0.143])
    '''
    alpha: Incomplete
    covariance: Incomplete
    def __init__(self, alpha: float = 0.01, *, mode: str = 'cd', covariance: Incomplete | None = None, tol: float = 0.0001, enet_tol: float = 0.0001, max_iter: int = 100, verbose: bool = False, eps=..., assume_centered: bool = False) -> None: ...
    location_: Incomplete
    def fit(self, X, y: Incomplete | None = None):
        """Fit the GraphicalLasso model to X.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Data from which to compute the covariance estimate.

        y : Ignored
            Not used, present for API consistency by convention.

        Returns
        -------
        self : object
            Returns the instance itself.
        """

def graphical_lasso_path(X, alphas, cov_init: Incomplete | None = None, X_test: Incomplete | None = None, mode: str = 'cd', tol: float = 0.0001, enet_tol: float = 0.0001, max_iter: int = 100, verbose: bool = False, eps=...):
    """l1-penalized covariance estimator along a path of decreasing alphas

    Read more in the :ref:`User Guide <sparse_inverse_covariance>`.

    Parameters
    ----------
    X : ndarray of shape (n_samples, n_features)
        Data from which to compute the covariance estimate.

    alphas : array-like of shape (n_alphas,)
        The list of regularization parameters, decreasing order.

    cov_init : array of shape (n_features, n_features), default=None
        The initial guess for the covariance.

    X_test : array of shape (n_test_samples, n_features), default=None
        Optional test matrix to measure generalisation error.

    mode : {'cd', 'lars'}, default='cd'
        The Lasso solver to use: coordinate descent or LARS. Use LARS for
        very sparse underlying graphs, where p > n. Elsewhere prefer cd
        which is more numerically stable.

    tol : float, default=1e-4
        The tolerance to declare convergence: if the dual gap goes below
        this value, iterations are stopped. The tolerance must be a positive
        number.

    enet_tol : float, default=1e-4
        The tolerance for the elastic net solver used to calculate the descent
        direction. This parameter controls the accuracy of the search direction
        for a given column update, not of the overall parameter estimate. Only
        used for mode='cd'. The tolerance must be a positive number.

    max_iter : int, default=100
        The maximum number of iterations. This parameter should be a strictly
        positive integer.

    verbose : int or bool, default=False
        The higher the verbosity flag, the more information is printed
        during the fitting.

    eps : float, default=eps
        The machine-precision regularization in the computation of the
        Cholesky diagonal factors. Increase this for very ill-conditioned
        systems. Default is `np.finfo(np.float64).eps`.

        .. versionadded:: 1.3

    Returns
    -------
    covariances_ : list of shape (n_alphas,) of ndarray of shape             (n_features, n_features)
        The estimated covariance matrices.

    precisions_ : list of shape (n_alphas,) of ndarray of shape             (n_features, n_features)
        The estimated (sparse) precision matrices.

    scores_ : list of shape (n_alphas,), dtype=float
        The generalisation error (log-likelihood) on the test data.
        Returned only if test data is passed.
    """

class GraphicalLassoCV(BaseGraphicalLasso):
    """Sparse inverse covariance w/ cross-validated choice of the l1 penalty.

    See glossary entry for :term:`cross-validation estimator`.

    Read more in the :ref:`User Guide <sparse_inverse_covariance>`.

    .. versionchanged:: v0.20
        GraphLassoCV has been renamed to GraphicalLassoCV

    Parameters
    ----------
    alphas : int or array-like of shape (n_alphas,), dtype=float, default=4
        If an integer is given, it fixes the number of points on the
        grids of alpha to be used. If a list is given, it gives the
        grid to be used. See the notes in the class docstring for
        more details. Range is [1, inf) for an integer.
        Range is (0, inf] for an array-like of floats.

    n_refinements : int, default=4
        The number of times the grid is refined. Not used if explicit
        values of alphas are passed. Range is [1, inf).

    cv : int, cross-validation generator or iterable, default=None
        Determines the cross-validation splitting strategy.
        Possible inputs for cv are:

        - None, to use the default 5-fold cross-validation,
        - integer, to specify the number of folds.
        - :term:`CV splitter`,
        - An iterable yielding (train, test) splits as arrays of indices.

        For integer/None inputs :class:`KFold` is used.

        Refer :ref:`User Guide <cross_validation>` for the various
        cross-validation strategies that can be used here.

        .. versionchanged:: 0.20
            ``cv`` default value if None changed from 3-fold to 5-fold.

    tol : float, default=1e-4
        The tolerance to declare convergence: if the dual gap goes below
        this value, iterations are stopped. Range is (0, inf].

    enet_tol : float, default=1e-4
        The tolerance for the elastic net solver used to calculate the descent
        direction. This parameter controls the accuracy of the search direction
        for a given column update, not of the overall parameter estimate. Only
        used for mode='cd'. Range is (0, inf].

    max_iter : int, default=100
        Maximum number of iterations.

    mode : {'cd', 'lars'}, default='cd'
        The Lasso solver to use: coordinate descent or LARS. Use LARS for
        very sparse underlying graphs, where number of features is greater
        than number of samples. Elsewhere prefer cd which is more numerically
        stable.

    n_jobs : int, default=None
        Number of jobs to run in parallel.
        ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
        ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
        for more details.

        .. versionchanged:: v0.20
           `n_jobs` default changed from 1 to None

    verbose : bool, default=False
        If verbose is True, the objective function and duality gap are
        printed at each iteration.

    eps : float, default=eps
        The machine-precision regularization in the computation of the
        Cholesky diagonal factors. Increase this for very ill-conditioned
        systems. Default is `np.finfo(np.float64).eps`.

        .. versionadded:: 1.3

    assume_centered : bool, default=False
        If True, data are not centered before computation.
        Useful when working with data whose mean is almost, but not exactly
        zero.
        If False, data are centered before computation.

    Attributes
    ----------
    location_ : ndarray of shape (n_features,)
        Estimated location, i.e. the estimated mean.

    covariance_ : ndarray of shape (n_features, n_features)
        Estimated covariance matrix.

    precision_ : ndarray of shape (n_features, n_features)
        Estimated precision matrix (inverse covariance).

    costs_ : list of (objective, dual_gap) pairs
        The list of values of the objective function and the dual gap at
        each iteration. Returned only if return_costs is True.

        .. versionadded:: 1.3

    alpha_ : float
        Penalization parameter selected.

    cv_results_ : dict of ndarrays
        A dict with keys:

        alphas : ndarray of shape (n_alphas,)
            All penalization parameters explored.

        split(k)_test_score : ndarray of shape (n_alphas,)
            Log-likelihood score on left-out data across (k)th fold.

            .. versionadded:: 1.0

        mean_test_score : ndarray of shape (n_alphas,)
            Mean of scores over the folds.

            .. versionadded:: 1.0

        std_test_score : ndarray of shape (n_alphas,)
            Standard deviation of scores over the folds.

            .. versionadded:: 1.0

    n_iter_ : int
        Number of iterations run for the optimal alpha.

    n_features_in_ : int
        Number of features seen during :term:`fit`.

        .. versionadded:: 0.24

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

        .. versionadded:: 1.0

    See Also
    --------
    graphical_lasso : L1-penalized covariance estimator.
    GraphicalLasso : Sparse inverse covariance estimation
        with an l1-penalized estimator.

    Notes
    -----
    The search for the optimal penalization parameter (`alpha`) is done on an
    iteratively refined grid: first the cross-validated scores on a grid are
    computed, then a new refined grid is centered around the maximum, and so
    on.

    One of the challenges which is faced here is that the solvers can
    fail to converge to a well-conditioned estimate. The corresponding
    values of `alpha` then come out as missing values, but the optimum may
    be close to these missing values.

    In `fit`, once the best parameter `alpha` is found through
    cross-validation, the model is fit again using the entire training set.

    Examples
    --------
    >>> import numpy as np
    >>> from sklearn.covariance import GraphicalLassoCV
    >>> true_cov = np.array([[0.8, 0.0, 0.2, 0.0],
    ...                      [0.0, 0.4, 0.0, 0.0],
    ...                      [0.2, 0.0, 0.3, 0.1],
    ...                      [0.0, 0.0, 0.1, 0.7]])
    >>> np.random.seed(0)
    >>> X = np.random.multivariate_normal(mean=[0, 0, 0, 0],
    ...                                   cov=true_cov,
    ...                                   size=200)
    >>> cov = GraphicalLassoCV().fit(X)
    >>> np.around(cov.covariance_, decimals=3)
    array([[0.816, 0.051, 0.22 , 0.017],
           [0.051, 0.364, 0.018, 0.036],
           [0.22 , 0.018, 0.322, 0.094],
           [0.017, 0.036, 0.094, 0.69 ]])
    >>> np.around(cov.location_, decimals=3)
    array([0.073, 0.04 , 0.038, 0.143])
    """
    alphas: Incomplete
    n_refinements: Incomplete
    cv: Incomplete
    n_jobs: Incomplete
    def __init__(self, *, alphas: int = 4, n_refinements: int = 4, cv: Incomplete | None = None, tol: float = 0.0001, enet_tol: float = 0.0001, max_iter: int = 100, mode: str = 'cd', n_jobs: Incomplete | None = None, verbose: bool = False, eps=..., assume_centered: bool = False) -> None: ...
    location_: Incomplete
    cv_results_: Incomplete
    alpha_: Incomplete
    def fit(self, X, y: Incomplete | None = None):
        """Fit the GraphicalLasso covariance model to X.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Data from which to compute the covariance estimate.

        y : Ignored
            Not used, present for API consistency by convention.

        Returns
        -------
        self : object
            Returns the instance itself.
        """
