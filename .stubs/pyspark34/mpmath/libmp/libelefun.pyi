from .backend import BACKEND as BACKEND, MPZ as MPZ, MPZ_FIVE as MPZ_FIVE, MPZ_ONE as MPZ_ONE, MPZ_TWO as MPZ_TWO, MPZ_ZERO as MPZ_ZERO, xrange as xrange
from .libintmath import ifib as ifib
from .libmpf import ComplexResult as ComplexResult, bctable as bctable, bitcount as bitcount, fhalf as fhalf, finf as finf, fnan as fnan, fninf as fninf, fnone as fnone, fone as fone, from_float as from_float, from_int as from_int, from_man_exp as from_man_exp, from_rational as from_rational, fzero as fzero, giant_steps as giant_steps, isqrt_fast as isqrt_fast, lshift as lshift, mpf_abs as mpf_abs, mpf_add as mpf_add, mpf_cmp as mpf_cmp, mpf_div as mpf_div, mpf_mul as mpf_mul, mpf_neg as mpf_neg, mpf_perturb as mpf_perturb, mpf_pos as mpf_pos, mpf_pow_int as mpf_pow_int, mpf_rdiv_int as mpf_rdiv_int, mpf_shift as mpf_shift, mpf_sign as mpf_sign, mpf_sqrt as mpf_sqrt, mpf_sub as mpf_sub, negative_rnd as negative_rnd, normalize as normalize, reciprocal_rnd as reciprocal_rnd, round_ceiling as round_ceiling, round_down as round_down, round_fast as round_fast, round_floor as round_floor, round_nearest as round_nearest, round_up as round_up, rshift as rshift, sqrt_fixed as sqrt_fixed, to_fixed as to_fixed, to_float as to_float, to_int as to_int
from _typeshed import Incomplete
from bisect import bisect as bisect

EXP_COSH_CUTOFF: int
EXP_SERIES_U_CUTOFF: int
COS_SIN_CACHE_PREC: int
COS_SIN_CACHE_STEP: int
cos_sin_cache: Incomplete
MAX_LOG_INT_CACHE: int
log_int_cache: Incomplete
LOG_TAYLOR_PREC: int
LOG_TAYLOR_SHIFT: int
log_taylor_cache: Incomplete
LOG_AGM_MAG_PREC_RATIO: int
ATAN_TAYLOR_PREC: int
ATAN_TAYLOR_SHIFT: int
atan_taylor_cache: Incomplete
cache_prec_steps: Incomplete

def constant_memo(f):
    """
    Decorator for caching computed values of mathematical
    constants. This decorator should be applied to a
    function taking a single argument prec as input and
    returning a fixed-point value with the given precision.
    """
def def_mpf_constant(fixed):
    """
    Create a function that computes the mpf value for a mathematical
    constant, given a function that computes the fixed-point value.

    Assumptions: the constant is positive and has magnitude ~= 1;
    the fixed-point function rounds to floor.
    """
def bsp_acot(q, a, b, hyperbolic): ...
def acot_fixed(a, prec, hyperbolic):
    """
    Compute acot(a) or acoth(a) for an integer a with binary splitting; see
    http://numbers.computation.free.fr/Constants/Algorithms/splitting.html
    """
def machin(coefs, prec, hyperbolic: bool = False):
    """
    Evaluate a Machin-like formula, i.e., a linear combination of
    acot(n) or acoth(n) for specific integer values of n, using fixed-
    point arithmetic. The input should be a list [(c, n), ...], giving
    c*acot[h](n) + ...
    """
def ln2_fixed(prec):
    """
    Computes ln(2). This is done with a hyperbolic Machin-type formula,
    with binary splitting at high precision.
    """
def ln10_fixed(prec):
    """
    Computes ln(10). This is done with a hyperbolic Machin-type formula.
    """

CHUD_A: Incomplete
CHUD_B: Incomplete
CHUD_C: Incomplete
CHUD_D: Incomplete

def bs_chudnovsky(a, b, level, verbose):
    """
    Computes the sum from a to b of the series in the Chudnovsky
    formula. Returns g, p, q where p/q is the sum as an exact
    fraction and g is a temporary value used to save work
    for recursive calls.
    """
def pi_fixed(prec, verbose: bool = False, verbose_base: Incomplete | None = None):
    """
    Compute floor(pi * 2**prec) as a big integer.

    This is done using Chudnovsky's series (see comments in
    libelefun.py for details).
    """
def degree_fixed(prec): ...
def bspe(a, b):
    """
    Sum series for exp(1)-1 between a, b, returning the result
    as an exact fraction (p, q).
    """
def e_fixed(prec):
    """
    Computes exp(1). This is done using the ordinary Taylor series for
    exp, with binary splitting. For a description of the algorithm,
    see:

        http://numbers.computation.free.fr/Constants/
            Algorithms/splitting.html
    """
def phi_fixed(prec):
    """
    Computes the golden ratio, (1+sqrt(5))/2
    """

mpf_phi: Incomplete
mpf_pi: Incomplete
mpf_e: Incomplete
mpf_degree: Incomplete
mpf_ln2: Incomplete
mpf_ln10: Incomplete

def ln_sqrt2pi_fixed(prec): ...
def sqrtpi_fixed(prec): ...

mpf_sqrtpi: Incomplete
mpf_ln_sqrt2pi: Incomplete

def mpf_pow(s, t, prec, rnd=...):
    """
    Compute s**t. Raises ComplexResult if s is negative and t is
    fractional.
    """
