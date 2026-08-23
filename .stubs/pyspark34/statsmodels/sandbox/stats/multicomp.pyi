from _typeshed import Incomplete
from collections.abc import Generator
from statsmodels.compat.python import lrange as lrange, lzip as lzip
from statsmodels.graphics import utils as utils
from statsmodels.iolib.table import SimpleTable as SimpleTable
from statsmodels.stats.libqsturng import psturng as psturng, qsturng as qsturng
from statsmodels.stats.multitest import fdrcorrection_twostage as fdrcorrection_twostage, multipletests as multipletests
from statsmodels.tools.sm_exceptions import ValueWarning as ValueWarning
from typing import NamedTuple

class studentized_range_tuple(NamedTuple):
    ppf: Incomplete
    sf: Incomplete

qcrit: str
res: Incomplete
c: Incomplete
ccols: Incomplete
crows: Incomplete
cv005: Incomplete
cv001: Incomplete

def get_tukeyQcrit(k, df, alpha: float = 0.05):
    """
    return critical values for Tukey's HSD (Q)

    Parameters
    ----------
    k : int in {2, ..., 10}
        number of tests
    df : int
        degrees of freedom of error term
    alpha : {0.05, 0.01}
        type 1 error, 1-confidence level



    not enough error checking for limitations
    """
def get_tukeyQcrit2(k, df, alpha: float = 0.05):
    """
    return critical values for Tukey's HSD (Q)

    Parameters
    ----------
    k : int in {2, ..., 10}
        number of tests
    df : int
        degrees of freedom of error term
    alpha : {0.05, 0.01}
        type 1 error, 1-confidence level



    not enough error checking for limitations
    """
def get_tukey_pvalue(k, df, q):
    """
    return adjusted p-values for Tukey's HSD

    Parameters
    ----------
    k : int in {2, ..., 10}
        number of tests
    df : int
        degrees of freedom of error term
    q : scalar, array_like; q >= 0
        quantile value of Studentized Range

    """
def Tukeythreegene(first, second, third): ...
def Tukeythreegene2(genes) -> None:
    """gend is a list, ie [first, second, third]"""
def catstack(args): ...
def maxzero(x):
    """find all up zero crossings and return the index of the highest

    Not used anymore


    >>> np.random.seed(12345)
    >>> x = np.random.randn(8)
    >>> x
    array([-0.20470766,  0.47894334, -0.51943872, -0.5557303 ,  1.96578057,
            1.39340583,  0.09290788,  0.28174615])
    >>> maxzero(x)
    (4, array([1, 4]))


    no up-zero-crossing at end

    >>> np.random.seed(0)
    >>> x = np.random.randn(8)
    >>> x
    array([ 1.76405235,  0.40015721,  0.97873798,  2.2408932 ,  1.86755799,
           -0.97727788,  0.95008842, -0.15135721])
    >>> maxzero(x)
    (None, array([6]))
    """
def maxzerodown(x):
    """find all up zero crossings and return the index of the highest

    Not used anymore

    >>> np.random.seed(12345)
    >>> x = np.random.randn(8)
    >>> x
    array([-0.20470766,  0.47894334, -0.51943872, -0.5557303 ,  1.96578057,
            1.39340583,  0.09290788,  0.28174615])
    >>> maxzero(x)
    (4, array([1, 4]))


    no up-zero-crossing at end

    >>> np.random.seed(0)
    >>> x = np.random.randn(8)
    >>> x
    array([ 1.76405235,  0.40015721,  0.97873798,  2.2408932 ,  1.86755799,
           -0.97727788,  0.95008842, -0.15135721])
    >>> maxzero(x)
    (None, array([6]))
"""
def rejectionline(n, alpha: float = 0.5):
    """reference line for rejection in multiple tests

    Not used anymore

    from: section 3.2, page 60
    """
def fdrcorrection_bak(pvals, alpha: float = 0.05, method: str = 'indep'):
    """Reject False discovery rate correction for pvalues

    Old version, to be deleted


    missing: methods that estimate fraction of true hypotheses

    """
