import statsmodels.tsa.base.tsa_model as tsbase
from _typeshed import Incomplete
from collections.abc import Generator
from statsmodels.base.data import PandasData as PandasData
from statsmodels.tools.decorators import cache_readonly as cache_readonly
from statsmodels.tools.eval_measures import aic as aic, aicc as aicc, bic as bic, hqic as hqic
from statsmodels.tools.numdiff import approx_fprime as approx_fprime, approx_fprime_cs as approx_fprime_cs, approx_hess_cs as approx_hess_cs
from statsmodels.tools.sm_exceptions import PrecisionWarning as PrecisionWarning
from statsmodels.tools.tools import pinv_extended as pinv_extended

class StateSpaceMLEModel(tsbase.TimeSeriesModel):
    """
    This is a temporary base model from ETS, here I just copy everything I need
    from statespace.mlemodel.MLEModel
    """
    use_pandas: Incomplete
    nobs: Incomplete
    def __init__(self, endog, exog: Incomplete | None = None, dates: Incomplete | None = None, freq: Incomplete | None = None, missing: str = 'none', **kwargs) -> None: ...
    @staticmethod
    def prepare_data(data) -> None: ...
    def clone(self, endog, exog: Incomplete | None = None, **kwargs) -> None: ...
    @property
    def k_params(self): ...
    def fix_params(self, params) -> Generator[None, None, None]:
        """
        Fix parameters to specific values (context manager)

        Parameters
        ----------
        params : dict
            Dictionary describing the fixed parameter values, of the form
            `param_name: fixed_value`. See the `param_names` property for valid
            parameter names.

        Examples
        --------
        >>> mod = sm.tsa.SARIMAX(endog, order=(1, 0, 1))
        >>> with mod.fix_params({'ar.L1': 0.5}):
                res = mod.fit()
        """
    def fit_constrained(self, constraints, start_params: Incomplete | None = None, **fit_kwds):
        """
        Fit the model with some parameters subject to equality constraints.

        Parameters
        ----------
        constraints : dict
            Dictionary of constraints, of the form `param_name: fixed_value`.
            See the `param_names` property for valid parameter names.
        start_params : array_like, optional
            Initial guess of the solution for the loglikelihood maximization.
            If None, the default is given by Model.start_params.
        **fit_kwds : keyword arguments
            fit_kwds are used in the optimization of the remaining parameters.

        Returns
        -------
        results : Results instance

        Examples
        --------
        >>> mod = sm.tsa.SARIMAX(endog, order=(1, 0, 1))
        >>> res = mod.fit_constrained({'ar.L1': 0.5})
        """
    @property
    def start_params(self):
        """
        (array) Starting parameters for maximum likelihood estimation.
        """
    @property
    def param_names(self):
        """
        (list of str) List of human readable parameter names (for parameters
        actually included in the model).
        """
    @classmethod
    def from_formula(cls, formula, data, subset: Incomplete | None = None, drop_cols: Incomplete | None = None, *args, **kwargs) -> None:
        """
        Not implemented for state space models
        """

