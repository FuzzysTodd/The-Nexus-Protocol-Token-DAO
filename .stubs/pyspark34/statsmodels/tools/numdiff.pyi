from _typeshed import Incomplete
from statsmodels.compat.pandas import Appender as Appender, Substitution as Substitution

EPS: Incomplete

def approx_fprime(x, f, epsilon: Incomplete | None = None, args=(), kwargs={}, centered: bool = False):
    """
    Gradient of function, or Jacobian if function f returns 1d array

    Parameters
    ----------
    x : ndarray
        parameters at which the derivative is evaluated
    f : function
        `f(*((x,)+args), **kwargs)` returning either one value or 1d array
    epsilon : float, optional
        Stepsize, if None, optimal stepsize is used. This is EPS**(1/2)*x for
        `centered` == False and EPS**(1/3)*x for `centered` == True.
    args : tuple
        Tuple of additional arguments for function `f`.
    kwargs : dict
        Dictionary of additional keyword arguments for function `f`.
    centered : bool
        Whether central difference should be returned. If not, does forward
        differencing.

    Returns
    -------
    grad : ndarray
        gradient or Jacobian

    Notes
    -----
    If f returns a 1d array, it returns a Jacobian. If a 2d array is returned
    by f (e.g., with a value for each observation), it returns a 3d array
    with the Jacobian of each observation with shape xk x nobs x xk. I.e.,
    the Jacobian of the first observation would be [:, 0, :]
    """
def approx_fprime_cs(x, f, epsilon: Incomplete | None = None, args=(), kwargs={}):
    """
    Calculate gradient or Jacobian with complex step derivative approximation

    Parameters
    ----------
    x : ndarray
        parameters at which the derivative is evaluated
    f : function
        `f(*((x,)+args), **kwargs)` returning either one value or 1d array
    epsilon : float, optional
        Stepsize, if None, optimal stepsize is used. Optimal step-size is
        EPS*x. See note.
    args : tuple
        Tuple of additional arguments for function `f`.
    kwargs : dict
        Dictionary of additional keyword arguments for function `f`.

    Returns
    -------
    partials : ndarray
       array of partial derivatives, Gradient or Jacobian

    Notes
    -----
    The complex-step derivative has truncation error O(epsilon**2), so
    truncation error can be eliminated by choosing epsilon to be very small.
    The complex-step derivative avoids the problem of round-off error with
    small epsilon because there is no subtraction.
    """
def approx_hess_cs(x, f, epsilon: Incomplete | None = None, args=(), kwargs={}):
    """Calculate Hessian with complex-step derivative approximation

    Parameters
    ----------
    x : array_like
       value at which function derivative is evaluated
    f : function
       function of one array f(x)
    epsilon : float
       stepsize, if None, then stepsize is automatically chosen

    Returns
    -------
    hess : ndarray
       array of partial second derivatives, Hessian

    Notes
    -----
    based on equation 10 in
    M. S. RIDOUT: Statistical Applications of the Complex-step Method
    of Numerical Differentiation, University of Kent, Canterbury, Kent, U.K.

    The stepsize is the same for the complex and the finite difference part.
    """
def approx_hess1(x, f, epsilon: Incomplete | None = None, args=(), kwargs={}, return_grad: bool = False): ...
def approx_hess2(x, f, epsilon: Incomplete | None = None, args=(), kwargs={}, return_grad: bool = False): ...
def approx_hess3(x, f, epsilon: Incomplete | None = None, args=(), kwargs={}): ...
approx_hess = approx_hess3
