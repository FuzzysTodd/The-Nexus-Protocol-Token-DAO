from ..base import MultiOutputMixin as MultiOutputMixin, RegressorMixin as RegressorMixin, is_classifier as is_classifier
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from ..metrics import check_scoring as check_scoring, get_scorer_names as get_scorer_names
from ..model_selection import GridSearchCV as GridSearchCV
from ..preprocessing import LabelBinarizer as LabelBinarizer
from ..utils import check_array as check_array, check_consistent_length as check_consistent_length, check_scalar as check_scalar, column_or_1d as column_or_1d, compute_sample_weight as compute_sample_weight
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from ..utils.extmath import row_norms as row_norms, safe_sparse_dot as safe_sparse_dot
from ..utils.sparsefuncs import mean_variance_axis as mean_variance_axis
from ..utils.validation import check_is_fitted as check_is_fitted
from ._base import LinearClassifierMixin as LinearClassifierMixin, LinearModel as LinearModel
from ._sag import sag_solver as sag_solver
from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod
from scipy import sparse

def ridge_regression(X, y, alpha, *, sample_weight: Incomplete | None = None, solver: str = 'auto', max_iter: Incomplete | None = None, tol: float = 0.0001, verbose: int = 0, positive: bool = False, random_state: Incomplete | None = None, return_n_iter: bool = False, return_intercept: bool = False, check_input: bool = True):
    """Solve the ridge equation by the method of normal equations.

    Read more in the :ref:`User Guide <ridge_regression>`.

    Parameters
    ----------
    X : {ndarray, sparse matrix, LinearOperator} of shape         (n_samples, n_features)
        Training data.

    y : ndarray of shape (n_samples,) or (n_samples, n_targets)
        Target values.

    alpha : float or array-like of shape (n_targets,)
        Constant that multiplies the L2 term, controlling regularization
        strength. `alpha` must be a non-negative float i.e. in `[0, inf)`.

        When `alpha = 0`, the objective is equivalent to ordinary least
        squares, solved by the :class:`LinearRegression` object. For numerical
        reasons, using `alpha = 0` with the `Ridge` object is not advised.
        Instead, you should use the :class:`LinearRegression` object.

        If an array is passed, penalties are assumed to be specific to the
        targets. Hence they must correspond in number.

    sample_weight : float or array-like of shape (n_samples,), default=None
        Individual weights for each sample. If given a float, every sample
        will have the same weight. If sample_weight is not None and
        solver='auto', the solver will be set to 'cholesky'.

        .. versionadded:: 0.17

    solver : {'auto', 'svd', 'cholesky', 'lsqr', 'sparse_cg',             'sag', 'saga', 'lbfgs'}, default='auto'
        Solver to use in the computational routines:

        - 'auto' chooses the solver automatically based on the type of data.

        - 'svd' uses a Singular Value Decomposition of X to compute the Ridge
          coefficients. It is the most stable solver, in particular more stable
          for singular matrices than 'cholesky' at the cost of being slower.

        - 'cholesky' uses the standard scipy.linalg.solve function to
          obtain a closed-form solution via a Cholesky decomposition of
          dot(X.T, X)

        - 'sparse_cg' uses the conjugate gradient solver as found in
          scipy.sparse.linalg.cg. As an iterative algorithm, this solver is
          more appropriate than 'cholesky' for large-scale data
          (possibility to set `tol` and `max_iter`).

        - 'lsqr' uses the dedicated regularized least-squares routine
          scipy.sparse.linalg.lsqr. It is the fastest and uses an iterative
          procedure.

        - 'sag' uses a Stochastic Average Gradient descent, and 'saga' uses
          its improved, unbiased version named SAGA. Both methods also use an
          iterative procedure, and are often faster than other solvers when
          both n_samples and n_features are large. Note that 'sag' and
          'saga' fast convergence is only guaranteed on features with
          approximately the same scale. You can preprocess the data with a
          scaler from sklearn.preprocessing.

        - 'lbfgs' uses L-BFGS-B algorithm implemented in
          `scipy.optimize.minimize`. It can be used only when `positive`
          is True.

        All solvers except 'svd' support both dense and sparse data. However, only
        'lsqr', 'sag', 'sparse_cg', and 'lbfgs' support sparse input when
        `fit_intercept` is True.

        .. versionadded:: 0.17
           Stochastic Average Gradient descent solver.
        .. versionadded:: 0.19
           SAGA solver.

    max_iter : int, default=None
        Maximum number of iterations for conjugate gradient solver.
        For the 'sparse_cg' and 'lsqr' solvers, the default value is determined
        by scipy.sparse.linalg. For 'sag' and saga solver, the default value is
        1000. For 'lbfgs' solver, the default value is 15000.

    tol : float, default=1e-4
        Precision of the solution. Note that `tol` has no effect for solvers 'svd' and
        'cholesky'.

        .. versionchanged:: 1.2
           Default value changed from 1e-3 to 1e-4 for consistency with other linear
           models.

    verbose : int, default=0
        Verbosity level. Setting verbose > 0 will display additional
        information depending on the solver used.

    positive : bool, default=False
        When set to ``True``, forces the coefficients to be positive.
        Only 'lbfgs' solver is supported in this case.

    random_state : int, RandomState instance, default=None
        Used when ``solver`` == 'sag' or 'saga' to shuffle the data.
        See :term:`Glossary <random_state>` for details.

    return_n_iter : bool, default=False
        If True, the method also returns `n_iter`, the actual number of
        iteration performed by the solver.

        .. versionadded:: 0.17

    return_intercept : bool, default=False
        If True and if X is sparse, the method also returns the intercept,
        and the solver is automatically changed to 'sag'. This is only a
        temporary fix for fitting the intercept with sparse data. For dense
        data, use sklearn.linear_model._preprocess_data before your regression.

        .. versionadded:: 0.17

    check_input : bool, default=True
        If False, the input arrays X and y will not be checked.

        .. versionadded:: 0.21

    Returns
    -------
    coef : ndarray of shape (n_features,) or (n_targets, n_features)
        Weight vector(s).

    n_iter : int, optional
        The actual number of iteration performed by the solver.
        Only returned if `return_n_iter` is True.

    intercept : float or ndarray of shape (n_targets,)
        The intercept of the model. Only returned if `return_intercept`
        is True and if X is a scipy sparse array.

    Notes
    -----
    This function won't compute the intercept.

    Regularization improves the conditioning of the problem and
    reduces the variance of the estimates. Larger values specify stronger
    regularization. Alpha corresponds to ``1 / (2C)`` in other linear
    models such as :class:`~sklearn.linear_model.LogisticRegression` or
    :class:`~sklearn.svm.LinearSVC`. If an array is passed, penalties are
    assumed to be specific to the targets. Hence they must correspond in
    number.
    """

