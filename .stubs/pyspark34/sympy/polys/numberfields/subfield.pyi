from _typeshed import Incomplete
from sympy.core.add import Add as Add
from sympy.core.numbers import AlgebraicNumber as AlgebraicNumber
from sympy.core.singleton import S as S
from sympy.core.symbol import Dummy as Dummy
from sympy.core.sympify import sympify as sympify
from sympy.ntheory import sieve as sieve
from sympy.polys.densetools import dup_eval as dup_eval
from sympy.polys.domains import QQ as QQ
from sympy.polys.numberfields.minpoly import minimal_polynomial as minimal_polynomial
from sympy.polys.polyerrors import IsomorphismFailed as IsomorphismFailed
from sympy.polys.polytools import Poly as Poly, PurePoly as PurePoly, factor_list as factor_list
from sympy.utilities import public as public

def is_isomorphism_possible(a, b):
    """Necessary but not sufficient test for isomorphism. """
def field_isomorphism_pslq(a, b):
    """Construct field isomorphism using PSLQ algorithm. """
def field_isomorphism_factor(a, b):
    """Construct field isomorphism via factorization. """
def field_isomorphism(a, b, *, fast: bool = True):
    """
    Find an embedding of one number field into another.

    Explanation
    ===========

    This function looks for an isomorphism from $\\mathbb{Q}(a)$ onto some
    subfield of $\\mathbb{Q}(b)$. Thus, it solves the Subfield Problem.

    Examples
    ========

    >>> from sympy import sqrt, field_isomorphism, I
    >>> print(field_isomorphism(3, sqrt(2)))  # doctest: +SKIP
    [3]
    >>> print(field_isomorphism( I*sqrt(3), I*sqrt(3)/2))  # doctest: +SKIP
    [2, 0]

    Parameters
    ==========

    a : :py:class:`~.Expr`
        Any expression representing an algebraic number.
    b : :py:class:`~.Expr`
        Any expression representing an algebraic number.
    fast : boolean, optional (default=True)
        If ``True``, we first attempt a potentially faster way of computing the
        isomorphism, falling back on a slower method if this fails. If
        ``False``, we go directly to the slower method, which is guaranteed to
        return a result.

    Returns
    =======

    List of rational numbers, or None
        If $\\mathbb{Q}(a)$ is not isomorphic to some subfield of
        $\\mathbb{Q}(b)$, then return ``None``. Otherwise, return a list of
        rational numbers representing an element of $\\mathbb{Q}(b)$ to which
        $a$ may be mapped, in order to define a monomorphism, i.e. an
        isomorphism from $\\mathbb{Q}(a)$ to some subfield of $\\mathbb{Q}(b)$.
        The elements of the list are the coefficients of falling powers of $b$.

    """
def primitive_element(extension, x: Incomplete | None = None, *, ex: bool = False, polys: bool = False):
    """
    Find a single generator for a number field given by several generators.

    Explanation
    ===========

    The basic problem is this: Given several algebraic numbers
    $\\alpha_1, \\alpha_2, \\ldots, \\alpha_n$, find a single algebraic number
    $\\theta$ such that
    $\\mathbb{Q}(\\alpha_1, \\alpha_2, \\ldots, \\alpha_n) = \\mathbb{Q}(\\theta)$.

    This function actually guarantees that $\\theta$ will be a linear
    combination of the $\\alpha_i$, with non-negative integer coefficients.

    Furthermore, if desired, this function will tell you how to express each
    $\\alpha_i$ as a $\\mathbb{Q}$-linear combination of the powers of $\\theta$.

    Examples
    ========

    >>> from sympy import primitive_element, sqrt, S, minpoly, simplify
    >>> from sympy.abc import x
    >>> f, lincomb, reps = primitive_element([sqrt(2), sqrt(3)], x, ex=True)

    Then ``lincomb`` tells us the primitive element as a linear combination of
    the given generators ``sqrt(2)`` and ``sqrt(3)``.

    >>> print(lincomb)
    [1, 1]

    This means the primtiive element is $\\sqrt{2} + \\sqrt{3}$.
    Meanwhile ``f`` is the minimal polynomial for this primitive element.

    >>> print(f)
    x**4 - 10*x**2 + 1
    >>> print(minpoly(sqrt(2) + sqrt(3), x))
    x**4 - 10*x**2 + 1

    Finally, ``reps`` (which was returned only because we set keyword arg
    ``ex=True``) tells us how to recover each of the generators $\\sqrt{2}$ and
    $\\sqrt{3}$ as $\\mathbb{Q}$-linear combinations of the powers of the
    primitive element $\\sqrt{2} + \\sqrt{3}$.

    >>> print([S(r) for r in reps[0]])
    [1/2, 0, -9/2, 0]
    >>> theta = sqrt(2) + sqrt(3)
    >>> print(simplify(theta**3/2 - 9*theta/2))
    sqrt(2)
    >>> print([S(r) for r in reps[1]])
    [-1/2, 0, 11/2, 0]
    >>> print(simplify(-theta**3/2 + 11*theta/2))
    sqrt(3)

    Parameters
    ==========

    extension : list of :py:class:`~.Expr`
        Each expression must represent an algebraic number $\\alpha_i$.
    x : :py:class:`~.Symbol`, optional (default=None)
        The desired symbol to appear in the computed minimal polynomial for the
        primitive element $\\theta$. If ``None``, we use a dummy symbol.
    ex : boolean, optional (default=False)
        If and only if ``True``, compute the representation of each $\\alpha_i$
        as a $\\mathbb{Q}$-linear combination over the powers of $\\theta$.
    polys : boolean, optional (default=False)
        If ``True``, return the minimal polynomial as a :py:class:`~.Poly`.
        Otherwise return it as an :py:class:`~.Expr`.

    Returns
    =======

    Pair (f, coeffs) or triple (f, coeffs, reps), where:
        ``f`` is the minimal polynomial for the primitive element.
        ``coeffs`` gives the primitive element as a linear combination of the
        given generators.
        ``reps`` is present if and only if argument ``ex=True`` was passed,
        and is a list of lists of rational numbers. Each list gives the
        coefficients of falling powers of the primitive element, to recover
        one of the original, given generators.

    """
