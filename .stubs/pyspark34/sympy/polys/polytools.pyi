from _typeshed import Incomplete
from sympy.core import Add as Add, Expr as Expr, S as S, Tuple as Tuple
from sympy.core.basic import Basic as Basic
from sympy.core.evalf import evalf as evalf, fastlog as fastlog, pure_complex as pure_complex, quad_to_mpmath as quad_to_mpmath
from sympy.core.exprtools import Factors as Factors, factor_nc as factor_nc, factor_terms as factor_terms
from sympy.core.function import Derivative as Derivative
from sympy.core.mul import Mul as Mul
from sympy.core.numbers import I as I, Integer as Integer, equal_valued as equal_valued, ilcm as ilcm
from sympy.core.relational import Equality as Equality, Relational as Relational
from sympy.core.sorting import ordered as ordered
from sympy.core.symbol import Dummy as Dummy, Symbol as Symbol
from sympy.core.sympify import sympify as sympify
from sympy.core.traversal import bottom_up as bottom_up, preorder_traversal as preorder_traversal
from sympy.logic.boolalg import BooleanAtom as BooleanAtom
from sympy.polys.constructor import construct_domain as construct_domain
from sympy.polys.domains import FF as FF, QQ as QQ, ZZ as ZZ
from sympy.polys.domains.domainelement import DomainElement as DomainElement
from sympy.polys.fglmtools import matrix_fglm as matrix_fglm
from sympy.polys.monomials import Monomial as Monomial
from sympy.polys.orderings import monomial_key as monomial_key
from sympy.polys.polyclasses import ANP as ANP, DMF as DMF, DMP as DMP
from sympy.polys.polyerrors import CoercionFailed as CoercionFailed, ComputationFailed as ComputationFailed, DomainError as DomainError, ExactQuotientFailed as ExactQuotientFailed, GeneratorsError as GeneratorsError, GeneratorsNeeded as GeneratorsNeeded, MultivariatePolynomialError as MultivariatePolynomialError, OperationNotSupported as OperationNotSupported, PolificationFailed as PolificationFailed, PolynomialError as PolynomialError, UnificationFailed as UnificationFailed
from sympy.polys.polyutils import basic_from_dict as basic_from_dict
from sympy.polys.rationaltools import together as together
from sympy.polys.rootisolation import dup_isolate_real_roots_list as dup_isolate_real_roots_list
from sympy.utilities import filldedent as filldedent, group as group, public as public
from sympy.utilities.exceptions import sympy_deprecation_warning as sympy_deprecation_warning
from sympy.utilities.iterables import iterable as iterable, sift as sift

