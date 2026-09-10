import statsmodels.base.wrapper as wrap
from _typeshed import Incomplete
from statsmodels.base import model as model
from statsmodels.tools.sm_exceptions import ConvergenceWarning as ConvergenceWarning

class _DimReductionRegression(model.Model):
    """
    A base class for dimension reduction regression methods.
    """
    def __init__(self, endog, exog, **kwargs) -> None: ...

class SlicedInverseReg(_DimReductionRegression):
    """
    Sliced Inverse Regression (SIR)

    Parameters
    ----------
    endog : array_like (1d)
        The dependent variable
    exog : array_like (2d)
        The covariates

    References
    ----------
    KC Li (1991).  Sliced inverse regression for dimension reduction.
    JASA 86, 316-342.
    """
    def fit(self, slice_n: int = 20, **kwargs):
        """
        Estimate the EDR space using Sliced Inverse Regression.

        Parameters
        ----------
        slice_n : int, optional
            Target number of observations per slice
        """
    ndim: Incomplete
    k_vars: Incomplete
    pen_mat: Incomplete
    n_slice: Incomplete
    def fit_regularized(self, ndim: int = 1, pen_mat: Incomplete | None = None, slice_n: int = 20, maxiter: int = 100, gtol: float = 0.001, **kwargs):
        '''
        Estimate the EDR space using regularized SIR.

        Parameters
        ----------
        ndim : int
            The number of EDR directions to estimate
        pen_mat : array_like
            A 2d array such that the squared Frobenius norm of
            `dot(pen_mat, dirs)`` is added to the objective function,
            where `dirs` is an orthogonal array whose columns span
            the estimated EDR space.
        slice_n : int, optional
            Target number of observations per slice
        maxiter :int
            The maximum number of iterations for estimating the EDR
            space.
        gtol : float
            If the norm of the gradient of the objective function
            falls below this value, the algorithm has converged.

        Returns
        -------
        A results class instance.

        Notes
        -----
        If each row of `exog` can be viewed as containing the values of a
        function evaluated at equally-spaced locations, then setting the
        rows of `pen_mat` to [[1, -2, 1, ...], [0, 1, -2, 1, ..], ...]
        will give smooth EDR coefficients.  This is a form of "functional
        SIR" using the squared second derivative as a penalty.

        References
        ----------
        L. Ferre, A.F. Yao (2003).  Functional sliced inverse regression
        analysis.  Statistics: a journal of theoretical and applied
        statistics 37(6) 475-488.
        '''

class PrincipalHessianDirections(_DimReductionRegression):
    """
    Principal Hessian Directions (PHD)

    Parameters
    ----------
    endog : array_like (1d)
        The dependent variable
    exog : array_like (2d)
        The covariates

    Returns
    -------
    A model instance.  Call `fit` to obtain a results instance,
    from which the estimated parameters can be obtained.

    References
    ----------
    KC Li (1992).  On Principal Hessian Directions for Data
    Visualization and Dimension Reduction: Another application
    of Stein's lemma. JASA 87:420.
    """
    def fit(self, **kwargs):
        """
        Estimate the EDR space using PHD.

        Parameters
        ----------
        resid : bool, optional
            If True, use least squares regression to remove the
            linear relationship between each covariate and the
            response, before conducting PHD.

        Returns
        -------
        A results instance which can be used to access the estimated
        parameters.
        """

class SlicedAverageVarianceEstimation(_DimReductionRegression):
    """
    Sliced Average Variance Estimation (SAVE)

    Parameters
    ----------
    endog : array_like (1d)
        The dependent variable
    exog : array_like (2d)
        The covariates
    bc : bool, optional
        If True, use the bias-corrected CSAVE method of Li and Zhu.

    References
    ----------
    RD Cook.  SAVE: A method for dimension reduction and graphics
    in regression.
    http://www.stat.umn.edu/RegGraph/RecentDev/save.pdf

    Y Li, L-X Zhu (2007). Asymptotics for sliced average
    variance estimation.  The Annals of Statistics.
    https://arxiv.org/pdf/0708.0462.pdf
    """
    bc: bool
    def __init__(self, endog, exog, **kwargs) -> None: ...
    def fit(self, **kwargs):
        """
        Estimate the EDR space.

        Parameters
        ----------
        slice_n : int
            Number of observations per slice
        """

class DimReductionResults(model.Results):
    """
    Results class for a dimension reduction regression.

    Notes
    -----
    The `params` attribute is a matrix whose columns span
    the effective dimension reduction (EDR) space.  Some
    methods produce a corresponding set of eigenvalues
    (`eigs`) that indicate how much information is contained
    in each basis direction.
    """
    eigs: Incomplete
    def __init__(self, model, params, eigs) -> None: ...

class DimReductionResultsWrapper(wrap.ResultsWrapper): ...

class CovarianceReduction(_DimReductionRegression):
    """
    Dimension reduction for covariance matrices (CORE).

    Parameters
    ----------
    endog : array_like
        The dependent variable, treated as group labels
    exog : array_like
        The independent variables.
    dim : int
        The dimension of the subspace onto which the covariance
        matrices are projected.

    Returns
    -------
    A model instance.  Call `fit` on the model instance to obtain
    a results instance, which contains the fitted model parameters.

    Notes
    -----
    This is a likelihood-based dimension reduction procedure based
    on Wishart models for sample covariance matrices.  The goal
    is to find a projection matrix P so that C_i | P'C_iP and
    C_j | P'C_jP are equal in distribution for all i, j, where
    the C_i are the within-group covariance matrices.

    The model and methodology are as described in Cook and Forzani.
    The optimization method follows Edelman et. al.

    References
    ----------
    DR Cook, L Forzani (2008).  Covariance reducing models: an alternative
    to spectral modeling of covariance matrices.  Biometrika 95:4.

    A Edelman, TA Arias, ST Smith (1998).  The geometry of algorithms with
    orthogonality constraints. SIAM J Matrix Anal Appl.
    http://math.mit.edu/~edelman/publications/geometry_of_algorithms.pdf
    """
    nobs: Incomplete
    covm: Incomplete
    covs: Incomplete
    ns: Incomplete
    dim: Incomplete
    def __init__(self, endog, exog, dim) -> None: ...
    def loglike(self, params):
        """
        Evaluate the log-likelihood

        Parameters
        ----------
        params : array_like
            The projection matrix used to reduce the covariances, flattened
            to 1d.

        Returns the log-likelihood.
        """
    def score(self, params):
        """
        Evaluate the score function.

        Parameters
        ----------
        params : array_like
            The projection matrix used to reduce the covariances,
            flattened to 1d.

        Returns the score function evaluated at 'params'.
        """
    def fit(self, start_params: Incomplete | None = None, maxiter: int = 200, gtol: float = 0.0001):
        """
        Fit the covariance reduction model.

        Parameters
        ----------
        start_params : array_like
            Starting value for the projection matrix. May be
            rectangular, or flattened.
        maxiter : int
            The maximum number of gradient steps to take.
        gtol : float
            Convergence criterion for the gradient norm.

        Returns
        -------
        A results instance that can be used to access the
        fitted parameters.
        """
SIR = SlicedInverseReg
PHD = PrincipalHessianDirections
SAVE = SlicedAverageVarianceEstimation
CORE = CovarianceReduction