def to_number_field(extension, theta: Incomplete | None = None, *, gen: Incomplete | None = None, alias: Incomplete | None = None):
    """
    Express one algebraic number in the field generated by another.

    Explanation
    ===========

    Given two algebraic numbers $\\eta, \\theta$, this function either expresses
    $\\eta$ as an element of $\\mathbb{Q}(\\theta)$, or else raises an exception
    if $\\eta \\not\\in \\mathbb{Q}(\\theta)$.

    This function is essentially just a convenience, utilizing
    :py:func:`~.field_isomorphism` (our solution of the Subfield Problem) to
    solve this, the Field Membership Problem.

    As an additional convenience, this function allows you to pass a list of
    algebraic numbers $\\alpha_1, \\alpha_2, \\ldots, \\alpha_n$ instead of $\\eta$.
    It then computes $\\eta$ for you, as a solution of the Primitive Element
    Problem, using :py:func:`~.primitive_element` on the list of $\\alpha_i$.

    Examples
    ========

    >>> from sympy import sqrt, to_number_field
    >>> eta = sqrt(2)
    >>> theta = sqrt(2) + sqrt(3)
    >>> a = to_number_field(eta, theta)
    >>> print(type(a))
    <class 'sympy.core.numbers.AlgebraicNumber'>
    >>> a.root
    sqrt(2) + sqrt(3)
    >>> print(a)
    sqrt(2)
    >>> a.coeffs()
    [1/2, 0, -9/2, 0]

    We get an :py:class:`~.AlgebraicNumber`, whose ``.root`` is $\\theta$, whose
    value is $\\eta$, and whose ``.coeffs()`` show how to write $\\eta$ as a
    $\\mathbb{Q}$-linear combination in falling powers of $\\theta$.

    Parameters
    ==========

    extension : :py:class:`~.Expr` or list of :py:class:`~.Expr`
        Either the algebraic number that is to be expressed in the other field,
        or else a list of algebraic numbers, a primitive element for which is
        to be expressed in the other field.
    theta : :py:class:`~.Expr`, None, optional (default=None)
        If an :py:class:`~.Expr` representing an algebraic number, behavior is
        as described under **Explanation**. If ``None``, then this function
        reduces to a shorthand for calling :py:func:`~.primitive_element` on
        ``extension`` and turning the computed primitive element into an
        :py:class:`~.AlgebraicNumber`.
    gen : :py:class:`~.Symbol`, None, optional (default=None)
        If provided, this will be used as the generator symbol for the minimal
        polynomial in the returned :py:class:`~.AlgebraicNumber`.
    alias : str, :py:class:`~.Symbol`, None, optional (default=None)
        If provided, this will be used as the alias symbol for the returned
        :py:class:`~.AlgebraicNumber`.

    Returns
    =======

    AlgebraicNumber
        Belonging to $\\mathbb{Q}(\\theta)$ and equaling $\\eta$.

    Raises
    ======

    IsomorphismFailed
        If $\\eta \\not\\in \\mathbb{Q}(\\theta)$.

    See Also
    ========

    field_isomorphism
    primitive_element

    """
