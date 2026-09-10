import statsmodels.base.model as base
import statsmodels.base.wrapper as wrap
from _typeshed import Incomplete
from statsmodels.regression._prediction import PredictionResults as PredictionResults
from typing import Literal, Sequence

__all__ = ['GLS', 'WLS', 'OLS', 'GLSAR', 'PredictionResults', 'RegressionResultsWrapper']

class RegressionModel(base.LikelihoodModel):
    """
    Base class for linear regression models. Should not be directly called.

    Intended for subclassing.
    """
    pinv_wexog: Incomplete
    def __init__(self, endog, exog, **kwargs) -> None: ...
    wexog: Incomplete
    wendog: Incomplete
    nobs: Incomplete
    rank: Incomplete
    def initialize(self) -> None:
        """Initialize model components."""
    @property
    def df_model(self):
        """
        The model degree of freedom.

        The dof is defined as the rank of the regressor matrix minus 1 if a
        constant is included.
        """
    @df_model.setter
    def df_model(self, value) -> None: ...
    @property
    def df_resid(self):
        """
        The residual degree of freedom.

        The dof is defined as the number of observations minus the rank of
        the regressor matrix.
        """
    @df_resid.setter
    def df_resid(self, value) -> None: ...
    def whiten(self, x) -> None:
        """
        Whiten method that must be overwritten by individual models.

        Parameters
        ----------
        x : array_like
            Data to be whitened.
        """
    normalized_cov_params: Incomplete
    wexog_singular_values: Incomplete
    effects: Incomplete
    def fit(self, method: Literal['pinv', 'qr'] = 'pinv', cov_type: Literal['nonrobust', 'fixed scale', 'HC0', 'HC1', 'HC2', 'HC3', 'HAC', 'hac-panel', 'hac-groupsum', 'cluster'] = 'nonrobust', cov_kwds: Incomplete | None = None, use_t: bool | None = None, **kwargs):
        '''
        Full fit of the model.

        The results include an estimate of covariance matrix, (whitened)
        residuals and an estimate of scale.

        Parameters
        ----------
        method : str, optional
            Can be "pinv", "qr".  "pinv" uses the Moore-Penrose pseudoinverse
            to solve the least squares problem. "qr" uses the QR
            factorization.
        cov_type : str, optional
            See `regression.linear_model.RegressionResults` for a description
            of the available covariance estimators.
        cov_kwds : list or None, optional
            See `linear_model.RegressionResults.get_robustcov_results` for a
            description required keywords for alternative covariance
            estimators.
        use_t : bool, optional
            Flag indicating to use the Student\'s t distribution when computing
            p-values.  Default behavior depends on cov_type. See
            `linear_model.RegressionResults.get_robustcov_results` for
            implementation details.
        **kwargs
            Additional keyword arguments that contain information used when
            constructing a model using the formula interface.

        Returns
        -------
        RegressionResults
            The model estimation results.

        See Also
        --------
        RegressionResults
            The results container.
        RegressionResults.get_robustcov_results
            A method to change the covariance estimator used when fitting the
            model.

        Notes
        -----
        The fit method uses the pseudoinverse of the design/exogenous variables
        to solve the least squares minimization.
        '''
    def predict(self, params, exog: Incomplete | None = None):
        """
        Return linear predicted values from a design matrix.

        Parameters
        ----------
        params : array_like
            Parameters of a linear model.
        exog : array_like, optional
            Design / exogenous data. Model exog is used if None.

        Returns
        -------
        array_like
            An array of fitted values.

        Notes
        -----
        If the model has not yet been fit, params is not optional.
        """
    def get_distribution(self, params, scale, exog: Incomplete | None = None, dist_class: Incomplete | None = None):
        """
        Construct a random number generator for the predictive distribution.

        Parameters
        ----------
        params : array_like
            The model parameters (regression coefficients).
        scale : scalar
            The variance parameter.
        exog : array_like
            The predictor variable matrix.
        dist_class : class
            A random number generator class.  Must take 'loc' and 'scale'
            as arguments and return a random number generator implementing
            an ``rvs`` method for simulating random values. Defaults to normal.

        Returns
        -------
        gen
            Frozen random number generator object with mean and variance
            determined by the fitted linear model.  Use the ``rvs`` method
            to generate random values.

        Notes
        -----
        Due to the behavior of ``scipy.stats.distributions objects``,
        the returned random number generator must be called with
        ``gen.rvs(n)`` where ``n`` is the number of observations in
        the data set used to fit the model.  If any other value is
        used for ``n``, misleading results will be produced.
        """

