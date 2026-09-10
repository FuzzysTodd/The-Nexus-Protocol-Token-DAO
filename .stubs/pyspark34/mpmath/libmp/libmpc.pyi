from .backend import BACKEND as BACKEND, MPZ as MPZ, MPZ_ONE as MPZ_ONE, MPZ_TWO as MPZ_TWO, MPZ_ZERO as MPZ_ZERO
from .libelefun import mpf_acos as mpf_acos, mpf_acosh as mpf_acosh, mpf_asin as mpf_asin, mpf_atan as mpf_atan, mpf_atan2 as mpf_atan2, mpf_cos as mpf_cos, mpf_cos_pi as mpf_cos_pi, mpf_cos_sin as mpf_cos_sin, mpf_cos_sin_pi as mpf_cos_sin_pi, mpf_cosh as mpf_cosh, mpf_cosh_sinh as mpf_cosh_sinh, mpf_exp as mpf_exp, mpf_fibonacci as mpf_fibonacci, mpf_log as mpf_log, mpf_log_hypot as mpf_log_hypot, mpf_nthroot as mpf_nthroot, mpf_phi as mpf_phi, mpf_pi as mpf_pi, mpf_pow_int as mpf_pow_int, mpf_sin as mpf_sin, mpf_sin_pi as mpf_sin_pi, mpf_sinh as mpf_sinh, mpf_tan as mpf_tan, mpf_tanh as mpf_tanh
from .libmpf import ComplexResult as ComplexResult, bctable as bctable, bitcount as bitcount, fhalf as fhalf, finf as finf, fnan as fnan, fninf as fninf, fnone as fnone, fone as fone, from_float as from_float, from_int as from_int, from_man_exp as from_man_exp, ftwo as ftwo, fzero as fzero, giant_steps as giant_steps, lshift as lshift, mpf_abs as mpf_abs, mpf_add as mpf_add, mpf_ceil as mpf_ceil, mpf_div as mpf_div, mpf_floor as mpf_floor, mpf_frac as mpf_frac, mpf_hash as mpf_hash, mpf_hypot as mpf_hypot, mpf_mul as mpf_mul, mpf_mul_int as mpf_mul_int, mpf_neg as mpf_neg, mpf_nint as mpf_nint, mpf_pos as mpf_pos, mpf_rdiv_int as mpf_rdiv_int, mpf_shift as mpf_shift, mpf_sign as mpf_sign, mpf_sqrt as mpf_sqrt, mpf_sub as mpf_sub, negative_rnd as negative_rnd, normalize as normalize, normalize1 as normalize1, reciprocal_rnd as reciprocal_rnd, round_ceiling as round_ceiling, round_down as round_down, round_fast as round_fast, round_floor as round_floor, round_nearest as round_nearest, round_up as round_up, rshift as rshift, to_fixed as to_fixed, to_float as to_float, to_int as to_int, to_str as to_str
from _typeshed import Incomplete

mpc_one: Incomplete
mpc_zero: Incomplete
mpc_two: Incomplete
mpc_half: Incomplete

def mpc_is_inf(z):
    """Check if either real or imaginary part is infinite"""
def mpc_is_infnan(z):
    """Check if either real or imaginary part is infinite or nan"""
def mpc_to_str(z, dps, **kwargs): ...
def mpc_to_complex(z, strict: bool = False, rnd=...): ...
def mpc_hash(z): ...
def mpc_conjugate(z, prec, rnd=...): ...
def mpc_is_nonzero(z): ...
def mpc_add(z, w, prec, rnd=...): ...
def mpc_add_mpf(z, x, prec, rnd=...): ...
def mpc_sub(z, w, prec: int = 0, rnd=...): ...
def mpc_sub_mpf(z, p, prec: int = 0, rnd=...): ...
def mpc_pos(z, prec, rnd=...): ...
def mpc_neg(z, prec: Incomplete | None = None, rnd=...): ...
def mpc_shift(z, n): ...
def mpc_abs(z, prec, rnd=...):
    """Absolute value of a complex number, |a+bi|.
    Returns an mpf value."""
def mpc_arg(z, prec, rnd=...):
    """Argument of a complex number. Returns an mpf value."""
def mpc_floor(z, prec, rnd=...): ...
def mpc_ceil(z, prec, rnd=...): ...
def mpc_nint(z, prec, rnd=...): ...
def mpc_frac(z, prec, rnd=...): ...
def mpc_mul(z, w, prec, rnd=...):
    """
    Complex multiplication.

    Returns the real and imaginary part of (a+bi)*(c+di), rounded to
    the specified precision. The rounding mode applies to the real and
    imaginary parts separately.
    """
def mpc_square(z, prec, rnd=...): ...
def mpc_mul_mpf(z, p, prec, rnd=...): ...
def mpc_mul_imag_mpf(z, x, prec, rnd=...):
    """
    Multiply the mpc value z by I*x where x is an mpf value.
    """
def mpc_mul_int(z, n, prec, rnd=...): ...
def mpc_div(z, w, prec, rnd=...): ...
def mpc_div_mpf(z, p, prec, rnd=...):
    """Calculate z/p where p is real"""