def mcfdr(nrepl: int = 100, nobs: int = 50, ntests: int = 10, ntrue: int = 6, mu: float = 0.5, alpha: float = 0.05, rho: float = 0.0):
    """MonteCarlo to test fdrcorrection
    """
def randmvn(rho, size=(1, 2), standardize: bool = False):
    """create random draws from equi-correlated multivariate normal distribution

    Parameters
    ----------
    rho : float
        correlation coefficient
    size : tuple of int
        size is interpreted (nobs, nvars) where each row

    Returns
    -------
    rvs : ndarray
        nobs by nvars where each row is a independent random draw of nvars-
        dimensional correlated rvs

    """
def tiecorrect(xranks):
    """

    should be equivalent of scipy.stats.tiecorrect

    """

class GroupsStats:
    """
    statistics by groups (another version)

    groupstats as a class with lazy evaluation (not yet - decorators are still
    missing)

    written this time as equivalent of scipy.stats.rankdata
    gs = GroupsStats(X, useranks=True)
    assert_almost_equal(gs.groupmeanfilter, stats.rankdata(X[:,0]), 15)

    TODO: incomplete doc strings

    """
    x: Incomplete
    useranks: Incomplete
    uni: Incomplete
    intlab: Incomplete
    groupnobs: Incomplete
    def __init__(self, x, useranks: bool = False, uni: Incomplete | None = None, intlab: Incomplete | None = None) -> None:
        """descriptive statistics by groups

        Parameters
        ----------
        x : ndarray, 2d
            first column data, second column group labels
        useranks : bool
            if true, then use ranks as data corresponding to the
            scipy.stats.rankdata definition (start at 1, ties get mean)
        uni, intlab : arrays (optional)
            to avoid call to unique, these can be given as inputs


        """
    xx: Incomplete
    groupsum: Incomplete
    groupmean: Incomplete
    groupmeanfilter: Incomplete
    def runbasic_old(self, useranks: bool = False) -> None:
        """runbasic_old"""
    def runbasic(self, useranks: bool = False) -> None:
        """runbasic"""
    def groupdemean(self):
        """groupdemean"""
    def groupsswithin(self):
        """groupsswithin"""
    def groupvarwithin(self):
        """groupvarwithin"""

class TukeyHSDResults:
    """Results from Tukey HSD test, with additional plot methods

    Can also compute and plot additional post-hoc evaluations using this
    results class.

    Attributes
    ----------
    reject : array of boolean, True if we reject Null for group pair
    meandiffs : pairwise mean differences
    confint : confidence interval for pairwise mean differences
    std_pairs : standard deviation of pairwise mean differences
    q_crit : critical value of studentized range statistic at given alpha
    halfwidths : half widths of simultaneous confidence interval
    pvalues : adjusted p-values from the HSD test

    Notes
    -----
    halfwidths is only available after call to `plot_simultaneous`.

    Other attributes contain information about the data from the
    MultiComparison instance: data, df_total, groups, groupsunique, variance.
    """
    q_crit: Incomplete
    reject: Incomplete
    meandiffs: Incomplete
    std_pairs: Incomplete
    confint: Incomplete
    df_total: Incomplete
    reject2: Incomplete
    variance: Incomplete
    pvalues: Incomplete
    data: Incomplete
    groups: Incomplete
    groupsunique: Incomplete
    def __init__(self, mc_object, results_table, q_crit, reject: Incomplete | None = None, meandiffs: Incomplete | None = None, std_pairs: Incomplete | None = None, confint: Incomplete | None = None, df_total: Incomplete | None = None, reject2: Incomplete | None = None, variance: Incomplete | None = None, pvalues: Incomplete | None = None) -> None: ...
    def summary(self):
        """Summary table that can be printed
        """
    def plot_simultaneous(self, comparison_name: Incomplete | None = None, ax: Incomplete | None = None, figsize=(10, 6), xlabel: Incomplete | None = None, ylabel: Incomplete | None = None):
        '''Plot a universal confidence interval of each group mean

        Visualize significant differences in a plot with one confidence
        interval per group instead of all pairwise confidence intervals.

        Parameters
        ----------
        comparison_name : str, optional
            if provided, plot_intervals will color code all groups that are
            significantly different from the comparison_name red, and will
            color code insignificant groups gray. Otherwise, all intervals will
            just be plotted in black.
        ax : matplotlib axis, optional
            An axis handle on which to attach the plot.
        figsize : tuple, optional
            tuple for the size of the figure generated
        xlabel : str, optional
            Name to be displayed on x axis
        ylabel : str, optional
            Name to be displayed on y axis

        Returns
        -------
        Figure
            handle to figure object containing interval plots

        Notes
        -----
        Multiple comparison tests are nice, but lack a good way to be
        visualized. If you have, say, 6 groups, showing a graph of the means
        between each group will require 15 confidence intervals.
        Instead, we can visualize inter-group differences with a single
        interval for each group mean. Hochberg et al. [1] first proposed this
        idea and used Tukey\'s Q critical value to compute the interval widths.
        Unlike plotting the differences in the means and their respective
        confidence intervals, any two pairs can be compared for significance
        by looking for overlap.

        References
        ----------
        .. [*] Hochberg, Y., and A. C. Tamhane. Multiple Comparison Procedures.
               Hoboken, NJ: John Wiley & Sons, 1987.

        Examples
        --------
        >>> from statsmodels.examples.try_tukey_hsd import cylinders, cyl_labels
        >>> from statsmodels.stats.multicomp import MultiComparison
        >>> cardata = MultiComparison(cylinders, cyl_labels)
        >>> results = cardata.tukeyhsd()
        >>> results.plot_simultaneous()
        <matplotlib.figure.Figure at 0x...>

        This example shows an example plot comparing significant differences
        in group means. Significant differences at the alpha=0.05 level can be
        identified by intervals that do not overlap (i.e. USA vs Japan,
        USA vs Germany).

        >>> results.plot_simultaneous(comparison_name="USA")
        <matplotlib.figure.Figure at 0x...>

        Optionally provide one of the group names to color code the plot to
        highlight group means different from comparison_name.
        '''