class _BaseRidge(LinearModel, metaclass=ABCMeta):
    alpha: Incomplete
    fit_intercept: Incomplete
    copy_X: Incomplete
    max_iter: Incomplete
    tol: Incomplete
    solver: Incomplete
    positive: Incomplete
    random_state: Incomplete
    @abstractmethod
    def __init__(self, alpha: float = 1.0, *, fit_intercept: bool = True, copy_X: bool = True, max_iter: Incomplete | None = None, tol: float = 0.0001, solver: str = 'auto', positive: bool = False, random_state: Incomplete | None = None): ...
    def fit(self, X, y, sample_weight: Incomplete | None = None): ...

class Ridge(MultiOutputMixin, RegressorMixin, _BaseRidge):
    """Linear least squares with l2 regularization.

    Minimizes the objective function::

    ||y - Xw||^2_2 + alpha * ||w||^2_2

    This model solves a regression model where the loss function is
    the linear least squares function and regularization is given by
    the l2-norm. Also known as Ridge Regression or Tikhonov regularization.
    This estimator has built-in support for multi-variate regression
    (i.e., when y is a 2d-array of shape (n_samples, n_targets)).

    Read more in the :ref:`User Guide <ridge_regression>`.

    Parameters
    ----------
    alpha : {float, ndarray of shape (n_targets,)}, default=1.0
        Constant that multiplies the L2 term, controlling regularization
        strength. `alpha` must be a non-negative float i.e. in `[0, inf)`.

        When `alpha = 0`, the objective is equivalent to ordinary least
        squares, solved by the :class:`LinearRegression` object. For numerical
        reasons, using `alpha = 0` with the `Ridge` object is not advised.
        Instead, you should use the :class:`LinearRegression` object.

        If an array is passed, penalties are assumed to be specific to the
        targets. Hence they must correspond in number.

    fit_intercept : bool, default=True
        Whether to fit the intercept for this model. If set
        to false, no intercept will be used in calculations
        (i.e. ``X`` and ``y`` are expected to be centered).

    copy_X : bool, default=True
        If True, X will be copied; else, it may be overwritten.

    max_iter : int, default=None
        Maximum number of iterations for conjugate gradient solver.
        For 'sparse_cg' and 'lsqr' solvers, the default value is determined
        by scipy.sparse.linalg. For 'sag' solver, the default value is 1000.
        For 'lbfgs' solver, the default value is 15000.

    tol : float, default=1e-4
        The precision of the solution (`coef_`) is determined by `tol` which
        specifies a different convergence criterion for each solver:

        - 'svd': `tol` has no impact.

        - 'cholesky': `tol` has no impact.

        - 'sparse_cg': norm of residuals smaller than `tol`.

        - 'lsqr': `tol` is set as atol and btol of scipy.sparse.linalg.lsqr,
          which control the norm of the residual vector in terms of the norms of
          matrix and coefficients.

        - 'sag' and 'saga': relative change of coef smaller than `tol`.

        - 'lbfgs': maximum of the absolute (projected) gradient=max|residuals|
          smaller than `tol`.

        .. versionchanged:: 1.2
           Default value changed from 1e-3 to 1e-4 for consistency with other linear
           models.

    solver : {'auto', 'svd', 'cholesky', 'lsqr', 'sparse_cg',             'sag', 'saga', 'lbfgs'}, default='auto'
        Solver to use in the computational routines:

        - 'auto' chooses the solver automatically based on the type of data.

        - 'svd' uses a Singular Value Decomposition of X to compute the Ridge
          coefficients. It is the most stable solver, in particular more stable
          for singular matrices than 'cholesky' at the cost of being slower.

        - 'cholesky' uses the standard scipy.linalg.solve function to
          obtain a closed-form solution.

        - 'sparse_cg' uses the conjugate gradient solver as found in
          scipy.sparse.linalg.cg. As an iterative algorithm, this solver is
          more appropriate than 'cholesky' for large-scale data
          (possibility to set `tol` and `max_iter`).

        - 'lsqr' uses the dedicated regularized least-squares routine
          scipy.sparse.linalg.lsqr. It is the fastest and uses an iterative
          procedure.

        - 'sag' uses a Stochastic Average Gradient descent, and 'saga' uses
          its improved, unbiased version named SAGA. Both methods also use an
          iterative procedure, and are often faster than other solvers when
          both n_samples and n_features are large. Note that 'sag' and
          'saga' fast convergence is only guaranteed on features with
          approximately the same scale. You can preprocess the data with a
          scaler from sklearn.preprocessing.

        - 'lbfgs' uses L-BFGS-B algorithm implemented in
          `scipy.optimize.minimize`. It can be used only when `positive`
          is True.

        All solvers except 'svd' support both dense and sparse data. However, only
        'lsqr', 'sag', 'sparse_cg', and 'lbfgs' support sparse input when
        `fit_intercept` is True.

        .. versionadded:: 0.17
           Stochastic Average Gradient descent solver.
        .. versionadded:: 0.19
           SAGA solver.

    positive : bool, default=False
        When set to ``True``, forces the coefficients to be positive.
        Only 'lbfgs' solver is supported in this case.

    random_state : int, RandomState instance, default=None
        Used when ``solver`` == 'sag' or 'saga' to shuffle the data.
        See :term:`Glossary <random_state>` for details.

        .. versionadded:: 0.17
           `random_state` to support Stochastic Average Gradient.

    Attributes
    ----------
    coef_ : ndarray of shape (n_features,) or (n_targets, n_features)
        Weight vector(s).

    intercept_ : float or ndarray of shape (n_targets,)
        Independent term in decision function. Set to 0.0 if
        ``fit_intercept = False``.

    n_iter_ : None or ndarray of shape (n_targets,)
        Actual number of iterations for each target. Available only for
        sag and lsqr solvers. Other solvers will return None.

        .. versionadded:: 0.17

    n_features_in_ : int
        Number of features seen during :term:`fit`.

        .. versionadded:: 0.24

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

        .. versionadded:: 1.0

    See Also
    --------
    RidgeClassifier : Ridge classifier.
    RidgeCV : Ridge regression with built-in cross validation.
    :class:`~sklearn.kernel_ridge.KernelRidge` : Kernel ridge regression
        combines ridge regression with the kernel trick.

    Notes
    -----
    Regularization improves the conditioning of the problem and
    reduces the variance of the estimates. Larger values specify stronger
    regularization. Alpha corresponds to ``1 / (2C)`` in other linear
    models such as :class:`~sklearn.linear_model.LogisticRegression` or
    :class:`~sklearn.svm.LinearSVC`.

    Examples
    --------
    >>> from sklearn.linear_model import Ridge
    >>> import numpy as np
    >>> n_samples, n_features = 10, 5
    >>> rng = np.random.RandomState(0)
    >>> y = rng.randn(n_samples)
    >>> X = rng.randn(n_samples, n_features)
    >>> clf = Ridge(alpha=1.0)
    >>> clf.fit(X, y)
    Ridge()
    """
    def __init__(self, alpha: float = 1.0, *, fit_intercept: bool = True, copy_X: bool = True, max_iter: Incomplete | None = None, tol: float = 0.0001, solver: str = 'auto', positive: bool = False, random_state: Incomplete | None = None) -> None: ...
    def fit(self, X, y, sample_weight: Incomplete | None = None):
        """Fit Ridge regression model.

        Parameters
        ----------
        X : {ndarray, sparse matrix} of shape (n_samples, n_features)
            Training data.

        y : ndarray of shape (n_samples,) or (n_samples, n_targets)
            Target values.

        sample_weight : float or ndarray of shape (n_samples,), default=None
            Individual weights for each sample. If given a float, every sample
            will have the same weight.

        Returns
        -------
        self : object
            Fitted estimator.
        """

