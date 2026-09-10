from _typeshed import Incomplete
from statsmodels.compat.python import Literal
from statsmodels.tsa._bds import bds as bds
from statsmodels.tsa._innovations import innovations_algo as innovations_algo, innovations_filter as innovations_filter
from typing import Tuple

__all__ = ['acovf', 'acf', 'pacf', 'pacf_yw', 'pacf_ols', 'ccovf', 'ccf', 'q_stat', 'coint', 'arma_order_select_ic', 'adfuller', 'kpss', 'bds', 'pacf_burg', 'innovations_algo', 'innovations_filter', 'levinson_durbin_pacf', 'levinson_durbin', 'zivot_andrews', 'range_unit_root_test']

def adfuller(x, maxlag: int | None = None, regression: str = 'c', autolag: str = 'AIC', store: bool = False, regresults: bool = False):
    '''
    Augmented Dickey-Fuller unit root test.

    The Augmented Dickey-Fuller test can be used to test for a unit root in a
    univariate process in the presence of serial correlation.

    Parameters
    ----------
    x : array_like, 1d
        The data series to test.
    maxlag : {None, int}
        Maximum lag which is included in test, default value of
        12*(nobs/100)^{1/4} is used when ``None``.
    regression : {"c","ct","ctt","n"}
        Constant and trend order to include in regression.

        * "c" : constant only (default).
        * "ct" : constant and trend.
        * "ctt" : constant, and linear and quadratic trend.
        * "n" : no constant, no trend.

    autolag : {"AIC", "BIC", "t-stat", None}
        Method to use when automatically determining the lag length among the
        values 0, 1, ..., maxlag.

        * If "AIC" (default) or "BIC", then the number of lags is chosen
          to minimize the corresponding information criterion.
        * "t-stat" based choice of maxlag.  Starts with maxlag and drops a
          lag until the t-statistic on the last lag length is significant
          using a 5%-sized test.
        * If None, then the number of included lags is set to maxlag.
    store : bool
        If True, then a result instance is returned additionally to
        the adf statistic. Default is False.
    regresults : bool, optional
        If True, the full regression results are returned. Default is False.

    Returns
    -------
    adf : float
        The test statistic.
    pvalue : float
        MacKinnon\'s approximate p-value based on MacKinnon (1994, 2010).
    usedlag : int
        The number of lags used.
    nobs : int
        The number of observations used for the ADF regression and calculation
        of the critical values.
    critical values : dict
        Critical values for the test statistic at the 1 %, 5 %, and 10 %
        levels. Based on MacKinnon (2010).
    icbest : float
        The maximized information criterion if autolag is not None.
    resstore : ResultStore, optional
        A dummy class with results attached as attributes.

    Notes
    -----
    The null hypothesis of the Augmented Dickey-Fuller is that there is a unit
    root, with the alternative that there is no unit root. If the pvalue is
    above a critical size, then we cannot reject that there is a unit root.

    The p-values are obtained through regression surface approximation from
    MacKinnon 1994, but using the updated 2010 tables. If the p-value is close
    to significant, then the critical values should be used to judge whether
    to reject the null.

    The autolag option and maxlag for it are described in Greene.

    See the notebook `Stationarity and detrending (ADF/KPSS)
    <../examples/notebooks/generated/stationarity_detrending_adf_kpss.html>`__
    for an overview.

    References
    ----------
    .. [1] W. Green.  "Econometric Analysis," 5th ed., Pearson, 2003.

    .. [2] Hamilton, J.D.  "Time Series Analysis".  Princeton, 1994.

    .. [3] MacKinnon, J.G. 1994.  "Approximate asymptotic distribution functions for
        unit-root and cointegration tests.  `Journal of Business and Economic
        Statistics` 12, 167-76.

    .. [4] MacKinnon, J.G. 2010. "Critical Values for Cointegration Tests."  Queen"s
        University, Dept of Economics, Working Papers.  Available at
        http://ideas.repec.org/p/qed/wpaper/1227.html
    '''
