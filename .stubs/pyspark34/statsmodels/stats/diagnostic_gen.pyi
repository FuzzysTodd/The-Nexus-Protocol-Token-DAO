from _typeshed import Incomplete
from statsmodels.stats.base import HolderTuple as HolderTuple

def test_chisquare_binning(counts, expected, sort_var: Incomplete | None = None, bins: int = 10, df: Incomplete | None = None, ordered: bool = False, sort_method: str = 'quicksort', alpha_nc: float = 0.05):
    """chisquare gof test with binning of data, Hosmer-Lemeshow type

    ``observed`` and ``expected`` are observation specific and should have
    observations in rows and choices in columns

    Parameters
    ----------
    counts : array_like
        Observed frequency, i.e. counts for all choices
    expected : array_like
        Expected counts or probability. If expected are counts, then they
        need to sum to the same total count as the sum of observed.
        If those sums are unequal and all expected values are smaller or equal
        to 1, then they are interpreted as probabilities and will be rescaled
        to match counts.
    sort_var : array_like
        1-dimensional array for binning. Groups will be formed according to
        quantiles of the sorted array ``sort_var``, so that group sizes have
        equal or approximately equal sizes.

    Returns
    -------
    Holdertuple instance
        This instance contains the results of the chisquare test and some
        information about the data

        - statistic : chisquare statistic of the goodness-of-fit test
        - pvalue : pvalue of the chisquare test
        = df : degrees of freedom of the test

    Notes
    -----
    Degrees of freedom for Hosmer-Lemeshow tests are given by

    g groups, c choices

    - binary: `df = (g - 2)` for insample,
         Stata uses `df = g` for outsample
    - multinomial: `df = (g−2) *(c−1)`, reduces to (g-2) for binary c=2,
         (Fagerland, Hosmer, Bofin SIM 2008)
    - ordinal: `df = (g - 2) * (c - 1) + (c - 2)`, reduces to (g-2) for c=2,
         (Hosmer, ... ?)

    Note: If there are ties in the ``sort_var`` array, then the split of
    observations into groups will depend on the sort algorithm.
    """
def prob_larger_ordinal_choice(prob):
    """probability that observed category is larger than distribution prob

    This is a helper function for Ordinal models, where endog is a 1-dim
    categorical variable and predicted probabilities are 2-dimensional with
    observations in rows and choices in columns.

    Parameter
    ---------
    prob : array_like
        Expected probabilities for ordinal choices, e.g. from prediction of
        an ordinal model with observations in rows and choices in columns.

    Returns
    -------
    cdf_mid : ndarray
        mid cdf, i.e ``P(x < y) + 0.5 P(x=y)``
    r : ndarray
        Probability residual ``P(x > y) - P(x < y)`` for all possible choices.
        Computed as ``r = cdf_mid * 2 - 1``

    References
    ----------
    .. [2] Li, Chun, and Bryan E. Shepherd. 2012. “A New Residual for Ordinal
       Outcomes.” Biometrika 99 (2): 473–80.

    See Also
    --------
    `statsmodels.stats.nonparametric.rank_compare_2ordinal`

    """
def prob_larger_2ordinal(probs1, probs2):
    """Stochastically large probability for two ordinal distributions

    Computes Pr(x1 > x2) + 0.5 * Pr(x1 = x2) for two ordered multinomial
    (ordinal) distributed random variables x1 and x2.

    This is vectorized with choices along last axis.
    Broadcasting if freq2 is 1-dim also seems to work correctly.

    Returns
    -------
    prob1 : float
        Probability that random draw from distribution 1 is larger than a
        random draw from distribution 2. Pr(x1 > x2) + 0.5 * Pr(x1 = x2)
    prob2 : float
        prob2 = 1 - prob1 = Pr(x1 < x2) + 0.5 * Pr(x1 = x2)
    """
def cov_multinomial(probs):
    """covariance matrix of multinomial distribution

    This is vectorized with choices along last axis.

    cov = diag(probs) - outer(probs, probs)

    """
def var_multinomial(probs):
    """variance of multinomial distribution

    var = probs * (1 - probs)

    """