class Poly(Basic):
    """
    Generic class for representing and operating on polynomial expressions.

    See :ref:`polys-docs` for general documentation.

    Poly is a subclass of Basic rather than Expr but instances can be
    converted to Expr with the :py:meth:`~.Poly.as_expr` method.

    .. deprecated:: 1.6

       Combining Poly with non-Poly objects in binary operations is
       deprecated. Explicitly convert both objects to either Poly or Expr
       first. See :ref:`deprecated-poly-nonpoly-binary-operations`.

    Examples
    ========

    >>> from sympy import Poly
    >>> from sympy.abc import x, y

    Create a univariate polynomial:

    >>> Poly(x*(x**2 + x - 1)**2)
    Poly(x**5 + 2*x**4 - x**3 - 2*x**2 + x, x, domain='ZZ')

    Create a univariate polynomial with specific domain:

    >>> from sympy import sqrt
    >>> Poly(x**2 + 2*x + sqrt(3), domain='R')
    Poly(1.0*x**2 + 2.0*x + 1.73205080756888, x, domain='RR')

    Create a multivariate polynomial:

    >>> Poly(y*x**2 + x*y + 1)
    Poly(x**2*y + x*y + 1, x, y, domain='ZZ')

    Create a univariate polynomial, where y is a constant:

    >>> Poly(y*x**2 + x*y + 1,x)
    Poly(y*x**2 + y*x + 1, x, domain='ZZ[y]')

    You can evaluate the above polynomial as a function of y:

    >>> Poly(y*x**2 + x*y + 1,x).eval(2)
    6*y + 1

    See Also
    ========

    sympy.core.expr.Expr

    """
    is_commutative: bool
    is_Poly: bool
    def __new__(cls, rep, *gens, **args):
        """Create a new polynomial instance out of something useful. """
    @classmethod
    def new(cls, rep, *gens):
        """Construct :class:`Poly` instance from raw representation. """
    @property
    def expr(self): ...
    @property
    def args(self): ...
    @classmethod
    def from_dict(cls, rep, *gens, **args):
        """Construct a polynomial from a ``dict``. """
    @classmethod
    def from_list(cls, rep, *gens, **args):
        """Construct a polynomial from a ``list``. """
    @classmethod
    def from_poly(cls, rep, *gens, **args):
        """Construct a polynomial from a polynomial. """
    @classmethod
    def from_expr(cls, rep, *gens, **args):
        """Construct a polynomial from an expression. """
    def __hash__(self): ...
    @property
    def free_symbols(self):
        """
        Free symbols of a polynomial expression.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x, y, z

        >>> Poly(x**2 + 1).free_symbols
        {x}
        >>> Poly(x**2 + y).free_symbols
        {x, y}
        >>> Poly(x**2 + y, x).free_symbols
        {x, y}
        >>> Poly(x**2 + y, x, z).free_symbols
        {x, y}

        """
    @property
    def free_symbols_in_domain(self):
        """
        Free symbols of the domain of ``self``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x, y

        >>> Poly(x**2 + 1).free_symbols_in_domain
        set()
        >>> Poly(x**2 + y).free_symbols_in_domain
        set()
        >>> Poly(x**2 + y, x).free_symbols_in_domain
        {y}

        """
    @property
    def gen(self):
        """
        Return the principal generator.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(x**2 + 1, x).gen
        x

        """
    @property
    def domain(self):
        """Get the ground domain of a :py:class:`~.Poly`

        Returns
        =======

        :py:class:`~.Domain`:
            Ground domain of the :py:class:`~.Poly`.

        Examples
        ========

        >>> from sympy import Poly, Symbol
        >>> x = Symbol('x')
        >>> p = Poly(x**2 + x)
        >>> p
        Poly(x**2 + x, x, domain='ZZ')
        >>> p.domain
        ZZ
        """
    @property
    def zero(self):
        """Return zero polynomial with ``self``'s properties. """
    @property
    def one(self):
        """Return one polynomial with ``self``'s properties. """
    @property
    def unit(self):
        """Return unit polynomial with ``self``'s properties. """
    def unify(f, g):
        """
        Make ``f`` and ``g`` belong to the same domain.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> f, g = Poly(x/2 + 1), Poly(2*x + 1)

        >>> f
        Poly(1/2*x + 1, x, domain='QQ')
        >>> g
        Poly(2*x + 1, x, domain='ZZ')

        >>> F, G = f.unify(g)

        >>> F
        Poly(1/2*x + 1, x, domain='QQ')
        >>> G
        Poly(2*x + 1, x, domain='QQ')

        """
    def per(f, rep, gens: Incomplete | None = None, remove: Incomplete | None = None):
        """
        Create a Poly out of the given representation.

        Examples
        ========

        >>> from sympy import Poly, ZZ
        >>> from sympy.abc import x, y

        >>> from sympy.polys.polyclasses import DMP

        >>> a = Poly(x**2 + 1)

        >>> a.per(DMP([ZZ(1), ZZ(1)], ZZ), gens=[y])
        Poly(y + 1, y, domain='ZZ')

        """
    def set_domain(f, domain):
        """Set the ground domain of ``f``. """
    def get_domain(f):
        """Get the ground domain of ``f``. """
    def set_modulus(f, modulus):
        """
        Set the modulus of ``f``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(5*x**2 + 2*x - 1, x).set_modulus(2)
        Poly(x**2 + 1, x, modulus=2)

        """
    def get_modulus(f):
        """
        Get the modulus of ``f``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(x**2 + 1, modulus=2).get_modulus()
        2

        """
    def exclude(f):
        """
        Remove unnecessary generators from ``f``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import a, b, c, d, x

        >>> Poly(a + x, a, b, c, d, x).exclude()
        Poly(a + x, a, x, domain='ZZ')

        """
    def replace(f, x, y: Incomplete | None = None, **_ignore):
        """
        Replace ``x`` with ``y`` in generators list.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x, y

        >>> Poly(x**2 + 1, x).replace(x, y)
        Poly(y**2 + 1, y, domain='ZZ')

        """
    def match(f, *args, **kwargs):
        """Match expression from Poly. See Basic.match()"""
    def reorder(f, *gens, **args):
        """
        Efficiently apply new order of generators.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x, y

        >>> Poly(x**2 + x*y**2, x, y).reorder(y, x)
        Poly(y**2*x + x**2, y, x, domain='ZZ')

        """
    def ltrim(f, gen):
        """
        Remove dummy generators from ``f`` that are to the left of
        specified ``gen`` in the generators as ordered. When ``gen``
        is an integer, it refers to the generator located at that
        position within the tuple of generators of ``f``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x, y, z

        >>> Poly(y**2 + y*z**2, x, y, z).ltrim(y)
        Poly(y**2 + y*z**2, y, z, domain='ZZ')
        >>> Poly(z, x, y, z).ltrim(-1)
        Poly(z, z, domain='ZZ')

        """
    def has_only_gens(f, *gens):
        """
        Return ``True`` if ``Poly(f, *gens)`` retains ground domain.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x, y, z

        >>> Poly(x*y + 1, x, y, z).has_only_gens(x, y)
        True
        >>> Poly(x*y + z, x, y, z).has_only_gens(x, y)
        False

        """
    def to_ring(f):
        """
        Make the ground domain a ring.

        Examples
        ========

        >>> from sympy import Poly, QQ
        >>> from sympy.abc import x

        >>> Poly(x**2 + 1, domain=QQ).to_ring()
        Poly(x**2 + 1, x, domain='ZZ')

        """
    def to_field(f):
        """
        Make the ground domain a field.

        Examples
        ========

        >>> from sympy import Poly, ZZ
        >>> from sympy.abc import x

        >>> Poly(x**2 + 1, x, domain=ZZ).to_field()
        Poly(x**2 + 1, x, domain='QQ')

        """
    def to_exact(f):
        """
        Make the ground domain exact.

        Examples
        ========

        >>> from sympy import Poly, RR
        >>> from sympy.abc import x

        >>> Poly(x**2 + 1.0, x, domain=RR).to_exact()
        Poly(x**2 + 1, x, domain='QQ')

        """
    def retract(f, field: Incomplete | None = None):
        """
        Recalculate the ground domain of a polynomial.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> f = Poly(x**2 + 1, x, domain='QQ[y]')
        >>> f
        Poly(x**2 + 1, x, domain='QQ[y]')

        >>> f.retract()
        Poly(x**2 + 1, x, domain='ZZ')
        >>> f.retract(field=True)
        Poly(x**2 + 1, x, domain='QQ')

        """
    def slice(f, x, m, n: Incomplete | None = None):
        """Take a continuous subsequence of terms of ``f``. """
    def coeffs(f, order: Incomplete | None = None):
        """
        Returns all non-zero coefficients from ``f`` in lex order.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(x**3 + 2*x + 3, x).coeffs()
        [1, 2, 3]

        See Also
        ========
        all_coeffs
        coeff_monomial
        nth

        """
    def monoms(f, order: Incomplete | None = None):
        """
        Returns all non-zero monomials from ``f`` in lex order.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x, y

        >>> Poly(x**2 + 2*x*y**2 + x*y + 3*y, x, y).monoms()
        [(2, 0), (1, 2), (1, 1), (0, 1)]

        See Also
        ========
        all_monoms

        """
    def terms(f, order: Incomplete | None = None):
        """
        Returns all non-zero terms from ``f`` in lex order.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x, y

        >>> Poly(x**2 + 2*x*y**2 + x*y + 3*y, x, y).terms()
        [((2, 0), 1), ((1, 2), 2), ((1, 1), 1), ((0, 1), 3)]

        See Also
        ========
        all_terms

        """
    def all_coeffs(f):
        """
        Returns all coefficients from a univariate polynomial ``f``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(x**3 + 2*x - 1, x).all_coeffs()
        [1, 0, 2, -1]

        """
    def all_monoms(f):
        """
        Returns all monomials from a univariate polynomial ``f``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(x**3 + 2*x - 1, x).all_monoms()
        [(3,), (2,), (1,), (0,)]

        See Also
        ========
        all_terms

        """
    def all_terms(f):
        """
        Returns all terms from a univariate polynomial ``f``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(x**3 + 2*x - 1, x).all_terms()
        [((3,), 1), ((2,), 0), ((1,), 2), ((0,), -1)]

        """
    def termwise(f, func, *gens, **args):
        """
        Apply a function to all terms of ``f``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> def func(k, coeff):
        ...     k = k[0]
        ...     return coeff//10**(2-k)

        >>> Poly(x**2 + 20*x + 400).termwise(func)
        Poly(x**2 + 2*x + 4, x, domain='ZZ')

        """
    def length(f):
        """
        Returns the number of non-zero terms in ``f``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(x**2 + 2*x - 1).length()
        3

        """
    def as_dict(f, native: bool = False, zero: bool = False):
        """
        Switch to a ``dict`` representation.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x, y

        >>> Poly(x**2 + 2*x*y**2 - y, x, y).as_dict()
        {(0, 1): -1, (1, 2): 2, (2, 0): 1}

        """
    def as_list(f, native: bool = False):
        """Switch to a ``list`` representation. """
    def as_expr(f, *gens):
        """
        Convert a Poly instance to an Expr instance.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x, y

        >>> f = Poly(x**2 + 2*x*y**2 - y, x, y)

        >>> f.as_expr()
        x**2 + 2*x*y**2 - y
        >>> f.as_expr({x: 5})
        10*y**2 - y + 25
        >>> f.as_expr(5, 6)
        379

        """
    def as_poly(self, *gens, **args):
        """Converts ``self`` to a polynomial or returns ``None``.

        >>> from sympy import sin
        >>> from sympy.abc import x, y

        >>> print((x**2 + x*y).as_poly())
        Poly(x**2 + x*y, x, y, domain='ZZ')

        >>> print((x**2 + x*y).as_poly(x, y))
        Poly(x**2 + x*y, x, y, domain='ZZ')

        >>> print((x**2 + sin(y)).as_poly(x, y))
        None

        """
    def lift(f):
        """
        Convert algebraic coefficients to rationals.

        Examples
        ========

        >>> from sympy import Poly, I
        >>> from sympy.abc import x

        >>> Poly(x**2 + I*x + 1, x, extension=I).lift()
        Poly(x**4 + 3*x**2 + 1, x, domain='QQ')

        """
    def deflate(f):
        """
        Reduce degree of ``f`` by mapping ``x_i**m`` to ``y_i``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x, y

        >>> Poly(x**6*y**2 + x**3 + 1, x, y).deflate()
        ((3, 2), Poly(x**2*y + x + 1, x, y, domain='ZZ'))

        """
    def inject(f, front: bool = False):
        """
        Inject ground domain generators into ``f``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x, y

        >>> f = Poly(x**2*y + x*y**3 + x*y + 1, x)

        >>> f.inject()
        Poly(x**2*y + x*y**3 + x*y + 1, x, y, domain='ZZ')
        >>> f.inject(front=True)
        Poly(y**3*x + y*x**2 + y*x + 1, y, x, domain='ZZ')

        """
    def eject(f, *gens):
        """
        Eject selected generators into the ground domain.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x, y

        >>> f = Poly(x**2*y + x*y**3 + x*y + 1, x, y)

        >>> f.eject(x)
        Poly(x*y**3 + (x**2 + x)*y + 1, y, domain='ZZ[x]')
        >>> f.eject(y)
        Poly(y*x**2 + (y**3 + y)*x + 1, x, domain='ZZ[y]')

        """
    def terms_gcd(f):
        """
        Remove GCD of terms from the polynomial ``f``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x, y

        >>> Poly(x**6*y**2 + x**3*y, x, y).terms_gcd()
        ((3, 1), Poly(x**3*y + 1, x, y, domain='ZZ'))

        """
    def add_ground(f, coeff):
        """
        Add an element of the ground domain to ``f``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(x + 1).add_ground(2)
        Poly(x + 3, x, domain='ZZ')

        """
    def sub_ground(f, coeff):
        """
        Subtract an element of the ground domain from ``f``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(x + 1).sub_ground(2)
        Poly(x - 1, x, domain='ZZ')

        """
    def mul_ground(f, coeff):
        """
        Multiply ``f`` by a an element of the ground domain.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(x + 1).mul_ground(2)
        Poly(2*x + 2, x, domain='ZZ')

        """
    def quo_ground(f, coeff):
        """
        Quotient of ``f`` by a an element of the ground domain.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(2*x + 4).quo_ground(2)
        Poly(x + 2, x, domain='ZZ')

        >>> Poly(2*x + 3).quo_ground(2)
        Poly(x + 1, x, domain='ZZ')

        """
    def exquo_ground(f, coeff):
        """
        Exact quotient of ``f`` by a an element of the ground domain.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(2*x + 4).exquo_ground(2)
        Poly(x + 2, x, domain='ZZ')

        >>> Poly(2*x + 3).exquo_ground(2)
        Traceback (most recent call last):
        ...
        ExactQuotientFailed: 2 does not divide 3 in ZZ

        """
    def abs(f):
        """
        Make all coefficients in ``f`` positive.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(x**2 - 1, x).abs()
        Poly(x**2 + 1, x, domain='ZZ')

        """
    def neg(f):
        """
        Negate all coefficients in ``f``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(x**2 - 1, x).neg()
        Poly(-x**2 + 1, x, domain='ZZ')

        >>> -Poly(x**2 - 1, x)
        Poly(-x**2 + 1, x, domain='ZZ')

        """
    def add(f, g):
        """
        Add two polynomials ``f`` and ``g``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(x**2 + 1, x).add(Poly(x - 2, x))
        Poly(x**2 + x - 1, x, domain='ZZ')

        >>> Poly(x**2 + 1, x) + Poly(x - 2, x)
        Poly(x**2 + x - 1, x, domain='ZZ')

        """
    def sub(f, g):
        """
        Subtract two polynomials ``f`` and ``g``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(x**2 + 1, x).sub(Poly(x - 2, x))
        Poly(x**2 - x + 3, x, domain='ZZ')

        >>> Poly(x**2 + 1, x) - Poly(x - 2, x)
        Poly(x**2 - x + 3, x, domain='ZZ')

        """
    def mul(f, g):
        """
        Multiply two polynomials ``f`` and ``g``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(x**2 + 1, x).mul(Poly(x - 2, x))
        Poly(x**3 - 2*x**2 + x - 2, x, domain='ZZ')

        >>> Poly(x**2 + 1, x)*Poly(x - 2, x)
        Poly(x**3 - 2*x**2 + x - 2, x, domain='ZZ')

        """
    def sqr(f):
        """
        Square a polynomial ``f``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(x - 2, x).sqr()
        Poly(x**2 - 4*x + 4, x, domain='ZZ')

        >>> Poly(x - 2, x)**2
        Poly(x**2 - 4*x + 4, x, domain='ZZ')

        """
    def pow(f, n):
        """
        Raise ``f`` to a non-negative power ``n``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(x - 2, x).pow(3)
        Poly(x**3 - 6*x**2 + 12*x - 8, x, domain='ZZ')

        >>> Poly(x - 2, x)**3
        Poly(x**3 - 6*x**2 + 12*x - 8, x, domain='ZZ')

        """
    def pdiv(f, g):
        """
        Polynomial pseudo-division of ``f`` by ``g``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(x**2 + 1, x).pdiv(Poly(2*x - 4, x))
        (Poly(2*x + 4, x, domain='ZZ'), Poly(20, x, domain='ZZ'))

        """
    def prem(f, g):
        """
        Polynomial pseudo-remainder of ``f`` by ``g``.

        Caveat: The function prem(f, g, x) can be safely used to compute
          in Z[x] _only_ subresultant polynomial remainder sequences (prs's).

          To safely compute Euclidean and Sturmian prs's in Z[x]
          employ anyone of the corresponding functions found in
          the module sympy.polys.subresultants_qq_zz. The functions
          in the module with suffix _pg compute prs's in Z[x] employing
          rem(f, g, x), whereas the functions with suffix _amv
          compute prs's in Z[x] employing rem_z(f, g, x).

          The function rem_z(f, g, x) differs from prem(f, g, x) in that
          to compute the remainder polynomials in Z[x] it premultiplies
          the divident times the absolute value of the leading coefficient
          of the divisor raised to the power degree(f, x) - degree(g, x) + 1.


        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(x**2 + 1, x).prem(Poly(2*x - 4, x))
        Poly(20, x, domain='ZZ')

        """
    def pquo(f, g):
        """
        Polynomial pseudo-quotient of ``f`` by ``g``.

        See the Caveat note in the function prem(f, g).

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(x**2 + 1, x).pquo(Poly(2*x - 4, x))
        Poly(2*x + 4, x, domain='ZZ')

        >>> Poly(x**2 - 1, x).pquo(Poly(2*x - 2, x))
        Poly(2*x + 2, x, domain='ZZ')

        """
    def pexquo(f, g):
        """
        Polynomial exact pseudo-quotient of ``f`` by ``g``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(x**2 - 1, x).pexquo(Poly(2*x - 2, x))
        Poly(2*x + 2, x, domain='ZZ')

        >>> Poly(x**2 + 1, x).pexquo(Poly(2*x - 4, x))
        Traceback (most recent call last):
        ...
        ExactQuotientFailed: 2*x - 4 does not divide x**2 + 1

        """
    def div(f, g, auto: bool = True):
        """
        Polynomial division with remainder of ``f`` by ``g``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(x**2 + 1, x).div(Poly(2*x - 4, x))
        (Poly(1/2*x + 1, x, domain='QQ'), Poly(5, x, domain='QQ'))

        >>> Poly(x**2 + 1, x).div(Poly(2*x - 4, x), auto=False)
        (Poly(0, x, domain='ZZ'), Poly(x**2 + 1, x, domain='ZZ'))

        """
    def rem(f, g, auto: bool = True):
        """
        Computes the polynomial remainder of ``f`` by ``g``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(x**2 + 1, x).rem(Poly(2*x - 4, x))
        Poly(5, x, domain='ZZ')

        >>> Poly(x**2 + 1, x).rem(Poly(2*x - 4, x), auto=False)
        Poly(x**2 + 1, x, domain='ZZ')

        """
    def quo(f, g, auto: bool = True):
        """
        Computes polynomial quotient of ``f`` by ``g``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(x**2 + 1, x).quo(Poly(2*x - 4, x))
        Poly(1/2*x + 1, x, domain='QQ')

        >>> Poly(x**2 - 1, x).quo(Poly(x - 1, x))
        Poly(x + 1, x, domain='ZZ')

        """
    def exquo(f, g, auto: bool = True):
        """
        Computes polynomial exact quotient of ``f`` by ``g``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(x**2 - 1, x).exquo(Poly(x - 1, x))
        Poly(x + 1, x, domain='ZZ')

        >>> Poly(x**2 + 1, x).exquo(Poly(2*x - 4, x))
        Traceback (most recent call last):
        ...
        ExactQuotientFailed: 2*x - 4 does not divide x**2 + 1

        """
    def degree(f, gen: int = 0):
        """
        Returns degree of ``f`` in ``x_j``.

        The degree of 0 is negative infinity.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x, y

        >>> Poly(x**2 + y*x + 1, x, y).degree()
        2
        >>> Poly(x**2 + y*x + y, x, y).degree(y)
        1
        >>> Poly(0, x).degree()
        -oo

        """
    def degree_list(f):
        """
        Returns a list of degrees of ``f``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x, y

        >>> Poly(x**2 + y*x + 1, x, y).degree_list()
        (2, 1)

        """
    def total_degree(f):
        """
        Returns the total degree of ``f``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x, y

        >>> Poly(x**2 + y*x + 1, x, y).total_degree()
        2
        >>> Poly(x + y**5, x, y).total_degree()
        5

        """
    def homogenize(f, s):
        """
        Returns the homogeneous polynomial of ``f``.

        A homogeneous polynomial is a polynomial whose all monomials with
        non-zero coefficients have the same total degree. If you only
        want to check if a polynomial is homogeneous, then use
        :func:`Poly.is_homogeneous`. If you want not only to check if a
        polynomial is homogeneous but also compute its homogeneous order,
        then use :func:`Poly.homogeneous_order`.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x, y, z

        >>> f = Poly(x**5 + 2*x**2*y**2 + 9*x*y**3)
        >>> f.homogenize(z)
        Poly(x**5 + 2*x**2*y**2*z + 9*x*y**3*z, x, y, z, domain='ZZ')

        """
    def homogeneous_order(f):
        """
        Returns the homogeneous order of ``f``.

        A homogeneous polynomial is a polynomial whose all monomials with
        non-zero coefficients have the same total degree. This degree is
        the homogeneous order of ``f``. If you only want to check if a
        polynomial is homogeneous, then use :func:`Poly.is_homogeneous`.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x, y

        >>> f = Poly(x**5 + 2*x**3*y**2 + 9*x*y**4)
        >>> f.homogeneous_order()
        5

        """
    def LC(f, order: Incomplete | None = None):
        """
        Returns the leading coefficient of ``f``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(4*x**3 + 2*x**2 + 3*x, x).LC()
        4

        """
    def TC(f):
        """
        Returns the trailing coefficient of ``f``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(x**3 + 2*x**2 + 3*x, x).TC()
        0

        """
    def EC(f, order: Incomplete | None = None):
        """
        Returns the last non-zero coefficient of ``f``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(x**3 + 2*x**2 + 3*x, x).EC()
        3

        """
    def coeff_monomial(f, monom):
        """
        Returns the coefficient of ``monom`` in ``f`` if there, else None.

        Examples
        ========

        >>> from sympy import Poly, exp
        >>> from sympy.abc import x, y

        >>> p = Poly(24*x*y*exp(8) + 23*x, x, y)

        >>> p.coeff_monomial(x)
        23
        >>> p.coeff_monomial(y)
        0
        >>> p.coeff_monomial(x*y)
        24*exp(8)

        Note that ``Expr.coeff()`` behaves differently, collecting terms
        if possible; the Poly must be converted to an Expr to use that
        method, however:

        >>> p.as_expr().coeff(x)
        24*y*exp(8) + 23
        >>> p.as_expr().coeff(y)
        24*x*exp(8)
        >>> p.as_expr().coeff(x*y)
        24*exp(8)

        See Also
        ========
        nth: more efficient query using exponents of the monomial's generators

        """
    def nth(f, *N):
        """
        Returns the ``n``-th coefficient of ``f`` where ``N`` are the
        exponents of the generators in the term of interest.

        Examples
        ========

        >>> from sympy import Poly, sqrt
        >>> from sympy.abc import x, y

        >>> Poly(x**3 + 2*x**2 + 3*x, x).nth(2)
        2
        >>> Poly(x**3 + 2*x*y**2 + y**2, x, y).nth(1, 2)
        2
        >>> Poly(4*sqrt(x)*y)
        Poly(4*y*(sqrt(x)), y, sqrt(x), domain='ZZ')
        >>> _.nth(1, 1)
        4

        See Also
        ========
        coeff_monomial

        """
    def coeff(f, x, n: int = 1, right: bool = False) -> None: ...
    def LM(f, order: Incomplete | None = None):
        """
        Returns the leading monomial of ``f``.

        The Leading monomial signifies the monomial having
        the highest power of the principal generator in the
        expression f.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x, y

        >>> Poly(4*x**2 + 2*x*y**2 + x*y + 3*y, x, y).LM()
        x**2*y**0

        """
    def EM(f, order: Incomplete | None = None):
        """
        Returns the last non-zero monomial of ``f``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x, y

        >>> Poly(4*x**2 + 2*x*y**2 + x*y + 3*y, x, y).EM()
        x**0*y**1

        """
    def LT(f, order: Incomplete | None = None):
        """
        Returns the leading term of ``f``.

        The Leading term signifies the term having
        the highest power of the principal generator in the
        expression f along with its coefficient.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x, y

        >>> Poly(4*x**2 + 2*x*y**2 + x*y + 3*y, x, y).LT()
        (x**2*y**0, 4)

        """
    def ET(f, order: Incomplete | None = None):
        """
        Returns the last non-zero term of ``f``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x, y

        >>> Poly(4*x**2 + 2*x*y**2 + x*y + 3*y, x, y).ET()
        (x**0*y**1, 3)

        """
    def max_norm(f):
        """
        Returns maximum norm of ``f``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(-x**2 + 2*x - 3, x).max_norm()
        3

        """
    def l1_norm(f):
        """
        Returns l1 norm of ``f``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(-x**2 + 2*x - 3, x).l1_norm()
        6

        """
    def clear_denoms(self, convert: bool = False):
        """
        Clear denominators, but keep the ground domain.

        Examples
        ========

        >>> from sympy import Poly, S, QQ
        >>> from sympy.abc import x

        >>> f = Poly(x/2 + S(1)/3, x, domain=QQ)

        >>> f.clear_denoms()
        (6, Poly(3*x + 2, x, domain='QQ'))
        >>> f.clear_denoms(convert=True)
        (6, Poly(3*x + 2, x, domain='ZZ'))

        """
    def rat_clear_denoms(self, g):
        """
        Clear denominators in a rational function ``f/g``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x, y

        >>> f = Poly(x**2/y + 1, x)
        >>> g = Poly(x**3 + y, x)

        >>> p, q = f.rat_clear_denoms(g)

        >>> p
        Poly(x**2 + y, x, domain='ZZ[y]')
        >>> q
        Poly(y*x**3 + y**2, x, domain='ZZ[y]')

        """
    def integrate(self, *specs, **args):
        """
        Computes indefinite integral of ``f``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x, y

        >>> Poly(x**2 + 2*x + 1, x).integrate()
        Poly(1/3*x**3 + x**2 + x, x, domain='QQ')

        >>> Poly(x*y**2 + x, x, y).integrate((0, 1), (1, 0))
        Poly(1/2*x**2*y**2 + 1/2*x**2, x, y, domain='QQ')

        """
    def diff(f, *specs, **kwargs):
        """
        Computes partial derivative of ``f``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x, y

        >>> Poly(x**2 + 2*x + 1, x).diff()
        Poly(2*x + 2, x, domain='ZZ')

        >>> Poly(x*y**2 + x, x, y).diff((0, 0), (1, 1))
        Poly(2*x*y, x, y, domain='ZZ')

        """
    def eval(self, x, a: Incomplete | None = None, auto: bool = True):
        """
        Evaluate ``f`` at ``a`` in the given variable.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x, y, z

        >>> Poly(x**2 + 2*x + 3, x).eval(2)
        11

        >>> Poly(2*x*y + 3*x + y + 2, x, y).eval(x, 2)
        Poly(5*y + 8, y, domain='ZZ')

        >>> f = Poly(2*x*y + 3*x + y + 2*z, x, y, z)

        >>> f.eval({x: 2})
        Poly(5*y + 2*z + 6, y, z, domain='ZZ')
        >>> f.eval({x: 2, y: 5})
        Poly(2*z + 31, z, domain='ZZ')
        >>> f.eval({x: 2, y: 5, z: 7})
        45

        >>> f.eval((2, 5))
        Poly(2*z + 31, z, domain='ZZ')
        >>> f(2, 5)
        Poly(2*z + 31, z, domain='ZZ')

        """
    def __call__(f, *values):
        """
        Evaluate ``f`` at the give values.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x, y, z

        >>> f = Poly(2*x*y + 3*x + y + 2*z, x, y, z)

        >>> f(2)
        Poly(5*y + 2*z + 6, y, z, domain='ZZ')
        >>> f(2, 5)
        Poly(2*z + 31, z, domain='ZZ')
        >>> f(2, 5, 7)
        45

        """
    def half_gcdex(f, g, auto: bool = True):
        """
        Half extended Euclidean algorithm of ``f`` and ``g``.

        Returns ``(s, h)`` such that ``h = gcd(f, g)`` and ``s*f = h (mod g)``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> f = x**4 - 2*x**3 - 6*x**2 + 12*x + 15
        >>> g = x**3 + x**2 - 4*x - 4

        >>> Poly(f).half_gcdex(Poly(g))
        (Poly(-1/5*x + 3/5, x, domain='QQ'), Poly(x + 1, x, domain='QQ'))

        """
    def gcdex(f, g, auto: bool = True):
        """
        Extended Euclidean algorithm of ``f`` and ``g``.

        Returns ``(s, t, h)`` such that ``h = gcd(f, g)`` and ``s*f + t*g = h``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> f = x**4 - 2*x**3 - 6*x**2 + 12*x + 15
        >>> g = x**3 + x**2 - 4*x - 4

        >>> Poly(f).gcdex(Poly(g))
        (Poly(-1/5*x + 3/5, x, domain='QQ'),
         Poly(1/5*x**2 - 6/5*x + 2, x, domain='QQ'),
         Poly(x + 1, x, domain='QQ'))

        """
    def invert(f, g, auto: bool = True):
        """
        Invert ``f`` modulo ``g`` when possible.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(x**2 - 1, x).invert(Poly(2*x - 1, x))
        Poly(-4/3, x, domain='QQ')

        >>> Poly(x**2 - 1, x).invert(Poly(x - 1, x))
        Traceback (most recent call last):
        ...
        NotInvertible: zero divisor

        """
    def revert(f, n):
        """
        Compute ``f**(-1)`` mod ``x**n``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(1, x).revert(2)
        Poly(1, x, domain='ZZ')

        >>> Poly(1 + x, x).revert(1)
        Poly(1, x, domain='ZZ')

        >>> Poly(x**2 - 2, x).revert(2)
        Traceback (most recent call last):
        ...
        NotReversible: only units are reversible in a ring

        >>> Poly(1/x, x).revert(1)
        Traceback (most recent call last):
        ...
        PolynomialError: 1/x contains an element of the generators set

        """
    def subresultants(f, g):
        """
        Computes the subresultant PRS of ``f`` and ``g``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(x**2 + 1, x).subresultants(Poly(x**2 - 1, x))
        [Poly(x**2 + 1, x, domain='ZZ'),
         Poly(x**2 - 1, x, domain='ZZ'),
         Poly(-2, x, domain='ZZ')]

        """
    def resultant(f, g, includePRS: bool = False):
        """
        Computes the resultant of ``f`` and ``g`` via PRS.

        If includePRS=True, it includes the subresultant PRS in the result.
        Because the PRS is used to calculate the resultant, this is more
        efficient than calling :func:`subresultants` separately.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> f = Poly(x**2 + 1, x)

        >>> f.resultant(Poly(x**2 - 1, x))
        4
        >>> f.resultant(Poly(x**2 - 1, x), includePRS=True)
        (4, [Poly(x**2 + 1, x, domain='ZZ'), Poly(x**2 - 1, x, domain='ZZ'),
             Poly(-2, x, domain='ZZ')])

        """
    def discriminant(f):
        """
        Computes the discriminant of ``f``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(x**2 + 2*x + 3, x).discriminant()
        -8

        """
    def dispersionset(f, g: Incomplete | None = None):
        """Compute the *dispersion set* of two polynomials.

        For two polynomials `f(x)` and `g(x)` with `\\deg f > 0`
        and `\\deg g > 0` the dispersion set `\\operatorname{J}(f, g)` is defined as:

        .. math::
            \\operatorname{J}(f, g)
            & := \\{a \\in \\mathbb{N}_0 | \\gcd(f(x), g(x+a)) \\neq 1\\} \\\\\n            &  = \\{a \\in \\mathbb{N}_0 | \\deg \\gcd(f(x), g(x+a)) \\geq 1\\}

        For a single polynomial one defines `\\operatorname{J}(f) := \\operatorname{J}(f, f)`.

        Examples
        ========

        >>> from sympy import poly
        >>> from sympy.polys.dispersion import dispersion, dispersionset
        >>> from sympy.abc import x

        Dispersion set and dispersion of a simple polynomial:

        >>> fp = poly((x - 3)*(x + 3), x)
        >>> sorted(dispersionset(fp))
        [0, 6]
        >>> dispersion(fp)
        6

        Note that the definition of the dispersion is not symmetric:

        >>> fp = poly(x**4 - 3*x**2 + 1, x)
        >>> gp = fp.shift(-3)
        >>> sorted(dispersionset(fp, gp))
        [2, 3, 4]
        >>> dispersion(fp, gp)
        4
        >>> sorted(dispersionset(gp, fp))
        []
        >>> dispersion(gp, fp)
        -oo

        Computing the dispersion also works over field extensions:

        >>> from sympy import sqrt
        >>> fp = poly(x**2 + sqrt(5)*x - 1, x, domain='QQ<sqrt(5)>')
        >>> gp = poly(x**2 + (2 + sqrt(5))*x + sqrt(5), x, domain='QQ<sqrt(5)>')
        >>> sorted(dispersionset(fp, gp))
        [2]
        >>> sorted(dispersionset(gp, fp))
        [1, 4]

        We can even perform the computations for polynomials
        having symbolic coefficients:

        >>> from sympy.abc import a
        >>> fp = poly(4*x**4 + (4*a + 8)*x**3 + (a**2 + 6*a + 4)*x**2 + (a**2 + 2*a)*x, x)
        >>> sorted(dispersionset(fp))
        [0, 1]

        See Also
        ========

        dispersion

        References
        ==========

        1. [ManWright94]_
        2. [Koepf98]_
        3. [Abramov71]_
        4. [Man93]_
        """
    def dispersion(f, g: Incomplete | None = None):
        """Compute the *dispersion* of polynomials.

        For two polynomials `f(x)` and `g(x)` with `\\deg f > 0`
        and `\\deg g > 0` the dispersion `\\operatorname{dis}(f, g)` is defined as:

        .. math::
            \\operatorname{dis}(f, g)
            & := \\max\\{ J(f,g) \\cup \\{0\\} \\} \\\\\n            &  = \\max\\{ \\{a \\in \\mathbb{N} | \\gcd(f(x), g(x+a)) \\neq 1\\} \\cup \\{0\\} \\}

        and for a single polynomial `\\operatorname{dis}(f) := \\operatorname{dis}(f, f)`.

        Examples
        ========

        >>> from sympy import poly
        >>> from sympy.polys.dispersion import dispersion, dispersionset
        >>> from sympy.abc import x

        Dispersion set and dispersion of a simple polynomial:

        >>> fp = poly((x - 3)*(x + 3), x)
        >>> sorted(dispersionset(fp))
        [0, 6]
        >>> dispersion(fp)
        6

        Note that the definition of the dispersion is not symmetric:

        >>> fp = poly(x**4 - 3*x**2 + 1, x)
        >>> gp = fp.shift(-3)
        >>> sorted(dispersionset(fp, gp))
        [2, 3, 4]
        >>> dispersion(fp, gp)
        4
        >>> sorted(dispersionset(gp, fp))
        []
        >>> dispersion(gp, fp)
        -oo

        Computing the dispersion also works over field extensions:

        >>> from sympy import sqrt
        >>> fp = poly(x**2 + sqrt(5)*x - 1, x, domain='QQ<sqrt(5)>')
        >>> gp = poly(x**2 + (2 + sqrt(5))*x + sqrt(5), x, domain='QQ<sqrt(5)>')
        >>> sorted(dispersionset(fp, gp))
        [2]
        >>> sorted(dispersionset(gp, fp))
        [1, 4]

        We can even perform the computations for polynomials
        having symbolic coefficients:

        >>> from sympy.abc import a
        >>> fp = poly(4*x**4 + (4*a + 8)*x**3 + (a**2 + 6*a + 4)*x**2 + (a**2 + 2*a)*x, x)
        >>> sorted(dispersionset(fp))
        [0, 1]

        See Also
        ========

        dispersionset

        References
        ==========

        1. [ManWright94]_
        2. [Koepf98]_
        3. [Abramov71]_
        4. [Man93]_
        """
    def cofactors(f, g):
        """
        Returns the GCD of ``f`` and ``g`` and their cofactors.

        Returns polynomials ``(h, cff, cfg)`` such that ``h = gcd(f, g)``, and
        ``cff = quo(f, h)`` and ``cfg = quo(g, h)`` are, so called, cofactors
        of ``f`` and ``g``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(x**2 - 1, x).cofactors(Poly(x**2 - 3*x + 2, x))
        (Poly(x - 1, x, domain='ZZ'),
         Poly(x + 1, x, domain='ZZ'),
         Poly(x - 2, x, domain='ZZ'))

        """
    def gcd(f, g):
        """
        Returns the polynomial GCD of ``f`` and ``g``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(x**2 - 1, x).gcd(Poly(x**2 - 3*x + 2, x))
        Poly(x - 1, x, domain='ZZ')

        """
    def lcm(f, g):
        """
        Returns polynomial LCM of ``f`` and ``g``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(x**2 - 1, x).lcm(Poly(x**2 - 3*x + 2, x))
        Poly(x**3 - 2*x**2 - x + 2, x, domain='ZZ')

        """
    def trunc(f, p):
        """
        Reduce ``f`` modulo a constant ``p``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(2*x**3 + 3*x**2 + 5*x + 7, x).trunc(3)
        Poly(-x**3 - x + 1, x, domain='ZZ')

        """
    def monic(self, auto: bool = True):
        """
        Divides all coefficients by ``LC(f)``.

        Examples
        ========

        >>> from sympy import Poly, ZZ
        >>> from sympy.abc import x

        >>> Poly(3*x**2 + 6*x + 9, x, domain=ZZ).monic()
        Poly(x**2 + 2*x + 3, x, domain='QQ')

        >>> Poly(3*x**2 + 4*x + 2, x, domain=ZZ).monic()
        Poly(x**2 + 4/3*x + 2/3, x, domain='QQ')

        """
    def content(f):
        """
        Returns the GCD of polynomial coefficients.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(6*x**2 + 8*x + 12, x).content()
        2

        """
    def primitive(f):
        """
        Returns the content and a primitive form of ``f``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(2*x**2 + 8*x + 12, x).primitive()
        (2, Poly(x**2 + 4*x + 6, x, domain='ZZ'))

        """
    def compose(f, g):
        """
        Computes the functional composition of ``f`` and ``g``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(x**2 + x, x).compose(Poly(x - 1, x))
        Poly(x**2 - x, x, domain='ZZ')

        """
    def decompose(f):
        """
        Computes a functional decomposition of ``f``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(x**4 + 2*x**3 - x - 1, x, domain='ZZ').decompose()
        [Poly(x**2 - x - 1, x, domain='ZZ'), Poly(x**2 + x, x, domain='ZZ')]

        """
    def shift(f, a):
        """
        Efficiently compute Taylor shift ``f(x + a)``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(x**2 - 2*x + 1, x).shift(2)
        Poly(x**2 + 2*x + 1, x, domain='ZZ')

        """
    def transform(f, p, q):
        """
        Efficiently evaluate the functional transformation ``q**n * f(p/q)``.


        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(x**2 - 2*x + 1, x).transform(Poly(x + 1, x), Poly(x - 1, x))
        Poly(4, x, domain='ZZ')

        """
    def sturm(self, auto: bool = True):
        """
        Computes the Sturm sequence of ``f``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(x**3 - 2*x**2 + x - 3, x).sturm()
        [Poly(x**3 - 2*x**2 + x - 3, x, domain='QQ'),
         Poly(3*x**2 - 4*x + 1, x, domain='QQ'),
         Poly(2/9*x + 25/9, x, domain='QQ'),
         Poly(-2079/4, x, domain='QQ')]

        """
    def gff_list(f):
        """
        Computes greatest factorial factorization of ``f``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> f = x**5 + 2*x**4 - x**3 - 2*x**2

        >>> Poly(f).gff_list()
        [(Poly(x, x, domain='ZZ'), 1), (Poly(x + 2, x, domain='ZZ'), 4)]

        """
    def norm(f):
        """
        Computes the product, ``Norm(f)``, of the conjugates of
        a polynomial ``f`` defined over a number field ``K``.

        Examples
        ========

        >>> from sympy import Poly, sqrt
        >>> from sympy.abc import x

        >>> a, b = sqrt(2), sqrt(3)

        A polynomial over a quadratic extension.
        Two conjugates x - a and x + a.

        >>> f = Poly(x - a, x, extension=a)
        >>> f.norm()
        Poly(x**2 - 2, x, domain='QQ')

        A polynomial over a quartic extension.
        Four conjugates x - a, x - a, x + a and x + a.

        >>> f = Poly(x - a, x, extension=(a, b))
        >>> f.norm()
        Poly(x**4 - 4*x**2 + 4, x, domain='QQ')

        """
    def sqf_norm(f):
        """
        Computes square-free norm of ``f``.

        Returns ``s``, ``f``, ``r``, such that ``g(x) = f(x-sa)`` and
        ``r(x) = Norm(g(x))`` is a square-free polynomial over ``K``,
        where ``a`` is the algebraic extension of the ground domain.

        Examples
        ========

        >>> from sympy import Poly, sqrt
        >>> from sympy.abc import x

        >>> s, f, r = Poly(x**2 + 1, x, extension=[sqrt(3)]).sqf_norm()

        >>> s
        1
        >>> f
        Poly(x**2 - 2*sqrt(3)*x + 4, x, domain='QQ<sqrt(3)>')
        >>> r
        Poly(x**4 - 4*x**2 + 16, x, domain='QQ')

        """
    def sqf_part(f):
        """
        Computes square-free part of ``f``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(x**3 - 3*x - 2, x).sqf_part()
        Poly(x**2 - x - 2, x, domain='ZZ')

        """
    def sqf_list(f, all: bool = False):
        """
        Returns a list of square-free factors of ``f``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> f = 2*x**5 + 16*x**4 + 50*x**3 + 76*x**2 + 56*x + 16

        >>> Poly(f).sqf_list()
        (2, [(Poly(x + 1, x, domain='ZZ'), 2),
             (Poly(x + 2, x, domain='ZZ'), 3)])

        >>> Poly(f).sqf_list(all=True)
        (2, [(Poly(1, x, domain='ZZ'), 1),
             (Poly(x + 1, x, domain='ZZ'), 2),
             (Poly(x + 2, x, domain='ZZ'), 3)])

        """
    def sqf_list_include(f, all: bool = False):
        """
        Returns a list of square-free factors of ``f``.

        Examples
        ========

        >>> from sympy import Poly, expand
        >>> from sympy.abc import x

        >>> f = expand(2*(x + 1)**3*x**4)
        >>> f
        2*x**7 + 6*x**6 + 6*x**5 + 2*x**4

        >>> Poly(f).sqf_list_include()
        [(Poly(2, x, domain='ZZ'), 1),
         (Poly(x + 1, x, domain='ZZ'), 3),
         (Poly(x, x, domain='ZZ'), 4)]

        >>> Poly(f).sqf_list_include(all=True)
        [(Poly(2, x, domain='ZZ'), 1),
         (Poly(1, x, domain='ZZ'), 2),
         (Poly(x + 1, x, domain='ZZ'), 3),
         (Poly(x, x, domain='ZZ'), 4)]

        """
    def factor_list(f):
        """
        Returns a list of irreducible factors of ``f``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x, y

        >>> f = 2*x**5 + 2*x**4*y + 4*x**3 + 4*x**2*y + 2*x + 2*y

        >>> Poly(f).factor_list()
        (2, [(Poly(x + y, x, y, domain='ZZ'), 1),
             (Poly(x**2 + 1, x, y, domain='ZZ'), 2)])

        """
    def factor_list_include(f):
        """
        Returns a list of irreducible factors of ``f``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x, y

        >>> f = 2*x**5 + 2*x**4*y + 4*x**3 + 4*x**2*y + 2*x + 2*y

        >>> Poly(f).factor_list_include()
        [(Poly(2*x + 2*y, x, y, domain='ZZ'), 1),
         (Poly(x**2 + 1, x, y, domain='ZZ'), 2)]

        """
    def intervals(f, all: bool = False, eps: Incomplete | None = None, inf: Incomplete | None = None, sup: Incomplete | None = None, fast: bool = False, sqf: bool = False):
        """
        Compute isolating intervals for roots of ``f``.

        For real roots the Vincent-Akritas-Strzebonski (VAS) continued fractions method is used.

        References
        ==========
        .. [#] Alkiviadis G. Akritas and Adam W. Strzebonski: A Comparative Study of Two Real Root
            Isolation Methods . Nonlinear Analysis: Modelling and Control, Vol. 10, No. 4, 297-304, 2005.
        .. [#] Alkiviadis G. Akritas, Adam W. Strzebonski and Panagiotis S. Vigklas: Improving the
            Performance of the Continued Fractions Method Using new Bounds of Positive Roots. Nonlinear
            Analysis: Modelling and Control, Vol. 13, No. 3, 265-279, 2008.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(x**2 - 3, x).intervals()
        [((-2, -1), 1), ((1, 2), 1)]
        >>> Poly(x**2 - 3, x).intervals(eps=1e-2)
        [((-26/15, -19/11), 1), ((19/11, 26/15), 1)]

        """
    def refine_root(f, s, t, eps: Incomplete | None = None, steps: Incomplete | None = None, fast: bool = False, check_sqf: bool = False):
        """
        Refine an isolating interval of a root to the given precision.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(x**2 - 3, x).refine_root(1, 2, eps=1e-2)
        (19/11, 26/15)

        """
    def count_roots(f, inf: Incomplete | None = None, sup: Incomplete | None = None):
        """
        Return the number of roots of ``f`` in ``[inf, sup]`` interval.

        Examples
        ========

        >>> from sympy import Poly, I
        >>> from sympy.abc import x

        >>> Poly(x**4 - 4, x).count_roots(-3, 3)
        2
        >>> Poly(x**4 - 4, x).count_roots(0, 1 + 3*I)
        1

        """
    def root(f, index, radicals: bool = True):
        """
        Get an indexed root of a polynomial.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> f = Poly(2*x**3 - 7*x**2 + 4*x + 4)

        >>> f.root(0)
        -1/2
        >>> f.root(1)
        2
        >>> f.root(2)
        2
        >>> f.root(3)
        Traceback (most recent call last):
        ...
        IndexError: root index out of [-3, 2] range, got 3

        >>> Poly(x**5 + x + 1).root(0)
        CRootOf(x**3 - x**2 + 1, 0)

        """
    def real_roots(f, multiple: bool = True, radicals: bool = True):
        """
        Return a list of real roots with multiplicities.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(2*x**3 - 7*x**2 + 4*x + 4).real_roots()
        [-1/2, 2, 2]
        >>> Poly(x**3 + x + 1).real_roots()
        [CRootOf(x**3 + x + 1, 0)]

        """
    def all_roots(f, multiple: bool = True, radicals: bool = True):
        """
        Return a list of real and complex roots with multiplicities.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(2*x**3 - 7*x**2 + 4*x + 4).all_roots()
        [-1/2, 2, 2]
        >>> Poly(x**3 + x + 1).all_roots()
        [CRootOf(x**3 + x + 1, 0),
         CRootOf(x**3 + x + 1, 1),
         CRootOf(x**3 + x + 1, 2)]

        """
    def nroots(f, n: int = 15, maxsteps: int = 50, cleanup: bool = True):
        """
        Compute numerical approximations of roots of ``f``.

        Parameters
        ==========

        n ... the number of digits to calculate
        maxsteps ... the maximum number of iterations to do

        If the accuracy `n` cannot be reached in `maxsteps`, it will raise an
        exception. You need to rerun with higher maxsteps.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(x**2 - 3).nroots(n=15)
        [-1.73205080756888, 1.73205080756888]
        >>> Poly(x**2 - 3).nroots(n=30)
        [-1.73205080756887729352744634151, 1.73205080756887729352744634151]

        """
    def ground_roots(f):
        """
        Compute roots of ``f`` by factorization in the ground domain.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(x**6 - 4*x**4 + 4*x**3 - x**2).ground_roots()
        {0: 2, 1: 2}

        """
    def nth_power_roots_poly(f, n):
        """
        Construct a polynomial with n-th powers of roots of ``f``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> f = Poly(x**4 - x**2 + 1)

        >>> f.nth_power_roots_poly(2)
        Poly(x**4 - 2*x**3 + 3*x**2 - 2*x + 1, x, domain='ZZ')
        >>> f.nth_power_roots_poly(3)
        Poly(x**4 + 2*x**2 + 1, x, domain='ZZ')
        >>> f.nth_power_roots_poly(4)
        Poly(x**4 + 2*x**3 + 3*x**2 + 2*x + 1, x, domain='ZZ')
        >>> f.nth_power_roots_poly(12)
        Poly(x**4 - 4*x**3 + 6*x**2 - 4*x + 1, x, domain='ZZ')

        """
    def same_root(f, a, b):
        """
        Decide whether two roots of this polynomial are equal.

        Examples
        ========

        >>> from sympy import Poly, cyclotomic_poly, exp, I, pi
        >>> f = Poly(cyclotomic_poly(5))
        >>> r0 = exp(2*I*pi/5)
        >>> indices = [i for i, r in enumerate(f.all_roots()) if f.same_root(r, r0)]
        >>> print(indices)
        [3]

        Raises
        ======

        DomainError
            If the domain of the polynomial is not :ref:`ZZ`, :ref:`QQ`,
            :ref:`RR`, or :ref:`CC`.
        MultivariatePolynomialError
            If the polynomial is not univariate.
        PolynomialError
            If the polynomial is of degree < 2.

        """
    def cancel(f, g, include: bool = False):
        """
        Cancel common factors in a rational function ``f/g``.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(2*x**2 - 2, x).cancel(Poly(x**2 - 2*x + 1, x))
        (1, Poly(2*x + 2, x, domain='ZZ'), Poly(x - 1, x, domain='ZZ'))

        >>> Poly(2*x**2 - 2, x).cancel(Poly(x**2 - 2*x + 1, x), include=True)
        (Poly(2*x + 2, x, domain='ZZ'), Poly(x - 1, x, domain='ZZ'))

        """
    def make_monic_over_integers_by_scaling_roots(f):
        """
        Turn any univariate polynomial over :ref:`QQ` or :ref:`ZZ` into a monic
        polynomial over :ref:`ZZ`, by scaling the roots as necessary.

        Explanation
        ===========

        This operation can be performed whether or not *f* is irreducible; when
        it is, this can be understood as determining an algebraic integer
        generating the same field as a root of *f*.

        Examples
        ========

        >>> from sympy import Poly, S
        >>> from sympy.abc import x
        >>> f = Poly(x**2/2 + S(1)/4 * x + S(1)/8, x, domain='QQ')
        >>> f.make_monic_over_integers_by_scaling_roots()
        (Poly(x**2 + 2*x + 4, x, domain='ZZ'), 4)

        Returns
        =======

        Pair ``(g, c)``
            g is the polynomial

            c is the integer by which the roots had to be scaled

        """
    def galois_group(f, by_name: bool = False, max_tries: int = 30, randomize: bool = False):
        """
        Compute the Galois group of this polynomial.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x
        >>> f = Poly(x**4 - 2)
        >>> G, _ = f.galois_group(by_name=True)
        >>> print(G)
        S4TransitiveSubgroups.D4

        See Also
        ========

        sympy.polys.numberfields.galoisgroups.galois_group

        """
    @property
    def is_zero(f):
        """
        Returns ``True`` if ``f`` is a zero polynomial.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(0, x).is_zero
        True
        >>> Poly(1, x).is_zero
        False

        """
    @property
    def is_one(f):
        """
        Returns ``True`` if ``f`` is a unit polynomial.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(0, x).is_one
        False
        >>> Poly(1, x).is_one
        True

        """
    @property
    def is_sqf(f):
        """
        Returns ``True`` if ``f`` is a square-free polynomial.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(x**2 - 2*x + 1, x).is_sqf
        False
        >>> Poly(x**2 - 1, x).is_sqf
        True

        """
    @property
    def is_monic(f):
        """
        Returns ``True`` if the leading coefficient of ``f`` is one.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(x + 2, x).is_monic
        True
        >>> Poly(2*x + 2, x).is_monic
        False

        """
    @property
    def is_primitive(f):
        """
        Returns ``True`` if GCD of the coefficients of ``f`` is one.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(2*x**2 + 6*x + 12, x).is_primitive
        False
        >>> Poly(x**2 + 3*x + 6, x).is_primitive
        True

        """
    @property
    def is_ground(f):
        """
        Returns ``True`` if ``f`` is an element of the ground domain.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x, y

        >>> Poly(x, x).is_ground
        False
        >>> Poly(2, x).is_ground
        True
        >>> Poly(y, x).is_ground
        True

        """
    @property
    def is_linear(f):
        """
        Returns ``True`` if ``f`` is linear in all its variables.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x, y

        >>> Poly(x + y + 2, x, y).is_linear
        True
        >>> Poly(x*y + 2, x, y).is_linear
        False

        """
    @property
    def is_quadratic(f):
        """
        Returns ``True`` if ``f`` is quadratic in all its variables.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x, y

        >>> Poly(x*y + 2, x, y).is_quadratic
        True
        >>> Poly(x*y**2 + 2, x, y).is_quadratic
        False

        """
    @property
    def is_monomial(f):
        """
        Returns ``True`` if ``f`` is zero or has only one term.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(3*x**2, x).is_monomial
        True
        >>> Poly(3*x**2 + 1, x).is_monomial
        False

        """
    @property
    def is_homogeneous(f):
        """
        Returns ``True`` if ``f`` is a homogeneous polynomial.

        A homogeneous polynomial is a polynomial whose all monomials with
        non-zero coefficients have the same total degree. If you want not
        only to check if a polynomial is homogeneous but also compute its
        homogeneous order, then use :func:`Poly.homogeneous_order`.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x, y

        >>> Poly(x**2 + x*y, x, y).is_homogeneous
        True
        >>> Poly(x**3 + x*y, x, y).is_homogeneous
        False

        """
    @property
    def is_irreducible(f):
        """
        Returns ``True`` if ``f`` has no factors over its domain.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> Poly(x**2 + x + 1, x, modulus=2).is_irreducible
        True
        >>> Poly(x**2 + 1, x, modulus=2).is_irreducible
        False

        """
    @property
    def is_univariate(f):
        """
        Returns ``True`` if ``f`` is a univariate polynomial.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x, y

        >>> Poly(x**2 + x + 1, x).is_univariate
        True
        >>> Poly(x*y**2 + x*y + 1, x, y).is_univariate
        False
        >>> Poly(x*y**2 + x*y + 1, x).is_univariate
        True
        >>> Poly(x**2 + x + 1, x, y).is_univariate
        False

        """
    @property
    def is_multivariate(f):
        """
        Returns ``True`` if ``f`` is a multivariate polynomial.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x, y

        >>> Poly(x**2 + x + 1, x).is_multivariate
        False
        >>> Poly(x*y**2 + x*y + 1, x, y).is_multivariate
        True
        >>> Poly(x*y**2 + x*y + 1, x).is_multivariate
        False
        >>> Poly(x**2 + x + 1, x, y).is_multivariate
        True

        """
    @property
    def is_cyclotomic(f):
        """
        Returns ``True`` if ``f`` is a cyclotomic polnomial.

        Examples
        ========

        >>> from sympy import Poly
        >>> from sympy.abc import x

        >>> f = x**16 + x**14 - x**10 + x**8 - x**6 + x**2 + 1

        >>> Poly(f).is_cyclotomic
        False

        >>> g = x**16 + x**14 - x**10 - x**8 - x**6 + x**2 + 1

        >>> Poly(g).is_cyclotomic
        True

        """
    def __abs__(f): ...
    def __neg__(f): ...
    def __add__(f, g): ...
    def __radd__(f, g): ...
    def __sub__(f, g): ...
    def __rsub__(f, g): ...
    def __mul__(f, g): ...
    def __rmul__(f, g): ...
    def __pow__(f, n): ...
    def __divmod__(f, g): ...
    def __rdivmod__(f, g): ...
    def __mod__(f, g): ...
    def __rmod__(f, g): ...
    def __floordiv__(f, g): ...
    def __rfloordiv__(f, g): ...
    def __truediv__(f, g): ...
    def __rtruediv__(f, g): ...
    def __eq__(self, other): ...
    def __ne__(f, g): ...
    def __bool__(f) -> bool: ...
    def eq(f, g, strict: bool = False): ...
    def ne(f, g, strict: bool = False): ...

