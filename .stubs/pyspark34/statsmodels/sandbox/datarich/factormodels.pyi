from _typeshed import Incomplete
from statsmodels.sandbox.tools import pca as pca
from statsmodels.sandbox.tools.cross_val import LeaveOneOut as LeaveOneOut

class FactorModelUnivariate:
    """

    Todo:
    check treatment of const, make it optional ?
        add hasconst (0 or 1), needed when selecting nfact+hasconst
    options are arguments in calc_factors, should be more public instead
    cross-validation is slow for large number of observations
    """
    endog: Incomplete
    exog: Incomplete
    def __init__(self, endog, exog) -> None: ...
    exog_reduced: Incomplete
    factors: Incomplete
    hasconst: int
    evals: Incomplete
    evecs: Incomplete
    def calc_factors(self, x: Incomplete | None = None, keepdim: int = 0, addconst: bool = True) -> None:
        """get factor decomposition of exogenous variables

        This uses principal component analysis to obtain the factors. The number
        of factors kept is the maximum that will be considered in the regression.
        """
    def fit_fixed_nfact(self, nfact): ...
    results_find_nfact: Incomplete
    best_nfact: Incomplete
    def fit_find_nfact(self, maxfact: Incomplete | None = None, skip_crossval: bool = True, cv_iter: Incomplete | None = None) -> None:
        """estimate the model and selection criteria for up to maxfact factors

        The selection criteria that are calculated are AIC, BIC, and R2_adj. and
        additionally cross-validation prediction error sum of squares if `skip_crossval`
        is false. Cross-validation is not used by default because it can be
        time consuming to calculate.

        By default the cross-validation method is Leave-one-out on the full dataset.
        A different cross-validation sample can be specified as an argument to
        cv_iter.

        Results are attached in `results_find_nfact`



        """
    def summary_find_nfact(self):
        """provides a summary for the selection of the number of factors

        Returns
        -------
        sumstr : str
            summary of the results for selecting the number of factors

        """
