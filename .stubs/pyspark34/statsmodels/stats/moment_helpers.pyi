def mc2mnc(mc):
    """convert central to non-central moments, uses recursive formula
    optionally adjusts first moment to return mean
    """
def mnc2mc(mnc, wmean: bool = True):
    """convert non-central to central moments, uses recursive formula
    optionally adjusts first moment to return mean
    """
def cum2mc(kappa):
    """convert non-central moments to cumulants
    recursive formula produces as many cumulants as moments

    References
    ----------
    Kenneth Lange: Numerical Analysis for Statisticians, page 40
    """
def mnc2cum(mnc):
    """convert non-central moments to cumulants
    recursive formula produces as many cumulants as moments

    https://en.wikipedia.org/wiki/Cumulant#Cumulants_and_moments
    """
def mc2cum(mc):
    """
    just chained because I have still the test case
    """
def mvsk2mc(args):
    """convert mean, variance, skew, kurtosis to central moments"""
def mvsk2mnc(args):
    """convert mean, variance, skew, kurtosis to non-central moments"""
def mc2mvsk(args):
    """convert central moments to mean, variance, skew, kurtosis"""
def mnc2mvsk(args):
    """convert central moments to mean, variance, skew, kurtosis
    """
def cov2corr(cov, return_std: bool = False):
    """
    convert covariance matrix to correlation matrix

    Parameters
    ----------
    cov : array_like, 2d
        covariance matrix, see Notes

    Returns
    -------
    corr : ndarray (subclass)
        correlation matrix
    return_std : bool
        If this is true then the standard deviation is also returned.
        By default only the correlation matrix is returned.

    Notes
    -----
    This function does not convert subclasses of ndarrays. This requires that
    division is defined elementwise. np.ma.array and np.matrix are allowed.
    """
def corr2cov(corr, std):
    """
    convert correlation matrix to covariance matrix given standard deviation

    Parameters
    ----------
    corr : array_like, 2d
        correlation matrix, see Notes
    std : array_like, 1d
        standard deviation

    Returns
    -------
    cov : ndarray (subclass)
        covariance matrix

    Notes
    -----
    This function does not convert subclasses of ndarrays. This requires
    that multiplication is defined elementwise. np.ma.array are allowed, but
    not matrices.
    """
def se_cov(cov):
    """
    get standard deviation from covariance matrix

    just a shorthand function np.sqrt(np.diag(cov))

    Parameters
    ----------
    cov : array_like, square
        covariance matrix

    Returns
    -------
    std : ndarray
        standard deviation from diagonal of cov
    """