class GLS(RegressionModel):
    __doc__: Incomplete
    def __init__(self, endog, exog, sigma: Incomplete | None = None, missing: str = 'none', hasconst: Incomplete | None = None, **kwargs) -> None: ...
    def whiten(self, x):
        """
        GLS whiten method.

        Parameters
        ----------
        x : array_like
            Data to be whitened.

        Returns
        -------
        ndarray
            The value np.dot(cholsigmainv,X).

        See Also
        --------
        GLS : Fit a linear model using Generalized Least Squares.
        """
    def loglike(self, params):
        """
        Compute the value of the Gaussian log-likelihood function at params.

        Given the whitened design matrix, the log-likelihood is evaluated
        at the parameter vector `params` for the dependent variable `endog`.

        Parameters
        ----------
        params : array_like
            The model parameters.

        Returns
        -------
        float
            The value of the log-likelihood function for a GLS Model.

        Notes
        -----
        The log-likelihood function for the normal distribution is

        .. math:: -\\frac{n}{2}\\log\\left(\\left(Y-\\hat{Y}\\right)^{\\prime}
                   \\left(Y-\\hat{Y}\\right)\\right)
                  -\\frac{n}{2}\\left(1+\\log\\left(\\frac{2\\pi}{n}\\right)\\right)
                  -\\frac{1}{2}\\log\\left(\\left|\\Sigma\\right|\\right)

        Y and Y-hat are whitened.
        """
    def hessian_factor(self, params, scale: Incomplete | None = None, observed: bool = True):
        """
        Compute weights for calculating Hessian.

        Parameters
        ----------
        params : ndarray
            The parameter at which Hessian is evaluated.
        scale : None or float
            If scale is None, then the default scale will be calculated.
            Default scale is defined by `self.scaletype` and set in fit.
            If scale is not None, then it is used as a fixed scale.
        observed : bool
            If True, then the observed Hessian is returned. If false then the
            expected information matrix is returned.

        Returns
        -------
        ndarray
            A 1d weight vector used in the calculation of the Hessian.
            The hessian is obtained by `(exog.T * hessian_factor).dot(exog)`.
        """
    def fit_regularized(self, method: str = 'elastic_net', alpha: float = 0.0, L1_wt: float = 1.0, start_params: Incomplete | None = None, profile_scale: bool = False, refit: bool = False, **kwargs): ...

class WLS(RegressionModel):
    __doc__: Incomplete
    def __init__(self, endog, exog, weights: float = 1.0, missing: str = 'none', hasconst: Incomplete | None = None, **kwargs) -> None: ...
    def whiten(self, x):
        """
        Whitener for WLS model, multiplies each column by sqrt(self.weights).

        Parameters
        ----------
        x : array_like
            Data to be whitened.

        Returns
        -------
        array_like
            The whitened values sqrt(weights)*X.
        """
    def loglike(self, params):
        """
        Compute the value of the gaussian log-likelihood function at params.

        Given the whitened design matrix, the log-likelihood is evaluated
        at the parameter vector `params` for the dependent variable `Y`.

        Parameters
        ----------
        params : array_like
            The parameter estimates.

        Returns
        -------
        float
            The value of the log-likelihood function for a WLS Model.

        Notes
        -----
        .. math:: -\\frac{n}{2}\\log SSR
                  -\\frac{n}{2}\\left(1+\\log\\left(\\frac{2\\pi}{n}\\right)\\right)
                  -\\frac{1}{2}\\log\\left(\\left|W\\right|\\right)

        where :math:`W` is a diagonal weight matrix matrix and
        :math:`SSR=\\left(Y-\\hat{Y}\\right)^\\prime W \\left(Y-\\hat{Y}\\right)` is
        the sum of the squared weighted residuals.
        """
    def hessian_factor(self, params, scale: Incomplete | None = None, observed: bool = True):
        """
        Compute the weights for calculating the Hessian.

        Parameters
        ----------
        params : ndarray
            The parameter at which Hessian is evaluated.
        scale : None or float
            If scale is None, then the default scale will be calculated.
            Default scale is defined by `self.scaletype` and set in fit.
            If scale is not None, then it is used as a fixed scale.
        observed : bool
            If True, then the observed Hessian is returned. If false then the
            expected information matrix is returned.

        Returns
        -------
        ndarray
            A 1d weight vector used in the calculation of the Hessian.
            The hessian is obtained by `(exog.T * hessian_factor).dot(exog)`.
        """
    def fit_regularized(self, method: str = 'elastic_net', alpha: float = 0.0, L1_wt: float = 1.0, start_params: Incomplete | None = None, profile_scale: bool = False, refit: bool = False, **kwargs): ...

