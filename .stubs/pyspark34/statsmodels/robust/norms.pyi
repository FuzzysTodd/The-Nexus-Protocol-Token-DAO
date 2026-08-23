from _typeshed import Incomplete

class RobustNorm:
    """
    The parent class for the norms used for robust regression.

    Lays out the methods expected of the robust norms to be used
    by statsmodels.RLM.

    See Also
    --------
    statsmodels.rlm

    Notes
    -----
    Currently only M-estimators are available.

    References
    ----------
    PJ Huber.  'Robust Statistics' John Wiley and Sons, Inc., New York, 1981.

    DC Montgomery, EA Peck. 'Introduction to Linear Regression Analysis',
        John Wiley and Sons, Inc., New York, 2001.

    R Venables, B Ripley. 'Modern Applied Statistics in S'
        Springer, New York, 2002.
    """
    def rho(self, z) -> None:
        """
        The robust criterion estimator function.

        Abstract method:

        -2 loglike used in M-estimator
        """
    def psi(self, z) -> None:
        """
        Derivative of rho.  Sometimes referred to as the influence function.

        Abstract method:

        psi = rho'
        """
    def weights(self, z) -> None:
        """
        Returns the value of psi(z) / z

        Abstract method:

        psi(z) / z
        """
    def psi_deriv(self, z) -> None:
        """
        Derivative of psi.  Used to obtain robust covariance matrix.

        See statsmodels.rlm for more information.

        Abstract method:

        psi_derive = psi'
        """
    def __call__(self, z):
        """
        Returns the value of estimator rho applied to an input
        """

class LeastSquares(RobustNorm):
    """
    Least squares rho for M-estimation and its derived functions.

    See Also
    --------
    statsmodels.robust.norms.RobustNorm
    """
    def rho(self, z):
        """
        The least squares estimator rho function

        Parameters
        ----------
        z : ndarray
            1d array

        Returns
        -------
        rho : ndarray
            rho(z) = (1/2.)*z**2
        """
    def psi(self, z):
        """
        The psi function for the least squares estimator

        The analytic derivative of rho

        Parameters
        ----------
        z : array_like
            1d array

        Returns
        -------
        psi : ndarray
            psi(z) = z
        """
    def weights(self, z):
        """
        The least squares estimator weighting function for the IRLS algorithm.

        The psi function scaled by the input z

        Parameters
        ----------
        z : array_like
            1d array

        Returns
        -------
        weights : ndarray
            weights(z) = np.ones(z.shape)
        """
    def psi_deriv(self, z):
        """
        The derivative of the least squares psi function.

        Returns
        -------
        psi_deriv : ndarray
            ones(z.shape)

        Notes
        -----
        Used to estimate the robust covariance matrix.
        """

class HuberT(RobustNorm):
    """
    Huber's T for M estimation.

    Parameters
    ----------
    t : float, optional
        The tuning constant for Huber's t function. The default value is
        1.345.

    See Also
    --------
    statsmodels.robust.norms.RobustNorm
    """
    t: Incomplete
    def __init__(self, t: float = 1.345) -> None: ...
    def rho(self, z):
        """
        The robust criterion function for Huber's t.

        Parameters
        ----------
        z : array_like
            1d array

        Returns
        -------
        rho : ndarray
            rho(z) = .5*z**2            for \\|z\\| <= t

            rho(z) = \\|z\\|*t - .5*t**2    for \\|z\\| > t
        """
    def psi(self, z):
        """
        The psi function for Huber's t estimator

        The analytic derivative of rho

        Parameters
        ----------
        z : array_like
            1d array

        Returns
        -------
        psi : ndarray
            psi(z) = z      for \\|z\\| <= t

            psi(z) = sign(z)*t for \\|z\\| > t
        """
    def weights(self, z):
        """
        Huber's t weighting function for the IRLS algorithm

        The psi function scaled by z

        Parameters
        ----------
        z : array_like
            1d array

        Returns
        -------
        weights : ndarray
            weights(z) = 1          for \\|z\\| <= t

            weights(z) = t/\\|z\\|      for \\|z\\| > t
        """
    def psi_deriv(self, z):
        """
        The derivative of Huber's t psi function

        Notes
        -----
        Used to estimate the robust covariance matrix.
        """

