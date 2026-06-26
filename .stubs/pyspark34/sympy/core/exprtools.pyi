from .add import Add as Add
from .basic import Basic as Basic
from .containers import Dict as Dict, Tuple as Tuple
from .coreerrors import NonCommutativeExpression as NonCommutativeExpression
from .expr import Expr as Expr
from .function import expand_power_exp as expand_power_exp
from .mul import Mul as Mul
from .numbers import I as I, Integer as Integer, Number as Number, Rational as Rational, equal_valued as equal_valued
from .power import Pow as Pow
from .singleton import S as S
from .sorting import default_sort_key as default_sort_key, ordered as ordered
from .symbol import Dummy as Dummy
from .sympify import sympify as sympify
from .traversal import preorder_traversal as preorder_traversal
from _typeshed import Incomplete
from sympy.external.gmpy import SYMPY_INTS as SYMPY_INTS
from sympy.utilities.iterables import common_prefix as common_prefix, common_suffix as common_suffix, is_sequence as is_sequence, iterable as iterable, variations as variations
from typing import Tuple as tTuple

def decompose_power(expr: Expr) -> tTuple[Expr, int]:
    """
    Decompose power into symbolic base and integer exponent.

    Examples
    ========

    >>> from sympy.core.exprtools import decompose_power
    >>> from sympy.abc import x, y
    >>> from sympy import exp

    >>> decompose_power(x)
    (x, 1)
    >>> decompose_power(x**2)
    (x, 2)
    >>> decompose_power(exp(2*y/3))
    (exp(y/3), 2)

    """
def decompose_power_rat(expr: Expr) -> tTuple[Expr, Rational]:
    """
    Decompose power into symbolic base and rational exponent;
    if the exponent is not a Rational, then separate only the
    integer coefficient.

    Examples
    ========

    >>> from sympy.core.exprtools import decompose_power_rat
    >>> from sympy.abc import x
    >>> from sympy import sqrt, exp

    >>> decompose_power_rat(sqrt(x))
    (x, 1/2)
    >>> decompose_power_rat(exp(-3*x/2))
    (exp(x/2), -3)

    """

