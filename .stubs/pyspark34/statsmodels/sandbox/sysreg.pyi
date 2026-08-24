from _typeshed import Incomplete
from statsmodels.base.model import LikelihoodModelResults

__all__ = ['SUR', 'Sem2SLS']

class SUR:
    """
    Seemingly Unrelated Regression

    Parameters
    ----------
    sys : list
        [endog1, exog1, endog2, exog2,...] It will be of length 2 x M,
        where M is the number of equations endog = exog.
    sigma : array_like
        M x M array where sigma[i,j] is the covariance between equation i and j
    dfk : None, 'dfk1', or 'dfk2'
        Default is None.  Correction for the degrees of freedom
        should be specified for small samples.  See the notes for more
        information.

    Attributes
    ----------
    cholsigmainv : ndarray
        The transpose of the Cholesky decomposition of `pinv_wexog`
    df_model : ndarray
        Model degrees of freedom of each equation. p_{m} - 1 where p is
        the number of regressors for each equation m and one is subtracted
        for the constant.
    df_resid : ndarray
        Residual degrees of freedom of each equation. Number of observations
        less the number of parameters.
    endog : ndarray
        The LHS variables for each equation in the system.
        It is a M x nobs array where M is the number of equations.
    exog : ndarray
        The RHS variable for each equation in the system.
        It is a nobs x sum(p_{m}) array.  Which is just each
        RHS array stacked next to each other in columns.
    history : dict
        Contains the history of fitting the model. Probably not of interest
        if the model is fit with `igls` = False.
    iterations : int
        The number of iterations until convergence if the model is fit
        iteratively.
    nobs : float
        The number of observations of the equations.
    normalized_cov_params : ndarray
        sum(p_{m}) x sum(p_{m}) array
        :math:`\\left[X^{T}\\left(\\Sigma^{-1}\\otimes\\boldsymbol{I}\\right)X\\right]^{-1}`
    pinv_wexog : ndarray
        The pseudo-inverse of the `wexog`
    sigma : ndarray
        M x M covariance matrix of the cross-equation disturbances. See notes.
    sp_exog : CSR sparse matrix
        Contains a block diagonal sparse matrix of the design so that
        exog1 ... exogM are on the diagonal.
    wendog : ndarray
        M * nobs x 1 array of the endogenous variables whitened by
        `cholsigmainv` and stacked into a single column.
    wexog : ndarray
        M*nobs x sum(p_{m}) array of the whitened exogenous variables.

    Notes
    -----
    All individual equations are assumed to be well-behaved, homoskedastic
    iid errors.  This is basically an extension of GLS, using sparse matrices.

    .. math:: \\Sigma=\\left[\\begin{array}{cccc}
              \\sigma_{11} & \\sigma_{12} & \\cdots & \\sigma_{1M}\\\\\n              \\sigma_{21} & \\sigma_{22} & \\cdots & \\sigma_{2M}\\\\\n              \\vdots & \\vdots & \\ddots & \\vdots\\\\\n              \\sigma_{M1} & \\sigma_{M2} & \\cdots & \\sigma_{MM}\\end{array}\\right]

    References
    ----------
    Zellner (1962), Greene (2003)
    """
    exog: Incomplete
    endog: Incomplete
    nobs: Incomplete
    df_resid: Incomplete
    df_model: Incomplete
    sp_exog: Incomplete
    sigma: Incomplete
    cholsigmainv: Incomplete
    def __init__(self, sys, sigma: Incomplete | None = None, dfk: Incomplete | None = None) -> None: ...
    wendog: Incomplete
    wexog: Incomplete
    pinv_wexog: Incomplete
    normalized_cov_params: Incomplete
    history: Incomplete
    iterations: int
    def initialize(self) -> None: ...
    def whiten(self, X):
        """
        SUR whiten method.

        Parameters
        ----------
        X : list of arrays
            Data to be whitened.

        Returns
        -------
        If X is the exogenous RHS of the system.
        ``np.dot(np.kron(cholsigmainv,np.eye(M)),np.diag(X))``

        If X is the endogenous LHS of the system.
        """
    def fit(self, igls: bool = False, tol: float = 1e-05, maxiter: int = 100):
        """
        igls : bool
            Iterate until estimates converge if sigma is None instead of
            two-step GLS, which is the default is sigma is None.

        tol : float

        maxiter : int

        Notes
        -----
        This ia naive implementation that does not exploit the block
        diagonal structure. It should work for ill-conditioned `sigma`
        but this is untested.
        """
    def predict(self, design) -> None: ...

class Sem2SLS:
    """
    Two-Stage Least Squares for Simultaneous equations

    Parameters
    ----------
    sys : list
        [endog1, exog1, endog2, exog2,...] It will be of length 2 x M,
        where M is the number of equations endog = exog.
    indep_endog : dict
        A dictionary mapping the equation to the column numbers of the
        the independent endogenous regressors in each equation.
        It is assumed that the system is entered as broken up into
        LHS and RHS. For now, the values of the dict have to be sequences.
        Note that the keys for the equations should be zero-indexed.
    instruments : ndarray
        Array of the exogenous independent variables.

    Notes
    -----
    This is unfinished, and the design should be refactored.
    Estimation is done by brute force and there is no exploitation of
    the structure of the system.
    """
    endog: Incomplete
    exog: Incomplete
    instruments: Incomplete
    wexog: Incomplete
    def __init__(self, sys, indep_endog: Incomplete | None = None, instruments: Incomplete | None = None) -> None: ...
    def whiten(self, Y):
        """
        Runs the first stage of the 2SLS.

        Returns the RHS variables that include the instruments.
        """
    def fit(self):
        """
        """

class SysResults(LikelihoodModelResults):
    """
    Not implemented yet.
    """
    def __init__(self, model, params, normalized_cov_params: Incomplete | None = None, scale: float = 1.0) -> None: ...