def acovf(x, adjusted: bool = False, demean: bool = True, fft: bool = True, missing: str = 'none', nlag: Incomplete | None = None):
    '''
    Estimate autocovariances.

    Parameters
    ----------
    x : array_like
        Time series data. Must be 1d.
    adjusted : bool, default False
        If True, then denominators is n-k, otherwise n.
    demean : bool, default True
        If True, then subtract the mean x from each element of x.
    fft : bool, default True
        If True, use FFT convolution.  This method should be preferred
        for long time series.
    missing : str, default "none"
        A string in ["none", "raise", "conservative", "drop"] specifying how
        the NaNs are to be treated. "none" performs no checks. "raise" raises
        an exception if NaN values are found. "drop" removes the missing
        observations and then estimates the autocovariances treating the
        non-missing as contiguous. "conservative" computes the autocovariance
        using nan-ops so that nans are removed when computing the mean
        and cross-products that are used to estimate the autocovariance.
        When using "conservative", n is set to the number of non-missing
        observations.
    nlag : {int, None}, default None
        Limit the number of autocovariances returned.  Size of returned
        array is nlag + 1.  Setting nlag when fft is False uses a simple,
        direct estimator of the autocovariances that only computes the first
        nlag + 1 values. This can be much faster when the time series is long
        and only a small number of autocovariances are needed.

    Returns
    -------
    ndarray
        The estimated autocovariances.

    References
    ----------
    .. [1] Parzen, E., 1963. On spectral analysis with missing observations
           and amplitude modulation. Sankhya: The Indian Journal of
           Statistics, Series A, pp.383-392.
    '''
def q_stat(x, nobs):
    """
    Compute Ljung-Box Q Statistic.

    Parameters
    ----------
    x : array_like
        Array of autocorrelation coefficients.  Can be obtained from acf.
    nobs : int, optional
        Number of observations in the entire sample (ie., not just the length
        of the autocorrelation function results.

    Returns
    -------
    q-stat : ndarray
        Ljung-Box Q-statistic for autocorrelation parameters.
    p-value : ndarray
        P-value of the Q statistic.

    See Also
    --------
    statsmodels.stats.diagnostic.acorr_ljungbox
        Ljung-Box Q-test for autocorrelation in time series based
        on a time series rather than the estimated autocorrelation
        function.

    Notes
    -----
    Designed to be used with acf.
    """
def acf(x, adjusted: bool = False, nlags: Incomplete | None = None, qstat: bool = False, fft: bool = True, alpha: Incomplete | None = None, bartlett_confint: bool = True, missing: str = 'none'):
    '''
    Calculate the autocorrelation function.

    Parameters
    ----------
    x : array_like
       The time series data.
    adjusted : bool, default False
       If True, then denominators for autocovariance are n-k, otherwise n.
    nlags : int, optional
        Number of lags to return autocorrelation for. If not provided,
        uses min(10 * np.log10(nobs), nobs - 1). The returned value
        includes lag 0 (ie., 1) so size of the acf vector is (nlags + 1,).
    qstat : bool, default False
        If True, returns the Ljung-Box q statistic for each autocorrelation
        coefficient.  See q_stat for more information.
    fft : bool, default True
        If True, computes the ACF via FFT.
    alpha : scalar, default None
        If a number is given, the confidence intervals for the given level are
        returned. For instance if alpha=.05, 95 % confidence intervals are
        returned where the standard deviation is computed according to
        Bartlett"s formula.
    bartlett_confint : bool, default True
        Confidence intervals for ACF values are generally placed at 2
        standard errors around r_k. The formula used for standard error
        depends upon the situation. If the autocorrelations are being used
        to test for randomness of residuals as part of the ARIMA routine,
        the standard errors are determined assuming the residuals are white
        noise. The approximate formula for any lag is that standard error
        of each r_k = 1/sqrt(N). See section 9.4 of [2] for more details on
        the 1/sqrt(N) result. For more elementary discussion, see section 5.3.2
        in [3].
        For the ACF of raw data, the standard error at a lag k is
        found as if the right model was an MA(k-1). This allows the possible
        interpretation that if all autocorrelations past a certain lag are
        within the limits, the model might be an MA of order defined by the
        last significant autocorrelation. In this case, a moving average
        model is assumed for the data and the standard errors for the
        confidence intervals should be generated using Bartlett\'s formula.
        For more details on Bartlett formula result, see section 7.2 in [2].
    missing : str, default "none"
        A string in ["none", "raise", "conservative", "drop"] specifying how
        the NaNs are to be treated. "none" performs no checks. "raise" raises
        an exception if NaN values are found. "drop" removes the missing
        observations and then estimates the autocovariances treating the
        non-missing as contiguous. "conservative" computes the autocovariance
        using nan-ops so that nans are removed when computing the mean
        and cross-products that are used to estimate the autocovariance.
        When using "conservative", n is set to the number of non-missing
        observations.

    Returns
    -------
    acf : ndarray
        The autocorrelation function for lags 0, 1, ..., nlags. Shape
        (nlags+1,).
    confint : ndarray, optional
        Confidence intervals for the ACF at lags 0, 1, ..., nlags. Shape
        (nlags + 1, 2). Returned if alpha is not None.
    qstat : ndarray, optional
        The Ljung-Box Q-Statistic for lags 1, 2, ..., nlags (excludes lag
        zero). Returned if q_stat is True.
    pvalues : ndarray, optional
        The p-values associated with the Q-statistics for lags 1, 2, ...,
        nlags (excludes lag zero). Returned if q_stat is True.

    Notes
    -----
    The acf at lag 0 (ie., 1) is returned.

    For very long time series it is recommended to use fft convolution instead.
    When fft is False uses a simple, direct estimator of the autocovariances
    that only computes the first nlag + 1 values. This can be much faster when
    the time series is long and only a small number of autocovariances are
    needed.

    If adjusted is true, the denominator for the autocovariance is adjusted
    for the loss of data.

    References
    ----------
    .. [1] Parzen, E., 1963. On spectral analysis with missing observations
       and amplitude modulation. Sankhya: The Indian Journal of
       Statistics, Series A, pp.383-392.
    .. [2] Brockwell and Davis, 1987. Time Series Theory and Methods
    .. [3] Brockwell and Davis, 2010. Introduction to Time Series and
       Forecasting, 2nd edition.
    '''