class Factors:
    """Efficient representation of ``f_1*f_2*...*f_n``."""
    factors: Incomplete
    gens: Incomplete
    def __init__(self, factors: Incomplete | None = None) -> None:
        """Initialize Factors from dict or expr.

        Examples
        ========

        >>> from sympy.core.exprtools import Factors
        >>> from sympy.abc import x
        >>> from sympy import I
        >>> e = 2*x**3
        >>> Factors(e)
        Factors({2: 1, x: 3})
        >>> Factors(e.as_powers_dict())
        Factors({2: 1, x: 3})
        >>> f = _
        >>> f.factors  # underlying dictionary
        {2: 1, x: 3}
        >>> f.gens  # base of each factor
        frozenset({2, x})
        >>> Factors(0)
        Factors({0: 1})
        >>> Factors(I)
        Factors({I: 1})

        Notes
        =====

        Although a dictionary can be passed, only minimal checking is
        performed: powers of -1 and I are made canonical.

        """
    def __hash__(self): ...
    @property
    def is_zero(self):
        """
        >>> from sympy.core.exprtools import Factors
        >>> Factors(0).is_zero
        True
        """
    @property
    def is_one(self):
        """
        >>> from sympy.core.exprtools import Factors
        >>> Factors(1).is_one
        True
        """
    def as_expr(self):
        """Return the underlying expression.

        Examples
        ========

        >>> from sympy.core.exprtools import Factors
        >>> from sympy.abc import x, y
        >>> Factors((x*y**2).as_powers_dict()).as_expr()
        x*y**2

        """
    def mul(self, other):
        """Return Factors of ``self * other``.

        Examples
        ========

        >>> from sympy.core.exprtools import Factors
        >>> from sympy.abc import x, y, z
        >>> a = Factors((x*y**2).as_powers_dict())
        >>> b = Factors((x*y/z).as_powers_dict())
        >>> a.mul(b)
        Factors({x: 2, y: 3, z: -1})
        >>> a*b
        Factors({x: 2, y: 3, z: -1})
        """
    def normal(self, other):
        """Return ``self`` and ``other`` with ``gcd`` removed from each.
        The only differences between this and method ``div`` is that this
        is 1) optimized for the case when there are few factors in common and
        2) this does not raise an error if ``other`` is zero.

        See Also
        ========
        div

        """
    def div(self, other):
        """Return ``self`` and ``other`` with ``gcd`` removed from each.
        This is optimized for the case when there are many factors in common.

        Examples
        ========

        >>> from sympy.core.exprtools import Factors
        >>> from sympy.abc import x, y, z
        >>> from sympy import S

        >>> a = Factors((x*y**2).as_powers_dict())
        >>> a.div(a)
        (Factors({}), Factors({}))
        >>> a.div(x*z)
        (Factors({y: 2}), Factors({z: 1}))

        The ``/`` operator only gives ``quo``:

        >>> a/x
        Factors({y: 2})

        Factors treats its factors as though they are all in the numerator, so
        if you violate this assumption the results will be correct but will
        not strictly correspond to the numerator and denominator of the ratio:

        >>> a.div(x/z)
        (Factors({y: 2}), Factors({z: -1}))

        Factors is also naive about bases: it does not attempt any denesting
        of Rational-base terms, for example the following does not become
        2**(2*x)/2.

        >>> Factors(2**(2*x + 2)).div(S(8))
        (Factors({2: 2*x + 2}), Factors({8: 1}))

        factor_terms can clean up such Rational-bases powers:

        >>> from sympy import factor_terms
        >>> n, d = Factors(2**(2*x + 2)).div(S(8))
        >>> n.as_expr()/d.as_expr()
        2**(2*x + 2)/8
        >>> factor_terms(_)
        2**(2*x)/2

        """
    def quo(self, other):
        """Return numerator Factor of ``self / other``.

        Examples
        ========

        >>> from sympy.core.exprtools import Factors
        >>> from sympy.abc import x, y, z
        >>> a = Factors((x*y**2).as_powers_dict())
        >>> b = Factors((x*y/z).as_powers_dict())
        >>> a.quo(b)  # same as a/b
        Factors({y: 1})
        """
    def rem(self, other):
        """Return denominator Factors of ``self / other``.

        Examples
        ========

        >>> from sympy.core.exprtools import Factors
        >>> from sympy.abc import x, y, z
        >>> a = Factors((x*y**2).as_powers_dict())
        >>> b = Factors((x*y/z).as_powers_dict())
        >>> a.rem(b)
        Factors({z: -1})
        >>> a.rem(a)
        Factors({})
        """
    def pow(self, other):
        """Return self raised to a non-negative integer power.

        Examples
        ========

        >>> from sympy.core.exprtools import Factors
        >>> from sympy.abc import x, y
        >>> a = Factors((x*y**2).as_powers_dict())
        >>> a**2
        Factors({x: 2, y: 4})

        """
    def gcd(self, other):
        """Return Factors of ``gcd(self, other)``. The keys are
        the intersection of factors with the minimum exponent for
        each factor.

        Examples
        ========

        >>> from sympy.core.exprtools import Factors
        >>> from sympy.abc import x, y, z
        >>> a = Factors((x*y**2).as_powers_dict())
        >>> b = Factors((x*y/z).as_powers_dict())
        >>> a.gcd(b)
        Factors({x: 1, y: 1})
        """
    def lcm(self, other):
        """Return Factors of ``lcm(self, other)`` which are
        the union of factors with the maximum exponent for
        each factor.

        Examples
        ========

        >>> from sympy.core.exprtools import Factors
        >>> from sympy.abc import x, y, z
        >>> a = Factors((x*y**2).as_powers_dict())
        >>> b = Factors((x*y/z).as_powers_dict())
        >>> a.lcm(b)
        Factors({x: 1, y: 2, z: -1})
        """
    def __mul__(self, other): ...
    def __divmod__(self, other): ...
    def __truediv__(self, other): ...
    def __mod__(self, other): ...
    def __pow__(self, other): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

class Term:
    """Efficient representation of ``coeff*(numer/denom)``. """
    coeff: Incomplete
    numer: Incomplete
    denom: Incomplete
    def __init__(self, term, numer: Incomplete | None = None, denom: Incomplete | None = None) -> None: ...
    def __hash__(self): ...
    def as_expr(self): ...
    def mul(self, other): ...
    def inv(self): ...
    def quo(self, other): ...
    def pow(self, other): ...
    def gcd(self, other): ...
    def lcm(self, other): ...
    def __mul__(self, other): ...
    def __truediv__(self, other): ...
    def __pow__(self, other): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

