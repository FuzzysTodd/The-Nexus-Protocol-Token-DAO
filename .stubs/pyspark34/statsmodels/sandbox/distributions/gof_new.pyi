from _typeshed import Incomplete
from statsmodels.compat.python import lmap as lmap
from statsmodels.tools.decorators import cache_readonly as cache_readonly

def ks_2samp(data1, data2):
    """
    Computes the Kolmogorov-Smirnof statistic on 2 samples.

    This is a two-sided test for the null hypothesis that 2 independent samples
    are drawn from the same continuous distribution.

    Parameters
    ----------
    a, b : sequence of 1-D ndarrays
        two arrays of sample observations assumed to be drawn from a continuous
        distribution, sample sizes can be different


    Returns
    -------
    D : float
        KS statistic
    p-value : float
        two-tailed p-value


    Notes
    -----

    This tests whether 2 samples are drawn from the same distribution. Note
    that, like in the case of the one-sample K-S test, the distribution is
    assumed to be continuous.

    This is the two-sided test, one-sided tests are not implemented.
    The test uses the two-sided asymptotic Kolmogorov-Smirnov distribution.

    If the K-S statistic is small or the p-value is high, then we cannot
    reject the hypothesis that the distributions of the two samples
    are the same.

    Examples
    --------

    >>> from scipy import stats
    >>> import numpy as np
    >>> from scipy.stats import ks_2samp

    >>> #fix random seed to get the same result
    >>> np.random.seed(12345678)

    >>> n1 = 200  # size of first sample
    >>> n2 = 300  # size of second sample

    different distribution
    we can reject the null hypothesis since the pvalue is below 1%

    >>> rvs1 = stats.norm.rvs(size=n1,loc=0.,scale=1)
    >>> rvs2 = stats.norm.rvs(size=n2,loc=0.5,scale=1.5)
    >>> ks_2samp(rvs1,rvs2)
    (0.20833333333333337, 4.6674975515806989e-005)

    slightly different distribution
    we cannot reject the null hypothesis at a 10% or lower alpha since
    the pvalue at 0.144 is higher than 10%

    >>> rvs3 = stats.norm.rvs(size=n2,loc=0.01,scale=1.0)
    >>> ks_2samp(rvs1,rvs3)
    (0.10333333333333333, 0.14498781825751686)

    identical distribution
    we cannot reject the null hypothesis since the pvalue is high, 41%

    >>> rvs4 = stats.norm.rvs(size=n2,loc=0.0,scale=1.0)
    >>> ks_2samp(rvs1,rvs4)
    (0.07999999999999996, 0.41126949729859719)
    """
def kstest(rvs, cdf, args=(), N: int = 20, alternative: str = 'two_sided', mode: str = 'approx', **kwds):
    '''
    Perform the Kolmogorov-Smirnov test for goodness of fit

    This performs a test of the distribution G(x) of an observed
    random variable against a given distribution F(x). Under the null
    hypothesis the two distributions are identical, G(x)=F(x). The
    alternative hypothesis can be either \'two_sided\' (default), \'less\'
    or \'greater\'. The KS test is only valid for continuous distributions.

    Parameters
    ----------
    rvs : str or array or callable
        string: name of a distribution in scipy.stats

        array: 1-D observations of random variables

        callable: function to generate random variables, requires keyword
        argument `size`

    cdf : str or callable
        string: name of a distribution in scipy.stats, if rvs is a string then
        cdf can evaluate to `False` or be the same as rvs
        callable: function to evaluate cdf

    args : tuple, sequence
        distribution parameters, used if rvs or cdf are strings
    N : int
        sample size if rvs is string or callable
    alternative : \'two_sided\' (default), \'less\' or \'greater\'
        defines the alternative hypothesis (see explanation)

    mode : \'approx\' (default) or \'asymp\'
        defines the distribution used for calculating p-value

        \'approx\' : use approximation to exact distribution of test statistic

        \'asymp\' : use asymptotic distribution of test statistic


    Returns
    -------
    D : float
        KS test statistic, either D, D+ or D-
    p-value :  float
        one-tailed or two-tailed p-value

    Notes
    -----

    In the one-sided test, the alternative is that the empirical
    cumulative distribution function of the random variable is "less"
    or "greater" than the cumulative distribution function F(x) of the
    hypothesis, G(x)<=F(x), resp. G(x)>=F(x).

    Examples
    --------

    >>> from scipy import stats
    >>> import numpy as np
    >>> from scipy.stats import kstest

    >>> x = np.linspace(-15,15,9)
    >>> kstest(x,\'norm\')
    (0.44435602715924361, 0.038850142705171065)

    >>> np.random.seed(987654321) # set random seed to get the same result
    >>> kstest(\'norm\',\'\',N=100)
    (0.058352892479417884, 0.88531190944151261)

    is equivalent to this

    >>> np.random.seed(987654321)
    >>> kstest(stats.norm.rvs(size=100),\'norm\')
    (0.058352892479417884, 0.88531190944151261)

    Test against one-sided alternative hypothesis:

    >>> np.random.seed(987654321)

    Shift distribution to larger values, so that cdf_dgp(x)< norm.cdf(x):

    >>> x = stats.norm.rvs(loc=0.2, size=100)
    >>> kstest(x,\'norm\', alternative = \'less\')
    (0.12464329735846891, 0.040989164077641749)

    Reject equal distribution against alternative hypothesis: less

    >>> kstest(x,\'norm\', alternative = \'greater\')
    (0.0072115233216311081, 0.98531158590396395)

    Do not reject equal distribution against alternative hypothesis: greater

    >>> kstest(x,\'norm\', mode=\'asymp\')
    (0.12464329735846891, 0.08944488871182088)


    Testing t distributed random variables against normal distribution:

    With 100 degrees of freedom the t distribution looks close to the normal
    distribution, and the kstest does not reject the hypothesis that the sample
    came from the normal distribution

    >>> np.random.seed(987654321)
    >>> stats.kstest(stats.t.rvs(100,size=100),\'norm\')
    (0.072018929165471257, 0.67630062862479168)

    With 3 degrees of freedom the t distribution looks sufficiently different
    from the normal distribution, that we can reject the hypothesis that the
    sample came from the normal distribution at a alpha=10% level

    >>> np.random.seed(987654321)
    >>> stats.kstest(stats.t.rvs(3,size=100),\'norm\')
    (0.131016895759829, 0.058826222555312224)
    '''
