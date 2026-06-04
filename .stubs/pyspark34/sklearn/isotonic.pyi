from .base import BaseEstimator, RegressorMixin, TransformerMixin
from _typeshed import Incomplete

__all__ = ['check_increasing', 'isotonic_regression', 'IsotonicRegression']

def check_increasing(x, y):
    """Determine whether y is monotonically correlated with x.

    y is found increasing or decreasing with respect to x based on a Spearman
    correlation test.

    Parameters
    ----------
    x : array-like of shape (n_samples,)
            Training data.

    y : array-like of shape (n_samples,)
        Training target.

    Returns
    -------
    increasing_bool : boolean
        Whether the relationship is increasing or decreasing.

    Notes
    -----
    The Spearman correlation coefficient is estimated from the data, and the
    sign of the resulting estimate is used as the result.

    In the event that the 95% confidence interval based on Fisher transform
    spans zero, a warning is raised.

    References
    ----------
    Fisher transformation. Wikipedia.
    https://en.wikipedia.org/wiki/Fisher_transformation
    """
def isotonic_regression(y, *, sample_weight: Incomplete | None = None, y_min: Incomplete | None = None, y_max: Incomplete | None = None, increasing: bool = True):
    '''Solve the isotonic regression model.

    Read more in the :ref:`User Guide <isotonic>`.

    Parameters
    ----------
    y : array-like of shape (n_samples,)
        The data.

    sample_weight : array-like of shape (n_samples,), default=None
        Weights on each point of the regression.
        If None, weight is set to 1 (equal weights).

    y_min : float, default=None
        Lower bound on the lowest predicted value (the minimum value may
        still be higher). If not set, defaults to -inf.

    y_max : float, default=None
        Upper bound on the highest predicted value (the maximum may still be
        lower). If not set, defaults to +inf.

    increasing : bool, default=True
        Whether to compute ``y_`` is increasing (if set to True) or decreasing
        (if set to False).

    Returns
    -------
    y_ : ndarray of shape (n_samples,)
        Isotonic fit of y.

    References
    ----------
    "Active set algorithms for isotonic regression; A unifying framework"
    by Michael J. Best and Nilotpal Chakravarti, section 3.
    '''

class IsotonicRegression(RegressorMixin, TransformerMixin, BaseEstimator):
    """Isotonic regression model.

    Read more in the :ref:`User Guide <isotonic>`.

    .. versionadded:: 0.13

    Parameters
    ----------
    y_min : float, default=None
        Lower bound on the lowest predicted value (the minimum value may
        still be higher). If not set, defaults to -inf.

    y_max : float, default=None
        Upper bound on the highest predicted value (the maximum may still be
        lower). If not set, defaults to +inf.

    increasing : bool or 'auto', default=True
        Determines whether the predictions should be constrained to increase
        or decrease with `X`. 'auto' will decide based on the Spearman
        correlation estimate's sign.

    out_of_bounds : {'nan', 'clip', 'raise'}, default='nan'
        Handles how `X` values outside of the training domain are handled
        during prediction.

        - 'nan', predictions will be NaN.
        - 'clip', predictions will be set to the value corresponding to
          the nearest train interval endpoint.
        - 'raise', a `ValueError` is raised.

    Attributes
    ----------
    X_min_ : float
        Minimum value of input array `X_` for left bound.

    X_max_ : float
        Maximum value of input array `X_` for right bound.

    X_thresholds_ : ndarray of shape (n_thresholds,)
        Unique ascending `X` values used to interpolate
        the y = f(X) monotonic function.

        .. versionadded:: 0.24

    y_thresholds_ : ndarray of shape (n_thresholds,)
        De-duplicated `y` values suitable to interpolate the y = f(X)
        monotonic function.

        .. versionadded:: 0.24

    f_ : function
        The stepwise interpolating function that covers the input domain ``X``.

    increasing_ : bool
        Inferred value for ``increasing``.

    See Also
    --------
    sklearn.linear_model.LinearRegression : Ordinary least squares Linear
        Regression.
    sklearn.ensemble.HistGradientBoostingRegressor : Gradient boosting that
        is a non-parametric model accepting monotonicity constraints.
    isotonic_regression : Function to solve the isotonic regression model.

    Notes
    -----
    Ties are broken using the secondary method from de Leeuw, 1977.

    References
    ----------
    Isotonic Median Regression: A Linear Programming Approach
    Nilotpal Chakravarti
    Mathematics of Operations Research
    Vol. 14, No. 2 (May, 1989), pp. 303-308

    Isotone Optimization in R : Pool-Adjacent-Violators
    Algorithm (PAVA) and Active Set Methods
    de Leeuw, Hornik, Mair
    Journal of Statistical Software 2009

    Correctness of Kruskal's algorithms for monotone regression with ties
    de Leeuw, Psychometrica, 1977

    Examples
    --------
    >>> from sklearn.datasets import make_regression
    >>> from sklearn.isotonic import IsotonicRegression
    >>> X, y = make_regression(n_samples=10, n_features=1, random_state=41)
    >>> iso_reg = IsotonicRegression().fit(X, y)
    >>> iso_reg.predict([.1, .2])
    array([1.8628..., 3.7256...])
    """
    y_min: Incomplete
    y_max: Incomplete
    increasing: Incomplete
    out_of_bounds: Incomplete
    def __init__(self, *, y_min: Incomplete | None = None, y_max: Incomplete | None = None, increasing: bool = True, out_of_bounds: str = 'nan') -> None: ...
    def fit(self, X, y, sample_weight: Incomplete | None = None):
        """Fit the model using X, y as training data.

        Parameters
        ----------
        X : array-like of shape (n_samples,) or (n_samples, 1)
            Training data.

            .. versionchanged:: 0.24
               Also accepts 2d array with 1 feature.

        y : array-like of shape (n_samples,)
            Training target.

        sample_weight : array-like of shape (n_samples,), default=None
            Weights. If set to None, all weights will be set to 1 (equal
            weights).

        Returns
        -------
        self : object
            Returns an instance of self.

        Notes
        -----
        X is stored for future use, as :meth:`transform` needs X to interpolate
        new input data.
        """
    def transform(self, T):
        """Transform new data by linear interpolation.

        Parameters
        ----------
        T : array-like of shape (n_samples,) or (n_samples, 1)
            Data to transform.

            .. versionchanged:: 0.24
               Also accepts 2d array with 1 feature.

        Returns
        -------
        y_pred : ndarray of shape (n_samples,)
            The transformed data.
        """
    def predict(self, T):
        """Predict new data by linear interpolation.

        Parameters
        ----------
        T : array-like of shape (n_samples,) or (n_samples, 1)
            Data to transform.

        Returns
        -------
        y_pred : ndarray of shape (n_samples,)
            Transformed data.
        """
    def get_feature_names_out(self, input_features: Incomplete | None = None):
        '''Get output feature names for transformation.

        Parameters
        ----------
        input_features : array-like of str or None, default=None
            Ignored.

        Returns
        -------
        feature_names_out : ndarray of str objects
            An ndarray with one string i.e. ["isotonicregression0"].
        '''