class PurePoly(Poly):
    """Class for representing pure polynomials. """
    def __hash__(self): ...
    @property
    def free_symbols(self):
        """
        Free symbols of a polynomial.

        Examples
        ========

        >>> from sympy import PurePoly
        >>> from sympy.abc import x, y

        >>> PurePoly(x**2 + 1).free_symbols
        set()
        >>> PurePoly(x**2 + y).free_symbols
        set()
        >>> PurePoly(x**2 + y, x).free_symbols
        {y}

        """
    def __eq__(self, other): ...

def poly_from_expr(expr, *gens, **args):
    """Construct a polynomial from an expression. """
def parallel_poly_from_expr(exprs, *gens, **args):
    """Construct polynomials from expressions. """
def degree(f, gen: int = 0):
    """
    Return the degree of ``f`` in the given variable.

    The degree of 0 is negative infinity.

    Examples
    ========

    >>> from sympy import degree
    >>> from sympy.abc import x, y

    >>> degree(x**2 + y*x + 1, gen=x)
    2
    >>> degree(x**2 + y*x + 1, gen=y)
    1
    >>> degree(0, x)
    -oo

    See also
    ========

    sympy.polys.polytools.Poly.total_degree
    degree_list
    """
def total_degree(f, *gens):
    """
    Return the total_degree of ``f`` in the given variables.

    Examples
    ========
    >>> from sympy import total_degree, Poly
    >>> from sympy.abc import x, y

    >>> total_degree(1)
    0
    >>> total_degree(x + x*y)
    2
    >>> total_degree(x + x*y, x)
    1

    If the expression is a Poly and no variables are given
    then the generators of the Poly will be used:

    >>> p = Poly(x + x*y, y)
    >>> total_degree(p)
    1

    To deal with the underlying expression of the Poly, convert
    it to an Expr:

    >>> total_degree(p.as_expr())
    2

    This is done automatically if any variables are given:

    >>> total_degree(p, x)
    1

    See also
    ========
    degree
    """
