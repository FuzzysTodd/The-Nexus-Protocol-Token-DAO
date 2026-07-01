from _typeshed import Incomplete
from sympy.core.add import Add as Add
from sympy.core.containers import Tuple as Tuple
from sympy.core.expr import Expr as Expr
from sympy.core.numbers import oo as oo, pi as pi
from sympy.core.singleton import S as S
from sympy.core.symbol import Dummy as Dummy, Symbol as Symbol, Wild as Wild
from sympy.core.sympify import sympify as sympify
from sympy.functions.elementary.trigonometric import cos as cos, sin as sin, sinc as sinc
from sympy.series.sequences import SeqFormula as SeqFormula
from sympy.series.series_class import SeriesBase as SeriesBase
from sympy.sets.sets import Interval as Interval
from sympy.utilities.iterables import is_sequence as is_sequence

def fourier_cos_seq(func, limits, n):
    """Returns the cos sequence in a Fourier series"""
def fourier_sin_seq(func, limits, n):
    """Returns the sin sequence in a Fourier series"""
def finite_check(f, x, L): ...

class FourierSeries(SeriesBase):
    """Represents Fourier sine/cosine series.

    Explanation
    ===========

    This class only represents a fourier series.
    No computation is performed.

    For how to compute Fourier series, see the :func:`fourier_series`
    docstring.

    See Also
    ========

    sympy.series.fourier.fourier_series
    """
    def __new__(cls, *args): ...
    @property
    def function(self): ...
    @property
    def x(self): ...
    @property
    def period(self): ...
    @property
    def a0(self): ...
    @property
    def an(self): ...
    @property
    def bn(self): ...
    @property
    def interval(self): ...
    @property
    def start(self): ...
    @property
    def stop(self): ...
    @property
    def length(self): ...
    @property
    def L(self): ...
    def truncate(self, n: int = 3):
        """
        Return the first n nonzero terms of the series.

        If ``n`` is None return an iterator.

        Parameters
        ==========

        n : int or None
            Amount of non-zero terms in approximation or None.

        Returns
        =======

        Expr or iterator :
            Approximation of function expanded into Fourier series.

        Examples
        ========

        >>> from sympy import fourier_series, pi
        >>> from sympy.abc import x
        >>> s = fourier_series(x, (x, -pi, pi))
        >>> s.truncate(4)
        2*sin(x) - sin(2*x) + 2*sin(3*x)/3 - sin(4*x)/2

        See Also
        ========

        sympy.series.fourier.FourierSeries.sigma_approximation
        """
    def sigma_approximation(self, n: int = 3):
        """
        Return :math:`\\sigma`-approximation of Fourier series with respect
        to order n.

        Explanation
        ===========

        Sigma approximation adjusts a Fourier summation to eliminate the Gibbs
        phenomenon which would otherwise occur at discontinuities.
        A sigma-approximated summation for a Fourier series of a T-periodical
        function can be written as

        .. math::
            s(\\theta) = \\frac{1}{2} a_0 + \\sum _{k=1}^{m-1}
            \\operatorname{sinc} \\Bigl( \\frac{k}{m} \\Bigr) \\cdot
            \\left[ a_k \\cos \\Bigl( \\frac{2\\pi k}{T} \\theta \\Bigr)
            + b_k \\sin \\Bigl( \\frac{2\\pi k}{T} \\theta \\Bigr) \\right],

        where :math:`a_0, a_k, b_k, k=1,\\ldots,{m-1}` are standard Fourier
        series coefficients and
        :math:`\\operatorname{sinc} \\Bigl( \\frac{k}{m} \\Bigr)` is a Lanczos
        :math:`\\sigma` factor (expressed in terms of normalized
        :math:`\\operatorname{sinc}` function).

        Parameters
        ==========

        n : int
            Highest order of the terms taken into account in approximation.

        Returns
        =======

        Expr :
            Sigma approximation of function expanded into Fourier series.

        Examples
        ========

        >>> from sympy import fourier_series, pi
        >>> from sympy.abc import x
        >>> s = fourier_series(x, (x, -pi, pi))
        >>> s.sigma_approximation(4)
        2*sin(x)*sinc(pi/4) - 2*sin(2*x)/pi + 2*sin(3*x)*sinc(3*pi/4)/3

        See Also
        ========

        sympy.series.fourier.FourierSeries.truncate

        Notes
        =====

        The behaviour of
        :meth:`~sympy.series.fourier.FourierSeries.sigma_approximation`
        is different from :meth:`~sympy.series.fourier.FourierSeries.truncate`
        - it takes all nonzero terms of degree smaller than n, rather than
        first n nonzero ones.

        References
        ==========

        .. [1] https://en.wikipedia.org/wiki/Gibbs_phenomenon
        .. [2] https://en.wikipedia.org/wiki/Sigma_approximation
        """
    def shift(self, s):
        """
        Shift the function by a term independent of x.

        Explanation
        ===========

        f(x) -> f(x) + s

        This is fast, if Fourier series of f(x) is already
        computed.

        Examples
        ========

        >>> from sympy import fourier_series, pi
        >>> from sympy.abc import x
        >>> s = fourier_series(x**2, (x, -pi, pi))
        >>> s.shift(1).truncate()
        -4*cos(x) + cos(2*x) + 1 + pi**2/3
        """
    def shiftx(self, s):
        """
        Shift x by a term independent of x.

        Explanation
        ===========

        f(x) -> f(x + s)

        This is fast, if Fourier series of f(x) is already
        computed.

        Examples
        ========

        >>> from sympy import fourier_series, pi
        >>> from sympy.abc import x
        >>> s = fourier_series(x**2, (x, -pi, pi))
        >>> s.shiftx(1).truncate()
        -4*cos(x + 1) + cos(2*x + 2) + pi**2/3
        """
    def scale(self, s):
        """
        Scale the function by a term independent of x.

        Explanation
        ===========

        f(x) -> s * f(x)

        This is fast, if Fourier series of f(x) is already
        computed.

        Examples
        ========

        >>> from sympy import fourier_series, pi
        >>> from sympy.abc import x
        >>> s = fourier_series(x**2, (x, -pi, pi))
        >>> s.scale(2).truncate()
        -8*cos(x) + 2*cos(2*x) + 2*pi**2/3
        """
    def scalex(self, s):
        """
        Scale x by a term independent of x.

        Explanation
        ===========

        f(x) -> f(s*x)

        This is fast, if Fourier series of f(x) is already
        computed.

        Examples
        ========

        >>> from sympy import fourier_series, pi
        >>> from sympy.abc import x
        >>> s = fourier_series(x**2, (x, -pi, pi))
        >>> s.scalex(2).truncate()
        -4*cos(2*x) + cos(4*x) + pi**2/3
        """
    def __neg__(self): ...
    def __add__(self, other): ...
    def __sub__(self, other): ...

