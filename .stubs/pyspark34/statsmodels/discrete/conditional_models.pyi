import statsmodels.base.model as base
import statsmodels.regression.linear_model as lm
from _typeshed import Incomplete
from statsmodels.discrete.discrete_model import MultinomialResults as MultinomialResults, MultinomialResultsWrapper as MultinomialResultsWrapper

class _ConditionalModel(base.LikelihoodModel):
    k_params: Incomplete
    nobs: int
    def __init__(self, endog, exog, missing: str = 'none', **kwargs) -> None: ...
    def hessian(self, params): ...
    def fit(self, start_params: Incomplete | None = None, method: str = 'BFGS', maxiter: int = 100, full_output: bool = True, disp: bool = False, fargs=(), callback: Incomplete | None = None, retall: bool = False, skip_hessian: bool = False, **kwargs): ...
    def fit_regularized(self, method: str = 'elastic_net', alpha: float = 0.0, start_params: Incomplete | None = None, refit: bool = False, **kwargs):
        """
        Return a regularized fit to a linear regression model.

        Parameters
        ----------
        method : {'elastic_net'}
            Only the `elastic_net` approach is currently implemented.
        alpha : scalar or array_like
            The penalty weight.  If a scalar, the same penalty weight
            applies to all variables in the model.  If a vector, it
            must have the same length as `params`, and contains a
            penalty weight for each coefficient.
        start_params : array_like
            Starting values for `params`.
        refit : bool
            If True, the model is refit using only the variables that
            have non-zero coefficients in the regularized fit.  The
            refitted model is not regularized.
        **kwargs
            Additional keyword argument that are used when fitting the model.

        Returns
        -------
        Results
            A results instance.
        """
    @classmethod
    def from_formula(cls, formula, data, subset: Incomplete | None = None, drop_cols: Incomplete | None = None, *args, **kwargs): ...

class ConditionalLogit(_ConditionalModel):
    """
    Fit a conditional logistic regression model to grouped data.

    Every group is implicitly given an intercept, but the model is fit using
    a conditional likelihood in which the intercepts are not present.  Thus,
    intercept estimates are not given, but the other parameter estimates can
    be interpreted as being adjusted for any group-level confounders.

    Parameters
    ----------
    endog : array_like
        The response variable, must contain only 0 and 1.
    exog : array_like
        The array of covariates.  Do not include an intercept
        in this array.
    groups : array_like
        Codes defining the groups. This is a required keyword parameter.
    """
    K: Incomplete
    def __init__(self, endog, exog, missing: str = 'none', **kwargs) -> None: ...
    def loglike(self, params): ...
    def score(self, params): ...
    def loglike_grp(self, grp, params): ...
    def score_grp(self, grp, params): ...

class ConditionalPoisson(_ConditionalModel):
    """
    Fit a conditional Poisson regression model to grouped data.

    Every group is implicitly given an intercept, but the model is fit using
    a conditional likelihood in which the intercepts are not present.  Thus,
    intercept estimates are not given, but the other parameter estimates can
    be interpreted as being adjusted for any group-level confounders.

    Parameters
    ----------
    endog : array_like
        The response variable
    exog : array_like
        The covariates
    groups : array_like
        Codes defining the groups. This is a required keyword parameter.
    """
    def loglike(self, params): ...
    def score(self, params): ...

class ConditionalResults(base.LikelihoodModelResults):
    def __init__(self, model, params, normalized_cov_params, scale) -> None: ...
    def summary(self, yname: Incomplete | None = None, xname: Incomplete | None = None, title: Incomplete | None = None, alpha: float = 0.05):
        '''
        Summarize the fitted model.

        Parameters
        ----------
        yname : str, optional
            Default is `y`
        xname : list[str], optional
            Names for the exogenous variables, default is "var_xx".
            Must match the number of parameters in the model
        title : str, optional
            Title for the top table. If not None, then this replaces the
            default title
        alpha : float
            Significance level for the confidence intervals

        Returns
        -------
        smry : Summary instance
            This holds the summary tables and text, which can be printed or
            converted to various output formats.

        See Also
        --------
        statsmodels.iolib.summary.Summary : class to hold summary
            results
        '''

class ConditionalMNLogit(_ConditionalModel):
    """
    Fit a conditional multinomial logit model to grouped data.

    Parameters
    ----------
    endog : array_like
        The dependent variable, must be integer-valued, coded
        0, 1, ..., c-1, where c is the number of response
        categories.
    exog : array_like
        The independent variables.
    groups : array_like
        Codes defining the groups. This is a required keyword parameter.

    Notes
    -----
    Equivalent to femlogit in Stata.

    References
    ----------
    Gary Chamberlain (1980).  Analysis of covariance with qualitative
    data. The Review of Economic Studies.  Vol. 47, No. 1, pp. 225-238.
    """
    endog: Incomplete
    k_cat: Incomplete
    df_model: Incomplete
    df_resid: Incomplete
    J: Incomplete
    K: Incomplete
    def __init__(self, endog, exog, missing: str = 'none', **kwargs) -> None: ...
    def fit(self, start_params: Incomplete | None = None, method: str = 'BFGS', maxiter: int = 100, full_output: bool = True, disp: bool = False, fargs=(), callback: Incomplete | None = None, retall: bool = False, skip_hessian: bool = False, **kwargs): ...
    def loglike(self, params): ...
    def score(self, params): ...

class ConditionalResultsWrapper(lm.RegressionResultsWrapper): ...