class OLS(WLS):
    __doc__: Incomplete
    def __init__(self, endog, exog: Incomplete | None = None, missing: str = 'none', hasconst: Incomplete | None = None, **kwargs) -> None: ...
    def loglike(self, params, scale: Incomplete | None = None):
        """
        The likelihood function for the OLS model.

        Parameters
        ----------
        params : array_like
            The coefficients with which to estimate the log-likelihood.
        scale : float or None
            If None, return the profile (concentrated) log likelihood
            (profiled over the scale parameter), else return the
            log-likelihood using the given scale value.

        Returns
        -------
        float
            The likelihood function evaluated at params.
        """
    def whiten(self, x):
        """
        OLS model whitener does nothing.

        Parameters
        ----------
        x : array_like
            Data to be whitened.

        Returns
        -------
        array_like
            The input array unmodified.

        See Also
        --------
        OLS : Fit a linear model using Ordinary Least Squares.
        """
    def score(self, params, scale: Incomplete | None = None):
        """
        Evaluate the score function at a given point.

        The score corresponds to the profile (concentrated)
        log-likelihood in which the scale parameter has been profiled
        out.

        Parameters
        ----------
        params : array_like
            The parameter vector at which the score function is
            computed.
        scale : float or None
            If None, return the profile (concentrated) log likelihood
            (profiled over the scale parameter), else return the
            log-likelihood using the given scale value.

        Returns
        -------
        ndarray
            The score vector.
        """
    def hessian(self, params, scale: Incomplete | None = None):
        """
        Evaluate the Hessian function at a given point.

        Parameters
        ----------
        params : array_like
            The parameter vector at which the Hessian is computed.
        scale : float or None
            If None, return the profile (concentrated) log likelihood
            (profiled over the scale parameter), else return the
            log-likelihood using the given scale value.

        Returns
        -------
        ndarray
            The Hessian matrix.
        """
    def hessian_factor(self, params, scale: Incomplete | None = None, observed: bool = True):
        """
        Calculate the weights for the Hessian.

        Parameters
        ----------
        params : ndarray
            The parameter at which Hessian is evaluated.
        scale : None or float
            If scale is None, then the default scale will be calculated.
            Default scale is defined by `self.scaletype` and set in fit.
            If scale is not None, then it is used as a fixed scale.
        observed : bool
            If True, then the observed Hessian is returned. If false then the
            expected information matrix is returned.

        Returns
        -------
        ndarray
            A 1d weight vector used in the calculation of the Hessian.
            The hessian is obtained by `(exog.T * hessian_factor).dot(exog)`.
        """
    def fit_regularized(self, method: str = 'elastic_net', alpha: float = 0.0, L1_wt: float = 1.0, start_params: Incomplete | None = None, profile_scale: bool = False, refit: bool = False, **kwargs): ...

class GLSAR(GLS):
    __doc__: Incomplete
    order: Incomplete
    rho: Incomplete
    def __init__(self, endog, exog: Incomplete | None = None, rho: int = 1, missing: str = 'none', hasconst: Incomplete | None = None, **kwargs) -> None: ...
    def iterative_fit(self, maxiter: int = 3, rtol: float = 0.0001, **kwargs):
        """
        Perform an iterative two-stage procedure to estimate a GLS model.

        The model is assumed to have AR(p) errors, AR(p) parameters and
        regression coefficients are estimated iteratively.

        Parameters
        ----------
        maxiter : int, optional
            The number of iterations.
        rtol : float, optional
            Relative tolerance between estimated coefficients to stop the
            estimation.  Stops if max(abs(last - current) / abs(last)) < rtol.
        **kwargs
            Additional keyword arguments passed to `fit`.

        Returns
        -------
        RegressionResults
            The results computed using an iterative fit.
        """
    def whiten(self, x):
        """
        Whiten a series of columns according to an AR(p) covariance structure.

        Whitening using this method drops the initial p observations.

        Parameters
        ----------
        x : array_like
            The data to be whitened.

        Returns
        -------
        ndarray
            The whitened data.
        """

