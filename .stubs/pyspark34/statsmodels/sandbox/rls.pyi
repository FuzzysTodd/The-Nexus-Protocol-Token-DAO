from _typeshed import Incomplete
from statsmodels.regression.linear_model import GLS as GLS, RegressionResults as RegressionResults

class RLS(GLS):
    '''
    Restricted general least squares model that handles linear constraints

    Parameters
    ----------
    endog : array_like
        n length array containing the dependent variable
    exog : array_like
        n-by-p array of independent variables
    constr : array_like
        k-by-p array of linear constraints
    param : array_like or scalar
        p-by-1 array (or scalar) of constraint parameters
    sigma (None): scalar or array_like
        The weighting matrix of the covariance. No scaling by default (OLS).
        If sigma is a scalar, then it is converted into an n-by-n diagonal
        matrix with sigma as each diagonal element.
        If sigma is an n-length array, then it is assumed to be a diagonal
        matrix with the given sigma on the diagonal (WLS).

    Notes
    -----
    endog = exog * beta + epsilon
    weights\' * constr * beta = param

    See Greene and Seaks, "The Restricted Least Squares Estimator:
    A Pedagogical Note", The Review of Economics and Statistics, 1991.
    '''
    ncoeffs: Incomplete
    nconstraint: Incomplete
    constraint: Incomplete
    param: Incomplete
    sigma: Incomplete
    cholsigmainv: Incomplete
    def __init__(self, endog, exog, constr, param: float = 0.0, sigma: Incomplete | None = None) -> None: ...
    @property
    def rwexog(self):
        """Whitened exogenous variables augmented with restrictions"""
    @property
    def inv_rwexog(self):
        """Inverse of self.rwexog"""
    @property
    def rwendog(self):
        """Whitened endogenous variable augmented with restriction parameters"""
    @property
    def rnorm_cov_params(self):
        """Parameter covariance under restrictions"""
    @property
    def wrnorm_cov_params(self):
        """
        Heteroskedasticity-consistent parameter covariance
        Used to calculate White standard errors.
        """
    @property
    def coeffs(self):
        """Estimated parameters"""
    def fit(self): ...
