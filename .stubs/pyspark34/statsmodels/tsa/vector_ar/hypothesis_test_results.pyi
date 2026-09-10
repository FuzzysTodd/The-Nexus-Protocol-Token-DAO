from _typeshed import Incomplete
from statsmodels.iolib.table import SimpleTable as SimpleTable

class HypothesisTestResults:
    '''
    Results class for hypothesis tests.

    Parameters
    ----------
    test_statistic : float
    crit_value : float
    pvalue : float, 0 <= `pvalue` <= 1
    df : int
        Degrees of freedom.
    signif : float, 0 < `signif` < 1
        Significance level.
    method : str
        The kind of test (e.g. ``"f"`` for F-test, ``"wald"`` for Wald-test).
    title : str
        A title describing the test. It will be part of the summary.
    h0 : str
        A string describing the null hypothesis. It will be used in the
        summary.
    '''
    test_statistic: Incomplete
    crit_value: Incomplete
    pvalue: Incomplete
    df: Incomplete
    signif: Incomplete
    method: Incomplete
    conclusion: str
    title: Incomplete
    h0: Incomplete
    conclusion_str: Incomplete
    signif_str: Incomplete
    def __init__(self, test_statistic, crit_value, pvalue, df, signif, method, title, h0) -> None: ...
    def summary(self):
        """Return summary"""
    def __eq__(self, other): ...

class CausalityTestResults(HypothesisTestResults):
    '''
    Results class for Granger-causality and instantaneous causality.

    Parameters
    ----------
    causing : list of str
        This list contains the potentially causing variables.
    caused : list of str
        This list contains the potentially caused variables.
    test_statistic : float
    crit_value : float
    pvalue : float
    df : int
        Degrees of freedom.
    signif : float
        Significance level.
    test : str {``"granger"``, ``"inst"``}, default: ``"granger"``
        If ``"granger"``, Granger-causality has been tested. If ``"inst"``,
        instantaneous causality has been tested.
    method : str {``"f"``, ``"wald"``}
        The kind of test. ``"f"`` indicates an F-test, ``"wald"`` indicates a
        Wald-test.
    '''
    causing: Incomplete
    caused: Incomplete
    test: Incomplete
    def __init__(self, causing, caused, test_statistic, crit_value, pvalue, df, signif, test: str = 'granger', method: Incomplete | None = None) -> None: ...
    def __eq__(self, other): ...

class NormalityTestResults(HypothesisTestResults):
    """
    Results class for the Jarque-Bera-test for nonnormality.

    Parameters
    ----------
    test_statistic : float
        The test's test statistic.
    crit_value : float
        The test's critical value.
    pvalue : float
        The test's p-value.
    df : int
        Degrees of freedom.
    signif : float
        Significance level.
    """
    def __init__(self, test_statistic, crit_value, pvalue, df, signif) -> None: ...

class WhitenessTestResults(HypothesisTestResults):
    """
    Results class for the Portmanteau-test for residual autocorrelation.

    Parameters
    ----------
    test_statistic : float
        The test's test statistic.
    crit_value : float
        The test's critical value.
    pvalue : float
        The test's p-value.
    df : int
        Degrees of freedom.
    signif : float
        Significance level.
    nlags : int
        Number of lags tested.
    """
    lags: Incomplete
    adjusted: Incomplete
    def __init__(self, test_statistic, crit_value, pvalue, df, signif, nlags, adjusted) -> None: ...