class _RidgeClassifierMixin(LinearClassifierMixin):
    def predict(self, X):
        """Predict class labels for samples in `X`.

        Parameters
        ----------
        X : {array-like, spare matrix} of shape (n_samples, n_features)
            The data matrix for which we want to predict the targets.

        Returns
        -------
        y_pred : ndarray of shape (n_samples,) or (n_samples, n_outputs)
            Vector or matrix containing the predictions. In binary and
            multiclass problems, this is a vector containing `n_samples`. In
            a multilabel problem, it returns a matrix of shape
            `(n_samples, n_outputs)`.
        """
    @property
    def classes_(self):
        """Classes labels."""

class RidgeClassifier(_RidgeClassifierMixin, _BaseRidge):
    '''Classifier using Ridge regression.

    This classifier first converts the target values into ``{-1, 1}`` and
    then treats the problem as a regression task (multi-output regression in
    the multiclass case).

    Read more in the :ref:`User Guide <ridge_regression>`.

    Parameters
    ----------
    alpha : float, default=1.0
        Regularization strength; must be a positive float. Regularization
        improves the conditioning of the problem and reduces the variance of
        the estimates. Larger values specify stronger regularization.
        Alpha corresponds to ``1 / (2C)`` in other linear models such as
        :class:`~sklearn.linear_model.LogisticRegression` or
        :class:`~sklearn.svm.LinearSVC`.

    fit_intercept : bool, default=True
        Whether to calculate the intercept for this model. If set to false, no
        intercept will be used in calculations (e.g. data is expected to be
        already centered).

    copy_X : bool, default=True
        If True, X will be copied; else, it may be overwritten.

    max_iter : int, default=None
        Maximum number of iterations for conjugate gradient solver.
        The default value is determined by scipy.sparse.linalg.

    tol : float, default=1e-4
        The precision of the solution (`coef_`) is determined by `tol` which
        specifies a different convergence criterion for each solver:

        - \'svd\': `tol` has no impact.

        - \'cholesky\': `tol` has no impact.

        - \'sparse_cg\': norm of residuals smaller than `tol`.

        - \'lsqr\': `tol` is set as atol and btol of scipy.sparse.linalg.lsqr,
          which control the norm of the residual vector in terms of the norms of
          matrix and coefficients.

        - \'sag\' and \'saga\': relative change of coef smaller than `tol`.

        - \'lbfgs\': maximum of the absolute (projected) gradient=max|residuals|
          smaller than `tol`.

        .. versionchanged:: 1.2
           Default value changed from 1e-3 to 1e-4 for consistency with other linear
           models.

    class_weight : dict or \'balanced\', default=None
        Weights associated with classes in the form ``{class_label: weight}``.
        If not given, all classes are supposed to have weight one.

        The "balanced" mode uses the values of y to automatically adjust
        weights inversely proportional to class frequencies in the input data
        as ``n_samples / (n_classes * np.bincount(y))``.

    solver : {\'auto\', \'svd\', \'cholesky\', \'lsqr\', \'sparse_cg\',             \'sag\', \'saga\', \'lbfgs\'}, default=\'auto\'
        Solver to use in the computational routines:

        - \'auto\' chooses the solver automatically based on the type of data.

        - \'svd\' uses a Singular Value Decomposition of X to compute the Ridge
          coefficients. It is the most stable solver, in particular more stable
          for singular matrices than \'cholesky\' at the cost of being slower.

        - \'cholesky\' uses the standard scipy.linalg.solve function to
          obtain a closed-form solution.

        - \'sparse_cg\' uses the conjugate gradient solver as found in
          scipy.sparse.linalg.cg. As an iterative algorithm, this solver is
          more appropriate than \'cholesky\' for large-scale data
          (possibility to set `tol` and `max_iter`).

        - \'lsqr\' uses the dedicated regularized least-squares routine
          scipy.sparse.linalg.lsqr. It is the fastest and uses an iterative
          procedure.

        - \'sag\' uses a Stochastic Average Gradient descent, and \'saga\' uses
          its unbiased and more flexible version named SAGA. Both methods
          use an iterative procedure, and are often faster than other solvers
          when both n_samples and n_features are large. Note that \'sag\' and
          \'saga\' fast convergence is only guaranteed on features with
          approximately the same scale. You can preprocess the data with a
          scaler from sklearn.preprocessing.

          .. versionadded:: 0.17
             Stochastic Average Gradient descent solver.
          .. versionadded:: 0.19
             SAGA solver.

        - \'lbfgs\' uses L-BFGS-B algorithm implemented in
          `scipy.optimize.minimize`. It can be used only when `positive`
          is True.

    positive : bool, default=False
        When set to ``True``, forces the coefficients to be positive.
        Only \'lbfgs\' solver is supported in this case.

    random_state : int, RandomState instance, default=None
        Used when ``solver`` == \'sag\' or \'saga\' to shuffle the data.
        See :term:`Glossary <random_state>` for details.

    Attributes
    ----------
    coef_ : ndarray of shape (1, n_features) or (n_classes, n_features)
        Coefficient of the features in the decision function.

        ``coef_`` is of shape (1, n_features) when the given problem is binary.

    intercept_ : float or ndarray of shape (n_targets,)
        Independent term in decision function. Set to 0.0 if
        ``fit_intercept = False``.

    n_iter_ : None or ndarray of shape (n_targets,)
        Actual number of iterations for each target. Available only for
        sag and lsqr solvers. Other solvers will return None.

    classes_ : ndarray of shape (n_classes,)
        The classes labels.

    n_features_in_ : int
        Number of features seen during :term:`fit`.

        .. versionadded:: 0.24

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

        .. versionadded:: 1.0

    See Also
    --------
    Ridge : Ridge regression.
    RidgeClassifierCV :  Ridge classifier with built-in cross validation.

    Notes
    -----
    For multi-class classification, n_class classifiers are trained in
    a one-versus-all approach. Concretely, this is implemented by taking
    advantage of the multi-variate response support in Ridge.

    Examples
    --------
    >>> from sklearn.datasets import load_breast_cancer
    >>> from sklearn.linear_model import RidgeClassifier
    >>> X, y = load_breast_cancer(return_X_y=True)
    >>> clf = RidgeClassifier().fit(X, y)
    >>> clf.score(X, y)
    0.9595...
    '''
    class_weight: Incomplete
    def __init__(self, alpha: float = 1.0, *, fit_intercept: bool = True, copy_X: bool = True, max_iter: Incomplete | None = None, tol: float = 0.0001, class_weight: Incomplete | None = None, solver: str = 'auto', positive: bool = False, random_state: Incomplete | None = None) -> None: ...
    def fit(self, X, y, sample_weight: Incomplete | None = None):
        """Fit Ridge classifier model.

        Parameters
        ----------
        X : {ndarray, sparse matrix} of shape (n_samples, n_features)
            Training data.

        y : ndarray of shape (n_samples,)
            Target values.

        sample_weight : float or ndarray of shape (n_samples,), default=None
            Individual weights for each sample. If given a float, every sample
            will have the same weight.

            .. versionadded:: 0.17
               *sample_weight* support to RidgeClassifier.

        Returns
        -------
        self : object
            Instance of the estimator.
        """