class RamsayE(RobustNorm):
    """
    Ramsay's Ea for M estimation.

    Parameters
    ----------
    a : float, optional
        The tuning constant for Ramsay's Ea function.  The default value is
        0.3.

    See Also
    --------
    statsmodels.robust.norms.RobustNorm
    """
    a: Incomplete
    def __init__(self, a: float = 0.3) -> None: ...
    def rho(self, z):
        """
        The robust criterion function for Ramsay's Ea.

        Parameters
        ----------
        z : array_like
            1d array

        Returns
        -------
        rho : ndarray
            rho(z) = a**-2 * (1 - exp(-a*\\|z\\|)*(1 + a*\\|z\\|))
        """
    def psi(self, z):
        """
        The psi function for Ramsay's Ea estimator

        The analytic derivative of rho

        Parameters
        ----------
        z : array_like
            1d array

        Returns
        -------
        psi : ndarray
            psi(z) = z*exp(-a*\\|z\\|)
        """
    def weights(self, z):
        """
        Ramsay's Ea weighting function for the IRLS algorithm

        The psi function scaled by z

        Parameters
        ----------
        z : array_like
            1d array

        Returns
        -------
        weights : ndarray
            weights(z) = exp(-a*\\|z\\|)
        """
    def psi_deriv(self, z):
        """
        The derivative of Ramsay's Ea psi function.

        Notes
        -----
        Used to estimate the robust covariance matrix.
        """

class AndrewWave(RobustNorm):
    """
    Andrew's wave for M estimation.

    Parameters
    ----------
    a : float, optional
        The tuning constant for Andrew's Wave function.  The default value is
        1.339.

    See Also
    --------
    statsmodels.robust.norms.RobustNorm
    """
    a: Incomplete
    def __init__(self, a: float = 1.339) -> None: ...
    def rho(self, z):
        """
        The robust criterion function for Andrew's wave.

        Parameters
        ----------
        z : array_like
            1d array

        Returns
        -------
        rho : ndarray
            The elements of rho are defined as:

            .. math::

                rho(z) & = a^2 *(1-cos(z/a)), |z| \\leq a\\pi \\\\\n                rho(z) & = 2a, |z|>q\\pi
        """
    def psi(self, z):
        """
        The psi function for Andrew's wave

        The analytic derivative of rho

        Parameters
        ----------
        z : array_like
            1d array

        Returns
        -------
        psi : ndarray
            psi(z) = a * sin(z/a)   for \\|z\\| <= a*pi

            psi(z) = 0              for \\|z\\| > a*pi
        """
    def weights(self, z):
        """
        Andrew's wave weighting function for the IRLS algorithm

        The psi function scaled by z

        Parameters
        ----------
        z : array_like
            1d array

        Returns
        -------
        weights : ndarray
            weights(z) = sin(z/a) / (z/a)     for \\|z\\| <= a*pi

            weights(z) = 0                    for \\|z\\| > a*pi
        """
    def psi_deriv(self, z):
        """
        The derivative of Andrew's wave psi function

        Notes
        -----
        Used to estimate the robust covariance matrix.
        """

class TrimmedMean(RobustNorm):
    """
    Trimmed mean function for M-estimation.

    Parameters
    ----------
    c : float, optional
        The tuning constant for Ramsay's Ea function.  The default value is
        2.0.

    See Also
    --------
    statsmodels.robust.norms.RobustNorm
    """
    c: Incomplete
    def __init__(self, c: float = 2.0) -> None: ...
    def rho(self, z):
        """
        The robust criterion function for least trimmed mean.

        Parameters
        ----------
        z : array_like
            1d array

        Returns
        -------
        rho : ndarray
            rho(z) = (1/2.)*z**2    for \\|z\\| <= c

            rho(z) = (1/2.)*c**2              for \\|z\\| > c
        """
    def psi(self, z):
        """
        The psi function for least trimmed mean

        The analytic derivative of rho

        Parameters
        ----------
        z : array_like
            1d array

        Returns
        -------
        psi : ndarray
            psi(z) = z              for \\|z\\| <= c

            psi(z) = 0              for \\|z\\| > c
        """
    def weights(self, z):
        """
        Least trimmed mean weighting function for the IRLS algorithm

        The psi function scaled by z

        Parameters
        ----------
        z : array_like
            1d array

        Returns
        -------
        weights : ndarray
            weights(z) = 1             for \\|z\\| <= c

            weights(z) = 0             for \\|z\\| > c
        """
    def psi_deriv(self, z):
        """
        The derivative of least trimmed mean psi function

        Notes
        -----
        Used to estimate the robust covariance matrix.
        """

