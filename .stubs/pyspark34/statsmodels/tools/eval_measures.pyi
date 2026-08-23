from statsmodels.tools.validation import array_like as array_like

def mse(x1, x2, axis: int = 0):
    """mean squared error

    Parameters
    ----------
    x1, x2 : array_like
       The performance measure depends on the difference between these two
       arrays.
    axis : int
       axis along which the summary statistic is calculated

    Returns
    -------
    mse : ndarray or float
       mean squared error along given axis.

    Notes
    -----
    If ``x1`` and ``x2`` have different shapes, then they need to broadcast.
    This uses ``numpy.asanyarray`` to convert the input. Whether this is the
    desired result or not depends on the array subclass, for example
    numpy matrices will silently produce an incorrect result.
    """
def rmse(x1, x2, axis: int = 0):
    """root mean squared error

    Parameters
    ----------
    x1, x2 : array_like
       The performance measure depends on the difference between these two
       arrays.
    axis : int
       axis along which the summary statistic is calculated

    Returns
    -------
    rmse : ndarray or float
       root mean squared error along given axis.

    Notes
    -----
    If ``x1`` and ``x2`` have different shapes, then they need to broadcast.
    This uses ``numpy.asanyarray`` to convert the input. Whether this is the
    desired result or not depends on the array subclass, for example
    numpy matrices will silently produce an incorrect result.
    """
def rmspe(y, y_hat, axis: int = 0, zeros=...):
    """
    Root Mean Squared Percentage Error

    Parameters
    ----------
    y : array_like
      The actual value.
    y_hat : array_like
       The predicted value.
    axis : int
       Axis along which the summary statistic is calculated
    zeros : float
       Value to assign to error where y is zero

    Returns
    -------
    rmspe : ndarray or float
       Root Mean Squared Percentage Error along given axis.
    """
def maxabs(x1, x2, axis: int = 0):
    """maximum absolute error

    Parameters
    ----------
    x1, x2 : array_like
       The performance measure depends on the difference between these two
       arrays.
    axis : int
       axis along which the summary statistic is calculated

    Returns
    -------
    maxabs : ndarray or float
       maximum absolute difference along given axis.

    Notes
    -----
    If ``x1`` and ``x2`` have different shapes, then they need to broadcast.
    This uses ``numpy.asanyarray`` to convert the input. Whether this is the
    desired result or not depends on the array subclass.
    """
def meanabs(x1, x2, axis: int = 0):
    """mean absolute error

    Parameters
    ----------
    x1, x2 : array_like
       The performance measure depends on the difference between these two
       arrays.
    axis : int
       axis along which the summary statistic is calculated

    Returns
    -------
    meanabs : ndarray or float
       mean absolute difference along given axis.

    Notes
    -----
    If ``x1`` and ``x2`` have different shapes, then they need to broadcast.
    This uses ``numpy.asanyarray`` to convert the input. Whether this is the
    desired result or not depends on the array subclass.
    """
def medianabs(x1, x2, axis: int = 0):
    """median absolute error

    Parameters
    ----------
    x1, x2 : array_like
       The performance measure depends on the difference between these two
       arrays.
    axis : int
       axis along which the summary statistic is calculated

    Returns
    -------
    medianabs : ndarray or float
       median absolute difference along given axis.

    Notes
    -----
    If ``x1`` and ``x2`` have different shapes, then they need to broadcast.
    This uses ``numpy.asanyarray`` to convert the input. Whether this is the
    desired result or not depends on the array subclass.
    """
def bias(x1, x2, axis: int = 0):
    """bias, mean error

    Parameters
    ----------
    x1, x2 : array_like
       The performance measure depends on the difference between these two
       arrays.
    axis : int
       axis along which the summary statistic is calculated

    Returns
    -------
    bias : ndarray or float
       bias, or mean difference along given axis.

    Notes
    -----
    If ``x1`` and ``x2`` have different shapes, then they need to broadcast.
    This uses ``numpy.asanyarray`` to convert the input. Whether this is the
    desired result or not depends on the array subclass.
    """
def medianbias(x1, x2, axis: int = 0):
    """median bias, median error

    Parameters
    ----------
    x1, x2 : array_like
       The performance measure depends on the difference between these two
       arrays.
    axis : int
       axis along which the summary statistic is calculated

    Returns
    -------
    medianbias : ndarray or float
       median bias, or median difference along given axis.

    Notes
    -----
    If ``x1`` and ``x2`` have different shapes, then they need to broadcast.
    This uses ``numpy.asanyarray`` to convert the input. Whether this is the
    desired result or not depends on the array subclass.
    """
def vare(x1, x2, ddof: int = 0, axis: int = 0):
    """variance of error

    Parameters
    ----------
    x1, x2 : array_like
       The performance measure depends on the difference between these two
       arrays.
    axis : int
       axis along which the summary statistic is calculated

    Returns
    -------
    vare : ndarray or float
       variance of difference along given axis.

    Notes
    -----
    If ``x1`` and ``x2`` have different shapes, then they need to broadcast.
    This uses ``numpy.asanyarray`` to convert the input. Whether this is the
    desired result or not depends on the array subclass.
    """
def stde(x1, x2, ddof: int = 0, axis: int = 0):
    """standard deviation of error

    Parameters
    ----------
    x1, x2 : array_like
       The performance measure depends on the difference between these two
       arrays.
    axis : int
       axis along which the summary statistic is calculated

    Returns
    -------
    stde : ndarray or float
       standard deviation of difference along given axis.

    Notes
    -----
    If ``x1`` and ``x2`` have different shapes, then they need to broadcast.
    This uses ``numpy.asanyarray`` to convert the input. Whether this is the
    desired result or not depends on the array subclass.
    """