class MultiComparison:
    """Tests for multiple comparisons

    Parameters
    ----------
    data : ndarray
        independent data samples
    groups : ndarray
        group labels corresponding to each data point
    group_order : list[str], optional
        the desired order for the group mean results to be reported in. If
        not specified, results are reported in increasing order.
        If group_order does not contain all labels that are in groups, then
        only those observations are kept that have a label in group_order.

    """
    data: Incomplete
    groups: Incomplete
    groupsunique: Incomplete
    groupintlab: Incomplete
    datali: Incomplete
    pairindices: Incomplete
    nobs: Incomplete
    ngroups: Incomplete
    def __init__(self, data, groups, group_order: Incomplete | None = None) -> None: ...
    ranks: Incomplete
    rankdata: Incomplete
    def getranks(self) -> None:
        """convert data to rankdata and attach


        This creates rankdata as it is used for non-parametric tests, where
        in the case of ties the average rank is assigned.


        """
    def kruskal(self, pairs: Incomplete | None = None, multimethod: str = 'T'):
        """
        pairwise comparison for kruskal-wallis test

        This is just a reimplementation of scipy.stats.kruskal and does
        not yet use a multiple comparison correction.

        """
    def allpairtest(self, testfunc, alpha: float = 0.05, method: str = 'bonf', pvalidx: int = 1):
        """run a pairwise test on all pairs with multiple test correction

        The statistical test given in testfunc is calculated for all pairs
        and the p-values are adjusted by methods in multipletests. The p-value
        correction is generic and based only on the p-values, and does not
        take any special structure of the hypotheses into account.

        Parameters
        ----------
        testfunc : function
            A test function for two (independent) samples. It is assumed that
            the return value on position pvalidx is the p-value.
        alpha : float
            familywise error rate
        method : str
            This specifies the method for the p-value correction. Any method
            of multipletests is possible.
        pvalidx : int (default: 1)
            position of the p-value in the return of testfunc

        Returns
        -------
        sumtab : SimpleTable instance
            summary table for printing

        errors:  TODO: check if this is still wrong, I think it's fixed.
        results from multipletests are in different order
        pval_corrected can be larger than 1 ???
        """
    groupstats: Incomplete
    def tukeyhsd(self, alpha: float = 0.05):
        """
        Tukey's range test to compare means of all pairs of groups

        Parameters
        ----------
        alpha : float, optional
            Value of FWER at which to calculate HSD.

        Returns
        -------
        results : TukeyHSDResults instance
            A results class containing relevant data and some post-hoc
            calculations
        """