class RegressionResults(base.LikelihoodModelResults):
    """
    This class summarizes the fit of a linear regression model.

    It handles the output of contrasts, estimates of covariance, etc.

    Parameters
    ----------
    model : RegressionModel
        The regression model instance.
    params : ndarray
        The estimated parameters.
    normalized_cov_params : ndarray
        The normalized covariance parameters.
    scale : float
        The estimated scale of the residuals.
    cov_type : str
        The covariance estimator used in the results.
    cov_kwds : dict
        Additional keywords used in the covariance specification.
    use_t : bool
        Flag indicating to use the Student's t in inference.
    **kwargs
        Additional keyword arguments used to initialize the results.

    Attributes
    ----------
    pinv_wexog
        See model class docstring for implementation details.
    cov_type
        Parameter covariance estimator used for standard errors and t-stats.
    df_model
        Model degrees of freedom. The number of regressors `p`. Does not
        include the constant if one is present.
    df_resid
        Residual degrees of freedom. `n - p - 1`, if a constant is present.
        `n - p` if a constant is not included.
    het_scale
        adjusted squared residuals for heteroscedasticity robust standard
        errors. Is only available after `HC#_se` or `cov_HC#` is called.
        See HC#_se for more information.
    history
        Estimation history for iterative estimators.
    model
        A pointer to the model instance that called fit() or results.
    params
        The linear coefficients that minimize the least squares
        criterion.  This is usually called Beta for the classical
        linear model.
    """
    df_model: Incomplete
    df_resid: Incomplete
    cov_type: str
    cov_kwds: Incomplete
    use_t: Incomplete
    def __init__(self, model, params, normalized_cov_params: Incomplete | None = None, scale: float = 1.0, cov_type: str = 'nonrobust', cov_kwds: Incomplete | None = None, use_t: Incomplete | None = None, **kwargs) -> None: ...
    def conf_int(self, alpha: float = 0.05, cols: Incomplete | None = None):
        """
        Compute the confidence interval of the fitted parameters.

        Parameters
        ----------
        alpha : float, optional
            The `alpha` level for the confidence interval. The default
            `alpha` = .05 returns a 95% confidence interval.
        cols : array_like, optional
            Columns to include in returned confidence intervals.

        Returns
        -------
        array_like
            The confidence intervals.

        Notes
        -----
        The confidence interval is based on Student's t-distribution.
        """
    def nobs(self):
        """Number of observations n."""
    def fittedvalues(self):
        """The predicted values for the original (unwhitened) design."""
    def wresid(self):
        """
        The residuals of the transformed/whitened regressand and regressor(s).
        """
    def resid(self):
        """The residuals of the model."""
    def scale(self):
        """
        A scale factor for the covariance matrix.

        The Default value is ssr/(n-p).  Note that the square root of `scale`
        is often called the standard error of the regression.
        """
    def ssr(self):
        """Sum of squared (whitened) residuals."""
    def centered_tss(self):
        """The total (weighted) sum of squares centered about the mean."""
    def uncentered_tss(self):
        """
        Uncentered sum of squares.

        The sum of the squared values of the (whitened) endogenous response
        variable.
        """
    def ess(self):
        """
        The explained sum of squares.

        If a constant is present, the centered total sum of squares minus the
        sum of squared residuals. If there is no constant, the uncentered total
        sum of squares is used.
        """
    def rsquared(self):
        """
        R-squared of the model.

        This is defined here as 1 - `ssr`/`centered_tss` if the constant is
        included in the model and 1 - `ssr`/`uncentered_tss` if the constant is
        omitted.
        """
    def rsquared_adj(self):
        """
        Adjusted R-squared.

        This is defined here as 1 - (`nobs`-1)/`df_resid` * (1-`rsquared`)
        if a constant is included and 1 - `nobs`/`df_resid` * (1-`rsquared`) if
        no constant is included.
        """
    def mse_model(self):
        """
        Mean squared error the model.

        The explained sum of squares divided by the model degrees of freedom.
        """
    def mse_resid(self):
        """
        Mean squared error of the residuals.

        The sum of squared residuals divided by the residual degrees of
        freedom.
        """
    def mse_total(self):
        """
        Total mean squared error.

        The uncentered total sum of squares divided by the number of
        observations.
        """
    def fvalue(self):
        """
        F-statistic of the fully specified model.

        Calculated as the mean squared error of the model divided by the mean
        squared error of the residuals if the nonrobust covariance is used.
        Otherwise computed using a Wald-like quadratic form that tests whether
        all coefficients (excluding the constant) are zero.
        """
    def f_pvalue(self):
        """The p-value of the F-statistic."""
    def bse(self):
        """The standard errors of the parameter estimates."""
    def aic(self):
        """
        Akaike's information criteria.

        For a model with a constant :math:`-2llf + 2(df\\_model + 1)`. For a
        model without a constant :math:`-2llf + 2(df\\_model)`.
        """
    def bic(self):
        """
        Bayes' information criteria.

        For a model with a constant :math:`-2llf + \\log(n)(df\\_model+1)`.
        For a model without a constant :math:`-2llf + \\log(n)(df\\_model)`.
        """
    def info_criteria(self, crit, dk_params: int = 0):
        """Return an information criterion for the model.

        Parameters
        ----------
        crit : string
            One of 'aic', 'bic', 'aicc' or 'hqic'.
        dk_params : int or float
            Correction to the number of parameters used in the information
            criterion. By default, only mean parameters are included, the
            scale parameter is not included in the parameter count.
            Use ``dk_params=1`` to include scale in the parameter count.

        Returns
        -------
        Value of information criterion.

        References
        ----------
        Burnham KP, Anderson KR (2002). Model Selection and Multimodel
        Inference; Springer New York.
        """
    def eigenvals(self):
        """
        Return eigenvalues sorted in decreasing order.
        """
    def condition_number(self):
        """
        Return condition number of exogenous matrix.

        Calculated as ratio of largest to smallest singular value of the
        exogenous variables. This value is the same as the square root of
        the ratio of the largest to smallest eigenvalue of the inner-product
        of the exogenous variables.
        """
    het_scale: Incomplete
    def cov_HC0(self):
        """
        Heteroscedasticity robust covariance matrix. See HC0_se.
        """
    def cov_HC1(self):
        """
        Heteroscedasticity robust covariance matrix. See HC1_se.
        """
    def cov_HC2(self):
        """
        Heteroscedasticity robust covariance matrix. See HC2_se.
        """
    def cov_HC3(self):
        """
        Heteroscedasticity robust covariance matrix. See HC3_se.
        """
    def HC0_se(self):
        """
        White's (1980) heteroskedasticity robust standard errors.

        Notes
        -----
        Defined as sqrt(diag(X.T X)^(-1)X.T diag(e_i^(2)) X(X.T X)^(-1)
        where e_i = resid[i].

        When HC0_se or cov_HC0 is called the RegressionResults instance will
        then have another attribute `het_scale`, which is in this case is just
        resid**2.
        """
    def HC1_se(self):
        """
        MacKinnon and White's (1985) heteroskedasticity robust standard errors.

        Notes
        -----
        Defined as sqrt(diag(n/(n-p)*HC_0).

        When HC1_se or cov_HC1 is called the RegressionResults instance will
        then have another attribute `het_scale`, which is in this case is
        n/(n-p)*resid**2.
        """
    def HC2_se(self):
        """
        MacKinnon and White's (1985) heteroskedasticity robust standard errors.

        Notes
        -----
        Defined as (X.T X)^(-1)X.T diag(e_i^(2)/(1-h_ii)) X(X.T X)^(-1)
        where h_ii = x_i(X.T X)^(-1)x_i.T

        When HC2_se or cov_HC2 is called the RegressionResults instance will
        then have another attribute `het_scale`, which is in this case is
        resid^(2)/(1-h_ii).
        """
    def HC3_se(self):
        """
        MacKinnon and White's (1985) heteroskedasticity robust standard errors.

        Notes
        -----
        Defined as (X.T X)^(-1)X.T diag(e_i^(2)/(1-h_ii)^(2)) X(X.T X)^(-1)
        where h_ii = x_i(X.T X)^(-1)x_i.T.

        When HC3_se or cov_HC3 is called the RegressionResults instance will
        then have another attribute `het_scale`, which is in this case is
        resid^(2)/(1-h_ii)^(2).
        """
    def resid_pearson(self):
        """
        Residuals, normalized to have unit variance.

        Returns
        -------
        array_like
            The array `wresid` normalized by the sqrt of the scale to have
            unit variance.
        """
    def compare_lm_test(self, restricted, demean: bool = True, use_lr: bool = False):
        """
        Use Lagrange Multiplier test to test a set of linear restrictions.

        Parameters
        ----------
        restricted : Result instance
            The restricted model is assumed to be nested in the
            current model. The result instance of the restricted model
            is required to have two attributes, residual sum of
            squares, `ssr`, residual degrees of freedom, `df_resid`.
        demean : bool
            Flag indicating whether the demean the scores based on the
            residuals from the restricted model.  If True, the covariance of
            the scores are used and the LM test is identical to the large
            sample version of the LR test.
        use_lr : bool
            A flag indicating whether to estimate the covariance of the model
            scores using the unrestricted model. Setting the to True improves
            the power of the test.

        Returns
        -------
        lm_value : float
            The test statistic which has a chi2 distributed.
        p_value : float
            The p-value of the test statistic.
        df_diff : int
            The degrees of freedom of the restriction, i.e. difference in df
            between models.

        Notes
        -----
        The LM test examines whether the scores from the restricted model are
        0. If the null is true, and the restrictions are valid, then the
        parameters of the restricted model should be close to the minimum of
        the sum of squared errors, and so the scores should be close to zero,
        on average.
        """
    def compare_f_test(self, restricted):
        """
        Use F test to test whether restricted model is correct.

        Parameters
        ----------
        restricted : Result instance
            The restricted model is assumed to be nested in the
            current model. The result instance of the restricted model
            is required to have two attributes, residual sum of
            squares, `ssr`, residual degrees of freedom, `df_resid`.

        Returns
        -------
        f_value : float
            The test statistic which has an F distribution.
        p_value : float
            The p-value of the test statistic.
        df_diff : int
            The degrees of freedom of the restriction, i.e. difference in
            df between models.

        Notes
        -----
        See mailing list discussion October 17,

        This test compares the residual sum of squares of the two
        models.  This is not a valid test, if there is unspecified
        heteroscedasticity or correlation. This method will issue a
        warning if this is detected but still return the results under
        the assumption of homoscedasticity and no autocorrelation
        (sphericity).
        """
    def compare_lr_test(self, restricted, large_sample: bool = False):
        """
        Likelihood ratio test to test whether restricted model is correct.

        Parameters
        ----------
        restricted : Result instance
            The restricted model is assumed to be nested in the current model.
            The result instance of the restricted model is required to have two
            attributes, residual sum of squares, `ssr`, residual degrees of
            freedom, `df_resid`.

        large_sample : bool
            Flag indicating whether to use a heteroskedasticity robust version
            of the LR test, which is a modified LM test.

        Returns
        -------
        lr_stat : float
            The likelihood ratio which is chisquare distributed with df_diff
            degrees of freedom.
        p_value : float
            The p-value of the test statistic.
        df_diff : int
            The degrees of freedom of the restriction, i.e. difference in df
            between models.

        Notes
        -----
        The exact likelihood ratio is valid for homoskedastic data,
        and is defined as

        .. math:: D=-2\\log\\left(\\frac{\\mathcal{L}_{null}}
           {\\mathcal{L}_{alternative}}\\right)

        where :math:`\\mathcal{L}` is the likelihood of the
        model. With :math:`D` distributed as chisquare with df equal
        to difference in number of parameters or equivalently
        difference in residual degrees of freedom.

        The large sample version of the likelihood ratio is defined as

        .. math:: D=n s^{\\prime}S^{-1}s

        where :math:`s=n^{-1}\\sum_{i=1}^{n} s_{i}`

        .. math:: s_{i} = x_{i,alternative} \\epsilon_{i,null}

        is the average score of the model evaluated using the
        residuals from null model and the regressors from the
        alternative model and :math:`S` is the covariance of the
        scores, :math:`s_{i}`.  The covariance of the scores is
        estimated using the same estimator as in the alternative
        model.

        This test compares the loglikelihood of the two models.  This
        may not be a valid test, if there is unspecified
        heteroscedasticity or correlation. This method will issue a
        warning if this is detected but still return the results
        without taking unspecified heteroscedasticity or correlation
        into account.

        This test compares the loglikelihood of the two models.  This
        may not be a valid test, if there is unspecified
        heteroscedasticity or correlation. This method will issue a
        warning if this is detected but still return the results
        without taking unspecified heteroscedasticity or correlation
        into account.

        is the average score of the model evaluated using the
        residuals from null model and the regressors from the
        alternative model and :math:`S` is the covariance of the
        scores, :math:`s_{i}`.  The covariance of the scores is
        estimated using the same estimator as in the alternative
        model.
        """
    n_groups: Incomplete
    def get_robustcov_results(self, cov_type: str = 'HC1', use_t: Incomplete | None = None, **kwargs):
        '''
        Create new results instance with robust covariance as default.

        Parameters
        ----------
        cov_type : str
            The type of robust sandwich estimator to use. See Notes below.
        use_t : bool
            If true, then the t distribution is used for inference.
            If false, then the normal distribution is used.
            If `use_t` is None, then an appropriate default is used, which is
            `True` if the cov_type is nonrobust, and `False` in all other
            cases.
        **kwargs
            Required or optional arguments for robust covariance calculation.
            See Notes below.

        Returns
        -------
        RegressionResults
            This method creates a new results instance with the
            requested robust covariance as the default covariance of
            the parameters.  Inferential statistics like p-values and
            hypothesis tests will be based on this covariance matrix.

        Notes
        -----
        The following covariance types and required or optional arguments are
        currently available:

        - \'fixed scale\' uses a predefined scale

          ``scale``: float, optional
            Argument to set the scale. Default is 1.

        - \'HC0\', \'HC1\', \'HC2\', \'HC3\': heteroscedasticity robust covariance

          - no keyword arguments

        - \'HAC\': heteroskedasticity-autocorrelation robust covariance

          ``maxlags`` :  integer, required
            number of lags to use

          ``kernel`` : {callable, str}, optional
            kernels currently available kernels are [\'bartlett\', \'uniform\'],
            default is Bartlett

          ``use_correction``: bool, optional
            If true, use small sample correction

        - \'cluster\': clustered covariance estimator

          ``groups`` : array_like[int], required :
            Integer-valued index of clusters or groups.

          ``use_correction``: bool, optional
            If True the sandwich covariance is calculated with a small
            sample correction.
            If False the sandwich covariance is calculated without
            small sample correction.

          ``df_correction``: bool, optional
            If True (default), then the degrees of freedom for the
            inferential statistics and hypothesis tests, such as
            pvalues, f_pvalue, conf_int, and t_test and f_test, are
            based on the number of groups minus one instead of the
            total number of observations minus the number of explanatory
            variables. `df_resid` of the results instance is also
            adjusted. When `use_t` is also True, then pvalues are
            computed using the Student\'s t distribution using the
            corrected values. These may differ substantially from
            p-values based on the normal is the number of groups is
            small.
            If False, then `df_resid` of the results instance is not
            adjusted.

        - \'hac-groupsum\': Driscoll and Kraay, heteroscedasticity and
          autocorrelation robust covariance for panel data
          # TODO: more options needed here

          ``time`` : array_like, required
            index of time periods
          ``maxlags`` : integer, required
            number of lags to use
          ``kernel`` : {callable, str}, optional
            The available kernels are [\'bartlett\', \'uniform\']. The default is
            Bartlett.
          ``use_correction`` : {False, \'hac\', \'cluster\'}, optional
            If False the the sandwich covariance is calculated without small
            sample correction. If `use_correction = \'cluster\'` (default),
            then the same small sample correction as in the case of
            `covtype=\'cluster\'` is used.
          ``df_correction`` : bool, optional
            The adjustment to df_resid, see cov_type \'cluster\' above

        - \'hac-panel\': heteroscedasticity and autocorrelation robust standard
          errors in panel data. The data needs to be sorted in this case, the
          time series for each panel unit or cluster need to be stacked. The
          membership to a time series of an individual or group can be either
          specified by group indicators or by increasing time periods. One of
          ``groups`` or ``time`` is required. # TODO: we need more options here

          ``groups`` : array_like[int]
            indicator for groups
          ``time`` : array_like[int]
            index of time periods
          ``maxlags`` : int, required
            number of lags to use
          ``kernel`` : {callable, str}, optional
            Available kernels are [\'bartlett\', \'uniform\'], default
            is Bartlett
          ``use_correction`` : {False, \'hac\', \'cluster\'}, optional
            If False the sandwich covariance is calculated without
            small sample correction.
          ``df_correction`` : bool, optional
            Adjustment to df_resid, see cov_type \'cluster\' above

        **Reminder**: ``use_correction`` in "hac-groupsum" and "hac-panel" is
        not bool, needs to be in {False, \'hac\', \'cluster\'}.

        .. todo:: Currently there is no check for extra or misspelled keywords,
             except in the case of cov_type `HCx`
        '''
    def get_prediction(self, exog: Incomplete | None = None, transform: bool = True, weights: Incomplete | None = None, row_labels: Incomplete | None = None, **kwargs): ...
    diagn: Incomplete
    def summary(self, yname: str | None = None, xname: Sequence[str] | None = None, title: str | None = None, alpha: float = 0.05, slim: bool = False):
        """
        Summarize the Regression Results.

        Parameters
        ----------
        yname : str, optional
            Name of endogenous (response) variable. The Default is `y`.
        xname : list[str], optional
            Names for the exogenous variables. Default is `var_##` for ## in
            the number of regressors. Must match the number of parameters
            in the model.
        title : str, optional
            Title for the top table. If not None, then this replaces the
            default title.
        alpha : float, optional
            The significance level for the confidence intervals.
        slim : bool, optional
            Flag indicating to produce reduced set or diagnostic information.
            Default is False.

        Returns
        -------
        Summary
            Instance holding the summary tables and text, which can be printed
            or converted to various output formats.

        See Also
        --------
        statsmodels.iolib.summary.Summary : A class that holds summary results.
        """
    def summary2(self, yname: str | None = None, xname: Sequence[str] | None = None, title: str | None = None, alpha: float = 0.05, float_format: str = '%.4f'):
        """
        Experimental summary function to summarize the regression results.

        Parameters
        ----------
        yname : str
            The name of the dependent variable (optional).
        xname : list[str], optional
            Names for the exogenous variables. Default is `var_##` for ## in
            the number of regressors. Must match the number of parameters
            in the model.
        title : str, optional
            Title for the top table. If not None, then this replaces the
            default title.
        alpha : float
            The significance level for the confidence intervals.
        float_format : str
            The format for floats in parameters summary.

        Returns
        -------
        Summary
            Instance holding the summary tables and text, which can be printed
            or converted to various output formats.

        See Also
        --------
        statsmodels.iolib.summary2.Summary
            A class that holds summary results.
        """

