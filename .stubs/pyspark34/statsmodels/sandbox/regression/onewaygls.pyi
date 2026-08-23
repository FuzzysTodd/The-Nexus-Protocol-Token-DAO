from _typeshed import Incomplete
from statsmodels.regression.linear_model import OLS as OLS, WLS as WLS

class OneWayLS:
    """Class to test equality of regression coefficients across groups

    This class performs tests whether the linear regression coefficients are
    the same across pre-specified groups. This can be used to test for
    structural breaks at given change points, or for ANOVA style analysis of
    differences in the effect of explanatory variables across groups.

    Notes
    -----
    The test is implemented by regression on the original pooled exogenous
    variables and on group dummies times the exogenous regressors.

    y_i = X_i beta_i + u_i  for all groups i

    The test is for the null hypothesis: beta_i = beta for all i
    against the alternative that at least one beta_i is different.

    By default it is assumed that all u_i have the same variance. If the
    keyword option het is True, then it is assumed that the variance is
    group specific. This uses WLS with weights given by the standard errors
    from separate regressions for each group.
    Note: het=True is not sufficiently tested

    The F-test assumes that the errors are normally distributed.



    original question from mailing list for equality of coefficients
    across regressions, and example in Stata FAQ

    *testing*:

    * if constant is the only regressor then the result for the F-test is
      the same as scipy.stats.f_oneway
      (which in turn is verified against NIST for not badly scaled problems)
    * f-test for simple structural break is the same as in original script
    * power and size of test look ok in examples
    * not checked/verified for heteroskedastic case
      - for constant only: ftest result is the same with WLS as with OLS - check?

    check: I might be mixing up group names (unique)
           and group id (integers in arange(ngroups)
           not tested for groups that are not arange(ngroups)
           make sure groupnames are always consistently sorted/ordered
           Fixed for getting the results, but groups are not printed yet, still
           inconsistent use for summaries of results.
    """
    endog: Incomplete
    exog: Incomplete
    groups: Incomplete
    het: Incomplete
    groupsint: Incomplete
    unique: Incomplete
    uniqueint: Incomplete
    def __init__(self, y, x, groups: Incomplete | None = None, het: bool = False, data: Incomplete | None = None, meta: Incomplete | None = None) -> None: ...
    olsbygroup: Incomplete
    sigmabygroup: Incomplete
    weights: Incomplete
    def fitbygroups(self) -> None:
        """Fit OLS regression for each group separately.

        Returns
        -------
        results are attached

        olsbygroup : dictionary of result instance
            the returned regression results for each group
        sigmabygroup : array (ngroups,) (this should be called sigma2group ??? check)
            mse_resid for each group
        weights : array (nobs,)
            standard deviation of group extended to the original observations. This can
            be used as weights in WLS for group-wise heteroscedasticity.



        """
    lsjoint: Incomplete
    contrasts: Incomplete
    def fitjoint(self) -> None:
        """fit a joint fixed effects model to all observations

        The regression results are attached as `lsjoint`.

        The contrasts for overall and pairwise tests for equality of coefficients are
        attached as a dictionary `contrasts`. This also includes the contrasts for the test
        that the coefficients of a level are zero. ::

        >>> res.contrasts.keys()
        [(0, 1), 1, 'all', 3, (1, 2), 2, (1, 3), (2, 3), (0, 3), (0, 2)]

        The keys are based on the original names or labels of the groups.

        TODO: keys can be numpy scalars and then the keys cannot be sorted



        """
    lspooled: Incomplete
    def fitpooled(self) -> None:
        """fit the pooled model, which assumes there are no differences across groups
        """
    summarytable: Incomplete
    def ftest_summary(self):
        """run all ftests on the joint model

        Returns
        -------
        fres : str
           a string that lists the results of all individual f-tests
        summarytable : list of tuples
           contains (pair, (fvalue, pvalue,df_denom, df_num)) for each f-test

        Note
        ----
        This are the raw results and not formatted for nice printing.

        """
    def print_summary(self, res):
        """printable string of summary

        """
    def lr_test(self):
        """
        generic likelihood ratio test between nested models

            \\begin{align}
            D & = -2(\\ln(\\text{likelihood for null model}) - \\ln(\\text{likelihood for alternative model})) \\\\\n            & = -2\\ln\\left( \\frac{\\text{likelihood for null model}}{\\text{likelihood for alternative model}} \\right).
            \\end{align}

        is distributed as chisquare with df equal to difference in number of parameters or equivalently
        difference in residual degrees of freedom  (sign?)

        TODO: put into separate function
        """
