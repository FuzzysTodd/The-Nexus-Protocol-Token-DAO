from sympy.core.numbers import igcd as igcd, igcdex as igcdex
from sympy.ntheory.primetest import isprime as isprime
from sympy.polys.domains import ZZ as ZZ
from sympy.polys.galoistools import gf_crt as gf_crt, gf_crt1 as gf_crt1, gf_crt2 as gf_crt2
from sympy.utilities.misc import as_int as as_int

def symmetric_residue(a, m):
    """Return the residual mod m such that it is within half of the modulus.

    >>> from sympy.ntheory.modular import symmetric_residue
    >>> symmetric_residue(1, 6)
    1
    >>> symmetric_residue(4, 6)
    -2
    """
def crt(m, v, symmetric: bool = False, check: bool = True):
    """Chinese Remainder Theorem.

    The moduli in m are assumed to be pairwise coprime.  The output
    is then an integer f, such that f = v_i mod m_i for each pair out
    of v and m. If ``symmetric`` is False a positive integer will be
    returned, else \\|f\\| will be less than or equal to the LCM of the
    moduli, and thus f may be negative.

    If the moduli are not co-prime the correct result will be returned
    if/when the test of the result is found to be incorrect. This result
    will be None if there is no solution.

    The keyword ``check`` can be set to False if it is known that the moduli
    are coprime.

    Examples
    ========

    As an example consider a set of residues ``U = [49, 76, 65]``
    and a set of moduli ``M = [99, 97, 95]``. Then we have::

       >>> from sympy.ntheory.modular import crt

       >>> crt([99, 97, 95], [49, 76, 65])
       (639985, 912285)

    This is the correct result because::

       >>> [639985 % m for m in [99, 97, 95]]
       [49, 76, 65]

    If the moduli are not co-prime, you may receive an incorrect result
    if you use ``check=False``:

       >>> crt([12, 6, 17], [3, 4, 2], check=False)
       (954, 1224)
       >>> [954 % m for m in [12, 6, 17]]
       [6, 0, 2]
       >>> crt([12, 6, 17], [3, 4, 2]) is None
       True
       >>> crt([3, 6], [2, 5])
       (5, 6)

    Note: the order of gf_crt's arguments is reversed relative to crt,
    and that solve_congruence takes residue, modulus pairs.

    Programmer's note: rather than checking that all pairs of moduli share
    no GCD (an O(n**2) test) and rather than factoring all moduli and seeing
    that there is no factor in common, a check that the result gives the
    indicated residuals is performed -- an O(n) operation.

    See Also
    ========

    solve_congruence
    sympy.polys.galoistools.gf_crt : low level crt routine used by this routine
    """
def crt1(m):
    """First part of Chinese Remainder Theorem, for multiple application.

    Examples
    ========

    >>> from sympy.ntheory.modular import crt1
    >>> crt1([18, 42, 6])
    (4536, [252, 108, 756], [0, 2, 0])
    """
def crt2(m, v, mm, e, s, symmetric: bool = False):
    """Second part of Chinese Remainder Theorem, for multiple application.

    Examples
    ========

    >>> from sympy.ntheory.modular import crt1, crt2
    >>> mm, e, s = crt1([18, 42, 6])
    >>> crt2([18, 42, 6], [0, 0, 0], mm, e, s)
    (0, 4536)
    """
def solve_congruence(*remainder_modulus_pairs, **hint):
    """Compute the integer ``n`` that has the residual ``ai`` when it is
    divided by ``mi`` where the ``ai`` and ``mi`` are given as pairs to
    this function: ((a1, m1), (a2, m2), ...). If there is no solution,
    return None. Otherwise return ``n`` and its modulus.

    The ``mi`` values need not be co-prime. If it is known that the moduli are
    not co-prime then the hint ``check`` can be set to False (default=True) and
    the check for a quicker solution via crt() (valid when the moduli are
    co-prime) will be skipped.

    If the hint ``symmetric`` is True (default is False), the value of ``n``
    will be within 1/2 of the modulus, possibly negative.

    Examples
    ========

    >>> from sympy.ntheory.modular import solve_congruence

    What number is 2 mod 3, 3 mod 5 and 2 mod 7?

    >>> solve_congruence((2, 3), (3, 5), (2, 7))
    (23, 105)
    >>> [23 % m for m in [3, 5, 7]]
    [2, 3, 2]

    If you prefer to work with all remainder in one list and
    all moduli in another, send the arguments like this:

    >>> solve_congruence(*zip((2, 3, 2), (3, 5, 7)))
    (23, 105)

    The moduli need not be co-prime; in this case there may or
    may not be a solution:

    >>> solve_congruence((2, 3), (4, 6)) is None
    True

    >>> solve_congruence((2, 3), (5, 6))
    (5, 6)

    The symmetric flag will make the result be within 1/2 of the modulus:

    >>> solve_congruence((2, 3), (5, 6), symmetric=True)
    (-1, 6)

    See Also
    ========

    crt : high level routine implementing the Chinese Remainder Theorem

    """
