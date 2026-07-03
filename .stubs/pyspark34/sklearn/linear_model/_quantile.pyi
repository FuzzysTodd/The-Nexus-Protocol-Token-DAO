from ..base import BaseEstimator as BaseEstimator, RegressorMixin as RegressorMixin
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from ..utils._param_validation import Hidden as Hidden, Interval as Interval, StrOptions as StrOptions
from ..utils.fixes import parse_version as parse_version, sp_version as sp_version
from ._base import LinearModel as LinearModel
from _typeshed import Incomplete

class QuantileRegressor(LinearModel, RegressorMixin, BaseEstimator):
    '''Linear regression model that predicts conditional quantiles.

    The linear :class:`QuantileRegressor` optimizes the pinball loss for a
    desired `quantile` and is robust to outliers.

    This model uses an L1 regularization like
    :class:`~sklearn.linear_model.Lasso`.

    Read more in the :ref:`User Guide <quantile_regression>`.

    .. versionadded:: 1.0

    Parameters
    ----------
    quantile : float, default=0.5
        The quantile that the model tries to predict. It must be strictly
        between 0 and 1. If 0.5 (default), the model predicts the 50%
        quantile, i.e. the median.

    alpha : float, default=1.0
        Regularization constant that multiplies the L1 penalty term.

    fit_intercept : bool, default=True
        Whether or not to fit the intercept.

    solver : {\'highs-ds\', \'highs-ipm\', \'highs\', \'interior-point\',             \'revised simplex\'}, default=\'interior-point\'
        Method used by :func:`scipy.optimize.linprog` to solve the linear
        programming formulation.

        From `scipy>=1.6.0`, it is recommended to use the highs methods because
        they are the fastest ones. Solvers "highs-ds", "highs-ipm" and "highs"
        support sparse input data and, in fact, always convert to sparse csc.

        From `scipy>=1.11.0`, "interior-point" is not available anymore.

        .. versionchanged:: 1.4
           The default of `solver` will change to `"highs"` in version 1.4.

    solver_options : dict, default=None
        Additional parameters passed to :func:`scipy.optimize.linprog` as
        options. If `None` and if `solver=\'interior-point\'`, then
        `{"lstsq": True}` is passed to :func:`scipy.optimize.linprog` for the
        sake of stability.

    Attributes
    ----------
    coef_ : array of shape (n_features,)
        Estimated coefficients for the features.

    intercept_ : float
        The intercept of the model, aka bias term.

    n_features_in_ : int
        Number of features seen during :term:`fit`.

        .. versionadded:: 0.24

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

        .. versionadded:: 1.0

    n_iter_ : int
        The actual number of iterations performed by the solver.

    See Also
    --------
    Lasso : The Lasso is a linear model that estimates sparse coefficients
        with l1 regularization.
    HuberRegressor : Linear regression model that is robust to outliers.

    Examples
    --------
    >>> from sklearn.linear_model import QuantileRegressor
    >>> import numpy as np
    >>> n_samples, n_features = 10, 2
    >>> rng = np.random.RandomState(0)
    >>> y = rng.randn(n_samples)
    >>> X = rng.randn(n_samples, n_features)
    >>> # the two following lines are optional in practice
    >>> from sklearn.utils.fixes import sp_version, parse_version
    >>> solver = "highs" if sp_version >= parse_version("1.6.0") else "interior-point"
    >>> reg = QuantileRegressor(quantile=0.8, solver=solver).fit(X, y)
    >>> np.mean(y <= reg.predict(X))
    0.8
    '''
    quantile: Incomplete
    alpha: Incomplete
    fit_intercept: Incomplete
    solver: Incomplete
    solver_options: Incomplete
    def __init__(self, *, quantile: float = 0.5, alpha: float = 1.0, fit_intercept: bool = True, solver: str = 'warn', solver_options: Incomplete | None = None) -> None: ...
    n_iter_: Incomplete
    coef_: Incomplete
    intercept_: Incomplete
    def fit(self, X, y, sample_weight: Incomplete | None = None):
        """Fit the model according to the given training data.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            Training data.

        y : array-like of shape (n_samples,)
            Target values.

        sample_weight : array-like of shape (n_samples,), default=None
            Sample weights.

        Returns
        -------
        self : object
            Returns self.
        """
