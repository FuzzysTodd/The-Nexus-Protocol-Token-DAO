import datetime
import numpy as np
import pandas as pd
import statsmodels.base.wrapper as wrap
from _typeshed import Incomplete
from statsmodels.tools.typing import ArrayLike, ArrayLike1D, ArrayLike2D
from statsmodels.tsa.base import tsa_model
from statsmodels.tsa.deterministic import DeterministicProcess
from typing import Any, Literal, Sequence

__all__ = ['AR', 'AutoReg']

class AutoReg(tsa_model.TimeSeriesModel):
    '''
    Autoregressive AR-X(p) model

    Estimate an AR-X model using Conditional Maximum Likelihood (OLS).

    Parameters
    ----------
    endog : array_like
        A 1-d endogenous response variable. The dependent variable.
    lags : {None, int, list[int]}
        The number of lags to include in the model if an integer or the
        list of lag indices to include.  For example, [1, 4] will only
        include lags 1 and 4 while lags=4 will include lags 1, 2, 3, and 4.
        None excludes all AR lags, and behave identically to 0.
    trend : {\'n\', \'c\', \'t\', \'ct\'}
        The trend to include in the model:

        * \'n\' - No trend.
        * \'c\' - Constant only.
        * \'t\' - Time trend only.
        * \'ct\' - Constant and time trend.

    seasonal : bool
        Flag indicating whether to include seasonal dummies in the model. If
        seasonal is True and trend includes \'c\', then the first period
        is excluded from the seasonal terms.
    exog : array_like, optional
        Exogenous variables to include in the model. Must have the same number
        of observations as endog and should be aligned so that endog[i] is
        regressed on exog[i].
    hold_back : {None, int}
        Initial observations to exclude from the estimation sample.  If None,
        then hold_back is equal to the maximum lag in the model.  Set to a
        non-zero value to produce comparable models with different lag
        length.  For example, to compare the fit of a model with lags=3 and
        lags=1, set hold_back=3 which ensures that both models are estimated
        using observations 3,...,nobs. hold_back must be >= the maximum lag in
        the model.
    period : {None, int}
        The period of the data. Only used if seasonal is True. This parameter
        can be omitted if using a pandas object for endog that contains a
        recognized frequency.
    missing : str
        Available options are \'none\', \'drop\', and \'raise\'. If \'none\', no nan
        checking is done. If \'drop\', any observations with nans are dropped.
        If \'raise\', an error is raised. Default is \'none\'.
    deterministic : DeterministicProcess
        A deterministic process.  If provided, trend and seasonal are ignored.
        A warning is raised if trend is not "n" and seasonal is not False.
    old_names : bool
        Flag indicating whether to use the v0.11 names or the v0.12+ names.

        .. deprecated:: 0.13.0

           old_names is deprecated and will be removed after 0.14 is
           released. You must update any code reliant on the old variable
           names to use the new names.

    See Also
    --------
    statsmodels.tsa.statespace.sarimax.SARIMAX
        Estimation of SARIMAX models using exact likelihood and the
        Kalman Filter.

    Notes
    -----
    See the notebook `Autoregressions
    <../examples/notebooks/generated/autoregressions.html>`__ for an overview.

    Examples
    --------
    >>> import statsmodels.api as sm
    >>> from statsmodels.tsa.ar_model import AutoReg
    >>> data = sm.datasets.sunspots.load_pandas().data[\'SUNACTIVITY\']
    >>> out = \'AIC: {0:0.3f}, HQIC: {1:0.3f}, BIC: {2:0.3f}\'

    Start by fitting an unrestricted Seasonal AR model

    >>> res = AutoReg(data, lags = [1, 11, 12]).fit()
    >>> print(out.format(res.aic, res.hqic, res.bic))
    AIC: 5.945, HQIC: 5.970, BIC: 6.007

    An alternative used seasonal dummies

    >>> res = AutoReg(data, lags=1, seasonal=True, period=11).fit()
    >>> print(out.format(res.aic, res.hqic, res.bic))
    AIC: 6.017, HQIC: 6.080, BIC: 6.175

    Finally, both the seasonal AR structure and dummies can be included

    >>> res = AutoReg(data, lags=[1, 11, 12], seasonal=True, period=11).fit()
    >>> print(out.format(res.aic, res.hqic, res.bic))
    AIC: 5.884, HQIC: 5.959, BIC: 6.071
    '''
    nobs: Incomplete
    def __init__(self, endog: ArrayLike1D, lags: int | Sequence[int] | None, trend: Literal['n', 'c', 't', 'ct'] = 'c', seasonal: bool = False, exog: ArrayLike2D | None = None, hold_back: int | None = None, period: int | None = None, missing: str = 'none', *, deterministic: DeterministicProcess | None = None, old_names: bool = False) -> None: ...
    @property
    def ar_lags(self) -> list[int] | None:
        """The autoregressive lags included in the model"""
    @property
    def hold_back(self) -> int | None:
        """The number of initial obs. excluded from the estimation sample."""
    @property
    def trend(self) -> Literal['n', 'c', 'ct', 'ctt']:
        """The trend used in the model."""
    @property
    def seasonal(self) -> bool:
        """Flag indicating that the model contains a seasonal component."""
    @property
    def deterministic(self) -> DeterministicProcess | None:
        """The deterministic used to construct the model"""
    @property
    def period(self) -> int | None:
        """The period of the seasonal component."""
    @property
    def df_model(self) -> int:
        """The model degrees of freedom."""
    @property
    def exog_names(self) -> list[str] | None:
        """Names of exogenous variables included in model"""
    def initialize(self) -> None:
        """Initialize the model (no-op)."""
    def fit(self, cov_type: str = 'nonrobust', cov_kwds: dict[str, Any] | None = None, use_t: bool = False) -> AutoRegResultsWrapper:
        """
        Estimate the model parameters.

        Parameters
        ----------
        cov_type : str
            The covariance estimator to use. The most common choices are listed
            below.  Supports all covariance estimators that are available
            in ``OLS.fit``.

            * 'nonrobust' - The class OLS covariance estimator that assumes
              homoskedasticity.
            * 'HC0', 'HC1', 'HC2', 'HC3' - Variants of White's
              (or Eiker-Huber-White) covariance estimator. `HC0` is the
              standard implementation.  The other make corrections to improve
              the finite sample performance of the heteroskedasticity robust
              covariance estimator.
            * 'HAC' - Heteroskedasticity-autocorrelation robust covariance
              estimation. Supports cov_kwds.

              - `maxlags` integer (required) : number of lags to use.
              - `kernel` callable or str (optional) : kernel
                  currently available kernels are ['bartlett', 'uniform'],
                  default is Bartlett.
              - `use_correction` bool (optional) : If true, use small sample
                  correction.
        cov_kwds : dict, optional
            A dictionary of keyword arguments to pass to the covariance
            estimator. `nonrobust` and `HC#` do not support cov_kwds.
        use_t : bool, optional
            A flag indicating that inference should use the Student's t
            distribution that accounts for model degree of freedom.  If False,
            uses the normal distribution. If None, defers the choice to
            the cov_type. It also removes degree of freedom corrections from
            the covariance estimator when cov_type is 'nonrobust'.

        Returns
        -------
        AutoRegResults
            Estimation results.

        See Also
        --------
        statsmodels.regression.linear_model.OLS
            Ordinary Least Squares estimation.
        statsmodels.regression.linear_model.RegressionResults
            See ``get_robustcov_results`` for a detailed list of available
            covariance estimators and options.

        Notes
        -----
        Use ``OLS`` to estimate model parameters and to estimate parameter
        covariance.
        """
    def loglike(self, params: ArrayLike) -> float:
        """
        Log-likelihood of model.

        Parameters
        ----------
        params : ndarray
            The model parameters used to compute the log-likelihood.

        Returns
        -------
        float
            The log-likelihood value.
        """
    def score(self, params: ArrayLike) -> np.ndarray:
        """
        Score vector of model.

        The gradient of logL with respect to each parameter.

        Parameters
        ----------
        params : ndarray
            The parameters to use when evaluating the Hessian.

        Returns
        -------
        ndarray
            The score vector evaluated at the parameters.
        """
    def information(self, params: ArrayLike) -> np.ndarray:
        """
        Fisher information matrix of model.

        Returns -1 * Hessian of the log-likelihood evaluated at params.

        Parameters
        ----------
        params : ndarray
            The model parameters.

        Returns
        -------
        ndarray
            The information matrix.
        """
    def hessian(self, params: ArrayLike) -> np.ndarray:
        """
        The Hessian matrix of the model.

        Parameters
        ----------
        params : ndarray
            The parameters to use when evaluating the Hessian.

        Returns
        -------
        ndarray
            The hessian evaluated at the parameters.
        """
    def predict(self, params: ArrayLike, start: int | str | datetime.datetime | pd.Timestamp | None = None, end: int | str | datetime.datetime | pd.Timestamp | None = None, dynamic: bool | int = False, exog: ArrayLike2D | None = None, exog_oos: ArrayLike2D | None = None) -> pd.Series:
        """
        In-sample prediction and out-of-sample forecasting.

        Parameters
        ----------
        params : array_like
            The fitted model parameters.
        start : int, str, or datetime, optional
            Zero-indexed observation number at which to start forecasting,
            i.e., the first forecast is start. Can also be a date string to
            parse or a datetime type. Default is the the zeroth observation.
        end : int, str, or datetime, optional
            Zero-indexed observation number at which to end forecasting, i.e.,
            the last forecast is end. Can also be a date string to
            parse or a datetime type. However, if the dates index does not
            have a fixed frequency, end must be an integer index if you
            want out-of-sample prediction. Default is the last observation in
            the sample. Unlike standard python slices, end is inclusive so
            that all the predictions [start, start+1, ..., end-1, end] are
            returned.
        dynamic : {bool, int, str, datetime, Timestamp}, optional
            Integer offset relative to `start` at which to begin dynamic
            prediction. Prior to this observation, true endogenous values
            will be used for prediction; starting with this observation and
            continuing through the end of prediction, forecasted endogenous
            values will be used instead. Datetime-like objects are not
            interpreted as offsets. They are instead used to find the index
            location of `dynamic` which is then used to to compute the offset.
        exog : array_like
            A replacement exogenous array.  Must have the same shape as the
            exogenous data array used when the model was created.
        exog_oos : array_like
            An array containing out-of-sample values of the exogenous variable.
            Must has the same number of columns as the exog used when the
            model was created, and at least as many rows as the number of
            out-of-sample forecasts.

        Returns
        -------
        predictions : {ndarray, Series}
            Array of out of in-sample predictions and / or out-of-sample
            forecasts.
        """