def rankdata(x):
    """rankdata, equivalent to scipy.stats.rankdata

    just a different implementation, I have not yet compared speed

    """
def compare_ordered(vals, alpha) -> None:
    """simple ordered sequential comparison of means

    vals : array_like
        means or rankmeans for independent groups

    incomplete, no return, not used yet
    """
def varcorrection_unbalanced(nobs_all, srange: bool = False):
    """correction factor for variance with unequal sample sizes

    this is just a harmonic mean

    Parameters
    ----------
    nobs_all : array_like
        The number of observations for each sample
    srange : bool
        if true, then the correction is divided by the number of samples
        for the variance of the studentized range statistic

    Returns
    -------
    correction : float
        Correction factor for variance.


    Notes
    -----

    variance correction factor is

    1/k * sum_i 1/n_i

    where k is the number of samples and summation is over i=0,...,k-1.
    If all n_i are the same, then the correction factor is 1.

    This needs to be multiplied by the joint variance estimate, means square
    error, MSE. To obtain the correction factor for the standard deviation,
    square root needs to be taken.

    """
def varcorrection_pairs_unbalanced(nobs_all, srange: bool = False):
    """correction factor for variance with unequal sample sizes for all pairs

    this is just a harmonic mean

    Parameters
    ----------
    nobs_all : array_like
        The number of observations for each sample
    srange : bool
        if true, then the correction is divided by 2 for the variance of
        the studentized range statistic

    Returns
    -------
    correction : ndarray
        Correction factor for variance.


    Notes
    -----

    variance correction factor is

    1/k * sum_i 1/n_i

    where k is the number of samples and summation is over i=0,...,k-1.
    If all n_i are the same, then the correction factor is 1.

    This needs to be multiplies by the joint variance estimate, means square
    error, MSE. To obtain the correction factor for the standard deviation,
    square root needs to be taken.

    For the studentized range statistic, the resulting factor has to be
    divided by 2.

    """
def varcorrection_unequal(var_all, nobs_all, df_all):
    """return joint variance from samples with unequal variances and unequal
    sample sizes

    something is wrong

    Parameters
    ----------
    var_all : array_like
        The variance for each sample
    nobs_all : array_like
        The number of observations for each sample
    df_all : array_like
        degrees of freedom for each sample

    Returns
    -------
    varjoint : float
        joint variance.
    dfjoint : float
        joint Satterthwait's degrees of freedom


    Notes
    -----
    (copy, paste not correct)
    variance is

    1/k * sum_i 1/n_i

    where k is the number of samples and summation is over i=0,...,k-1.
    If all n_i are the same, then the correction factor is 1/n.

    This needs to be multiplies by the joint variance estimate, means square
    error, MSE. To obtain the correction factor for the standard deviation,
    square root needs to be taken.

    This is for variance of mean difference not of studentized range.
    """
def varcorrection_pairs_unequal(var_all, nobs_all, df_all):
    """return joint variance from samples with unequal variances and unequal
    sample sizes for all pairs

    something is wrong

    Parameters
    ----------
    var_all : array_like
        The variance for each sample
    nobs_all : array_like
        The number of observations for each sample
    df_all : array_like
        degrees of freedom for each sample

    Returns
    -------
    varjoint : ndarray
        joint variance.
    dfjoint : ndarray
        joint Satterthwait's degrees of freedom


    Notes
    -----

    (copy, paste not correct)
    variance is

    1/k * sum_i 1/n_i

    where k is the number of samples and summation is over i=0,...,k-1.
    If all n_i are the same, then the correction factor is 1.

    This needs to be multiplies by the joint variance estimate, means square
    error, MSE. To obtain the correction factor for the standard deviation,
    square root needs to be taken.

    TODO: something looks wrong with dfjoint, is formula from SPSS
    """