class OLSResults(RegressionResults):
    """
    Results class for for an OLS model.

    Parameters
    ----------
    model : RegressionModel
        The regression model instance.
    params : ndarray
        The estimated parameters.
    normalized_cov_params : ndarray
        The normalized covariance parameters.
    scale : float
        The estimated scale of the residuals.
    cov_type : str
        The covariance estimator used in the results.
    cov_kwds : dict
        Additional keywords used in the covariance specification.
    use_t : bool
        Flag indicating to use the Student's t in inference.
    **kwargs
        Additional keyword arguments used to initialize the results.

    See Also
    --------
    RegressionResults
        Results store for WLS and GLW models.

    Notes
    -----
    Most of the methods and attributes are inherited from RegressionResults.
    The special methods that are only available for OLS are:

    - get_influence
    - outlier_test
    - el_test
    - conf_int_el
    """
    def get_influence(self):
        """
        Calculate influence and outlier measures.

        Returns
        -------
        OLSInfluence
            The instance containing methods to calculate the main influence and
            outlier measures for the OLS regression.

        See Also
        --------
        statsmodels.stats.outliers_influence.OLSInfluence
            A class that exposes methods to examine observation influence.
        """
    def outlier_test(self, method: str = 'bonf', alpha: float = 0.05, labels: Incomplete | None = None, order: bool = False, cutoff: Incomplete | None = None):
        """
        Test observations for outliers according to method.

        Parameters
        ----------
        method : str
            The method to use in the outlier test.  Must be one of:

            - `bonferroni` : one-step correction
            - `sidak` : one-step correction
            - `holm-sidak` :
            - `holm` :
            - `simes-hochberg` :
            - `hommel` :
            - `fdr_bh` : Benjamini/Hochberg
            - `fdr_by` : Benjamini/Yekutieli

            See `statsmodels.stats.multitest.multipletests` for details.
        alpha : float
            The familywise error rate (FWER).
        labels : None or array_like
            If `labels` is not None, then it will be used as index to the
            returned pandas DataFrame. See also Returns below.
        order : bool
            Whether or not to order the results by the absolute value of the
            studentized residuals. If labels are provided they will also be
            sorted.
        cutoff : None or float in [0, 1]
            If cutoff is not None, then the return only includes observations
            with multiple testing corrected p-values strictly below the cutoff.
            The returned array or dataframe can be empty if t.

        Returns
        -------
        array_like
            Returns either an ndarray or a DataFrame if labels is not None.
            Will attempt to get labels from model_results if available. The
            columns are the Studentized residuals, the unadjusted p-value,
            and the corrected p-value according to method.

        Notes
        -----
        The unadjusted p-value is stats.t.sf(abs(resid), df) where
        df = df_resid - 1.
        """
    def el_test(self, b0_vals, param_nums, return_weights: int = 0, ret_params: int = 0, method: str = 'nm', stochastic_exog: int = 1):
        """
        Test single or joint hypotheses using Empirical Likelihood.

        Parameters
        ----------
        b0_vals : 1darray
            The hypothesized value of the parameter to be tested.
        param_nums : 1darray
            The parameter number to be tested.
        return_weights : bool
            If true, returns the weights that optimize the likelihood
            ratio at b0_vals. The default is False.
        ret_params : bool
            If true, returns the parameter vector that maximizes the likelihood
            ratio at b0_vals.  Also returns the weights.  The default is False.
        method : str
            Can either be 'nm' for Nelder-Mead or 'powell' for Powell.  The
            optimization method that optimizes over nuisance parameters.
            The default is 'nm'.
        stochastic_exog : bool
            When True, the exogenous variables are assumed to be stochastic.
            When the regressors are nonstochastic, moment conditions are
            placed on the exogenous variables.  Confidence intervals for
            stochastic regressors are at least as large as non-stochastic
            regressors. The default is True.

        Returns
        -------
        tuple
            The p-value and -2 times the log-likelihood ratio for the
            hypothesized values.

        Examples
        --------
        >>> import statsmodels.api as sm
        >>> data = sm.datasets.stackloss.load()
        >>> endog = data.endog
        >>> exog = sm.add_constant(data.exog)
        >>> model = sm.OLS(endog, exog)
        >>> fitted = model.fit()
        >>> fitted.params
        >>> array([-39.91967442,   0.7156402 ,   1.29528612,  -0.15212252])
        >>> fitted.rsquared
        >>> 0.91357690446068196
        >>> # Test that the slope on the first variable is 0
        >>> fitted.el_test([0], [1])
        >>> (27.248146353888796, 1.7894660442330235e-07)
        """
    def conf_int_el(self, param_num, sig: float = 0.05, upper_bound: Incomplete | None = None, lower_bound: Incomplete | None = None, method: str = 'nm', stochastic_exog: bool = True):
        """
        Compute the confidence interval using Empirical Likelihood.

        Parameters
        ----------
        param_num : float
            The parameter for which the confidence interval is desired.
        sig : float
            The significance level.  Default is 0.05.
        upper_bound : float
            The maximum value the upper limit can be.  Default is the
            99.9% confidence value under OLS assumptions.
        lower_bound : float
            The minimum value the lower limit can be.  Default is the 99.9%
            confidence value under OLS assumptions.
        method : str
            Can either be 'nm' for Nelder-Mead or 'powell' for Powell.  The
            optimization method that optimizes over nuisance parameters.
            The default is 'nm'.
        stochastic_exog : bool
            When True, the exogenous variables are assumed to be stochastic.
            When the regressors are nonstochastic, moment conditions are
            placed on the exogenous variables.  Confidence intervals for
            stochastic regressors are at least as large as non-stochastic
            regressors.  The default is True.

        Returns
        -------
        lowerl : float
            The lower bound of the confidence interval.
        upperl : float
            The upper bound of the confidence interval.

        See Also
        --------
        el_test : Test parameters using Empirical Likelihood.

        Notes
        -----
        This function uses brentq to find the value of beta where
        test_beta([beta], param_num)[1] is equal to the critical value.

        The function returns the results of each iteration of brentq at each
        value of beta.

        The current function value of the last printed optimization should be
        the critical value at the desired significance level. For alpha=.05,
        the value is 3.841459.

        To ensure optimization terminated successfully, it is suggested to do
        el_test([lower_limit], [param_num]).

        If the optimization does not terminate successfully, consider switching
        optimization algorithms.

        If optimization is still not successful, try changing the values of
        start_int_params.  If the current function value repeatedly jumps
        from a number between 0 and the critical value and a very large number
        (>50), the starting parameters of the interior minimization need
        to be changed.
        """

class RegressionResultsWrapper(wrap.ResultsWrapper): ...