def degree_list(f, *gens, **args):
    """
    Return a list of degrees of ``f`` in all variables.

    Examples
    ========

    >>> from sympy import degree_list
    >>> from sympy.abc import x, y

    >>> degree_list(x**2 + y*x + 1)
    (2, 1)

    """
def LC(f, *gens, **args):
    """
    Return the leading coefficient of ``f``.

    Examples
    ========

    >>> from sympy import LC
    >>> from sympy.abc import x, y

    >>> LC(4*x**2 + 2*x*y**2 + x*y + 3*y)
    4

    """
def LM(f, *gens, **args):
    """
    Return the leading monomial of ``f``.

    Examples
    ========

    >>> from sympy import LM
    >>> from sympy.abc import x, y

    >>> LM(4*x**2 + 2*x*y**2 + x*y + 3*y)
    x**2

    """
def LT(f, *gens, **args):
    """
    Return the leading term of ``f``.

    Examples
    ========

    >>> from sympy import LT
    >>> from sympy.abc import x, y

    >>> LT(4*x**2 + 2*x*y**2 + x*y + 3*y)
    4*x**2

    """
def pdiv(f, g, *gens, **args):
    """
    Compute polynomial pseudo-division of ``f`` and ``g``.

    Examples
    ========

    >>> from sympy import pdiv
    >>> from sympy.abc import x

    >>> pdiv(x**2 + 1, 2*x - 4)
    (2*x + 4, 20)

    """
