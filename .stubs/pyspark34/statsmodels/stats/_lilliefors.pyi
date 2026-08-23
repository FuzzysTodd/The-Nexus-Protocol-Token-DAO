from ._lilliefors_critical_values import PERCENTILES as PERCENTILES, asymp_critical_values as asymp_critical_values, critical_values as critical_values
from .tabledist import TableDist as TableDist
from _typeshed import Incomplete
from statsmodels.tools.validation import string_like as string_like

def ksstat(x, cdf, alternative: str = 'two_sided', args=()):
    '''
    Calculate statistic for the Kolmogorov-Smirnov test for goodness of fit

    This calculates the test statistic for a test of the distribution G(x) of
    an observed variable against a given distribution F(x). Under the null
    hypothesis the two distributions are identical, G(x)=F(x). The
    alternative hypothesis can be either \'two_sided\' (default), \'less\'
    or \'greater\'. The KS test is only valid for continuous distributions.

    Parameters
    ----------
    x : array_like, 1d
        array of observations
    cdf : str or callable
        string: name of a distribution in scipy.stats
        callable: function to evaluate cdf
    alternative : \'two_sided\' (default), \'less\' or \'greater\'
        defines the alternative hypothesis (see explanation)
    args : tuple, sequence
        distribution parameters for call to cdf


    Returns
    -------
    D : float
        KS test statistic, either D, D+ or D-

    See Also
    --------
    scipy.stats.kstest

    Notes
    -----

    In the one-sided test, the alternative is that the empirical
    cumulative distribution function of the random variable is "less"
    or "greater" than the cumulative distribution function F(x) of the
    hypothesis, G(x)<=F(x), resp. G(x)>=F(x).

    In contrast to scipy.stats.kstest, this function only calculates the
    statistic which can be used either as distance measure or to implement
    case specific p-values.
    '''
def get_lilliefors_table(dist: str = 'norm'):
    """
    Generates tables for significance levels of Lilliefors test statistics

    Tables for available normal and exponential distribution testing,
    as specified in Lilliefors references above

    Parameters
    ----------
    dist : str
        distribution being tested in set {'norm', 'exp'}.

    Returns
    -------
    lf : TableDist object.
        table of critical values
    """

lilliefors_table_norm: Incomplete
lilliefors_table_expon: Incomplete

def pval_lf(d_max, n):
    """
    Approximate pvalues for Lilliefors test

    This is only valid for pvalues smaller than 0.1 which is not checked in
    this function.

    Parameters
    ----------
    d_max : array_like
        two-sided Kolmogorov-Smirnov test statistic
    n : int or float
        sample size

    Returns
    -------
    p-value : float or ndarray
        pvalue according to approximation formula of Dallal and Wilkinson.

    Notes
    -----
    This is mainly a helper function where the calling code should dispatch
    on bound violations. Therefore it does not check whether the pvalue is in
    the valid range.

    Precision for the pvalues is around 2 to 3 decimals. This approximation is
    also used by other statistical packages (e.g. R:fBasics) but might not be
    the most precise available.

    References
    ----------
    DallalWilkinson1986
    """
def kstest_fit(x, dist: str = 'norm', pvalmethod: str = 'table'):
    """
    Test assumed normal or exponential distribution using Lilliefors' test.

    Lilliefors' test is a Kolmogorov-Smirnov test with estimated parameters.

    Parameters
    ----------
    x : array_like, 1d
        Data to test.
    dist : {'norm', 'exp'}, optional
        The assumed distribution.
    pvalmethod : {'approx', 'table'}, optional
        The method used to compute the p-value of the test statistic. In
        general, 'table' is preferred and makes use of a very large simulation.
        'approx' is only valid for normality. if `dist = 'exp'` `table` is
        always used. 'approx' uses the approximation formula of Dalal and
        Wilkinson, valid for pvalues < 0.1. If the pvalue is larger than 0.1,
        then the result of `table` is returned.

    Returns
    -------
    ksstat : float
        Kolmogorov-Smirnov test statistic with estimated mean and variance.
    pvalue : float
        If the pvalue is lower than some threshold, e.g. 0.05, then we can
        reject the Null hypothesis that the sample comes from a normal
        distribution.

    Notes
    -----
    'table' uses an improved table based on 10,000,000 simulations. The
    critical values are approximated using
    log(cv_alpha) = b_alpha + c[0] log(n) + c[1] log(n)**2
    where cv_alpha is the critical value for a test with size alpha,
    b_alpha is an alpha-specific intercept term and c[1] and c[2] are
    coefficients that are shared all alphas.
    Values in the table are linearly interpolated. Values outside the
    range are be returned as bounds, 0.990 for large and 0.001 for small
    pvalues.

    For implementation details, see  lilliefors_critical_value_simulation.py in
    the test directory.
    """
lilliefors = kstest_fit
kstest_normal = kstest_fit
kstest_exponential: Incomplete