def pacf_yw(x, nlags: Incomplete | None = None, method: str = 'adjusted'):
    '''
    Partial autocorrelation estimated with non-recursive yule_walker.

    Parameters
    ----------
    x : array_like
        The observations of time series for which pacf is calculated.
    nlags : int, optional
        Number of lags to return autocorrelation for. If not provided,
        uses min(10 * np.log10(nobs), nobs - 1).
    method : {"adjusted", "mle"}, default "adjusted"
        The method for the autocovariance calculations in yule walker.

    Returns
    -------
    ndarray
        The partial autocorrelations, maxlag+1 elements.

    See Also
    --------
    statsmodels.tsa.stattools.pacf
        Partial autocorrelation estimation.
    statsmodels.tsa.stattools.pacf_ols
        Partial autocorrelation estimation using OLS.
    statsmodels.tsa.stattools.pacf_burg
        Partial autocorrelation estimation using Burg"s method.

    Notes
    -----
    This solves yule_walker for each desired lag and contains
    currently duplicate calculations.
    '''
def pacf_burg(x, nlags: Incomplete | None = None, demean: bool = True):
    '''
    Calculate Burg"s partial autocorrelation estimator.

    Parameters
    ----------
    x : array_like
        Observations of time series for which pacf is calculated.
    nlags : int, optional
        Number of lags to return autocorrelation for. If not provided,
        uses min(10 * np.log10(nobs), nobs - 1).
    demean : bool, optional
        Flag indicating to demean that data. Set to False if x has been
        previously demeaned.

    Returns
    -------
    pacf : ndarray
        Partial autocorrelations for lags 0, 1, ..., nlag.
    sigma2 : ndarray
        Residual variance estimates where the value in position m is the
        residual variance in an AR model that includes m lags.

    See Also
    --------
    statsmodels.tsa.stattools.pacf
        Partial autocorrelation estimation.
    statsmodels.tsa.stattools.pacf_yw
         Partial autocorrelation estimation using Yule-Walker.
    statsmodels.tsa.stattools.pacf_ols
        Partial autocorrelation estimation using OLS.

    References
    ----------
    .. [1] Brockwell, P.J. and Davis, R.A., 2016. Introduction to time series
        and forecasting. Springer.
    '''
