from _typeshed import Incomplete
from statsmodels import iolib as iolib
from statsmodels.tools import sm_exceptions as sm_exceptions
from statsmodels.tools.decorators import cache_readonly as cache_readonly

class _Bunch: ...

class Table:
    """
    A two-way contingency table.

    Parameters
    ----------
    table : array_like
        A contingency table.
    shift_zeros : bool
        If True and any cell count is zero, add 0.5 to all values
        in the table.

    Attributes
    ----------
    table_orig : array_like
        The original table is cached as `table_orig`.

    See Also
    --------
    statsmodels.graphics.mosaicplot.mosaic
    scipy.stats.chi2_contingency

    Notes
    -----
    The inference procedures used here are all based on a sampling
    model in which the units are independent and identically
    distributed, with each unit being classified with respect to two
    categorical variables.

    References
    ----------
    Definitions of residuals:
        https://onlinecourses.science.psu.edu/stat504/node/86
    """
    table_orig: Incomplete
    table: Incomplete
    def __init__(self, table, shift_zeros: bool = True) -> None: ...
    @classmethod
    def from_data(cls, data, shift_zeros: bool = True):
        """
        Construct a Table object from data.

        Parameters
        ----------
        data : array_like
            The raw data, from which a contingency table is constructed
            using the first two columns.
        shift_zeros : bool
            If True and any cell count is zero, add 0.5 to all values
            in the table.

        Returns
        -------
        A Table instance.
        """
    def test_nominal_association(self):
        """
        Assess independence for nominal factors.

        Assessment of independence between rows and columns using
        chi^2 testing.  The rows and columns are treated as nominal
        (unordered) categorical variables.

        Returns
        -------
        A bunch containing the following attributes:

        statistic : float
            The chi^2 test statistic.
        df : int
            The degrees of freedom of the reference distribution
        pvalue : float
            The p-value for the test.
        """
    def test_ordinal_association(self, row_scores: Incomplete | None = None, col_scores: Incomplete | None = None):
        """
        Assess independence between two ordinal variables.

        This is the 'linear by linear' association test, which uses
        weights or scores to target the test to have more power
        against ordered alternatives.

        Parameters
        ----------
        row_scores : array_like
            An array of numeric row scores
        col_scores : array_like
            An array of numeric column scores

        Returns
        -------
        A bunch with the following attributes:

        statistic : float
            The test statistic.
        null_mean : float
            The expected value of the test statistic under the null
            hypothesis.
        null_sd : float
            The standard deviation of the test statistic under the
            null hypothesis.
        zscore : float
            The Z-score for the test statistic.
        pvalue : float
            The p-value for the test.

        Notes
        -----
        The scores define the trend to which the test is most sensitive.

        Using the default row and column scores gives the
        Cochran-Armitage trend test.
        """
    def marginal_probabilities(self):
        """
        Estimate marginal probability distributions for the rows and columns.

        Returns
        -------
        row : ndarray
            Marginal row probabilities
        col : ndarray
            Marginal column probabilities
        """
    def independence_probabilities(self):
        """
        Returns fitted joint probabilities under independence.

        The returned table is outer(row, column), where row and
        column are the estimated marginal distributions
        of the rows and columns.
        """
    def fittedvalues(self):
        """
        Returns fitted cell counts under independence.

        The returned cell counts are estimates under a model
        where the rows and columns of the table are independent.
        """
    def resid_pearson(self):
        """
        Returns Pearson residuals.

        The Pearson residuals are calculated under a model where
        the rows and columns of the table are independent.
        """
    def standardized_resids(self):
        """
        Returns standardized residuals under independence.
        """
    def chi2_contribs(self):
        """
        Returns the contributions to the chi^2 statistic for independence.

        The returned table contains the contribution of each cell to the chi^2
        test statistic for the null hypothesis that the rows and columns
        are independent.
        """
    def local_log_oddsratios(self):
        """
        Returns local log odds ratios.

        The local log odds ratios are the log odds ratios
        calculated for contiguous 2x2 sub-tables.
        """
    def local_oddsratios(self):
        """
        Returns local odds ratios.

        See documentation for local_log_oddsratios.
        """
    def cumulative_log_oddsratios(self):
        """
        Returns cumulative log odds ratios.

        The cumulative log odds ratios for a contingency table
        with ordered rows and columns are calculated by collapsing
        all cells to the left/right and above/below a given point,
        to obtain a 2x2 table from which a log odds ratio can be
        calculated.
        """
    def cumulative_oddsratios(self):
        """
        Returns the cumulative odds ratios for a contingency table.

        See documentation for cumulative_log_oddsratio.
        """