class AR:
    """
    The AR class has been removed and replaced with AutoReg

    See Also
    --------
    AutoReg
        The replacement for AR that improved deterministic modeling
    """
    def __init__(self, *args, **kwargs) -> None: ...

class ARResults:
    """
    Removed and replaced by AutoRegResults.

    See Also
    --------
    AutoReg
    """
    def __init__(self, *args, **kwargs) -> None: ...

class AutoRegResults(tsa_model.TimeSeriesModelResults):
    """
    Class to hold results from fitting an AutoReg model.

    Parameters
    ----------
    model : AutoReg
        Reference to the model that is fit.
    params : ndarray
        The fitted parameters from the AR Model.
    cov_params : ndarray
        The estimated covariance matrix of the model parameters.
    normalized_cov_params : ndarray
        The array inv(dot(x.T,x)) where x contains the regressors in the
        model.
    scale : float, optional
        An estimate of the scale of the model.
    use_t : bool, optional
        Whether use_t was set in fit
    summary_text : str, optional
        Additional text to append to results summary
    """
    cov_params_default: Incomplete
    def __init__(self, model, params, cov_params, normalized_cov_params: Incomplete | None = None, scale: float = 1.0, use_t: bool = False, summary_text: str = '') -> None: ...
    model: Incomplete
    def initialize(self, model, params, **kwargs) -> None:
        """
        Initialize (possibly re-initialize) a Results instance.

        Parameters
        ----------
        model : Model
            The model instance.
        params : ndarray
            The model parameters.
        **kwargs
            Any additional keyword arguments required to initialize the model.
        """
    @property
    def ar_lags(self):
        """The autoregressive lags included in the model"""
    @property
    def params(self):
        """The estimated parameters."""
    @property
    def df_model(self):
        """The degrees of freedom consumed by the model."""
    @property
    def df_resid(self):
        """The remaining degrees of freedom in the residuals."""
    @property
    def nobs(self):
        """
        The number of observations after adjusting for losses due to lags.
        """
    def sigma2(self): ...
    def scale(self): ...
    def bse(self):
        """
        The standard errors of the estimated parameters.

        If `method` is 'cmle', then the standard errors that are returned are
        the OLS standard errors of the coefficients. If the `method` is 'mle'
        then they are computed using the numerical Hessian.
        """
    def aic(self):
        """
        Akaike Information Criterion using Lutkepohl's definition.

        :math:`-2 llf + \\ln(nobs) (1 + df_{model})`
        """
    def hqic(self):
        """
        Hannan-Quinn Information Criterion using Lutkepohl's definition.

        :math:`-2 llf + 2 \\ln(\\ln(nobs)) (1 + df_{model})`
        """
    def fpe(self):
        """
        Final prediction error using Lütkepohl's definition.

        :math:`((nobs+df_{model})/(nobs-df_{model})) \\sigma^2`
        """
    def aicc(self):
        """
        Akaike Information Criterion with small sample correction

        :math:`2.0 * df_{model} * nobs / (nobs - df_{model} - 1.0)`
        """
    def bic(self):
        """
        Bayes Information Criterion

        :math:`-2 llf + \\ln(nobs) (1 + df_{model})`
        """
    def resid(self):
        """
        The residuals of the model.
        """
    def roots(self):
        """
        The roots of the AR process.

        The roots are the solution to
        (1 - arparams[0]*z - arparams[1]*z**2 -...- arparams[p-1]*z**k_ar) = 0.
        Stability requires that the roots in modulus lie outside the unit
        circle.
        """
    def arfreq(self):
        """
        Returns the frequency of the AR roots.

        This is the solution, x, to z = abs(z)*exp(2j*np.pi*x) where z are the
        roots.
        """
    def fittedvalues(self):
        """
        The in-sample predicted values of the fitted AR model.

        The `k_ar` initial values are computed via the Kalman Filter if the
        model is fit by `mle`.
        """
    def test_serial_correlation(self, lags: Incomplete | None = None, model_df: Incomplete | None = None):
        """
        Ljung-Box test for residual serial correlation

        Parameters
        ----------
        lags : int
            The maximum number of lags to use in the test. Jointly tests that
            all autocorrelations up to and including lag j are zero for
            j = 1, 2, ..., lags. If None, uses min(10, nobs // 5).
        model_df : int
            The model degree of freedom to use when adjusting computing the
            test statistic to account for parameter estimation. If None, uses
            the number of AR lags included in the model.

        Returns
        -------
        output : DataFrame
            DataFrame containing three columns: the test statistic, the
            p-value of the test, and the degree of freedom used in the test.

        Notes
        -----
        Null hypothesis is no serial correlation.

        The the test degree-of-freedom is 0 or negative once accounting for
        model_df, then the test statistic's p-value is missing.

        See Also
        --------
        statsmodels.stats.diagnostic.acorr_ljungbox
            Ljung-Box test for serial correlation.
        """
    def test_normality(self):
        """
        Test for normality of standardized residuals.

        Returns
        -------
        Series
            Series containing four values, the test statistic and its p-value,
            the skewness and the kurtosis.

        Notes
        -----
        Null hypothesis is normality.

        See Also
        --------
        statsmodels.stats.stattools.jarque_bera
            The Jarque-Bera test of normality.
        """
    def test_heteroskedasticity(self, lags: Incomplete | None = None):
        """
        ARCH-LM test of residual heteroskedasticity

        Parameters
        ----------
        lags : int
            The maximum number of lags to use in the test. Jointly tests that
            all squared autocorrelations up to and including lag j are zero for
            j = 1, 2, ..., lags. If None, uses lag=12*(nobs/100)^{1/4}.

        Returns
        -------
        Series
            Series containing the test statistic and its p-values.

        See Also
        --------
        statsmodels.stats.diagnostic.het_arch
            ARCH-LM test.
        statsmodels.stats.diagnostic.acorr_lm
            LM test for autocorrelation.
        """
    def diagnostic_summary(self):
        """
        Returns a summary containing standard model diagnostic tests

        Returns
        -------
        Summary
            A summary instance with panels for serial correlation tests,
            normality tests and heteroskedasticity tests.

        See Also
        --------
        test_serial_correlation
            Test models residuals for serial correlation.
        test_normality
            Test models residuals for deviations from normality.
        test_heteroskedasticity
            Test models residuals for conditional heteroskedasticity.
        """
    def predict(self, start: Incomplete | None = None, end: Incomplete | None = None, dynamic: bool = False, exog: Incomplete | None = None, exog_oos: Incomplete | None = None): ...
    def get_prediction(self, start: Incomplete | None = None, end: Incomplete | None = None, dynamic: bool = False, exog: Incomplete | None = None, exog_oos: Incomplete | None = None):
        """
        Predictions and prediction intervals

        Parameters
        ----------
        start : int, str, or datetime, optional
            Zero-indexed observation number at which to start forecasting,
            i.e., the first forecast is start. Can also be a date string to
            parse or a datetime type. Default is the the zeroth observation.
        end : int, str, or datetime, optional
            Zero-indexed observation number at which to end forecasting, i.e.,
            the last forecast is end. Can also be a date string to
            parse or a datetime type. However, if the dates index does not
            have a fixed frequency, end must be an integer index if you
            want out-of-sample prediction. Default is the last observation in
            the sample. Unlike standard python slices, end is inclusive so
            that all the predictions [start, start+1, ..., end-1, end] are
            returned.
        dynamic : {bool, int, str, datetime, Timestamp}, optional
            Integer offset relative to `start` at which to begin dynamic
            prediction. Prior to this observation, true endogenous values
            will be used for prediction; starting with this observation and
            continuing through the end of prediction, forecasted endogenous
            values will be used instead. Datetime-like objects are not
            interpreted as offsets. They are instead used to find the index
            location of `dynamic` which is then used to to compute the offset.
        exog : array_like
            A replacement exogenous array.  Must have the same shape as the
            exogenous data array used when the model was created.
        exog_oos : array_like
            An array containing out-of-sample values of the exogenous variable.
            Must has the same number of columns as the exog used when the
            model was created, and at least as many rows as the number of
            out-of-sample forecasts.

        Returns
        -------
        PredictionResults
            Prediction results with mean and prediction intervals
        """
    def forecast(self, steps: int = 1, exog: Incomplete | None = None):
        """
        Out-of-sample forecasts

        Parameters
        ----------
        steps : {int, str, datetime}, default 1
            If an integer, the number of steps to forecast from the end of the
            sample. Can also be a date string to parse or a datetime type.
            However, if the dates index does not have a fixed frequency,
            steps must be an integer.
        exog : {ndarray, DataFrame}
            Exogenous values to use out-of-sample. Must have same number of
            columns as original exog data and at least `steps` rows

        Returns
        -------
        array_like
            Array of out of in-sample predictions and / or out-of-sample
            forecasts.

        See Also
        --------
        AutoRegResults.predict
            In- and out-of-sample predictions
        AutoRegResults.get_prediction
            In- and out-of-sample predictions and confidence intervals
        """
    def plot_predict(self, start: Incomplete | None = None, end: Incomplete | None = None, dynamic: bool = False, exog: Incomplete | None = None, exog_oos: Incomplete | None = None, alpha: float = 0.05, in_sample: bool = True, fig: Incomplete | None = None, figsize: Incomplete | None = None):
        """
        Plot in- and out-of-sample predictions

        Parameters
        ----------
%(predict_params)s
        alpha : {float, None}
            The tail probability not covered by the confidence interval. Must
            be in (0, 1). Confidence interval is constructed assuming normally
            distributed shocks. If None, figure will not show the confidence
            interval.
        in_sample : bool
            Flag indicating whether to include the in-sample period in the
            plot.
        fig : Figure
            An existing figure handle. If not provided, a new figure is
            created.
        figsize: tuple[float, float]
            Tuple containing the figure size values.

        Returns
        -------
        Figure
            Figure handle containing the plot.
        """
    def plot_diagnostics(self, lags: int = 10, fig: Incomplete | None = None, figsize: Incomplete | None = None):
        """
        Diagnostic plots for standardized residuals

        Parameters
        ----------
        lags : int, optional
            Number of lags to include in the correlogram. Default is 10.
        fig : Figure, optional
            If given, subplots are created in this figure instead of in a new
            figure. Note that the 2x2 grid will be created in the provided
            figure using `fig.add_subplot()`.
        figsize : tuple, optional
            If a figure is created, this argument allows specifying a size.
            The tuple is (width, height).

        Notes
        -----
        Produces a 2x2 plot grid with the following plots (ordered clockwise
        from top left):

        1. Standardized residuals over time
        2. Histogram plus estimated density of standardized residuals, along
           with a Normal(0,1) density plotted for reference.
        3. Normal Q-Q plot, with Normal reference line.
        4. Correlogram

        See Also
        --------
        statsmodels.graphics.gofplots.qqplot
        statsmodels.graphics.tsaplots.plot_acf
        """
    def summary(self, alpha: float = 0.05):
        """
        Summarize the Model

        Parameters
        ----------
        alpha : float, optional
            Significance level for the confidence intervals.

        Returns
        -------
        smry : Summary instance
            This holds the summary table and text, which can be printed or
            converted to various output formats.

        See Also
        --------
        statsmodels.iolib.summary.Summary
        """
    def apply(self, endog, exog: Incomplete | None = None, refit: bool = False, fit_kwargs: Incomplete | None = None):
        '''
        Apply the fitted parameters to new data unrelated to the original data

        Creates a new result object using the current fitted parameters,
        applied to a completely new dataset that is assumed to be unrelated to
        the model\'s original data. The new results can then be used for
        analysis or forecasting.

        Parameters
        ----------
        endog : array_like
            New observations from the modeled time-series process.
        exog : array_like, optional
            New observations of exogenous regressors, if applicable.
        refit : bool, optional
            Whether to re-fit the parameters, using the new dataset.
            Default is False (so parameters from the current results object
            are used to create the new results object).
        fit_kwargs : dict, optional
            Keyword arguments to pass to `fit` (if `refit=True`).

        Returns
        -------
        AutoRegResults
            Updated results object containing results for the new dataset.

        See Also
        --------
        AutoRegResults.append
        statsmodels.tsa.statespace.mlemodel.MLEResults.apply

        Notes
        -----
        The `endog` argument to this method should consist of new observations
        that are not necessarily related to the original model\'s `endog`
        dataset.

        Care is needed when using deterministic processes with cyclical
        components such as seasonal dummies or Fourier series. These
        deterministic components will align to the first observation
        in the data and so it is essential that any new data have the
        same initial period.

        Examples
        --------
        >>> import pandas as pd
        >>> from statsmodels.tsa.ar_model import AutoReg
        >>> index = pd.period_range(start=\'2000\', periods=3, freq=\'A\')
        >>> original_observations = pd.Series([1.2, 1.5, 1.8], index=index)
        >>> mod = AutoReg(original_observations, lags=1, trend="n")
        >>> res = mod.fit()
        >>> print(res.params)
        y.L1    1.219512
        dtype: float64
        >>> print(res.fittedvalues)
        2001    1.463415
        2002    1.829268
        Freq: A-DEC, dtype: float64
        >>> print(res.forecast(1))
        2003    2.195122
        Freq: A-DEC, dtype: float64

        >>> new_index = pd.period_range(start=\'1980\', periods=3, freq=\'A\')
        >>> new_observations = pd.Series([1.4, 0.3, 1.2], index=new_index)
        >>> new_res = res.apply(new_observations)
        >>> print(new_res.params)
        y.L1    1.219512
        dtype: float64
        >>> print(new_res.fittedvalues)
        1981    1.707317
        1982    0.365854
        Freq: A-DEC, dtype: float64
        >>> print(new_res.forecast(1))
        1983    1.463415
        Freq: A-DEC, dtype: float64
        '''
    def append(self, endog, exog: Incomplete | None = None, refit: bool = False, fit_kwargs: Incomplete | None = None):
        '''
        Append observations to the ones used to fit the model

        Creates a new result object using the current fitted parameters
        where additional observations are appended to the data used
        to fit the model. The new results can then be used for
        analysis or forecasting.

        Parameters
        ----------
        endog : array_like
            New observations from the modeled time-series process.
        exog : array_like, optional
            New observations of exogenous regressors, if applicable.
        refit : bool, optional
            Whether to re-fit the parameters, using the new dataset.
            Default is False (so parameters from the current results object
            are used to create the new results object).
        fit_kwargs : dict, optional
            Keyword arguments to pass to `fit` (if `refit=True`).

        Returns
        -------
        AutoRegResults
            Updated results object containing results for the new dataset.

        See Also
        --------
        AutoRegResults.apply
        statsmodels.tsa.statespace.mlemodel.MLEResults.append

        Notes
        -----
        The endog and exog arguments to this method must be formatted in the
        same way (e.g. Pandas Series versus Numpy array) as were the endog
        and exog arrays passed to the original model.

        The endog argument to this method should consist of new observations
        that occurred directly after the last element of endog. For any other
        kind of dataset, see the apply method.

        Examples
        --------
        >>> import pandas as pd
        >>> from statsmodels.tsa.ar_model import AutoReg
        >>> index = pd.period_range(start=\'2000\', periods=3, freq=\'A\')
        >>> original_observations = pd.Series([1.2, 1.4, 1.8], index=index)
        >>> mod = AutoReg(original_observations, lags=1, trend="n")
        >>> res = mod.fit()
        >>> print(res.params)
        y.L1    1.235294
        dtype: float64
        >>> print(res.fittedvalues)
        2001    1.482353
        2002    1.729412
        Freq: A-DEC, dtype: float64
        >>> print(res.forecast(1))
        2003    2.223529
        Freq: A-DEC, dtype: float64

        >>> new_index = pd.period_range(start=\'2003\', periods=3, freq=\'A\')
        >>> new_observations = pd.Series([2.1, 2.4, 2.7], index=new_index)
        >>> updated_res = res.append(new_observations)
        >>> print(updated_res.params)
        y.L1    1.235294
        dtype: float64
        >>> print(updated_res.fittedvalues)
        dtype: float64
        2001    1.482353
        2002    1.729412
        2003    2.223529
        2004    2.594118
        2005    2.964706
        Freq: A-DEC, dtype: float64
        >>> print(updated_res.forecast(1))
        2006    3.335294
        Freq: A-DEC, dtype: float64
        '''

