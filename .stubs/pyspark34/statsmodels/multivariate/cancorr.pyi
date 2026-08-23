from .multivariate_ols import multivariate_stats as multivariate_stats
from _typeshed import Incomplete
from statsmodels.base.model import Model as Model
from statsmodels.iolib import summary2 as summary2

class CanCorr(Model):
    """
    Canonical correlation analysis using singular value decomposition

    For matrices exog=x and endog=y, find projections x_cancoef and y_cancoef
    such that:

        x1 = x * x_cancoef, x1' * x1 is identity matrix
        y1 = y * y_cancoef, y1' * y1 is identity matrix

    and the correlation between x1 and y1 is maximized.

    Attributes
    ----------
    endog : ndarray
        See Parameters.
    exog : ndarray
        See Parameters.
    cancorr : ndarray
        The canonical correlation values
    y_cancoeff : ndarray
        The canonical coefficients for endog
    x_cancoeff : ndarray
        The canonical coefficients for exog

    References
    ----------
    .. [*] http://numerical.recipes/whp/notes/CanonCorrBySVD.pdf
    .. [*] http://www.csun.edu/~ata20315/psy524/docs/Psy524%20Lecture%208%20CC.pdf
    .. [*] http://www.mathematica-journal.com/2014/06/canonical-correlation-analysis/
    """
    def __init__(self, endog, exog, tolerance: float = 1e-08, missing: str = 'none', hasconst: Incomplete | None = None, **kwargs) -> None: ...
    def corr_test(self):
        """Approximate F test
        Perform multivariate statistical tests of the hypothesis that
        there is no canonical correlation between endog and exog.
        For each canonical correlation, testing its significance based on
        Wilks' lambda.

        Returns
        -------
        CanCorrTestResults instance
        """

class CanCorrTestResults:
    """
    Canonical correlation results class

    Attributes
    ----------
    stats : DataFrame
        Contain statistical tests results for each canonical correlation
    stats_mv : DataFrame
        Contain the multivariate statistical tests results
    """
    stats: Incomplete
    stats_mv: Incomplete
    def __init__(self, stats, stats_mv) -> None: ...
    def summary(self): ...
