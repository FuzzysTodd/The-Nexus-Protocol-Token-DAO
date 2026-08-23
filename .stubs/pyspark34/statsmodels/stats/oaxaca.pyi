from _typeshed import Incomplete
from statsmodels.regression.linear_model import OLS as OLS
from statsmodels.tools.tools import add_constant as add_constant

class OaxacaBlinder:
    """
    Class to perform Oaxaca-Blinder Decomposition.

    Parameters
    ----------
    endog : array_like
        The endogenous variable or the dependent variable that you are trying
        to explain.
    exog : array_like
        The exogenous variable(s) or the independent variable(s) that you are
        using to explain the endogenous variable.
    bifurcate : {int, str}
        The column of the exogenous variable(s) on which to split. This would
        generally be the group that you wish to explain the two means for.
        Int of the column for a NumPy array or int/string for the name of
        the column in Pandas.
    hasconst : bool, optional
        Indicates whether the two exogenous variables include a user-supplied
        constant. If True, a constant is assumed. If False, a constant is added
        at the start. If nothing is supplied, then True is assumed.
    swap : bool, optional
        Imitates the STATA Oaxaca command by allowing users to choose to swap
        groups. Unlike STATA, this is assumed to be True instead of False
    cov_type : str, optional
        See regression.linear_model.RegressionResults for a description of the
        available covariance estimators
    cov_kwds : dict, optional
        See linear_model.RegressionResults.get_robustcov_results for a
        description required keywords for alternative covariance estimators

    Notes
    -----
    Please check if your data includes at constant. This will still run, but
    will return incorrect values if set incorrectly.

    You can access the models by using their code as an attribute, e.g.,
    _t_model for the total model, _f_model for the first model, _s_model for
    the second model.

    Examples
    --------
    >>> import numpy as np
    >>> import statsmodels.api as sm
    >>> data = sm.datasets.ccards.load()

    '3' is the column of which we want to explain or which indicates
    the two groups. In this case, it is if you rent.

    >>> model = sm.OaxacaBlinder(df.endog, df.exog, 3, hasconst = False)
    >>> model.two_fold().summary()
    Oaxaca-Blinder Two-fold Effects
    Unexplained Effect: 27.94091
    Explained Effect: 130.80954
    Gap: 158.75044

    >>> model.three_fold().summary()
    Oaxaca-Blinder Three-fold Effects
    Endowments Effect: 321.74824
    Coefficient Effect: 75.45371
    Interaction Effect: -238.45151
    Gap: 158.75044
    """
    two_fold_type: Incomplete
    bifurcate: Incomplete
    cov_type: Incomplete
    cov_kwds: Incomplete
    neumark: Incomplete
    exog: Incomplete
    hasconst: Incomplete
    bi_col: Incomplete
    endog: Incomplete
    gap: Incomplete
    bi: Incomplete
    exog_f_mean: Incomplete
    exog_s_mean: Incomplete
    def __init__(self, endog, exog, bifurcate, hasconst: bool = True, swap: bool = True, cov_type: str = 'nonrobust', cov_kwds: Incomplete | None = None) -> None: ...
    def variance(self, decomp_type, n: int = 5000, conf: float = 0.99):
        """
        A helper function to calculate the variance/std. Used to keep
        the decomposition functions cleaner
        """
    submitted_n: Incomplete
    submitted_conf: Incomplete
    submitted_weight: Incomplete
    endow_eff: Incomplete
    coef_eff: Incomplete
    int_eff: Incomplete
    def three_fold(self, std: bool = False, n: Incomplete | None = None, conf: Incomplete | None = None):
        """
        Calculates the three-fold Oaxaca Blinder Decompositions

        Parameters
        ----------
        std: boolean, optional
            If true, bootstrapped standard errors will be calculated.
        n: int, optional
            A amount of iterations to calculate the bootstrapped
            standard errors. This defaults to 5000.
        conf: float, optional
            This is the confidence required for the standard error
            calculation. Defaults to .99, but could be anything less
            than or equal to one. One is heavy discouraged, due to the
            extreme outliers inflating the variance.

        Returns
        -------
        OaxacaResults
            A results container for the three-fold decomposition.
        """
    t_params: Incomplete
    unexplained: Incomplete
    explained: Incomplete
    def two_fold(self, std: bool = False, two_fold_type: str = 'pooled', submitted_weight: Incomplete | None = None, n: Incomplete | None = None, conf: Incomplete | None = None):
        """
        Calculates the two-fold or pooled Oaxaca Blinder Decompositions

        Methods
        -------
        std: boolean, optional
            If true, bootstrapped standard errors will be calculated.

        two_fold_type: string, optional
            This method allows for the specific calculation of the
            non-discriminatory model. There are four different types
            available at this time. pooled, cotton, reimers, self_submitted.
            Pooled is assumed and if a non-viable parameter is given,
            pooled will be ran.

            pooled - This type assumes that the pooled model's parameters
            (a normal regression) is the non-discriminatory model.
            This includes the indicator variable. This is generally
            the best idea. If you have economic justification for
            using others, then use others.

            nuemark - This is similar to the pooled type, but the regression
            is not done including the indicator variable.

            cotton - This type uses the adjusted in Cotton (1988), which
            accounts for the undervaluation of one group causing the
            overevalution of another. It uses the sample size weights for
            a linear combination of the two model parameters

            reimers - This type uses a linear combination of the two
            models with both parameters being 50% of the
            non-discriminatory model.

            self_submitted - This allows the user to submit their
            own weights. Please be sure to put the weight of the larger mean
            group only. This should be submitted in the
            submitted_weights variable.

        submitted_weight: int/float, required only for self_submitted,
            This is the submitted weight for the larger mean. If the
            weight for the larger mean is p, then the weight for the
            other mean is 1-p. Only submit the first value.

        n: int, optional
            A amount of iterations to calculate the bootstrapped
            standard errors. This defaults to 5000.
        conf: float, optional
            This is the confidence required for the standard error
            calculation. Defaults to .99, but could be anything less
            than or equal to one. One is heavy discouraged, due to the
            extreme outliers inflating the variance.

        Returns
        -------
        OaxacaResults
            A results container for the two-fold decomposition.
        """

