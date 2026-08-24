import statsmodels.base.model as base
import statsmodels.regression.linear_model as lm
from _typeshed import Incomplete
from statsmodels.genmod import families as families
from statsmodels.genmod.families import links as links, varfuncs as varfuncs
from statsmodels.genmod.generalized_linear_model import GLM as GLM
from statsmodels.tools.decorators import cache_readonly as cache_readonly

class QIFCovariance:
    """
    A covariance model for quadratic inference function regression.

    The mat method returns a basis matrix B such that the inverse
    of the working covariance lies in the linear span of the
    basis matrices.

    Subclasses should set the number of basis matrices `num_terms`,
    so that `mat(d, j)` for j=0, ..., num_terms-1 gives the basis
    of dimension d.`
    """
    def mat(self, dim, term) -> None:
        """
        Returns the term'th basis matrix, which is a dim x dim
        matrix.
        """

class QIFIndependence(QIFCovariance):
    """
    Independent working covariance for QIF regression.  This covariance
    model gives identical results to GEE with the independence working
    covariance.  When using QIFIndependence as the working covariance,
    the QIF value will be zero, and cannot be used for chi^2 testing, or
    for model selection using AIC, BIC, etc.
    """
    num_terms: int
    def __init__(self) -> None: ...
    def mat(self, dim, term): ...

class QIFExchangeable(QIFCovariance):
    """
    Exchangeable working covariance for QIF regression.
    """
    num_terms: int
    def __init__(self) -> None: ...
    def mat(self, dim, term): ...

class QIFAutoregressive(QIFCovariance):
    """
    Autoregressive working covariance for QIF regression.
    """
    num_terms: int
    def __init__(self) -> None: ...
    def mat(self, dim, term): ...

class QIF(base.Model):
    """
    Fit a regression model using quadratic inference functions (QIF).

    QIF is an alternative to GEE that can be more efficient, and that
    offers different approaches for model selection and inference.

    Parameters
    ----------
    endog : array_like
        The dependent variables of the regression.
    exog : array_like
        The independent variables of the regression.
    groups : array_like
        Labels indicating which group each observation belongs to.
        Observations in different groups should be independent.
    family : genmod family
        An instance of a GLM family.\x7f
    cov_struct : QIFCovariance instance
        An instance of a QIFCovariance.

    References
    ----------
    A. Qu, B. Lindsay, B. Li (2000).  Improving Generalized Estimating
    Equations using Quadratic Inference Functions, Biometrika 87:4.
    www.jstor.org/stable/2673612
    """
    family: Incomplete
    cov_struct: Incomplete
    group_names: Incomplete
    nobs: Incomplete
    groups_ix: Incomplete
    def __init__(self, endog, exog, groups, family: Incomplete | None = None, cov_struct: Incomplete | None = None, missing: str = 'none', **kwargs) -> None: ...
    def objective(self, params):
        """
        Calculate the gradient of the QIF objective function.

        Parameters
        ----------
        params : array_like
            The model parameters at which the gradient is evaluated.

        Returns
        -------
        grad : array_like
            The gradient vector of the QIF objective function.
        gn_deriv : array_like
            The gradients of each estimating equation with
            respect to the parameter.
        """
    def estimate_scale(self, params):
        """
        Estimate the dispersion/scale.

        The scale parameter for binomial and Poisson families is
        fixed at 1, otherwise it is estimated from the data.
        """
    @classmethod
    def from_formula(cls, formula, groups, data, subset: Incomplete | None = None, *args, **kwargs):
        """
        Create a QIF model instance from a formula and dataframe.

        Parameters
        ----------
        formula : str or generic Formula object
            The formula specifying the model
        groups : array_like or string
            Array of grouping labels.  If a string, this is the name
            of a variable in `data` that contains the grouping labels.
        data : array_like
            The data for the model.
        subset : array_like
            An array_like object of booleans, integers, or index
            values that indicate the subset of the data to used when
            fitting the model.

        Returns
        -------
        model : QIF model instance
        """
    ddof_scale: Incomplete
    def fit(self, maxiter: int = 100, start_params: Incomplete | None = None, tol: float = 1e-06, gtol: float = 0.0001, ddof_scale: Incomplete | None = None):
        """
        Fit a GLM to correlated data using QIF.

        Parameters
        ----------
        maxiter : int
            Maximum number of iterations.
        start_params : array_like, optional
            Starting values
        tol : float
            Convergence threshold for difference of successive
            estimates.
        gtol : float
            Convergence threshold for gradient.
        ddof_scale : int, optional
            Degrees of freedom for the scale parameter

        Returns
        -------
        QIFResults object
        """

class QIFResults(base.LikelihoodModelResults):
    """Results class for QIF Regression"""
    def __init__(self, model, params, cov_params, scale, use_t: bool = False, **kwds) -> None: ...
    def aic(self):
        """
        An AIC-like statistic for models fit using QIF.
        """
    def bic(self):
        """
        A BIC-like statistic for models fit using QIF.
        """
    def fittedvalues(self):
        """
        Returns the fitted values from the model.
        """
    def summary(self, yname: Incomplete | None = None, xname: Incomplete | None = None, title: Incomplete | None = None, alpha: float = 0.05):
        """
        Summarize the QIF regression results

        Parameters
        ----------
        yname : str, optional
            Default is `y`
        xname : list[str], optional
            Names for the exogenous variables, default is `var_#` for ## in
            the number of regressors. Must match the number of parameters in
            the model
        title : str, optional
            Title for the top table. If not None, then this replaces
            the default title
        alpha : float
            significance level for the confidence intervals

        Returns
        -------
        smry : Summary instance
            this holds the summary tables and text, which can be
            printed or converted to various output formats.

        See Also
        --------
        statsmodels.iolib.summary.Summary : class to hold summary results
        """

class QIFResultsWrapper(lm.RegressionResultsWrapper): ...