class StateSpaceMLEResults(tsbase.TimeSeriesModelResults):
    """
    Class to hold results from fitting a state space model.

    Parameters
    ----------
    model : MLEModel instance
        The fitted model instance
    params : ndarray
        Fitted parameters

    Attributes
    ----------
    model : Model instance
        A reference to the model that was fit.
    nobs : float
        The number of observations used to fit the model.
    params : ndarray
        The parameters of the model.
    """
    data: Incomplete
    endog: Incomplete
    fixed_params: Incomplete
    param_names: Incomplete
    nobs: Incomplete
    k_params: Incomplete
    def __init__(self, model, params, scale: float = 1.0) -> None: ...
    def nobs_effective(self) -> None: ...
    def df_resid(self): ...
    def aic(self):
        """
        (float) Akaike Information Criterion
        """
    def aicc(self):
        """
        (float) Akaike Information Criterion with small sample correction
        """
    def bic(self):
        """
        (float) Bayes Information Criterion
        """
    def fittedvalues(self) -> None: ...
    def hqic(self):
        """
        (float) Hannan-Quinn Information Criterion
        """
    def llf(self) -> None:
        """
        (float) The value of the log-likelihood function evaluated at `params`.
        """
    def mae(self):
        """
        (float) Mean absolute error
        """
    def mse(self):
        """
        (float) Mean squared error
        """
    def pvalues(self):
        """
        (array) The p-values associated with the z-statistics of the
        coefficients. Note that the coefficients are assumed to have a Normal
        distribution.
        """
    def resid(self) -> None: ...
    def sse(self):
        """
        (float) Sum of squared errors
        """
    def zvalues(self):
        """
        (array) The z-statistics for the coefficients.
        """
    def cov_params_approx(self):
        """
        (array) The variance / covariance matrix. Computed using the numerical
        Hessian approximated by complex step or finite differences methods.
        """
    def test_serial_correlation(self, method, lags: Incomplete | None = None):
        """
        Ljung-Box test for no serial correlation of standardized residuals

        Null hypothesis is no serial correlation.

        Parameters
        ----------
        method : {'ljungbox','boxpierece', None}
            The statistical test for serial correlation. If None, an attempt is
            made to select an appropriate test.
        lags : None, int or array_like
            If lags is an integer then this is taken to be the largest lag
            that is included, the test result is reported for all smaller lag
            length.
            If lags is a list or array, then all lags are included up to the
            largest lag in the list, however only the tests for the lags in the
            list are reported.
            If lags is None, then the default maxlag is min(10, nobs//5) for
            non-seasonal time series and min (2*m, nobs//5) for seasonal time
            series.

        Returns
        -------
        output : ndarray
            An array with `(test_statistic, pvalue)` for each endogenous
            variable and each lag. The array is then sized
            `(k_endog, 2, lags)`. If the method is called as
            `ljungbox = res.test_serial_correlation()`, then `ljungbox[i]`
            holds the results of the Ljung-Box test (as would be returned by
            `statsmodels.stats.diagnostic.acorr_ljungbox`) for the `i` th
            endogenous variable.

        See Also
        --------
        statsmodels.stats.diagnostic.acorr_ljungbox
            Ljung-Box test for serial correlation.

        Notes
        -----
        For statespace models: let `d` = max(loglikelihood_burn, nobs_diffuse);
        this test is calculated ignoring the first `d` residuals.

        Output is nan for any endogenous variable which has missing values.
        """
    def test_heteroskedasticity(self, method, alternative: str = 'two-sided', use_f: bool = True):
        """
        Test for heteroskedasticity of standardized residuals

        Tests whether the sum-of-squares in the first third of the sample is
        significantly different than the sum-of-squares in the last third
        of the sample. Analogous to a Goldfeld-Quandt test. The null hypothesis
        is of no heteroskedasticity.

        Parameters
        ----------
        method : {'breakvar', None}
            The statistical test for heteroskedasticity. Must be 'breakvar'
            for test of a break in the variance. If None, an attempt is
            made to select an appropriate test.
        alternative : str, 'increasing', 'decreasing' or 'two-sided'
            This specifies the alternative for the p-value calculation. Default
            is two-sided.
        use_f : bool, optional
            Whether or not to compare against the asymptotic distribution
            (chi-squared) or the approximate small-sample distribution (F).
            Default is True (i.e. default is to compare against an F
            distribution).

        Returns
        -------
        output : ndarray
            An array with `(test_statistic, pvalue)` for each endogenous
            variable. The array is then sized `(k_endog, 2)`. If the method is
            called as `het = res.test_heteroskedasticity()`, then `het[0]` is
            an array of size 2 corresponding to the first endogenous variable,
            where `het[0][0]` is the test statistic, and `het[0][1]` is the
            p-value.

        Notes
        -----
        The null hypothesis is of no heteroskedasticity. That means different
        things depending on which alternative is selected:

        - Increasing: Null hypothesis is that the variance is not increasing
          throughout the sample; that the sum-of-squares in the later
          subsample is *not* greater than the sum-of-squares in the earlier
          subsample.
        - Decreasing: Null hypothesis is that the variance is not decreasing
          throughout the sample; that the sum-of-squares in the earlier
          subsample is *not* greater than the sum-of-squares in the later
          subsample.
        - Two-sided: Null hypothesis is that the variance is not changing
          throughout the sample. Both that the sum-of-squares in the earlier
          subsample is not greater than the sum-of-squares in the later
          subsample *and* that the sum-of-squares in the later subsample is
          not greater than the sum-of-squares in the earlier subsample.

        For :math:`h = [T/3]`, the test statistic is:

        .. math::

            H(h) = \\sum_{t=T-h+1}^T  \\tilde v_t^2
            \\Bigg / \\sum_{t=d+1}^{d+1+h} \\tilde v_t^2

        where :math:`d` = max(loglikelihood_burn, nobs_diffuse)` (usually
        corresponding to diffuse initialization under either the approximate
        or exact approach).

        This statistic can be tested against an :math:`F(h,h)` distribution.
        Alternatively, :math:`h H(h)` is asymptotically distributed according
        to :math:`\\chi_h^2`; this second test can be applied by passing
        `asymptotic=True` as an argument.

        See section 5.4 of [1]_ for the above formula and discussion, as well
        as additional details.

        TODO

        - Allow specification of :math:`h`

        References
        ----------
        .. [1] Harvey, Andrew C. 1990. *Forecasting, Structural Time Series*
               *Models and the Kalman Filter.* Cambridge University Press.
        """
    def test_normality(self, method):
        """
        Test for normality of standardized residuals.

        Null hypothesis is normality.

        Parameters
        ----------
        method : {'jarquebera', None}
            The statistical test for normality. Must be 'jarquebera' for
            Jarque-Bera normality test. If None, an attempt is made to select
            an appropriate test.

        See Also
        --------
        statsmodels.stats.stattools.jarque_bera
            The Jarque-Bera test of normality.

        Notes
        -----
        For statespace models: let `d` = max(loglikelihood_burn, nobs_diffuse);
        this test is calculated ignoring the first `d` residuals.

        In the case of missing data, the maintained hypothesis is that the
        data are missing completely at random. This test is then run on the
        standardized residuals excluding those corresponding to missing
        observations.
        """
    def summary(self, alpha: float = 0.05, start: Incomplete | None = None, title: Incomplete | None = None, model_name: Incomplete | None = None, display_params: bool = True):
        """
        Summarize the Model

        Parameters
        ----------
        alpha : float, optional
            Significance level for the confidence intervals. Default is 0.05.
        start : int, optional
            Integer of the start observation. Default is 0.
        model_name : str
            The name of the model used. Default is to use model class name.

        Returns
        -------
        summary : Summary instance
            This holds the summary table and text, which can be printed or
            converted to various output formats.

        See Also
        --------
        statsmodels.iolib.summary.Summary
        """
