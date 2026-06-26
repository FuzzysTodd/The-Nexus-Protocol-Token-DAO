import statsmodels.base.wrapper as wrap
from _typeshed import Incomplete
from statsmodels.base.model import Results as Results
from statsmodels.tools.decorators import cache_readonly as cache_readonly

def fit_elasticnet(model, method: str = 'coord_descent', maxiter: int = 100, alpha: float = 0.0, L1_wt: float = 1.0, start_params: Incomplete | None = None, cnvrg_tol: float = 1e-07, zero_tol: float = 1e-08, refit: bool = False, check_step: bool = True, loglike_kwds: Incomplete | None = None, score_kwds: Incomplete | None = None, hess_kwds: Incomplete | None = None):
    """
    Return an elastic net regularized fit to a regression model.

    Parameters
    ----------
    model : model object
        A statsmodels object implementing ``loglike``, ``score``, and
        ``hessian``.
    method : {'coord_descent'}
        Only the coordinate descent algorithm is implemented.
    maxiter : int
        The maximum number of iteration cycles (an iteration cycle
        involves running coordinate descent on all variables).
    alpha : scalar or array_like
        The penalty weight.  If a scalar, the same penalty weight
        applies to all variables in the model.  If a vector, it
        must have the same length as `params`, and contains a
        penalty weight for each coefficient.
    L1_wt : scalar
        The fraction of the penalty given to the L1 penalty term.
        Must be between 0 and 1 (inclusive).  If 0, the fit is
        a ridge fit, if 1 it is a lasso fit.
    start_params : array_like
        Starting values for `params`.
    cnvrg_tol : scalar
        If `params` changes by less than this amount (in sup-norm)
        in one iteration cycle, the algorithm terminates with
        convergence.
    zero_tol : scalar
        Any estimated coefficient smaller than this value is
        replaced with zero.
    refit : bool
        If True, the model is refit using only the variables that have
        non-zero coefficients in the regularized fit.  The refitted
        model is not regularized.
    check_step : bool
        If True, confirm that the first step is an improvement and search
        further if it is not.
    loglike_kwds : dict-like or None
        Keyword arguments for the log-likelihood function.
    score_kwds : dict-like or None
        Keyword arguments for the score function.
    hess_kwds : dict-like or None
        Keyword arguments for the Hessian function.

    Returns
    -------
    Results
        A results object.

    Notes
    -----
    The ``elastic net`` penalty is a combination of L1 and L2
    penalties.

    The function that is minimized is:

    -loglike/n + alpha*((1-L1_wt)*|params|_2^2/2 + L1_wt*|params|_1)

    where |*|_1 and |*|_2 are the L1 and L2 norms.

    The computational approach used here is to obtain a quadratic
    approximation to the smooth part of the target function:

    -loglike/n + alpha*(1-L1_wt)*|params|_2^2/2

    then repeatedly optimize the L1 penalized version of this function
    along coordinate axes.
    """

class RegularizedResults(Results):
    """
    Results for models estimated using regularization

    Parameters
    ----------
    model : Model
        The model instance used to estimate the parameters.
    params : ndarray
        The estimated (regularized) parameters.
    """
    def __init__(self, model, params) -> None: ...
    def fittedvalues(self):
        """
        The predicted values from the model at the estimated parameters.
        """

class RegularizedResultsWrapper(wrap.ResultsWrapper): ...