class FiniteFourierSeries(FourierSeries):
    """Represents Finite Fourier sine/cosine series.

    For how to compute Fourier series, see the :func:`fourier_series`
    docstring.

    Parameters
    ==========

    f : Expr
        Expression for finding fourier_series

    limits : ( x, start, stop)
        x is the independent variable for the expression f
        (start, stop) is the period of the fourier series

    exprs: (a0, an, bn) or Expr
        a0 is the constant term a0 of the fourier series
        an is a dictionary of coefficients of cos terms
         an[k] = coefficient of cos(pi*(k/L)*x)
        bn is a dictionary of coefficients of sin terms
         bn[k] = coefficient of sin(pi*(k/L)*x)

        or exprs can be an expression to be converted to fourier form

    Methods
    =======

    This class is an extension of FourierSeries class.
    Please refer to sympy.series.fourier.FourierSeries for
    further information.

    See Also
    ========

    sympy.series.fourier.FourierSeries
    sympy.series.fourier.fourier_series
    """
    def __new__(cls, f, limits, exprs): ...
    @property
    def interval(self): ...
    @property
    def length(self): ...
    def shiftx(self, s): ...
    def scale(self, s): ...
    def scalex(self, s): ...
    def __add__(self, other): ...

def fourier_series(f, limits: Incomplete | None = None, finite: bool = True):
    """Computes the Fourier trigonometric series expansion.

    Explanation
    ===========

    Fourier trigonometric series of $f(x)$ over the interval $(a, b)$
    is defined as:

    .. math::
        \\frac{a_0}{2} + \\sum_{n=1}^{\\infty}
        (a_n \\cos(\\frac{2n \\pi x}{L}) + b_n \\sin(\\frac{2n \\pi x}{L}))

    where the coefficients are:

    .. math::
        L = b - a

    .. math::
        a_0 = \\frac{2}{L} \\int_{a}^{b}{f(x) dx}

    .. math::
        a_n = \\frac{2}{L} \\int_{a}^{b}{f(x) \\cos(\\frac{2n \\pi x}{L}) dx}

    .. math::
        b_n = \\frac{2}{L} \\int_{a}^{b}{f(x) \\sin(\\frac{2n \\pi x}{L}) dx}

    The condition whether the function $f(x)$ given should be periodic
    or not is more than necessary, because it is sufficient to consider
    the series to be converging to $f(x)$ only in the given interval,
    not throughout the whole real line.

    This also brings a lot of ease for the computation because
    you do not have to make $f(x)$ artificially periodic by
    wrapping it with piecewise, modulo operations,
    but you can shape the function to look like the desired periodic
    function only in the interval $(a, b)$, and the computed series will
    automatically become the series of the periodic version of $f(x)$.

    This property is illustrated in the examples section below.

    Parameters
    ==========

    limits : (sym, start, end), optional
        *sym* denotes the symbol the series is computed with respect to.

        *start* and *end* denotes the start and the end of the interval
        where the fourier series converges to the given function.

        Default range is specified as $-\\pi$ and $\\pi$.

    Returns
    =======

    FourierSeries
        A symbolic object representing the Fourier trigonometric series.

    Examples
    ========

    Computing the Fourier series of $f(x) = x^2$:

    >>> from sympy import fourier_series, pi
    >>> from sympy.abc import x
    >>> f = x**2
    >>> s = fourier_series(f, (x, -pi, pi))
    >>> s1 = s.truncate(n=3)
    >>> s1
    -4*cos(x) + cos(2*x) + pi**2/3

    Shifting of the Fourier series:

    >>> s.shift(1).truncate()
    -4*cos(x) + cos(2*x) + 1 + pi**2/3
    >>> s.shiftx(1).truncate()
    -4*cos(x + 1) + cos(2*x + 2) + pi**2/3

    Scaling of the Fourier series:

    >>> s.scale(2).truncate()
    -8*cos(x) + 2*cos(2*x) + 2*pi**2/3
    >>> s.scalex(2).truncate()
    -4*cos(2*x) + cos(4*x) + pi**2/3

    Computing the Fourier series of $f(x) = x$:

    This illustrates how truncating to the higher order gives better
    convergence.

    .. plot::
        :context: reset
        :format: doctest
        :include-source: True

        >>> from sympy import fourier_series, pi, plot
        >>> from sympy.abc import x
        >>> f = x
        >>> s = fourier_series(f, (x, -pi, pi))
        >>> s1 = s.truncate(n = 3)
        >>> s2 = s.truncate(n = 5)
        >>> s3 = s.truncate(n = 7)
        >>> p = plot(f, s1, s2, s3, (x, -pi, pi), show=False, legend=True)

        >>> p[0].line_color = (0, 0, 0)
        >>> p[0].label = 'x'
        >>> p[1].line_color = (0.7, 0.7, 0.7)
        >>> p[1].label = 'n=3'
        >>> p[2].line_color = (0.5, 0.5, 0.5)
        >>> p[2].label = 'n=5'
        >>> p[3].line_color = (0.3, 0.3, 0.3)
        >>> p[3].label = 'n=7'

        >>> p.show()

    This illustrates how the series converges to different sawtooth
    waves if the different ranges are specified.

    .. plot::
        :context: close-figs
        :format: doctest
        :include-source: True

        >>> s1 = fourier_series(x, (x, -1, 1)).truncate(10)
        >>> s2 = fourier_series(x, (x, -pi, pi)).truncate(10)
        >>> s3 = fourier_series(x, (x, 0, 1)).truncate(10)
        >>> p = plot(x, s1, s2, s3, (x, -5, 5), show=False, legend=True)

        >>> p[0].line_color = (0, 0, 0)
        >>> p[0].label = 'x'
        >>> p[1].line_color = (0.7, 0.7, 0.7)
        >>> p[1].label = '[-1, 1]'
        >>> p[2].line_color = (0.5, 0.5, 0.5)
        >>> p[2].label = '[-pi, pi]'
        >>> p[3].line_color = (0.3, 0.3, 0.3)
        >>> p[3].label = '[0, 1]'

        >>> p.show()

    Notes
    =====

    Computing Fourier series can be slow
    due to the integration required in computing
    an, bn.

    It is faster to compute Fourier series of a function
    by using shifting and scaling on an already
    computed Fourier series rather than computing
    again.

    e.g. If the Fourier series of ``x**2`` is known
    the Fourier series of ``x**2 - 1`` can be found by shifting by ``-1``.

    See Also
    ========

    sympy.series.fourier.FourierSeries

    References
    ==========

    .. [1] https://mathworld.wolfram.com/FourierSeries.html
    """
