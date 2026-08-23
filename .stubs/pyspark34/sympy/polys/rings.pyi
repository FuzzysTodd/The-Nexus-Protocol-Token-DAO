from _typeshed import Incomplete
from sympy.core.expr import Expr as Expr
from sympy.core.numbers import igcd as igcd, oo as oo
from sympy.core.symbol import Symbol as Symbol
from sympy.core.sympify import CantSympify as CantSympify, sympify as sympify
from sympy.ntheory.multinomial import multinomial_coefficients as multinomial_coefficients
from sympy.polys.compatibility import IPolys as IPolys
from sympy.polys.constructor import construct_domain as construct_domain
from sympy.polys.densebasic import dmp_from_dict as dmp_from_dict, dmp_to_dict as dmp_to_dict
from sympy.polys.domains.domainelement import DomainElement as DomainElement
from sympy.polys.domains.polynomialring import PolynomialRing as PolynomialRing
from sympy.polys.heuristicgcd import heugcd as heugcd
from sympy.polys.monomials import MonomialOps as MonomialOps
from sympy.polys.orderings import lex as lex
from sympy.polys.polyerrors import CoercionFailed as CoercionFailed, ExactQuotientFailed as ExactQuotientFailed, GeneratorsError as GeneratorsError, MultivariatePolynomialError as MultivariatePolynomialError
from sympy.polys.polyoptions import build_options as build_options
from sympy.polys.polyutils import expr_from_dict as expr_from_dict
from sympy.printing.defaults import DefaultPrinting as DefaultPrinting
from sympy.utilities import public as public, subsets as subsets
from sympy.utilities.iterables import is_sequence as is_sequence
from sympy.utilities.magic import pollute as pollute

def ring(symbols, domain, order=...):
    '''Construct a polynomial ring returning ``(ring, x_1, ..., x_n)``.

    Parameters
    ==========

    symbols : str
        Symbol/Expr or sequence of str, Symbol/Expr (non-empty)
    domain : :class:`~.Domain` or coercible
    order : :class:`~.MonomialOrder` or coercible, optional, defaults to ``lex``

    Examples
    ========

    >>> from sympy.polys.rings import ring
    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.orderings import lex

    >>> R, x, y, z = ring("x,y,z", ZZ, lex)
    >>> R
    Polynomial ring in x, y, z over ZZ with lex order
    >>> x + y + z
    x + y + z
    >>> type(_)
    <class \'sympy.polys.rings.PolyElement\'>

    '''
def xring(symbols, domain, order=...):
    '''Construct a polynomial ring returning ``(ring, (x_1, ..., x_n))``.

    Parameters
    ==========

    symbols : str
        Symbol/Expr or sequence of str, Symbol/Expr (non-empty)
    domain : :class:`~.Domain` or coercible
    order : :class:`~.MonomialOrder` or coercible, optional, defaults to ``lex``

    Examples
    ========

    >>> from sympy.polys.rings import xring
    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.orderings import lex

    >>> R, (x, y, z) = xring("x,y,z", ZZ, lex)
    >>> R
    Polynomial ring in x, y, z over ZZ with lex order
    >>> x + y + z
    x + y + z
    >>> type(_)
    <class \'sympy.polys.rings.PolyElement\'>

    '''
def vring(symbols, domain, order=...):
    '''Construct a polynomial ring and inject ``x_1, ..., x_n`` into the global namespace.

    Parameters
    ==========

    symbols : str
        Symbol/Expr or sequence of str, Symbol/Expr (non-empty)
    domain : :class:`~.Domain` or coercible
    order : :class:`~.MonomialOrder` or coercible, optional, defaults to ``lex``

    Examples
    ========

    >>> from sympy.polys.rings import vring
    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.orderings import lex

    >>> vring("x,y,z", ZZ, lex)
    Polynomial ring in x, y, z over ZZ with lex order
    >>> x + y + z # noqa:
    x + y + z
    >>> type(_)
    <class \'sympy.polys.rings.PolyElement\'>

    '''
