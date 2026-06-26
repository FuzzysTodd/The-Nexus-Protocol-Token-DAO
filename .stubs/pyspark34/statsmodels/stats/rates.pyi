from _typeshed import Incomplete
from statsmodels.stats.base import HolderTuple as HolderTuple

norm: Incomplete
method_names_poisson_1samp: Incomplete

def test_poisson(count, nobs, value, method: Incomplete | None = None, alternative: str = 'two-sided', dispersion: int = 1):
    '''Test for one sample poisson mean or rate

    Parameters
    ----------
    count : array_like
        Observed count, number of events.
    nobs : arrat_like
        Currently this is total exposure time of the count variable.
        This will likely change.
    value : float, array_like
        This is the value of poisson rate under the null hypothesis.
    method : str
        Method to use for confidence interval.
        This is required, there is currently no default method.
        See Notes for available methods.
    alternative : {\'two-sided\', \'smaller\', \'larger\'}
        alternative hypothesis, which can be two-sided or either one of the
        one-sided tests.
    dispersion : float
        Dispersion scale coefficient for Poisson QMLE. Default is that the
        data follows a Poisson distribution. Dispersion different from 1
        correspond to excess-dispersion in Poisson quasi-likelihood (GLM).
        Dispersion coeffficient different from one is currently only used in
        wald and score method.

    Returns
    -------
    HolderTuple instance with test statistic, pvalue and other attributes.

    Notes
    -----
    The implementatio of the hypothesis test is mainly based on the references
    for the confidence interval, see confint_poisson.

    Available methods are:

    - "score" : based on score test, uses variance under null value
    - "wald" : based on wald test, uses variance base on estimated rate.
    - "waldccv" : based on wald test with 0.5 count added to variance
      computation. This does not use continuity correction for the center of
      the confidence interval.
    - "exact-c" central confidence interval based on gamma distribution
    - "midp-c" : based on midp correction of central exact confidence interval.
      this uses numerical inversion of the test function. not vectorized.
    - "sqrt" : based on square root transformed counts
    - "sqrt-a" based on Anscombe square root transformation of counts + 3/8.

    See Also
    --------
    confint_poisson

    '''
def confint_poisson(count, exposure, method: Incomplete | None = None, alpha: float = 0.05):
    '''Confidence interval for a Poisson mean or rate

    The function is vectorized for all methods except "midp-c", which uses
    an iterative method to invert the hypothesis test function.

    All current methods are central, that is the probability of each tail is
    smaller or equal to alpha / 2. The one-sided interval limits can be
    obtained by doubling alpha.

    Parameters
    ----------
    count : array_like
        Observed count, number of events.
    exposure : arrat_like
        Currently this is total exposure time of the count variable.
        This will likely change.
    method : str
        Method to use for confidence interval
        This is required, there is currently no default method
    alpha : float in (0, 1)
        Significance level, nominal coverage of the confidence interval is
        1 - alpha.

    Returns
    -------
    tuple (low, upp) : confidence limits.

    Notes
    -----
    Methods are mainly based on Barker (2002) [1]_ and Swift (2009) [3]_.

    Available methods are:

    - "exact-c" central confidence interval based on gamma distribution
    - "score" : based on score test, uses variance under null value
    - "wald" : based on wald test, uses variance base on estimated rate.
    - "waldccv" : based on wald test with 0.5 count added to variance
      computation. This does not use continuity correction for the center of
      the confidence interval.
    - "midp-c" : based on midp correction of central exact confidence interval.
      this uses numerical inversion of the test function. not vectorized.
    - "jeffreys" : based on Jeffreys\' prior. computed using gamma distribution
    - "sqrt" : based on square root transformed counts
    - "sqrt-a" based on Anscombe square root transformation of counts + 3/8.
    - "sqrt-centcc" will likely be dropped. anscombe with continuity corrected
      center.
      (Similar to R survival cipoisson, but without the 3/8 right shift of
      the confidence interval).

    sqrt-cent is the same as sqrt-a, using a different computation, will be
    deleted.

    sqrt-v is a corrected square root method attributed to vandenbrouke, which
    might also be deleted.

    Todo:

    - missing dispersion,
    - maybe split nobs and exposure (? needed in NB). Exposure could be used
      to standardize rate.
    - modified wald, switch method if count=0.

    See Also
    --------
    test_poisson

    References
    ----------
    .. [1] Barker, Lawrence. 2002. “A Comparison of Nine Confidence Intervals
       for a Poisson Parameter When the Expected Number of Events Is ≤ 5.”
       The American Statistician 56 (2): 85–89.
       https://doi.org/10.1198/000313002317572736.
    .. [2] Patil, VV, and HV Kulkarni. 2012. “Comparison of Confidence
       Intervals for the Poisson Mean: Some New Aspects.”
       REVSTAT–Statistical Journal 10(2): 211–27.
    .. [3] Swift, Michael Bruce. 2009. “Comparison of Confidence Intervals for
       a Poisson Mean – Further Considerations.” Communications in Statistics -
       Theory and Methods 38 (5): 748–59.
       https://doi.org/10.1080/03610920802255856.

    '''
