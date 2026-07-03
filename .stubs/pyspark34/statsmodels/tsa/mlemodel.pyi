from _typeshed import Incomplete
from statsmodels.base.model import LikelihoodModel as LikelihoodModel

class TSMLEModel(LikelihoodModel):
    """
    univariate time series model for estimation with maximum likelihood

    Note: This is not working yet
    """
    nar: int
    nma: int
    def __init__(self, endog, exog: Incomplete | None = None) -> None: ...
    def geterrors(self, params) -> None: ...
    def loglike(self, params) -> None:
        """
        Loglikelihood for timeseries model

        Parameters
        ----------
        params : array_like
            The model parameters

        Notes
        -----
        needs to be overwritten by subclass
        """
    def score(self, params):
        """
        Score vector for Arma model
        """
    def hessian(self, params):
        """
        Hessian of arma model.  Currently uses numdifftools
        """
    def fit(self, start_params: Incomplete | None = None, maxiter: int = 5000, method: str = 'fmin', tol: float = 1e-08):
        """estimate model by minimizing negative loglikelihood

        does this need to be overwritten ?
        """