def pacf_ols(x, nlags: Incomplete | None = None, efficient: bool = True, adjusted: bool = False):
    '''
    Calculate partial autocorrelations via OLS.

    Parameters
    ----------
    x : array_like
        Observations of time series for which pacf is calculated.
    nlags : int, optional
        Number of lags to return autocorrelation for. If not provided,
        uses min(10 * np.log10(nobs), nobs - 1).
    efficient : bool, optional
        If true, uses the maximum number of available observations to compute
        each partial autocorrelation. If not, uses the same number of
        observations to compute all pacf values.
    adjusted : bool, optional
        Adjust each partial autocorrelation by n / (n - lag).

    Returns
    -------
    ndarray
        The partial autocorrelations, (maxlag,) array corresponding to lags
        0, 1, ..., maxlag.

    See Also
    --------
    statsmodels.tsa.stattools.pacf
        Partial autocorrelation estimation.
    statsmodels.tsa.stattools.pacf_yw
         Partial autocorrelation estimation using Yule-Walker.
    statsmodels.tsa.stattools.pacf_burg
        Partial autocorrelation estimation using Burg"s method.

    Notes
    -----
    This solves a separate OLS estimation for each desired lag using method in
    [1]_. Setting efficient to True has two effects. First, it uses
    `nobs - lag` observations of estimate each pacf.  Second, it re-estimates
    the mean in each regression. If efficient is False, then the data are first
    demeaned, and then `nobs - maxlag` observations are used to estimate each
    partial autocorrelation.

    The inefficient estimator appears to have better finite sample properties.
    This option should only be used in time series that are covariance
    stationary.

    OLS estimation of the pacf does not guarantee that all pacf values are
    between -1 and 1.

    References
    ----------
    .. [1] Box, G. E., Jenkins, G. M., Reinsel, G. C., & Ljung, G. M. (2015).
       Time series analysis: forecasting and control. John Wiley & Sons, p. 66
    '''
def pacf(x, nlags: Incomplete | None = None, method: str = 'ywadjusted', alpha: Incomplete | None = None):
    '''
    Partial autocorrelation estimate.

    Parameters
    ----------
    x : array_like
        Observations of time series for which pacf is calculated.
    nlags : int, optional
        Number of lags to return autocorrelation for. If not provided,
        uses min(10 * np.log10(nobs), nobs // 2 - 1). The returned value
        includes lag 0 (ie., 1) so size of the pacf vector is (nlags + 1,).
    method : str, default "ywunbiased"
        Specifies which method for the calculations to use.

        - "yw" or "ywadjusted" : Yule-Walker with sample-size adjustment in
          denominator for acovf. Default.
        - "ywm" or "ywmle" : Yule-Walker without adjustment.
        - "ols" : regression of time series on lags of it and on constant.
        - "ols-inefficient" : regression of time series on lags using a single
          common sample to estimate all pacf coefficients.
        - "ols-adjusted" : regression of time series on lags with a bias
          adjustment.
        - "ld" or "ldadjusted" : Levinson-Durbin recursion with bias
          correction.
        - "ldb" or "ldbiased" : Levinson-Durbin recursion without bias
          correction.
        - "burg" :  Burg"s partial autocorrelation estimator.

    alpha : float, optional
        If a number is given, the confidence intervals for the given level are
        returned. For instance if alpha=.05, 95 % confidence intervals are
        returned where the standard deviation is computed according to
        1/sqrt(len(x)).

    Returns
    -------
    pacf : ndarray
        The partial autocorrelations for lags 0, 1, ..., nlags. Shape
        (nlags+1,).
    confint : ndarray, optional
        Confidence intervals for the PACF at lags 0, 1, ..., nlags. Shape
        (nlags + 1, 2). Returned if alpha is not None.

    See Also
    --------
    statsmodels.tsa.stattools.acf
        Estimate the autocorrelation function.
    statsmodels.tsa.stattools.pacf
        Partial autocorrelation estimation.
    statsmodels.tsa.stattools.pacf_yw
         Partial autocorrelation estimation using Yule-Walker.
    statsmodels.tsa.stattools.pacf_ols
        Partial autocorrelation estimation using OLS.
    statsmodels.tsa.stattools.pacf_burg
        Partial autocorrelation estimation using Burg"s method.

    Notes
    -----
    Based on simulation evidence across a range of low-order ARMA models,
    the best methods based on root MSE are Yule-Walker (MLW), Levinson-Durbin
    (MLE) and Burg, respectively. The estimators with the lowest bias included
    included these three in addition to OLS and OLS-adjusted.

    Yule-Walker (adjusted) and Levinson-Durbin (adjusted) performed
    consistently worse than the other options.
    '''