class _X_CenterStackOp(sparse.linalg.LinearOperator):
    """Behaves as centered and scaled X with an added intercept column.

    This operator behaves as
    np.hstack([X - sqrt_sw[:, None] * X_mean, sqrt_sw[:, None]])
    """
    X: Incomplete
    X_mean: Incomplete
    sqrt_sw: Incomplete
    def __init__(self, X, X_mean, sqrt_sw) -> None: ...

class _XT_CenterStackOp(sparse.linalg.LinearOperator):
    """Behaves as transposed centered and scaled X with an intercept column.

    This operator behaves as
    np.hstack([X - sqrt_sw[:, None] * X_mean, sqrt_sw[:, None]]).T
    """
    X: Incomplete
    X_mean: Incomplete
    sqrt_sw: Incomplete
    def __init__(self, X, X_mean, sqrt_sw) -> None: ...

class _IdentityRegressor:
    """Fake regressor which will directly output the prediction."""
    def decision_function(self, y_predict): ...
    def predict(self, y_predict): ...

class _IdentityClassifier(LinearClassifierMixin):
    """Fake classifier which will directly output the prediction.

    We inherit from LinearClassifierMixin to get the proper shape for the
    output `y`.
    """
    classes_: Incomplete
    def __init__(self, classes) -> None: ...
    def decision_function(self, y_predict): ...