def tolerance_int_poisson(count, exposure, prob: float = 0.95, exposure_new: float = 1.0, method: Incomplete | None = None, alpha: float = 0.05, alternative: str = 'two-sided'):
    '''tolerance interval for a poisson observation

    Parameters
    ----------
    count : array_like
        Observed count, number of events.
    exposure : arrat_like
        Currently this is total exposure time of the count variable.
    prob : float in (0, 1)
        Probability of poisson interval, often called "content".
        With known parameters, each tail would have at most probability
        ``1 - prob / 2`` in the two-sided interval.
    exposure_new : float
        Exposure of the new or predicted observation.
    method : str
        Method to used for confidence interval of the estimate of the
        poisson rate, used in `confint_poisson`.
        This is required, there is currently no default method.
    alpha : float in (0, 1)
        Significance level for the confidence interval of the estimate of the
        Poisson rate. Nominal coverage of the confidence interval is
        1 - alpha.
    alternative : {"two-sider", "larger", "smaller")
        The tolerance interval can be two-sided or one-sided.
        Alternative "larger" provides the upper bound of the confidence
        interval, larger counts are outside the interval.

    Returns
    -------
    tuple (low, upp) of limits of tolerance interval.
        The tolerance interval is a closed interval, that is both ``low`` and
        ``upp`` are in the interval.

    Notes
    -----
    verified against R package tolerance `poistol.int`

    See Also
    --------
    confint_poisson
    confint_quantile_poisson

    References
    ----------
    .. [1] Hahn, Gerald J., and William Q. Meeker. 1991. Statistical Intervals:
       A Guide for Practitioners. 1st ed. Wiley Series in Probability and
       Statistics. Wiley. https://doi.org/10.1002/9780470316771.
    .. [2] Hahn, Gerald J., and Ramesh Chandra. 1981. “Tolerance Intervals for
       Poisson and Binomial Variables.” Journal of Quality Technology 13 (2):
       100–110. https://doi.org/10.1080/00224065.1981.11980998.

    '''
def confint_quantile_poisson(count, exposure, prob, exposure_new: float = 1.0, method: Incomplete | None = None, alpha: float = 0.05, alternative: str = 'two-sided'):
    '''confidence interval for quantile of poisson random variable

    Parameters
    ----------
    count : array_like
        Observed count, number of events.
    exposure : arrat_like
        Currently this is total exposure time of the count variable.
    prob : float in (0, 1)
        Probability for the quantile, e.g. 0.95 to get the upper 95% quantile.
        With known mean mu, the quantile would be poisson.ppf(prob, mu).
    exposure_new : float
        Exposure of the new or predicted observation.
    method : str
        Method to used for confidence interval of the estimate of the
        poisson rate, used in `confint_poisson`.
        This is required, there is currently no default method.
    alpha : float in (0, 1)
        Significance level for the confidence interval of the estimate of the
        Poisson rate. Nominal coverage of the confidence interval is
        1 - alpha.
    alternative : {"two-sider", "larger", "smaller")
        The tolerance interval can be two-sided or one-sided.
        Alternative "larger" provides the upper bound of the confidence
        interval, larger counts are outside the interval.

    Returns
    -------
    tuple (low, upp) of limits of tolerance interval.
    The confidence interval is a closed interval, that is both ``low`` and
    ``upp`` are in the interval.

    See Also
    --------
    confint_poisson
    tolerance_int_poisson

    References
    ----------
    Hahn, Gerald J, and William Q Meeker. 2010. Statistical Intervals: A Guide
    for Practitioners.
    '''

method_names_poisson_2indep: Incomplete

