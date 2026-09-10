from _typeshed import Incomplete

__all__ = ['diff', 'tilbert', 'itilbert', 'hilbert', 'ihilbert', 'cs_diff', 'cc_diff', 'sc_diff', 'ss_diff', 'shift']

def diff(x, order: int = 1, period: Incomplete | None = None, _cache=...):
    """
    Return kth derivative (or integral) of a periodic sequence x.

    If x_j and y_j are Fourier coefficients of periodic functions x
    and y, respectively, then::

      y_j = pow(sqrt(-1)*j*2*pi/period, order) * x_j
      y_0 = 0 if order is not 0.

    Parameters
    ----------
    x : array_like
        Input array.
    order : int, optional
        The order of differentiation. Default order is 1. If order is
        negative, then integration is carried out under the assumption
        that ``x_0 == 0``.
    period : float, optional
        The assumed period of the sequence. Default is ``2*pi``.

    Notes
    -----
    If ``sum(x, axis=0) = 0`` then ``diff(diff(x, k), -k) == x`` (within
    numerical accuracy).

    For odd order and even ``len(x)``, the Nyquist mode is taken zero.

    """
def tilbert(x, h, period: Incomplete | None = None, _cache=...):
    """
    Return h-Tilbert transform of a periodic sequence x.

    If x_j and y_j are Fourier coefficients of periodic functions x
    and y, respectively, then::

        y_j = sqrt(-1)*coth(j*h*2*pi/period) * x_j
        y_0 = 0

    Parameters
    ----------
    x : array_like
        The input array to transform.
    h : float
        Defines the parameter of the Tilbert transform.
    period : float, optional
        The assumed period of the sequence. Default period is ``2*pi``.

    Returns
    -------
    tilbert : ndarray
        The result of the transform.

    Notes
    -----
    If ``sum(x, axis=0) == 0`` and ``n = len(x)`` is odd, then
    ``tilbert(itilbert(x)) == x``.

    If ``2 * pi * h / period`` is approximately 10 or larger, then
    numerically ``tilbert == hilbert``
    (theoretically oo-Tilbert == Hilbert).

    For even ``len(x)``, the Nyquist mode of ``x`` is taken zero.

    """
def itilbert(x, h, period: Incomplete | None = None, _cache=...):
    """
    Return inverse h-Tilbert transform of a periodic sequence x.

    If ``x_j`` and ``y_j`` are Fourier coefficients of periodic functions x
    and y, respectively, then::

      y_j = -sqrt(-1)*tanh(j*h*2*pi/period) * x_j
      y_0 = 0

    For more details, see `tilbert`.

    """
def hilbert(x, _cache=...):
    """
    Return Hilbert transform of a periodic sequence x.

    If x_j and y_j are Fourier coefficients of periodic functions x
    and y, respectively, then::

      y_j = sqrt(-1)*sign(j) * x_j
      y_0 = 0

    Parameters
    ----------
    x : array_like
        The input array, should be periodic.
    _cache : dict, optional
        Dictionary that contains the kernel used to do a convolution with.

    Returns
    -------
    y : ndarray
        The transformed input.

    See Also
    --------
    scipy.signal.hilbert : Compute the analytic signal, using the Hilbert
                           transform.

    Notes
    -----
    If ``sum(x, axis=0) == 0`` then ``hilbert(ihilbert(x)) == x``.

    For even len(x), the Nyquist mode of x is taken zero.

    The sign of the returned transform does not have a factor -1 that is more
    often than not found in the definition of the Hilbert transform. Note also
    that `scipy.signal.hilbert` does have an extra -1 factor compared to this
    function.

    """
def ihilbert(x):
    """
    Return inverse Hilbert transform of a periodic sequence x.

    If ``x_j`` and ``y_j`` are Fourier coefficients of periodic functions x
    and y, respectively, then::

      y_j = -sqrt(-1)*sign(j) * x_j
      y_0 = 0

    """