class Hampel(RobustNorm):
    """

    Hampel function for M-estimation.

    Parameters
    ----------
    a : float, optional
    b : float, optional
    c : float, optional
        The tuning constants for Hampel's function.  The default values are
        a,b,c = 2, 4, 8.

    See Also
    --------
    statsmodels.robust.norms.RobustNorm
    """
    a: Incomplete
    b: Incomplete
    c: Incomplete
    def __init__(self, a: float = 2.0, b: float = 4.0, c: float = 8.0) -> None: ...
    def rho(self, z):
        """
        The robust criterion function for Hampel's estimator

        Parameters
        ----------
        z : array_like
            1d array

        Returns
        -------
        rho : ndarray
            rho(z) = z**2 / 2                     for \\|z\\| <= a

            rho(z) = a*\\|z\\| - 1/2.*a**2               for a < \\|z\\| <= b

            rho(z) = a*(c - \\|z\\|)**2 / (c - b) / 2    for b < \\|z\\| <= c

            rho(z) = a*(b + c - a) / 2                 for \\|z\\| > c
        """
    def psi(self, z):
        """
        The psi function for Hampel's estimator

        The analytic derivative of rho

        Parameters
        ----------
        z : array_like
            1d array

        Returns
        -------
        psi : ndarray
            psi(z) = z                            for \\|z\\| <= a

            psi(z) = a*sign(z)                    for a < \\|z\\| <= b

            psi(z) = a*sign(z)*(c - \\|z\\|)/(c-b)    for b < \\|z\\| <= c

            psi(z) = 0                            for \\|z\\| > c
        """
    def weights(self, z):
        """
        Hampel weighting function for the IRLS algorithm

        The psi function scaled by z

        Parameters
        ----------
        z : array_like
            1d array

        Returns
        -------
        weights : ndarray
            weights(z) = 1                                for \\|z\\| <= a

            weights(z) = a/\\|z\\|                          for a < \\|z\\| <= b

            weights(z) = a*(c - \\|z\\|)/(\\|z\\|*(c-b))      for b < \\|z\\| <= c

            weights(z) = 0                                for \\|z\\| > c
        """
    def psi_deriv(self, z):
        """Derivative of psi function, second derivative of rho function.
        """

class TukeyBiweight(RobustNorm):
    """

    Tukey's biweight function for M-estimation.

    Parameters
    ----------
    c : float, optional
        The tuning constant for Tukey's Biweight.  The default value is
        c = 4.685.

    Notes
    -----
    Tukey's biweight is sometime's called bisquare.
    """
    c: Incomplete
    def __init__(self, c: float = 4.685) -> None: ...
    def rho(self, z):
        """
        The robust criterion function for Tukey's biweight estimator

        Parameters
        ----------
        z : array_like
            1d array

        Returns
        -------
        rho : ndarray
            rho(z) = -(1 - (z/c)**2)**3 * c**2/6.   for \\|z\\| <= R

            rho(z) = 0                              for \\|z\\| > R
        """
    def psi(self, z):
        """
        The psi function for Tukey's biweight estimator

        The analytic derivative of rho

        Parameters
        ----------
        z : array_like
            1d array

        Returns
        -------
        psi : ndarray
            psi(z) = z*(1 - (z/c)**2)**2        for \\|z\\| <= R

            psi(z) = 0                           for \\|z\\| > R
        """
    def weights(self, z):
        """
        Tukey's biweight weighting function for the IRLS algorithm

        The psi function scaled by z

        Parameters
        ----------
        z : array_like
            1d array

        Returns
        -------
        weights : ndarray
            psi(z) = (1 - (z/c)**2)**2          for \\|z\\| <= R

            psi(z) = 0                          for \\|z\\| > R
        """
    def psi_deriv(self, z):
        """
        The derivative of Tukey's biweight psi function

        Notes
        -----
        Used to estimate the robust covariance matrix.
        """