class SquareTable(Table):
    """
    Methods for analyzing a square contingency table.

    Parameters
    ----------
    table : array_like
        A square contingency table, or DataFrame that is converted
        to a square form.
    shift_zeros : bool
        If True and any cell count is zero, add 0.5 to all values
        in the table.

    Notes
    -----
    These methods should only be used when the rows and columns of the
    table have the same categories.  If `table` is provided as a
    Pandas DataFrame, the row and column indices will be extended to
    create a square table, inserting zeros where a row or column is
    missing.  Otherwise the table should be provided in a square form,
    with the (implicit) row and column categories appearing in the
    same order.
    """
    def __init__(self, table, shift_zeros: bool = True) -> None: ...
    def symmetry(self, method: str = 'bowker'):
        """
        Test for symmetry of a joint distribution.

        This procedure tests the null hypothesis that the joint
        distribution is symmetric around the main diagonal, that is

        .. math::

        p_{i, j} = p_{j, i}  for all i, j

        Returns
        -------
        Bunch
            A bunch with attributes

            * statistic : float
                chisquare test statistic
            * p-value : float
                p-value of the test statistic based on chisquare distribution
            * df : int
                degrees of freedom of the chisquare distribution

        Notes
        -----
        The implementation is based on the SAS documentation. R includes
        it in `mcnemar.test` if the table is not 2 by 2.  However a more
        direct generalization of the McNemar test to larger tables is
        provided by the homogeneity test (TableSymmetry.homogeneity).

        The p-value is based on the chi-square distribution which requires
        that the sample size is not very small to be a good approximation
        of the true distribution. For 2x2 contingency tables the exact
        distribution can be obtained with `mcnemar`

        See Also
        --------
        mcnemar
        homogeneity
        """
    def homogeneity(self, method: str = 'stuart_maxwell'):
        """
        Compare row and column marginal distributions.

        Parameters
        ----------
        method : str
            Either 'stuart_maxwell' or 'bhapkar', leading to two different
            estimates of the covariance matrix for the estimated
            difference between the row margins and the column margins.

        Returns
        -------
        Bunch
            A bunch with attributes:

            * statistic : float
                The chi^2 test statistic
            * pvalue : float
                The p-value of the test statistic
            * df : int
                The degrees of freedom of the reference distribution

        Notes
        -----
        For a 2x2 table this is equivalent to McNemar's test.  More
        generally the procedure tests the null hypothesis that the
        marginal distribution of the row factor is equal to the
        marginal distribution of the column factor.  For this to be
        meaningful, the two factors must have the same sample space
        (i.e. the same categories).
        """
    def summary(self, alpha: float = 0.05, float_format: str = '%.3f'):
        """
        Produce a summary of the analysis.

        Parameters
        ----------
        alpha : float
            `1 - alpha` is the nominal coverage probability of the interval.
        float_format : str
            Used to format numeric values in the table.
        method : str
            The method for producing the confidence interval.  Currently
            must be 'normal' which uses the normal approximation.
        """

