from . import function_docs as function_docs, libmp as libmp, rational as rational
from .ctx_base import StandardBaseContext as StandardBaseContext
from .ctx_mp_python import PythonMPContext as BaseMPContext, mpnumeric as mpnumeric
from .libmp import ComplexResult as ComplexResult, MPZ as MPZ, MPZ_ONE as MPZ_ONE, MPZ_ZERO as MPZ_ZERO, bitcount as bitcount, dps_to_prec as dps_to_prec, finf as finf, fnan as fnan, fninf as fninf, fone as fone, from_float as from_float, from_int as from_int, from_man_exp as from_man_exp, from_pickable as from_pickable, from_rational as from_rational, from_str as from_str, fzero as fzero, int_types as int_types, mpc_abs as mpc_abs, mpc_add as mpc_add, mpc_add_mpf as mpc_add_mpf, mpc_conjugate as mpc_conjugate, mpc_div as mpc_div, mpc_div_mpf as mpc_div_mpf, mpc_hash as mpc_hash, mpc_is_nonzero as mpc_is_nonzero, mpc_mpf_div as mpc_mpf_div, mpc_mul as mpc_mul, mpc_mul_int as mpc_mul_int, mpc_mul_mpf as mpc_mul_mpf, mpc_neg as mpc_neg, mpc_pos as mpc_pos, mpc_pow as mpc_pow, mpc_pow_int as mpc_pow_int, mpc_pow_mpf as mpc_pow_mpf, mpc_sub as mpc_sub, mpc_sub_mpf as mpc_sub_mpf, mpc_to_complex as mpc_to_complex, mpc_to_str as mpc_to_str, mpf_abs as mpf_abs, mpf_add as mpf_add, mpf_apery as mpf_apery, mpf_catalan as mpf_catalan, mpf_cmp as mpf_cmp, mpf_degree as mpf_degree, mpf_div as mpf_div, mpf_e as mpf_e, mpf_eq as mpf_eq, mpf_euler as mpf_euler, mpf_ge as mpf_ge, mpf_glaisher as mpf_glaisher, mpf_gt as mpf_gt, mpf_hash as mpf_hash, mpf_khinchin as mpf_khinchin, mpf_le as mpf_le, mpf_ln10 as mpf_ln10, mpf_ln2 as mpf_ln2, mpf_lt as mpf_lt, mpf_mertens as mpf_mertens, mpf_mod as mpf_mod, mpf_mul as mpf_mul, mpf_mul_int as mpf_mul_int, mpf_neg as mpf_neg, mpf_phi as mpf_phi, mpf_pi as mpf_pi, mpf_pos as mpf_pos, mpf_pow as mpf_pow, mpf_pow_int as mpf_pow_int, mpf_rand as mpf_rand, mpf_rdiv_int as mpf_rdiv_int, mpf_sub as mpf_sub, mpf_sum as mpf_sum, mpf_twinprime as mpf_twinprime, normalize as normalize, prec_to_dps as prec_to_dps, repr_dps as repr_dps, round_ceiling as round_ceiling, round_floor as round_floor, round_nearest as round_nearest, to_fixed as to_fixed, to_float as to_float, to_int as to_int, to_pickable as to_pickable, to_str as to_str
from .libmp.backend import BACKEND as BACKEND, basestring as basestring
from _typeshed import Incomplete

__docformat__: str
new: Incomplete
get_complex: Incomplete