def cs_diff(x, a, b, period: Incomplete | None = None, _cache=...):
    """
    Return (a,b)-cosh/sinh pseudo-derivative of a periodic sequence.

    If ``x_j`` and ``y_j`` are Fourier coefficients of periodic functions x
    and y, respectively, then::

      y_j = -sqrt(-1)*cosh(j*a*2*pi/period)/sinh(j*b*2*pi/period) * x_j
      y_0 = 0

    Parameters
    ----------
    x : array_like
        The array to take the pseudo-derivative from.
    a, b : float
        Defines the parameters of the cosh/sinh pseudo-differential
        operator.
    period : float, optional
        The period of the sequence. Default period is ``2*pi``.

    Returns
    -------
    cs_diff : ndarray
        Pseudo-derivative of periodic sequence `x`.

    Notes
    -----
    For even len(`x`), the Nyquist mode of `x` is taken as zero.

    """
def sc_diff(x, a, b, period: Incomplete | None = None, _cache=...):
    """
    Return (a,b)-sinh/cosh pseudo-derivative of a periodic sequence x.

    If x_j and y_j are Fourier coefficients of periodic functions x
    and y, respectively, then::

      y_j = sqrt(-1)*sinh(j*a*2*pi/period)/cosh(j*b*2*pi/period) * x_j
      y_0 = 0

    Parameters
    ----------
    x : array_like
        Input array.
    a,b : float
        Defines the parameters of the sinh/cosh pseudo-differential
        operator.
    period : float, optional
        The period of the sequence x. Default is 2*pi.

    Notes
    -----
    ``sc_diff(cs_diff(x,a,b),b,a) == x``
    For even ``len(x)``, the Nyquist mode of x is taken as zero.

    """
def ss_diff(x, a, b, period: Incomplete | None = None, _cache=...):
    """
    Return (a,b)-sinh/sinh pseudo-derivative of a periodic sequence x.

    If x_j and y_j are Fourier coefficients of periodic functions x
    and y, respectively, then::

      y_j = sinh(j*a*2*pi/period)/sinh(j*b*2*pi/period) * x_j
      y_0 = a/b * x_0

    Parameters
    ----------
    x : array_like
        The array to take the pseudo-derivative from.
    a,b
        Defines the parameters of the sinh/sinh pseudo-differential
        operator.
    period : float, optional
        The period of the sequence x. Default is ``2*pi``.

    Notes
    -----
    ``ss_diff(ss_diff(x,a,b),b,a) == x``

    """
def cc_diff(x, a, b, period: Incomplete | None = None, _cache=...):
    """
    Return (a,b)-cosh/cosh pseudo-derivative of a periodic sequence.

    If x_j and y_j are Fourier coefficients of periodic functions x
    and y, respectively, then::

      y_j = cosh(j*a*2*pi/period)/cosh(j*b*2*pi/period) * x_j

    Parameters
    ----------
    x : array_like
        The array to take the pseudo-derivative from.
    a,b : float
        Defines the parameters of the sinh/sinh pseudo-differential
        operator.
    period : float, optional
        The period of the sequence x. Default is ``2*pi``.

    Returns
    -------
    cc_diff : ndarray
        Pseudo-derivative of periodic sequence `x`.

    Notes
    -----
    ``cc_diff(cc_diff(x,a,b),b,a) == x``

    """
def shift(x, a, period: Incomplete | None = None, _cache=...):
    """
    Shift periodic sequence x by a: y(u) = x(u+a).

    If x_j and y_j are Fourier coefficients of periodic functions x
    and y, respectively, then::

          y_j = exp(j*a*2*pi/period*sqrt(-1)) * x_f

    Parameters
    ----------
    x : array_like
        The array to take the pseudo-derivative from.
    a : float
        Defines the parameters of the sinh/sinh pseudo-differential
    period : float, optional
        The period of the sequences x and y. Default period is ``2*pi``.
    """
