from .backend import BACKEND as BACKEND, MPZ_ONE as MPZ_ONE, MPZ_ZERO as MPZ_ZERO, exec_ as exec_, xrange as xrange
from .gammazeta import euler_fixed as euler_fixed, mpf_euler as mpf_euler, mpf_gamma_int as mpf_gamma_int
from .libelefun import agm_fixed as agm_fixed, mpf_cos as mpf_cos, mpf_cos_sin as mpf_cos_sin, mpf_exp as mpf_exp, mpf_log as mpf_log, mpf_pi as mpf_pi, mpf_sin as mpf_sin, mpf_sqrt as mpf_sqrt, pi_fixed as pi_fixed
from .libintmath import gcd as gcd, ifac as ifac
from .libmpc import complex_int_pow as complex_int_pow, mpc_abs as mpc_abs, mpc_add as mpc_add, mpc_add_mpf as mpc_add_mpf, mpc_div as mpc_div, mpc_exp as mpc_exp, mpc_is_infnan as mpc_is_infnan, mpc_log as mpc_log, mpc_mpf_div as mpc_mpf_div, mpc_mul as mpc_mul, mpc_mul_mpf as mpc_mul_mpf, mpc_neg as mpc_neg, mpc_one as mpc_one, mpc_pos as mpc_pos, mpc_shift as mpc_shift, mpc_sqrt as mpc_sqrt, mpc_square as mpc_square, mpc_sub as mpc_sub, mpc_sub_mpf as mpc_sub_mpf, mpc_zero as mpc_zero
from .libmpf import ComplexResult as ComplexResult, bitcount as bitcount, finf as finf, fnan as fnan, fninf as fninf, fnone as fnone, fone as fone, from_int as from_int, from_man_exp as from_man_exp, from_rational as from_rational, ftwo as ftwo, fzero as fzero, mpf_abs as mpf_abs, mpf_add as mpf_add, mpf_cmp as mpf_cmp, mpf_div as mpf_div, mpf_gt as mpf_gt, mpf_le as mpf_le, mpf_lt as mpf_lt, mpf_min_max as mpf_min_max, mpf_mul as mpf_mul, mpf_neg as mpf_neg, mpf_perturb as mpf_perturb, mpf_pos as mpf_pos, mpf_pow_int as mpf_pow_int, mpf_rdiv_int as mpf_rdiv_int, mpf_shift as mpf_shift, mpf_sign as mpf_sign, mpf_sub as mpf_sub, negative_rnd as negative_rnd, round_fast as round_fast, round_nearest as round_nearest, sqrt_fixed as sqrt_fixed, to_fixed as to_fixed, to_int as to_int, to_rational as to_rational

class NoConvergence(Exception): ...

def make_hyp_summator(key):
    """
    Returns a function that sums a generalized hypergeometric series,
    for given parameter types (integer, rational, real, complex).

    """
def mpf_erf(x, prec, rnd=...): ...
def erfc_check_series(x, prec): ...
def mpf_erfc(x, prec, rnd=...): ...
def ei_taylor(x, prec): ...
def complex_ei_taylor(zre, zim, prec): ...
def ei_asymptotic(x, prec): ...
def complex_ei_asymptotic(zre, zim, prec): ...
def mpf_ei(x, prec, rnd=..., e1: bool = False): ...
def mpc_ei(z, prec, rnd=..., e1: bool = False): ...
def mpf_e1(x, prec, rnd=...): ...
def mpc_e1(x, prec, rnd=...): ...
def mpf_expint(n, x, prec, rnd=..., gamma: bool = False):
    """
    E_n(x), n an integer, x real

    With gamma=True, computes Gamma(n,x)   (upper incomplete gamma function)

    Returns (real, None) if real, otherwise (real, imag)
    The imaginary part is an optional branch cut term

    """
def mpf_ci_si_taylor(x, wp, which: int = 0):
    """
    0 - Ci(x) - (euler+log(x))
    1 - Si(x)
    """
def mpc_ci_si_taylor(re, im, wp, which: int = 0): ...
def mpf_ci_si(x, prec, rnd=..., which: int = 2):
    """
    Calculation of Ci(x), Si(x) for real x.

    which = 0 -- returns (Ci(x), -)
    which = 1 -- returns (Si(x), -)
    which = 2 -- returns (Ci(x), Si(x))

    Note: if x < 0, Ci(x) needs an additional imaginary term, pi*i.
    """
def mpf_ci(x, prec, rnd=...): ...
def mpf_si(x, prec, rnd=...): ...
def mpc_ci(z, prec, rnd=...): ...
def mpc_si(z, prec, rnd=...): ...
def mpf_besseljn(n, x, prec, rounding=...): ...
def mpc_besseljn(n, z, prec, rounding=...): ...
def mpf_agm(a, b, prec, rnd=...):
    """
    Computes the arithmetic-geometric mean agm(a,b) for
    nonnegative mpf values a, b.
    """
def mpf_agm1(a, prec, rnd=...):
    """
    Computes the arithmetic-geometric mean agm(1,a) for a nonnegative
    mpf value a.
    """
def mpc_agm(a, b, prec, rnd=...):
    """
    Complex AGM.

    TODO:
    * check that convergence works as intended
    * optimize
    * select a nonarbitrary branch
    """
def mpc_agm1(a, prec, rnd=...): ...
def mpf_ellipk(x, prec, rnd=...): ...
def mpc_ellipk(z, prec, rnd=...): ...
def mpf_ellipe(x, prec, rnd=...): ...
def mpc_ellipe(z, prec, rnd=...): ...
