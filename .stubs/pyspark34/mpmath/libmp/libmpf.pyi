from .backend import BACKEND as BACKEND, HASH_BITS as HASH_BITS, HASH_MODULUS as HASH_MODULUS, MPZ as MPZ, MPZ_FIVE as MPZ_FIVE, MPZ_ONE as MPZ_ONE, MPZ_TWO as MPZ_TWO, MPZ_TYPE as MPZ_TYPE, MPZ_ZERO as MPZ_ZERO, STRICT as STRICT, gmpy as gmpy, sage as sage, sage_utils as sage_utils
from .libintmath import bctable as bctable, bin_to_radix as bin_to_radix, bitcount as bitcount, giant_steps as giant_steps, isqrt as isqrt, isqrt_fast as isqrt_fast, lshift as lshift, numeral as numeral, rshift as rshift, sqrt_fixed as sqrt_fixed, sqrtrem as sqrtrem, trailing as trailing, trailtable as trailtable
from _typeshed import Incomplete
from bisect import bisect as bisect

__docformat__: str
getrandbits: Incomplete

def to_pickable(x): ...
def from_pickable(x): ...

class ComplexResult(ValueError): ...

intern: Incomplete
round_nearest: Incomplete
round_floor: Incomplete
round_ceiling: Incomplete
round_up: Incomplete
round_down: Incomplete
round_fast = round_down

def prec_to_dps(n):
    """Return number of accurate decimals that can be represented
    with a precision of n bits."""
def dps_to_prec(n):
    """Return the number of bits required to represent n decimals
    accurately."""
def repr_dps(n):
    """Return the number of decimal digits required to represent
    a number with n-bit precision so that it can be uniquely
    reconstructed from the representation."""

fzero: Incomplete
fnzero: Incomplete
fone: Incomplete
fnone: Incomplete
ftwo: Incomplete
ften: Incomplete
fhalf: Incomplete
fnan: Incomplete
finf: Incomplete
fninf: Incomplete
math_float_inf: Incomplete

def round_int(x, n, rnd): ...

class h_mask_big:
    def __getitem__(self, n): ...

h_mask_small: Incomplete
h_mask: Incomplete
shifts_down: Incomplete

def strict_normalize(sign, man, exp, bc, prec, rnd):
    """Additional checks on the components of an mpf. Enable tests by setting
       the environment variable MPMATH_STRICT to Y."""
def strict_normalize1(sign, man, exp, bc, prec, rnd):
    """Additional checks on the components of an mpf. Enable tests by setting
       the environment variable MPMATH_STRICT to Y."""
normalize = strict_normalize
normalize1 = strict_normalize1

def from_man_exp(man, exp, prec: Incomplete | None = None, rnd=...):
    """Create raw mpf from (man, exp) pair. The mantissa may be signed.
    If no precision is specified, the mantissa is stored exactly."""

int_cache: Incomplete
from_man_exp: Incomplete

def from_int(n, prec: int = 0, rnd=...):
    """Create a raw mpf from an integer. If no precision is specified,
    the mantissa is stored exactly."""
def to_man_exp(s):
    """Return (man, exp) of a raw mpf. Raise an error if inf/nan."""
def to_int(s, rnd: Incomplete | None = None):
    """Convert a raw mpf to the nearest int. Rounding is done down by
    default (same as int(float) in Python), but can be changed. If the
    input is inf/nan, an exception is raised."""
def mpf_round_int(s, rnd): ...
def mpf_floor(s, prec: int = 0, rnd=...): ...
def mpf_ceil(s, prec: int = 0, rnd=...): ...
def mpf_nint(s, prec: int = 0, rnd=...): ...
def mpf_frac(s, prec: int = 0, rnd=...): ...
def from_float(x, prec: int = 53, rnd=...):
    """Create a raw mpf from a Python float, rounding if necessary.
    If prec >= 53, the result is guaranteed to represent exactly the
    same number as the input. If prec is not specified, use prec=53."""
def from_npfloat(x, prec: int = 113, rnd=...):
    """Create a raw mpf from a numpy float, rounding if necessary.
    If prec >= 113, the result is guaranteed to represent exactly the
    same number as the input. If prec is not specified, use prec=113."""
def from_Decimal(x, prec: Incomplete | None = None, rnd=...):
    """Create a raw mpf from a Decimal, rounding if necessary.
    If prec is not specified, use the equivalent bit precision
    of the number of significant digits in x."""
def to_float(s, strict: bool = False, rnd=...):
    """
    Convert a raw mpf to a Python float. The result is exact if the
    bitcount of s is <= 53 and no underflow/overflow occurs.

    If the number is too large or too small to represent as a regular
    float, it will be converted to inf or 0.0. Setting strict=True
    forces an OverflowError to be raised instead.

    Warning: with a directed rounding mode, the correct nearest representable
    floating-point number in the specified direction might not be computed
    in case of overflow or (gradual) underflow.
    """
def from_rational(p, q, prec, rnd=...):
    """Create a raw mpf from a rational number p/q, round if
    necessary."""
def to_rational(s):
    """Convert a raw mpf to a rational number. Return integers (p, q)
    such that s = p/q exactly."""
def to_fixed(s, prec):
    """Convert a raw mpf to a fixed-point big integer"""
def mpf_rand(prec):
    """Return a raw mpf chosen randomly from [0, 1), with prec bits
    in the mantissa."""
def mpf_eq(s, t):
    """Test equality of two raw mpfs. This is simply tuple comparison
    unless either number is nan, in which case the result is False."""
