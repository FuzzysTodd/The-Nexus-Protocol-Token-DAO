from . import norms as norms
from _typeshed import Incomplete
from statsmodels.tools import tools as tools
from statsmodels.tools.validation import array_like as array_like, float_like as float_like

def mad(a, c=..., axis: int = 0, center=...):
    """
    The Median Absolute Deviation along given axis of an array

    Parameters
    ----------
    a : array_like
        Input array.
    c : float, optional
        The normalization constant.  Defined as scipy.stats.norm.ppf(3/4.),
        which is approximately 0.6745.
    axis : int, optional
        The default is 0. Can also be None.
    center : callable or float
        If a callable is provided, such as the default `np.median` then it
        is expected to be called center(a). The axis argument will be applied
        via np.apply_over_axes. Otherwise, provide a float.

    Returns
    -------
    mad : float
        `mad` = median(abs(`a` - center))/`c`
    """
def iqr(a, c=..., axis: int = 0):
    """
    The normalized interquartile range along given axis of an array

    Parameters
    ----------
    a : array_like
        Input array.
    c : float, optional
        The normalization constant, used to get consistent estimates of the
        standard deviation at the normal distribution.  Defined as
        scipy.stats.norm.ppf(3/4.) - scipy.stats.norm.ppf(1/4.), which is
        approximately 1.349.
    axis : int, optional
        The default is 0. Can also be None.

    Returns
    -------
    The normalized interquartile range
    """
def qn_scale(a, c=..., axis: int = 0):
    """
    Computes the Qn robust estimator of scale

    The Qn scale estimator is a more efficient alternative to the MAD.
    The Qn scale estimator of an array a of length n is defined as
    c * {abs(a[i] - a[j]): i<j}_(k), for k equal to [n/2] + 1 choose 2. Thus,
    the Qn estimator is the k-th order statistic of the absolute differences
    of the array. The optional constant is used to normalize the estimate
    as explained below. The implementation follows the algorithm described
    in Croux and Rousseeuw (1992).

    Parameters
    ----------
    a : array_like
        Input array.
    c : float, optional
        The normalization constant. The default value is used to get consistent
        estimates of the standard deviation at the normal distribution.
    axis : int, optional
        The default is 0.

    Returns
    -------
    {float, ndarray}
        The Qn robust estimator of scale
    """

class Huber:
    """
    Huber's proposal 2 for estimating location and scale jointly.

    Parameters
    ----------
    c : float, optional
        Threshold used in threshold for chi=psi**2.  Default value is 1.5.
    tol : float, optional
        Tolerance for convergence.  Default value is 1e-08.
    maxiter : int, optional0
        Maximum number of iterations.  Default value is 30.
    norm : statsmodels.robust.norms.RobustNorm, optional
        A robust norm used in M estimator of location. If None,
        the location estimator defaults to a one-step
        fixed point version of the M-estimator using Huber's T.

    call
        Return joint estimates of Huber's scale and location.

    Examples
    --------
    >>> import numpy as np
    >>> import statsmodels.api as sm
    >>> chem_data = np.array([2.20, 2.20, 2.4, 2.4, 2.5, 2.7, 2.8, 2.9, 3.03,
    ...        3.03, 3.10, 3.37, 3.4, 3.4, 3.4, 3.5, 3.6, 3.7, 3.7, 3.7, 3.7,
    ...        3.77, 5.28, 28.95])
    >>> sm.robust.scale.huber(chem_data)
    (array(3.2054980819923693), array(0.67365260010478967))
    """
    c: Incomplete
    maxiter: Incomplete
    tol: Incomplete
    norm: Incomplete
    gamma: Incomplete
    def __init__(self, c: float = 1.5, tol: float = 1e-08, maxiter: int = 30, norm: Incomplete | None = None) -> None: ...
    def __call__(self, a, mu: Incomplete | None = None, initscale: Incomplete | None = None, axis: int = 0):
        """
        Compute Huber's proposal 2 estimate of scale, using an optional
        initial value of scale and an optional estimate of mu. If mu
        is supplied, it is not reestimated.

        Parameters
        ----------
        a : ndarray
            1d array
        mu : float or None, optional
            If the location mu is supplied then it is not reestimated.
            Default is None, which means that it is estimated.
        initscale : float or None, optional
            A first guess on scale.  If initscale is None then the standardized
            median absolute deviation of a is used.

        Notes
        -----
        `Huber` minimizes the function

        sum(psi((a[i]-mu)/scale)**2)

        as a function of (mu, scale), where

        psi(x) = np.clip(x, -self.c, self.c)
        """

huber: Incomplete

class HuberScale:
    """
    Huber's scaling for fitting robust linear models.

    Huber's scale is intended to be used as the scale estimate in the
    IRLS algorithm and is slightly different than the `Huber` class.

    Parameters
    ----------
    d : float, optional
        d is the tuning constant for Huber's scale.  Default is 2.5
    tol : float, optional
        The convergence tolerance
    maxiter : int, optiona
        The maximum number of iterations.  The default is 30.

    Methods
    -------
    call
        Return's Huber's scale computed as below

    Notes
    -----
    Huber's scale is the iterative solution to

    scale_(i+1)**2 = 1/(n*h)*sum(chi(r/sigma_i)*sigma_i**2

    where the Huber function is

    chi(x) = (x**2)/2       for \\|x\\| < d
    chi(x) = (d**2)/2       for \\|x\\| >= d

    and the Huber constant h = (n-p)/n*(d**2 + (1-d**2)*
    scipy.stats.norm.cdf(d) - .5 - d*sqrt(2*pi)*exp(-0.5*d**2)
    """
    d: Incomplete
    tol: Incomplete
    maxiter: Incomplete
    def __init__(self, d: float = 2.5, tol: float = 1e-08, maxiter: int = 30) -> None: ...
    def __call__(self, df_resid, nobs, resid): ...

hubers_scale: Incomplete