class AutoRegResultsWrapper(wrap.ResultsWrapper): ...

class AROrderSelectionResults:
    """
    Results from an AR order selection

    Contains the information criteria for all fitted model orders.
    """
    def __init__(self, model: AutoReg, ics: list[tuple[int | tuple[int, ...], tuple[float, float, float]]], trend: Literal['n', 'c', 'ct', 'ctt'], seasonal: bool, period: int | None) -> None: ...
    @property
    def model(self) -> AutoReg:
        """The model selected using the chosen information criterion."""
    @property
    def seasonal(self) -> bool:
        """Flag indicating if a seasonal component is included."""
    @property
    def trend(self) -> Literal['n', 'c', 'ct', 'ctt']:
        """The trend included in the model selection."""
    @property
    def period(self) -> int | None:
        """The period of the seasonal component."""
    @property
    def aic(self) -> dict[int | tuple[int, ...], float]:
        """
        The Akaike information criterion for the models fit.

        Returns
        -------
        dict[tuple, float]
        """
    @property
    def bic(self) -> dict[int | tuple[int, ...], float]:
        """
        The Bayesian (Schwarz) information criteria for the models fit.

        Returns
        -------
        dict[tuple, float]
        """
    @property
    def hqic(self) -> dict[int | tuple[int, ...], float]:
        """
        The Hannan-Quinn information criteria for the models fit.

        Returns
        -------
        dict[tuple, float]
        """
    @property
    def ar_lags(self) -> list[int] | None:
        """The lags included in the selected model."""