def test_poisson_2indep(count1, exposure1, count2, exposure2, value: Incomplete | None = None, ratio_null: Incomplete | None = None, method: Incomplete | None = None, compare: str = 'ratio', alternative: str = 'two-sided', etest_kwds: Incomplete | None = None):
    '''Test for comparing two sample Poisson intensity rates.

    Rates are defined as expected count divided by exposure.

    The Null and alternative hypothesis for the rates, rate1 and rate2, of two
    independent Poisson samples are

    for compare = \'diff\'

    - H0: rate1 - rate2 - value = 0
    - H1: rate1 - rate2 - value != 0  if alternative = \'two-sided\'
    - H1: rate1 - rate2 - value > 0   if alternative = \'larger\'
    - H1: rate1 - rate2 - value < 0   if alternative = \'smaller\'

    for compare = \'ratio\'

    - H0: rate1 / rate2 - value = 0
    - H1: rate1 / rate2 - value != 0  if alternative = \'two-sided\'
    - H1: rate1 / rate2 - value > 0   if alternative = \'larger\'
    - H1: rate1 / rate2 - value < 0   if alternative = \'smaller\'

    Parameters
    ----------
    count1 : int
        Number of events in first sample, treatment group.
    exposure1 : float
        Total exposure (time * subjects) in first sample.
    count2 : int
        Number of events in second sample, control group.
    exposure2 : float
        Total exposure (time * subjects) in second sample.
    ratio_null: float
        Ratio of the two Poisson rates under the Null hypothesis. Default is 1.
        Deprecated, use ``value`` instead.

        .. deprecated:: 0.14.0

            Use ``value`` instead.

    value : float
        Value of the ratio or difference of 2 independent rates under the null
        hypothesis. Default is equal rates, i.e. 1 for ratio and 0 for diff.

        .. versionadded:: 0.14.0

            Replacement for ``ratio_null``.

    method : string
        Method for the test statistic and the p-value. Defaults to `\'score\'`.
        see Notes.

        ratio:

        - \'wald\': method W1A, wald test, variance based on observed rates
        - \'score\': method W2A, score test, variance based on estimate under
          the Null hypothesis
        - \'wald-log\': W3A, uses log-ratio, variance based on observed rates
        - \'score-log\' W4A, uses log-ratio, variance based on estimate under
          the Null hypothesis
        - \'sqrt\': W5A, based on variance stabilizing square root transformation
        - \'exact-cond\': exact conditional test based on binomial distribution
           This uses ``binom_test`` which is minlike in the two-sided case.
        - \'cond-midp\': midpoint-pvalue of exact conditional test
        - \'etest\' or \'etest-score: etest with score test statistic
        - \'etest-wald\': etest with wald test statistic

        diff:

        - \'wald\',
        - \'waldccv\'
        - \'score\'
        - \'etest-score\' or \'etest: etest with score test statistic
        - \'etest-wald\': etest with wald test statistic

    compare : {\'diff\', \'ratio\'}
        Default is "ratio".
        If compare is `ratio`, then the hypothesis test is for the
        rate ratio defined by ratio = rate1 / rate2.
        If compare is `diff`, then the hypothesis test is for
        diff = rate1 - rate2.
    alternative : {"two-sided" (default), "larger", smaller}
        The alternative hypothesis, H1, has to be one of the following

        - \'two-sided\': H1: ratio, or diff, of rates is not equal to value
        - \'larger\' :   H1: ratio, or diff, of rates is larger than value
        - \'smaller\' :  H1: ratio, or diff, of rates is smaller than value
    etest_kwds: dictionary
        Additional optional parameters to be passed to the etest_poisson_2indep
        function, namely y_grid.

    Returns
    -------
    results : instance of HolderTuple class
        The two main attributes are test statistic `statistic` and p-value
        `pvalue`.

    See Also
    --------
    tost_poisson_2indep
    etest_poisson_2indep

    Notes
    -----
    The hypothesis tests for compare="ratio" are based on Gu et al 2018.
    The e-tests are also based on ...

    - \'wald\': method W1A, wald test, variance based on separate estimates
    - \'score\': method W2A, score test, variance based on estimate under Null
    - \'wald-log\': W3A, wald test for log transformed ratio
    - \'score-log\' W4A, score test for log transformed ratio
    - \'sqrt\': W5A, based on variance stabilizing square root transformation
    - \'exact-cond\': exact conditional test based on binomial distribution
    - \'cond-midp\': midpoint-pvalue of exact conditional test
    - \'etest\': etest with score test statistic
    - \'etest-wald\': etest with wald test statistic

    The hypothesis test for compare="diff" are mainly based on Ng et al 2007
    and ...

    - wald
    - score
    - etest-score
    - etest-wald

    Note the etests use the constraint maximum likelihood estimate (cmle) as
    parameters for the underlying Poisson probabilities. The constraint cmle
    parameters are the same as in the score test.
    The E-test in Krishnamoorty and Thomson uses a moment estimator instead of
    the score estimator.

    References
    ----------
    .. [1] Gu, Ng, Tang, Schucany 2008: Testing the Ratio of Two Poisson Rates,
       Biometrical Journal 50 (2008) 2, 2008

    .. [2] Ng, H. K. T., K. Gu, and M. L. Tang. 2007. “A Comparative Study of
       Tests for the Difference of Two Poisson Means.”
       Computational Statistics & Data Analysis 51 (6): 3085–99.
       https://doi.org/10.1016/j.csda.2006.02.004.

    '''