def ccovf(x, y, adjusted: bool = True, demean: bool = True, fft: bool = True):
    """
    Calculate the crosscovariance between two series.

    Parameters
    ----------
    x, y : array_like
       The time series data to use in the calculation.
    adjusted : bool, optional
       If True, then denominators for crosscovariance is n-k, otherwise n.
    demean : bool, optional
        Flag indicating whether to demean x and y.
    fft : bool, default True
        If True, use FFT convolution.  This method should be preferred
        for long time series.

    Returns
    -------
    ndarray
        The estimated crosscovariance function.
    """
def ccf(x, y, adjusted: bool = True, fft: bool = True):
    """
    The cross-correlation function.

    Parameters
    ----------
    x, y : array_like
        The time series data to use in the calculation.
    adjusted : bool
        If True, then denominators for cross-correlation is n-k, otherwise n.
    fft : bool, default True
        If True, use FFT convolution.  This method should be preferred
        for long time series.

    Returns
    -------
    ndarray
        The cross-correlation function of x and y.

    Notes
    -----
    If adjusted is true, the denominator for the autocovariance is adjusted.
    """
def levinson_durbin(s, nlags: int = 10, isacov: bool = False):
    """
    Levinson-Durbin recursion for autoregressive processes.

    Parameters
    ----------
    s : array_like
        If isacov is False, then this is the time series. If iasacov is true
        then this is interpreted as autocovariance starting with lag 0.
    nlags : int, optional
        The largest lag to include in recursion or order of the autoregressive
        process.
    isacov : bool, optional
        Flag indicating whether the first argument, s, contains the
        autocovariances or the data series.

    Returns
    -------
    sigma_v : float
        The estimate of the error variance.
    arcoefs : ndarray
        The estimate of the autoregressive coefficients for a model including
        nlags.
    pacf : ndarray
        The partial autocorrelation function.
    sigma : ndarray
        The entire sigma array from intermediate result, last value is sigma_v.
    phi : ndarray
        The entire phi array from intermediate result, last column contains
        autoregressive coefficients for AR(nlags).

    Notes
    -----
    This function returns currently all results, but maybe we drop sigma and
    phi from the returns.

    If this function is called with the time series (isacov=False), then the
    sample autocovariance function is calculated with the default options
    (biased, no fft).
    """
def levinson_durbin_pacf(pacf, nlags: Incomplete | None = None):
    """
    Levinson-Durbin algorithm that returns the acf and ar coefficients.

    Parameters
    ----------
    pacf : array_like
        Partial autocorrelation array for lags 0, 1, ... p.
    nlags : int, optional
        Number of lags in the AR model.  If omitted, returns coefficients from
        an AR(p) and the first p autocorrelations.

    Returns
    -------
    arcoefs : ndarray
        AR coefficients computed from the partial autocorrelations.
    acf : ndarray
        The acf computed from the partial autocorrelations. Array returned
        contains the autocorrelations corresponding to lags 0, 1, ..., p.

    References
    ----------
    .. [1] Brockwell, P.J. and Davis, R.A., 2016. Introduction to time series
        and forecasting. Springer.
    """
