from .descriptive import _OptFuncts
from _typeshed import Incomplete

class _ANOVAOpt(_OptFuncts):
    """

    Class containing functions that are optimized over when
    conducting ANOVA.
    """

class ANOVA(_ANOVAOpt):
    """
    A class for ANOVA and comparing means.

    Parameters
    ----------

    endog : list of arrays
        endog should be a list containing 1 dimensional arrays.  Each array
        is the data collected from a certain group.
    """
    endog: Incomplete
    num_groups: Incomplete
    nobs: int
    def __init__(self, endog) -> None: ...
    def compute_ANOVA(self, mu: Incomplete | None = None, mu_start: int = 0, return_weights: int = 0):
        """
        Returns -2 log likelihood, the pvalue and the maximum likelihood
        estimate for a common mean.

        Parameters
        ----------

        mu : float
            If a mu is specified, ANOVA is conducted with mu as the
            common mean.  Otherwise, the common mean is the maximum
            empirical likelihood estimate of the common mean.
            Default is None.

        mu_start : float
            Starting value for commean mean if specific mu is not specified.
            Default = 0.

        return_weights : bool
            if TRUE, returns the weights on observations that maximize the
            likelihood.  Default is FALSE.

        Returns
        -------

        res: tuple
            The log-likelihood, p-value and estimate for the common mean.
        """
