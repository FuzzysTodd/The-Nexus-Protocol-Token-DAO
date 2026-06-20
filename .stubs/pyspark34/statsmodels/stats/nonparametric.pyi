from _typeshed import Incomplete
from statsmodels.stats.base import HolderTuple as HolderTuple

def rankdata_2samp(x1, x2):
    """Compute midranks for two samples

    Parameters
    ----------
    x1, x2 : array_like
        Original data for two samples that will be converted to midranks.

    Returns
    -------
    rank1 : ndarray
        Midranks of the first sample in the pooled sample.
    rank2 : ndarray
        Midranks of the second sample in the pooled sample.
    ranki1 : ndarray
        Internal midranks of the first sample.
    ranki2 : ndarray
        Internal midranks of the second sample.

    """

class RankCompareResult(HolderTuple):
    """Results for rank comparison

    This is a subclass of HolderTuple that includes results from intermediate
    computations, as well as methods for hypothesis tests, confidence intervals
    and summary.
    """
    def conf_int(self, value: Incomplete | None = None, alpha: float = 0.05, alternative: str = 'two-sided'):
        '''
        Confidence interval for probability that sample 1 has larger values

        Confidence interval is for the shifted probability

            P(x1 > x2) + 0.5 * P(x1 = x2) - value

        Parameters
        ----------
        value : float
            Value, default 0, shifts the confidence interval,
            e.g. ``value=0.5`` centers the confidence interval at zero.
        alpha : float
            Significance level for the confidence interval, coverage is
            ``1-alpha``
        alternative : str
            The alternative hypothesis, H1, has to be one of the following

               * \'two-sided\' : H1: ``prob - value`` not equal to 0.
               * \'larger\' :   H1: ``prob - value > 0``
               * \'smaller\' :  H1: ``prob - value < 0``

        Returns
        -------
        lower : float or ndarray
            Lower confidence limit. This is -inf for the one-sided alternative
            "smaller".
        upper : float or ndarray
            Upper confidence limit. This is inf for the one-sided alternative
            "larger".

        '''
    def test_prob_superior(self, value: float = 0.5, alternative: str = 'two-sided'):
        """test for superiority probability

        H0: P(x1 > x2) + 0.5 * P(x1 = x2) = value

        The alternative is that the probability is either not equal, larger
        or smaller than the null-value depending on the chosen alternative.

        Parameters
        ----------
        value : float
            Value of the probability under the Null hypothesis.
        alternative : str
            The alternative hypothesis, H1, has to be one of the following

               * 'two-sided' : H1: ``prob - value`` not equal to 0.
               * 'larger' :   H1: ``prob - value > 0``
               * 'smaller' :  H1: ``prob - value < 0``

        Returns
        -------
        res : HolderTuple
            HolderTuple instance with the following main attributes

            statistic : float
                Test statistic for z- or t-test
            pvalue : float
                Pvalue of the test based on either normal or t distribution.

        """
    def tost_prob_superior(self, low, upp):
        """test of stochastic (non-)equivalence of p = P(x1 > x2)

        Null hypothesis:  p < low or p > upp
        Alternative hypothesis:  low < p < upp

        where p is the probability that a random draw from the population of
        the first sample has a larger value than a random draw from the
        population of the second sample, specifically

            p = P(x1 > x2) + 0.5 * P(x1 = x2)

        If the pvalue is smaller than a threshold, say 0.05, then we reject the
        hypothesis that the probability p that distribution 1 is stochastically
        superior to distribution 2 is outside of the interval given by
        thresholds low and upp.

        Parameters
        ----------
        low, upp : float
            equivalence interval low < mean < upp

        Returns
        -------
        res : HolderTuple
            HolderTuple instance with the following main attributes

            pvalue : float
                Pvalue of the equivalence test given by the larger pvalue of
                the two one-sided tests.
            statistic : float
                Test statistic of the one-sided test that has the larger
                pvalue.
            results_larger : HolderTuple
                Results instanc with test statistic, pvalue and degrees of
                freedom for lower threshold test.
            results_smaller : HolderTuple
                Results instanc with test statistic, pvalue and degrees of
                freedom for upper threshold test.

        """
    def confint_lintransf(self, const: int = -1, slope: int = 2, alpha: float = 0.05, alternative: str = 'two-sided'):
        '''confidence interval of a linear transformation of prob1

        This computes the confidence interval for

            d = const + slope * prob1

        Default values correspond to Somers\' d.

        Parameters
        ----------
        const, slope : float
            Constant and slope for linear (affine) transformation.
        alpha : float
            Significance level for the confidence interval, coverage is
            ``1-alpha``
        alternative : str
            The alternative hypothesis, H1, has to be one of the following

               * \'two-sided\' : H1: ``prob - value`` not equal to 0.
               * \'larger\' :   H1: ``prob - value > 0``
               * \'smaller\' :  H1: ``prob - value < 0``

        Returns
        -------
        lower : float or ndarray
            Lower confidence limit. This is -inf for the one-sided alternative
            "smaller".
        upper : float or ndarray
            Upper confidence limit. This is inf for the one-sided alternative
            "larger".

        '''
    def effectsize_normal(self, prob: Incomplete | None = None):
        """
        Cohen's d, standardized mean difference under normality assumption.

        This computes the standardized mean difference, Cohen's d, effect size
        that is equivalent to the rank based probability ``p`` of being
        stochastically larger if we assume that the data is normally
        distributed, given by

            :math: `d = F^{-1}(p) * \\sqrt{2}`

        where :math:`F^{-1}` is the inverse of the cdf of the normal
        distribution.

        Parameters
        ----------
        prob : float in (0, 1)
            Probability to be converted to Cohen's d effect size.
            If prob is None, then the ``prob1`` attribute is used.

        Returns
        -------
        equivalent Cohen's d effect size under normality assumption.

        """
    def summary(self, alpha: float = 0.05, xname: Incomplete | None = None):
        """summary table for probability that random draw x1 is larger than x2

        Parameters
        ----------
        alpha : float
            Significance level for confidence intervals. Coverage is 1 - alpha
        xname : None or list of str
            If None, then each row has a name column with generic names.
            If xname is a list of strings, then it will be included as part
            of those names.

        Returns
        -------
        SimpleTable instance with methods to convert to different output
        formats.
        """

