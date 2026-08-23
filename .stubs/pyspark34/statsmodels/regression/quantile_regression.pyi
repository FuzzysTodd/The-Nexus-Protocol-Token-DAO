from _typeshed import Incomplete
from statsmodels.regression.linear_model import RegressionModel as RegressionModel, RegressionResults as RegressionResults, RegressionResultsWrapper as RegressionResultsWrapper
from statsmodels.tools.decorators import cache_readonly as cache_readonly
from statsmodels.tools.sm_exceptions import ConvergenceWarning as ConvergenceWarning, IterationLimitWarning as IterationLimitWarning

class QuantReg(RegressionModel):
    """Quantile Regression

    Estimate a quantile regression model using iterative reweighted least
    squares.

    Parameters
    ----------
    endog : array or dataframe
        endogenous/response variable
    exog : array or dataframe
        exogenous/explanatory variable(s)

    Notes
    -----
    The Least Absolute Deviation (LAD) estimator is a special case where
    quantile is set to 0.5 (q argument of the fit method).

    The asymptotic covariance matrix is estimated following the procedure in
    Greene (2008, p.407-408), using either the logistic or gaussian kernels
    (kernel argument of the fit method).

    References
    ----------
    General:

    * Birkes, D. and Y. Dodge(1993). Alternative Methods of Regression, John Wiley and Sons.
    * Green,W. H. (2008). Econometric Analysis. Sixth Edition. International Student Edition.
    * Koenker, R. (2005). Quantile Regression. New York: Cambridge University Press.
    * LeSage, J. P.(1999). Applied Econometrics Using MATLAB,

    Kernels (used by the fit method):

    * Green (2008) Table 14.2

    Bandwidth selection (used by the fit method):

    * Bofinger, E. (1975). Estimation of a density function using order statistics. Australian Journal of Statistics 17: 1-17.
    * Chamberlain, G. (1994). Quantile regression, censoring, and the structure of wages. In Advances in Econometrics, Vol. 1: Sixth World Congress, ed. C. A. Sims, 171-209. Cambridge: Cambridge University Press.
    * Hall, P., and S. Sheather. (1988). On the distribution of the Studentized quantile. Journal of the Royal Statistical Society, Series B 50: 381-391.

    Keywords: Least Absolute Deviation(LAD) Regression, Quantile Regression,
    Regression, Robust Estimation.
    """
    def __init__(self, endog, exog, **kwargs) -> None: ...
    def whiten(self, data):
        """
        QuantReg model whitener does nothing: returns data.
        """
    rank: Incomplete
    df_model: Incomplete
    df_resid: Incomplete
    def fit(self, q: float = 0.5, vcov: str = 'robust', kernel: str = 'epa', bandwidth: str = 'hsheather', max_iter: int = 1000, p_tol: float = 1e-06, **kwargs):
        """
        Solve by Iterative Weighted Least Squares

        Parameters
        ----------
        q : float
            Quantile must be strictly between 0 and 1
        vcov : str, method used to calculate the variance-covariance matrix
            of the parameters. Default is ``robust``:

            - robust : heteroskedasticity robust standard errors (as suggested
              in Greene 6th edition)
            - iid : iid errors (as in Stata 12)

        kernel : str, kernel to use in the kernel density estimation for the
            asymptotic covariance matrix:

            - epa: Epanechnikov
            - cos: Cosine
            - gau: Gaussian
            - par: Parzene

        bandwidth : str, Bandwidth selection method in kernel density
            estimation for asymptotic covariance estimate (full
            references in QuantReg docstring):

            - hsheather: Hall-Sheather (1988)
            - bofinger: Bofinger (1975)
            - chamberlain: Chamberlain (1994)
        """

kernels: Incomplete

def hall_sheather(n, q, alpha: float = 0.05): ...
def bofinger(n, q): ...
def chamberlain(n, q, alpha: float = 0.05): ...

class QuantRegResults(RegressionResults):
    """Results instance for the QuantReg model"""
    def prsquared(self): ...
    def scale(self): ...
    def bic(self): ...
    def aic(self): ...
    def llf(self): ...
    def rsquared(self): ...
    def rsquared_adj(self): ...
    def mse(self): ...
    def mse_model(self): ...
    def mse_total(self): ...
    def centered_tss(self): ...
    def uncentered_tss(self): ...
    def HC0_se(self) -> None: ...
    def HC1_se(self) -> None: ...
    def HC2_se(self) -> None: ...
    def HC3_se(self) -> None: ...
    def summary(self, yname: Incomplete | None = None, xname: Incomplete | None = None, title: Incomplete | None = None, alpha: float = 0.05):
        """Summarize the Regression Results

        Parameters
        ----------
        yname : str, optional
            Default is `y`
        xname : list[str], optional
            Names for the exogenous variables. Default is `var_##` for ## in
            the number of regressors. Must match the number of parameters
            in the model
        title : str, optional
            Title for the top table. If not None, then this replaces the
            default title
        alpha : float
            significance level for the confidence intervals

        Returns
        -------
        smry : Summary instance
            this holds the summary tables and text, which can be printed or
            converted to various output formats.

        See Also
        --------
        statsmodels.iolib.summary.Summary : class to hold summary results
        """