class MQuantileNorm(RobustNorm):
    """M-quantiles objective function based on a base norm

    This norm has the same asymmetric structure as the objective function
    in QuantileRegression but replaces the L1 absolute value by a chosen
    base norm.

        rho_q(u) = abs(q - I(q < 0)) * rho_base(u)

    or, equivalently,

        rho_q(u) = q * rho_base(u)  if u >= 0
        rho_q(u) = (1 - q) * rho_base(u)  if u < 0


    Parameters
    ----------
    q : float
        M-quantile, must be between 0 and 1
    base_norm : RobustNorm instance
        basic norm that is transformed into an asymmetric M-quantile norm

    Notes
    -----
    This is mainly for base norms that are not redescending, like HuberT or
    LeastSquares. (See Jones for the relationship of M-quantiles to quantiles
    in the case of non-redescending Norms.)

    Expectiles are M-quantiles with the LeastSquares as base norm.

    References
    ----------

    .. [*] Bianchi, Annamaria, and Nicola Salvati. 2015. “Asymptotic Properties
       and Variance Estimators of the M-Quantile Regression Coefficients
       Estimators.” Communications in Statistics - Theory and Methods 44 (11):
       2416–29. doi:10.1080/03610926.2013.791375.

    .. [*] Breckling, Jens, and Ray Chambers. 1988. “M-Quantiles.”
       Biometrika 75 (4): 761–71. doi:10.2307/2336317.

    .. [*] Jones, M. C. 1994. “Expectiles and M-Quantiles Are Quantiles.”
       Statistics & Probability Letters 20 (2): 149–53.
       doi:10.1016/0167-7152(94)90031-0.

    .. [*] Newey, Whitney K., and James L. Powell. 1987. “Asymmetric Least
       Squares Estimation and Testing.” Econometrica 55 (4): 819–47.
       doi:10.2307/1911031.
    """
    q: Incomplete
    base_norm: Incomplete
    def __init__(self, q, base_norm) -> None: ...
    def rho(self, z):
        """
        The robust criterion function for MQuantileNorm.

        Parameters
        ----------
        z : array_like
            1d array

        Returns
        -------
        rho : ndarray
        """
    def psi(self, z):
        """
        The psi function for MQuantileNorm estimator.

        The analytic derivative of rho

        Parameters
        ----------
        z : array_like
            1d array

        Returns
        -------
        psi : ndarray
        """
    def weights(self, z):
        """
        MQuantileNorm weighting function for the IRLS algorithm

        The psi function scaled by z, psi(z) / z

        Parameters
        ----------
        z : array_like
            1d array

        Returns
        -------
        weights : ndarray
        """
    def psi_deriv(self, z):
        """
        The derivative of MQuantileNorm function

        Parameters
        ----------
        z : array_like
            1d array

        Returns
        -------
        psi_deriv : ndarray

        Notes
        -----
        Used to estimate the robust covariance matrix.
        """
    def __call__(self, z):
        """
        Returns the value of estimator rho applied to an input
        """

def estimate_location(a, scale, norm: Incomplete | None = None, axis: int = 0, initial: Incomplete | None = None, maxiter: int = 30, tol: float = 1e-06):
    """
    M-estimator of location using self.norm and a current
    estimator of scale.

    This iteratively finds a solution to

    norm.psi((a-mu)/scale).sum() == 0

    Parameters
    ----------
    a : ndarray
        Array over which the location parameter is to be estimated
    scale : ndarray
        Scale parameter to be used in M-estimator
    norm : RobustNorm, optional
        Robust norm used in the M-estimator.  The default is HuberT().
    axis : int, optional
        Axis along which to estimate the location parameter.  The default is 0.
    initial : ndarray, optional
        Initial condition for the location parameter.  Default is None, which
        uses the median of a.
    niter : int, optional
        Maximum number of iterations.  The default is 30.
    tol : float, optional
        Toleration for convergence.  The default is 1e-06.

    Returns
    -------
    mu : ndarray
        Estimate of location
    """
