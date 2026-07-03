from sympy.core.numbers import igcd as igcd
from sympy.core.power import integer_nthroot as integer_nthroot
from sympy.core.sympify import sympify as sympify
from sympy.external.gmpy import HAS_GMPY as HAS_GMPY
from sympy.utilities.misc import as_int as as_int

def is_euler_pseudoprime(n, b):
    """Returns True if n is prime or an Euler pseudoprime to base b, else False.

    Euler Pseudoprime : In arithmetic, an odd composite integer n is called an
    euler pseudoprime to base a, if a and n are coprime and satisfy the modular
    arithmetic congruence relation :

    a ^ (n-1)/2 = + 1(mod n) or
    a ^ (n-1)/2 = - 1(mod n)

    (where mod refers to the modulo operation).

    Examples
    ========

    >>> from sympy.ntheory.primetest import is_euler_pseudoprime
    >>> is_euler_pseudoprime(2, 5)
    True

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Euler_pseudoprime
    """
def is_square(n, prep: bool = True):
    """Return True if n == a * a for some integer a, else False.
    If n is suspected of *not* being a square then this is a
    quick method of confirming that it is not.

    Examples
    ========

    >>> from sympy.ntheory.primetest import is_square
    >>> is_square(25)
    True
    >>> is_square(2)
    False

    References
    ==========

    .. [1]  https://mersenneforum.org/showpost.php?p=110896

    See Also
    ========
    sympy.core.power.integer_nthroot
    """
def mr(n, bases):
    '''Perform a Miller-Rabin strong pseudoprime test on n using a
    given list of bases/witnesses.

    References
    ==========

    .. [1] Richard Crandall & Carl Pomerance (2005), "Prime Numbers:
           A Computational Perspective", Springer, 2nd edition, 135-138

    A list of thresholds and the bases they require are here:
    https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Deterministic_variants

    Examples
    ========

    >>> from sympy.ntheory.primetest import mr
    >>> mr(1373651, [2, 3])
    False
    >>> mr(479001599, [31, 73])
    True

    '''
def is_lucas_prp(n):
    '''Standard Lucas compositeness test with Selfridge parameters.  Returns
    False if n is definitely composite, and True if n is a Lucas probable
    prime.

    This is typically used in combination with the Miller-Rabin test.

    References
    ==========
    - "Lucas Pseudoprimes", Baillie and Wagstaff, 1980.
      http://mpqs.free.fr/LucasPseudoprimes.pdf
    - OEIS A217120: Lucas Pseudoprimes
      https://oeis.org/A217120
    - https://en.wikipedia.org/wiki/Lucas_pseudoprime

    Examples
    ========

    >>> from sympy.ntheory.primetest import isprime, is_lucas_prp
    >>> for i in range(10000):
    ...     if is_lucas_prp(i) and not isprime(i):
    ...        print(i)
    323
    377
    1159
    1829
    3827
    5459
    5777
    9071
    9179
    '''
def is_strong_lucas_prp(n):
    '''Strong Lucas compositeness test with Selfridge parameters.  Returns
    False if n is definitely composite, and True if n is a strong Lucas
    probable prime.

    This is often used in combination with the Miller-Rabin test, and
    in particular, when combined with M-R base 2 creates the strong BPSW test.

    References
    ==========
    - "Lucas Pseudoprimes", Baillie and Wagstaff, 1980.
      http://mpqs.free.fr/LucasPseudoprimes.pdf
    - OEIS A217255: Strong Lucas Pseudoprimes
      https://oeis.org/A217255
    - https://en.wikipedia.org/wiki/Lucas_pseudoprime
    - https://en.wikipedia.org/wiki/Baillie-PSW_primality_test

    Examples
    ========

    >>> from sympy.ntheory.primetest import isprime, is_strong_lucas_prp
    >>> for i in range(20000):
    ...     if is_strong_lucas_prp(i) and not isprime(i):
    ...        print(i)
    5459
    5777
    10877
    16109
    18971
    '''
