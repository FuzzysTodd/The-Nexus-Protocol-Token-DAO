from .basis import nilradical_mod_p as nilradical_mod_p, round_two as round_two
from .exceptions import StructureError as StructureError
from .modules import ModuleEndomorphism as ModuleEndomorphism, find_min_poly as find_min_poly
from .utilities import coeff_search as coeff_search, supplement_a_subspace as supplement_a_subspace
from _typeshed import Incomplete
from sympy.polys.domains.finitefield import FF as FF
from sympy.polys.domains.integerring import ZZ as ZZ
from sympy.polys.domains.rationalfield import QQ as QQ
from sympy.polys.matrices.domainmatrix import DomainMatrix as DomainMatrix
from sympy.polys.polyerrors import CoercionFailed as CoercionFailed
from sympy.polys.polytools import Poly as Poly
from sympy.polys.polyutils import IntegerPowerable as IntegerPowerable
from sympy.utilities.decorator import public as public

class PrimeIdeal(IntegerPowerable):
    """
    A prime ideal in a ring of algebraic integers.
    """
    ZK: Incomplete
    p: Incomplete
    alpha: Incomplete
    f: Incomplete
    e: Incomplete
    def __init__(self, ZK, p, alpha, f, e: Incomplete | None = None) -> None:
        """
        Parameters
        ==========

        ZK : :py:class:`~.Submodule`
            The maximal order where this ideal lives.
        p : int
            The rational prime this ideal divides.
        alpha : :py:class:`~.PowerBasisElement`
            Such that the ideal is equal to ``p*ZK + alpha*ZK``.
        f : int
            The inertia degree.
        e : int, ``None``, optional
            The ramification index, if already known. If ``None``, we will
            compute it here.

        """
    @property
    def is_inert(self):
        """
        Say whether the rational prime we divide is inert, i.e. stays prime in
        our ring of integers.
        """
    def repr(self, field_gen: Incomplete | None = None, just_gens: bool = False):
        '''
        Print a representation of this prime ideal.

        Examples
        ========

        >>> from sympy import cyclotomic_poly, QQ
        >>> from sympy.abc import x, zeta
        >>> T = cyclotomic_poly(7, x)
        >>> K = QQ.algebraic_field((T, zeta))
        >>> P = K.primes_above(11)
        >>> print(P[0].repr())
        [ (11, x**3 + 5*x**2 + 4*x - 1) e=1, f=3 ]
        >>> print(P[0].repr(field_gen=zeta))
        [ (11, zeta**3 + 5*zeta**2 + 4*zeta - 1) e=1, f=3 ]
        >>> print(P[0].repr(field_gen=zeta, just_gens=True))
        (11, zeta**3 + 5*zeta**2 + 4*zeta - 1)

        Parameters
        ==========

        field_gen : :py:class:`~.Symbol`, ``None``, optional (default=None)
            The symbol to use for the generator of the field. This will appear
            in our representation of ``self.alpha``. If ``None``, we use the
            variable of the defining polynomial of ``self.ZK``.
        just_gens : bool, optional (default=False)
            If ``True``, just print the "(p, alpha)" part, showing "just the
            generators" of the prime ideal. Otherwise, print a string of the
            form "[ (p, alpha) e=..., f=... ]", giving the ramification index
            and inertia degree, along with the generators.

        '''
    def as_submodule(self):
        """
        Represent this prime ideal as a :py:class:`~.Submodule`.

        Explanation
        ===========

        The :py:class:`~.PrimeIdeal` class serves to bundle information about
        a prime ideal, such as its inertia degree, ramification index, and
        two-generator representation, as well as to offer helpful methods like
        :py:meth:`~.PrimeIdeal.valuation` and
        :py:meth:`~.PrimeIdeal.test_factor`.

        However, in order to be added and multiplied by other ideals or
        rational numbers, it must first be converted into a
        :py:class:`~.Submodule`, which is a class that supports these
        operations.

        In many cases, the user need not perform this conversion deliberately,
        since it is automatically performed by the arithmetic operator methods
        :py:meth:`~.PrimeIdeal.__add__` and :py:meth:`~.PrimeIdeal.__mul__`.

        Raising a :py:class:`~.PrimeIdeal` to a non-negative integer power is
        also supported.

        Examples
        ========

        >>> from sympy import Poly, cyclotomic_poly, prime_decomp
        >>> T = Poly(cyclotomic_poly(7))
        >>> P0 = prime_decomp(7, T)[0]
        >>> print(P0**6 == 7*P0.ZK)
        True

        Note that, on both sides of the equation above, we had a
        :py:class:`~.Submodule`. In the next equation we recall that adding
        ideals yields their GCD. This time, we need a deliberate conversion
        to :py:class:`~.Submodule` on the right:

        >>> print(P0 + 7*P0.ZK == P0.as_submodule())
        True

        Returns
        =======

        :py:class:`~.Submodule`
            Will be equal to ``self.p * self.ZK + self.alpha * self.ZK``.

        See Also
        ========

        __add__
        __mul__

        """
    def __eq__(self, other): ...
    def __add__(self, other):
        """
        Convert to a :py:class:`~.Submodule` and add to another
        :py:class:`~.Submodule`.

        See Also
        ========

        as_submodule

        """
    __radd__ = __add__
    def __mul__(self, other):
        """
        Convert to a :py:class:`~.Submodule` and multiply by another
        :py:class:`~.Submodule` or a rational number.

        See Also
        ========

        as_submodule

        """
    __rmul__ = __mul__
    def test_factor(self):
        '''
        Compute a test factor for this prime ideal.

        Explanation
        ===========

        Write $\\mathfrak{p}$ for this prime ideal, $p$ for the rational prime
        it divides. Then, for computing $\\mathfrak{p}$-adic valuations it is
        useful to have a number $\\beta \\in \\mathbb{Z}_K$ such that
        $p/\\mathfrak{p} = p \\mathbb{Z}_K + \\beta \\mathbb{Z}_K$.

        Essentially, this is the same as the number $\\Psi$ (or the "reagent")
        from Kummer\'s 1847 paper (*Ueber die Zerlegung...*, Crelle vol. 35) in
        which ideal divisors were invented.
        '''
    def valuation(self, I):
        """
        Compute the $\\mathfrak{p}$-adic valuation of integral ideal I at this
        prime ideal.

        Parameters
        ==========

        I : :py:class:`~.Submodule`

        See Also
        ========

        prime_valuation

        """
    def reduce_element(self, elt):
        '''
        Reduce a :py:class:`~.PowerBasisElement` to a "small representative"
        modulo this prime ideal.

        Parameters
        ==========

        elt : :py:class:`~.PowerBasisElement`
            The element to be reduced.

        Returns
        =======

        :py:class:`~.PowerBasisElement`
            The reduced element.

        See Also
        ========

        reduce_ANP
        reduce_alg_num
        .Submodule.reduce_element

        '''
    def reduce_ANP(self, a):
        '''
        Reduce an :py:class:`~.ANP` to a "small representative" modulo this
        prime ideal.

        Parameters
        ==========

        elt : :py:class:`~.ANP`
            The element to be reduced.

        Returns
        =======

        :py:class:`~.ANP`
            The reduced element.

        See Also
        ========

        reduce_element
        reduce_alg_num
        .Submodule.reduce_element

        '''
    def reduce_alg_num(self, a):
        '''
        Reduce an :py:class:`~.AlgebraicNumber` to a "small representative"
        modulo this prime ideal.

        Parameters
        ==========

        elt : :py:class:`~.AlgebraicNumber`
            The element to be reduced.

        Returns
        =======

        :py:class:`~.AlgebraicNumber`
            The reduced element.

        See Also
        ========

        reduce_element
        reduce_ANP
        .Submodule.reduce_element

        '''