class _RidgeGCV(LinearModel):
    """Ridge regression with built-in Leave-one-out Cross-Validation.

    This class is not intended to be used directly. Use RidgeCV instead.

    Notes
    -----

    We want to solve (K + alpha*Id)c = y,
    where K = X X^T is the kernel matrix.

    Let G = (K + alpha*Id).

    Dual solution: c = G^-1y
    Primal solution: w = X^T c

    Compute eigendecomposition K = Q V Q^T.
    Then G^-1 = Q (V + alpha*Id)^-1 Q^T,
    where (V + alpha*Id) is diagonal.
    It is thus inexpensive to inverse for many alphas.

    Let loov be the vector of prediction values for each example
    when the model was fitted with all examples but this example.

    loov = (KG^-1Y - diag(KG^-1)Y) / diag(I-KG^-1)

    Let looe be the vector of prediction errors for each example
    when the model was fitted with all examples but this example.

    looe = y - loov = c / diag(G^-1)

    The best score (negative mean squared error or user-provided scoring) is
    stored in the `best_score_` attribute, and the selected hyperparameter in
    `alpha_`.

    References
    ----------
    http://cbcl.mit.edu/publications/ps/MIT-CSAIL-TR-2007-025.pdf
    https://www.mit.edu/~9.520/spring07/Classes/rlsslides.pdf
    """
    alphas: Incomplete
    fit_intercept: Incomplete
    scoring: Incomplete
    copy_X: Incomplete
    gcv_mode: Incomplete
    store_cv_values: Incomplete
    is_clf: Incomplete
    alpha_per_target: Incomplete
    def __init__(self, alphas=(0.1, 1.0, 10.0), *, fit_intercept: bool = True, scoring: Incomplete | None = None, copy_X: bool = True, gcv_mode: Incomplete | None = None, store_cv_values: bool = False, is_clf: bool = False, alpha_per_target: bool = False) -> None: ...
    cv_values_: Incomplete
    alpha_: Incomplete
    best_score_: Incomplete
    dual_coef_: Incomplete
    coef_: Incomplete
    def fit(self, X, y, sample_weight: Incomplete | None = None):
        """Fit Ridge regression model with gcv.

        Parameters
        ----------
        X : {ndarray, sparse matrix} of shape (n_samples, n_features)
            Training data. Will be cast to float64 if necessary.

        y : ndarray of shape (n_samples,) or (n_samples, n_targets)
            Target values. Will be cast to float64 if necessary.

        sample_weight : float or ndarray of shape (n_samples,), default=None
            Individual weights for each sample. If given a float, every sample
            will have the same weight.

        Returns
        -------
        self : object
        """

