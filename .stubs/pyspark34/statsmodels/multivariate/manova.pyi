from .multivariate_ols import MultivariateTestResults as MultivariateTestResults
from _typeshed import Incomplete
from statsmodels.base.model import Model as Model
from statsmodels.compat.pandas import Substitution as Substitution

__docformat__: str

class MANOVA(Model):
    """
    Multivariate Analysis of Variance

    The implementation of MANOVA is based on multivariate regression and does
    not assume that the explanatory variables are categorical. Any type of
    variables as in regression is allowed.

    Parameters
    ----------
    endog : array_like
        Dependent variables. A nobs x k_endog array where nobs is
        the number of observations and k_endog is the number of dependent
        variables.
    exog : array_like
        Independent variables. A nobs x k_exog array where nobs is the
        number of observations and k_exog is the number of independent
        variables. An intercept is not included by default and should be added
        by the user. Models specified using a formula include an intercept by
        default.

    Attributes
    ----------
    endog : ndarray
        See Parameters.
    exog : ndarray
        See Parameters.

    Notes
    -----
    MANOVA is used though the `mv_test` function, and `fit` is not used.

    The ``from_formula`` interface is the recommended method to specify
    a model and simplifies testing without needing to manually configure
    the contrast matrices.

    References
    ----------
    .. [*] ftp://public.dhe.ibm.com/software/analytics/spss/documentation/
       statistics/20.0/en/client/Manuals/IBM_SPSS_Statistics_Algorithms.pdf
    """
    def __init__(self, endog, exog, missing: str = 'none', hasconst: Incomplete | None = None, **kwargs) -> None: ...
    def fit(self) -> None: ...
    def mv_test(self, hypotheses: Incomplete | None = None, skip_intercept_test: bool = False):
        """
        Linear hypotheses testing

        Parameters
        ----------
        %(hypotheses_doc)s
        skip_intercept_test : bool
            If true, then testing the intercept is skipped, the model is not
            changed.
            Note: If a term has a numerically insignificant effect, then
            an exception because of emtpy arrays may be raised. This can
            happen for the intercept if the data has been demeaned.

        Returns
        -------
        results: MultivariateTestResults

        Notes
        -----
        Testing the linear hypotheses

            L * params * M = 0

        where `params` is the regression coefficient matrix for the
        linear model y = x * params

        If the model is not specified using the formula interfact, then the
        hypotheses test each included exogenous variable, one at a time. In
        most applications with categorical variables, the ``from_formula``
        interface should be preferred when specifying a model since it
        provides knowledge about the model when specifying the hypotheses.
        """
