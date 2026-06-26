from ._penalties import NonePenalty as NonePenalty
from _typeshed import Incomplete
from statsmodels.tools.numdiff import approx_fprime as approx_fprime, approx_fprime_cs as approx_fprime_cs

class PenalizedMixin:
    """Mixin class for Maximum Penalized Likelihood

    Parameters
    ----------
    args and kwds for the model super class
    penal : None or instance of Penalized function class
        If penal is None, then NonePenalty is used.
    pen_weight : float or None
        factor for weighting the penalization term.
        If None, then pen_weight is set to nobs.


    TODO: missing **kwds or explicit keywords

    TODO: do we adjust the inherited docstrings?
    We would need templating to add the penalization parameters
    """
    penal: Incomplete
    pen_weight: Incomplete
    def __init__(self, *args, **kwds) -> None: ...
    def loglike(self, params, pen_weight: Incomplete | None = None, **kwds):
        """
        Log-likelihood of model at params
        """
    def loglikeobs(self, params, pen_weight: Incomplete | None = None, **kwds):
        """
        Log-likelihood of model observations at params
        """
    def score_numdiff(self, params, pen_weight: Incomplete | None = None, method: str = 'fd', **kwds):
        """score based on finite difference derivative
        """
    def score(self, params, pen_weight: Incomplete | None = None, **kwds):
        """
        Gradient of model at params
        """
    def score_obs(self, params, pen_weight: Incomplete | None = None, **kwds):
        """
        Gradient of model observations at params
        """
    def hessian_numdiff(self, params, pen_weight: Incomplete | None = None, **kwds):
        """hessian based on finite difference derivative
        """
    def hessian(self, params, pen_weight: Incomplete | None = None, **kwds):
        """
        Hessian of model at params
        """
    def fit(self, method: Incomplete | None = None, trim: Incomplete | None = None, **kwds):
        """minimize negative penalized log-likelihood

        Parameters
        ----------
        method : None or str
            Method specifies the scipy optimizer as in nonlinear MLE models.
        trim : {bool, float}
            Default is False or None, which uses no trimming.
            If trim is True or a float, then small parameters are set to zero.
            If True, then a default threshold is used. If trim is a float, then
            it will be used as threshold.
            The default threshold is currently 1e-4, but it will change in
            future and become penalty function dependent.
        kwds : extra keyword arguments
            This keyword arguments are treated in the same way as in the
            fit method of the underlying model class.
            Specifically, additional optimizer keywords and cov_type related
            keywords can be added.
        """
