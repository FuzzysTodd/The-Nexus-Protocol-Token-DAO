from .backend import MPZ as MPZ, MPZ_ONE as MPZ_ONE, MPZ_THREE as MPZ_THREE, MPZ_ZERO as MPZ_ZERO, gmpy as gmpy, xrange as xrange
from .libelefun import constant_memo as constant_memo, cos_sin_fixed as cos_sin_fixed, def_mpf_constant as def_mpf_constant, exp_fixed as exp_fixed, ln2_fixed as ln2_fixed, ln_sqrt2pi_fixed as ln_sqrt2pi_fixed, log_int_fixed as log_int_fixed, mpf_cos_pi as mpf_cos_pi, mpf_cos_sin as mpf_cos_sin, mpf_cos_sin_pi as mpf_cos_sin_pi, mpf_cosh as mpf_cosh, mpf_cosh_sinh as mpf_cosh_sinh, mpf_exp as mpf_exp, mpf_ln2 as mpf_ln2, mpf_ln_sqrt2pi as mpf_ln_sqrt2pi, mpf_log as mpf_log, mpf_pi as mpf_pi, mpf_pow as mpf_pow, mpf_sin_pi as mpf_sin_pi, mpf_sqrtpi as mpf_sqrtpi, pi_fixed as pi_fixed, sqrtpi_fixed as sqrtpi_fixed
from .libintmath import ifac as ifac, ifac2 as ifac2, list_primes as list_primes, moebius as moebius
from .libmpc import mpc_abs as mpc_abs, mpc_add as mpc_add, mpc_add_mpf as mpc_add_mpf, mpc_cos_pi as mpc_cos_pi, mpc_div as mpc_div, mpc_div_mpf as mpc_div_mpf, mpc_exp as mpc_exp, mpc_half as mpc_half, mpc_log as mpc_log, mpc_mpf_div as mpc_mpf_div, mpc_mul as mpc_mul, mpc_mul_int as mpc_mul_int, mpc_mul_mpf as mpc_mul_mpf, mpc_neg as mpc_neg, mpc_one as mpc_one, mpc_pos as mpc_pos, mpc_pow as mpc_pow, mpc_pow_int as mpc_pow_int, mpc_reciprocal as mpc_reciprocal, mpc_shift as mpc_shift, mpc_sin_pi as mpc_sin_pi, mpc_square as mpc_square, mpc_sub as mpc_sub, mpc_sub_mpf as mpc_sub_mpf, mpc_two as mpc_two, mpc_zero as mpc_zero
from .libmpf import ComplexResult as ComplexResult, bitcount as bitcount, fhalf as fhalf, finf as finf, fnan as fnan, fninf as fninf, fnone as fnone, fone as fone, from_int as from_int, from_man_exp as from_man_exp, from_rational as from_rational, ftwo as ftwo, fzero as fzero, isqrt_fast as isqrt_fast, lshift as lshift, mpf_abs as mpf_abs, mpf_add as mpf_add, mpf_div as mpf_div, mpf_floor as mpf_floor, mpf_gt as mpf_gt, mpf_le as mpf_le, mpf_lt as mpf_lt, mpf_mul as mpf_mul, mpf_mul_int as mpf_mul_int, mpf_neg as mpf_neg, mpf_perturb as mpf_perturb, mpf_pos as mpf_pos, mpf_pow_int as mpf_pow_int, mpf_rdiv_int as mpf_rdiv_int, mpf_shift as mpf_shift, mpf_sign as mpf_sign, mpf_sqrt as mpf_sqrt, mpf_sub as mpf_sub, negative_rnd as negative_rnd, reciprocal_rnd as reciprocal_rnd, round_ceiling as round_ceiling, round_down as round_down, round_fast as round_fast, round_floor as round_floor, round_nearest as round_nearest, round_up as round_up, sqrt_fixed as sqrt_fixed, to_fixed as to_fixed, to_float as to_float, to_int as to_int
from _typeshed import Incomplete

def catalan_fixed(prec): ...
def khinchin_fixed(prec): ...
def glaisher_fixed(prec): ...
def apery_fixed(prec): ...
def euler_fixed(prec): ...
def mertens_fixed(prec): ...
def twinprime_fixed(prec): ...

mpf_euler: Incomplete
mpf_apery: Incomplete
mpf_khinchin: Incomplete
mpf_glaisher: Incomplete
mpf_catalan: Incomplete
mpf_mertens: Incomplete
mpf_twinprime: Incomplete
MAX_BERNOULLI_CACHE: int
bernoulli_cache: Incomplete
f3: Incomplete
f6: Incomplete

def bernoulli_size(n):
    """Accurately estimate the size of B_n (even n > 2 only)"""

BERNOULLI_PREC_CUTOFF: Incomplete

def mpf_bernoulli(n, prec, rnd: Incomplete | None = None):
    """Computation of Bernoulli numbers (numerically)"""
