from _typeshed import Incomplete
from statsmodels.base._penalties import Penalty as Penalty

class UnivariateGamPenalty(Penalty):
    """
    Penalty for smooth term in Generalized Additive Models

    Parameters
    ----------
    univariate_smoother : instance
        instance of univariate smoother or spline class
    alpha : float
        default penalty weight, alpha can be provided to each method
    weights:
        TODO: not used and verified, might be removed

    Attributes
    ----------
    Parameters are stored, additionally
    nob s: The number of samples used during the estimation
    n_columns : number of columns in smoother basis
    """
    weights: Incomplete
    alpha: Incomplete
    univariate_smoother: Incomplete
    nobs: Incomplete
    n_columns: Incomplete
    def __init__(self, univariate_smoother, alpha: int = 1, weights: int = 1) -> None: ...
    def func(self, params, alpha: Incomplete | None = None):
        """evaluate penalization at params

        Parameters
        ----------
        params : ndarray
            coefficients for the spline basis in the regression model
        alpha : float
            default penalty weight

        Returns
        -------
        func : float
            value of the penalty evaluated at params
        """
    def deriv(self, params, alpha: Incomplete | None = None):
        """evaluate derivative of penalty with respect to params

        Parameters
        ----------
        params : ndarray
            coefficients for the spline basis in the regression model
        alpha : float
            default penalty weight

        Returns
        -------
        deriv : ndarray
            derivative, gradient of the penalty with respect to params
        """
    def deriv2(self, params, alpha: Incomplete | None = None):
        """evaluate second derivative of penalty with respect to params

        Parameters
        ----------
        params : ndarray
            coefficients for the spline basis in the regression model
        alpha : float
            default penalty weight

        Returns
        -------
        deriv2 : ndarray, 2-Dim
            second derivative, hessian of the penalty with respect to params
        """
    def penalty_matrix(self, alpha: Incomplete | None = None):
        """penalty matrix for the smooth term of a GAM

        Parameters
        ----------
        alpha : list of floats or None
            penalty weights

        Returns
        -------
        penalty matrix
            square penalty matrix for quadratic penalization. The number
            of rows and columns are equal to the number of columns in the
            smooth terms, i.e. the number of parameters for this smooth
            term in the regression model
        """

class MultivariateGamPenalty(Penalty):
    """
    Penalty for Generalized Additive Models

    Parameters
    ----------
    multivariate_smoother : instance
        instance of additive smoother or spline class
    alpha : list of float
        default penalty weight, list with length equal to the number of smooth
        terms. ``alpha`` can also be provided to each method.
    weights : array_like
        currently not used
        is a list of doubles of the same length as alpha or a list
        of ndarrays where each component has the length equal to the number
        of columns in that component
    start_idx : int
        number of parameters that come before the smooth terms. If the model
        has a linear component, then the parameters for the smooth components
        start at ``start_index``.

    Attributes
    ----------
    Parameters are stored, additionally
    nob s: The number of samples used during the estimation

    dim_basis : number of columns of additive smoother. Number of columns
        in all smoothers.
    k_variables : number of smooth terms
    k_params : total number of parameters in the regression model
    """
    multivariate_smoother: Incomplete
    dim_basis: Incomplete
    k_variables: Incomplete
    nobs: Incomplete
    alpha: Incomplete
    start_idx: Incomplete
    k_params: Incomplete
    weights: Incomplete
    mask: Incomplete
    gp: Incomplete
    def __init__(self, multivariate_smoother, alpha, weights: Incomplete | None = None, start_idx: int = 0) -> None: ...
    def func(self, params, alpha: Incomplete | None = None):
        """evaluate penalization at params

        Parameters
        ----------
        params : ndarray
            coefficients in the regression model
        alpha : float or list of floats
            penalty weights

        Returns
        -------
        func : float
            value of the penalty evaluated at params
        """
    def deriv(self, params, alpha: Incomplete | None = None):
        """evaluate derivative of penalty with respect to params

        Parameters
        ----------
        params : ndarray
            coefficients in the regression model
        alpha : list of floats or None
            penalty weights

        Returns
        -------
        deriv : ndarray
            derivative, gradient of the penalty with respect to params
        """
    def deriv2(self, params, alpha: Incomplete | None = None):
        """evaluate second derivative of penalty with respect to params

        Parameters
        ----------
        params : ndarray
            coefficients in the regression model
        alpha : list of floats or None
            penalty weights

        Returns
        -------
        deriv2 : ndarray, 2-Dim
            second derivative, hessian of the penalty with respect to params
        """
    def penalty_matrix(self, alpha: Incomplete | None = None):
        """penalty matrix for generalized additive model

        Parameters
        ----------
        alpha : list of floats or None
            penalty weights

        Returns
        -------
        penalty matrix
            block diagonal, square penalty matrix for quadratic penalization.
            The number of rows and columns are equal to the number of
            parameters in the regression model ``k_params``.

        Notes
        -----
        statsmodels does not support backwards compatibility when keywords are
        used as positional arguments. The order of keywords might change.
        We might need to add a ``params`` keyword if the need arises.
        """
