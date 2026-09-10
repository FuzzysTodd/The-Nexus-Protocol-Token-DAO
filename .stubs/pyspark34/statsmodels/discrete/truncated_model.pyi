import statsmodels.regression.linear_model as lm
from _typeshed import Incomplete
from statsmodels.discrete.discrete_model import CountModel, CountResults, L1CountResults

__all__ = ['TruncatedLFPoisson', 'TruncatedLFNegativeBinomialP', 'HurdleCountModel']

class TruncatedLFGeneric(CountModel):
    __doc__: Incomplete
    exog: Incomplete
    endog: Incomplete
    offset: Incomplete
    exposure: Incomplete
    trunc: Incomplete
    truncation: Incomplete
    def __init__(self, endog, exog, truncation: int = 0, offset: Incomplete | None = None, exposure: Incomplete | None = None, missing: str = 'none', **kwargs) -> None: ...
    def loglike(self, params):
        """
        Loglikelihood of Generic Truncated model

        Parameters
        ----------
        params : array-like
            The parameters of the model.

        Returns
        -------
        loglike : float
            The log-likelihood function of the model evaluated at `params`.
            See notes.

        Notes
        -----

        """
    def loglikeobs(self, params):
        """
        Loglikelihood for observations of Generic Truncated model

        Parameters
        ----------
        params : array-like
            The parameters of the model.

        Returns
        -------
        loglike : ndarray (nobs,)
            The log likelihood for each observation of the model evaluated
            at `params`. See Notes

        Notes
        -----

        """
    def score_obs(self, params):
        """
        Generic Truncated model score (gradient) vector of the log-likelihood

        Parameters
        ----------
        params : array-like
            The parameters of the model

        Returns
        -------
        score : ndarray, 1-D
            The score vector of the model, i.e. the first derivative of the
            loglikelihood function, evaluated at `params`
        """
    def score(self, params):
        """
        Generic Truncated model score (gradient) vector of the log-likelihood

        Parameters
        ----------
        params : array-like
            The parameters of the model

        Returns
        -------
        score : ndarray, 1-D
            The score vector of the model, i.e. the first derivative of the
            loglikelihood function, evaluated at `params`
        """
    df_resid: Incomplete
    def fit(self, start_params: Incomplete | None = None, method: str = 'bfgs', maxiter: int = 35, full_output: int = 1, disp: int = 1, callback: Incomplete | None = None, cov_type: str = 'nonrobust', cov_kwds: Incomplete | None = None, use_t: Incomplete | None = None, **kwargs): ...
    def fit_regularized(self, start_params: Incomplete | None = None, method: str = 'l1', maxiter: str = 'defined_by_method', full_output: int = 1, disp: int = 1, callback: Incomplete | None = None, alpha: int = 0, trim_mode: str = 'auto', auto_trim_tol: float = 0.01, size_trim_tol: float = 0.0001, qc_tol: float = 0.03, **kwargs): ...
    def hessian(self, params):
        """
        Generic Truncated model Hessian matrix of the loglikelihood

        Parameters
        ----------
        params : array-like
            The parameters of the model

        Returns
        -------
        hess : ndarray, (k_vars, k_vars)
            The Hessian, second derivative of loglikelihood function,
            evaluated at `params`

        Notes
        -----
        """
    def predict(self, params, exog: Incomplete | None = None, exposure: Incomplete | None = None, offset: Incomplete | None = None, which: str = 'mean', y_values: Incomplete | None = None):
        '''
        Predict response variable or other statistic given exogenous variables.

        Parameters
        ----------
        params : array_like
            The parameters of the model.
        exog : ndarray, optional
            Explanatory variables for the main count model.
            If ``exog`` is None, then the data from the model will be used.
        offset : ndarray, optional
            Offset is added to the linear predictor of the mean function with
            coefficient equal to 1.
            Default is zero if exog is not None, and the model offset if exog
            is None.
        exposure : ndarray, optional
            Log(exposure) is added to the linear predictor with coefficient
            equal to 1. If exposure is specified, then it will be logged by
            the method. The user does not need to log it first.
            Default is one if exog is is not None, and it is the model exposure
            if exog is None.
        which : str (optional)
            Statitistic to predict. Default is \'mean\'.

            - \'mean\' : the conditional expectation of endog E(y | x)
            - \'mean-main\' : mean parameter of truncated count model.
              Note, this is not the mean of the truncated distribution.
            - \'linear\' : the linear predictor of the truncated count model.
            - \'var\' : returns the estimated variance of endog implied by the
              model.
            - \'prob-trunc\' : probability of truncation. This is the probability
              of observing a zero count implied
              by the truncation model.
            - \'prob\' : probabilities of each count from 0 to max(endog), or
              for y_values if those are provided. This is a multivariate
              return (2-dim when predicting for several observations).
              The probabilities in the truncated region are zero.
            - \'prob-base\' : probabilities for untruncated base distribution.
              The probabilities are for each count from 0 to max(endog), or
              for y_values if those are provided. This is a multivariate
              return (2-dim when predicting for several observations).


        y_values : array_like
            Values of the random variable endog at which pmf is evaluated.
            Only used if ``which="prob"``

        Returns
        -------
        predicted values

        Notes
        -----
        If exposure is specified, then it will be logged by the method.
        The user does not need to log it first.
        '''