class _BaseRidgeCV(LinearModel):
    alphas: Incomplete
    fit_intercept: Incomplete
    scoring: Incomplete
    cv: Incomplete
    gcv_mode: Incomplete
    store_cv_values: Incomplete
    alpha_per_target: Incomplete
    def __init__(self, alphas=(0.1, 1.0, 10.0), *, fit_intercept: bool = True, scoring: Incomplete | None = None, cv: Incomplete | None = None, gcv_mode: Incomplete | None = None, store_cv_values: bool = False, alpha_per_target: bool = False) -> None: ...
    alpha_: Incomplete
    best_score_: Incomplete
    cv_values_: Incomplete
    coef_: Incomplete
    intercept_: Incomplete
    n_features_in_: Incomplete
    feature_names_in_: Incomplete
    def fit(self, X, y, sample_weight: Incomplete | None = None):
        """Fit Ridge regression model with cv.

        Parameters
        ----------
        X : ndarray of shape (n_samples, n_features)
            Training data. If using GCV, will be cast to float64
            if necessary.

        y : ndarray of shape (n_samples,) or (n_samples, n_targets)
            Target values. Will be cast to X's dtype if necessary.

        sample_weight : float or ndarray of shape (n_samples,), default=None
            Individual weights for each sample. If given a float, every sample
            will have the same weight.

        Returns
        -------
        self : object
            Fitted estimator.

        Notes
        -----
        When sample_weight is provided, the selected hyperparameter may depend
        on whether we use leave-one-out cross-validation (cv=None or cv='auto')
        or another form of cross-validation, because only leave-one-out
        cross-validation takes the sample weights into account when computing
        the validation score.
        """

