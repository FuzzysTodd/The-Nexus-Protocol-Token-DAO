from sympy.core import sympify as sympify
from sympy.core.evalf import pure_complex as pure_complex
from sympy.core.sorting import ordered as ordered
from sympy.polys.domains import EX as EX, QQ as QQ, QQ_I as QQ_I, ZZ as ZZ, ZZ_I as ZZ_I
from sympy.polys.domains.complexfield import ComplexField as ComplexField
from sympy.polys.domains.realfield import RealField as RealField
from sympy.polys.polyoptions import build_options as build_options
from sympy.polys.polyutils import parallel_dict_from_basic as parallel_dict_from_basic
from sympy.utilities import public as public

def construct_domain(obj, **args):
    """Construct a minimal domain for a list of expressions.

    Explanation
    ===========

    Given a list of normal SymPy expressions (of type :py:class:`~.Expr`)
    ``construct_domain`` will find a minimal :py:class:`~.Domain` that can
    represent those expressions. The expressions will be converted to elements
    of the domain and both the domain and the domain elements are returned.

    Parameters
    ==========

    obj: list or dict
        The expressions to build a domain for.

    **args: keyword arguments
        Options that affect the choice of domain.

    Returns
    =======

    (K, elements): Domain and list of domain elements
        The domain K that can represent the expressions and the list or dict
        of domain elements representing the same expressions as elements of K.

    Examples
    ========

    Given a list of :py:class:`~.Integer` ``construct_domain`` will return the
    domain :ref:`ZZ` and a list of integers as elements of :ref:`ZZ`.

    >>> from sympy import construct_domain, S
    >>> expressions = [S(2), S(3), S(4)]
    >>> K, elements = construct_domain(expressions)
    >>> K
    ZZ
    >>> elements
    [2, 3, 4]
    >>> type(elements[0])  # doctest: +SKIP
    <class 'int'>
    >>> type(expressions[0])
    <class 'sympy.core.numbers.Integer'>

    If there are any :py:class:`~.Rational` then :ref:`QQ` is returned
    instead.

    >>> construct_domain([S(1)/2, S(3)/4])
    (QQ, [1/2, 3/4])

    If there are symbols then a polynomial ring :ref:`K[x]` is returned.

    >>> from sympy import symbols
    >>> x, y = symbols('x, y')
    >>> construct_domain([2*x + 1, S(3)/4])
    (QQ[x], [2*x + 1, 3/4])
    >>> construct_domain([2*x + 1, y])
    (ZZ[x,y], [2*x + 1, y])

    If any symbols appear with negative powers then a rational function field
    :ref:`K(x)` will be returned.

    >>> construct_domain([y/x, x/(1 - y)])
    (ZZ(x,y), [y/x, -x/(y - 1)])

    Irrational algebraic numbers will result in the :ref:`EX` domain by
    default. The keyword argument ``extension=True`` leads to the construction
    of an algebraic number field :ref:`QQ(a)`.

    >>> from sympy import sqrt
    >>> construct_domain([sqrt(2)])
    (EX, [EX(sqrt(2))])
    >>> construct_domain([sqrt(2)], extension=True)  # doctest: +SKIP
    (QQ<sqrt(2)>, [ANP([1, 0], [1, 0, -2], QQ)])

    See also
    ========

    Domain
    Expr
    """