def coint(y0, y1, trend: str = 'c', method: str = 'aeg', maxlag: Incomplete | None = None, autolag: str | None = 'aic', return_results: Incomplete | None = None):
    '''
    Test for no-cointegration of a univariate equation.

    The null hypothesis is no cointegration. Variables in y0 and y1 are
    assumed to be integrated of order 1, I(1).

    This uses the augmented Engle-Granger two-step cointegration test.
    Constant or trend is included in 1st stage regression, i.e. in
    cointegrating equation.

    **Warning:** The autolag default has changed compared to statsmodels 0.8.
    In 0.8 autolag was always None, no the keyword is used and defaults to
    "aic". Use `autolag=None` to avoid the lag search.

    Parameters
    ----------
    y0 : array_like
        The first element in cointegrated system. Must be 1-d.
    y1 : array_like
        The remaining elements in cointegrated system.
    trend : str {"c", "ct"}
        The trend term included in regression for cointegrating equation.

        * "c" : constant.
        * "ct" : constant and linear trend.
        * also available quadratic trend "ctt", and no constant "n".

    method : {"aeg"}
        Only "aeg" (augmented Engle-Granger) is available.
    maxlag : None or int
        Argument for `adfuller`, largest or given number of lags.
    autolag : str
        Argument for `adfuller`, lag selection criterion.

        * If None, then maxlag lags are used without lag search.
        * If "AIC" (default) or "BIC", then the number of lags is chosen
          to minimize the corresponding information criterion.
        * "t-stat" based choice of maxlag.  Starts with maxlag and drops a
          lag until the t-statistic on the last lag length is significant
          using a 5%-sized test.
    return_results : bool
        For future compatibility, currently only tuple available.
        If True, then a results instance is returned. Otherwise, a tuple
        with the test outcome is returned. Set `return_results=False` to
        avoid future changes in return.

    Returns
    -------
    coint_t : float
        The t-statistic of unit-root test on residuals.
    pvalue : float
        MacKinnon"s approximate, asymptotic p-value based on MacKinnon (1994).
    crit_value : dict
        Critical values for the test statistic at the 1 %, 5 %, and 10 %
        levels based on regression curve. This depends on the number of
        observations.

    Notes
    -----
    The Null hypothesis is that there is no cointegration, the alternative
    hypothesis is that there is cointegrating relationship. If the pvalue is
    small, below a critical size, then we can reject the hypothesis that there
    is no cointegrating relationship.

    P-values and critical values are obtained through regression surface
    approximation from MacKinnon 1994 and 2010.

    If the two series are almost perfectly collinear, then computing the
    test is numerically unstable. However, the two series will be cointegrated
    under the maintained assumption that they are integrated. In this case
    the t-statistic will be set to -inf and the pvalue to zero.

    TODO: We could handle gaps in data by dropping rows with nans in the
    Auxiliary regressions. Not implemented yet, currently assumes no nans
    and no gaps in time series.

    References
    ----------
    .. [1] MacKinnon, J.G. 1994  "Approximate Asymptotic Distribution Functions
       for Unit-Root and Cointegration Tests." Journal of Business & Economics
       Statistics, 12.2, 167-76.
    .. [2] MacKinnon, J.G. 2010.  "Critical Values for Cointegration Tests."
       Queen"s University, Dept of Economics Working Papers 1227.
       http://ideas.repec.org/p/qed/wpaper/1227.html
    '''
def arma_order_select_ic(y, max_ar: int = 4, max_ma: int = 2, ic: str = 'bic', trend: str = 'c', model_kw: Incomplete | None = None, fit_kw: Incomplete | None = None):
    '''
    Compute information criteria for many ARMA models.

    Parameters
    ----------
    y : array_like
        Array of time-series data.
    max_ar : int
        Maximum number of AR lags to use. Default 4.
    max_ma : int
        Maximum number of MA lags to use. Default 2.
    ic : str, list
        Information criteria to report. Either a single string or a list
        of different criteria is possible.
    trend : str
        The trend to use when fitting the ARMA models.
    model_kw : dict
        Keyword arguments to be passed to the ``ARMA`` model.
    fit_kw : dict
        Keyword arguments to be passed to ``ARMA.fit``.

    Returns
    -------
    Bunch
        Dict-like object with attribute access. Each ic is an attribute with a
        DataFrame for the results. The AR order used is the row index. The ma
        order used is the column index. The minimum orders are available as
        ``ic_min_order``.

    Notes
    -----
    This method can be used to tentatively identify the order of an ARMA
    process, provided that the time series is stationary and invertible. This
    function computes the full exact MLE estimate of each model and can be,
    therefore a little slow. An implementation using approximate estimates
    will be provided in the future. In the meantime, consider passing
    {method : "css"} to fit_kw.

    Examples
    --------

    >>> from statsmodels.tsa.arima_process import arma_generate_sample
    >>> import statsmodels.api as sm
    >>> import numpy as np

    >>> arparams = np.array([.75, -.25])
    >>> maparams = np.array([.65, .35])
    >>> arparams = np.r_[1, -arparams]
    >>> maparam = np.r_[1, maparams]
    >>> nobs = 250
    >>> np.random.seed(2014)
    >>> y = arma_generate_sample(arparams, maparams, nobs)
    >>> res = sm.tsa.arma_order_select_ic(y, ic=["aic", "bic"], trend="n")
    >>> res.aic_min_order
    >>> res.bic_min_order
    '''