def dplus_st70_upp(stat, nobs): ...
dminus_st70_upp = dplus_st70_upp

def d_st70_upp(stat, nobs): ...
def v_st70_upp(stat, nobs): ...
def wsqu_st70_upp(stat, nobs): ...
def usqu_st70_upp(stat, nobs): ...
def a_st70_upp(stat, nobs): ...

gof_pvals: Incomplete

def pval_kstest_approx(D, N): ...

class GOF:
    """One Sample Goodness of Fit tests

    includes Kolmogorov-Smirnov D, D+, D-, Kuiper V, Cramer-von Mises W^2, U^2 and
    Anderson-Darling A, A^2. The p-values for all tests except for A^2 are based on
    the approximatiom given in Stephens 1970. A^2 has currently no p-values. For
    the Kolmogorov-Smirnov test the tests as given in scipy.stats are also available
    as options.




    design: I might want to retest with different distributions, to calculate
    data summary statistics only once, or add separate class that holds
    summary statistics and data (sounds good).




    """
    nobs: Incomplete
    vals_sorted: Incomplete
    cdfvals: Incomplete
    def __init__(self, rvs, cdf, args=(), N: int = 20) -> None: ...
    def d_plus(self): ...
    def d_minus(self): ...
    def d(self): ...
    def v(self):
        """Kuiper"""
    def wsqu(self):
        """Cramer von Mises"""
    def usqu(self): ...
    def a(self): ...
    def asqu(self):
        """Stephens 1974, does not have p-value formula for A^2"""
    def get_test(self, testid: str = 'd', pvals: str = 'stephens70upp'):
        """

        """

def gof_mc(randfn, distr, nobs: int = 100) -> None: ...
def asquare(cdfvals, axis: int = 0):
    """vectorized Anderson Darling A^2, Stephens 1974"""
def bootstrap(distr, args=(), nobs: int = 200, nrep: int = 100, value: Incomplete | None = None, batch_size: Incomplete | None = None):
    """Monte Carlo (or parametric bootstrap) p-values for gof

    currently hardcoded for A^2 only

    assumes vectorized fit_vec method,
    builds and analyses (nobs, nrep) sample in one step

    rename function to less generic

    this works also with nrep=1

    """
def bootstrap2(value, distr, args=(), nobs: int = 200, nrep: int = 100):
    """Monte Carlo (or parametric bootstrap) p-values for gof

    currently hardcoded for A^2 only

    non vectorized, loops over all parametric bootstrap replications and calculates
    and returns specific p-value,

    rename function to less generic

    """

class NewNorm:
    """just a holder for modified distributions
    """
    def fit_vec(self, x, axis: int = 0): ...
    def cdf(self, x, args): ...
    def rvs(self, args, size): ...