class RidgeCV(MultiOutputMixin, RegressorMixin, _BaseRidgeCV):
    """Ridge regression with built-in cross-validation.

    See glossary entry for :term:`cross-validation estimator`.

    By default, it performs efficient Leave-One-Out Cross-Validation.

    Read more in the :ref:`User Guide <ridge_regression>`.

    Parameters
    ----------
    alphas : array-like of shape (n_alphas,), default=(0.1, 1.0, 10.0)
        Array of alpha values to try.
        Regularization strength; must be a positive float. Regularization
        improves the conditioning of the problem and reduces the variance of
        the estimates. Larger values specify stronger regularization.
        Alpha corresponds to ``1 / (2C)`` in other linear models such as
        :class:`~sklearn.linear_model.LogisticRegression` or
        :class:`~sklearn.svm.LinearSVC`.
        If using Leave-One-Out cross-validation, alphas must be positive.

    fit_intercept : bool, default=True
        Whether to calculate the intercept for this model. If set
        to false, no intercept will be used in calculations
        (i.e. data is expected to be centered).

    scoring : str, callable, default=None
        A string (see model evaluation documentation) or
        a scorer callable object / function with signature
        ``scorer(estimator, X, y)``.
        If None, the negative mean squared error if cv is 'auto' or None
        (i.e. when using leave-one-out cross-validation), and r2 score
        otherwise.

    cv : int, cross-validation generator or an iterable, default=None
        Determines the cross-validation splitting strategy.
        Possible inputs for cv are:

        - None, to use the efficient Leave-One-Out cross-validation
        - integer, to specify the number of folds.
        - :term:`CV splitter`,
        - An iterable yielding (train, test) splits as arrays of indices.

        For integer/None inputs, if ``y`` is binary or multiclass,
        :class:`~sklearn.model_selection.StratifiedKFold` is used, else,
        :class:`~sklearn.model_selection.KFold` is used.

        Refer :ref:`User Guide <cross_validation>` for the various
        cross-validation strategies that can be used here.

    gcv_mode : {'auto', 'svd', 'eigen'}, default='auto'
        Flag indicating which strategy to use when performing
        Leave-One-Out Cross-Validation. Options are::

            'auto' : use 'svd' if n_samples > n_features, otherwise use 'eigen'
            'svd' : force use of singular value decomposition of X when X is
                dense, eigenvalue decomposition of X^T.X when X is sparse.
            'eigen' : force computation via eigendecomposition of X.X^T

        The 'auto' mode is the default and is intended to pick the cheaper
        option of the two depending on the shape of the training data.

    store_cv_values : bool, default=False
        Flag indicating if the cross-validation values corresponding to
        each alpha should be stored in the ``cv_values_`` attribute (see
        below). This flag is only compatible with ``cv=None`` (i.e. using
        Leave-One-Out Cross-Validation).

    alpha_per_target : bool, default=False
        Flag indicating whether to optimize the alpha value (picked from the
        `alphas` parameter list) for each target separately (for multi-output
        settings: multiple prediction targets). When set to `True`, after
        fitting, the `alpha_` attribute will contain a value for each target.
        When set to `False`, a single alpha is used for all targets.

        .. versionadded:: 0.24

    Attributes
    ----------
    cv_values_ : ndarray of shape (n_samples, n_alphas) or             shape (n_samples, n_targets, n_alphas), optional
        Cross-validation values for each alpha (only available if
        ``store_cv_values=True`` and ``cv=None``). After ``fit()`` has been
        called, this attribute will contain the mean squared errors if
        `scoring is None` otherwise it will contain standardized per point
        prediction values.

    coef_ : ndarray of shape (n_features) or (n_targets, n_features)
        Weight vector(s).

    intercept_ : float or ndarray of shape (n_targets,)
        Independent term in decision function. Set to 0.0 if
        ``fit_intercept = False``.

    alpha_ : float or ndarray of shape (n_targets,)
        Estimated regularization parameter, or, if ``alpha_per_target=True``,
        the estimated regularization parameter for each target.

    best_score_ : float or ndarray of shape (n_targets,)
        Score of base estimator with best alpha, or, if
        ``alpha_per_target=True``, a score for each target.

        .. versionadded:: 0.23

    n_features_in_ : int
        Number of features seen during :term:`fit`.

        .. versionadded:: 0.24

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

        .. versionadded:: 1.0

    See Also
    --------
    Ridge : Ridge regression.
    RidgeClassifier : Classifier based on ridge regression on {-1, 1} labels.
    RidgeClassifierCV : Ridge classifier with built-in cross validation.

    Examples
    --------
    >>> from sklearn.datasets import load_diabetes
    >>> from sklearn.linear_model import RidgeCV
    >>> X, y = load_diabetes(return_X_y=True)
    >>> clf = RidgeCV(alphas=[1e-3, 1e-2, 1e-1, 1]).fit(X, y)
    >>> clf.score(X, y)
    0.5166...
    """
    def fit(self, X, y, sample_weight: Incomplete | None = None):
        """Fit Ridge regression model with cv.

        Parameters
        ----------
        X : ndarray of shape (n_samples, n_features)
            Training data. If using GCV, will be cast to float64
            if necessary.

        y : ndarray of shape (n_samples,) or (n_samples, n_targets)
            Target values. Will be cast to X's dtype if necessary.

        sample_weight : float or ndarray of shape (n_samples,), default=None
            Individual weights for each sample. If given a float, every sample
            will have the same weight.

        Returns
        -------
        self : object
            Fitted estimator.

        Notes
        -----
        When sample_weight is provided, the selected hyperparameter may depend
        on whether we use leave-one-out cross-validation (cv=None or cv='auto')
        or another form of cross-validation, because only leave-one-out
        cross-validation takes the sample weights into account when computing
        the validation score.
        """