def rank_compare_2indep(x1, x2, use_t: bool = True):
    '''
    Statistics and tests for the probability that x1 has larger values than x2.

    p is the probability that a random draw from the population of
    the first sample has a larger value than a random draw from the
    population of the second sample, specifically

            p = P(x1 > x2) + 0.5 * P(x1 = x2)

    This is a measure underlying Wilcoxon-Mann-Whitney\'s U test,
    Fligner-Policello test and Brunner-Munzel test, and
    Inference is based on the asymptotic distribution of the Brunner-Munzel
    test. The half probability for ties corresponds to the use of midranks
    and make it valid for discrete variables.

    The Null hypothesis for stochastic equality is p = 0.5, which corresponds
    to the Brunner-Munzel test.

    Parameters
    ----------
    x1, x2 : array_like
        Array of samples, should be one-dimensional.
    use_t : boolean
        If use_t is true, the t distribution with Welch-Satterthwaite type
        degrees of freedom is used for p-value and confidence interval.
        If use_t is false, then the normal distribution is used.

    Returns
    -------
    res : RankCompareResult
        The results instance contains the results for the Brunner-Munzel test
        and has methods for hypothesis tests, confidence intervals and summary.

        statistic : float
            The Brunner-Munzel W statistic.
        pvalue : float
            p-value assuming an t distribution. One-sided or
            two-sided, depending on the choice of `alternative` and `use_t`.

    See Also
    --------
    RankCompareResult
    scipy.stats.brunnermunzel : Brunner-Munzel test for stochastic equality
    scipy.stats.mannwhitneyu : Mann-Whitney rank test on two samples.

    Notes
    -----
    Wilcoxon-Mann-Whitney assumes equal variance or equal distribution under
    the Null hypothesis. Fligner-Policello test allows for unequal variances
    but assumes continuous distribution, i.e. no ties.
    Brunner-Munzel extend the test to allow for unequal variance and discrete
    or ordered categorical random variables.

    Brunner and Munzel recommended to estimate the p-value by t-distribution
    when the size of data is 50 or less. If the size is lower than 10, it would
    be better to use permuted Brunner Munzel test (see [2]_) for the test
    of stochastic equality.

    This measure has been introduced in the literature under many different
    names relying on a variety of assumptions.
    In psychology, McGraw and Wong (1992) introduced it as Common Language
    effect size for the continuous, normal distribution case,
    Vargha and Delaney (2000) [3]_ extended it to the nonparametric
    continuous distribution case as in Fligner-Policello.

    WMW and related tests can only be interpreted as test of medians or tests
    of central location only under very restrictive additional assumptions
    such as both distribution are identical under the equality null hypothesis
    (assumed by Mann-Whitney) or both distributions are symmetric (shown by
    Fligner-Policello). If the distribution of the two samples can differ in
    an arbitrary way, then the equality Null hypothesis corresponds to p=0.5
    against an alternative p != 0.5.  see for example Conroy (2012) [4]_ and
    Divine et al (2018) [5]_ .

    Note: Brunner-Munzel and related literature define the probability that x1
    is stochastically smaller than x2, while here we use stochastically larger.
    This equivalent to switching x1 and x2 in the two sample case.

    References
    ----------
    .. [1] Brunner, E. and Munzel, U. "The nonparametric Benhrens-Fisher
           problem: Asymptotic theory and a small-sample approximation".
           Biometrical Journal. Vol. 42(2000): 17-25.
    .. [2] Neubert, K. and Brunner, E. "A studentized permutation test for the
           non-parametric Behrens-Fisher problem". Computational Statistics and
           Data Analysis. Vol. 51(2007): 5192-5204.
    .. [3] Vargha, András, and Harold D. Delaney. 2000. “A Critique and
           Improvement of the CL Common Language Effect Size Statistics of
           McGraw and Wong.” Journal of Educational and Behavioral Statistics
           25 (2): 101–32. https://doi.org/10.3102/10769986025002101.
    .. [4] Conroy, Ronán M. 2012. “What Hypotheses Do ‘Nonparametric’ Two-Group
           Tests Actually Test?” The Stata Journal: Promoting Communications on
           Statistics and Stata 12 (2): 182–90.
           https://doi.org/10.1177/1536867X1201200202.
    .. [5] Divine, George W., H. James Norton, Anna E. Barón, and Elizabeth
           Juarez-Colunga. 2018. “The Wilcoxon–Mann–Whitney Procedure Fails as
           a Test of Medians.” The American Statistician 72 (3): 278–86.
           https://doi.org/10.1080/00031305.2017.1305291.

    '''