def tukeyhsd(mean_all, nobs_all, var_all, df: Incomplete | None = None, alpha: float = 0.05, q_crit: Incomplete | None = None):
    """simultaneous Tukey HSD


    check: instead of sorting, I use absolute value of pairwise differences
    in means. That's irrelevant for the test, but maybe reporting actual
    differences would be better.
    CHANGED: meandiffs are with sign, studentized range uses abs

    q_crit added for testing

    TODO: error in variance calculation when nobs_all is scalar, missing 1/n

    """
def simultaneous_ci(q_crit, var, groupnobs, pairindices: Incomplete | None = None):
    """Compute simultaneous confidence intervals for comparison of means.

    q_crit value is generated from tukey hsd test. Variance is considered
    across all groups. Returned halfwidths can be thought of as uncertainty
    intervals around each group mean. They allow for simultaneous
    comparison of pairwise significance among any pairs (by checking for
    overlap)

    Parameters
    ----------
    q_crit : float
        The Q critical value studentized range statistic from Tukey's HSD
    var : float
        The group variance
    groupnobs : array_like object
        Number of observations contained in each group.
    pairindices : tuple of lists, optional
        Indices corresponding to the upper triangle of matrix. Computed
        here if not supplied

    Returns
    -------
    halfwidths : ndarray
        Half the width of each confidence interval for each group given in
        groupnobs

    See Also
    --------
    MultiComparison : statistics class providing significance tests
    tukeyhsd : among other things, computes q_crit value

    References
    ----------
    .. [*] Hochberg, Y., and A. C. Tamhane. Multiple Comparison Procedures.
           Hoboken, NJ: John Wiley & Sons, 1987.)
    """
def distance_st_range(mean_all, nobs_all, var_all, df: Incomplete | None = None, triu: bool = False):
    """pairwise distance matrix, outsourced from tukeyhsd



    CHANGED: meandiffs are with sign, studentized range uses abs

    q_crit added for testing

    TODO: error in variance calculation when nobs_all is scalar, missing 1/n

    """
def contrast_allpairs(nm):
    """contrast or restriction matrix for all pairs of nm variables

    Parameters
    ----------
    nm : int

    Returns
    -------
    contr : ndarray, 2d, (nm*(nm-1)/2, nm)
       contrast matrix for all pairwise comparisons

    """
def contrast_all_one(nm):
    """contrast or restriction matrix for all against first comparison

    Parameters
    ----------
    nm : int

    Returns
    -------
    contr : ndarray, 2d, (nm-1, nm)
       contrast matrix for all against first comparisons

    """
def contrast_diff_mean(nm):
    """contrast or restriction matrix for all against mean comparison

    Parameters
    ----------
    nm : int

    Returns
    -------
    contr : ndarray, 2d, (nm-1, nm)
       contrast matrix for all against mean comparisons

    """
def tukey_pvalues(std_range, nm, df): ...
def multicontrast_pvalues(tstat, tcorr, df: Incomplete | None = None, dist: str = 't', alternative: str = 'two-sided'):
    """pvalues for simultaneous tests

    """

