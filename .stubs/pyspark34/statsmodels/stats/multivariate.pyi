from _typeshed import Incomplete
from statsmodels.stats.base import HolderTuple as HolderTuple
from statsmodels.stats.moment_helpers import cov2corr as cov2corr
from statsmodels.tools.validation import array_like as array_like

def test_mvmean(data, mean_null: int = 0, return_results: bool = True):
    """Hotellings test for multivariate mean in one sample

    Parameters
    ----------
    data : array_like
        data with observations in rows and variables in columns
    mean_null : array_like
        mean of the multivariate data under the null hypothesis
    return_results : bool
        If true, then a results instance is returned. If False, then only
        the test statistic and pvalue are returned.

    Returns
    -------
    results : instance of a results class with attributes
        statistic, pvalue, t2 and df
    (statistic, pvalue) : tuple
        If return_results is false, then only the test statistic and the
        pvalue are returned.

    """
def test_mvmean_2indep(data1, data2):
    """Hotellings test for multivariate mean in two independent samples

    The null hypothesis is that both samples have the same mean.
    The alternative hypothesis is that means differ.

    Parameters
    ----------
    data1 : array_like
        first sample data with observations in rows and variables in columns
    data2 : array_like
        second sample data with observations in rows and variables in columns

    Returns
    -------
    results : instance of a results class with attributes
        statistic, pvalue, t2 and df
    """
def confint_mvmean(data, lin_transf: Incomplete | None = None, alpha: float = 0.5, simult: bool = False):
    """Confidence interval for linear transformation of a multivariate mean

    Either pointwise or simultaneous confidence intervals are returned.

    Parameters
    ----------
    data : array_like
        data with observations in rows and variables in columns
    lin_transf : array_like or None
        The linear transformation or contrast matrix for transforming the
        vector of means. If this is None, then the identity matrix is used
        which specifies the means themselves.
    alpha : float in (0, 1)
        confidence level for the confidence interval, commonly used is
        alpha=0.05.
    simult : bool
        If ``simult`` is False (default), then the pointwise confidence
        interval is returned.
        Otherwise, a simultaneous confidence interval is returned.
        Warning: additional simultaneous confidence intervals might be added
        and the default for those might change.

    Returns
    -------
    low : ndarray
        lower confidence bound on the linear transformed
    upp : ndarray
        upper confidence bound on the linear transformed
    values : ndarray
        mean or their linear transformation, center of the confidence region

    Notes
    -----
    Pointwise confidence interval is based on Johnson and Wichern
    equation (5-21) page 224.

    Simultaneous confidence interval is based on Johnson and Wichern
    Result 5.3 page 225.
    This looks like Sheffe simultaneous confidence intervals.

    Bonferroni corrected simultaneous confidence interval might be added in
    future

    References
    ----------
    Johnson, Richard A., and Dean W. Wichern. 2007. Applied Multivariate
    Statistical Analysis. 6th ed. Upper Saddle River, N.J: Pearson Prentice
    Hall.
    """
def confint_mvmean_fromstats(mean, cov, nobs, lin_transf: Incomplete | None = None, alpha: float = 0.05, simult: bool = False):
    """Confidence interval for linear transformation of a multivariate mean

    Either pointwise or simultaneous confidence intervals are returned.
    Data is provided in the form of summary statistics, mean, cov, nobs.

    Parameters
    ----------
    mean : ndarray
    cov : ndarray
    nobs : int
    lin_transf : array_like or None
        The linear transformation or contrast matrix for transforming the
        vector of means. If this is None, then the identity matrix is used
        which specifies the means themselves.
    alpha : float in (0, 1)
        confidence level for the confidence interval, commonly used is
        alpha=0.05.
    simult : bool
        If simult is False (default), then pointwise confidence interval is
        returned.
        Otherwise, a simultaneous confidence interval is returned.
        Warning: additional simultaneous confidence intervals might be added
        and the default for those might change.

    Notes
    -----
    Pointwise confidence interval is based on Johnson and Wichern
    equation (5-21) page 224.

    Simultaneous confidence interval is based on Johnson and Wichern
    Result 5.3 page 225.
    This looks like Sheffe simultaneous confidence intervals.

    Bonferroni corrected simultaneous confidence interval might be added in
    future

    References
    ----------
    Johnson, Richard A., and Dean W. Wichern. 2007. Applied Multivariate
    Statistical Analysis. 6th ed. Upper Saddle River, N.J: Pearson Prentice
    Hall.

    """
def test_cov(cov, nobs, cov_null):
    """One sample hypothesis test for covariance equal to null covariance

    The Null hypothesis is that cov = cov_null, against the alternative that
    it is not equal to cov_null

    Parameters
    ----------
    cov : array_like
        Covariance matrix of the data, estimated with denominator ``(N - 1)``,
        i.e. `ddof=1`.
    nobs : int
        number of observations used in the estimation of the covariance
    cov_null : nd_array
        covariance under the null hypothesis

    Returns
    -------
    res : instance of HolderTuple
        results with ``statistic, pvalue`` and other attributes like ``df``

    References
    ----------
    Bartlett, M. S. 1954. “A Note on the Multiplying Factors for Various Χ2
    Approximations.” Journal of the Royal Statistical Society. Series B
    (Methodological) 16 (2): 296–98.

    Rencher, Alvin C., and William F. Christensen. 2012. Methods of
    Multivariate Analysis: Rencher/Methods. Wiley Series in Probability and
    Statistics. Hoboken, NJ, USA: John Wiley & Sons, Inc.
    https://doi.org/10.1002/9781118391686.

    StataCorp, L. P. Stata Multivariate Statistics: Reference Manual.
    Stata Press Publication.

    """