def etest_poisson_2indep(count1, exposure1, count2, exposure2, ratio_null: Incomplete | None = None, value: Incomplete | None = None, method: str = 'score', compare: str = 'ratio', alternative: str = 'two-sided', ygrid: Incomplete | None = None, y_grid: Incomplete | None = None):
    '''
    E-test for ratio of two sample Poisson rates.

    Rates are defined as expected count divided by exposure. The Null and
    alternative hypothesis for the rates, rate1 and rate2, of two independent
    Poisson samples are:

    for compare = \'diff\'

    - H0: rate1 - rate2 - value = 0
    - H1: rate1 - rate2 - value != 0  if alternative = \'two-sided\'
    - H1: rate1 - rate2 - value > 0   if alternative = \'larger\'
    - H1: rate1 - rate2 - value < 0   if alternative = \'smaller\'

    for compare = \'ratio\'

    - H0: rate1 / rate2 - value = 0
    - H1: rate1 / rate2 - value != 0  if alternative = \'two-sided\'
    - H1: rate1 / rate2 - value > 0   if alternative = \'larger\'
    - H1: rate1 / rate2 - value < 0   if alternative = \'smaller\'

    Parameters
    ----------
    count1 : int
        Number of events in first sample
    exposure1 : float
        Total exposure (time * subjects) in first sample
    count2 : int
        Number of events in first sample
    exposure2 : float
        Total exposure (time * subjects) in first sample
    ratio_null: float
        Ratio of the two Poisson rates under the Null hypothesis. Default is 1.
        Deprecated, use ``value`` instead.

        .. deprecated:: 0.14.0

            Use ``value`` instead.

    value : float
        Value of the ratio or diff of 2 independent rates under the null
        hypothesis. Default is equal rates, i.e. 1 for ratio and 0 for diff.

        .. versionadded:: 0.14.0

            Replacement for ``ratio_null``.

    method : {"score", "wald"}
        Method for the test statistic that defines the rejection region.
    alternative : string
        The alternative hypothesis, H1, has to be one of the following

        - \'two-sided\': H1: ratio of rates is not equal to ratio_null (default)
        - \'larger\' :   H1: ratio of rates is larger than ratio_null
        - \'smaller\' :  H1: ratio of rates is smaller than ratio_null

    y_grid : None or 1-D ndarray
        Grid values for counts of the Poisson distribution used for computing
        the pvalue. By default truncation is based on an upper tail Poisson
        quantiles.

    ygrid : None or 1-D ndarray
        Same as y_grid. Deprecated. If both y_grid and ygrid are provided,
        ygrid will be ignored.

        .. deprecated:: 0.14.0

            Use ``y_grid`` instead.

    Returns
    -------
    stat_sample : float
        test statistic for the sample
    pvalue : float

    References
    ----------
    Gu, Ng, Tang, Schucany 2008: Testing the Ratio of Two Poisson Rates,
    Biometrical Journal 50 (2008) 2, 2008
    Ng, H. K. T., K. Gu, and M. L. Tang. 2007. “A Comparative Study of Tests
    for the Difference of Two Poisson Means.” Computational Statistics & Data
    Analysis 51 (6): 3085–99. https://doi.org/10.1016/j.csda.2006.02.004.

    '''
def tost_poisson_2indep(count1, exposure1, count2, exposure2, low, upp, method: str = 'score', compare: str = 'ratio'):
    """Equivalence test based on two one-sided `test_proportions_2indep`

    This assumes that we have two independent poisson samples.

    The Null and alternative hypothesis for equivalence testing are

    for compare = 'ratio'

    - H0: rate1 / rate2 <= low or upp <= rate1 / rate2
    - H1: low < rate1 / rate2 < upp

    for compare = 'diff'

    - H0: rate1 - rate2 <= low or upp <= rate1 - rate2
    - H1: low < rate - rate < upp

    Parameters
    ----------
    count1 : int
        Number of events in first sample
    exposure1 : float
        Total exposure (time * subjects) in first sample
    count2 : int
        Number of events in second sample
    exposure2 : float
        Total exposure (time * subjects) in second sample
    low, upp :
        equivalence margin for the ratio or difference of Poisson rates
    method: string
        TOST uses ``test_poisson_2indep`` and has the same methods.

        ratio:

        - 'wald': method W1A, wald test, variance based on observed rates
        - 'score': method W2A, score test, variance based on estimate under
          the Null hypothesis
        - 'wald-log': W3A, uses log-ratio, variance based on observed rates
        - 'score-log' W4A, uses log-ratio, variance based on estimate under
          the Null hypothesis
        - 'sqrt': W5A, based on variance stabilizing square root transformation
        - 'exact-cond': exact conditional test based on binomial distribution
           This uses ``binom_test`` which is minlike in the two-sided case.
        - 'cond-midp': midpoint-pvalue of exact conditional test
        - 'etest' or 'etest-score: etest with score test statistic
        - 'etest-wald': etest with wald test statistic

        diff:

        - 'wald',
        - 'waldccv'
        - 'score'
        - 'etest-score' or 'etest: etest with score test statistic
        - 'etest-wald': etest with wald test statistic

    Returns
    -------
    results : instance of HolderTuple class
        The two main attributes are test statistic `statistic` and p-value
        `pvalue`.

    References
    ----------
    Gu, Ng, Tang, Schucany 2008: Testing the Ratio of Two Poisson Rates,
    Biometrical Journal 50 (2008) 2, 2008

    See Also
    --------
    test_poisson_2indep
    confint_poisson_2indep
    """
