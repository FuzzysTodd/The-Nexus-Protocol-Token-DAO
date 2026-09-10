from .backend import BACKEND as BACKEND, MPZ as MPZ, MPZ_ONE as MPZ_ONE, MPZ_ZERO as MPZ_ZERO, gmpy as gmpy, sage as sage, sage_utils as sage_utils, xrange as xrange
from _typeshed import Incomplete

small_trailing: Incomplete

def giant_steps(start, target, n: int = 2):
    """
    Return a list of integers ~=

    [start, n*start, ..., target/n^2, target/n, target]

    but conservatively rounded so that the quotient between two
    successive elements is actually slightly less than n.

    With n = 2, this describes suitable precision steps for a
    quadratically convergent algorithm such as Newton's method;
    with n = 3 steps for cubic convergence (Halley's method), etc.

        >>> giant_steps(50,1000)
        [66, 128, 253, 502, 1000]
        >>> giant_steps(50,1000,4)
        [65, 252, 1000]

    """
def rshift(x, n):
    """For an integer x, calculate x >> n with the fastest (floor)
    rounding. Unlike the plain Python expression (x >> n), n is
    allowed to be negative, in which case a left shift is performed."""
def lshift(x, n):
    """For an integer x, calculate x << n. Unlike the plain Python
    expression (x << n), n is allowed to be negative, in which case a
    right shift with default (floor) rounding is performed."""

rshift: Incomplete
lshift: Incomplete

def python_trailing(n):
    """Count the number of trailing zero bits in abs(n)."""
def gmpy_trailing(n):
    """Count the number of trailing zero bits in abs(n) using gmpy."""

powers: Incomplete

def python_bitcount(n):
    """Calculate bit size of the nonnegative integer n."""
def gmpy_bitcount(n):
    """Calculate bit size of the nonnegative integer n."""
def sage_trailing(n): ...
bitcount = gmpy_bitcount
trailing = gmpy_trailing
sage_bitcount: Incomplete
bitcount = sage_bitcount
trailing = sage_trailing
bitcount = python_bitcount
trailing = python_trailing
trailtable: Incomplete
bctable: Incomplete

def bin_to_radix(x, xbits, base, bdigits):
    """Changes radix of a fixed-point number; i.e., converts
    x * 2**xbits to floor(x * 10**bdigits)."""

stddigits: str

def small_numeral(n, base: int = 10, digits=...):
    """Return the string numeral of a positive integer in an arbitrary
    base. Most efficient for small input."""
def numeral_python(n, base: int = 10, size: int = 0, digits=...):
    """Represent the integer n as a string of digits in the given base.
    Recursive division is used to make this function about 3x faster
    than Python's str() for converting integers to decimal strings.

    The 'size' parameters specifies the number of digits in n; this
    number is only used to determine splitting points and need not be
    exact."""
def numeral_gmpy(n, base: int = 10, size: int = 0, digits=...):
    """Represent the integer n as a string of digits in the given base.
    Recursive division is used to make this function about 3x faster
    than Python's str() for converting integers to decimal strings.

    The 'size' parameters specifies the number of digits in n; this
    number is only used to determine splitting points and need not be
    exact."""
numeral = numeral_gmpy
numeral = numeral_python

def isqrt_small_python(x):
    """
    Correctly (floor) rounded integer square root, using
    division. Fast up to ~200 digits.
    """
def isqrt_fast_python(x):
    """
    Fast approximate integer square root, computed using division-free
    Newton iteration for large x. For random integers the result is almost
    always correct (floor(sqrt(x))), but is 1 ulp too small with a roughly
    0.1% probability. If x is very close to an exact square, the answer is
    1 ulp wrong with high probability.

    With 0 guard bits, the largest error over a set of 10^5 random
    inputs of size 1-10^5 bits was 3 ulp. The use of 10 guard bits
    almost certainly guarantees a max 1 ulp error.
    """
def sqrtrem_python(x):
    """Correctly rounded integer (floor) square root with remainder."""
def isqrt_python(x):
    """Integer square root with correct (floor) rounding."""
def sqrt_fixed(x, prec): ...
sqrt_fixed2 = sqrt_fixed
isqrt_small: Incomplete
isqrt_fast: Incomplete
isqrt: Incomplete
sqrtrem: Incomplete
isqrt_small = isqrt_small_python
isqrt_fast = isqrt_fast_python
isqrt = isqrt_python
sqrtrem = sqrtrem_python

def ifib(n, _cache={}):
    """Computes the nth Fibonacci number as an integer, for
    integer n."""

MAX_FACTORIAL_CACHE: int

def ifac(n, memo={0: 1, 1: 1}):
    """Return n factorial (for integers n >= 0 only)."""
def ifac2(n, memo_pair=[{0: 1}, {1: 1}]):
    """Return n!! (double factorial), integers n >= 0 only."""

ifac: Incomplete
ifib: Incomplete

def list_primes(n): ...

small_odd_primes: Incomplete
small_odd_primes_set: Incomplete

def isprime(n):
    """
    Determines whether n is a prime number. A probabilistic test is
    performed if n is very large. No special trick is used for detecting
    perfect powers.

        >>> sum(list_primes(100000))
        454396537
        >>> sum(n*isprime(n) for n in range(100000))
        454396537

    """
def moebius(n):
    """
    Evaluates the Moebius function which is `mu(n) = (-1)^k` if `n`
    is a product of `k` distinct primes and `mu(n) = 0` otherwise.

    TODO: speed up using factorization
    """
def gcd(*args): ...

MAX_EULER_CACHE: int

def eulernum(m, _cache=...):
    """
    Computes the Euler numbers `E(n)`, which can be defined as
    coefficients of the Taylor expansion of `1/cosh x`:

    .. math ::

        \\frac{1}{\\cosh x} = \\sum_{n=0}^\\infty \\frac{E_n}{n!} x^n

    Example::

        >>> [int(eulernum(n)) for n in range(11)]
        [1, 0, -1, 0, 5, 0, -61, 0, 1385, 0, -50521]
        >>> [int(eulernum(n)) for n in range(11)]   # test cache
        [1, 0, -1, 0, 5, 0, -61, 0, 1385, 0, -50521]

    """
def stirling1(n, k):
    """
    Stirling number of the first kind.
    """
def stirling2(n, k):
    """
    Stirling number of the second kind.
    """