def rank_compare_2ordinal(count1, count2, ddof: int = 1, use_t: bool = True):
    """
    Stochastically larger probability for 2 independent ordinal samples.

    This is a special case of `rank_compare_2indep` when the data are given as
    counts of two independent ordinal, i.e. ordered multinomial, samples.

    The statistic of interest is the probability that a random draw from the
    population of the first sample has a larger value than a random draw from
    the population of the second sample, specifically

        p = P(x1 > x2) + 0.5 * P(x1 = x2)

    Parameters
    ----------
    count1 : array_like
        Counts of the first sample, categories are assumed to be ordered.
    count2 : array_like
        Counts of the second sample, number of categories and ordering needs
        to be the same as for sample 1.
    ddof : scalar
        Degrees of freedom correction for variance estimation. The default
        ddof=1 corresponds to `rank_compare_2indep`.
    use_t : bool
        If use_t is true, the t distribution with Welch-Satterthwaite type
        degrees of freedom is used for p-value and confidence interval.
        If use_t is false, then the normal distribution is used.

    Returns
    -------
    res : RankCompareResult
        This includes methods for hypothesis tests and confidence intervals
        for the probability that sample 1 is stochastically larger than
        sample 2.

    See Also
    --------
    rank_compare_2indep
    RankCompareResult

    Notes
    -----
    The implementation is based on the appendix of Munzel and Hauschke (2003)
    with the addition of ``ddof`` so that the results match the general
    function `rank_compare_2indep`.

    """
def prob_larger_continuous(distr1, distr2):
    """
    Probability indicating that distr1 is stochastically larger than distr2.

    This computes

        p = P(x1 > x2)

    for two continuous distributions, where `distr1` and `distr2` are the
    distributions of random variables x1 and x2 respectively.

    Parameters
    ----------
    distr1, distr2 : distributions
        Two instances of scipy.stats.distributions. The required methods are
        cdf of the second distribution and expect of the first distribution.

    Returns
    -------
    p : probability x1 is larger than x2


    Notes
    -----
    This is a one-liner that is added mainly as reference.

    Examples
    --------
    >>> from scipy import stats
    >>> prob_larger_continuous(stats.norm, stats.t(5))
    0.4999999999999999

    # which is the same as
    >>> stats.norm.expect(stats.t(5).cdf)
    0.4999999999999999

    # distribution 1 with smaller mean (loc) than distribution 2
    >>> prob_larger_continuous(stats.norm, stats.norm(loc=1))
    0.23975006109347669

    """
def cohensd2problarger(d):
    """
    Convert Cohen's d effect size to stochastically-larger-probability.

    This assumes observations are normally distributed.

    Computed as

        p = Prob(x1 > x2) = F(d / sqrt(2))

    where `F` is cdf of normal distribution. Cohen's d is defined as

        d = (mean1 - mean2) / std

    where ``std`` is the pooled within standard deviation.

    Parameters
    ----------
    d : float or array_like
        Cohen's d effect size for difference mean1 - mean2.

    Returns
    -------
    prob : float or ndarray
        Prob(x1 > x2)
    """