class StepDown:
    """a class for step down methods

    This is currently for simple tree subset descend, similar to homogeneous_subsets,
    but checks all leave-one-out subsets instead of assuming an ordered set.
    Comment in SAS manual:
    SAS only uses interval subsets of the sorted list, which is sufficient for range
    tests (maybe also equal variance and balanced sample sizes are required).
    For F-test based critical distances, the restriction to intervals is not sufficient.

    This version uses a single critical value of the studentized range distribution
    for all comparisons, and is therefore a step-down version of Tukey HSD.
    The class is written so it can be subclassed, where the get_distance_matrix and
    get_crit are overwritten to obtain other step-down procedures such as REGW.

    iter_subsets can be overwritten, to get a recursion as in the many to one comparison
    with a control such as in Dunnet's test.


    A one-sided right tail test is not covered because the direction of the inequality
    is hard coded in check_set.  Also Peritz's check of partitions is not possible, but
    I have not seen it mentioned in any more recent references.
    I have only partially read the step-down procedure for closed tests by Westfall.

    One change to make it more flexible, is to separate out the decision on a subset,
    also because the F-based tests, FREGW in SPSS, take information from all elements of
    a set and not just pairwise comparisons. I have not looked at the details of
    the F-based tests such as Sheffe yet. It looks like running an F-test on equality
    of means in each subset. This would also outsource how pairwise conditions are
    combined, any larger or max. This would also imply that the distance matrix cannot
    be calculated in advance for tests like the F-based ones.


    """
    vals: Incomplete
    n_vals: Incomplete
    nobs_all: Incomplete
    var_all: Incomplete
    df: Incomplete
    def __init__(self, vals, nobs_all, var_all, df: Incomplete | None = None) -> None: ...
    def get_crit(self, alpha):
        """
        get_tukeyQcrit

        currently tukey Q, add others
        """
    distance_matrix: Incomplete
    def get_distance_matrix(self) -> None:
        """studentized range statistic"""
    def iter_subsets(self, indices) -> Generator[Incomplete, None, None]:
        """Iterate substeps"""
    def check_set(self, indices):
        """check whether pairwise distances of indices satisfy condition

        """
    def stepdown(self, indices):
        """stepdown"""
    cache_result: Incomplete
    crit: Incomplete
    accepted: Incomplete
    rejected: Incomplete
    def run(self, alpha):
        """main function to run the test,

        could be done in __call__ instead
        this could have all the initialization code

        """

def homogeneous_subsets(vals, dcrit):
    """recursively check all pairs of vals for minimum distance

    step down method as in Newman-Keuls and Ryan procedures. This is not a
    closed procedure since not all partitions are checked.

    Parameters
    ----------
    vals : array_like
        values that are pairwise compared
    dcrit : array_like or float
        critical distance for rejecting, either float, or 2-dimensional array
        with distances on the upper triangle.

    Returns
    -------
    rejs : list of pairs
        list of pair-indices with (strictly) larger than critical difference
    nrejs : list of pairs
        list of pair-indices with smaller than critical difference
    lli : list of tuples
        list of subsets with smaller than critical difference
    res : tree
        result of all comparisons (for checking)


    this follows description in SPSS notes on Post-Hoc Tests

    Because of the recursive structure, some comparisons are made several
    times, but only unique pairs or sets are returned.

    Examples
    --------
    >>> m = [0, 2, 2.5, 3, 6, 8, 9, 9.5,10 ]
    >>> rej, nrej, ssli, res = homogeneous_subsets(m, 2)
    >>> set_partition(ssli)
    ([(5, 6, 7, 8), (1, 2, 3), (4,)], [0])
    >>> [np.array(m)[list(pp)] for pp in set_partition(ssli)[0]]
    [array([  8. ,   9. ,   9.5,  10. ]), array([ 2. ,  2.5,  3. ]), array([ 6.])]


    """
def set_partition(ssli):
    """extract a partition from a list of tuples

    this should be correctly called select largest disjoint sets.
    Begun and Gabriel 1981 do not seem to be bothered by sets of accepted
    hypothesis with joint elements,
    e.g. maximal_accepted_sets = { {1,2,3}, {2,3,4} }

    This creates a set partition from a list of sets given as tuples.
    It tries to find the partition with the largest sets. That is, sets are
    included after being sorted by length.

    If the list does not include the singletons, then it will be only a
    partial partition. Missing items are singletons (I think).

    Examples
    --------
    >>> li
    [(5, 6, 7, 8), (1, 2, 3), (4, 5), (0, 1)]
    >>> set_partition(li)
    ([(5, 6, 7, 8), (1, 2, 3)], [0, 4])

    """
def set_remove_subs(ssli):
    """remove sets that are subsets of another set from a list of tuples

    Parameters
    ----------
    ssli : list of tuples
        each tuple is considered as a set

    Returns
    -------
    part : list of tuples
        new list with subset tuples removed, it is sorted by set-length of tuples. The
        list contains original tuples, duplicate elements are not removed.

    Examples
    --------
    >>> set_remove_subs([(0, 1), (1, 2), (1, 2, 3), (0,)])
    [(1, 2, 3), (0, 1)]
    >>> set_remove_subs([(0, 1), (1, 2), (1,1, 1, 2, 3), (0,)])
    [(1, 1, 1, 2, 3), (0, 1)]

    """