def test_cov_spherical(cov, nobs):
    """One sample hypothesis test that covariance matrix is spherical

    The Null and alternative hypotheses are

    .. math::

       H0 &: \\Sigma = \\sigma I \\\\\n       H1 &: \\Sigma \\neq \\sigma I

    where :math:`\\sigma_i` is the common variance with unspecified value.

    Parameters
    ----------
    cov : array_like
        Covariance matrix of the data, estimated with denominator ``(N - 1)``,
        i.e. `ddof=1`.
    nobs : int
        number of observations used in the estimation of the covariance

    Returns
    -------
    res : instance of HolderTuple
        results with ``statistic, pvalue`` and other attributes like ``df``

    References
    ----------
    Bartlett, M. S. 1954. “A Note on the Multiplying Factors for Various Χ2
    Approximations.” Journal of the Royal Statistical Society. Series B
    (Methodological) 16 (2): 296–98.

    Rencher, Alvin C., and William F. Christensen. 2012. Methods of
    Multivariate Analysis: Rencher/Methods. Wiley Series in Probability and
    Statistics. Hoboken, NJ, USA: John Wiley & Sons, Inc.
    https://doi.org/10.1002/9781118391686.

    StataCorp, L. P. Stata Multivariate Statistics: Reference Manual.
    Stata Press Publication.
    """
def test_cov_diagonal(cov, nobs):
    """One sample hypothesis test that covariance matrix is diagonal matrix.

    The Null and alternative hypotheses are

    .. math::

       H0 &: \\Sigma = diag(\\sigma_i) \\\\\n       H1 &: \\Sigma \\neq diag(\\sigma_i)

    where :math:`\\sigma_i` are the variances with unspecified values.

    Parameters
    ----------
    cov : array_like
        Covariance matrix of the data, estimated with denominator ``(N - 1)``,
        i.e. `ddof=1`.
    nobs : int
        number of observations used in the estimation of the covariance

    Returns
    -------
    res : instance of HolderTuple
        results with ``statistic, pvalue`` and other attributes like ``df``

    References
    ----------
    Rencher, Alvin C., and William F. Christensen. 2012. Methods of
    Multivariate Analysis: Rencher/Methods. Wiley Series in Probability and
    Statistics. Hoboken, NJ, USA: John Wiley & Sons, Inc.
    https://doi.org/10.1002/9781118391686.

    StataCorp, L. P. Stata Multivariate Statistics: Reference Manual.
    Stata Press Publication.
    """
def test_cov_blockdiagonal(cov, nobs, block_len):
    """One sample hypothesis test that covariance is block diagonal.

    The Null and alternative hypotheses are

    .. math::

       H0 &: \\Sigma = diag(\\Sigma_i) \\\\\n       H1 &: \\Sigma \\neq diag(\\Sigma_i)

    where :math:`\\Sigma_i` are covariance blocks with unspecified values.

    Parameters
    ----------
    cov : array_like
        Covariance matrix of the data, estimated with denominator ``(N - 1)``,
        i.e. `ddof=1`.
    nobs : int
        number of observations used in the estimation of the covariance
    block_len : list
        list of length of each square block

    Returns
    -------
    res : instance of HolderTuple
        results with ``statistic, pvalue`` and other attributes like ``df``

    References
    ----------
    Rencher, Alvin C., and William F. Christensen. 2012. Methods of
    Multivariate Analysis: Rencher/Methods. Wiley Series in Probability and
    Statistics. Hoboken, NJ, USA: John Wiley & Sons, Inc.
    https://doi.org/10.1002/9781118391686.

    StataCorp, L. P. Stata Multivariate Statistics: Reference Manual.
    Stata Press Publication.
    """
def test_cov_oneway(cov_list, nobs_list):
    '''Multiple sample hypothesis test that covariance matrices are equal.

    This is commonly known as Box-M test.

    The Null and alternative hypotheses are

    .. math::

       H0 &: \\Sigma_i = \\Sigma_j  \\text{ for all i and j} \\\\\n       H1 &: \\Sigma_i \\neq \\Sigma_j \\text{ for at least one i and j}

    where :math:`\\Sigma_i` is the covariance of sample `i`.

    Parameters
    ----------
    cov_list : list of array_like
        Covariance matrices of the sample, estimated with denominator
        ``(N - 1)``, i.e. `ddof=1`.
    nobs_list : list
        List of the number of observations used in the estimation of the
        covariance for each sample.

    Returns
    -------
    res : instance of HolderTuple
        Results contains test statistic and pvalues for both chisquare and F
        distribution based tests, identified by the name ending "_chi2" and
        "_f".
        Attributes ``statistic, pvalue`` refer to the F-test version.

    Notes
    -----
    approximations to distribution of test statistic is by Box

    References
    ----------
    Rencher, Alvin C., and William F. Christensen. 2012. Methods of
    Multivariate Analysis: Rencher/Methods. Wiley Series in Probability and
    Statistics. Hoboken, NJ, USA: John Wiley & Sons, Inc.
    https://doi.org/10.1002/9781118391686.

    StataCorp, L. P. Stata Multivariate Statistics: Reference Manual.
    Stata Press Publication.
    '''
