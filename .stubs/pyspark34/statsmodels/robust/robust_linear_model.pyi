import statsmodels.base.model as base
import statsmodels.regression.linear_model as lm
from _typeshed import Incomplete

__all__ = ['RLM']

class RLM(base.LikelihoodModel):
    __doc__: Incomplete
    M: Incomplete
    def __init__(self, endog, exog, M: Incomplete | None = None, missing: str = 'none', **kwargs) -> None: ...
    def score(self, params) -> None: ...
    def information(self, params) -> None: ...
    def predict(self, params, exog: Incomplete | None = None):
        """
        Return linear predicted values from a design matrix.

        Parameters
        ----------
        params : array_like
            Parameters of a linear model
        exog : array_like, optional.
            Design / exogenous data. Model exog is used if None.

        Returns
        -------
        An array of fitted values
        """
    def loglike(self, params) -> None: ...
    def deviance(self, tmp_results):
        """
        Returns the (unnormalized) log-likelihood from the M estimator.
        """
    cov: Incomplete
    scale_est: Incomplete
    scale: Incomplete
    weights: Incomplete
    def fit(self, maxiter: int = 50, tol: float = 1e-08, scale_est: str = 'mad', init: Incomplete | None = None, cov: str = 'H1', update_scale: bool = True, conv: str = 'dev', start_params: Incomplete | None = None):
        '''
        Fits the model using iteratively reweighted least squares.

        The IRLS routine runs until the specified objective converges to `tol`
        or `maxiter` has been reached.

        Parameters
        ----------
        conv : str
            Indicates the convergence criteria.
            Available options are "coefs" (the coefficients), "weights" (the
            weights in the iteration), "sresid" (the standardized residuals),
            and "dev" (the un-normalized log-likelihood for the M
            estimator).  The default is "dev".
        cov : str, optional
            \'H1\', \'H2\', or \'H3\'
            Indicates how the covariance matrix is estimated.  Default is \'H1\'.
            See rlm.RLMResults for more information.
        init : str
            Specifies method for the initial estimates of the parameters.
            Default is None, which means that the least squares estimate
            is used.  Currently it is the only available choice.
        maxiter : int
            The maximum number of iterations to try. Default is 50.
        scale_est : str or HuberScale()
            \'mad\' or HuberScale()
            Indicates the estimate to use for scaling the weights in the IRLS.
            The default is \'mad\' (median absolute deviation.  Other options are
            \'HuberScale\' for Huber\'s proposal 2. Huber\'s proposal 2 has
            optional keyword arguments d, tol, and maxiter for specifying the
            tuning constant, the convergence tolerance, and the maximum number
            of iterations. See statsmodels.robust.scale for more information.
        tol : float
            The convergence tolerance of the estimate.  Default is 1e-8.
        update_scale : Bool
            If `update_scale` is False then the scale estimate for the
            weights is held constant over the iteration.  Otherwise, it
            is updated for each fit in the iteration.  Default is True.
        start_params : array_like, optional
            Initial guess of the solution of the optimizer. If not provided,
            the initial parameters are computed using OLS.

        Returns
        -------
        results : statsmodels.rlm.RLMresults
            Results instance
        '''

