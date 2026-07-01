import math
from . import function_docs as function_docs, libmp as libmp, math2 as math2
from .ctx_base import StandardBaseContext as StandardBaseContext
from .libmp import int_types as int_types, mpf_bernoulli as mpf_bernoulli, to_float as to_float
from _typeshed import Incomplete

class FPContext(StandardBaseContext):
    """
    Context for fast low-precision arithmetic (53-bit precision, giving at most
    about 15-digit accuracy), using Python's builtin float and complex.
    """
    def __init__(ctx) -> None: ...
    NoConvergence = libmp.NoConvergence
    prec: Incomplete
    dps: Incomplete
    zero: float
    one: float
    eps: Incomplete
    inf: Incomplete
    ninf: Incomplete
    nan: Incomplete
    j: complex
    def bernoulli(ctx, n): ...
    pi: Incomplete
    e: Incomplete
    euler: Incomplete
    sqrt2: float
    sqrt5: float
    phi: float
    ln2: float
    ln10: float
    catalan: float
    khinchin: float
    apery: float
    glaisher: float
    absmin = abs
    absmax = abs
    def is_special(ctx, x): ...
    def isnan(ctx, x): ...
    def isinf(ctx, x): ...
    def isnormal(ctx, x): ...
    def isnpint(ctx, x): ...
    mpf = float
    mpc = complex
    def convert(ctx, x): ...
    power: Incomplete
    sqrt: Incomplete
    exp: Incomplete
    ln: Incomplete
    log: Incomplete
    cos: Incomplete
    sin: Incomplete
    tan: Incomplete
    cos_sin: Incomplete
    acos: Incomplete
    asin: Incomplete
    atan: Incomplete
    cosh: Incomplete
    sinh: Incomplete
    tanh: Incomplete
    gamma: Incomplete
    rgamma: Incomplete
    fac: Incomplete
    factorial: Incomplete
    floor: Incomplete
    ceil: Incomplete
    cospi: Incomplete
    sinpi: Incomplete
    cbrt: Incomplete
    def arg(ctx, z): ...
    def expj(ctx, x): ...
    def expjpi(ctx, x): ...
    ldexp = math.ldexp
    frexp = math.frexp
    def mag(ctx, z): ...
    def isint(ctx, z): ...
    def nint_distance(ctx, z): ...
    def hypsum(ctx, p, q, types, coeffs, z, maxterms: int = 6000, **kwargs): ...
    def atan2(ctx, x, y): ...
    def psi(ctx, m, z): ...
    digamma: Incomplete
    def harmonic(ctx, x): ...
    nstr = str
    def to_fixed(ctx, x, prec): ...
    def rand(ctx): ...
    def sum_accurately(ctx, terms, check_step: int = 1): ...