class MPContext(BaseMPContext, StandardBaseContext):
    """
    Context for multiprecision arithmetic with a global precision.
    """
    def __init__(ctx) -> None: ...
    def init_builtins(ctx): ...
    def to_fixed(ctx, x, prec): ...
    def hypot(ctx, x, y):
        """
        Computes the Euclidean norm of the vector `(x, y)`, equal
        to `\\sqrt{x^2 + y^2}`. Both `x` and `y` must be real."""
    def bernoulli(ctx, n): ...
    def atan2(ctx, y, x): ...
    def psi(ctx, m, z): ...
    def cos_sin(ctx, x, **kwargs): ...
    def cospi_sinpi(ctx, x, **kwargs): ...
    def clone(ctx):
        """
        Create a copy of the context, with the same working precision.
        """
    def isnan(ctx, x):
        """
        Return *True* if *x* is a NaN (not-a-number), or for a complex
        number, whether either the real or complex part is NaN;
        otherwise return *False*::

            >>> from mpmath import *
            >>> isnan(3.14)
            False
            >>> isnan(nan)
            True
            >>> isnan(mpc(3.14,2.72))
            False
            >>> isnan(mpc(3.14,nan))
            True

        """
    def isfinite(ctx, x):
        """
        Return *True* if *x* is a finite number, i.e. neither
        an infinity or a NaN.

            >>> from mpmath import *
            >>> isfinite(inf)
            False
            >>> isfinite(-inf)
            False
            >>> isfinite(3)
            True
            >>> isfinite(nan)
            False
            >>> isfinite(3+4j)
            True
            >>> isfinite(mpc(3,inf))
            False
            >>> isfinite(mpc(nan,3))
            False

        """
    def isnpint(ctx, x):
        """
        Determine if *x* is a nonpositive integer.
        """
    def extraprec(ctx, n, normalize_output: bool = False):
        """
        The block

            with extraprec(n):
                <code>

        increases the precision n bits, executes <code>, and then
        restores the precision.

        extraprec(n)(f) returns a decorated version of the function f
        that increases the working precision by n bits before execution,
        and restores the parent precision afterwards. With
        normalize_output=True, it rounds the return value to the parent
        precision.
        """
    def extradps(ctx, n, normalize_output: bool = False):
        """
        This function is analogous to extraprec (see documentation)
        but changes the decimal precision instead of the number of bits.
        """
    def workprec(ctx, n, normalize_output: bool = False):
        """
        The block

            with workprec(n):
                <code>

        sets the precision to n bits, executes <code>, and then restores
        the precision.

        workprec(n)(f) returns a decorated version of the function f
        that sets the precision to n bits before execution,
        and restores the precision afterwards. With normalize_output=True,
        it rounds the return value to the parent precision.
        """
    def workdps(ctx, n, normalize_output: bool = False):
        """
        This function is analogous to workprec (see documentation)
        but changes the decimal precision instead of the number of bits.
        """
    def autoprec(ctx, f, maxprec: Incomplete | None = None, catch=(), verbose: bool = False):
        '''
        Return a wrapped copy of *f* that repeatedly evaluates *f*
        with increasing precision until the result converges to the
        full precision used at the point of the call.

        This heuristically protects against rounding errors, at the cost of
        roughly a 2x slowdown compared to manually setting the optimal
        precision. This method can, however, easily be fooled if the results
        from *f* depend "discontinuously" on the precision, for instance
        if catastrophic cancellation can occur. Therefore, :func:`~mpmath.autoprec`
        should be used judiciously.

        **Examples**

        Many functions are sensitive to perturbations of the input arguments.
        If the arguments are decimal numbers, they may have to be converted
        to binary at a much higher precision. If the amount of required
        extra precision is unknown, :func:`~mpmath.autoprec` is convenient::

            >>> from mpmath import *
            >>> mp.dps = 15
            >>> mp.pretty = True
            >>> besselj(5, 125 * 10**28)    # Exact input
            -8.03284785591801e-17
            >>> besselj(5, \'1.25e30\')   # Bad
            7.12954868316652e-16
            >>> autoprec(besselj)(5, \'1.25e30\')   # Good
            -8.03284785591801e-17

        The following fails to converge because `\\sin(\\pi) = 0` whereas all
        finite-precision approximations of `\\pi` give nonzero values::

            >>> autoprec(sin)(pi) # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
              ...
            NoConvergence: autoprec: prec increased to 2910 without convergence

        As the following example shows, :func:`~mpmath.autoprec` can protect against
        cancellation, but is fooled by too severe cancellation::

            >>> x = 1e-10
            >>> exp(x)-1; expm1(x); autoprec(lambda t: exp(t)-1)(x)
            1.00000008274037e-10
            1.00000000005e-10
            1.00000000005e-10
            >>> x = 1e-50
            >>> exp(x)-1; expm1(x); autoprec(lambda t: exp(t)-1)(x)
            0.0
            1.0e-50
            0.0

        With *catch*, an exception or list of exceptions to intercept
        may be specified. The raised exception is interpreted
        as signaling insufficient precision. This permits, for example,
        evaluating a function where a too low precision results in a
        division by zero::

            >>> f = lambda x: 1/(exp(x)-1)
            >>> f(1e-30)
            Traceback (most recent call last):
              ...
            ZeroDivisionError
            >>> autoprec(f, catch=ZeroDivisionError)(1e-30)
            1.0e+30


        '''
    def nstr(ctx, x, n: int = 6, **kwargs):
        '''
        Convert an ``mpf`` or ``mpc`` to a decimal string literal with *n*
        significant digits. The small default value for *n* is chosen to
        make this function useful for printing collections of numbers
        (lists, matrices, etc).

        If *x* is a list or tuple, :func:`~mpmath.nstr` is applied recursively
        to each element. For unrecognized classes, :func:`~mpmath.nstr`
        simply returns ``str(x)``.

        The companion function :func:`~mpmath.nprint` prints the result
        instead of returning it.

        The keyword arguments *strip_zeros*, *min_fixed*, *max_fixed*
        and *show_zero_exponent* are forwarded to :func:`~mpmath.libmp.to_str`.

        The number will be printed in fixed-point format if the position
        of the leading digit is strictly between min_fixed
        (default = min(-dps/3,-5)) and max_fixed (default = dps).

        To force fixed-point format always, set min_fixed = -inf,
        max_fixed = +inf. To force floating-point format, set
        min_fixed >= max_fixed.

            >>> from mpmath import *
            >>> nstr([+pi, ldexp(1,-500)])
            \'[3.14159, 3.05494e-151]\'
            >>> nprint([+pi, ldexp(1,-500)])
            [3.14159, 3.05494e-151]
            >>> nstr(mpf("5e-10"), 5)
            \'5.0e-10\'
            >>> nstr(mpf("5e-10"), 5, strip_zeros=False)
            \'5.0000e-10\'
            >>> nstr(mpf("5e-10"), 5, strip_zeros=False, min_fixed=-11)
            \'0.00000000050000\'
            >>> nstr(mpf(0), 5, show_zero_exponent=True)
            \'0.0e+0\'

        '''
    def mpmathify(ctx, *args, **kwargs): ...
    def hypsum(ctx, p, q, flags, coeffs, z, accurate_small: bool = True, **kwargs): ...
    def ldexp(ctx, x, n):
        """
        Computes `x 2^n` efficiently. No rounding is performed.
        The argument `x` must be a real floating-point number (or
        possible to convert into one) and `n` must be a Python ``int``.

            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = False
            >>> ldexp(1, 10)
            mpf('1024.0')
            >>> ldexp(1, -3)
            mpf('0.125')

        """
    def frexp(ctx, x):
        """
        Given a real number `x`, returns `(y, n)` with `y \\in [0.5, 1)`,
        `n` a Python integer, and such that `x = y 2^n`. No rounding is
        performed.

            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = False
            >>> frexp(7.5)
            (mpf('0.9375'), 3)

        """
    def fneg(ctx, x, **kwargs):
        """
        Negates the number *x*, giving a floating-point result, optionally
        using a custom precision and rounding mode.

        See the documentation of :func:`~mpmath.fadd` for a detailed description
        of how to specify precision and rounding.

        **Examples**

        An mpmath number is returned::

            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = False
            >>> fneg(2.5)
            mpf('-2.5')
            >>> fneg(-5+2j)
            mpc(real='5.0', imag='-2.0')

        Precise control over rounding is possible::

            >>> x = fadd(2, 1e-100, exact=True)
            >>> fneg(x)
            mpf('-2.0')
            >>> fneg(x, rounding='f')
            mpf('-2.0000000000000004')

        Negating with and without roundoff::

            >>> n = 200000000000000000000001
            >>> print(int(-mpf(n)))
            -200000000000000016777216
            >>> print(int(fneg(n)))
            -200000000000000016777216
            >>> print(int(fneg(n, prec=log(n,2)+1)))
            -200000000000000000000001
            >>> print(int(fneg(n, dps=log(n,10)+1)))
            -200000000000000000000001
            >>> print(int(fneg(n, prec=inf)))
            -200000000000000000000001
            >>> print(int(fneg(n, dps=inf)))
            -200000000000000000000001
            >>> print(int(fneg(n, exact=True)))
            -200000000000000000000001

        """
    def fadd(ctx, x, y, **kwargs):
        """
        Adds the numbers *x* and *y*, giving a floating-point result,
        optionally using a custom precision and rounding mode.

        The default precision is the working precision of the context.
        You can specify a custom precision in bits by passing the *prec* keyword
        argument, or by providing an equivalent decimal precision with the *dps*
        keyword argument. If the precision is set to ``+inf``, or if the flag
        *exact=True* is passed, an exact addition with no rounding is performed.

        When the precision is finite, the optional *rounding* keyword argument
        specifies the direction of rounding. Valid options are ``'n'`` for
        nearest (default), ``'f'`` for floor, ``'c'`` for ceiling, ``'d'``
        for down, ``'u'`` for up.

        **Examples**

        Using :func:`~mpmath.fadd` with precision and rounding control::

            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = False
            >>> fadd(2, 1e-20)
            mpf('2.0')
            >>> fadd(2, 1e-20, rounding='u')
            mpf('2.0000000000000004')
            >>> nprint(fadd(2, 1e-20, prec=100), 25)
            2.00000000000000000001
            >>> nprint(fadd(2, 1e-20, dps=15), 25)
            2.0
            >>> nprint(fadd(2, 1e-20, dps=25), 25)
            2.00000000000000000001
            >>> nprint(fadd(2, 1e-20, exact=True), 25)
            2.00000000000000000001

        Exact addition avoids cancellation errors, enforcing familiar laws
        of numbers such as `x+y-x = y`, which don't hold in floating-point
        arithmetic with finite precision::

            >>> x, y = mpf(2), mpf('1e-1000')
            >>> print(x + y - x)
            0.0
            >>> print(fadd(x, y, prec=inf) - x)
            1.0e-1000
            >>> print(fadd(x, y, exact=True) - x)
            1.0e-1000

        Exact addition can be inefficient and may be impossible to perform
        with large magnitude differences::

            >>> fadd(1, '1e-100000000000000000000', prec=inf)
            Traceback (most recent call last):
              ...
            OverflowError: the exact result does not fit in memory

        """
    def fsub(ctx, x, y, **kwargs):
        """
        Subtracts the numbers *x* and *y*, giving a floating-point result,
        optionally using a custom precision and rounding mode.

        See the documentation of :func:`~mpmath.fadd` for a detailed description
        of how to specify precision and rounding.

        **Examples**

        Using :func:`~mpmath.fsub` with precision and rounding control::

            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = False
            >>> fsub(2, 1e-20)
            mpf('2.0')
            >>> fsub(2, 1e-20, rounding='d')
            mpf('1.9999999999999998')
            >>> nprint(fsub(2, 1e-20, prec=100), 25)
            1.99999999999999999999
            >>> nprint(fsub(2, 1e-20, dps=15), 25)
            2.0
            >>> nprint(fsub(2, 1e-20, dps=25), 25)
            1.99999999999999999999
            >>> nprint(fsub(2, 1e-20, exact=True), 25)
            1.99999999999999999999

        Exact subtraction avoids cancellation errors, enforcing familiar laws
        of numbers such as `x-y+y = x`, which don't hold in floating-point
        arithmetic with finite precision::

            >>> x, y = mpf(2), mpf('1e1000')
            >>> print(x - y + y)
            0.0
            >>> print(fsub(x, y, prec=inf) + y)
            2.0
            >>> print(fsub(x, y, exact=True) + y)
            2.0

        Exact addition can be inefficient and may be impossible to perform
        with large magnitude differences::

            >>> fsub(1, '1e-100000000000000000000', prec=inf)
            Traceback (most recent call last):
              ...
            OverflowError: the exact result does not fit in memory

        """
    def fmul(ctx, x, y, **kwargs):
        """
        Multiplies the numbers *x* and *y*, giving a floating-point result,
        optionally using a custom precision and rounding mode.

        See the documentation of :func:`~mpmath.fadd` for a detailed description
        of how to specify precision and rounding.

        **Examples**

        The result is an mpmath number::

            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = False
            >>> fmul(2, 5.0)
            mpf('10.0')
            >>> fmul(0.5j, 0.5)
            mpc(real='0.0', imag='0.25')

        Avoiding roundoff::

            >>> x, y = 10**10+1, 10**15+1
            >>> print(x*y)
            10000000001000010000000001
            >>> print(mpf(x) * mpf(y))
            1.0000000001e+25
            >>> print(int(mpf(x) * mpf(y)))
            10000000001000011026399232
            >>> print(int(fmul(x, y)))
            10000000001000011026399232
            >>> print(int(fmul(x, y, dps=25)))
            10000000001000010000000001
            >>> print(int(fmul(x, y, exact=True)))
            10000000001000010000000001

        Exact multiplication with complex numbers can be inefficient and may
        be impossible to perform with large magnitude differences between
        real and imaginary parts::

            >>> x = 1+2j
            >>> y = mpc(2, '1e-100000000000000000000')
            >>> fmul(x, y)
            mpc(real='2.0', imag='4.0')
            >>> fmul(x, y, rounding='u')
            mpc(real='2.0', imag='4.0000000000000009')
            >>> fmul(x, y, exact=True)
            Traceback (most recent call last):
              ...
            OverflowError: the exact result does not fit in memory

        """
    def fdiv(ctx, x, y, **kwargs):
        """
        Divides the numbers *x* and *y*, giving a floating-point result,
        optionally using a custom precision and rounding mode.

        See the documentation of :func:`~mpmath.fadd` for a detailed description
        of how to specify precision and rounding.

        **Examples**

        The result is an mpmath number::

            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = False
            >>> fdiv(3, 2)
            mpf('1.5')
            >>> fdiv(2, 3)
            mpf('0.66666666666666663')
            >>> fdiv(2+4j, 0.5)
            mpc(real='4.0', imag='8.0')

        The rounding direction and precision can be controlled::

            >>> fdiv(2, 3, dps=3)    # Should be accurate to at least 3 digits
            mpf('0.6666259765625')
            >>> fdiv(2, 3, rounding='d')
            mpf('0.66666666666666663')
            >>> fdiv(2, 3, prec=60)
            mpf('0.66666666666666667')
            >>> fdiv(2, 3, rounding='u')
            mpf('0.66666666666666674')

        Checking the error of a division by performing it at higher precision::

            >>> fdiv(2, 3) - fdiv(2, 3, prec=100)
            mpf('-3.7007434154172148e-17')

        Unlike :func:`~mpmath.fadd`, :func:`~mpmath.fmul`, etc., exact division is not
        allowed since the quotient of two floating-point numbers generally
        does not have an exact floating-point representation. (In the
        future this might be changed to allow the case where the division
        is actually exact.)

            >>> fdiv(2, 3, exact=True)
            Traceback (most recent call last):
              ...
            ValueError: division is not an exact operation

        """
    def nint_distance(ctx, x):
        """
        Return `(n,d)` where `n` is the nearest integer to `x` and `d` is
        an estimate of `\\log_2(|x-n|)`. If `d < 0`, `-d` gives the precision
        (measured in bits) lost to cancellation when computing `x-n`.

            >>> from mpmath import *
            >>> n, d = nint_distance(5)
            >>> print(n); print(d)
            5
            -inf
            >>> n, d = nint_distance(mpf(5))
            >>> print(n); print(d)
            5
            -inf
            >>> n, d = nint_distance(mpf(5.00000001))
            >>> print(n); print(d)
            5
            -26
            >>> n, d = nint_distance(mpf(4.99999999))
            >>> print(n); print(d)
            5
            -26
            >>> n, d = nint_distance(mpc(5,10))
            >>> print(n); print(d)
            5
            4
            >>> n, d = nint_distance(mpc(5,0.000001))
            >>> print(n); print(d)
            5
            -19

        """
    def fprod(ctx, factors):
        """
        Calculates a product containing a finite number of factors (for
        infinite products, see :func:`~mpmath.nprod`). The factors will be
        converted to mpmath numbers.

            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = False
            >>> fprod([1, 2, 0.5, 7])
            mpf('7.0')

        """
    def rand(ctx):
        """
        Returns an ``mpf`` with value chosen randomly from `[0, 1)`.
        The number of randomly generated bits in the mantissa is equal
        to the working precision.
        """
    def fraction(ctx, p, q):
        """
        Given Python integers `(p, q)`, returns a lazy ``mpf`` representing
        the fraction `p/q`. The value is updated with the precision.

            >>> from mpmath import *
            >>> mp.dps = 15
            >>> a = fraction(1,100)
            >>> b = mpf(1)/100
            >>> print(a); print(b)
            0.01
            0.01
            >>> mp.dps = 30
            >>> print(a); print(b)      # a will be accurate
            0.01
            0.0100000000000000002081668171172
            >>> mp.dps = 15
        """
    def absmin(ctx, x): ...
    def absmax(ctx, x): ...

class PrecisionManager:
    ctx: Incomplete
    precfun: Incomplete
    dpsfun: Incomplete
    normalize_output: Incomplete
    def __init__(self, ctx, precfun, dpsfun, normalize_output: bool = False) -> None: ...
    def __call__(self, f): ...
    origp: Incomplete
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None): ...
