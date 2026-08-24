from statsmodels.emplike.descriptive import _OptFuncts

class _ELRegOpts(_OptFuncts):
    """

    A class that holds functions to be optimized over when conducting
    hypothesis tests and calculating confidence intervals.

    Parameters
    ----------

    OLSResults : Results instance
        A fitted OLS result.
    """
    def __init__(self) -> None: ...