def is_extra_strong_lucas_prp(n):
    '''Extra Strong Lucas compositeness test.  Returns False if n is
    definitely composite, and True if n is a "extra strong" Lucas probable
    prime.

    The parameters are selected using P = 3, Q = 1, then incrementing P until
    (D|n) == -1.  The test itself is as defined in Grantham 2000, from the
    Mo and Jones preprint.  The parameter selection and test are the same as
    used in OEIS A217719, Perl\'s Math::Prime::Util, and the Lucas pseudoprime
    page on Wikipedia.

    With these parameters, there are no counterexamples below 2^64 nor any
    known above that range.  It is 20-50% faster than the strong test.

    Because of the different parameters selected, there is no relationship
    between the strong Lucas pseudoprimes and extra strong Lucas pseudoprimes.
    In particular, one is not a subset of the other.

    References
    ==========
    - "Frobenius Pseudoprimes", Jon Grantham, 2000.
      https://www.ams.org/journals/mcom/2001-70-234/S0025-5718-00-01197-2/
    - OEIS A217719: Extra Strong Lucas Pseudoprimes
      https://oeis.org/A217719
    - https://en.wikipedia.org/wiki/Lucas_pseudoprime

    Examples
    ========

    >>> from sympy.ntheory.primetest import isprime, is_extra_strong_lucas_prp
    >>> for i in range(20000):
    ...     if is_extra_strong_lucas_prp(i) and not isprime(i):
    ...        print(i)
    989
    3239
    5777
    10877
    '''
def isprime(n):
    '''
    Test if n is a prime number (True) or not (False). For n < 2^64 the
    answer is definitive; larger n values have a small probability of actually
    being pseudoprimes.

    Negative numbers (e.g. -2) are not considered prime.

    The first step is looking for trivial factors, which if found enables
    a quick return.  Next, if the sieve is large enough, use bisection search
    on the sieve.  For small numbers, a set of deterministic Miller-Rabin
    tests are performed with bases that are known to have no counterexamples
    in their range.  Finally if the number is larger than 2^64, a strong
    BPSW test is performed.  While this is a probable prime test and we
    believe counterexamples exist, there are no known counterexamples.

    Examples
    ========

    >>> from sympy.ntheory import isprime
    >>> isprime(13)
    True
    >>> isprime(13.0)  # limited precision
    False
    >>> isprime(15)
    False

    Notes
    =====

    This routine is intended only for integer input, not numerical
    expressions which may represent numbers. Floats are also
    rejected as input because they represent numbers of limited
    precision. While it is tempting to permit 7.0 to represent an
    integer there are errors that may "pass silently" if this is
    allowed:

    >>> from sympy import Float, S
    >>> int(1e3) == 1e3 == 10**3
    True
    >>> int(1e23) == 1e23
    True
    >>> int(1e23) == 10**23
    False

    >>> near_int = 1 + S(1)/10**19
    >>> near_int == int(near_int)
    False
    >>> n = Float(near_int, 10)  # truncated by precision
    >>> n == int(n)
    True
    >>> n = Float(near_int, 20)
    >>> n == int(n)
    False

    See Also
    ========

    sympy.ntheory.generate.primerange : Generates all primes in a given range
    sympy.ntheory.generate.primepi : Return the number of primes less than or equal to n
    sympy.ntheory.generate.prime : Return the nth prime

    References
    ==========
    - https://en.wikipedia.org/wiki/Strong_pseudoprime
    - "Lucas Pseudoprimes", Baillie and Wagstaff, 1980.
      http://mpqs.free.fr/LucasPseudoprimes.pdf
    - https://en.wikipedia.org/wiki/Baillie-PSW_primality_test
    '''
def is_gaussian_prime(num):
    """Test if num is a Gaussian prime number.

    References
    ==========

    .. [1] https://oeis.org/wiki/Gaussian_primes
    """