def mpc_reciprocal(z, prec, rnd=...):
    """Calculate 1/z efficiently"""
def mpc_mpf_div(p, z, prec, rnd=...):
    """Calculate p/z where p is real efficiently"""
def complex_int_pow(a, b, n):
    """Complex integer power: computes (a+b*I)**n exactly for
    nonnegative n (a and b must be Python ints)."""
def mpc_pow(z, w, prec, rnd=...): ...
def mpc_pow_mpf(z, p, prec, rnd=...): ...
def mpc_pow_int(z, n, prec, rnd=...): ...
def mpc_sqrt(z, prec, rnd=...):
    """Complex square root (principal branch).

    We have sqrt(a+bi) = sqrt((r+a)/2) + b/sqrt(2*(r+a))*i where
    r = abs(a+bi), when a+bi is not a negative real number."""
def mpc_nthroot_fixed(a, b, n, prec): ...
def mpc_nthroot(z, n, prec, rnd=...):
    """
    Complex n-th root.

    Use Newton method as in the real case when it is faster,
    otherwise use z**(1/n)
    """
def mpc_cbrt(z, prec, rnd=...):
    """
    Complex cubic root.
    """
def mpc_exp(z, prec, rnd=...):
    """
    Complex exponential function.

    We use the direct formula exp(a+bi) = exp(a) * (cos(b) + sin(b)*i)
    for the computation. This formula is very nice because it is
    pefectly stable; since we just do real multiplications, the only
    numerical errors that can creep in are single-ulp rounding errors.

    The formula is efficient since mpmath's real exp is quite fast and
    since we can compute cos and sin simultaneously.

    It is no problem if a and b are large; if the implementations of
    exp/cos/sin are accurate and efficient for all real numbers, then
    so is this function for all complex numbers.
    """
def mpc_log(z, prec, rnd=...): ...
def mpc_cos(z, prec, rnd=...):
    """Complex cosine. The formula used is cos(a+bi) = cos(a)*cosh(b) -
    sin(a)*sinh(b)*i.

    The same comments apply as for the complex exp: only real
    multiplications are pewrormed, so no cancellation errors are
    possible. The formula is also efficient since we can compute both
    pairs (cos, sin) and (cosh, sinh) in single stwps."""
def mpc_sin(z, prec, rnd=...):
    """Complex sine. We have sin(a+bi) = sin(a)*cosh(b) +
    cos(a)*sinh(b)*i. See the docstring for mpc_cos for additional
    comments."""
def mpc_tan(z, prec, rnd=...):
    """Complex tangent. Computed as tan(a+bi) = sin(2a)/M + sinh(2b)/M*i
    where M = cos(2a) + cosh(2b)."""
def mpc_cos_pi(z, prec, rnd=...): ...
def mpc_sin_pi(z, prec, rnd=...): ...
def mpc_cos_sin(z, prec, rnd=...): ...
def mpc_cos_sin_pi(z, prec, rnd=...): ...
def mpc_cosh(z, prec, rnd=...):
    """Complex hyperbolic cosine. Computed as cosh(z) = cos(z*i)."""
def mpc_sinh(z, prec, rnd=...):
    """Complex hyperbolic sine. Computed as sinh(z) = -i*sin(z*i)."""
def mpc_tanh(z, prec, rnd=...):
    """Complex hyperbolic tangent. Computed as tanh(z) = -i*tan(z*i)."""
def mpc_atan(z, prec, rnd=...): ...

beta_crossover: Incomplete
alpha_crossover: Incomplete

def acos_asin(z, prec, rnd, n):
    """ complex acos for n = 0, asin for n = 1
    The algorithm is described in
    T.E. Hull, T.F. Fairgrieve and P.T.P. Tang
    'Implementing the Complex Arcsine and Arcosine Functions
    using Exception Handling',
    ACM Trans. on Math. Software Vol. 23 (1997), p299
    The complex acos and asin can be defined as
    acos(z) = acos(beta) - I*sign(a)* log(alpha + sqrt(alpha**2 -1))
    asin(z) = asin(beta) + I*sign(a)* log(alpha + sqrt(alpha**2 -1))
    where z = a + I*b
    alpha = (1/2)*(r + s); beta = (1/2)*(r - s) = a/alpha
    r = sqrt((a+1)**2 + y**2); s = sqrt((a-1)**2 + y**2)
    These expressions are rewritten in different ways in different
    regions, delimited by two crossovers alpha_crossover and beta_crossover,
    and by abs(a) <= 1, in order to improve the numerical accuracy.
    """
def mpc_acos(z, prec, rnd=...): ...
def mpc_asin(z, prec, rnd=...): ...
def mpc_asinh(z, prec, rnd=...): ...
def mpc_acosh(z, prec, rnd=...): ...
def mpc_atanh(z, prec, rnd=...): ...
def mpc_fibonacci(z, prec, rnd=...): ...
def mpf_expj(x, prec, rnd: str = 'f') -> None: ...
def mpc_expj(z, prec, rnd: str = 'f'): ...
def mpf_expjpi(x, prec, rnd: str = 'f') -> None: ...
def mpc_expjpi(z, prec, rnd: str = 'f'): ...

mpc_exp: Incomplete
mpc_sqrt: Incomplete
