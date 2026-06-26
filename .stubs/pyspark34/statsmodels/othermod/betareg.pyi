import statsmodels.regression.linear_model as lm
from _typeshed import Incomplete
from statsmodels.base.model import GenericLikelihoodModel as GenericLikelihoodModel, GenericLikelihoodModelResults as GenericLikelihoodModelResults, _LLRMixin
from statsmodels.genmod import families as families
from statsmodels.tools.decorators import cache_readonly as cache_readonly

class BetaModel(GenericLikelihoodModel):
    __doc__: Incomplete
    link: Incomplete
    link_precision: Incomplete
    nobs: Incomplete
    k_extra: int
    df_model: Incomplete
    df_resid: Incomplete
    hess_type: str
    results_class: Incomplete
    results_class_wrapper: Incomplete
    def __init__(self, endog, exog, exog_precision: Incomplete | None = None, link=..., link_precision=..., **kwds) -> None: ...
    @classmethod
    def from_formula(cls, formula, data, exog_precision_formula: Incomplete | None = None, *args, **kwargs): ...
    def predict(self, params, exog: Incomplete | None = None, exog_precision: Incomplete | None = None, which: str = 'mean'):
        '''Predict values for mean or precision

        Parameters
        ----------
        params : array_like
            The model parameters.
        exog : array_like
            Array of predictor variables for mean.
        exog_precision : array_like
            Array of predictor variables for precision parameter.
        which : str

            - "mean" : mean, conditional expectation E(endog | exog)
            - "precision" : predicted precision
            - "linear" : linear predictor for the mean function
            - "linear-precision" : linear predictor for the precision parameter

        Returns
        -------
        ndarray, predicted values
        '''
    def loglikeobs(self, params):
        """
        Loglikelihood for observations of the Beta regressionmodel.

        Parameters
        ----------
        params : ndarray
            The parameters of the model, coefficients for linear predictors
            of the mean and of the precision function.

        Returns
        -------
        loglike : ndarray
            The log likelihood for each observation of the model evaluated
            at `params`.
        """
    def score(self, params):
        """
        Returns the score vector of the log-likelihood.

        http://www.tandfonline.com/doi/pdf/10.1080/00949650903389993

        Parameters
        ----------
        params : ndarray
            Parameter at which score is evaluated.

        Returns
        -------
        score : ndarray
            First derivative of loglikelihood function.
        """
    def score_factor(self, params, endog: Incomplete | None = None):
        """Derivative of loglikelihood function w.r.t. linear predictors.

        This needs to be multiplied with the exog to obtain the score_obs.

        Parameters
        ----------
        params : ndarray
            Parameter at which score is evaluated.

        Returns
        -------
        score_factor : ndarray, 2-D
            A 2d weight vector used in the calculation of the score_obs.

        Notes
        -----
        The score_obs can be obtained from score_factor ``sf`` using

            - d1 = sf[:, :1] * exog
            - d2 = sf[:, 1:2] * exog_precision

        """
    def score_hessian_factor(self, params, return_hessian: bool = False, observed: bool = True):
        """Derivatives of loglikelihood function w.r.t. linear predictors.

        This calculates score and hessian factors at the same time, because
        there is a large overlap in calculations.

        Parameters
        ----------
        params : ndarray
            Parameter at which score is evaluated.
        return_hessian : bool
            If False, then only score_factors are returned
            If True, the both score and hessian factors are returned
        observed : bool
            If True, then the observed Hessian is returned (default).
            If False, then the expected information matrix is returned.

        Returns
        -------
        score_factor : ndarray, 2-D
            A 2d weight vector used in the calculation of the score_obs.
        (-jbb, -jbg, -jgg) : tuple
            A tuple with 3 hessian factors, corresponding to the upper
            triangle of the Hessian matrix.
            TODO: check why there are minus
        """
    def score_obs(self, params):
        """
        Score, first derivative of the loglikelihood for each observation.

        Parameters
        ----------
        params : ndarray
            Parameter at which score is evaluated.

        Returns
        -------
        score_obs : ndarray, 2d
            The first derivative of the loglikelihood function evaluated at
            params for each observation.
        """
    def hessian(self, params, observed: Incomplete | None = None):
        """Hessian, second derivative of loglikelihood function

        Parameters
        ----------
        params : ndarray
            Parameter at which Hessian is evaluated.
        observed : bool
            If True, then the observed Hessian is returned (default).
            If False, then the expected information matrix is returned.

        Returns
        -------
        hessian : ndarray
            Hessian, i.e. observed information, or expected information matrix.
        """
    def hessian_factor(self, params, observed: bool = True):
        """Derivatives of loglikelihood function w.r.t. linear predictors.
        """
    def fit(self, start_params: Incomplete | None = None, maxiter: int = 1000, disp: bool = False, method: str = 'bfgs', **kwds):
        """
        Fit the model by maximum likelihood.

        Parameters
        ----------
        start_params : array-like
            A vector of starting values for the regression
            coefficients.  If None, a default is chosen.
        maxiter : integer
            The maximum number of iterations
        disp : bool
            Show convergence stats.
        method : str
            The optimization method to use.
        kwds :
            Keyword arguments for the optimizer.

        Returns
        -------
        BetaResults instance.
        """
    def get_distribution_params(self, params, exog: Incomplete | None = None, exog_precision: Incomplete | None = None):
        """
        Return distribution parameters converted from model prediction.

        Parameters
        ----------
        params : array_like
            The model parameters.
        exog : array_like
            Array of predictor variables for mean.
        exog_precision : array_like
            Array of predictor variables for mean.

        Returns
        -------
        (alpha, beta) : tuple of ndarrays
            Parameters for the scipy distribution to evaluate predictive
            distribution.
        """
    def get_distribution(self, params, exog: Incomplete | None = None, exog_precision: Incomplete | None = None):
        """
        Return a instance of the predictive distribution.

        Parameters
        ----------
        params : array_like
            The model parameters.
        exog : array_like
            Array of predictor variables for mean.
        exog_precision : array_like
            Array of predictor variables for mean.

        Returns
        -------
        Instance of a scipy frozen distribution based on estimated
        parameters.

        See Also
        --------
        predict

        Notes
        -----
        This function delegates to the predict method to handle exog and
        exog_precision, which in turn makes any required transformations.

        Due to the behavior of ``scipy.stats.distributions objects``, the
        returned random number generator must be called with ``gen.rvs(n)``
        where ``n`` is the number of observations in the data set used
        to fit the model.  If any other value is used for ``n``, misleading
        results will be produced.
        """

