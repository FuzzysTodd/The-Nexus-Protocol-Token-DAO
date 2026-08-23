import statsmodels.regression.linear_model as lm
from _typeshed import Incomplete
from statsmodels.discrete.discrete_model import CountModel, CountResults, L1CountResults

__all__ = ['ZeroInflatedPoisson', 'ZeroInflatedGeneralizedPoisson', 'ZeroInflatedNegativeBinomialP']

class GenericZeroInflated(CountModel):
    __doc__: Incomplete
    k_inflate: int
    exog_infl: Incomplete
    k_exog: int
    infl: Incomplete
    model_infl: Incomplete
    inflation: Incomplete
    k_extra: Incomplete
    def __init__(self, endog, exog, exog_infl: Incomplete | None = None, offset: Incomplete | None = None, inflation: str = 'logit', exposure: Incomplete | None = None, missing: str = 'none', **kwargs) -> None: ...
    def loglike(self, params):
        """
        Loglikelihood of Generic Zero Inflated model.

        Parameters
        ----------
        params : array_like
            The parameters of the model.

        Returns
        -------
        loglike : float
            The log-likelihood function of the model evaluated at `params`.
            See notes.

        Notes
        -----
        .. math:: \\ln L=\\sum_{y_{i}=0}\\ln(w_{i}+(1-w_{i})*P_{main\\_model})+
            \\sum_{y_{i}>0}(\\ln(1-w_{i})+L_{main\\_model})
            where P - pdf of main model, L - loglike function of main model.
        """
    def loglikeobs(self, params):
        """
        Loglikelihood for observations of Generic Zero Inflated model.

        Parameters
        ----------
        params : array_like
            The parameters of the model.

        Returns
        -------
        loglike : ndarray
            The log likelihood for each observation of the model evaluated
            at `params`. See Notes for definition.

        Notes
        -----
        .. math:: \\ln L=\\ln(w_{i}+(1-w_{i})*P_{main\\_model})+
            \\ln(1-w_{i})+L_{main\\_model}
            where P - pdf of main model, L - loglike function of main model.

        for observations :math:`i=1,...,n`
        """
    def fit(self, start_params: Incomplete | None = None, method: str = 'bfgs', maxiter: int = 35, full_output: int = 1, disp: int = 1, callback: Incomplete | None = None, cov_type: str = 'nonrobust', cov_kwds: Incomplete | None = None, use_t: Incomplete | None = None, **kwargs): ...
    def fit_regularized(self, start_params: Incomplete | None = None, method: str = 'l1', maxiter: str = 'defined_by_method', full_output: int = 1, disp: int = 1, callback: Incomplete | None = None, alpha: int = 0, trim_mode: str = 'auto', auto_trim_tol: float = 0.01, size_trim_tol: float = 0.0001, qc_tol: float = 0.03, **kwargs): ...
    def score_obs(self, params):
        """
        Generic Zero Inflated model score (gradient) vector of the log-likelihood

        Parameters
        ----------
        params : array_like
            The parameters of the model

        Returns
        -------
        score : ndarray, 1-D
            The score vector of the model, i.e. the first derivative of the
            loglikelihood function, evaluated at `params`
        """
    def score(self, params): ...
    def hessian(self, params):
        """
        Generic Zero Inflated model Hessian matrix of the loglikelihood

        Parameters
        ----------
        params : array_like
            The parameters of the model

        Returns
        -------
        hess : ndarray, (k_vars, k_vars)
            The Hessian, second derivative of loglikelihood function,
            evaluated at `params`

        Notes
        -----
        """
    def predict(self, params, exog: Incomplete | None = None, exog_infl: Incomplete | None = None, exposure: Incomplete | None = None, offset: Incomplete | None = None, which: str = 'mean', y_values: Incomplete | None = None):
        '''
        Predict expected response or other statistic given exogenous variables.

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

            - \'mean\' : the conditional expectation of endog E(y | x). This
              takes inflated zeros into account.
            - \'linear\' : the linear predictor of the mean function.
            - \'var\' : returns the estimated variance of endog implied by the
              model.
            - \'mean-main\' : mean of the main count model
            - \'prob-main\' : probability of selecting the main model.
                The probability of zero inflation is ``1 - prob-main``.
            - \'mean-nonzero\' : expected value conditional on having observation
              larger than zero, E(y | X, y>0)
            - \'prob-zero\' : probability of observing a zero count. P(y=0 | x)
            - \'prob\' : probabilities of each count from 0 to max(endog), or
              for y_values if those are provided. This is a multivariate
              return (2-dim when predicting for several observations).

        y_values : array_like
            Values of the random variable endog at which pmf is evaluated.
            Only used if ``which="prob"``
        '''

class ZeroInflatedPoisson(GenericZeroInflated):
    __doc__: Incomplete
    model_main: Incomplete
    distribution: Incomplete
    result_class: Incomplete
    result_class_wrapper: Incomplete
    result_class_reg: Incomplete
    result_class_reg_wrapper: Incomplete
    def __init__(self, endog, exog, exog_infl: Incomplete | None = None, offset: Incomplete | None = None, exposure: Incomplete | None = None, inflation: str = 'logit', missing: str = 'none', **kwargs) -> None: ...
    def get_distribution(self, params, exog: Incomplete | None = None, exog_infl: Incomplete | None = None, exposure: Incomplete | None = None, offset: Incomplete | None = None):
        """Get frozen instance of distribution based on predicted parameters.

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
            Log(exposure) is added to the linear predictor  of the mean
            function with coefficient equal to 1. If exposure is specified,
            then it will be logged by the method. The user does not need to
            log it first.
            Default is one if exog is is not None, and it is the model exposure
            if exog is None.

        Returns
        -------
        Instance of frozen scipy distribution subclass.
        """