def nonequivalence_poisson_2indep(count1, exposure1, count2, exposure2, low, upp, method: str = 'score', compare: str = 'ratio'):
    """Test for non-equivalence, minimum effect for poisson.

    This reverses null and alternative hypothesis compared to equivalence
    testing. The null hypothesis is that the effect, ratio (or diff), is in
    an interval that specifies a range of irrelevant or unimportant
    differences between the two samples.

    The Null and alternative hypothesis comparing the ratio of rates are

    for compare = 'ratio':

    - H0: low < rate1 / rate2 < upp
    - H1: rate1 / rate2 <= low or upp <= rate1 / rate2

    for compare = 'diff':

    - H0: rate1 - rate2 <= low or upp <= rate1 - rate2
    - H1: low < rate - rate < upp


    Notes
    -----
    This is implemented as two one-sided tests at the minimum effect boundaries
    (low, upp) with (nominal) size alpha / 2 each.
    The size of the test is the sum of the two one-tailed tests, which
    corresponds to an equal-tailed two-sided test.
    If low and upp are equal, then the result is the same as the standard
    two-sided test.

    The p-value is computed as `2 * min(pvalue_low, pvalue_upp)` in analogy to
    two-sided equal-tail tests.

    In large samples the nominal size of the test will be below alpha.

    References
    ----------
    .. [1] Hodges, J. L., Jr., and E. L. Lehmann. 1954. Testing the Approximate
       Validity of Statistical Hypotheses. Journal of the Royal Statistical
       Society, Series B (Methodological) 16: 261–68.

    .. [2] Kim, Jae H., and Andrew P. Robinson. 2019. “Interval-Based
       Hypothesis Testing and Its Applications to Economics and Finance.”
       Econometrics 7 (2): 21. https://doi.org/10.3390/econometrics7020021.

    """
def confint_poisson_2indep(count1, exposure1, count2, exposure2, method: str = 'score', compare: str = 'ratio', alpha: float = 0.05, method_mover: str = 'score'):
    '''Confidence interval for ratio or difference of 2 indep poisson rates.

    Parameters
    ----------
    count1 : int
        Number of events in first sample.
    exposure1 : float
        Total exposure (time * subjects) in first sample.
    count2 : int
        Number of events in second sample.
    exposure2 : float
        Total exposure (time * subjects) in second sample.
    method : string
        Method for the test statistic and the p-value. Defaults to `\'score\'`.
        see Notes.

        ratio:

        - \'wald\': NOT YET, method W1A, wald test, variance based on observed
          rates
        - \'waldcc\' :
        - \'score\': method W2A, score test, variance based on estimate under
          the Null hypothesis
        - \'wald-log\': W3A, uses log-ratio, variance based on observed rates
        - \'score-log\' W4A, uses log-ratio, variance based on estimate under
          the Null hypothesis
        - \'sqrt\': W5A, based on variance stabilizing square root transformation
        - \'sqrtcc\' :
        - \'exact-cond\': NOT YET, exact conditional test based on binomial
          distribution
          This uses ``binom_test`` which is minlike in the two-sided case.
        - \'cond-midp\': NOT YET, midpoint-pvalue of exact conditional test
        - \'mover\' :

        diff:

        - \'wald\',
        - \'waldccv\'
        - \'score\'
        - \'mover\'

    compare : {\'diff\', \'ratio\'}
        Default is "ratio".
        If compare is `diff`, then the hypothesis test is for
        diff = rate1 - rate2.
        If compare is `ratio`, then the hypothesis test is for the
        rate ratio defined by ratio = rate1 / rate2.
    alternative : string
        The alternative hypothesis, H1, has to be one of the following

        - \'two-sided\': H1: ratio of rates is not equal to ratio_null (default)
        - \'larger\' :   H1: ratio of rates is larger than ratio_null
        - \'smaller\' :  H1: ratio of rates is smaller than ratio_null

    alpha : float in (0, 1)
        Significance level, nominal coverage of the confidence interval is
        1 - alpha.

    Returns
    -------
    tuple (low, upp) : confidence limits.

    '''