def prem(f, g, *gens, **args):
    """
    Compute polynomial pseudo-remainder of ``f`` and ``g``.

    Examples
    ========

    >>> from sympy import prem
    >>> from sympy.abc import x

    >>> prem(x**2 + 1, 2*x - 4)
    20

    """
def pquo(f, g, *gens, **args):
    """
    Compute polynomial pseudo-quotient of ``f`` and ``g``.

    Examples
    ========

    >>> from sympy import pquo
    >>> from sympy.abc import x

    >>> pquo(x**2 + 1, 2*x - 4)
    2*x + 4
    >>> pquo(x**2 - 1, 2*x - 1)
    2*x + 1

    """
def pexquo(f, g, *gens, **args):
    """
    Compute polynomial exact pseudo-quotient of ``f`` and ``g``.

    Examples
    ========

    >>> from sympy import pexquo
    >>> from sympy.abc import x

    >>> pexquo(x**2 - 1, 2*x - 2)
    2*x + 2

    >>> pexquo(x**2 + 1, 2*x - 4)
    Traceback (most recent call last):
    ...
    ExactQuotientFailed: 2*x - 4 does not divide x**2 + 1

    """
def div(f, g, *gens, **args):
    """
    Compute polynomial division of ``f`` and ``g``.

    Examples
    ========

    >>> from sympy import div, ZZ, QQ
    >>> from sympy.abc import x

    >>> div(x**2 + 1, 2*x - 4, domain=ZZ)
    (0, x**2 + 1)
    >>> div(x**2 + 1, 2*x - 4, domain=QQ)
    (x/2 + 1, 5)

    """
