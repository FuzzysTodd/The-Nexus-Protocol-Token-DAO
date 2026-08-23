from _typeshed import Incomplete
from statsmodels.genmod import families as families
from statsmodels.genmod.generalized_linear_model import GLM as GLM
from statsmodels.sandbox.nonparametric.smoothers import PolySmoother as PolySmoother
from statsmodels.tools.sm_exceptions import IterationLimitWarning as IterationLimitWarning, iteration_limit_doc as iteration_limit_doc

DEBUG: bool

def default_smoother(x, s_arg: Incomplete | None = None):
    """

    """

class Offset:
    fn: Incomplete
    offset: Incomplete
    def __init__(self, fn, offset) -> None: ...
    def __call__(self, *args, **kw): ...

class Results:
    Y: Incomplete
    alpha: Incomplete
    smoothers: Incomplete
    offset: Incomplete
    family: Incomplete
    exog: Incomplete
    mu: Incomplete
    def __init__(self, Y, alpha, exog, smoothers, family, offset) -> None: ...
    def __call__(self, exog):
        """expected value ? check new GLM, same as mu for given exog
        maybe remove this
        """
    def linkinversepredict(self, exog):
        """expected value ? check new GLM, same as mu for given exog
        """
    def predict(self, exog):
        """predict response, sum of smoothed components
        TODO: What's this in the case of GLM, corresponds to X*beta ?
        """
    def smoothed(self, exog):
        """get smoothed prediction for each component

        """
    def smoothed_demeaned(self, exog): ...

class AdditiveModel:
    """additive model with non-parametric, smoothed components

    Parameters
    ----------
    exog : ndarray
    smoothers : None or list of smoother instances
        smoother instances not yet checked
    weights : None or ndarray
    family : None or family instance
        I think only used because of shared results with GAM and subclassing.
        If None, then Gaussian is used.
    """
    exog: Incomplete
    weights: Incomplete
    smoothers: Incomplete
    family: Incomplete
    def __init__(self, exog, smoothers: Incomplete | None = None, weights: Incomplete | None = None, family: Incomplete | None = None) -> None: ...
    def next(self):
        """internal calculation for one fit iteration

        BUG: I think this does not improve, what is supposed to improve
            offset does not seem to be used, neither an old alpha
            The smoothers keep coef/params from previous iteration
        """
    dev: Incomplete
    def cont(self):
        """condition to continue iteration loop

        Parameters
        ----------
        tol

        Returns
        -------
        cont : bool
            If true, then iteration should be continued.

        """
    def df_resid(self):
        """degrees of freedom of residuals, ddof is sum of all smoothers df
        """
    def estimate_scale(self):
        """estimate standard deviation of residuals
        """
    rtol: Incomplete
    maxiter: Incomplete
    results: Incomplete
    def fit(self, Y, rtol: float = 1e-06, maxiter: int = 30):
        """fit the model to a given endogenous variable Y

        This needs to change for consistency with statsmodels

        """

class Model(GLM, AdditiveModel):
    def __init__(self, endog, exog, smoothers: Incomplete | None = None, family=...) -> None: ...
    weights: Incomplete
    results: Incomplete
    def next(self): ...
    def estimate_scale(self, Y: Incomplete | None = None):
        """
        Return Pearson's X^2 estimate of scale.
        """
    rtol: Incomplete
    maxiter: Incomplete
    Y: Incomplete
    history: Incomplete
    scale: Incomplete
    def fit(self, Y, rtol: float = 1e-06, maxiter: int = 30): ...