def power_poisson_ratio_2indep(rate1, rate2, nobs1, nobs_ratio: int = 1, exposure: int = 1, value: int = 0, alpha: float = 0.05, dispersion: int = 1, alternative: str = 'smaller', method_var: str = 'alt', return_results: bool = True):
    '''Power of test of ratio of 2 independent poisson rates.

    This is based on Zhu and Zhu and Lakkis. It does not directly correspond
    to `test_poisson_2indep`.

    Parameters
    ----------
    rate1 : float
        Poisson rate for the first sample, treatment group, under the
        alternative hypothesis.
    rate2 : float
        Poisson rate for the second sample, reference group, under the
        alternative hypothesis.
    nobs1 : float or int
        Number of observations in sample 1.
    nobs_ratio : float
        Sample size ratio, nobs2 = nobs_ratio * nobs1.
    exposure : float
        Exposure for each observation. Total exposure is nobs1 * exposure
        and nobs2 * exposure.
    alpha : float in interval (0,1)
        Significance level, e.g. 0.05, is the probability of a type I
        error, that is wrong rejections if the Null Hypothesis is true.
    value : float
        Rate ratio, rate1 / rate2, under the null hypothesis.
    dispersion : float
        Dispersion coefficient for quasi-Poisson. Dispersion different from
        one can capture over or under dispersion relative to Poisson
        distribution.
    method_var : {"score", "alt"}
        The variance of the test statistic for the null hypothesis given the
        rates under the alternative can be either equal to the rates under the
        alternative ``method_var="alt"``, or estimated under the constrained
        of the null hypothesis, ``method_var="score"``.
    alternative : string, \'two-sided\' (default), \'larger\', \'smaller\'
        Alternative hypothesis whether the power is calculated for a
        two-sided (default) or one sided test. The one-sided test can be
        either \'larger\', \'smaller\'.
    return_results : bool
        If true, then a results instance with extra information is returned,
        otherwise only the computed power is returned.

    Returns
    -------
    results : results instance or float
        If return_results is False, then only the power is returned.
        If return_results is True, then a results instance with the
        information in attributes is returned.

        power : float
            Power of the test, e.g. 0.8, is one minus the probability of a
            type II error. Power is the probability that the test correctly
            rejects the Null Hypothesis if the Alternative Hypothesis is true.

        Other attributes in results instance include :

        std_null
            standard error of difference under the null hypothesis (without
            sqrt(nobs1))
        std_alt
            standard error of difference under the alternative hypothesis
            (without sqrt(nobs1))

    References
    ----------
    .. [1] Zhu, Haiyuan. 2017. “Sample Size Calculation for Comparing Two
       Poisson or Negative Binomial Rates in Noninferiority or Equivalence
       Trials.” Statistics in Biopharmaceutical Research, March.
       https://doi.org/10.1080/19466315.2016.1225594
    .. [2] Zhu, Haiyuan, and Hassan Lakkis. 2014. “Sample Size Calculation for
       Comparing Two Negative Binomial Rates.” Statistics in Medicine 33 (3):
       376–87. https://doi.org/10.1002/sim.5947.
    .. [3] PASS documentation
    '''
def power_equivalence_poisson_2indep(rate1, rate2, nobs1, low, upp, nobs_ratio: int = 1, exposure: int = 1, alpha: float = 0.05, dispersion: int = 1, method_var: str = 'alt', return_results: bool = False):
    '''Power of equivalence test of ratio of 2 independent poisson rates.

    Parameters
    ----------
    rate1 : float
        Poisson rate for the first sample, treatment group, under the
        alternative hypothesis.
    rate2 : float
        Poisson rate for the second sample, reference group, under the
        alternative hypothesis.
    nobs1 : float or int
        Number of observations in sample 1.
    low : float
        Lower equivalence margin for the rate ratio, rate1 / rate2.
    upp : float
        Upper equivalence margin for the rate ratio, rate1 / rate2.
    nobs_ratio : float
        Sample size ratio, nobs2 = nobs_ratio * nobs1.
    exposure : float
        Exposure for each observation. Total exposure is nobs1 * exposure
        and nobs2 * exposure.
    alpha : float in interval (0,1)
        Significance level, e.g. 0.05, is the probability of a type I
        error, that is wrong rejections if the Null Hypothesis is true.
    value : float
        Difference between rates 1 and 2 under the null hypothesis.
    method_var : {"score", "alt"}
        The variance of the test statistic for the null hypothesis given the
        rates uder the alternative, can be either equal to the rates under the
        alternative ``method_var="alt"``, or estimated under the constrained
        of the null hypothesis, ``method_var="score"``.
    alternative : string, \'two-sided\' (default), \'larger\', \'smaller\'
        Alternative hypothesis whether the power is calculated for a
        two-sided (default) or one sided test. The one-sided test can be
        either \'larger\', \'smaller\'.
    return_results : bool
        If true, then a results instance with extra information is returned,
        otherwise only the computed power is returned.

    Returns
    -------
    results : results instance or float
        If return_results is False, then only the power is returned.
        If return_results is True, then a results instance with the
        information in attributes is returned.

        power : float
            Power of the test, e.g. 0.8, is one minus the probability of a
            type II error. Power is the probability that the test correctly
            rejects the Null Hypothesis if the Alternative Hypothesis is true.

        Other attributes in results instance include :

        std_null
            standard error of difference under the null hypothesis (without
            sqrt(nobs1))
        std_alt
            standard error of difference under the alternative hypothesis
            (without sqrt(nobs1))

    References
    ----------
    .. [1] Zhu, Haiyuan. 2017. “Sample Size Calculation for Comparing Two
       Poisson or Negative Binomial Rates in Noninferiority or Equivalence
       Trials.” Statistics in Biopharmaceutical Research, March.
       https://doi.org/10.1080/19466315.2016.1225594
    .. [2] Zhu, Haiyuan, and Hassan Lakkis. 2014. “Sample Size Calculation for
       Comparing Two Negative Binomial Rates.” Statistics in Medicine 33 (3):
       376–87. https://doi.org/10.1002/sim.5947.
    .. [3] PASS documentation
    '''