def gcd_terms(terms, isprimitive: bool = False, clear: bool = True, fraction: bool = True):
    """Compute the GCD of ``terms`` and put them together.

    Parameters
    ==========

    terms : Expr
        Can be an expression or a non-Basic sequence of expressions
        which will be handled as though they are terms from a sum.

    isprimitive : bool, optional
        If ``isprimitive`` is True the _gcd_terms will not run the primitive
        method on the terms.

    clear : bool, optional
        It controls the removal of integers from the denominator of an Add
        expression. When True (default), all numerical denominator will be cleared;
        when False the denominators will be cleared only if all terms had numerical
        denominators other than 1.

    fraction : bool, optional
        When True (default), will put the expression over a common
        denominator.

    Examples
    ========

    >>> from sympy import gcd_terms
    >>> from sympy.abc import x, y

    >>> gcd_terms((x + 1)**2*y + (x + 1)*y**2)
    y*(x + 1)*(x + y + 1)
    >>> gcd_terms(x/2 + 1)
    (x + 2)/2
    >>> gcd_terms(x/2 + 1, clear=False)
    x/2 + 1
    >>> gcd_terms(x/2 + y/2, clear=False)
    (x + y)/2
    >>> gcd_terms(x/2 + 1/x)
    (x**2 + 2)/(2*x)
    >>> gcd_terms(x/2 + 1/x, fraction=False)
    (x + 2/x)/2
    >>> gcd_terms(x/2 + 1/x, fraction=False, clear=False)
    x/2 + 1/x

    >>> gcd_terms(x/2/y + 1/x/y)
    (x**2 + 2)/(2*x*y)
    >>> gcd_terms(x/2/y + 1/x/y, clear=False)
    (x**2/2 + 1)/(x*y)
    >>> gcd_terms(x/2/y + 1/x/y, clear=False, fraction=False)
    (x/2 + 1/x)/y

    The ``clear`` flag was ignored in this case because the returned
    expression was a rational expression, not a simple sum.

    See Also
    ========

    factor_terms, sympy.polys.polytools.terms_gcd

    """
def factor_terms(expr, radical: bool = False, clear: bool = False, fraction: bool = False, sign: bool = True):
    """Remove common factors from terms in all arguments without
    changing the underlying structure of the expr. No expansion or
    simplification (and no processing of non-commutatives) is performed.

    Parameters
    ==========

    radical: bool, optional
        If radical=True then a radical common to all terms will be factored
        out of any Add sub-expressions of the expr.

    clear : bool, optional
        If clear=False (default) then coefficients will not be separated
        from a single Add if they can be distributed to leave one or more
        terms with integer coefficients.

    fraction : bool, optional
        If fraction=True (default is False) then a common denominator will be
        constructed for the expression.

    sign : bool, optional
        If sign=True (default) then even if the only factor in common is a -1,
        it will be factored out of the expression.

    Examples
    ========

    >>> from sympy import factor_terms, Symbol
    >>> from sympy.abc import x, y
    >>> factor_terms(x + x*(2 + 4*y)**3)
    x*(8*(2*y + 1)**3 + 1)
    >>> A = Symbol('A', commutative=False)
    >>> factor_terms(x*A + x*A + x*y*A)
    x*(y*A + 2*A)

    When ``clear`` is False, a rational will only be factored out of an
    Add expression if all terms of the Add have coefficients that are
    fractions:

    >>> factor_terms(x/2 + 1, clear=False)
    x/2 + 1
    >>> factor_terms(x/2 + 1, clear=True)
    (x + 2)/2

    If a -1 is all that can be factored out, to *not* factor it out, the
    flag ``sign`` must be False:

    >>> factor_terms(-x - y)
    -(x + y)
    >>> factor_terms(-x - y, sign=False)
    -x - y
    >>> factor_terms(-2*x - 2*y, sign=False)
    -2*(x + y)

    See Also
    ========

    gcd_terms, sympy.polys.polytools.terms_gcd

    """
def factor_nc(expr):
    """Return the factored form of ``expr`` while handling non-commutative
    expressions.

    Examples
    ========

    >>> from sympy import factor_nc, Symbol
    >>> from sympy.abc import x
    >>> A = Symbol('A', commutative=False)
    >>> B = Symbol('B', commutative=False)
    >>> factor_nc((x**2 + 2*A*x + A**2).expand())
    (x + A)**2
    >>> factor_nc(((x + A)*(x + B)).expand())
    (x + A)*(x + B)
    """