def kpss(x, regression: Literal['c', 'ct'] = 'c', nlags: Literal['auto', 'legacy'] | int = 'auto', store: bool = False) -> Tuple[float, float, int, dict[str, float]]:
    '''
    Kwiatkowski-Phillips-Schmidt-Shin test for stationarity.

    Computes the Kwiatkowski-Phillips-Schmidt-Shin (KPSS) test for the null
    hypothesis that x is level or trend stationary.

    Parameters
    ----------
    x : array_like, 1d
        The data series to test.
    regression : str{"c", "ct"}
        The null hypothesis for the KPSS test.

        * "c" : The data is stationary around a constant (default).
        * "ct" : The data is stationary around a trend.
    nlags : {str, int}, optional
        Indicates the number of lags to be used. If "auto" (default), lags
        is calculated using the data-dependent method of Hobijn et al. (1998).
        See also Andrews (1991), Newey & West (1994), and Schwert (1989). If
        set to "legacy",  uses int(12 * (n / 100)**(1 / 4)) , as outlined in
        Schwert (1989).
    store : bool
        If True, then a result instance is returned additionally to
        the KPSS statistic (default is False).

    Returns
    -------
    kpss_stat : float
        The KPSS test statistic.
    p_value : float
        The p-value of the test. The p-value is interpolated from
        Table 1 in Kwiatkowski et al. (1992), and a boundary point
        is returned if the test statistic is outside the table of
        critical values, that is, if the p-value is outside the
        interval (0.01, 0.1).
    lags : int
        The truncation lag parameter.
    crit : dict
        The critical values at 10%, 5%, 2.5% and 1%. Based on
        Kwiatkowski et al. (1992).
    resstore : (optional) instance of ResultStore
        An instance of a dummy class with results attached as attributes.

    Notes
    -----
    To estimate sigma^2 the Newey-West estimator is used. If lags is "legacy",
    the truncation lag parameter is set to int(12 * (n / 100) ** (1 / 4)),
    as outlined in Schwert (1989). The p-values are interpolated from
    Table 1 of Kwiatkowski et al. (1992). If the computed statistic is
    outside the table of critical values, then a warning message is
    generated.

    Missing values are not handled.

    See the notebook `Stationarity and detrending (ADF/KPSS)
    <../examples/notebooks/generated/stationarity_detrending_adf_kpss.html>`__
    for an overview.

    References
    ----------
    .. [1] Andrews, D.W.K. (1991). Heteroskedasticity and autocorrelation
       consistent covariance matrix estimation. Econometrica, 59: 817-858.

    .. [2] Hobijn, B., Frances, B.H., & Ooms, M. (2004). Generalizations of the
       KPSS-test for stationarity. Statistica Neerlandica, 52: 483-502.

    .. [3] Kwiatkowski, D., Phillips, P.C.B., Schmidt, P., & Shin, Y. (1992).
       Testing the null hypothesis of stationarity against the alternative of a
       unit root. Journal of Econometrics, 54: 159-178.

    .. [4] Newey, W.K., & West, K.D. (1994). Automatic lag selection in
       covariance matrix estimation. Review of Economic Studies, 61: 631-653.

    .. [5] Schwert, G. W. (1989). Tests for unit roots: A Monte Carlo
       investigation. Journal of Business and Economic Statistics, 7 (2):
       147-159.
    '''