def power_poisson_diff_2indep(rate1, rate2, nobs1, nobs_ratio: int = 1, alpha: float = 0.05, value: int = 0, method_var: str = 'score', alternative: str = 'two-sided', return_results: bool = True):
    '''Power of ztest for the difference between two independent poisson rates.

    Parameters
    ----------
    rate1 : float
        Poisson rate for the first sample, treatment group, under the
        alternative hypothesis.
    rate2 : float
        Poisson rate for the second sample, reference group, under the
        alternative hypothesis.
    nobs1 : float or int
        Number of observations in sample 1.
    nobs_ratio : float
        Sample size ratio, nobs2 = nobs_ratio * nobs1.
    alpha : float in interval (0,1)
        Significance level, e.g. 0.05, is the probability of a type I
        error, that is wrong rejections if the Null Hypothesis is true.
    value : float
        Difference between rates 1 and 2 under the null hypothesis.
    method_var : {"score", "alt"}
        The variance of the test statistic for the null hypothesis given the
        rates uder the alternative, can be either equal to the rates under the
        alternative ``method_var="alt"``, or estimated under the constrained
        of the null hypothesis, ``method_var="score"``.
    alternative : string, \'two-sided\' (default), \'larger\', \'smaller\'
        Alternative hypothesis whether the power is calculated for a
        two-sided (default) or one sided test. The one-sided test can be
        either \'larger\', \'smaller\'.
    return_results : bool
        If true, then a results instance with extra information is returned,
        otherwise only the computed power is returned.

    Returns
    -------
    results : results instance or float
        If return_results is False, then only the power is returned.
        If return_results is True, then a results instance with the
        information in attributes is returned.

        power : float
            Power of the test, e.g. 0.8, is one minus the probability of a
            type II error. Power is the probability that the test correctly
            rejects the Null Hypothesis if the Alternative Hypothesis is true.

        Other attributes in results instance include :

        std_null
            standard error of difference under the null hypothesis (without
            sqrt(nobs1))
        std_alt
            standard error of difference under the alternative hypothesis
            (without sqrt(nobs1))

    References
    ----------
    .. [1] Stucke, Kathrin, and Meinhard Kieser. 2013. “Sample Size
       Calculations for Noninferiority Trials with Poisson Distributed Count
       Data.” Biometrical Journal 55 (2): 203–16.
       https://doi.org/10.1002/bimj.201200142.
    .. [2] PASS manual chapter 436

    '''