def rem(f, g, *gens, **args):
    """
    Compute polynomial remainder of ``f`` and ``g``.

    Examples
    ========

    >>> from sympy import rem, ZZ, QQ
    >>> from sympy.abc import x

    >>> rem(x**2 + 1, 2*x - 4, domain=ZZ)
    x**2 + 1
    >>> rem(x**2 + 1, 2*x - 4, domain=QQ)
    5

    """
def quo(f, g, *gens, **args):
    """
    Compute polynomial quotient of ``f`` and ``g``.

    Examples
    ========

    >>> from sympy import quo
    >>> from sympy.abc import x

    >>> quo(x**2 + 1, 2*x - 4)
    x/2 + 1
    >>> quo(x**2 - 1, x - 1)
    x + 1

    """
def exquo(f, g, *gens, **args):
    """
    Compute polynomial exact quotient of ``f`` and ``g``.

    Examples
    ========

    >>> from sympy import exquo
    >>> from sympy.abc import x

    >>> exquo(x**2 - 1, x - 1)
    x + 1

    >>> exquo(x**2 + 1, 2*x - 4)
    Traceback (most recent call last):
    ...
    ExactQuotientFailed: 2*x - 4 does not divide x**2 + 1

    """
def half_gcdex(f, g, *gens, **args):
    """
    Half extended Euclidean algorithm of ``f`` and ``g``.

    Returns ``(s, h)`` such that ``h = gcd(f, g)`` and ``s*f = h (mod g)``.

    Examples
    ========

    >>> from sympy import half_gcdex
    >>> from sympy.abc import x

    >>> half_gcdex(x**4 - 2*x**3 - 6*x**2 + 12*x + 15, x**3 + x**2 - 4*x - 4)
    (3/5 - x/5, x + 1)

    """
def gcdex(f, g, *gens, **args):
    """
    Extended Euclidean algorithm of ``f`` and ``g``.

    Returns ``(s, t, h)`` such that ``h = gcd(f, g)`` and ``s*f + t*g = h``.

    Examples
    ========

    >>> from sympy import gcdex
    >>> from sympy.abc import x

    >>> gcdex(x**4 - 2*x**3 - 6*x**2 + 12*x + 15, x**3 + x**2 - 4*x - 4)
    (3/5 - x/5, x**2/5 - 6*x/5 + 2, x + 1)

    """
def invert(f, g, *gens, **args):
    """
    Invert ``f`` modulo ``g`` when possible.

    Examples
    ========

    >>> from sympy import invert, S, mod_inverse
    >>> from sympy.abc import x

    >>> invert(x**2 - 1, 2*x - 1)
    -4/3

    >>> invert(x**2 - 1, x - 1)
    Traceback (most recent call last):
    ...
    NotInvertible: zero divisor

    For more efficient inversion of Rationals,
    use the :obj:`~.mod_inverse` function:

    >>> mod_inverse(3, 5)
    2
    >>> (S(2)/5).invert(S(7)/3)
    5/2

    See Also
    ========

    sympy.core.numbers.mod_inverse

    """
def subresultants(f, g, *gens, **args):
    """
    Compute subresultant PRS of ``f`` and ``g``.

    Examples
    ========

    >>> from sympy import subresultants
    >>> from sympy.abc import x

    >>> subresultants(x**2 + 1, x**2 - 1)
    [x**2 + 1, x**2 - 1, -2]

    """
def resultant(f, g, *gens, includePRS: bool = False, **args):
    """
    Compute resultant of ``f`` and ``g``.

    Examples
    ========

    >>> from sympy import resultant
    >>> from sympy.abc import x

    >>> resultant(x**2 + 1, x**2 - 1)
    4

    """
def discriminant(f, *gens, **args):
    """
    Compute discriminant of ``f``.

    Examples
    ========

    >>> from sympy import discriminant
    >>> from sympy.abc import x

    >>> discriminant(x**2 + 2*x + 3)
    -8

    """
def cofactors(f, g, *gens, **args):
    """
    Compute GCD and cofactors of ``f`` and ``g``.

    Returns polynomials ``(h, cff, cfg)`` such that ``h = gcd(f, g)``, and
    ``cff = quo(f, h)`` and ``cfg = quo(g, h)`` are, so called, cofactors
    of ``f`` and ``g``.

    Examples
    ========

    >>> from sympy import cofactors
    >>> from sympy.abc import x

    >>> cofactors(x**2 - 1, x**2 - 3*x + 2)
    (x - 1, x + 1, x - 2)

    """
def gcd_list(seq, *gens, **args):
    """
    Compute GCD of a list of polynomials.

    Examples
    ========

    >>> from sympy import gcd_list
    >>> from sympy.abc import x

    >>> gcd_list([x**3 - 1, x**2 - 1, x**2 - 3*x + 2])
    x - 1

    """
def gcd(f, g: Incomplete | None = None, *gens, **args):
    """
    Compute GCD of ``f`` and ``g``.

    Examples
    ========

    >>> from sympy import gcd
    >>> from sympy.abc import x

    >>> gcd(x**2 - 1, x**2 - 3*x + 2)
    x - 1

    """
def lcm_list(seq, *gens, **args):
    """
    Compute LCM of a list of polynomials.

    Examples
    ========

    >>> from sympy import lcm_list
    >>> from sympy.abc import x

    >>> lcm_list([x**3 - 1, x**2 - 1, x**2 - 3*x + 2])
    x**5 - x**4 - 2*x**3 - x**2 + x + 2

    """