class TruncatedLFPoisson(TruncatedLFGeneric):
    __doc__: Incomplete
    model_main: Incomplete
    model_dist: Incomplete
    result_class: Incomplete
    result_class_wrapper: Incomplete
    result_class_reg: Incomplete
    result_class_reg_wrapper: Incomplete
    def __init__(self, endog, exog, offset: Incomplete | None = None, exposure: Incomplete | None = None, truncation: int = 0, missing: str = 'none', **kwargs) -> None: ...

class TruncatedLFNegativeBinomialP(TruncatedLFGeneric):
    __doc__: Incomplete
    model_main: Incomplete
    k_extra: Incomplete
    model_dist: Incomplete
    result_class: Incomplete
    result_class_wrapper: Incomplete
    result_class_reg: Incomplete
    result_class_reg_wrapper: Incomplete
    def __init__(self, endog, exog, offset: Incomplete | None = None, exposure: Incomplete | None = None, truncation: int = 0, p: int = 2, missing: str = 'none', **kwargs) -> None: ...

class TruncatedLFGeneralizedPoisson(TruncatedLFGeneric):
    __doc__: Incomplete
    model_main: Incomplete
    k_extra: Incomplete
    model_dist: Incomplete
    result_class: Incomplete
    result_class_wrapper: Incomplete
    result_class_reg: Incomplete
    result_class_reg_wrapper: Incomplete
    def __init__(self, endog, exog, offset: Incomplete | None = None, exposure: Incomplete | None = None, truncation: int = 0, p: int = 2, missing: str = 'none', **kwargs) -> None: ...

class _RCensoredGeneric(CountModel):
    __doc__: Incomplete
    zero_idx: Incomplete
    nonzero_idx: Incomplete
    def __init__(self, endog, exog, offset: Incomplete | None = None, exposure: Incomplete | None = None, missing: str = 'none', **kwargs) -> None: ...
    def loglike(self, params):
        """
        Loglikelihood of Generic Censored model

        Parameters
        ----------
        params : array-like
            The parameters of the model.

        Returns
        -------
        loglike : float
            The log-likelihood function of the model evaluated at `params`.
            See notes.

        Notes
        -----

        """
    def loglikeobs(self, params):
        """
        Loglikelihood for observations of Generic Censored model

        Parameters
        ----------
        params : array-like
            The parameters of the model.

        Returns
        -------
        loglike : ndarray (nobs,)
            The log likelihood for each observation of the model evaluated
            at `params`. See Notes

        Notes
        -----

        """
    def score_obs(self, params):
        """
        Generic Censored model score (gradient) vector of the log-likelihood

        Parameters
        ----------
        params : array-like
            The parameters of the model

        Returns
        -------
        score : ndarray, 1-D
            The score vector of the model, i.e. the first derivative of the
            loglikelihood function, evaluated at `params`
        """
    def score(self, params):
        """
        Generic Censored model score (gradient) vector of the log-likelihood

        Parameters
        ----------
        params : array-like
            The parameters of the model

        Returns
        -------
        score : ndarray, 1-D
            The score vector of the model, i.e. the first derivative of the
            loglikelihood function, evaluated at `params`
        """
    def fit(self, start_params: Incomplete | None = None, method: str = 'bfgs', maxiter: int = 35, full_output: int = 1, disp: int = 1, callback: Incomplete | None = None, cov_type: str = 'nonrobust', cov_kwds: Incomplete | None = None, use_t: Incomplete | None = None, **kwargs): ...
    def fit_regularized(self, start_params: Incomplete | None = None, method: str = 'l1', maxiter: str = 'defined_by_method', full_output: int = 1, disp: int = 1, callback: Incomplete | None = None, alpha: int = 0, trim_mode: str = 'auto', auto_trim_tol: float = 0.01, size_trim_tol: float = 0.0001, qc_tol: float = 0.03, **kwargs): ...
    def hessian(self, params):
        """
        Generic Censored model Hessian matrix of the loglikelihood

        Parameters
        ----------
        params : array-like
            The parameters of the model

        Returns
        -------
        hess : ndarray, (k_vars, k_vars)
            The Hessian, second derivative of loglikelihood function,
            evaluated at `params`

        Notes
        -----
        """

