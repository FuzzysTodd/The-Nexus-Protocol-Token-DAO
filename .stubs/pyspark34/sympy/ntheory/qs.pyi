from _typeshed import Incomplete
from sympy.core.numbers import igcd as igcd, mod_inverse as mod_inverse
from sympy.core.power import integer_nthroot as integer_nthroot
from sympy.ntheory import isprime as isprime

rgen: Incomplete

class SievePolynomial:
    modified_coeff: Incomplete
    a: Incomplete
    b: Incomplete
    def __init__(self, modified_coeff=(), a: Incomplete | None = None, b: Incomplete | None = None) -> None:
        """This class denotes the seive polynomial.
        If ``g(x) = (a*x + b)**2 - N``. `g(x)` can be expanded
        to ``a*x**2 + 2*a*b*x + b**2 - N``, so the coefficient
        is stored in the form `[a**2, 2*a*b, b**2 - N]`. This
        ensures faster `eval` method because we dont have to
        perform `a**2, 2*a*b, b**2` every time we call the
        `eval` method. As multiplication is more expensive
        than addition, by using modified_coefficient we get
        a faster seiving process.

        Parameters
        ==========

        modified_coeff : modified_coefficient of sieve polynomial
        a : parameter of the sieve polynomial
        b : parameter of the sieve polynomial
        """
    def eval(self, x):
        """
        Compute the value of the sieve polynomial at point x.

        Parameters
        ==========

        x : Integer parameter for sieve polynomial
        """

class FactorBaseElem:
    """This class stores an element of the `factor_base`.
    """
    prime: Incomplete
    tmem_p: Incomplete
    log_p: Incomplete
    soln1: Incomplete
    soln2: Incomplete
    a_inv: Incomplete
    b_ainv: Incomplete
    def __init__(self, prime, tmem_p, log_p) -> None:
        """
        Initialization of factor_base_elem.

        Parameters
        ==========

        prime : prime number of the factor_base
        tmem_p : Integer square root of x**2 = n mod prime
        log_p : Compute Natural Logarithm of the prime
        """

def qs(N, prime_bound, M, ERROR_TERM: int = 25, seed: int = 1234):
    """Performs factorization using Self-Initializing Quadratic Sieve.
    In SIQS, let N be a number to be factored, and this N should not be a
    perfect power. If we find two integers such that ``X**2 = Y**2 modN`` and
    ``X != +-Y modN``, then `gcd(X + Y, N)` will reveal a proper factor of N.
    In order to find these integers X and Y we try to find relations of form
    t**2 = u modN where u is a product of small primes. If we have enough of
    these relations then we can form ``(t1*t2...ti)**2 = u1*u2...ui modN`` such that
    the right hand side is a square, thus we found a relation of ``X**2 = Y**2 modN``.

    Here, several optimizations are done like using multiple polynomials for
    sieving, fast changing between polynomials and using partial relations.
    The use of partial relations can speeds up the factoring by 2 times.

    Parameters
    ==========

    N : Number to be Factored
    prime_bound : upper bound for primes in the factor base
    M : Sieve Interval
    ERROR_TERM : Error term for checking smoothness
    threshold : Extra smooth relations for factorization
    seed : generate pseudo prime numbers

    Examples
    ========

    >>> from sympy.ntheory import qs
    >>> qs(25645121643901801, 2000, 10000)
    {5394769, 4753701529}
    >>> qs(9804659461513846513, 2000, 10000)
    {4641991, 2112166839943}

    References
    ==========

    .. [1] https://pdfs.semanticscholar.org/5c52/8a975c1405bd35c65993abf5a4edb667c1db.pdf
    .. [2] https://www.rieselprime.de/ziki/Self-initializing_quadratic_sieve
    """
