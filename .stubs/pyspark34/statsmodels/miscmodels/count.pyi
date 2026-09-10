from _typeshed import Incomplete
from statsmodels.base.model import GenericLikelihoodModel as GenericLikelihoodModel

def maxabs(arr1, arr2): ...
def maxabsrel(arr1, arr2): ...

class PoissonGMLE(GenericLikelihoodModel):
    """Maximum Likelihood Estimation of Poisson Model

    This is an example for generic MLE which has the same
    statistical model as discretemod.Poisson.

    Except for defining the negative log-likelihood method, all
    methods and results are generic. Gradients and Hessian
    and all resulting statistics are based on numerical
    differentiation.

    """
    def nloglikeobs(self, params):
        """
        Loglikelihood of Poisson model

        Parameters
        ----------
        params : array_like
            The parameters of the model.

        Returns
        -------
        The log likelihood of the model evaluated at `params`

        Notes
        -----
        .. math:: \\ln L=\\sum_{i=1}^{n}\\left[-\\lambda_{i}+y_{i}x_{i}^{\\prime}\\beta-\\ln y_{i}!\\right]
        """
    def predict_distribution(self, exog):
        """return frozen scipy.stats distribution with mu at estimated prediction
        """

class PoissonOffsetGMLE(GenericLikelihoodModel):
    """Maximum Likelihood Estimation of Poisson Model

    This is an example for generic MLE which has the same
    statistical model as discretemod.Poisson but adds offset

    Except for defining the negative log-likelihood method, all
    methods and results are generic. Gradients and Hessian
    and all resulting statistics are based on numerical
    differentiation.

    """
    offset: Incomplete
    def __init__(self, endog, exog: Incomplete | None = None, offset: Incomplete | None = None, missing: str = 'none', **kwds) -> None: ...
    def nloglikeobs(self, params):
        """
        Loglikelihood of Poisson model

        Parameters
        ----------
        params : array_like
            The parameters of the model.

        Returns
        -------
        The log likelihood of the model evaluated at `params`

        Notes
        -----
        .. math:: \\ln L=\\sum_{i=1}^{n}\\left[-\\lambda_{i}+y_{i}x_{i}^{\\prime}\\beta-\\ln y_{i}!\\right]
        """

class PoissonZiGMLE(GenericLikelihoodModel):
    """Maximum Likelihood Estimation of Poisson Model

    This is an example for generic MLE which has the same statistical model
    as discretemod.Poisson but adds offset and zero-inflation.

    Except for defining the negative log-likelihood method, all
    methods and results are generic. Gradients and Hessian
    and all resulting statistics are based on numerical
    differentiation.

    There are numerical problems if there is no zero-inflation.

    """
    k_extra: int
    offset: Incomplete
    exog: Incomplete
    nparams: Incomplete
    start_params: Incomplete
    cloneattr: Incomplete
    def __init__(self, endog, exog: Incomplete | None = None, offset: Incomplete | None = None, missing: str = 'none', **kwds) -> None: ...
    def nloglikeobs(self, params):
        """
        Loglikelihood of Poisson model

        Parameters
        ----------
        params : array_like
            The parameters of the model.

        Returns
        -------
        The log likelihood of the model evaluated at `params`

        Notes
        -----
        .. math:: \\ln L=\\sum_{i=1}^{n}\\left[-\\lambda_{i}+y_{i}x_{i}^{\\prime}\\beta-\\ln y_{i}!\\right]
        """