def prime_valuation(I, P):
    """
    Compute the *P*-adic valuation for an integral ideal *I*.

    Examples
    ========

    >>> from sympy import QQ
    >>> from sympy.polys.numberfields import prime_valuation
    >>> K = QQ.cyclotomic_field(5)
    >>> P = K.primes_above(5)
    >>> ZK = K.maximal_order()
    >>> print(prime_valuation(25*ZK, P[0]))
    8

    Parameters
    ==========

    I : :py:class:`~.Submodule`
        An integral ideal whose valuation is desired.

    P : :py:class:`~.PrimeIdeal`
        The prime at which to compute the valuation.

    Returns
    =======

    int

    See Also
    ========

    .PrimeIdeal.valuation

    References
    ==========

    .. [1] Cohen, H. *A Course in Computational Algebraic Number Theory.*
       (See Algorithm 4.8.17.)

    """
def prime_decomp(p, T: Incomplete | None = None, ZK: Incomplete | None = None, dK: Incomplete | None = None, radical: Incomplete | None = None):
    """
    Compute the decomposition of rational prime *p* in a number field.

    Explanation
    ===========

    Ordinarily this should be accessed through the
    :py:meth:`~.AlgebraicField.primes_above` method of an
    :py:class:`~.AlgebraicField`.

    Examples
    ========

    >>> from sympy import Poly, QQ
    >>> from sympy.abc import x, theta
    >>> T = Poly(x ** 3 + x ** 2 - 2 * x + 8)
    >>> K = QQ.algebraic_field((T, theta))
    >>> print(K.primes_above(2))
    [[ (2, x**2 + 1) e=1, f=1 ], [ (2, (x**2 + 3*x + 2)/2) e=1, f=1 ],
     [ (2, (3*x**2 + 3*x)/2) e=1, f=1 ]]

    Parameters
    ==========

    p : int
        The rational prime whose decomposition is desired.

    T : :py:class:`~.Poly`, optional
        Monic irreducible polynomial defining the number field $K$ in which to
        factor. NOTE: at least one of *T* or *ZK* must be provided.

    ZK : :py:class:`~.Submodule`, optional
        The maximal order for $K$, if already known.
        NOTE: at least one of *T* or *ZK* must be provided.

    dK : int, optional
        The discriminant of the field $K$, if already known.

    radical : :py:class:`~.Submodule`, optional
        The nilradical mod *p* in the integers of $K$, if already known.

    Returns
    =======

    List of :py:class:`~.PrimeIdeal` instances.

    References
    ==========

    .. [1] Cohen, H. *A Course in Computational Algebraic Number Theory.*
       (See Algorithm 6.2.9.)

    """