class _RCensoredPoisson(_RCensoredGeneric):
    __doc__: Incomplete
    model_main: Incomplete
    model_dist: Incomplete
    result_class: Incomplete
    result_class_wrapper: Incomplete
    result_class_reg: Incomplete
    result_class_reg_wrapper: Incomplete
    def __init__(self, endog, exog, offset: Incomplete | None = None, exposure: Incomplete | None = None, missing: str = 'none', **kwargs) -> None: ...

class _RCensoredGeneralizedPoisson(_RCensoredGeneric):
    __doc__: Incomplete
    model_main: Incomplete
    model_dist: Incomplete
    result_class: Incomplete
    result_class_wrapper: Incomplete
    result_class_reg: Incomplete
    result_class_reg_wrapper: Incomplete
    def __init__(self, endog, exog, offset: Incomplete | None = None, p: int = 2, exposure: Incomplete | None = None, missing: str = 'none', **kwargs) -> None: ...

class _RCensoredNegativeBinomialP(_RCensoredGeneric):
    __doc__: Incomplete
    model_main: Incomplete
    model_dist: Incomplete
    result_class: Incomplete
    result_class_wrapper: Incomplete
    result_class_reg: Incomplete
    result_class_reg_wrapper: Incomplete
    def __init__(self, endog, exog, offset: Incomplete | None = None, p: int = 2, exposure: Incomplete | None = None, missing: str = 'none', **kwargs) -> None: ...

class _RCensored(_RCensoredGeneric):
    __doc__: Incomplete
    model_main: Incomplete
    model_dist: Incomplete
    k_extra: Incomplete
    result_class: Incomplete
    result_class_wrapper: Incomplete
    result_class_reg: Incomplete
    result_class_reg_wrapper: Incomplete
    def __init__(self, endog, exog, model=..., distribution=..., offset: Incomplete | None = None, exposure: Incomplete | None = None, missing: str = 'none', **kwargs) -> None: ...

