from _typeshed import Incomplete
from statsmodels.base.model import Model as Model

class Results:
    """just a dummy placeholder for now
    most results from RegressionResults can be used here
    """

class NonlinearLS(Model):
    """Base class for estimation of a non-linear model with least squares

    This class is supposed to be subclassed, and the subclass has to provide a method
    `_predict` that defines the non-linear function `f(params) that is predicting the endogenous
    variable. The model is assumed to be

    :math: y = f(params) + error

    and the estimator minimizes the sum of squares of the estimated error.

    :math: min_parmas \\sum (y - f(params))**2

    f has to return the prediction for each observation. Exogenous or explanatory variables
    should be accessed as attributes of the class instance, and can be given as arguments
    when the instance is created.

    Warning:
    Weights are not correctly handled yet in the results statistics,
    but included when estimating the parameters.

    similar to scipy.optimize.curve_fit
    API difference: params are array_like not split up, need n_params information

    includes now weights similar to curve_fit
    no general sigma yet (OLS and WLS, but no GLS)

    This is currently holding on to intermediate results that are not necessary
    but useful for testing.

    Fit returns and instance of RegressionResult, in contrast to the linear
    model, results in this case are based on a local approximation, essentially
    y = f(X, params) is replaced by y = grad * params where grad is the Gradient
    or Jacobian with the shape (nobs, nparams). See for example Greene

    Examples
    --------

    class Myfunc(NonlinearLS):

        def _predict(self, params):
            x = self.exog
            a, b, c = params
            return a*np.exp(-b*x) + c

    Ff we have data (y, x), we can create an instance and fit it with

    mymod = Myfunc(y, x)
    myres = mymod.fit(nparams=3)

    and use the non-linear regression results, for example

    myres.params
    myres.bse
    myres.tvalues


    """
    endog: Incomplete
    exog: Incomplete
    sigma: Incomplete
    weights: Incomplete
    def __init__(self, endog: Incomplete | None = None, exog: Incomplete | None = None, weights: Incomplete | None = None, sigma: Incomplete | None = None, missing: str = 'none') -> None: ...
    def predict(self, exog, params: Incomplete | None = None): ...
    def start_value(self) -> None: ...
    def geterrors(self, params, weights: Incomplete | None = None): ...
    def errorsumsquares(self, params): ...
    df_resid: Incomplete
    df_model: Incomplete
    wendog: Incomplete
    wexog: Incomplete
    normalized_cov_params: Incomplete
    def fit(self, start_value: Incomplete | None = None, nparams: Incomplete | None = None, **kw): ...
    def fit_minimal(self, start_value, **kwargs):
        """minimal fitting with no extra calculations"""
    def fit_random(self, ntries: int = 10, rvs_generator: Incomplete | None = None, nparams: Incomplete | None = None):
        """fit with random starting values

        this could be replaced with a global fitter

        """
    def jac_predict(self, params):
        """jacobian of prediction function using complex step derivative

        This assumes that the predict function does not use complex variable
        but is designed to do so.

        """

class Myfunc(NonlinearLS): ...