def sring(exprs, *symbols, **options):
    '''Construct a ring deriving generators and domain from options and input expressions.

    Parameters
    ==========

    exprs : :class:`~.Expr` or sequence of :class:`~.Expr` (sympifiable)
    symbols : sequence of :class:`~.Symbol`/:class:`~.Expr`
    options : keyword arguments understood by :class:`~.Options`

    Examples
    ========

    >>> from sympy import sring, symbols

    >>> x, y, z = symbols("x,y,z")
    >>> R, f = sring(x + 2*y + 3*z)
    >>> R
    Polynomial ring in x, y, z over ZZ with lex order
    >>> f
    x + 2*y + 3*z
    >>> type(_)
    <class \'sympy.polys.rings.PolyElement\'>

    '''

class PolyRing(DefaultPrinting, IPolys):
    """Multivariate distributed polynomial ring. """
    def __new__(cls, symbols, domain, order=...): ...
    def __getnewargs__(self): ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def clone(self, symbols: Incomplete | None = None, domain: Incomplete | None = None, order: Incomplete | None = None): ...
    def monomial_basis(self, i):
        """Return the ith-basis element. """
    @property
    def zero(self): ...
    @property
    def one(self): ...
    def domain_new(self, element, orig_domain: Incomplete | None = None): ...
    def ground_new(self, coeff): ...
    def term_new(self, monom, coeff): ...
    def ring_new(self, element): ...
    __call__ = ring_new
    def from_dict(self, element, orig_domain: Incomplete | None = None): ...
    def from_terms(self, element, orig_domain: Incomplete | None = None): ...
    def from_list(self, element): ...
    def from_expr(self, expr): ...
    def index(self, gen):
        """Compute index of ``gen`` in ``self.gens``. """
    def drop(self, *gens):
        """Remove specified generators from this ring. """
    def __getitem__(self, key): ...
    def to_ground(self): ...
    def to_domain(self): ...
    def to_field(self): ...
    @property
    def is_univariate(self): ...
    @property
    def is_multivariate(self): ...
    def add(self, *objs):
        '''
        Add a sequence of polynomials or containers of polynomials.

        Examples
        ========

        >>> from sympy.polys.rings import ring
        >>> from sympy.polys.domains import ZZ

        >>> R, x = ring("x", ZZ)
        >>> R.add([ x**2 + 2*i + 3 for i in range(4) ])
        4*x**2 + 24
        >>> _.factor_list()
        (4, [(x**2 + 6, 1)])

        '''
    def mul(self, *objs):
        '''
        Multiply a sequence of polynomials or containers of polynomials.

        Examples
        ========

        >>> from sympy.polys.rings import ring
        >>> from sympy.polys.domains import ZZ

        >>> R, x = ring("x", ZZ)
        >>> R.mul([ x**2 + 2*i + 3 for i in range(4) ])
        x**8 + 24*x**6 + 206*x**4 + 744*x**2 + 945
        >>> _.factor_list()
        (1, [(x**2 + 3, 1), (x**2 + 5, 1), (x**2 + 7, 1), (x**2 + 9, 1)])

        '''
    def drop_to_ground(self, *gens):
        """
        Remove specified generators from the ring and inject them into
        its domain.
        """
    def compose(self, other):
        """Add the generators of ``other`` to ``self``"""
    def add_gens(self, symbols):
        """Add the elements of ``symbols`` as generators to ``self``"""
    def symmetric_poly(self, n):
        """
        Return the elementary symmetric polynomial of degree *n* over
        this ring's generators.
        """