def lcm(f, g: Incomplete | None = None, *gens, **args):
    """
    Compute LCM of ``f`` and ``g``.

    Examples
    ========

    >>> from sympy import lcm
    >>> from sympy.abc import x

    >>> lcm(x**2 - 1, x**2 - 3*x + 2)
    x**3 - 2*x**2 - x + 2

    """
def terms_gcd(f, *gens, **args):
    """
    Remove GCD of terms from ``f``.

    If the ``deep`` flag is True, then the arguments of ``f`` will have
    terms_gcd applied to them.

    If a fraction is factored out of ``f`` and ``f`` is an Add, then
    an unevaluated Mul will be returned so that automatic simplification
    does not redistribute it. The hint ``clear``, when set to False, can be
    used to prevent such factoring when all coefficients are not fractions.

    Examples
    ========

    >>> from sympy import terms_gcd, cos
    >>> from sympy.abc import x, y
    >>> terms_gcd(x**6*y**2 + x**3*y, x, y)
    x**3*y*(x**3*y + 1)

    The default action of polys routines is to expand the expression
    given to them. terms_gcd follows this behavior:

    >>> terms_gcd((3+3*x)*(x+x*y))
    3*x*(x*y + x + y + 1)

    If this is not desired then the hint ``expand`` can be set to False.
    In this case the expression will be treated as though it were comprised
    of one or more terms:

    >>> terms_gcd((3+3*x)*(x+x*y), expand=False)
    (3*x + 3)*(x*y + x)

    In order to traverse factors of a Mul or the arguments of other
    functions, the ``deep`` hint can be used:

    >>> terms_gcd((3 + 3*x)*(x + x*y), expand=False, deep=True)
    3*x*(x + 1)*(y + 1)
    >>> terms_gcd(cos(x + x*y), deep=True)
    cos(x*(y + 1))

    Rationals are factored out by default:

    >>> terms_gcd(x + y/2)
    (2*x + y)/2

    Only the y-term had a coefficient that was a fraction; if one
    does not want to factor out the 1/2 in cases like this, the
    flag ``clear`` can be set to False:

    >>> terms_gcd(x + y/2, clear=False)
    x + y/2
    >>> terms_gcd(x*y/2 + y**2, clear=False)
    y*(x/2 + y)

    The ``clear`` flag is ignored if all coefficients are fractions:

    >>> terms_gcd(x/3 + y/2, clear=False)
    (2*x + 3*y)/6

    See Also
    ========
    sympy.core.exprtools.gcd_terms, sympy.core.exprtools.factor_terms

    """
def trunc(f, p, *gens, **args):
    """
    Reduce ``f`` modulo a constant ``p``.

    Examples
    ========

    >>> from sympy import trunc
    >>> from sympy.abc import x

    >>> trunc(2*x**3 + 3*x**2 + 5*x + 7, 3)
    -x**3 - x + 1

    """
def monic(f, *gens, **args):
    """
    Divide all coefficients of ``f`` by ``LC(f)``.

    Examples
    ========

    >>> from sympy import monic
    >>> from sympy.abc import x

    >>> monic(3*x**2 + 4*x + 2)
    x**2 + 4*x/3 + 2/3

    """
def content(f, *gens, **args):
    """
    Compute GCD of coefficients of ``f``.

    Examples
    ========

    >>> from sympy import content
    >>> from sympy.abc import x

    >>> content(6*x**2 + 8*x + 12)
    2

    """
def primitive(f, *gens, **args):
    """
    Compute content and the primitive form of ``f``.

    Examples
    ========

    >>> from sympy.polys.polytools import primitive
    >>> from sympy.abc import x

    >>> primitive(6*x**2 + 8*x + 12)
    (2, 3*x**2 + 4*x + 6)

    >>> eq = (2 + 2*x)*x + 2

    Expansion is performed by default:

    >>> primitive(eq)
    (2, x**2 + x + 1)

    Set ``expand`` to False to shut this off. Note that the
    extraction will not be recursive; use the as_content_primitive method
    for recursive, non-destructive Rational extraction.

    >>> primitive(eq, expand=False)
    (1, x*(2*x + 2) + 2)

    >>> eq.as_content_primitive()
    (2, x*(x + 1) + 1)

    """
def compose(f, g, *gens, **args):
    """
    Compute functional composition ``f(g)``.

    Examples
    ========

    >>> from sympy import compose
    >>> from sympy.abc import x

    >>> compose(x**2 + x, x - 1)
    x**2 - x

    """
def decompose(f, *gens, **args):
    """
    Compute functional decomposition of ``f``.

    Examples
    ========

    >>> from sympy import decompose
    >>> from sympy.abc import x

    >>> decompose(x**4 + 2*x**3 - x - 1)
    [x**2 - x - 1, x**2 + x]

    """
def sturm(f, *gens, **args):
    """
    Compute Sturm sequence of ``f``.

    Examples
    ========

    >>> from sympy import sturm
    >>> from sympy.abc import x

    >>> sturm(x**3 - 2*x**2 + x - 3)
    [x**3 - 2*x**2 + x - 3, 3*x**2 - 4*x + 1, 2*x/9 + 25/9, -2079/4]

    """
def gff_list(f, *gens, **args):
    """
    Compute a list of greatest factorial factors of ``f``.

    Note that the input to ff() and rf() should be Poly instances to use the
    definitions here.

    Examples
    ========

    >>> from sympy import gff_list, ff, Poly
    >>> from sympy.abc import x

    >>> f = Poly(x**5 + 2*x**4 - x**3 - 2*x**2, x)

    >>> gff_list(f)
    [(Poly(x, x, domain='ZZ'), 1), (Poly(x + 2, x, domain='ZZ'), 4)]

    >>> (ff(Poly(x), 1)*ff(Poly(x + 2), 4)) == f
    True

    >>> f = Poly(x**12 + 6*x**11 - 11*x**10 - 56*x**9 + 220*x**8 + 208*x**7 -         1401*x**6 + 1090*x**5 + 2715*x**4 - 6720*x**3 - 1092*x**2 + 5040*x, x)

    >>> gff_list(f)
    [(Poly(x**3 + 7, x, domain='ZZ'), 2), (Poly(x**2 + 5*x, x, domain='ZZ'), 3)]

    >>> ff(Poly(x**3 + 7, x), 2)*ff(Poly(x**2 + 5*x, x), 3) == f
    True

    """
def gff(f, *gens, **args) -> None:
    """Compute greatest factorial factorization of ``f``. """
def sqf_norm(f, *gens, **args):
    """
    Compute square-free norm of ``f``.

    Returns ``s``, ``f``, ``r``, such that ``g(x) = f(x-sa)`` and
    ``r(x) = Norm(g(x))`` is a square-free polynomial over ``K``,
    where ``a`` is the algebraic extension of the ground domain.

    Examples
    ========

    >>> from sympy import sqf_norm, sqrt
    >>> from sympy.abc import x

    >>> sqf_norm(x**2 + 1, extension=[sqrt(3)])
    (1, x**2 - 2*sqrt(3)*x + 4, x**4 - 4*x**2 + 16)

    """
def sqf_part(f, *gens, **args):
    """
    Compute square-free part of ``f``.

    Examples
    ========

    >>> from sympy import sqf_part
    >>> from sympy.abc import x

    >>> sqf_part(x**3 - 3*x - 2)
    x**2 - x - 2

    """
def to_rational_coeffs(f):
    """
    try to transform a polynomial to have rational coefficients

    try to find a transformation ``x = alpha*y``

    ``f(x) = lc*alpha**n * g(y)`` where ``g`` is a polynomial with
    rational coefficients, ``lc`` the leading coefficient.

    If this fails, try ``x = y + beta``
    ``f(x) = g(y)``

    Returns ``None`` if ``g`` not found;
    ``(lc, alpha, None, g)`` in case of rescaling
    ``(None, None, beta, g)`` in case of translation

    Notes
    =====

    Currently it transforms only polynomials without roots larger than 2.

    Examples
    ========

    >>> from sympy import sqrt, Poly, simplify
    >>> from sympy.polys.polytools import to_rational_coeffs
    >>> from sympy.abc import x
    >>> p = Poly(((x**2-1)*(x-2)).subs({x:x*(1 + sqrt(2))}), x, domain='EX')
    >>> lc, r, _, g = to_rational_coeffs(p)
    >>> lc, r
    (7 + 5*sqrt(2), 2 - 2*sqrt(2))
    >>> g
    Poly(x**3 + x**2 - 1/4*x - 1/4, x, domain='QQ')
    >>> r1 = simplify(1/r)
    >>> Poly(lc*r**3*(g.as_expr()).subs({x:x*r1}), x, domain='EX') == p
    True

    """
def sqf_list(f, *gens, **args):
    """
    Compute a list of square-free factors of ``f``.

    Examples
    ========

    >>> from sympy import sqf_list
    >>> from sympy.abc import x

    >>> sqf_list(2*x**5 + 16*x**4 + 50*x**3 + 76*x**2 + 56*x + 16)
    (2, [(x + 1, 2), (x + 2, 3)])

    """
def sqf(f, *gens, **args):
    """
    Compute square-free factorization of ``f``.

    Examples
    ========

    >>> from sympy import sqf
    >>> from sympy.abc import x

    >>> sqf(2*x**5 + 16*x**4 + 50*x**3 + 76*x**2 + 56*x + 16)
    2*(x + 1)**2*(x + 2)**3

    """
def factor_list(f, *gens, **args):
    """
    Compute a list of irreducible factors of ``f``.

    Examples
    ========

    >>> from sympy import factor_list
    >>> from sympy.abc import x, y

    >>> factor_list(2*x**5 + 2*x**4*y + 4*x**3 + 4*x**2*y + 2*x + 2*y)
    (2, [(x + y, 1), (x**2 + 1, 2)])

    """
def factor(f, *gens, deep: bool = False, **args):
    """
    Compute the factorization of expression, ``f``, into irreducibles. (To
    factor an integer into primes, use ``factorint``.)

    There two modes implemented: symbolic and formal. If ``f`` is not an
    instance of :class:`Poly` and generators are not specified, then the
    former mode is used. Otherwise, the formal mode is used.

    In symbolic mode, :func:`factor` will traverse the expression tree and
    factor its components without any prior expansion, unless an instance
    of :class:`~.Add` is encountered (in this case formal factorization is
    used). This way :func:`factor` can handle large or symbolic exponents.

    By default, the factorization is computed over the rationals. To factor
    over other domain, e.g. an algebraic or finite field, use appropriate
    options: ``extension``, ``modulus`` or ``domain``.

    Examples
    ========

    >>> from sympy import factor, sqrt, exp
    >>> from sympy.abc import x, y

    >>> factor(2*x**5 + 2*x**4*y + 4*x**3 + 4*x**2*y + 2*x + 2*y)
    2*(x + y)*(x**2 + 1)**2

    >>> factor(x**2 + 1)
    x**2 + 1
    >>> factor(x**2 + 1, modulus=2)
    (x + 1)**2
    >>> factor(x**2 + 1, gaussian=True)
    (x - I)*(x + I)

    >>> factor(x**2 - 2, extension=sqrt(2))
    (x - sqrt(2))*(x + sqrt(2))

    >>> factor((x**2 - 1)/(x**2 + 4*x + 4))
    (x - 1)*(x + 1)/(x + 2)**2
    >>> factor((x**2 + 4*x + 4)**10000000*(x**2 + 1))
    (x + 2)**20000000*(x**2 + 1)

    By default, factor deals with an expression as a whole:

    >>> eq = 2**(x**2 + 2*x + 1)
    >>> factor(eq)
    2**(x**2 + 2*x + 1)

    If the ``deep`` flag is True then subexpressions will
    be factored:

    >>> factor(eq, deep=True)
    2**((x + 1)**2)

    If the ``fraction`` flag is False then rational expressions
    will not be combined. By default it is True.

    >>> factor(5*x + 3*exp(2 - 7*x), deep=True)
    (5*x*exp(7*x) + 3*exp(2))*exp(-7*x)
    >>> factor(5*x + 3*exp(2 - 7*x), deep=True, fraction=False)
    5*x + 3*exp(2)*exp(-7*x)

    See Also
    ========
    sympy.ntheory.factor_.factorint

    """