class RidgeClassifierCV(_RidgeClassifierMixin, _BaseRidgeCV):
    '''Ridge classifier with built-in cross-validation.

    See glossary entry for :term:`cross-validation estimator`.

    By default, it performs Leave-One-Out Cross-Validation. Currently,
    only the n_features > n_samples case is handled efficiently.

    Read more in the :ref:`User Guide <ridge_regression>`.

    Parameters
    ----------
    alphas : array-like of shape (n_alphas,), default=(0.1, 1.0, 10.0)
        Array of alpha values to try.
        Regularization strength; must be a positive float. Regularization
        improves the conditioning of the problem and reduces the variance of
        the estimates. Larger values specify stronger regularization.
        Alpha corresponds to ``1 / (2C)`` in other linear models such as
        :class:`~sklearn.linear_model.LogisticRegression` or
        :class:`~sklearn.svm.LinearSVC`.

    fit_intercept : bool, default=True
        Whether to calculate the intercept for this model. If set
        to false, no intercept will be used in calculations
        (i.e. data is expected to be centered).

    scoring : str, callable, default=None
        A string (see model evaluation documentation) or
        a scorer callable object / function with signature
        ``scorer(estimator, X, y)``.

    cv : int, cross-validation generator or an iterable, default=None
        Determines the cross-validation splitting strategy.
        Possible inputs for cv are:

        - None, to use the efficient Leave-One-Out cross-validation
        - integer, to specify the number of folds.
        - :term:`CV splitter`,
        - An iterable yielding (train, test) splits as arrays of indices.

        Refer :ref:`User Guide <cross_validation>` for the various
        cross-validation strategies that can be used here.

    class_weight : dict or \'balanced\', default=None
        Weights associated with classes in the form ``{class_label: weight}``.
        If not given, all classes are supposed to have weight one.

        The "balanced" mode uses the values of y to automatically adjust
        weights inversely proportional to class frequencies in the input data
        as ``n_samples / (n_classes * np.bincount(y))``.

    store_cv_values : bool, default=False
        Flag indicating if the cross-validation values corresponding to
        each alpha should be stored in the ``cv_values_`` attribute (see
        below). This flag is only compatible with ``cv=None`` (i.e. using
        Leave-One-Out Cross-Validation).

    Attributes
    ----------
    cv_values_ : ndarray of shape (n_samples, n_targets, n_alphas), optional
        Cross-validation values for each alpha (only if ``store_cv_values=True`` and
        ``cv=None``). After ``fit()`` has been called, this attribute will
        contain the mean squared errors if `scoring is None` otherwise it
        will contain standardized per point prediction values.

    coef_ : ndarray of shape (1, n_features) or (n_targets, n_features)
        Coefficient of the features in the decision function.

        ``coef_`` is of shape (1, n_features) when the given problem is binary.

    intercept_ : float or ndarray of shape (n_targets,)
        Independent term in decision function. Set to 0.0 if
        ``fit_intercept = False``.

    alpha_ : float
        Estimated regularization parameter.

    best_score_ : float
        Score of base estimator with best alpha.

        .. versionadded:: 0.23

    classes_ : ndarray of shape (n_classes,)
        The classes labels.

    n_features_in_ : int
        Number of features seen during :term:`fit`.

        .. versionadded:: 0.24

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

        .. versionadded:: 1.0

    See Also
    --------
    Ridge : Ridge regression.
    RidgeClassifier : Ridge classifier.
    RidgeCV : Ridge regression with built-in cross validation.

    Notes
    -----
    For multi-class classification, n_class classifiers are trained in
    a one-versus-all approach. Concretely, this is implemented by taking
    advantage of the multi-variate response support in Ridge.

    Examples
    --------
    >>> from sklearn.datasets import load_breast_cancer
    >>> from sklearn.linear_model import RidgeClassifierCV
    >>> X, y = load_breast_cancer(return_X_y=True)
    >>> clf = RidgeClassifierCV(alphas=[1e-3, 1e-2, 1e-1, 1]).fit(X, y)
    >>> clf.score(X, y)
    0.9630...
    '''
    class_weight: Incomplete
    def __init__(self, alphas=(0.1, 1.0, 10.0), *, fit_intercept: bool = True, scoring: Incomplete | None = None, cv: Incomplete | None = None, class_weight: Incomplete | None = None, store_cv_values: bool = False) -> None: ...
    def fit(self, X, y, sample_weight: Incomplete | None = None):
        """Fit Ridge classifier with cv.

        Parameters
        ----------
        X : ndarray of shape (n_samples, n_features)
            Training vectors, where `n_samples` is the number of samples
            and `n_features` is the number of features. When using GCV,
            will be cast to float64 if necessary.

        y : ndarray of shape (n_samples,)
            Target values. Will be cast to X's dtype if necessary.

        sample_weight : float or ndarray of shape (n_samples,), default=None
            Individual weights for each sample. If given a float, every sample
            will have the same weight.

        Returns
        -------
        self : object
            Fitted estimator.
        """