def mpf_hash(s): ...
def mpf_cmp(s, t):
    """Compare the raw mpfs s and t. Return -1 if s < t, 0 if s == t,
    and 1 if s > t. (Same convention as Python's cmp() function.)"""
def mpf_lt(s, t): ...
def mpf_le(s, t): ...
def mpf_gt(s, t): ...
def mpf_ge(s, t): ...
def mpf_min_max(seq): ...
def mpf_pos(s, prec: int = 0, rnd=...):
    """Calculate 0+s for a raw mpf (i.e., just round s to the specified
    precision)."""
def mpf_neg(s, prec: Incomplete | None = None, rnd=...):
    """Negate a raw mpf (return -s), rounding the result to the
    specified precision. The prec argument can be omitted to do the
    operation exactly."""
def mpf_abs(s, prec: Incomplete | None = None, rnd=...):
    """Return abs(s) of the raw mpf s, rounded to the specified
    precision. The prec argument can be omitted to generate an
    exact result."""
def mpf_sign(s):
    """Return -1, 0, or 1 (as a Python int, not a raw mpf) depending on
    whether s is negative, zero, or positive. (Nan is taken to give 0.)"""
def mpf_add(s, t, prec: int = 0, rnd=..., _sub: int = 0):
    """
    Add the two raw mpf values s and t.

    With prec=0, no rounding is performed. Note that this can
    produce a very large mantissa (potentially too large to fit
    in memory) if exponents are far apart.
    """
def mpf_sub(s, t, prec: int = 0, rnd=...):
    """Return the difference of two raw mpfs, s-t. This function is
    simply a wrapper of mpf_add that changes the sign of t."""
def mpf_sum(xs, prec: int = 0, rnd=..., absolute: bool = False):
    """
    Sum a list of mpf values efficiently and accurately
    (typically no temporary roundoff occurs). If prec=0,
    the final result will not be rounded either.

    There may be roundoff error or cancellation if extremely
    large exponent differences occur.

    With absolute=True, sums the absolute values.
    """
def gmpy_mpf_mul(s, t, prec: int = 0, rnd=...):
    """Multiply two raw mpfs"""
def gmpy_mpf_mul_int(s, n, prec, rnd=...):
    """Multiply by a Python integer."""
def python_mpf_mul(s, t, prec: int = 0, rnd=...):
    """Multiply two raw mpfs"""
def python_mpf_mul_int(s, n, prec, rnd=...):
    """Multiply by a Python integer."""
mpf_mul = gmpy_mpf_mul
mpf_mul_int = gmpy_mpf_mul_int
mpf_mul = python_mpf_mul
mpf_mul_int = python_mpf_mul_int

def mpf_shift(s, n):
    """Quickly multiply the raw mpf s by 2**n without rounding."""
def mpf_frexp(x):
    """Convert x = y*2**n to (y, n) with abs(y) in [0.5, 1) if nonzero"""
def mpf_div(s, t, prec, rnd=...):
    """Floating-point division"""
def mpf_rdiv_int(n, t, prec, rnd=...):
    """Floating-point division n/t with a Python integer as numerator"""
def mpf_mod(s, t, prec, rnd=...): ...

reciprocal_rnd: Incomplete
negative_rnd: Incomplete

def mpf_pow_int(s, n, prec, rnd=...):
    """Compute s**n, where s is a raw mpf and n is a Python integer."""
def mpf_perturb(x, eps_sign, prec, rnd):
    """
    For nonzero x, calculate x + eps with directed rounding, where
    eps < prec relatively and eps has the given sign (0 for
    positive, 1 for negative).

    With rounding to nearest, this is taken to simply normalize
    x to the given precision.
    """
def to_digits_exp(s, dps):
    """Helper function for representing the floating-point number s as
    a decimal with dps digits. Returns (sign, string, exponent) where
    sign is '' or '-', string is the digit string, and exponent is
    the decimal exponent as an int.

    If inexact, the decimal representation is rounded toward zero."""
def to_str(s, dps, strip_zeros: bool = True, min_fixed: Incomplete | None = None, max_fixed: Incomplete | None = None, show_zero_exponent: bool = False):
    """
    Convert a raw mpf to a decimal floating-point literal with at
    most `dps` decimal digits in the mantissa (not counting extra zeros
    that may be inserted for visual purposes).

    The number will be printed in fixed-point format if the position
    of the leading digit is strictly between min_fixed
    (default = min(-dps/3,-5)) and max_fixed (default = dps).

    To force fixed-point format always, set min_fixed = -inf,
    max_fixed = +inf. To force floating-point format, set
    min_fixed >= max_fixed.

    The literal is formatted so that it can be parsed back to a number
    by to_str, float() or Decimal().
    """
def str_to_man_exp(x, base: int = 10):
    """Helper function for from_str."""

special_str: Incomplete

def from_str(x, prec, rnd=...):
    """Create a raw mpf from a decimal literal, rounding in the
    specified direction if the input number cannot be represented
    exactly as a binary floating-point number with the given number of
    bits. The literal syntax accepted is the same as for Python
    floats.

    TODO: the rounding does not work properly for large exponents.
    """
def from_bstr(x): ...
def to_bstr(x): ...
def mpf_sqrt(s, prec, rnd=...):
    """
    Compute the square root of a nonnegative mpf value. The
    result is correctly rounded.
    """
def mpf_hypot(x, y, prec, rnd=...):
    """Compute the Euclidean norm sqrt(x**2 + y**2) of two raw mpfs
    x and y."""

mpf_add: Incomplete
mpf_sub: Incomplete
mpf_div: Incomplete
mpf_sqrt: Incomplete