def mpf_bernoulli_huge(n, prec, rnd: Incomplete | None = None): ...
def bernfrac(n):
    '''
    Returns a tuple of integers `(p, q)` such that `p/q = B_n` exactly,
    where `B_n` denotes the `n`-th Bernoulli number. The fraction is
    always reduced to lowest terms. Note that for `n > 1` and `n` odd,
    `B_n = 0`, and `(0, 1)` is returned.

    **Examples**

    The first few Bernoulli numbers are exactly::

        >>> from mpmath import *
        >>> for n in range(15):
        ...     p, q = bernfrac(n)
        ...     print("%s %s/%s" % (n, p, q))
        ...
        0 1/1
        1 -1/2
        2 1/6
        3 0/1
        4 -1/30
        5 0/1
        6 1/42
        7 0/1
        8 -1/30
        9 0/1
        10 5/66
        11 0/1
        12 -691/2730
        13 0/1
        14 7/6

    This function works for arbitrarily large `n`::

        >>> p, q = bernfrac(10**4)
        >>> print(q)
        2338224387510
        >>> print(len(str(p)))
        27692
        >>> mp.dps = 15
        >>> print(mpf(p) / q)
        -9.04942396360948e+27677
        >>> print(bernoulli(10**4))
        -9.04942396360948e+27677

    .. note ::

        :func:`~mpmath.bernoulli` computes a floating-point approximation
        directly, without computing the exact fraction first.
        This is much faster for large `n`.

    **Algorithm**

    :func:`~mpmath.bernfrac` works by computing the value of `B_n` numerically
    and then using the von Staudt-Clausen theorem [1] to reconstruct
    the exact fraction. For large `n`, this is significantly faster than
    computing `B_1, B_2, \\ldots, B_2` recursively with exact arithmetic.
    The implementation has been tested for `n = 10^m` up to `m = 6`.

    In practice, :func:`~mpmath.bernfrac` appears to be about three times
    slower than the specialized program calcbn.exe [2]

    **References**

    1. MathWorld, von Staudt-Clausen Theorem:
       http://mathworld.wolfram.com/vonStaudt-ClausenTheorem.html

    2. The Bernoulli Number Page:
       http://www.bernoulli.org/

    '''
def mpf_harmonic(x, prec, rnd): ...
def mpc_harmonic(z, prec, rnd): ...
def mpf_psi0(x, prec, rnd=...):
    """
    Computation of the digamma function (psi function of order 0)
    of a real argument.
    """
def mpc_psi0(z, prec, rnd=...):
    """
    Computation of the digamma function (psi function of order 0)
    of a complex argument.
    """
def mpf_psi(m, x, prec, rnd=...):
    """
    Computation of the polygamma function of arbitrary integer order
    m >= 0, for a real argument x.
    """
def mpc_psi(m, z, prec, rnd=...):
    """
    Computation of the polygamma function of arbitrary integer order
    m >= 0, for a complex argument z.
    """

borwein_cache: Incomplete

def borwein_coefficients(n): ...

ZETA_INT_CACHE_MAX_PREC: int
zeta_int_cache: Incomplete

def mpf_zeta_int(s, prec, rnd=...):
    """
    Optimized computation of zeta(s) for an integer s.
    """
def mpf_zeta(s, prec, rnd=..., alt: int = 0): ...
def mpc_zeta(s, prec, rnd=..., alt: int = 0, force: bool = False): ...
def mpf_altzeta(s, prec, rnd=...): ...
def mpc_altzeta(s, prec, rnd=...): ...

mpf_zetasum: Incomplete

def pow_fixed(x, n, wp): ...

sieve_cache: Incomplete
primes_cache: Incomplete
mult_cache: Incomplete

def primesieve(n): ...
def zetasum_sieved(critical_line, sre, sim, a, n, wp): ...

ZETASUM_SIEVE_CUTOFF: int

def mpc_zetasum(s, a, n, derivatives, reflect, prec):
    """
    Fast version of mp._zetasum, assuming s = complex, a = integer.
    """

MAX_GAMMA_TAYLOR_PREC: int
GAMMA_STIRLING_BETA: float
SMALL_FACTORIAL_CACHE_SIZE: int
gamma_taylor_cache: Incomplete
gamma_stirling_cache: Incomplete
small_factorial_cache: Incomplete

def zeta_array(N, prec):
    """
    zeta(n) = A * pi**n / n! + B

    where A is a rational number (A = Bernoulli number
    for n even) and B is an infinite sum over powers of exp(2*pi).
    (B = 0 for n even).

    TODO: this is currently only used for gamma, but could
    be very useful elsewhere.
    """
def gamma_taylor_coefficients(inprec):
    """
    Gives the Taylor coefficients of 1/gamma(1+x) as
    a list of fixed-point numbers. Enough coefficients are returned
    to ensure that the series converges to the given precision
    when x is in [0.5, 1.5].
    """
def gamma_fixed_taylor(xmpf, x, wp, prec, rnd, type): ...
def stirling_coefficient(n): ...
def real_stirling_series(x, prec):
    """
    Sums the rational part of Stirling's expansion,

    log(sqrt(2*pi)) - z + 1/(12*z) - 1/(360*z^3) + ...

    """
def complex_stirling_series(x, y, prec): ...
def mpf_gamma(x, prec, rnd: str = 'd', type: int = 0):
    """
    This function implements multipurpose evaluation of the gamma
    function, G(x), as well as the following versions of the same:

    type = 0 -- G(x)                    [standard gamma function]
    type = 1 -- G(x+1) = x*G(x+1) = x!  [factorial]
    type = 2 -- 1/G(x)                  [reciprocal gamma function]
    type = 3 -- log(|G(x)|)             [log-gamma function, real part]
    """
def mpc_gamma(z, prec, rnd: str = 'd', type: int = 0): ...
def mpf_factorial(x, prec, rnd: str = 'd'): ...
def mpc_factorial(x, prec, rnd: str = 'd'): ...
def mpf_rgamma(x, prec, rnd: str = 'd'): ...
def mpc_rgamma(x, prec, rnd: str = 'd'): ...
def mpf_loggamma(x, prec, rnd: str = 'd'): ...
def mpc_loggamma(z, prec, rnd: str = 'd'): ...
def mpf_gamma_int(n, prec, rnd=...): ...