def iqr(x1, x2, axis: int = 0):
    """
    Interquartile range of error

    Parameters
    ----------
    x1 : array_like
       One of the inputs into the IQR calculation.
    x2 : array_like
       The other input into the IQR calculation.
    axis : {None, int}
       axis along which the summary statistic is calculated

    Returns
    -------
    irq : {float, ndarray}
       Interquartile range along given axis.

    Notes
    -----
    If ``x1`` and ``x2`` have different shapes, then they must broadcast.
    """
def aic(llf, nobs, df_modelwc):
    """
    Akaike information criterion

    Parameters
    ----------
    llf : {float, array_like}
        value of the loglikelihood
    nobs : int
        number of observations
    df_modelwc : int
        number of parameters including constant

    Returns
    -------
    aic : float
        information criterion

    References
    ----------
    https://en.wikipedia.org/wiki/Akaike_information_criterion
    """
def aicc(llf, nobs, df_modelwc):
    """
    Akaike information criterion (AIC) with small sample correction

    Parameters
    ----------
    llf : {float, array_like}
        value of the loglikelihood
    nobs : int
        number of observations
    df_modelwc : int
        number of parameters including constant

    Returns
    -------
    aicc : float
        information criterion

    References
    ----------
    https://en.wikipedia.org/wiki/Akaike_information_criterion#AICc

    Notes
    -----
    Returns +inf if the effective degrees of freedom, defined as
    ``nobs - df_modelwc - 1.0``, is <= 0.
    """
def bic(llf, nobs, df_modelwc):
    """
    Bayesian information criterion (BIC) or Schwarz criterion

    Parameters
    ----------
    llf : {float, array_like}
        value of the loglikelihood
    nobs : int
        number of observations
    df_modelwc : int
        number of parameters including constant

    Returns
    -------
    bic : float
        information criterion

    References
    ----------
    https://en.wikipedia.org/wiki/Bayesian_information_criterion
    """
def hqic(llf, nobs, df_modelwc):
    """
    Hannan-Quinn information criterion (HQC)

    Parameters
    ----------
    llf : {float, array_like}
        value of the loglikelihood
    nobs : int
        number of observations
    df_modelwc : int
        number of parameters including constant

    Returns
    -------
    hqic : float
        information criterion

    References
    ----------
    Wikipedia does not say much
    """
def aic_sigma(sigma2, nobs, df_modelwc, islog: bool = False):
    """
    Akaike information criterion

    Parameters
    ----------
    sigma2 : float
        estimate of the residual variance or determinant of Sigma_hat in the
        multivariate case. If islog is true, then it is assumed that sigma
        is already log-ed, for example logdetSigma.
    nobs : int
        number of observations
    df_modelwc : int
        number of parameters including constant

    Returns
    -------
    aic : float
        information criterion

    Notes
    -----
    A constant has been dropped in comparison to the loglikelihood base
    information criteria. The information criteria should be used to compare
    only comparable models.

    For example, AIC is defined in terms of the loglikelihood as

    :math:`-2 llf + 2 k`

    in terms of :math:`\\hat{\\sigma}^2`

    :math:`log(\\hat{\\sigma}^2) + 2 k / n`

    in terms of the determinant of :math:`\\hat{\\Sigma}`

    :math:`log(\\|\\hat{\\Sigma}\\|) + 2 k / n`

    Note: In our definition we do not divide by n in the log-likelihood
    version.

    TODO: Latex math

    reference for example lecture notes by Herman Bierens

    See Also
    --------

    References
    ----------
    https://en.wikipedia.org/wiki/Akaike_information_criterion
    """
def aicc_sigma(sigma2, nobs, df_modelwc, islog: bool = False):
    """
    Akaike information criterion (AIC) with small sample correction

    Parameters
    ----------
    sigma2 : float
        estimate of the residual variance or determinant of Sigma_hat in the
        multivariate case. If islog is true, then it is assumed that sigma
        is already log-ed, for example logdetSigma.
    nobs : int
        number of observations
    df_modelwc : int
        number of parameters including constant

    Returns
    -------
    aicc : float
        information criterion

    Notes
    -----
    A constant has been dropped in comparison to the loglikelihood base
    information criteria. These should be used to compare for comparable
    models.

    References
    ----------
    https://en.wikipedia.org/wiki/Akaike_information_criterion#AICc
    """
def bic_sigma(sigma2, nobs, df_modelwc, islog: bool = False):
    """Bayesian information criterion (BIC) or Schwarz criterion

    Parameters
    ----------
    sigma2 : float
        estimate of the residual variance or determinant of Sigma_hat in the
        multivariate case. If islog is true, then it is assumed that sigma
        is already log-ed, for example logdetSigma.
    nobs : int
        number of observations
    df_modelwc : int
        number of parameters including constant

    Returns
    -------
    bic : float
        information criterion

    Notes
    -----
    A constant has been dropped in comparison to the loglikelihood base
    information criteria. These should be used to compare for comparable
    models.

    References
    ----------
    https://en.wikipedia.org/wiki/Bayesian_information_criterion
    """
def hqic_sigma(sigma2, nobs, df_modelwc, islog: bool = False):
    """Hannan-Quinn information criterion (HQC)

    Parameters
    ----------
    sigma2 : float
        estimate of the residual variance or determinant of Sigma_hat in the
        multivariate case. If islog is true, then it is assumed that sigma
        is already log-ed, for example logdetSigma.
    nobs : int
        number of observations
    df_modelwc : int
        number of parameters including constant

    Returns
    -------
    hqic : float
        information criterion

    Notes
    -----
    A constant has been dropped in comparison to the loglikelihood base
    information criteria. These should be used to compare for comparable
    models.

    References
    ----------
    xxx
    """
