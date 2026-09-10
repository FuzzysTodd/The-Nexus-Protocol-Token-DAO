from scipy.special import beta as beta

def tukeylambda_variance(lam):
    """Variance of the Tukey Lambda distribution.

    Parameters
    ----------
    lam : array_like
        The lambda values at which to compute the variance.

    Returns
    -------
    v : ndarray
        The variance.  For lam < -0.5, the variance is not defined, so
        np.nan is returned.  For lam = 0.5, np.inf is returned.

    Notes
    -----
    In an interval around lambda=0, this function uses the [4,4] Pade
    approximation to compute the variance.  Otherwise it uses the standard
    formula (https://en.wikipedia.org/wiki/Tukey_lambda_distribution).  The
    Pade approximation is used because the standard formula has a removable
    discontinuity at lambda = 0, and does not produce accurate numerical
    results near lambda = 0.
    """
def tukeylambda_kurtosis(lam):
    """Kurtosis of the Tukey Lambda distribution.

    Parameters
    ----------
    lam : array_like
        The lambda values at which to compute the variance.

    Returns
    -------
    v : ndarray
        The variance.  For lam < -0.25, the variance is not defined, so
        np.nan is returned.  For lam = 0.25, np.inf is returned.

    """