class ZeroInflatedGeneralizedPoisson(GenericZeroInflated):
    __doc__: Incomplete
    model_main: Incomplete
    distribution: Incomplete
    result_class: Incomplete
    result_class_wrapper: Incomplete
    result_class_reg: Incomplete
    result_class_reg_wrapper: Incomplete
    def __init__(self, endog, exog, exog_infl: Incomplete | None = None, offset: Incomplete | None = None, exposure: Incomplete | None = None, inflation: str = 'logit', p: int = 2, missing: str = 'none', **kwargs) -> None: ...
    def get_distribution(self, params, exog: Incomplete | None = None, exog_infl: Incomplete | None = None, exposure: Incomplete | None = None, offset: Incomplete | None = None): ...

class ZeroInflatedNegativeBinomialP(GenericZeroInflated):
    __doc__: Incomplete
    model_main: Incomplete
    distribution: Incomplete
    result_class: Incomplete
    result_class_wrapper: Incomplete
    result_class_reg: Incomplete
    result_class_reg_wrapper: Incomplete
    def __init__(self, endog, exog, exog_infl: Incomplete | None = None, offset: Incomplete | None = None, exposure: Incomplete | None = None, inflation: str = 'logit', p: int = 2, missing: str = 'none', **kwargs) -> None: ...
    def get_distribution(self, params, exog: Incomplete | None = None, exog_infl: Incomplete | None = None, exposure: Incomplete | None = None, offset: Incomplete | None = None): ...

class ZeroInflatedResults(CountResults):
    def get_prediction(self, exog: Incomplete | None = None, exog_infl: Incomplete | None = None, exposure: Incomplete | None = None, offset: Incomplete | None = None, which: str = 'mean', average: bool = False, agg_weights: Incomplete | None = None, y_values: Incomplete | None = None, transform: bool = True, row_labels: Incomplete | None = None): ...
    def get_influence(self):
        """
        Influence and outlier measures

        See notes section for influence measures that do not apply for
        zero inflated models.

        Returns
        -------
        MLEInfluence
            The instance has methods to calculate the main influence and
            outlier measures as attributes.

        See Also
        --------
        statsmodels.stats.outliers_influence.MLEInfluence

        Notes
        -----
        ZeroInflated models have functions that are not differentiable
        with respect to sample endog if endog=0. This means that generalized
        leverage cannot be computed in the usual definition.

        Currently, both the generalized leverage, in `hat_matrix_diag`
        attribute and studetized residuals are not available. In the influence
        plot generalized leverage is replaced by a hat matrix diagonal that
        only takes combined exog into account, computed in the same way as
        for OLS. This is a measure for exog outliers but does not take
        specific features of the model into account.
        """

class ZeroInflatedPoissonResults(ZeroInflatedResults):
    __doc__: Incomplete
    def get_margeff(self, at: str = 'overall', method: str = 'dydx', atexog: Incomplete | None = None, dummy: bool = False, count: bool = False) -> None:
        """Get marginal effects of the fitted model.

        Not yet implemented for Zero Inflated Models
        """

class L1ZeroInflatedPoissonResults(L1CountResults, ZeroInflatedPoissonResults): ...
class ZeroInflatedPoissonResultsWrapper(lm.RegressionResultsWrapper): ...
class L1ZeroInflatedPoissonResultsWrapper(lm.RegressionResultsWrapper): ...

class ZeroInflatedGeneralizedPoissonResults(ZeroInflatedResults):
    __doc__: Incomplete
    def get_margeff(self, at: str = 'overall', method: str = 'dydx', atexog: Incomplete | None = None, dummy: bool = False, count: bool = False) -> None:
        """Get marginal effects of the fitted model.

        Not yet implemented for Zero Inflated Models
        """

class L1ZeroInflatedGeneralizedPoissonResults(L1CountResults, ZeroInflatedGeneralizedPoissonResults): ...
class ZeroInflatedGeneralizedPoissonResultsWrapper(lm.RegressionResultsWrapper): ...
class L1ZeroInflatedGeneralizedPoissonResultsWrapper(lm.RegressionResultsWrapper): ...

class ZeroInflatedNegativeBinomialResults(ZeroInflatedResults):
    __doc__: Incomplete
    def get_margeff(self, at: str = 'overall', method: str = 'dydx', atexog: Incomplete | None = None, dummy: bool = False, count: bool = False) -> None:
        """Get marginal effects of the fitted model.

        Not yet implemented for Zero Inflated Models
        """

class L1ZeroInflatedNegativeBinomialResults(L1CountResults, ZeroInflatedNegativeBinomialResults): ...
class ZeroInflatedNegativeBinomialResultsWrapper(lm.RegressionResultsWrapper): ...
class L1ZeroInflatedNegativeBinomialResultsWrapper(lm.RegressionResultsWrapper): ...
