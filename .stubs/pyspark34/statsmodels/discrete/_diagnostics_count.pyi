from _typeshed import Incomplete
from statsmodels.discrete.discrete_model import Poisson as Poisson
from statsmodels.regression.linear_model import OLS as OLS
from statsmodels.stats.base import HolderTuple as HolderTuple

def plot_probs(freq, probs_predicted, label: str = 'predicted', upp_xlim: Incomplete | None = None, fig: Incomplete | None = None):
    '''diagnostic plots for comparing two lists of discrete probabilities

    Parameters
    ----------
    freq, probs_predicted : nd_arrays
        two arrays of probabilities, this can be any probabilities for
        the same events, default is designed for comparing predicted
        and observed probabilities
    label : str or tuple
        If string, then it will be used as the label for probs_predicted and
        "freq" is used for the other probabilities.
        If label is a tuple of strings, then the first is they are used as
        label for both probabilities

    upp_xlim : None or int
        If it is not None, then the xlim of the first two plots are set to
        (0, upp_xlim), otherwise the matplotlib default is used
    fig : None or matplotlib figure instance
        If fig is provided, then the axes will be added to it in a (3,1)
        subplots, otherwise a matplotlib figure instance is created

    Returns
    -------
    Figure
        The figure contains 3 subplot with probabilities, cumulative
        probabilities and a PP-plot
    '''
def test_chisquare_prob(results, probs, bin_edges: Incomplete | None = None, method: Incomplete | None = None):
    """
    chisquare test for predicted probabilities using cmt-opg

    Parameters
    ----------
    results : results instance
        Instance of a count regression results
    probs : ndarray
        Array of predicted probabilities with observations
        in rows and event counts in columns
    bin_edges : None or array
        intervals to combine several counts into cells
        see combine_bins

    Returns
    -------
    (api not stable, replace by test-results class)
    statistic : float
        chisquare statistic for tes
    p-value : float
        p-value of test
    df : int
        degrees of freedom for chisquare distribution
    extras : ???
        currently returns a tuple with some intermediate results
        (diff, res_aux)

    Notes
    -----

    Status : experimental, no verified unit tests, needs to be generalized
    currently only OPG version with auxiliary regression is implemented

    Assumes counts are np.arange(probs.shape[1]), i.e. consecutive
    integers starting at zero.

    Auxiliary regression drops the last column of binned probs to avoid
    that probabilities sum to 1.

    References
    ----------
    .. [1] Andrews, Donald W. K. 1988a. “Chi-Square Diagnostic Tests for
           Econometric Models: Theory.” Econometrica 56 (6): 1419–53.
           https://doi.org/10.2307/1913105.

    .. [2] Andrews, Donald W. K. 1988b. “Chi-Square Diagnostic Tests for
           Econometric Models.” Journal of Econometrics 37 (1): 135–56.
           https://doi.org/10.1016/0304-4076(88)90079-6.

    .. [3] Manjón, M., and O. Martínez. 2014. “The Chi-Squared Goodness-of-Fit
           Test for Count-Data Models.” Stata Journal 14 (4): 798–816.
    """

class DispersionResults(HolderTuple):
    def summary_frame(self): ...

def test_poisson_dispersion(results, method: str = 'all', _old: bool = False):
    """Score/LM type tests for Poisson variance assumptions

    Null Hypothesis is

    H0: var(y) = E(y) and assuming E(y) is correctly specified
    H1: var(y) ~= E(y)

    The tests are based on the constrained model, i.e. the Poisson model.
    The tests differ in their assumed alternatives, and in their maintained
    assumptions.

    Parameters
    ----------
    results : Poisson results instance
        This can be a results instance for either a discrete Poisson or a GLM
        with family Poisson.
    method : str
        Not used yet. Currently results for all methods are returned.
    _old : bool
        Temporary keyword for backwards compatibility, will be removed
        in future version of statsmodels.

    Returns
    -------
    res : instance
        The instance of DispersionResults has the hypothesis test results,
        statistic, pvalue, method, alternative, as main attributes and a
        summary_frame method that returns the results as pandas DataFrame.

    """
def test_poisson_zeroinflation_jh(results_poisson, exog_infl: Incomplete | None = None):
    """score test for zero inflation or deflation in Poisson

    This implements Jansakul and Hinde 2009 score test
    for excess zeros against a zero modified Poisson
    alternative. They use a linear link function for the
    inflation model to allow for zero deflation.

    Parameters
    ----------
    results_poisson: results instance
        The test is only valid if the results instance is a Poisson
        model.
    exog_infl : ndarray
        Explanatory variables for the zero inflated or zero modified
        alternative. I exog_infl is None, then the inflation
        probability is assumed to be constant.

    Returns
    -------
    score test results based on chisquare distribution

    Notes
    -----
    This is a score test based on the null hypothesis that
    the true model is Poisson. It will also reject for
    other deviations from a Poisson model if those affect
    the zero probabilities, e.g. in the direction of
    excess dispersion as in the Negative Binomial
    or Generalized Poisson model.
    Therefore, rejection in this test does not imply that
    zero-inflated Poisson is the appropriate model.

    Status: experimental, no verified unit tests,

    TODO: If the zero modification probability is assumed
    to be constant under the alternative, then we only have
    a scalar test score and we can use one-sided tests to
    distinguish zero inflation and deflation from the
    two-sided deviations. (The general one-sided case is
    difficult.)
    In this case the test specializes to the test by Broek

    References
    ----------
    .. [1] Jansakul, N., and J. P. Hinde. 2002. “Score Tests for Zero-Inflated
           Poisson Models.” Computational Statistics & Data Analysis 40 (1):
           75–96. https://doi.org/10.1016/S0167-9473(01)00104-9.
    """
def test_poisson_zeroinflation_broek(results_poisson):
    """score test for zero modification in Poisson, special case

    This assumes that the Poisson model has a constant and that
    the zero modification probability is constant.

    This is a special case of test_poisson_zeroinflation derived by
    van den Broek 1995.

    The test reports two sided and one sided alternatives based on
    the normal distribution of the test statistic.

    References
    ----------
    .. [1] Broek, Jan van den. 1995. “A Score Test for Zero Inflation in a
           Poisson Distribution.” Biometrics 51 (2): 738–43.
           https://doi.org/10.2307/2532959.

    """
def test_poisson_zeros(results):
    """Test for excess zeros in Poisson regression model.

    The test is implemented following Tang and Tang [1]_ equ. (12) which is
    based on the test derived in He et al 2019 [2]_.

    References
    ----------

    .. [1] Tang, Yi, and Wan Tang. 2018. “Testing Modified Zeros for Poisson
           Regression Models:” Statistical Methods in Medical Research,
           September. https://doi.org/10.1177/0962280218796253.

    .. [2] He, Hua, Hui Zhang, Peng Ye, and Wan Tang. 2019. “A Test of Inflated
           Zeros for Poisson Regression Models.” Statistical Methods in
           Medical Research 28 (4): 1157–69.
           https://doi.org/10.1177/0962280217749991.

    """