def power_negbin_ratio_2indep(rate1, rate2, nobs1, nobs_ratio: int = 1, exposure: int = 1, value: int = 1, alpha: float = 0.05, dispersion: float = 0.01, alternative: str = 'two-sided', method_var: str = 'alt', return_results: bool = True):
    '''
    Power of test of ratio of 2 independent negative binomial rates.

    Parameters
    ----------
    rate1 : float
        Poisson rate for the first sample, treatment group, under the
        alternative hypothesis.
    rate2 : float
        Poisson rate for the second sample, reference group, under the
        alternative hypothesis.
    nobs1 : float or int
        Number of observations in sample 1.
    low : float
        Lower equivalence margin for the rate ratio, rate1 / rate2.
    upp : float
        Upper equivalence margin for the rate ratio, rate1 / rate2.
    nobs_ratio : float
        Sample size ratio, nobs2 = nobs_ratio * nobs1.
    exposure : float
        Exposure for each observation. Total exposure is nobs1 * exposure
        and nobs2 * exposure.
    value : float
        Rate ratio, rate1 / rate2, under the null hypothesis.
    alpha : float in interval (0,1)
        Significance level, e.g. 0.05, is the probability of a type I
        error, that is wrong rejections if the Null Hypothesis is true.
    dispersion : float >= 0.
        Dispersion parameter for Negative Binomial distribution.
        The Poisson limiting case corresponds to ``dispersion=0``.
    method_var : {"score", "alt"}
        The variance of the test statistic for the null hypothesis given the
        rates under the alternative, can be either equal to the rates under the
        alternative ``method_var="alt"``, or estimated under the constrained
        of the null hypothesis, ``method_var="score"``, or based on a moment
        constrained estimate, ``method_var="ftotal"``. see references.
    alternative : string, \'two-sided\' (default), \'larger\', \'smaller\'
        Alternative hypothesis whether the power is calculated for a
        two-sided (default) or one sided test. The one-sided test can be
        either \'larger\', \'smaller\'.
    return_results : bool
        If true, then a results instance with extra information is returned,
        otherwise only the computed power is returned.

    Returns
    -------
    results : results instance or float
        If return_results is False, then only the power is returned.
        If return_results is True, then a results instance with the
        information in attributes is returned.

        power : float
            Power of the test, e.g. 0.8, is one minus the probability of a
            type II error. Power is the probability that the test correctly
            rejects the Null Hypothesis if the Alternative Hypothesis is true.

        Other attributes in results instance include :

        std_null
            standard error of difference under the null hypothesis (without
            sqrt(nobs1))
        std_alt
            standard error of difference under the alternative hypothesis
            (without sqrt(nobs1))

    References
    ----------
    .. [1] Zhu, Haiyuan. 2017. “Sample Size Calculation for Comparing Two
       Poisson or Negative Binomial Rates in Noninferiority or Equivalence
       Trials.” Statistics in Biopharmaceutical Research, March.
       https://doi.org/10.1080/19466315.2016.1225594
    .. [2] Zhu, Haiyuan, and Hassan Lakkis. 2014. “Sample Size Calculation for
       Comparing Two Negative Binomial Rates.” Statistics in Medicine 33 (3):
       376–87. https://doi.org/10.1002/sim.5947.
    .. [3] PASS documentation
    '''
def power_equivalence_neginb_2indep(rate1, rate2, nobs1, low, upp, nobs_ratio: int = 1, exposure: int = 1, alpha: float = 0.05, dispersion: int = 0, method_var: str = 'alt', return_results: bool = False):
    '''
    Power of equivalence test of ratio of 2 indep. negative binomial rates.

    Parameters
    ----------
    rate1 : float
        Poisson rate for the first sample, treatment group, under the
        alternative hypothesis.
    rate2 : float
        Poisson rate for the second sample, reference group, under the
        alternative hypothesis.
    nobs1 : float or int
        Number of observations in sample 1.
    low : float
        Lower equivalence margin for the rate ratio, rate1 / rate2.
    upp : float
        Upper equivalence margin for the rate ratio, rate1 / rate2.
    nobs_ratio : float
        Sample size ratio, nobs2 = nobs_ratio * nobs1.
    alpha : float in interval (0,1)
        Significance level, e.g. 0.05, is the probability of a type I
        error, that is wrong rejections if the Null Hypothesis is true.
    dispersion : float >= 0.
        Dispersion parameter for Negative Binomial distribution.
        The Poisson limiting case corresponds to ``dispersion=0``.
    method_var : {"score", "alt"}
        The variance of the test statistic for the null hypothesis given the
        rates under the alternative, can be either equal to the rates under the
        alternative ``method_var="alt"``, or estimated under the constrained
        of the null hypothesis, ``method_var="score"``, or based on a moment
        constrained estimate, ``method_var="ftotal"``. see references.
    alternative : string, \'two-sided\' (default), \'larger\', \'smaller\'
        Alternative hypothesis whether the power is calculated for a
        two-sided (default) or one sided test. The one-sided test can be
        either \'larger\', \'smaller\'.
    return_results : bool
        If true, then a results instance with extra information is returned,
        otherwise only the computed power is returned.

    Returns
    -------
    results : results instance or float
        If return_results is False, then only the power is returned.
        If return_results is True, then a results instance with the
        information in attributes is returned.

        power : float
            Power of the test, e.g. 0.8, is one minus the probability of a
            type II error. Power is the probability that the test correctly
            rejects the Null Hypothesis if the Alternative Hypothesis is true.

        Other attributes in results instance include :

        std_null
            standard error of difference under the null hypothesis (without
            sqrt(nobs1))
        std_alt
            standard error of difference under the alternative hypothesis
            (without sqrt(nobs1))


    References
    ----------
    .. [1] Zhu, Haiyuan. 2017. “Sample Size Calculation for Comparing Two
       Poisson or Negative Binomial Rates in Noninferiority or Equivalence
       Trials.” Statistics in Biopharmaceutical Research, March.
       https://doi.org/10.1080/19466315.2016.1225594
    .. [2] Zhu, Haiyuan, and Hassan Lakkis. 2014. “Sample Size Calculation for
       Comparing Two Negative Binomial Rates.” Statistics in Medicine 33 (3):
       376–87. https://doi.org/10.1002/sim.5947.
    .. [3] PASS documentation
    '''
