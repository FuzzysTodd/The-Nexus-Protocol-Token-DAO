from _typeshed import Incomplete
from statsmodels.base.model import GenericLikelihoodModel as GenericLikelihoodModel
from statsmodels.tsa.arma_mle import Arma as Arma

np_log: Incomplete
np_pi: Incomplete
sps_gamln: Incomplete

class TLinearModel(GenericLikelihoodModel):
    """Maximum Likelihood Estimation of Linear Model with t-distributed errors

    This is an example for generic MLE.

    Except for defining the negative log-likelihood method, all
    methods and results are generic. Gradients and Hessian
    and all resulting statistics are based on numerical
    differentiation.

    """
    k_vars: Incomplete
    fix_df: bool
    fixed_params: Incomplete
    fixed_paramsmask: Incomplete
    k_params: Incomplete
    def initialize(self) -> None: ...
    def loglike(self, params): ...
    def nloglikeobs(self, params):
        """
        Loglikelihood of linear model with t distributed errors.

        Parameters
        ----------
        params : ndarray
            The parameters of the model. The last 2 parameters are degrees of
            freedom and scale.

        Returns
        -------
        loglike : ndarray
            The log likelihood of the model evaluated at `params` for each
            observation defined by self.endog and self.exog.

        Notes
        -----
        .. math:: \\ln L=\\sum_{i=1}^{n}\\left[-\\lambda_{i}+y_{i}x_{i}^{\\prime}\\beta-\\ln y_{i}!\\right]

        The t distribution is the standard t distribution and not a standardized
        t distribution, which means that the scale parameter is not equal to the
        standard deviation.

        self.fixed_params and self.expandparams can be used to fix some
        parameters. (I doubt this has been tested in this model.)
        """
    def predict(self, params, exog: Incomplete | None = None): ...

class TArma(Arma):
    """Univariate Arma Model with t-distributed errors

    This inherit all methods except loglike from tsa.arma_mle.Arma

    This uses the standard t-distribution, the implied variance of
    the error is not equal to scale, but ::

        error_variance = df/(df-2)*scale**2

    Notes
    -----
    This might be replaced by a standardized t-distribution with scale**2
    equal to variance

    """
    def loglike(self, params): ...
    def nloglikeobs(self, params):
        """
        Loglikelihood for arma model for each observation, t-distribute

        Notes
        -----
        The ancillary parameter is assumed to be the last element of
        the params vector
        """
    def fit_mle(self, order, start_params: Incomplete | None = None, method: str = 'nm', maxiter: int = 5000, tol: float = 1e-08, **kwds): ...
