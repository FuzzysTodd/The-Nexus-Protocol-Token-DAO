from _typeshed import Incomplete
from statsmodels.tools.sm_exceptions import HypothesisTestWarning as HypothesisTestWarning
from typing import NamedTuple

class DistDependStat(NamedTuple):
    test_statistic: Incomplete
    distance_correlation: Incomplete
    distance_covariance: Incomplete
    dvar_x: Incomplete
    dvar_y: Incomplete
    S: Incomplete

def distance_covariance_test(x, y, B: Incomplete | None = None, method: str = 'auto'):
    '''The Distance Covariance (dCov) test

    Apply the Distance Covariance (dCov) test of independence to `x` and `y`.
    This test was introduced in [1]_, and is based on the distance covariance
    statistic. The test is applicable to random vectors of arbitrary length
    (see the notes section for more details).

    Parameters
    ----------
    x : array_like, 1-D or 2-D
        If `x` is 1-D than it is assumed to be a vector of observations of a
        single random variable. If `x` is 2-D than the rows should be
        observations and the columns are treated as the components of a
        random vector, i.e., each column represents a different component of
        the random vector `x`.
    y : array_like, 1-D or 2-D
        Same as `x`, but only the number of observation has to match that of
        `x`. If `y` is 2-D note that the number of columns of `y` (i.e., the
        number of components in the random vector) does not need to match
        the number of columns in `x`.
    B : int, optional, default=`None`
        The number of iterations to perform when evaluating the null
        distribution of the test statistic when the `emp` method is
        applied (see below). if `B` is `None` than as in [1]_ we set
        `B` to be ``B = 200 + 5000/n``, where `n` is the number of
        observations.
    method : {\'auto\', \'emp\', \'asym\'}, optional, default=auto
        The method by which to obtain the p-value for the test.

        - `auto` : Default method. The number of observations will be used to
          determine the method.
        - `emp` : Empirical evaluation of the p-value using permutations of
          the rows of `y` to obtain the null distribution.
        - `asym` : An asymptotic approximation of the distribution of the test
          statistic is used to find the p-value.

    Returns
    -------
    test_statistic : float
        The value of the test statistic used in the test.
    pval : float
        The p-value.
    chosen_method : str
        The method that was used to obtain the p-value. Mostly relevant when
        the function is called with `method=\'auto\'`.

    Notes
    -----
    The test applies to random vectors of arbitrary dimensions, i.e., `x`
    can be a 1-D vector of observations for a single random variable while
    `y` can be a `k` by `n` 2-D array (where `k > 1`). In other words, it
    is also possible for `x` and `y` to both be 2-D arrays and have the
    same number of rows (observations) while differing in the number of
    columns.

    As noted in [1]_ the statistics are sensitive to all types of departures
    from independence, including nonlinear or nonmonotone dependence
    structure.

    References
    ----------
    .. [1] Szekely, G.J., Rizzo, M.L., and Bakirov, N.K. (2007)
       "Measuring and testing by correlation of distances".
       Annals of Statistics, Vol. 35 No. 6, pp. 2769-2794.

    Examples
    --------
    >>> from statsmodels.stats.dist_dependence_measures import
    ... distance_covariance_test
    >>> data = np.random.rand(1000, 10)
    >>> x, y = data[:, :3], data[:, 3:]
    >>> x.shape
    (1000, 3)
    >>> y.shape
    (1000, 7)
    >>> distance_covariance_test(x, y)
    (1.0426404792714983, 0.2971148340813543, \'asym\')
    # (test_statistic, pval, chosen_method)

    '''
def distance_statistics(x, y, x_dist: Incomplete | None = None, y_dist: Incomplete | None = None):
    '''Calculate various distance dependence statistics.

    Calculate several distance dependence statistics as described in [1]_.

    Parameters
    ----------
    x : array_like, 1-D or 2-D
        If `x` is 1-D than it is assumed to be a vector of observations of a
        single random variable. If `x` is 2-D than the rows should be
        observations and the columns are treated as the components of a
        random vector, i.e., each column represents a different component of
        the random vector `x`.
    y : array_like, 1-D or 2-D
        Same as `x`, but only the number of observation has to match that of
        `x`. If `y` is 2-D note that the number of columns of `y` (i.e., the
        number of components in the random vector) does not need to match
        the number of columns in `x`.
    x_dist : array_like, 2-D, optional
        A square 2-D array_like object whose values are the euclidean
        distances between `x`\'s rows.
    y_dist : array_like, 2-D, optional
        A square 2-D array_like object whose values are the euclidean
        distances between `y`\'s rows.

    Returns
    -------
    namedtuple
        A named tuple of distance dependence statistics (DistDependStat) with
        the following values:

        - test_statistic : float - The "basic" test statistic (i.e., the one
          used when the `emp` method is chosen when calling
          ``distance_covariance_test()``
        - distance_correlation : float - The distance correlation
          between `x` and `y`.
        - distance_covariance : float - The distance covariance of
          `x` and `y`.
        - dvar_x : float - The distance variance of `x`.
        - dvar_y : float - The distance variance of `y`.
        - S : float - The mean of the euclidean distances in `x` multiplied
          by those of `y`. Mostly used internally.

    References
    ----------
    .. [1] Szekely, G.J., Rizzo, M.L., and Bakirov, N.K. (2007)
       "Measuring and testing dependence by correlation of distances".
       Annals of Statistics, Vol. 35 No. 6, pp. 2769-2794.

    Examples
    --------

    >>> from statsmodels.stats.dist_dependence_measures import
    ... distance_statistics
    >>> distance_statistics(np.random.random(1000), np.random.random(1000))
    DistDependStat(test_statistic=0.07948284320205831,
    distance_correlation=0.04269511890990793,
    distance_covariance=0.008915315092696293,
    dvar_x=0.20719027438266704, dvar_y=0.21044934264957588,
    S=0.10892061635588891)

    '''
