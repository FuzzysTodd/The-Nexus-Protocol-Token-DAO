from _typeshed import Incomplete
from statsmodels.base.model import Model as Model
from statsmodels.compat.pandas import Substitution as Substitution
from statsmodels.iolib import summary2 as summary2

__docformat__: str

def multivariate_stats(eigenvals, r_err_sscp, r_contrast, df_resid, tolerance: float = 1e-08):
    """
    For multivariate linear model Y = X * B
    Testing hypotheses
        L*B*M = 0
    where L is contrast matrix, B is the parameters of the
    multivariate linear model and M is dependent variable transform matrix.
        T = L*inv(X'X)*L'
        H = M'B'L'*inv(T)*LBM
        E =  M'(Y'Y - B'X'XB)M

    Parameters
    ----------
    eigenvals : ndarray
        The eigenvalues of inv(E + H)*H
    r_err_sscp : int
        Rank of E + H
    r_contrast : int
        Rank of T matrix
    df_resid : int
        Residual degree of freedom (n_samples minus n_variables of X)
    tolerance : float
        smaller than which eigenvalue is considered 0

    Returns
    -------
    A DataFrame

    References
    ----------
    .. [*] https://support.sas.com/documentation/cdl/en/statug/63033/HTML/default/viewer.htm#statug_introreg_sect012.htm
    """

class _MultivariateOLS(Model):
    """
    Multivariate linear model via least squares


    Parameters
    ----------
    endog : array_like
        Dependent variables. A nobs x k_endog array where nobs is
        the number of observations and k_endog is the number of dependent
        variables
    exog : array_like
        Independent variables. A nobs x k_exog array where nobs is the
        number of observations and k_exog is the number of independent
        variables. An intercept is not included by default and should be added
        by the user (models specified using a formula include an intercept by
        default)

    Attributes
    ----------
    endog : ndarray
        See Parameters.
    exog : ndarray
        See Parameters.
    """
    def __init__(self, endog, exog, missing: str = 'none', hasconst: Incomplete | None = None, **kwargs) -> None: ...
    def fit(self, method: str = 'svd'): ...

class _MultivariateOLSResults:
    """
    _MultivariateOLS results class
    """
    design_info: Incomplete
    exog_names: Incomplete
    endog_names: Incomplete
    def __init__(self, fitted_mv_ols) -> None: ...
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
        results: _MultivariateOLSResults

        Notes
        -----
        Tests hypotheses of the form

            L * params * M = C

        where `params` is the regression coefficient matrix for the
        linear model y = x * params, `L` is the contrast matrix, `M` is the
        dependent variable transform matrix and C is the constant matrix.
        """
    def summary(self) -> None: ...

class MultivariateTestResults:
    """
    Multivariate test results class

    Returned by `mv_test` method of `_MultivariateOLSResults` class

    Parameters
    ----------
    results : dict[str, dict]
        Dictionary containing test results. See the description
        below for the expected format.
    endog_names : sequence[str]
        A list or other sequence of endogenous variables names
    exog_names : sequence[str]
        A list of other sequence of exogenous variables names

    Attributes
    ----------
    results : dict
        Each hypothesis is contained in a single`key`. Each test must
        have the following keys:

        * 'stat' - contains the multivariate test results
        * 'contrast_L' - contains the contrast_L matrix
        * 'transform_M' - contains the transform_M matrix
        * 'constant_C' - contains the constant_C matrix
        * 'H' - contains an intermediate Hypothesis matrix,
          or the between groups sums of squares and cross-products matrix,
          corresponding to the numerator of the univariate F test.
        * 'E' - contains an intermediate Error matrix,
          corresponding to the denominator of the univariate F test.
          The Hypotheses and Error matrices can be used to calculate
          the same test statistics in 'stat', as well as to calculate
          the discriminant function (canonical correlates) from the
          eigenvectors of inv(E)H.

    endog_names : list[str]
        The endogenous names
    exog_names : list[str]
        The exogenous names
    summary_frame : DataFrame
        Returns results as a MultiIndex DataFrame
    """
    results: Incomplete
    endog_names: Incomplete
    exog_names: Incomplete
    def __init__(self, results, endog_names, exog_names) -> None: ...
    def __getitem__(self, item): ...
    @property
    def summary_frame(self):
        """
        Return results as a multiindex dataframe
        """
    def summary(self, show_contrast_L: bool = False, show_transform_M: bool = False, show_constant_C: bool = False):
        """
        Summary of test results

        Parameters
        ----------
        show_contrast_L : bool
            Whether to show contrast_L matrix
        show_transform_M : bool
            Whether to show transform_M matrix
        show_constant_C : bool
            Whether to show the constant_C
        """
