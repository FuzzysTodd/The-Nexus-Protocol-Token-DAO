def norm_lls(y, params):
    """normal loglikelihood given observations and mean mu and variance sigma2

    Parameters
    ----------
    y : ndarray, 1d
        normally distributed random variable
    params : ndarray, (nobs, 2)
        array of mean, variance (mu, sigma2) with observations in rows

    Returns
    -------
    lls : ndarray
        contribution to loglikelihood for each observation
    """
def norm_lls_grad(y, params):
    """Jacobian of normal loglikelihood wrt mean mu and variance sigma2

    Parameters
    ----------
    y : ndarray, 1d
        normally distributed random variable
    params : ndarray, (nobs, 2)
        array of mean, variance (mu, sigma2) with observations in rows

    Returns
    -------
    grad : array (nobs, 2)
        derivative of loglikelihood for each observation wrt mean in first
        column, and wrt variance in second column

    Notes
    -----
    this is actually the derivative wrt sigma not sigma**2, but evaluated
    with parameter sigma2 = sigma**2

    """
def mean_grad(x, beta):
    """gradient/Jacobian for d (x*beta)/ d beta
    """
def normgrad(y, x, params):
    """Jacobian of normal loglikelihood wrt mean mu and variance sigma2

    Parameters
    ----------
    y : ndarray, 1d
        normally distributed random variable with mean x*beta, and variance sigma2
    x : ndarray, 2d
        explanatory variables, observation in rows, variables in columns
    params : array_like, (nvars + 1)
        array of coefficients and variance (beta, sigma2)

    Returns
    -------
    grad : array (nobs, 2)
        derivative of loglikelihood for each observation wrt mean in first
        column, and wrt scale (sigma) in second column
    assume params = (beta, sigma2)

    Notes
    -----
    TODO: for heteroscedasticity need sigma to be a 1d array

    """
def tstd_lls(y, params, df):
    """t loglikelihood given observations and mean mu and variance sigma2 = 1

    Parameters
    ----------
    y : ndarray, 1d
        normally distributed random variable
    params : ndarray, (nobs, 2)
        array of mean, variance (mu, sigma2) with observations in rows
    df : int
        degrees of freedom of the t distribution

    Returns
    -------
    lls : ndarray
        contribution to loglikelihood for each observation

    Notes
    -----
    parametrized for garch
    """
def norm_dlldy(y):
    """derivative of log pdf of standard normal with respect to y
    """
def tstd_pdf(x, df):
    """pdf for standardized (not standard) t distribution, variance is one

    """
def ts_lls(y, params, df):
    """t loglikelihood given observations and mean mu and variance sigma2 = 1

    Parameters
    ----------
    y : ndarray, 1d
        normally distributed random variable
    params : ndarray, (nobs, 2)
        array of mean, variance (mu, sigma2) with observations in rows
    df : int
        degrees of freedom of the t distribution

    Returns
    -------
    lls : ndarray
        contribution to loglikelihood for each observation

    Notes
    -----
    parametrized for garch
    normalized/rescaled so that sigma2 is the variance

    >>> df = 10; sigma = 1.
    >>> stats.t.stats(df, loc=0., scale=sigma.*np.sqrt((df-2.)/df))
    (array(0.0), array(1.0))
    >>> sigma = np.sqrt(2.)
    >>> stats.t.stats(df, loc=0., scale=sigma*np.sqrt((df-2.)/df))
    (array(0.0), array(2.0))
    """
def ts_dlldy(y, df):
    """derivative of log pdf of standard t with respect to y

    Parameters
    ----------
    y : array_like
        data points of random variable at which loglike is evaluated
    df : array_like
        degrees of freedom,shape parameters of log-likelihood function
        of t distribution

    Returns
    -------
    dlldy : ndarray
        derivative of loglikelihood wrt random variable y evaluated at the
        points given in y

    Notes
    -----
    with mean 0 and scale 1, but variance is df/(df-2)

    """
def tstd_dlldy(y, df):
    """derivative of log pdf of standardized t with respect to y

        Parameters
        ----------
    y : array_like
        data points of random variable at which loglike is evaluated
    df : array_like
        degrees of freedom,shape parameters of log-likelihood function
        of t distribution

    Returns
    -------
    dlldy : ndarray
        derivative of loglikelihood wrt random variable y evaluated at the
        points given in y


    Notes
    -----
    parametrized for garch, standardized to variance=1
    """
def locscale_grad(y, loc, scale, dlldy, *args):
    """derivative of log-likelihood with respect to location and scale

    Parameters
    ----------
    y : array_like
        data points of random variable at which loglike is evaluated
    loc : float
        location parameter of distribution
    scale : float
        scale parameter of distribution
    dlldy : function
        derivative of loglikelihood fuction wrt. random variable x
    args : array_like
        shape parameters of log-likelihood function

    Returns
    -------
    dlldloc : ndarray
        derivative of loglikelihood wrt location evaluated at the
        points given in y
    dlldscale : ndarray
        derivative of loglikelihood wrt scale evaluated at the
        points given in y

    """