class Table2x2(SquareTable):
    """
    Analyses that can be performed on a 2x2 contingency table.

    Parameters
    ----------
    table : array_like
        A 2x2 contingency table
    shift_zeros : bool
        If true, 0.5 is added to all cells of the table if any cell is
        equal to zero.

    Notes
    -----
    The inference procedures used here are all based on a sampling
    model in which the units are independent and identically
    distributed, with each unit being classified with respect to two
    categorical variables.

    Note that for the risk ratio, the analysis is not symmetric with
    respect to the rows and columns of the contingency table.  The two
    rows define population subgroups, column 0 is the number of
    'events', and column 1 is the number of 'non-events'.
    """
    def __init__(self, table, shift_zeros: bool = True) -> None: ...
    @classmethod
    def from_data(cls, data, shift_zeros: bool = True):
        """
        Construct a Table object from data.

        Parameters
        ----------
        data : array_like
            The raw data, the first column defines the rows and the
            second column defines the columns.
        shift_zeros : bool
            If True, and if there are any zeros in the contingency
            table, add 0.5 to all four cells of the table.
        """
    def log_oddsratio(self):
        """
        Returns the log odds ratio for a 2x2 table.
        """
    def oddsratio(self):
        """
        Returns the odds ratio for a 2x2 table.
        """
    def log_oddsratio_se(self):
        """
        Returns the standard error for the log odds ratio.
        """
    def oddsratio_pvalue(self, null: int = 1):
        """
        P-value for a hypothesis test about the odds ratio.

        Parameters
        ----------
        null : float
            The null value of the odds ratio.
        """
    def log_oddsratio_pvalue(self, null: int = 0):
        """
        P-value for a hypothesis test about the log odds ratio.

        Parameters
        ----------
        null : float
            The null value of the log odds ratio.
        """
    def log_oddsratio_confint(self, alpha: float = 0.05, method: str = 'normal'):
        """
        A confidence level for the log odds ratio.

        Parameters
        ----------
        alpha : float
            `1 - alpha` is the nominal coverage probability of the
            confidence interval.
        method : str
            The method for producing the confidence interval.  Currently
            must be 'normal' which uses the normal approximation.
        """
    def oddsratio_confint(self, alpha: float = 0.05, method: str = 'normal'):
        """
        A confidence interval for the odds ratio.

        Parameters
        ----------
        alpha : float
            `1 - alpha` is the nominal coverage probability of the
            confidence interval.
        method : str
            The method for producing the confidence interval.  Currently
            must be 'normal' which uses the normal approximation.
        """
    def riskratio(self):
        """
        Returns the risk ratio for a 2x2 table.

        The risk ratio is calculated with respect to the rows.
        """
    def log_riskratio(self):
        """
        Returns the log of the risk ratio.
        """
    def log_riskratio_se(self):
        """
        Returns the standard error of the log of the risk ratio.
        """
    def riskratio_pvalue(self, null: int = 1):
        """
        p-value for a hypothesis test about the risk ratio.

        Parameters
        ----------
        null : float
            The null value of the risk ratio.
        """
    def log_riskratio_pvalue(self, null: int = 0):
        """
        p-value for a hypothesis test about the log risk ratio.

        Parameters
        ----------
        null : float
            The null value of the log risk ratio.
        """
    def log_riskratio_confint(self, alpha: float = 0.05, method: str = 'normal'):
        """
        A confidence interval for the log risk ratio.

        Parameters
        ----------
        alpha : float
            `1 - alpha` is the nominal coverage probability of the
            confidence interval.
        method : str
            The method for producing the confidence interval.  Currently
            must be 'normal' which uses the normal approximation.
        """
    def riskratio_confint(self, alpha: float = 0.05, method: str = 'normal'):
        """
        A confidence interval for the risk ratio.

        Parameters
        ----------
        alpha : float
            `1 - alpha` is the nominal coverage probability of the
            confidence interval.
        method : str
            The method for producing the confidence interval.  Currently
            must be 'normal' which uses the normal approximation.
        """
    def summary(self, alpha: float = 0.05, float_format: str = '%.3f', method: str = 'normal'):
        """
        Summarizes results for a 2x2 table analysis.

        Parameters
        ----------
        alpha : float
            `1 - alpha` is the nominal coverage probability of the confidence
            intervals.
        float_format : str
            Used to format the numeric values in the table.
        method : str
            The method for producing the confidence interval.  Currently
            must be 'normal' which uses the normal approximation.
        """