def intervals(F, all: bool = False, eps: Incomplete | None = None, inf: Incomplete | None = None, sup: Incomplete | None = None, strict: bool = False, fast: bool = False, sqf: bool = False):
    """
    Compute isolating intervals for roots of ``f``.

    Examples
    ========

    >>> from sympy import intervals
    >>> from sympy.abc import x

    >>> intervals(x**2 - 3)
    [((-2, -1), 1), ((1, 2), 1)]
    >>> intervals(x**2 - 3, eps=1e-2)
    [((-26/15, -19/11), 1), ((19/11, 26/15), 1)]

    """
def refine_root(f, s, t, eps: Incomplete | None = None, steps: Incomplete | None = None, fast: bool = False, check_sqf: bool = False):
    """
    Refine an isolating interval of a root to the given precision.

    Examples
    ========

    >>> from sympy import refine_root
    >>> from sympy.abc import x

    >>> refine_root(x**2 - 3, 1, 2, eps=1e-2)
    (19/11, 26/15)

    """
def count_roots(f, inf: Incomplete | None = None, sup: Incomplete | None = None):
    """
    Return the number of roots of ``f`` in ``[inf, sup]`` interval.

    If one of ``inf`` or ``sup`` is complex, it will return the number of roots
    in the complex rectangle with corners at ``inf`` and ``sup``.

    Examples
    ========

    >>> from sympy import count_roots, I
    >>> from sympy.abc import x

    >>> count_roots(x**4 - 4, -3, 3)
    2
    >>> count_roots(x**4 - 4, 0, 1 + 3*I)
    1

    """
def real_roots(f, multiple: bool = True):
    """
    Return a list of real roots with multiplicities of ``f``.

    Examples
    ========

    >>> from sympy import real_roots
    >>> from sympy.abc import x

    >>> real_roots(2*x**3 - 7*x**2 + 4*x + 4)
    [-1/2, 2, 2]
    """
def nroots(f, n: int = 15, maxsteps: int = 50, cleanup: bool = True):
    """
    Compute numerical approximations of roots of ``f``.

    Examples
    ========

    >>> from sympy import nroots
    >>> from sympy.abc import x

    >>> nroots(x**2 - 3, n=15)
    [-1.73205080756888, 1.73205080756888]
    >>> nroots(x**2 - 3, n=30)
    [-1.73205080756887729352744634151, 1.73205080756887729352744634151]

    """
def ground_roots(f, *gens, **args):
    """
    Compute roots of ``f`` by factorization in the ground domain.

    Examples
    ========

    >>> from sympy import ground_roots
    >>> from sympy.abc import x

    >>> ground_roots(x**6 - 4*x**4 + 4*x**3 - x**2)
    {0: 2, 1: 2}

    """
def nth_power_roots_poly(f, n, *gens, **args):
    """
    Construct a polynomial with n-th powers of roots of ``f``.

    Examples
    ========

    >>> from sympy import nth_power_roots_poly, factor, roots
    >>> from sympy.abc import x

    >>> f = x**4 - x**2 + 1
    >>> g = factor(nth_power_roots_poly(f, 2))

    >>> g
    (x**2 - x + 1)**2

    >>> R_f = [ (r**2).expand() for r in roots(f) ]
    >>> R_g = roots(g).keys()

    >>> set(R_f) == set(R_g)
    True

    """
def cancel(f, *gens, _signsimp: bool = True, **args):
    """
    Cancel common factors in a rational function ``f``.

    Examples
    ========

    >>> from sympy import cancel, sqrt, Symbol, together
    >>> from sympy.abc import x
    >>> A = Symbol('A', commutative=False)

    >>> cancel((2*x**2 - 2)/(x**2 - 2*x + 1))
    (2*x + 2)/(x - 1)
    >>> cancel((sqrt(3) + sqrt(15)*A)/(sqrt(2) + sqrt(10)*A))
    sqrt(6)/2

    Note: due to automatic distribution of Rationals, a sum divided by an integer
    will appear as a sum. To recover a rational form use `together` on the result:

    >>> cancel(x/2 + 1)
    x/2 + 1
    >>> together(_)
    (x + 2)/2
    """
def reduced(f, G, *gens, **args):
    """
    Reduces a polynomial ``f`` modulo a set of polynomials ``G``.

    Given a polynomial ``f`` and a set of polynomials ``G = (g_1, ..., g_n)``,
    computes a set of quotients ``q = (q_1, ..., q_n)`` and the remainder ``r``
    such that ``f = q_1*g_1 + ... + q_n*g_n + r``, where ``r`` vanishes or ``r``
    is a completely reduced polynomial with respect to ``G``.

    Examples
    ========

    >>> from sympy import reduced
    >>> from sympy.abc import x, y

    >>> reduced(2*x**4 + y**2 - x**2 + y**3, [x**3 - x, y**3 - y])
    ([2*x, 1], x**2 + y**2 + y)

    """
def groebner(F, *gens, **args):
    """
    Computes the reduced Groebner basis for a set of polynomials.

    Use the ``order`` argument to set the monomial ordering that will be
    used to compute the basis. Allowed orders are ``lex``, ``grlex`` and
    ``grevlex``. If no order is specified, it defaults to ``lex``.

    For more information on Groebner bases, see the references and the docstring
    of :func:`~.solve_poly_system`.

    Examples
    ========

    Example taken from [1].

    >>> from sympy import groebner
    >>> from sympy.abc import x, y

    >>> F = [x*y - 2*y, 2*y**2 - x**2]

    >>> groebner(F, x, y, order='lex')
    GroebnerBasis([x**2 - 2*y**2, x*y - 2*y, y**3 - 2*y], x, y,
                  domain='ZZ', order='lex')
    >>> groebner(F, x, y, order='grlex')
    GroebnerBasis([y**3 - 2*y, x**2 - 2*y**2, x*y - 2*y], x, y,
                  domain='ZZ', order='grlex')
    >>> groebner(F, x, y, order='grevlex')
    GroebnerBasis([y**3 - 2*y, x**2 - 2*y**2, x*y - 2*y], x, y,
                  domain='ZZ', order='grevlex')

    By default, an improved implementation of the Buchberger algorithm is
    used. Optionally, an implementation of the F5B algorithm can be used. The
    algorithm can be set using the ``method`` flag or with the
    :func:`sympy.polys.polyconfig.setup` function.

    >>> F = [x**2 - x - 1, (2*x - 1) * y - (x**10 - (1 - x)**10)]

    >>> groebner(F, x, y, method='buchberger')
    GroebnerBasis([x**2 - x - 1, y - 55], x, y, domain='ZZ', order='lex')
    >>> groebner(F, x, y, method='f5b')
    GroebnerBasis([x**2 - x - 1, y - 55], x, y, domain='ZZ', order='lex')

    References
    ==========

    1. [Buchberger01]_
    2. [Cox97]_

    """
def is_zero_dimensional(F, *gens, **args):
    """
    Checks if the ideal generated by a Groebner basis is zero-dimensional.

    The algorithm checks if the set of monomials not divisible by the
    leading monomial of any element of ``F`` is bounded.

    References
    ==========

    David A. Cox, John B. Little, Donal O'Shea. Ideals, Varieties and
    Algorithms, 3rd edition, p. 230

    """

class GroebnerBasis(Basic):
    """Represents a reduced Groebner basis. """
    def __new__(cls, F, *gens, **args):
        """Compute a reduced Groebner basis for a system of polynomials. """
    @property
    def args(self): ...
    @property
    def exprs(self): ...
    @property
    def polys(self): ...
    @property
    def gens(self): ...
    @property
    def domain(self): ...
    @property
    def order(self): ...
    def __len__(self) -> int: ...
    def __iter__(self): ...
    def __getitem__(self, item): ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    @property
    def is_zero_dimensional(self):
        """
        Checks if the ideal generated by a Groebner basis is zero-dimensional.

        The algorithm checks if the set of monomials not divisible by the
        leading monomial of any element of ``F`` is bounded.

        References
        ==========

        David A. Cox, John B. Little, Donal O'Shea. Ideals, Varieties and
        Algorithms, 3rd edition, p. 230

        """
    def fglm(self, order):
        """
        Convert a Groebner basis from one ordering to another.

        The FGLM algorithm converts reduced Groebner bases of zero-dimensional
        ideals from one ordering to another. This method is often used when it
        is infeasible to compute a Groebner basis with respect to a particular
        ordering directly.

        Examples
        ========

        >>> from sympy.abc import x, y
        >>> from sympy import groebner

        >>> F = [x**2 - 3*y - x + 1, y**2 - 2*x + y - 1]
        >>> G = groebner(F, x, y, order='grlex')

        >>> list(G.fglm('lex'))
        [2*x - y**2 - y + 1, y**4 + 2*y**3 - 3*y**2 - 16*y + 7]
        >>> list(groebner(F, x, y, order='lex'))
        [2*x - y**2 - y + 1, y**4 + 2*y**3 - 3*y**2 - 16*y + 7]

        References
        ==========

        .. [1] J.C. Faugere, P. Gianni, D. Lazard, T. Mora (1994). Efficient
               Computation of Zero-dimensional Groebner Bases by Change of
               Ordering

        """
    def reduce(self, expr, auto: bool = True):
        """
        Reduces a polynomial modulo a Groebner basis.

        Given a polynomial ``f`` and a set of polynomials ``G = (g_1, ..., g_n)``,
        computes a set of quotients ``q = (q_1, ..., q_n)`` and the remainder ``r``
        such that ``f = q_1*f_1 + ... + q_n*f_n + r``, where ``r`` vanishes or ``r``
        is a completely reduced polynomial with respect to ``G``.

        Examples
        ========

        >>> from sympy import groebner, expand
        >>> from sympy.abc import x, y

        >>> f = 2*x**4 - x**2 + y**3 + y**2
        >>> G = groebner([x**3 - x, y**3 - y])

        >>> G.reduce(f)
        ([2*x, 1], x**2 + y**2 + y)
        >>> Q, r = _

        >>> expand(sum(q*g for q, g in zip(Q, G)) + r)
        2*x**4 - x**2 + y**3 + y**2
        >>> _ == f
        True

        """
    def contains(self, poly):
        """
        Check if ``poly`` belongs the ideal generated by ``self``.

        Examples
        ========

        >>> from sympy import groebner
        >>> from sympy.abc import x, y

        >>> f = 2*x**3 + y**3 + 3*y
        >>> G = groebner([x**2 + y**2 - 1, x*y - 2])

        >>> G.contains(f)
        True
        >>> G.contains(f + 1)
        False

        """

def poly(expr, *gens, **args):
    """
    Efficiently transform an expression into a polynomial.

    Examples
    ========

    >>> from sympy import poly
    >>> from sympy.abc import x

    >>> poly(x*(x**2 + x - 1)**2)
    Poly(x**5 + 2*x**4 - x**3 - 2*x**2 + x, x, domain='ZZ')

    """
def named_poly(n, f, K, name, x, polys):
    """Common interface to the low-level polynomial generating functions
    in orthopolys and appellseqs.

    Parameters
    ==========

    n : int
        Index of the polynomial, which may or may not equal its degree.
    f : callable
        Low-level generating function to use.
    K : Domain or None
        Domain in which to perform the computations. If None, use the smallest
        field containing the rationals and the extra parameters of x (see below).
    name : str
        Name of an arbitrary individual polynomial in the sequence generated
        by f, only used in the error message for invalid n.
    x : seq
        The first element of this argument is the main variable of all
        polynomials in this sequence. Any further elements are extra
        parameters required by f.
    polys : bool, optional
        If True, return a Poly, otherwise (default) return an expression.
    """
