from _typeshed import Incomplete
from statsmodels.regression.linear_model import GLS as GLS, OLS as OLS
from statsmodels.tools.grouputils import GroupSorted as GroupSorted

def sum_outer_product_loop(x, group_iter):
    """sum outerproduct dot(x_i, x_i.T) over individuals

    loop version

    """
def sum_outer_product_balanced(x, n_groups):
    """sum outerproduct dot(x_i, x_i.T) over individuals

    where x_i is (nobs_i, 1), and result is (nobs_i, nobs_i)

    reshape-dot version, for x.ndim=1 only

    """
def whiten_individuals_loop(x, transform, group_iter):
    """apply linear transform for each individual

    loop version
    """

class ShortPanelGLS2:
    """Short Panel with general intertemporal within correlation

    assumes data is stacked by individuals, panel is balanced and
    within correlation structure is identical across individuals.

    It looks like this can just inherit GLS and overwrite whiten
    """
    endog: Incomplete
    exog: Incomplete
    group: Incomplete
    n_groups: Incomplete
    def __init__(self, endog, exog, group) -> None: ...
    res_pooled: Incomplete
    def fit_ols(self): ...
    def get_within_cov(self, resid): ...
    def whiten_groups(self, x, cholsigmainv_i): ...
    cholsigmainv_i: Incomplete
    res1: Incomplete
    def fit(self): ...

class ShortPanelGLS(GLS):
    """Short Panel with general intertemporal within correlation

    assumes data is stacked by individuals, panel is balanced and
    within correlation structure is identical across individuals.

    It looks like this can just inherit GLS and overwrite whiten
    """
    group: Incomplete
    n_groups: Incomplete
    cholsigmainv_i: Incomplete
    def __init__(self, endog, exog, group, sigma_i: Incomplete | None = None) -> None: ...
    def get_within_cov(self, resid): ...
    def whiten_groups(self, x, cholsigmainv_i): ...
    def whiten(self, x): ...
    history: Incomplete
    results_old: Incomplete
    def fit_iterative(self, maxiter: int = 3):
        """
        Perform an iterative two-step procedure to estimate the GLS model.

        Parameters
        ----------
        maxiter : int, optional
            the number of iterations

        Notes
        -----
        maxiter=1: returns the estimated based on given weights
        maxiter=2: performs a second estimation with the updated weights,
                   this is 2-step estimation
        maxiter>2: iteratively estimate and update the weights

        TODO: possible extension stop iteration if change in parameter
            estimates is smaller than x_tol

        Repeated calls to fit_iterative, will do one redundant pinv_wexog
        calculation. Calling fit_iterative(maxiter) once does not do any
        redundant recalculations (whitening or calculating pinv_wexog).
        """