class PolyElement(DomainElement, DefaultPrinting, CantSympify, dict):
    """Element of multivariate distributed polynomial ring. """
    def new(self, init): ...
    def parent(self): ...
    def __getnewargs__(self): ...
    def __hash__(self): ...
    def copy(self):
        """Return a copy of polynomial self.

        Polynomials are mutable; if one is interested in preserving
        a polynomial, and one plans to use inplace operations, one
        can copy the polynomial. This method makes a shallow copy.

        Examples
        ========

        >>> from sympy.polys.domains import ZZ
        >>> from sympy.polys.rings import ring

        >>> R, x, y = ring('x, y', ZZ)
        >>> p = (x + y)**2
        >>> p1 = p.copy()
        >>> p2 = p
        >>> p[R.zero_monom] = 3
        >>> p
        x**2 + 2*x*y + y**2 + 3
        >>> p1
        x**2 + 2*x*y + y**2
        >>> p2
        x**2 + 2*x*y + y**2 + 3

        """
    def set_ring(self, new_ring): ...
    def as_expr(self, *symbols): ...
    def as_expr_dict(self): ...
    def clear_denoms(self): ...
    def strip_zero(self) -> None:
        """Eliminate monomials with zero coefficient. """
    def __eq__(p1, p2):
        """Equality test for polynomials.

        Examples
        ========

        >>> from sympy.polys.domains import ZZ
        >>> from sympy.polys.rings import ring

        >>> _, x, y = ring('x, y', ZZ)
        >>> p1 = (x + y)**2 + (x - y)**2
        >>> p1 == 4*x*y
        False
        >>> p1 == 2*(x**2 + y**2)
        True

        """
    def __ne__(p1, p2): ...
    def almosteq(p1, p2, tolerance: Incomplete | None = None):
        """Approximate equality test for polynomials. """
    def sort_key(self): ...
    def __lt__(p1, p2): ...
    def __le__(p1, p2): ...
    def __gt__(p1, p2): ...
    def __ge__(p1, p2): ...
    def drop(self, gen): ...
    def drop_to_ground(self, gen): ...
    def to_dense(self): ...
    def to_dict(self): ...
    def str(self, printer, precedence, exp_pattern, mul_symbol): ...
    @property
    def is_generator(self): ...
    @property
    def is_ground(self): ...
    @property
    def is_monomial(self): ...
    @property
    def is_term(self): ...
    @property
    def is_negative(self): ...
    @property
    def is_positive(self): ...
    @property
    def is_nonnegative(self): ...
    @property
    def is_nonpositive(self): ...
    @property
    def is_zero(f): ...
    @property
    def is_one(f): ...
    @property
    def is_monic(f): ...
    @property
    def is_primitive(f): ...
    @property
    def is_linear(f): ...
    @property
    def is_quadratic(f): ...
    @property
    def is_squarefree(f): ...
    @property
    def is_irreducible(f): ...
    @property
    def is_cyclotomic(f): ...
    def __neg__(self): ...
    def __pos__(self): ...
    def __add__(p1, p2):
        """Add two polynomials.

        Examples
        ========

        >>> from sympy.polys.domains import ZZ
        >>> from sympy.polys.rings import ring

        >>> _, x, y = ring('x, y', ZZ)
        >>> (x + y)**2 + (x - y)**2
        2*x**2 + 2*y**2

        """
    def __radd__(p1, n): ...
    def __sub__(p1, p2):
        """Subtract polynomial p2 from p1.

        Examples
        ========

        >>> from sympy.polys.domains import ZZ
        >>> from sympy.polys.rings import ring

        >>> _, x, y = ring('x, y', ZZ)
        >>> p1 = x + y**2
        >>> p2 = x*y + y**2
        >>> p1 - p2
        -x*y + x

        """
    def __rsub__(p1, n):
        """n - p1 with n convertible to the coefficient domain.

        Examples
        ========

        >>> from sympy.polys.domains import ZZ
        >>> from sympy.polys.rings import ring

        >>> _, x, y = ring('x, y', ZZ)
        >>> p = x + y
        >>> 4 - p
        -x - y + 4

        """
    def __mul__(p1, p2):
        """Multiply two polynomials.

        Examples
        ========

        >>> from sympy.polys.domains import QQ
        >>> from sympy.polys.rings import ring

        >>> _, x, y = ring('x, y', QQ)
        >>> p1 = x + y
        >>> p2 = x - y
        >>> p1*p2
        x**2 - y**2

        """
    def __rmul__(p1, p2):
        """p2 * p1 with p2 in the coefficient domain of p1.

        Examples
        ========

        >>> from sympy.polys.domains import ZZ
        >>> from sympy.polys.rings import ring

        >>> _, x, y = ring('x, y', ZZ)
        >>> p = x + y
        >>> 4 * p
        4*x + 4*y

        """
    def __pow__(self, n):
        """raise polynomial to power `n`

        Examples
        ========

        >>> from sympy.polys.domains import ZZ
        >>> from sympy.polys.rings import ring

        >>> _, x, y = ring('x, y', ZZ)
        >>> p = x + y**2
        >>> p**3
        x**3 + 3*x**2*y**2 + 3*x*y**4 + y**6

        """
    def square(self):
        """square of a polynomial

        Examples
        ========

        >>> from sympy.polys.rings import ring
        >>> from sympy.polys.domains import ZZ

        >>> _, x, y = ring('x, y', ZZ)
        >>> p = x + y**2
        >>> p.square()
        x**2 + 2*x*y**2 + y**4

        """
    def __divmod__(p1, p2): ...
    def __rdivmod__(p1, p2): ...
    def __mod__(p1, p2): ...
    def __rmod__(p1, p2): ...
    def __truediv__(p1, p2): ...
    def __rtruediv__(p1, p2): ...
    __floordiv__ = __truediv__
    __rfloordiv__ = __rtruediv__
    def div(self, fv):
        """Division algorithm, see [CLO] p64.

        fv array of polynomials
           return qv, r such that
           self = sum(fv[i]*qv[i]) + r

        All polynomials are required not to be Laurent polynomials.

        Examples
        ========

        >>> from sympy.polys.rings import ring
        >>> from sympy.polys.domains import ZZ

        >>> _, x, y = ring('x, y', ZZ)
        >>> f = x**3
        >>> f0 = x - y**2
        >>> f1 = x - y
        >>> qv, r = f.div((f0, f1))
        >>> qv[0]
        x**2 + x*y**2 + y**4
        >>> qv[1]
        0
        >>> r
        y**6

        """
    def rem(self, G): ...
    def quo(f, G): ...
    def exquo(f, G): ...
    def degree(f, x: Incomplete | None = None):
        """
        The leading degree in ``x`` or the main variable.

        Note that the degree of 0 is negative infinity (the SymPy object -oo).

        """
    def degrees(f):
        """
        A tuple containing leading degrees in all variables.

        Note that the degree of 0 is negative infinity (the SymPy object -oo)

        """
    def tail_degree(f, x: Incomplete | None = None):
        """
        The tail degree in ``x`` or the main variable.

        Note that the degree of 0 is negative infinity (the SymPy object -oo)

        """
    def tail_degrees(f):
        """
        A tuple containing tail degrees in all variables.

        Note that the degree of 0 is negative infinity (the SymPy object -oo)

        """
    def leading_expv(self):
        """Leading monomial tuple according to the monomial ordering.

        Examples
        ========

        >>> from sympy.polys.rings import ring
        >>> from sympy.polys.domains import ZZ

        >>> _, x, y, z = ring('x, y, z', ZZ)
        >>> p = x**4 + x**3*y + x**2*z**2 + z**7
        >>> p.leading_expv()
        (4, 0, 0)

        """
    def coeff(self, element):
        '''
        Returns the coefficient that stands next to the given monomial.

        Parameters
        ==========

        element : PolyElement (with ``is_monomial = True``) or 1

        Examples
        ========

        >>> from sympy.polys.rings import ring
        >>> from sympy.polys.domains import ZZ

        >>> _, x, y, z = ring("x,y,z", ZZ)
        >>> f = 3*x**2*y - x*y*z + 7*z**3 + 23

        >>> f.coeff(x**2*y)
        3
        >>> f.coeff(x*y)
        0
        >>> f.coeff(1)
        23

        '''
    def const(self):
        """Returns the constant coefficient. """
    @property
    def LC(self): ...
    @property
    def LM(self): ...
    def leading_monom(self):
        """
        Leading monomial as a polynomial element.

        Examples
        ========

        >>> from sympy.polys.rings import ring
        >>> from sympy.polys.domains import ZZ

        >>> _, x, y = ring('x, y', ZZ)
        >>> (3*x*y + y**2).leading_monom()
        x*y

        """
    @property
    def LT(self): ...
    def leading_term(self):
        """Leading term as a polynomial element.

        Examples
        ========

        >>> from sympy.polys.rings import ring
        >>> from sympy.polys.domains import ZZ

        >>> _, x, y = ring('x, y', ZZ)
        >>> (3*x*y + y**2).leading_term()
        3*x*y

        """
    def coeffs(self, order: Incomplete | None = None):
        '''Ordered list of polynomial coefficients.

        Parameters
        ==========

        order : :class:`~.MonomialOrder` or coercible, optional

        Examples
        ========

        >>> from sympy.polys.rings import ring
        >>> from sympy.polys.domains import ZZ
        >>> from sympy.polys.orderings import lex, grlex

        >>> _, x, y = ring("x, y", ZZ, lex)
        >>> f = x*y**7 + 2*x**2*y**3

        >>> f.coeffs()
        [2, 1]
        >>> f.coeffs(grlex)
        [1, 2]

        '''
    def monoms(self, order: Incomplete | None = None):
        '''Ordered list of polynomial monomials.

        Parameters
        ==========

        order : :class:`~.MonomialOrder` or coercible, optional

        Examples
        ========

        >>> from sympy.polys.rings import ring
        >>> from sympy.polys.domains import ZZ
        >>> from sympy.polys.orderings import lex, grlex

        >>> _, x, y = ring("x, y", ZZ, lex)
        >>> f = x*y**7 + 2*x**2*y**3

        >>> f.monoms()
        [(2, 3), (1, 7)]
        >>> f.monoms(grlex)
        [(1, 7), (2, 3)]

        '''
    def terms(self, order: Incomplete | None = None):
        '''Ordered list of polynomial terms.

        Parameters
        ==========

        order : :class:`~.MonomialOrder` or coercible, optional

        Examples
        ========

        >>> from sympy.polys.rings import ring
        >>> from sympy.polys.domains import ZZ
        >>> from sympy.polys.orderings import lex, grlex

        >>> _, x, y = ring("x, y", ZZ, lex)
        >>> f = x*y**7 + 2*x**2*y**3

        >>> f.terms()
        [((2, 3), 2), ((1, 7), 1)]
        >>> f.terms(grlex)
        [((1, 7), 1), ((2, 3), 2)]

        '''
    def itercoeffs(self):
        """Iterator over coefficients of a polynomial. """
    def itermonoms(self):
        """Iterator over monomials of a polynomial. """
    def iterterms(self):
        """Iterator over terms of a polynomial. """
    def listcoeffs(self):
        """Unordered list of polynomial coefficients. """
    def listmonoms(self):
        """Unordered list of polynomial monomials. """
    def listterms(self):
        """Unordered list of polynomial terms. """
    def imul_num(p, c):
        """multiply inplace the polynomial p by an element in the
        coefficient ring, provided p is not one of the generators;
        else multiply not inplace

        Examples
        ========

        >>> from sympy.polys.rings import ring
        >>> from sympy.polys.domains import ZZ

        >>> _, x, y = ring('x, y', ZZ)
        >>> p = x + y**2
        >>> p1 = p.imul_num(3)
        >>> p1
        3*x + 3*y**2
        >>> p1 is p
        True
        >>> p = x
        >>> p1 = p.imul_num(3)
        >>> p1
        3*x
        >>> p1 is p
        False

        """
    def content(f):
        """Returns GCD of polynomial's coefficients. """
    def primitive(f):
        """Returns content and a primitive polynomial. """
    def monic(f):
        """Divides all coefficients by the leading coefficient. """
    def mul_ground(f, x): ...
    def mul_monom(f, monom): ...
    def mul_term(f, term): ...
    def quo_ground(f, x): ...
    def quo_term(f, term): ...
    def trunc_ground(f, p): ...
    rem_ground = trunc_ground
    def extract_ground(self, g): ...
    def max_norm(f): ...
    def l1_norm(f): ...
    def deflate(f, *G): ...
    def inflate(f, J): ...
    def lcm(self, g): ...
    def gcd(f, g): ...
    def cofactors(f, g): ...
    def cancel(self, g):
        '''
        Cancel common factors in a rational function ``f/g``.

        Examples
        ========

        >>> from sympy.polys import ring, ZZ
        >>> R, x,y = ring("x,y", ZZ)

        >>> (2*x**2 - 2).cancel(x**2 - 2*x + 1)
        (2*x + 2, x - 1)

        '''
    def canonical_unit(f): ...
    def diff(f, x):
        '''Computes partial derivative in ``x``.

        Examples
        ========

        >>> from sympy.polys.rings import ring
        >>> from sympy.polys.domains import ZZ

        >>> _, x, y = ring("x,y", ZZ)
        >>> p = x + x**2*y**3
        >>> p.diff(x)
        2*x*y**3 + 1

        '''
    def __call__(f, *values): ...
    def evaluate(self, x, a: Incomplete | None = None): ...
    def subs(self, x, a: Incomplete | None = None): ...
    def symmetrize(self):
        '''
        Rewrite *self* in terms of elementary symmetric polynomials.

        Explanation
        ===========

        If this :py:class:`~.PolyElement` belongs to a ring of $n$ variables,
        we can try to write it as a function of the elementary symmetric
        polynomials on $n$ variables. We compute a symmetric part, and a
        remainder for any part we were not able to symmetrize.

        Examples
        ========

        >>> from sympy.polys.rings import ring
        >>> from sympy.polys.domains import ZZ
        >>> R, x, y = ring("x,y", ZZ)

        >>> f = x**2 + y**2
        >>> f.symmetrize()
        (x**2 - 2*y, 0, [(x, x + y), (y, x*y)])

        >>> f = x**2 - y**2
        >>> f.symmetrize()
        (x**2 - 2*y, -2*y**2, [(x, x + y), (y, x*y)])

        Returns
        =======

        Triple ``(p, r, m)``
            ``p`` is a :py:class:`~.PolyElement` that represents our attempt
            to express *self* as a function of elementary symmetric
            polynomials. Each variable in ``p`` stands for one of the
            elementary symmetric polynomials. The correspondence is given
            by ``m``.

            ``r`` is the remainder.

            ``m`` is a list of pairs, giving the mapping from variables in
            ``p`` to elementary symmetric polynomials.

            The triple satisfies the equation ``p.compose(m) + r == self``.
            If the remainder ``r`` is zero, *self* is symmetric. If it is
            nonzero, we were not able to represent *self* as symmetric.

        See Also
        ========

        sympy.polys.polyfuncs.symmetrize

        References
        ==========

        .. [1] Lauer, E. Algorithms for symmetrical polynomials, Proc. 1976
            ACM Symp. on Symbolic and Algebraic Computing, NY 242-247.
            https://dl.acm.org/doi/pdf/10.1145/800205.806342

        '''
    def compose(f, x, a: Incomplete | None = None): ...
    def pdiv(f, g): ...
    def prem(f, g): ...
    def pquo(f, g): ...
    def pexquo(f, g): ...
    def half_gcdex(f, g): ...
    def gcdex(f, g): ...
    def subresultants(f, g): ...
    def resultant(f, g): ...
    def discriminant(f): ...
    def decompose(f): ...
    def shift(f, a): ...
    def sturm(f): ...
    def gff_list(f): ...
    def sqf_norm(f): ...
    def sqf_part(f): ...
    def sqf_list(f, all: bool = False): ...
    def factor_list(f): ...
