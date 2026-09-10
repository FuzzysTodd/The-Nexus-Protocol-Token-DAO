from _typeshed import Incomplete
from statsmodels.regression.linear_model import OLS as OLS

class RegularizedInvCovariance:
    """
    Class for estimating regularized inverse covariance with
    nodewise regression

    Parameters
    ----------
    exog : array_like
        A weighted design matrix for covariance

    Attributes
    ----------
    exog : array_like
        A weighted design matrix for covariance
    alpha : scalar
        Regularizing constant
    """
    exog: Incomplete
    def __init__(self, exog) -> None: ...
    def fit(self, alpha: int = 0) -> None:
        """estimates the regularized inverse covariance using nodewise
        regression

        Parameters
        ----------
        alpha : scalar
            Regularizing constant
        """
    def approx_inv_cov(self): ...