class HurdleCountModel(CountModel):
    __doc__: Incomplete
    k_extra1: int
    k_extra2: int
    result_class: Incomplete
    result_class_wrapper: Incomplete
    result_class_reg: Incomplete
    result_class_reg_wrapper: Incomplete
    def __init__(self, endog, exog, offset: Incomplete | None = None, dist: str = 'poisson', zerodist: str = 'poisson', p: int = 2, pzero: int = 2, exposure: Incomplete | None = None, missing: str = 'none', **kwargs) -> None: ...
    def loglike(self, params):
        """
        Loglikelihood of Generic Hurdle model

        Parameters
        ----------
        params : array-like
            The parameters of the model.

        Returns
        -------
        loglike : float
            The log-likelihood function of the model evaluated at `params`.
            See notes.

        Notes
        -----

        """
    k_extra: Incomplete
    def fit(self, start_params: Incomplete | None = None, method: str = 'bfgs', maxiter: int = 35, full_output: int = 1, disp: int = 1, callback: Incomplete | None = None, cov_type: str = 'nonrobust', cov_kwds: Incomplete | None = None, use_t: Incomplete | None = None, **kwargs): ...
    def predict(self, params, exog: Incomplete | None = None, exposure: Incomplete | None = None, offset: Incomplete | None = None, which: str = 'mean', y_values: Incomplete | None = None):
        '''
        Predict response variable or other statistic given exogenous variables.

        Parameters
        ----------
        params : array_like
            The parameters of the model.
        exog : ndarray, optional
            Explanatory variables for the main count model.
            If ``exog`` is None, then the data from the model will be used.
        exog_infl : ndarray, optional
            Explanatory variables for the zero-inflation model.
            ``exog_infl`` has to be provided if ``exog`` was provided unless
            ``exog_infl`` in the model is only a constant.
        offset : ndarray, optional
            Offset is added to the linear predictor of the mean function with
            coefficient equal to 1.
            Default is zero if exog is not None, and the model offset if exog
            is None.
        exposure : ndarray, optional
            Log(exposure) is added to the linear predictor with coefficient
            equal to 1. If exposure is specified, then it will be logged by
            the method. The user does not need to log it first.
            Default is one if exog is is not None, and it is the model exposure
            if exog is None.
        which : str (optional)
            Statitistic to predict. Default is \'mean\'.

            - \'mean\' : the conditional expectation of endog E(y | x)
            - \'mean-main\' : mean parameter of truncated count model.
              Note, this is not the mean of the truncated distribution.
            - \'linear\' : the linear predictor of the truncated count model.
            - \'var\' : returns the estimated variance of endog implied by the
              model.
            - \'prob-main\' : probability of selecting the main model which is
              the probability of observing a nonzero count P(y > 0 | x).
            - \'prob-zero\' : probability of observing a zero count. P(y=0 | x).
              This is equal to is ``1 - prob-main``
            - \'prob-trunc\' : probability of truncation of the truncated count
              model. This is the probability of observing a zero count implied
              by the truncation model.
            - \'mean-nonzero\' : expected value conditional on having observation
              larger than zero, E(y | X, y>0)
            - \'prob\' : probabilities of each count from 0 to max(endog), or
              for y_values if those are provided. This is a multivariate
              return (2-dim when predicting for several observations).

        y_values : array_like
            Values of the random variable endog at which pmf is evaluated.
            Only used if ``which="prob"``

        Returns
        -------
        predicted values

        Notes
        -----
        \'prob-zero\' / \'prob-trunc\' is the ratio of probabilities of observing
        a zero count between hurdle model and the truncated count model.
        If this ratio is larger than one, then the hurdle model has an inflated
        number of zeros compared to the count model. If it is smaller than one,
        then the number of zeros is deflated.
        '''

class TruncatedLFGenericResults(CountResults):
    __doc__: Incomplete

class TruncatedLFPoissonResults(TruncatedLFGenericResults):
    __doc__: Incomplete

class TruncatedNegativeBinomialResults(TruncatedLFGenericResults):
    __doc__: Incomplete

class L1TruncatedLFGenericResults(L1CountResults, TruncatedLFGenericResults): ...
class TruncatedLFGenericResultsWrapper(lm.RegressionResultsWrapper): ...
class L1TruncatedLFGenericResultsWrapper(lm.RegressionResultsWrapper): ...

class HurdleCountResults(CountResults):
    __doc__: Incomplete
    results_zero: Incomplete
    results_count: Incomplete
    df_resid: Incomplete
    def __init__(self, model, mlefit, results_zero, results_count, cov_type: str = 'nonrobust', cov_kwds: Incomplete | None = None, use_t: Incomplete | None = None) -> None: ...
    def llnull(self): ...
    def bse(self): ...

class L1HurdleCountResults(L1CountResults, HurdleCountResults): ...
class HurdleCountResultsWrapper(lm.RegressionResultsWrapper): ...
class L1HurdleCountResultsWrapper(lm.RegressionResultsWrapper): ...
