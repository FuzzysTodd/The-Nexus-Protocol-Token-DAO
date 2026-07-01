from _typeshed import Incomplete
from statsmodels.iolib import summary2 as summary2

class RegressionFDR:
    """
    Control FDR in a regression procedure.

    Parameters
    ----------
    endog : array_like
        The dependent variable of the regression
    exog : array_like
        The independent variables of the regression
    regeffects : RegressionEffects instance
        An instance of a RegressionEffects class that can compute
        effect sizes for the regression coefficients.
    method : str
        The approach used to assess and control FDR, currently
        must be 'knockoff'.

    Returns
    -------
    Returns an instance of the RegressionFDR class.  The `fdr` attribute
    holds the estimated false discovery rates.

    Notes
    -----
    This class Implements the knockoff method of Barber and Candes.
    This is an approach for controlling the FDR of a variety of
    regression estimation procedures, including correlation
    coefficients, OLS regression, OLS with forward selection, and
    LASSO regression.

    For other approaches to FDR control in regression, see the
    statsmodels.stats.multitest module.  Methods provided in that
    module use Z-scores or p-values, and therefore require standard
    errors for the coefficient estimates to be available.

    The default method for constructing the augmented design matrix is
    the 'equivariant' approach, set `design_method='sdp'` to use an
    alternative approach involving semidefinite programming.  See
    Barber and Candes for more information about both approaches.  The
    sdp approach requires that the cvxopt package be installed.
    """
    xnames: Incomplete
    endog: Incomplete
    exog: Incomplete
    exog1: Incomplete
    exog2: Incomplete
    stats: Incomplete
    fdr: Incomplete
    fdrp: Incomplete
    fdr_df: Incomplete
    def __init__(self, endog, exog, regeffects, method: str = 'knockoff', **kwargs) -> None: ...
    def threshold(self, tfdr):
        """
        Returns the threshold statistic for a given target FDR.
        """
    def summary(self): ...