class OaxacaResults:
    """
    This class summarizes the fit of the OaxacaBlinder model.

    Use .summary() to get a table of the fitted values or
    use .params to receive a list of the values
    use .std to receive a list of the standard errors

    If a two-fold model was fitted, this will return
    unexplained effect, explained effect, and the
    mean gap. The list will always be of the following order
    and type. If standard error was asked for, then standard error
    calculations will also be included for each variable after each
    calculated effect.

    unexplained : float
        This is the effect that cannot be explained by the data at hand.
        This does not mean it cannot be explained with more.
    explained : float
        This is the effect that can be explained using the data.
    gap : float
        This is the gap in the mean differences of the two groups.

    If a three-fold model was fitted, this will
    return characteristic effect, coefficient effect
    interaction effect, and the mean gap. The list will
    be of the following order and type. If standard error was asked
    for, then standard error calculations will also be included for
    each variable after each calculated effect.

    endowment effect : float
        This is the effect due to the group differences in
        predictors
    coefficient effect : float
        This is the effect due to differences of the coefficients
        of the two groups
    interaction effect : float
        This is the effect due to differences in both effects
        existing at the same time between the two groups.
    gap : float
        This is the gap in the mean differences of the two groups.

    Attributes
    ----------
    params
        A list of all values for the fitted models.
    std
        A list of standard error calculations.
    """
    params: Incomplete
    std: Incomplete
    model_type: Incomplete
    def __init__(self, results, model_type, std_val: Incomplete | None = None) -> None: ...
    def summary(self) -> None:
        """
        Print a summary table with the Oaxaca-Blinder effects
        """