class RLMResults(base.LikelihoodModelResults):
    '''
    Class to contain RLM results

    Attributes
    ----------

    bcov_scaled : ndarray
        p x p scaled covariance matrix specified in the model fit method.
        The default is H1. H1 is defined as
        ``k**2 * (1/df_resid*sum(M.psi(sresid)**2)*scale**2)/
        ((1/nobs*sum(M.psi_deriv(sresid)))**2) * (X.T X)^(-1)``

        where ``k = 1 + (df_model +1)/nobs * var_psiprime/m**2``
        where ``m = mean(M.psi_deriv(sresid))`` and
        ``var_psiprime = var(M.psi_deriv(sresid))``

        H2 is defined as
        ``k * (1/df_resid) * sum(M.psi(sresid)**2) *scale**2/
        ((1/nobs)*sum(M.psi_deriv(sresid)))*W_inv``

        H3 is defined as
        ``1/k * (1/df_resid * sum(M.psi(sresid)**2)*scale**2 *
        (W_inv X.T X W_inv))``

        where `k` is defined as above and
        ``W_inv = (M.psi_deriv(sresid) exog.T exog)^(-1)``

        See the technical documentation for cleaner formulae.
    bcov_unscaled : ndarray
        The usual p x p covariance matrix with scale set equal to 1.  It
        is then just equivalent to normalized_cov_params.
    bse : ndarray
        An array of the standard errors of the parameters.  The standard
        errors are taken from the robust covariance matrix specified in the
        argument to fit.
    chisq : ndarray
        An array of the chi-squared values of the parameter estimates.
    df_model
        See RLM.df_model
    df_resid
        See RLM.df_resid
    fit_history : dict
        Contains information about the iterations. Its keys are `deviance`,
        `params`, `iteration` and the convergence criteria specified in
        `RLM.fit`, if different from `deviance` or `params`.
    fit_options : dict
        Contains the options given to fit.
    fittedvalues : ndarray
        The linear predicted values.  dot(exog, params)
    model : statsmodels.rlm.RLM
        A reference to the model instance
    nobs : float
        The number of observations n
    normalized_cov_params : ndarray
        See RLM.normalized_cov_params
    params : ndarray
        The coefficients of the fitted model
    pinv_wexog : ndarray
        See RLM.pinv_wexog
    pvalues : ndarray
        The p values associated with `tvalues`. Note that `tvalues` are assumed
        to be distributed standard normal rather than Student\'s t.
    resid : ndarray
        The residuals of the fitted model.  endog - fittedvalues
    scale : float
        The type of scale is determined in the arguments to the fit method in
        RLM.  The reported scale is taken from the residuals of the weighted
        least squares in the last IRLS iteration if update_scale is True.  If
        update_scale is False, then it is the scale given by the first OLS
        fit before the IRLS iterations.
    sresid : ndarray
        The scaled residuals.
    tvalues : ndarray
        The "t-statistics" of params. These are defined as params/bse where
        bse are taken from the robust covariance matrix specified in the
        argument to fit.
    weights : ndarray
        The reported weights are determined by passing the scaled residuals
        from the last weighted least squares fit in the IRLS algorithm.

    See Also
    --------
    statsmodels.base.model.LikelihoodModelResults
    '''
    model: Incomplete
    df_model: Incomplete
    df_resid: Incomplete
    nobs: Incomplete
    cov_params_default: Incomplete
    def __init__(self, model, params, normalized_cov_params, scale) -> None: ...
    def fittedvalues(self): ...
    def resid(self): ...
    def sresid(self): ...
    def bcov_unscaled(self): ...
    def weights(self): ...
    def bcov_scaled(self): ...
    def pvalues(self): ...
    def bse(self): ...
    def chisq(self): ...
    def summary(self, yname: Incomplete | None = None, xname: Incomplete | None = None, title: int = 0, alpha: float = 0.05, return_fmt: str = 'text'):
        """
        This is for testing the new summary setup
        """
    def summary2(self, xname: Incomplete | None = None, yname: Incomplete | None = None, title: Incomplete | None = None, alpha: float = 0.05, float_format: str = '%.4f'):
        """Experimental summary function for regression results

        Parameters
        ----------
        yname : str
            Name of the dependent variable (optional)
        xname : list[str], optional
            Names for the exogenous variables. Default is `var_##` for ## in
            the number of regressors. Must match the number of parameters
            in the model
        title : str, optional
            Title for the top table. If not None, then this replaces the
            default title
        alpha : float
            significance level for the confidence intervals
        float_format : str
            print format for floats in parameters summary

        Returns
        -------
        smry : Summary instance
            this holds the summary tables and text, which can be printed or
            converted to various output formats.

        See Also
        --------
        statsmodels.iolib.summary2.Summary : class to hold summary results
        """

class RLMResultsWrapper(lm.RegressionResultsWrapper): ...