def distance_covariance(x, y):
    '''Distance covariance.

    Calculate the empirical distance covariance as described in [1]_.

    Parameters
    ----------
    x : array_like, 1-D or 2-D
        If `x` is 1-D than it is assumed to be a vector of observations of a
        single random variable. If `x` is 2-D than the rows should be
        observations and the columns are treated as the components of a
        random vector, i.e., each column represents a different component of
        the random vector `x`.
    y : array_like, 1-D or 2-D
        Same as `x`, but only the number of observation has to match that of
        `x`. If `y` is 2-D note that the number of columns of `y` (i.e., the
        number of components in the random vector) does not need to match
        the number of columns in `x`.

    Returns
    -------
    float
        The empirical distance covariance between `x` and `y`.

    References
    ----------
    .. [1] Szekely, G.J., Rizzo, M.L., and Bakirov, N.K. (2007)
       "Measuring and testing dependence by correlation of distances".
       Annals of Statistics, Vol. 35 No. 6, pp. 2769-2794.

    Examples
    --------

    >>> from statsmodels.stats.dist_dependence_measures import
    ... distance_covariance
    >>> distance_covariance(np.random.random(1000), np.random.random(1000))
    0.007575063951951362

    '''
def distance_variance(x):
    '''Distance variance.

    Calculate the empirical distance variance as described in [1]_.

    Parameters
    ----------
    x : array_like, 1-D or 2-D
        If `x` is 1-D than it is assumed to be a vector of observations of a
        single random variable. If `x` is 2-D than the rows should be
        observations and the columns are treated as the components of a
        random vector, i.e., each column represents a different component of
        the random vector `x`.

    Returns
    -------
    float
        The empirical distance variance of `x`.

    References
    ----------
    .. [1] Szekely, G.J., Rizzo, M.L., and Bakirov, N.K. (2007)
       "Measuring and testing dependence by correlation of distances".
       Annals of Statistics, Vol. 35 No. 6, pp. 2769-2794.

    Examples
    --------

    >>> from statsmodels.stats.dist_dependence_measures import
    ... distance_variance
    >>> distance_variance(np.random.random(1000))
    0.21732609190659702

    '''
def distance_correlation(x, y):
    '''Distance correlation.

    Calculate the empirical distance correlation as described in [1]_.
    This statistic is analogous to product-moment correlation and describes
    the dependence between `x` and `y`, which are random vectors of
    arbitrary length. The statistics\' values range between 0 (implies
    independence) and 1 (implies complete dependence).

    Parameters
    ----------
    x : array_like, 1-D or 2-D
        If `x` is 1-D than it is assumed to be a vector of observations of a
        single random variable. If `x` is 2-D than the rows should be
        observations and the columns are treated as the components of a
        random vector, i.e., each column represents a different component of
        the random vector `x`.
    y : array_like, 1-D or 2-D
        Same as `x`, but only the number of observation has to match that of
        `x`. If `y` is 2-D note that the number of columns of `y` (i.e., the
        number of components in the random vector) does not need to match
        the number of columns in `x`.

    Returns
    -------
    float
        The empirical distance correlation between `x` and `y`.

    References
    ----------
    .. [1] Szekely, G.J., Rizzo, M.L., and Bakirov, N.K. (2007)
       "Measuring and testing dependence by correlation of distances".
       Annals of Statistics, Vol. 35 No. 6, pp. 2769-2794.

    Examples
    --------

    >>> from statsmodels.stats.dist_dependence_measures import
    ... distance_correlation
    >>> distance_correlation(np.random.random(1000), np.random.random(1000))
    0.04060497840149489

    '''
