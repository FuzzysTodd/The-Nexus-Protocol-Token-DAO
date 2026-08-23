from . import libmp as libmp
from .calculus.calculus import CalculusMethods as CalculusMethods
from .calculus.inverselaplace import LaplaceTransformInversionMethods as LaplaceTransformInversionMethods
from .calculus.odes import ODEMethods as ODEMethods
from .calculus.optimization import OptimizationMethods as OptimizationMethods
from .calculus.quadrature import QuadratureMethods as QuadratureMethods
from .functions.functions import SpecialFunctions as SpecialFunctions
from .functions.rszeta import RSCache as RSCache
from .identification import IdentificationMethods as IdentificationMethods
from .libmp.backend import xrange as xrange
from .matrices.calculus import MatrixCalculusMethods as MatrixCalculusMethods
from .matrices.eigen import Eigen as Eigen
from .matrices.linalg import LinearAlgebraMethods as LinearAlgebraMethods
from .matrices.matrices import MatrixMethods as MatrixMethods
from .visualization import VisualizationMethods as VisualizationMethods
from _typeshed import Incomplete

class Context: ...

class StandardBaseContext(Context, SpecialFunctions, RSCache, QuadratureMethods, LaplaceTransformInversionMethods, CalculusMethods, MatrixMethods, MatrixCalculusMethods, LinearAlgebraMethods, Eigen, IdentificationMethods, OptimizationMethods, ODEMethods, VisualizationMethods):
    NoConvergence = libmp.NoConvergence
    ComplexResult = libmp.ComplexResult
    def __init__(ctx) -> None: ...
    verbose: bool
    def warn(ctx, msg) -> None: ...
    def bad_domain(ctx, msg) -> None: ...
    def fneg(ctx, x, **kwargs): ...
    def fadd(ctx, x, y, **kwargs): ...
    def fsub(ctx, x, y, **kwargs): ...
    def fmul(ctx, x, y, **kwargs): ...
    def fdiv(ctx, x, y, **kwargs): ...
    def fsum(ctx, args, absolute: bool = False, squared: bool = False): ...
    def fdot(ctx, xs, ys: Incomplete | None = None, conjugate: bool = False): ...
    def fprod(ctx, args): ...
    def nprint(ctx, x, n: int = 6, **kwargs) -> None:
        """
        Equivalent to ``print(nstr(x, n))``.
        """
    def chop(ctx, x, tol: Incomplete | None = None):
        """
        Chops off small real or imaginary parts, or converts
        numbers close to zero to exact zeros. The input can be a
        single number or an iterable::

            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = False
            >>> chop(5+1e-10j, tol=1e-9)
            mpf('5.0')
            >>> nprint(chop([1.0, 1e-20, 3+1e-18j, -4, 2]))
            [1.0, 0.0, 3.0, -4.0, 2.0]

        The tolerance defaults to ``100*eps``.
        """
    def almosteq(ctx, s, t, rel_eps: Incomplete | None = None, abs_eps: Incomplete | None = None):
        """
        Determine whether the difference between `s` and `t` is smaller
        than a given epsilon, either relatively or absolutely.

        Both a maximum relative difference and a maximum difference
        ('epsilons') may be specified. The absolute difference is
        defined as `|s-t|` and the relative difference is defined
        as `|s-t|/\\max(|s|, |t|)`.

        If only one epsilon is given, both are set to the same value.
        If none is given, both epsilons are set to `2^{-p+m}` where
        `p` is the current working precision and `m` is a small
        integer. The default setting typically allows :func:`~mpmath.almosteq`
        to be used to check for mathematical equality
        in the presence of small rounding errors.

        **Examples**

            >>> from mpmath import *
            >>> mp.dps = 15
            >>> almosteq(3.141592653589793, 3.141592653589790)
            True
            >>> almosteq(3.141592653589793, 3.141592653589700)
            False
            >>> almosteq(3.141592653589793, 3.141592653589700, 1e-10)
            True
            >>> almosteq(1e-20, 2e-20)
            True
            >>> almosteq(1e-20, 2e-20, rel_eps=0, abs_eps=0)
            False

        """
    def arange(ctx, *args):
        """
        This is a generalized version of Python's :func:`~mpmath.range` function
        that accepts fractional endpoints and step sizes and
        returns a list of ``mpf`` instances. Like :func:`~mpmath.range`,
        :func:`~mpmath.arange` can be called with 1, 2 or 3 arguments:

        ``arange(b)``
            `[0, 1, 2, \\ldots, x]`
        ``arange(a, b)``
            `[a, a+1, a+2, \\ldots, x]`
        ``arange(a, b, h)``
            `[a, a+h, a+h, \\ldots, x]`

        where `b-1 \\le x < b` (in the third case, `b-h \\le x < b`).

        Like Python's :func:`~mpmath.range`, the endpoint is not included. To
        produce ranges where the endpoint is included, :func:`~mpmath.linspace`
        is more convenient.

        **Examples**

            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = False
            >>> arange(4)
            [mpf('0.0'), mpf('1.0'), mpf('2.0'), mpf('3.0')]
            >>> arange(1, 2, 0.25)
            [mpf('1.0'), mpf('1.25'), mpf('1.5'), mpf('1.75')]
            >>> arange(1, -1, -0.75)
            [mpf('1.0'), mpf('0.25'), mpf('-0.5')]

        """
    def linspace(ctx, *args, **kwargs):
        """
        ``linspace(a, b, n)`` returns a list of `n` evenly spaced
        samples from `a` to `b`. The syntax ``linspace(mpi(a,b), n)``
        is also valid.

        This function is often more convenient than :func:`~mpmath.arange`
        for partitioning an interval into subintervals, since
        the endpoint is included::

            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = False
            >>> linspace(1, 4, 4)
            [mpf('1.0'), mpf('2.0'), mpf('3.0'), mpf('4.0')]

        You may also provide the keyword argument ``endpoint=False``::

            >>> linspace(1, 4, 4, endpoint=False)
            [mpf('1.0'), mpf('1.75'), mpf('2.5'), mpf('3.25')]

        """
    def cos_sin(ctx, z, **kwargs): ...
    def cospi_sinpi(ctx, z, **kwargs): ...
    list_primes: Incomplete
    isprime: Incomplete
    bernfrac: Incomplete
    moebius: Incomplete
    def sum_accurately(ctx, terms, check_step: int = 1): ...
    def mul_accurately(ctx, factors, check_step: int = 1): ...
    def power(ctx, x, y):
        """Converts `x` and `y` to mpmath numbers and evaluates
        `x^y = \\exp(y \\log(x))`::

            >>> from mpmath import *
            >>> mp.dps = 30; mp.pretty = True
            >>> power(2, 0.5)
            1.41421356237309504880168872421

        This shows the leading few digits of a large Mersenne prime
        (performing the exact calculation ``2**43112609-1`` and
        displaying the result in Python would be very slow)::

            >>> power(2, 43112609)-1
            3.16470269330255923143453723949e+12978188
        """
    def maxcalls(ctx, f, N):
        """
        Return a wrapped copy of *f* that raises ``NoConvergence`` when *f*
        has been called more than *N* times::

            >>> from mpmath import *
            >>> mp.dps = 15
            >>> f = maxcalls(sin, 10)
            >>> print(sum(f(n) for n in range(10)))
            1.95520948210738
            >>> f(10) # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
              ...
            NoConvergence: maxcalls: function evaluated 10 times

        """
    def memoize(ctx, f):
        """
        Return a wrapped copy of *f* that caches computed values, i.e.
        a memoized copy of *f*. Values are only reused if the cached precision
        is equal to or higher than the working precision::

            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = True
            >>> f = memoize(maxcalls(sin, 1))
            >>> f(2)
            0.909297426825682
            >>> f(2)
            0.909297426825682
            >>> mp.dps = 25
            >>> f(2) # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
              ...
            NoConvergence: maxcalls: function evaluated 1 times

        """
