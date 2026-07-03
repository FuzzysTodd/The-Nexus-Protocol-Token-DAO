from _typeshed import Incomplete
from statsmodels import regression as regression
from statsmodels.graphics.tsaplots import plot_acf as plot_acf
from statsmodels.tsa.arima.model import ARIMA as ARIMA
from statsmodels.tsa.arima_process import arma_acf as arma_acf, arma_acovf as arma_acovf, arma_generate_sample as arma_generate_sample, arma_impulse_response as arma_impulse_response
from statsmodels.tsa.stattools import acf as acf, acovf as acovf

ar: Incomplete
ma: Incomplete
mod: str
x: Incomplete
x_acf: Incomplete
x_ir: Incomplete

def detrend(x, key: Incomplete | None = None): ...
def demean(x, axis: int = 0):
    """Return x minus its mean along the specified axis"""
def detrend_mean(x):
    """Return x minus the mean(x)"""
def detrend_none(x):
    """Return x: no detrending"""
def detrend_linear(y):
    """Return y minus best fit line; 'linear' detrending """
def acovf_explicit(ar, ma, nobs):
    """add correlation of MA representation explicitely

    """
def acovf_arma11(ar, ma): ...
def acovf_ma2(ma): ...
def acovf_ma1(ma): ...

ar1: Incomplete
ar0: Incomplete
ma1: Incomplete
ma2: Incomplete
ma0: Incomplete
comparefn: Incomplete
cases: Incomplete
myacovf: Incomplete
myacf: Incomplete
othacovf: Incomplete

def ar_generator(N: int = 512, sigma: float = 1.0): ...
def autocorr(s, axis: int = -1):
    """Returns the autocorrelation of signal s at all lags. Adheres to the
definition r(k) = E{s(n)s*(n-k)} where E{} is the expectation operator.
"""
def norm_corr(x, y, mode: str = 'valid'):
    """Returns the correlation between two ndarrays, by calling np.correlate in
'same' mode and normalizing the result by the std of the arrays and by
their lengths. This results in a correlation = 1 for an auto-correlation"""
def pltacorr(self, x, **kwargs):
    """
    call signature::

        acorr(x, normed=True, detrend=detrend_none, usevlines=True,
              maxlags=10, **kwargs)

    Plot the autocorrelation of *x*.  If *normed* = *True*,
    normalize the data by the autocorrelation at 0-th lag.  *x* is
    detrended by the *detrend* callable (default no normalization).

    Data are plotted as ``plot(lags, c, **kwargs)``

    Return value is a tuple (*lags*, *c*, *line*) where:

      - *lags* are a length 2*maxlags+1 lag vector

      - *c* is the 2*maxlags+1 auto correlation vector

      - *line* is a :class:`~matplotlib.lines.Line2D` instance
        returned by :meth:`plot`

    The default *linestyle* is None and the default *marker* is
    ``'o'``, though these can be overridden with keyword args.
    The cross correlation is performed with
    :func:`numpy.correlate` with *mode* = 2.

    If *usevlines* is *True*, :meth:`~matplotlib.axes.Axes.vlines`
    rather than :meth:`~matplotlib.axes.Axes.plot` is used to draw
    vertical lines from the origin to the acorr.  Otherwise, the
    plot style is determined by the kwargs, which are
    :class:`~matplotlib.lines.Line2D` properties.

    *maxlags* is a positive integer detailing the number of lags
    to show.  The default value of *None* will return all
    :math:`2 \\mathrm{len}(x) - 1` lags.

    The return value is a tuple (*lags*, *c*, *linecol*, *b*)
    where

    - *linecol* is the
      :class:`~matplotlib.collections.LineCollection`

    - *b* is the *x*-axis.

    .. seealso::

        :meth:`~matplotlib.axes.Axes.plot` or
        :meth:`~matplotlib.axes.Axes.vlines`
           For documentation on valid kwargs.

    **Example:**

    :func:`~matplotlib.pyplot.xcorr` above, and
    :func:`~matplotlib.pyplot.acorr` below.

    **Example:**

    .. plot:: mpl_examples/pylab_examples/xcorr_demo.py
    """
def pltxcorr(self, x, y, normed: bool = True, detrend=..., usevlines: bool = True, maxlags: int = 10, **kwargs):
    """
    call signature::

        def xcorr(self, x, y, normed=True, detrend=detrend_none,
          usevlines=True, maxlags=10, **kwargs):

    Plot the cross correlation between *x* and *y*.  If *normed* =
    *True*, normalize the data by the cross correlation at 0-th
    lag.  *x* and y are detrended by the *detrend* callable
    (default no normalization).  *x* and *y* must be equal length.

    Data are plotted as ``plot(lags, c, **kwargs)``

    Return value is a tuple (*lags*, *c*, *line*) where:

      - *lags* are a length ``2*maxlags+1`` lag vector

      - *c* is the ``2*maxlags+1`` auto correlation vector

      - *line* is a :class:`~matplotlib.lines.Line2D` instance
         returned by :func:`~matplotlib.pyplot.plot`.

    The default *linestyle* is *None* and the default *marker* is
    'o', though these can be overridden with keyword args.  The
    cross correlation is performed with :func:`numpy.correlate`
    with *mode* = 2.

    If *usevlines* is *True*:

       :func:`~matplotlib.pyplot.vlines`
       rather than :func:`~matplotlib.pyplot.plot` is used to draw
       vertical lines from the origin to the xcorr.  Otherwise the
       plotstyle is determined by the kwargs, which are
       :class:`~matplotlib.lines.Line2D` properties.

       The return value is a tuple (*lags*, *c*, *linecol*, *b*)
       where *linecol* is the
       :class:`matplotlib.collections.LineCollection` instance and
       *b* is the *x*-axis.

    *maxlags* is a positive integer detailing the number of lags to show.
    The default value of *None* will return all ``(2*len(x)-1)`` lags.

    **Example:**

    :func:`~matplotlib.pyplot.xcorr` above, and
    :func:`~matplotlib.pyplot.acorr` below.

    **Example:**

    .. plot:: mpl_examples/pylab_examples/xcorr_demo.py
    """

arrvs: Incomplete
arma: Incomplete
res: Incomplete
acf1: Incomplete
acovf1b: Incomplete
acf2: Incomplete
acf2m: Incomplete
ax: Incomplete
