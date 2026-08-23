from _typeshed import Incomplete
from statsmodels.tsa.arima_process import ArmaProcess as ArmaProcess

class ArmaFft(ArmaProcess):
    """fft tools for arma processes

    This class contains several methods that are providing the same or similar
    returns to try out and test different implementations.

    Notes
    -----
    TODO:
    check whether we do not want to fix maxlags, and create new instance if
    maxlag changes. usage for different lengths of timeseries ?
    or fix frequency and length for fft

    check default frequencies w, terminology norw  n_or_w

    some ffts are currently done without padding with zeros

    returns for spectral density methods needs checking, is it always the power
    spectrum hw*hw.conj()

    normalization of the power spectrum, spectral density: not checked yet, for
    example no variance of underlying process is used

    """
    ar: Incomplete
    ma: Incomplete
    nobs: Incomplete
    arpoly: Incomplete
    mapoly: Incomplete
    nar: Incomplete
    nma: Incomplete
    def __init__(self, ar, ma, n) -> None: ...
    def padarr(self, arr, maxlag, atend: bool = True):
        """pad 1d array with zeros at end to have length maxlag
        function that is a method, no self used

        Parameters
        ----------
        arr : array_like, 1d
            array that will be padded with zeros
        maxlag : int
            length of array after padding
        atend : bool
            If True (default), then the zeros are added to the end, otherwise
            to the front of the array

        Returns
        -------
        arrp : ndarray
            zero-padded array

        Notes
        -----
        This is mainly written to extend coefficient arrays for the lag-polynomials.
        It returns a copy.

        """
    def pad(self, maxlag):
        """construct AR and MA polynomials that are zero-padded to a common length

        Parameters
        ----------
        maxlag : int
            new length of lag-polynomials

        Returns
        -------
        ar : ndarray
            extended AR polynomial coefficients
        ma : ndarray
            extended AR polynomial coefficients

        """
    def fftar(self, n: Incomplete | None = None):
        """Fourier transform of AR polynomial, zero-padded at end to n

        Parameters
        ----------
        n : int
            length of array after zero-padding

        Returns
        -------
        fftar : ndarray
            fft of zero-padded ar polynomial
        """
    def fftma(self, n):
        """Fourier transform of MA polynomial, zero-padded at end to n

        Parameters
        ----------
        n : int
            length of array after zero-padding

        Returns
        -------
        fftar : ndarray
            fft of zero-padded ar polynomial
        """
    def fftarma(self, n: Incomplete | None = None):
        """Fourier transform of ARMA polynomial, zero-padded at end to n

        The Fourier transform of the ARMA process is calculated as the ratio
        of the fft of the MA polynomial divided by the fft of the AR polynomial.

        Parameters
        ----------
        n : int
            length of array after zero-padding

        Returns
        -------
        fftarma : ndarray
            fft of zero-padded arma polynomial
        """
    def spd(self, npos):
        """raw spectral density, returns Fourier transform

        n is number of points in positive spectrum, the actual number of points
        is twice as large. different from other spd methods with fft
        """
    def spdshift(self, n):
        """power spectral density using fftshift

        currently returns two-sided according to fft frequencies, use first half
        """
    def spddirect(self, n):
        """power spectral density using padding to length n done by fft

        currently returns two-sided according to fft frequencies, use first half
        """
    def spdroots(self, w):
        """spectral density for frequency using polynomial roots

        builds two arrays (number of roots, number of frequencies)
        """
    def spdpoly(self, w, nma: int = 50):
        """spectral density from MA polynomial representation for ARMA process

        References
        ----------
        Cochrane, section 8.3.3
        """
    def filter(self, x):
        """
        filter a timeseries with the ARMA filter

        padding with zero is missing, in example I needed the padding to get
        initial conditions identical to direct filter

        Initial filtered observations differ from filter2 and signal.lfilter, but
        at end they are the same.

        See Also
        --------
        tsa.filters.fftconvolve

        """
    def filter2(self, x, pad: int = 0):
        """filter a time series using fftconvolve3 with ARMA filter

        padding of x currently works only if x is 1d
        in example it produces same observations at beginning as lfilter even
        without padding.

        TODO: this returns 1 additional observation at the end
        """
    def acf2spdfreq(self, acovf, nfreq: int = 100, w: Incomplete | None = None):
        """
        not really a method
        just for comparison, not efficient for large n or long acf

        this is also similarly use in tsa.stattools.periodogram with window
        """
    def invpowerspd(self, n):
        """autocovariance from spectral density

        scaling is correct, but n needs to be large for numerical accuracy
        maybe padding with zero in fft would be faster
        without slicing it returns 2-sided autocovariance with fftshift

        >>> ArmaFft([1, -0.5], [1., 0.4], 40).invpowerspd(2**8)[:10]
        array([ 2.08    ,  1.44    ,  0.72    ,  0.36    ,  0.18    ,  0.09    ,
                0.045   ,  0.0225  ,  0.01125 ,  0.005625])
        >>> ArmaFft([1, -0.5], [1., 0.4], 40).acovf(10)
        array([ 2.08    ,  1.44    ,  0.72    ,  0.36    ,  0.18    ,  0.09    ,
                0.045   ,  0.0225  ,  0.01125 ,  0.005625])
        """
    def spdmapoly(self, w, twosided: bool = False):
        """ma only, need division for ar, use LagPolynomial
        """
    def plot4(self, fig: Incomplete | None = None, nobs: int = 100, nacf: int = 20, nfreq: int = 100):
        """Plot results"""

def spdar1(ar, w): ...