def range_unit_root_test(x, store: bool = False):
    """
    Range unit-root test for stationarity.

    Computes the Range Unit-Root (RUR) test for the null
    hypothesis that x is stationary.

    Parameters
    ----------
    x : array_like, 1d
        The data series to test.
    store : bool
        If True, then a result instance is returned additionally to
        the RUR statistic (default is False).

    Returns
    -------
    rur_stat : float
        The RUR test statistic.
    p_value : float
        The p-value of the test. The p-value is interpolated from
        Table 1 in Aparicio et al. (2006), and a boundary point
        is returned if the test statistic is outside the table of
        critical values, that is, if the p-value is outside the
        interval (0.01, 0.1).
    crit : dict
        The critical values at 10%, 5%, 2.5% and 1%. Based on
        Aparicio et al. (2006).
    resstore : (optional) instance of ResultStore
        An instance of a dummy class with results attached as attributes.

    Notes
    -----
    The p-values are interpolated from
    Table 1 of Aparicio et al. (2006). If the computed statistic is
    outside the table of critical values, then a warning message is
    generated.

    Missing values are not handled.

    References
    ----------
    .. [1] Aparicio, F., Escribano A., Sipols, A.E. (2006). Range Unit-Root (RUR)
        tests: robust against nonlinearities, error distributions, structural breaks
        and outliers. Journal of Time Series Analysis, 27 (4): 545-576.
    """

class ZivotAndrewsUnitRoot:
    """
    Class wrapper for Zivot-Andrews structural-break unit-root test
    """
    def __init__(self) -> None:
        """
        Critical values for the three different models specified for the
        Zivot-Andrews unit-root test.

        Notes
        -----
        The p-values are generated through Monte Carlo simulation using
        100,000 replications and 2000 data points.
        """
    def run(self, x, trim: float = 0.15, maxlag: Incomplete | None = None, regression: str = 'c', autolag: str = 'AIC'):
        '''
        Zivot-Andrews structural-break unit-root test.

        The Zivot-Andrews test tests for a unit root in a univariate process
        in the presence of serial correlation and a single structural break.

        Parameters
        ----------
        x : array_like
            The data series to test.
        trim : float
            The percentage of series at begin/end to exclude from break-period
            calculation in range [0, 0.333] (default=0.15).
        maxlag : int
            The maximum lag which is included in test, default is
            12*(nobs/100)^{1/4} (Schwert, 1989).
        regression : {"c","t","ct"}
            Constant and trend order to include in regression.

            * "c" : constant only (default).
            * "t" : trend only.
            * "ct" : constant and trend.
        autolag : {"AIC", "BIC", "t-stat", None}
            The method to select the lag length when using automatic selection.

            * if None, then maxlag lags are used,
            * if "AIC" (default) or "BIC", then the number of lags is chosen
              to minimize the corresponding information criterion,
            * "t-stat" based choice of maxlag.  Starts with maxlag and drops a
              lag until the t-statistic on the last lag length is significant
              using a 5%-sized test.

        Returns
        -------
        zastat : float
            The test statistic.
        pvalue : float
            The pvalue based on MC-derived critical values.
        cvdict : dict
            The critical values for the test statistic at the 1%, 5%, and 10%
            levels.
        baselag : int
            The number of lags used for period regressions.
        bpidx : int
            The index of x corresponding to endogenously calculated break period
            with values in the range [0..nobs-1].

        Notes
        -----
        H0 = unit root with a single structural break

        Algorithm follows Baum (2004/2015) approximation to original
        Zivot-Andrews method. Rather than performing an autolag regression at
        each candidate break period (as per the original paper), a single
        autolag regression is run up-front on the base model (constant + trend
        with no dummies) to determine the best lag length. This lag length is
        then used for all subsequent break-period regressions. This results in
        significant run time reduction but also slightly more pessimistic test
        statistics than the original Zivot-Andrews method, although no attempt
        has been made to characterize the size/power trade-off.

        References
        ----------
        .. [1] Baum, C.F. (2004). ZANDREWS: Stata module to calculate
           Zivot-Andrews unit root test in presence of structural break,"
           Statistical Software Components S437301, Boston College Department
           of Economics, revised 2015.

        .. [2] Schwert, G.W. (1989). Tests for unit roots: A Monte Carlo
           investigation. Journal of Business & Economic Statistics, 7:
           147-159.

        .. [3] Zivot, E., and Andrews, D.W.K. (1992). Further evidence on the
           great crash, the oil-price shock, and the unit-root hypothesis.
           Journal of Business & Economic Studies, 10: 251-270.
        '''
    def __call__(self, x, trim: float = 0.15, maxlag: Incomplete | None = None, regression: str = 'c', autolag: str = 'AIC'): ...

zivot_andrews: Incomplete