def int_pow_fixed(y, n, prec):
    """n-th power of a fixed point number with precision prec

       Returns the power in the form man, exp,
       man * 2**exp ~= y**n
    """
def nthroot_fixed(y, n, prec, exp1): ...
def mpf_nthroot(s, n, prec, rnd=...):
    """nth-root of a positive number

    Use the Newton method when faster, otherwise use x**(1/n)
    """
def mpf_cbrt(s, prec, rnd=...):
    """cubic root of a positive number"""
def log_int_fixed(n, prec, ln2: Incomplete | None = None):
    """
    Fast computation of log(n), caching the value for small n,
    intended for zeta sums.
    """
def agm_fixed(a, b, prec):
    """
    Fixed-point computation of agm(a,b), assuming
    a, b both close to unit magnitude.
    """
def log_agm(x, prec):
    '''
    Fixed-point computation of -log(x) = log(1/x), suitable
    for large precision. It is required that 0 < x < 1. The
    algorithm used is the Sasaki-Kanada formula

        -log(x) = pi/agm(theta2(x)^2,theta3(x)^2). [1]

    For faster convergence in the theta functions, x should
    be chosen closer to 0.

    Guard bits must be added by the caller.

    HYPOTHESIS: if x = 2^(-n), n bits need to be added to
    account for the truncation to a fixed-point number,
    and this is the only significant cancellation error.

    The number of bits lost to roundoff is small and can be
    considered constant.

    [1] Richard P. Brent, "Fast Algorithms for High-Precision
        Computation of Elementary Functions (extended abstract)",
        http://wwwmaths.anu.edu.au/~brent/pd/RNC7-Brent.pdf

    '''
def log_taylor(x, prec, r: int = 0):
    """
    Fixed-point calculation of log(x). It is assumed that x is close
    enough to 1 for the Taylor series to converge quickly. Convergence
    can be improved by specifying r > 0 to compute
    log(x^(1/2^r))*2^r, at the cost of performing r square roots.

    The caller must provide sufficient guard bits.
    """
def log_taylor_cached(x, prec):
    """
    Fixed-point computation of log(x), assuming x in (0.5, 2)
    and prec <= LOG_TAYLOR_PREC.
    """
def mpf_log(x, prec, rnd=...):
    """
    Compute the natural logarithm of the mpf value x. If x is negative,
    ComplexResult is raised.
    """
def mpf_log_hypot(a, b, prec, rnd):
    """
    Computes log(sqrt(a^2+b^2)) accurately.
    """
def atan_newton(x, prec): ...
def atan_taylor_get_cached(n, prec): ...
def atan_taylor(x, prec): ...
def atan_inf(sign, prec, rnd): ...
def mpf_atan(x, prec, rnd=...): ...
def mpf_atan2(y, x, prec, rnd=...): ...
def mpf_asin(x, prec, rnd=...): ...
def mpf_acos(x, prec, rnd=...): ...
def mpf_asinh(x, prec, rnd=...): ...
def mpf_acosh(x, prec, rnd=...): ...
def mpf_atanh(x, prec, rnd=...): ...
def mpf_fibonacci(x, prec, rnd=...): ...
def exponential_series(x, prec, type: int = 0):
    """
    Taylor series for cosh/sinh or cos/sin.

    type = 0 -- returns exp(x)  (slightly faster than cosh+sinh)
    type = 1 -- returns (cosh(x), sinh(x))
    type = 2 -- returns (cos(x), sin(x))
    """
def exp_basecase(x, prec):
    """
    Compute exp(x) as a fixed-point number. Works for any x,
    but for speed should have |x| < 1. For an arbitrary number,
    use exp(x) = exp(x-m*log(2)) * 2^m where m = floor(x/log(2)).
    """
def exp_expneg_basecase(x, prec):
    """
    Computation of exp(x), exp(-x)
    """
def cos_sin_basecase(x, prec):
    """
    Compute cos(x), sin(x) as fixed-point numbers, assuming x
    in [0, pi/2). For an arbitrary number, use x' = x - m*(pi/2)
    where m = floor(x/(pi/2)) along with quarter-period symmetries.
    """
def mpf_exp(x, prec, rnd=...): ...
def mpf_cosh_sinh(x, prec, rnd=..., tanh: int = 0):
    """Simultaneously compute (cosh(x), sinh(x)) for real x"""
def mod_pi2(man, exp, mag, wp): ...
def mpf_cos_sin(x, prec, rnd=..., which: int = 0, pi: bool = False):
    """
    which:
    0 -- return cos(x), sin(x)
    1 -- return cos(x)
    2 -- return sin(x)
    3 -- return tan(x)

    if pi=True, compute for pi*x
    """
def mpf_cos(x, prec, rnd=...): ...
def mpf_sin(x, prec, rnd=...): ...
def mpf_tan(x, prec, rnd=...): ...
def mpf_cos_sin_pi(x, prec, rnd=...): ...
def mpf_cos_pi(x, prec, rnd=...): ...
def mpf_sin_pi(x, prec, rnd=...): ...
def mpf_cosh(x, prec, rnd=...): ...
def mpf_sinh(x, prec, rnd=...): ...
def mpf_tanh(x, prec, rnd=...): ...
def cos_sin_fixed(x, prec, pi2: Incomplete | None = None): ...
def exp_fixed(x, prec, ln2: Incomplete | None = None): ...

mpf_exp: Incomplete
mpf_log: Incomplete
mpf_cos: Incomplete
mpf_sin: Incomplete
mpf_pow: Incomplete
exp_fixed: Incomplete
cos_sin_fixed: Incomplete
log_int_fixed: Incomplete