class BetaResults(GenericLikelihoodModelResults, _LLRMixin):
    """Results class for Beta regression

    This class inherits from GenericLikelihoodModelResults and not all
    inherited methods might be appropriate in this case.
    """
    def fittedvalues(self):
        """In-sample predicted mean, conditional expectation."""
    def fitted_precision(self):
        """In-sample predicted precision"""
    def resid(self):
        """Response residual"""
    def resid_pearson(self):
        """Pearson standardize residual"""
    def prsquared(self):
        """Cox-Snell Likelihood-Ratio pseudo-R-squared.

        1 - exp((llnull - .llf) * (2 / nobs))
        """
    def get_distribution_params(self, exog: Incomplete | None = None, exog_precision: Incomplete | None = None, transform: bool = True):
        """
        Return distribution parameters converted from model prediction.

        Parameters
        ----------
        params : array_like
            The model parameters.
        exog : array_like
            Array of predictor variables for mean.
        transform : bool
            If transform is True and formulas have been used, then predictor
            ``exog`` is passed through the formula processing. Default is True.

        Returns
        -------
        (alpha, beta) : tuple of ndarrays
            Parameters for the scipy distribution to evaluate predictive
            distribution.
        """
    def get_distribution(self, exog: Incomplete | None = None, exog_precision: Incomplete | None = None, transform: bool = True):
        """
        Return a instance of the predictive distribution.

        Parameters
        ----------
        exog : array_like
            Array of predictor variables for mean.
        exog_precision : array_like
            Array of predictor variables for mean.
        transform : bool
            If transform is True and formulas have been used, then predictor
            ``exog`` is passed through the formula processing. Default is True.

        Returns
        -------
        Instance of a scipy frozen distribution based on estimated
        parameters.

        See Also
        --------
        predict

        Notes
        -----
        This function delegates to the predict method to handle exog and
        exog_precision, which in turn makes any required transformations.

        Due to the behavior of ``scipy.stats.distributions objects``, the
        returned random number generator must be called with ``gen.rvs(n)``
        where ``n`` is the number of observations in the data set used
        to fit the model.  If any other value is used for ``n``, misleading
        results will be produced.
        """
    def get_influence(self):
        """
        Get an instance of MLEInfluence with influence and outlier measures

        Returns
        -------
        infl : MLEInfluence instance
            The instance has methods to calculate the main influence and
            outlier measures as attributes.

        See Also
        --------
        statsmodels.stats.outliers_influence.MLEInfluence

        Notes
        -----
        Support for mutli-link and multi-exog models is still experimental
        in MLEInfluence. Interface and some definitions might still change.

        Note: Difference to R betareg: Betareg has the same general leverage
        as this model. However, they use a linear approximation hat matrix
        to scale and studentize influence and residual statistics.
        MLEInfluence uses the generalized leverage as hat_matrix_diag.
        Additionally, MLEInfluence uses pearson residuals for residual
        analusis.

        References
        ----------
        todo

        """
    def bootstrap(self, *args, **kwargs) -> None: ...

class BetaResultsWrapper(lm.RegressionResultsWrapper): ...