class StratifiedTable:
    """
    Analyses for a collection of 2x2 contingency tables.

    Such a collection may arise by stratifying a single 2x2 table with
    respect to another factor.  This class implements the
    'Cochran-Mantel-Haenszel' and 'Breslow-Day' procedures for
    analyzing collections of 2x2 contingency tables.

    Parameters
    ----------
    tables : list or ndarray
        Either a list containing several 2x2 contingency tables, or
        a 2x2xk ndarray in which each slice along the third axis is a
        2x2 contingency table.

    Notes
    -----
    This results are based on a sampling model in which the units are
    independent both within and between strata.
    """
    table: Incomplete
    def __init__(self, tables, shift_zeros: bool = False) -> None: ...
    @classmethod
    def from_data(cls, var1, var2, strata, data):
        """
        Construct a StratifiedTable object from data.

        Parameters
        ----------
        var1 : int or string
            The column index or name of `data` specifying the variable
            defining the rows of the contingency table.  The variable
            must have only two distinct values.
        var2 : int or string
            The column index or name of `data` specifying the variable
            defining the columns of the contingency table.  The variable
            must have only two distinct values.
        strata : int or string
            The column index or name of `data` specifying the variable
            defining the strata.
        data : array_like
            The raw data.  A cross-table for analysis is constructed
            from the first two columns.

        Returns
        -------
        StratifiedTable
        """
    def test_null_odds(self, correction: bool = False):
        """
        Test that all tables have odds ratio equal to 1.

        This is the 'Mantel-Haenszel' test.

        Parameters
        ----------
        correction : bool
            If True, use the continuity correction when calculating the
            test statistic.

        Returns
        -------
        Bunch
            A bunch containing the chi^2 test statistic and p-value.
        """
    def oddsratio_pooled(self):
        """
        The pooled odds ratio.

        The value is an estimate of a common odds ratio across all of the
        stratified tables.
        """
    def logodds_pooled(self):
        """
        Returns the logarithm of the pooled odds ratio.

        See oddsratio_pooled for more information.
        """
    def riskratio_pooled(self):
        """
        Estimate of the pooled risk ratio.
        """
    def logodds_pooled_se(self):
        '''
        Estimated standard error of the pooled log odds ratio

        References
        ----------
        J. Robins, N. Breslow, S. Greenland. "Estimators of the
        Mantel-Haenszel Variance Consistent in Both Sparse Data and
        Large-Strata Limiting Models." Biometrics 42, no. 2 (1986): 311-23.
        '''
    def logodds_pooled_confint(self, alpha: float = 0.05, method: str = 'normal'):
        """
        A confidence interval for the pooled log odds ratio.

        Parameters
        ----------
        alpha : float
            `1 - alpha` is the nominal coverage probability of the
            interval.
        method : str
            The method for producing the confidence interval.  Currently
            must be 'normal' which uses the normal approximation.

        Returns
        -------
        lcb : float
            The lower confidence limit.
        ucb : float
            The upper confidence limit.
        """
    def oddsratio_pooled_confint(self, alpha: float = 0.05, method: str = 'normal'):
        """
        A confidence interval for the pooled odds ratio.

        Parameters
        ----------
        alpha : float
            `1 - alpha` is the nominal coverage probability of the
            interval.
        method : str
            The method for producing the confidence interval.  Currently
            must be 'normal' which uses the normal approximation.

        Returns
        -------
        lcb : float
            The lower confidence limit.
        ucb : float
            The upper confidence limit.
        """
    def test_equal_odds(self, adjust: bool = False):
        """
        Test that all odds ratios are identical.

        This is the 'Breslow-Day' testing procedure.

        Parameters
        ----------
        adjust : bool
            Use the 'Tarone' adjustment to achieve the chi^2
            asymptotic distribution.

        Returns
        -------
        A bunch containing the following attributes:

        statistic : float
            The chi^2 test statistic.
        p-value : float
            The p-value for the test.
        """
    def summary(self, alpha: float = 0.05, float_format: str = '%.3f', method: str = 'normal'):
        """
        A summary of all the main results.

        Parameters
        ----------
        alpha : float
            `1 - alpha` is the nominal coverage probability of the
            confidence intervals.
        float_format : str
            Used for formatting numeric values in the summary.
        method : str
            The method for producing the confidence interval.  Currently
            must be 'normal' which uses the normal approximation.
        """

def mcnemar(table, exact: bool = True, correction: bool = True):
    """
    McNemar test of homogeneity.

    Parameters
    ----------
    table : array_like
        A square contingency table.
    exact : bool
        If exact is true, then the binomial distribution will be used.
        If exact is false, then the chisquare distribution will be
        used, which is the approximation to the distribution of the
        test statistic for large sample sizes.
    correction : bool
        If true, then a continuity correction is used for the chisquare
        distribution (if exact is false.)

    Returns
    -------
    A bunch with attributes:

    statistic : float or int, array
        The test statistic is the chisquare statistic if exact is
        false. If the exact binomial distribution is used, then this
        contains the min(n1, n2), where n1, n2 are cases that are zero
        in one sample but one in the other sample.
    pvalue : float or array
        p-value of the null hypothesis of equal marginal distributions.

    Notes
    -----
    This is a special case of Cochran's Q test, and of the homogeneity
    test. The results when the chisquare distribution is used are
    identical, except for continuity correction.
    """
def cochrans_q(x, return_object: bool = True):
    """
    Cochran's Q test for identical binomial proportions.

    Parameters
    ----------
    x : array_like, 2d (N, k)
        data with N cases and k variables
    return_object : bool
        Return values as bunch instead of as individual values.

    Returns
    -------
    Returns a bunch containing the following attributes, or the
    individual values according to the value of `return_object`.

    statistic : float
       test statistic
    pvalue : float
       pvalue from the chisquare distribution

    Notes
    -----
    Cochran's Q is a k-sample extension of the McNemar test. If there
    are only two groups, then Cochran's Q test and the McNemar test
    are equivalent.

    The procedure tests that the probability of success is the same
    for every group.  The alternative hypothesis is that at least two
    groups have a different probability of success.

    In Wikipedia terminology, rows are blocks and columns are
    treatments.  The number of rows N, should be large for the
    chisquare distribution to be a good approximation.

    The Null hypothesis of the test is that all treatments have the
    same effect.

    References
    ----------
    https://en.wikipedia.org/wiki/Cochran_test
    SAS Manual for NPAR TESTS
    """
