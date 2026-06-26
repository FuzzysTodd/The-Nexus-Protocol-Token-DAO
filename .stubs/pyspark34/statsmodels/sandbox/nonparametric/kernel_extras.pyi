from _typeshed import Incomplete
from statsmodels.nonparametric.api import KernelReg

__all__ = ['SingleIndexModel', 'SemiLinear', 'TestFForm']

class TestFForm:
    '''
    Nonparametric test for functional form.

    Parameters
    ----------
    endog : list
        Dependent variable (training set)
    exog : list of array_like objects
        The independent (right-hand-side) variables
    bw : array_like, str
        Bandwidths for exog or specify method for bandwidth selection
    fform : function
        The functional form ``y = g(b, x)`` to be tested. Takes as inputs
        the RHS variables `exog` and the coefficients ``b`` (betas)
        and returns a fitted ``y_hat``.
    var_type : str
        The type of the independent `exog` variables:

            - c: continuous
            - o: ordered
            - u: unordered

    estimator : function
        Must return the estimated coefficients b (betas). Takes as inputs
        ``(endog, exog)``.  E.g. least square estimator::

            lambda (x,y): np.dot(np.pinv(np.dot(x.T, x)), np.dot(x.T, y))

    References
    ----------
    See Racine, J.: "Consistent Significance Testing for Nonparametric
    Regression" Journal of Business & Economics Statistics.

    See chapter 12 in [1]  pp. 355-357.
    '''
    endog: Incomplete
    exog: Incomplete
    var_type: Incomplete
    fform: Incomplete
    estimator: Incomplete
    nboot: Incomplete
    bw: Incomplete
    sig: Incomplete
    def __init__(self, endog, exog, bw, var_type, fform, estimator, nboot: int = 100) -> None: ...

class SingleIndexModel(KernelReg):
    """
    Single index semiparametric model ``y = g(X * b) + e``.

    Parameters
    ----------
    endog : array_like
        The dependent variable
    exog : array_like
        The independent variable(s)
    var_type : str
        The type of variables in X:

            - c: continuous
            - o: ordered
            - u: unordered

    Attributes
    ----------
    b : array_like
        The linear coefficients b (betas)
    bw : array_like
        Bandwidths

    Methods
    -------
    fit(): Computes the fitted values ``E[Y|X] = g(X * b)``
           and the marginal effects ``dY/dX``.

    References
    ----------
    See chapter on semiparametric models in [1]

    Notes
    -----
    This model resembles the binary choice models. The user knows
    that X and b interact linearly, but ``g(X * b)`` is unknown.
    In the parametric binary choice models the user usually assumes
    some distribution of g() such as normal or logistic.
    """
    var_type: Incomplete
    K: Incomplete
    endog: Incomplete
    exog: Incomplete
    nobs: Incomplete
    data_type: Incomplete
    ckertype: str
    okertype: str
    ukertype: str
    func: Incomplete
    def __init__(self, endog, exog, var_type) -> None: ...
    def cv_loo(self, params): ...
    def fit(self, data_predict: Incomplete | None = None): ...

class SemiLinear(KernelReg):
    """
    Semiparametric partially linear model, ``Y = Xb + g(Z) + e``.

    Parameters
    ----------
    endog : array_like
        The dependent variable
    exog : array_like
        The linear component in the regression
    exog_nonparametric : array_like
        The nonparametric component in the regression
    var_type : str
        The type of the variables in the nonparametric component;

            - c: continuous
            - o: ordered
            - u: unordered

    k_linear : int
        The number of variables that comprise the linear component.

    Attributes
    ----------
    bw : array_like
        Bandwidths for the nonparametric component exog_nonparametric
    b : array_like
        Coefficients in the linear component
    nobs : int
        The number of observations.
    k_linear : int
        The number of variables that comprise the linear component.

    Methods
    -------
    fit
        Returns the fitted mean and marginal effects dy/dz

    Notes
    -----
    This model uses only the local constant regression estimator

    References
    ----------
    See chapter on Semiparametric Models in [1]
    """
    endog: Incomplete
    exog: Incomplete
    K: Incomplete
    exog_nonparametric: Incomplete
    k_linear: Incomplete
    nobs: Incomplete
    var_type: Incomplete
    data_type: Incomplete
    ckertype: str
    okertype: str
    ukertype: str
    func: Incomplete
    def __init__(self, endog, exog, exog_nonparametric, var_type, k_linear) -> None: ...
    def cv_loo(self, params):
        """
        Similar to the cross validation leave-one-out estimator.

        Modified to reflect the linear components.

        Parameters
        ----------
        params : array_like
            Vector consisting of the coefficients (b) and the bandwidths (bw).
            The first ``k_linear`` elements are the coefficients.

        Returns
        -------
        L : float
            The value of the objective function

        References
        ----------
        See p.254 in [1]
        """
    def fit(self, exog_predict: Incomplete | None = None, exog_nonparametric_predict: Incomplete | None = None):
        """Computes fitted values and marginal effects"""
